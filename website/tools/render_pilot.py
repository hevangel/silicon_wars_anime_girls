"""Validate and assemble the pilot from independent panel PNGs and editable lettering."""
import argparse
from itertools import combinations
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "chapters/pilot-001/render.yaml"


def read_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def prompt_for(panel, style):
    return "\n\n".join((panel["direction"], style["visual_language"], panel["framing"]))


def point(position, size):
    if len(position) != 2 or not all(0 <= value <= 1 for value in position):
        raise ValueError(f"Invalid normalized point {position}")
    return tuple(round(value * limit) for value, limit in zip(position, size))


def load_source(plan):
    storyboard = read_yaml(ROOT / plan["storyboard"])
    layout = read_yaml(ROOT / storyboard["layout"])
    lettering = read_yaml(ROOT / plan["lettering"])
    style = read_yaml(ROOT / plan["global_prompt"])
    page = storyboard["page"]
    if plan["page"] != page or lettering["page"] != page or plan["chapter"] != storyboard["chapter"]:
        raise ValueError("Render plan, storyboard, and lettering must agree on page and pilot IDs")
    if any(doc["reading_direction"] != "rtl" for doc in (storyboard, layout, lettering)):
        raise ValueError("This pilot uses right-to-left reading order")

    boxes = {}
    for panel in layout["panels"]:
        panel_id = panel["id"]
        x, y, width, height = (panel[key] for key in ("x", "y", "width", "height"))
        if panel_id in boxes or not (
            0 <= x < x + width <= layout["page"]["width"]
            and 0 <= y < y + height <= layout["page"]["height"]
        ):
            raise ValueError(f"Invalid rectangle for {panel_id}")
        boxes[panel_id] = (x, y, x + width, y + height)
    for first, second in combinations(boxes.values(), 2):
        if max(first[0], second[0]) < min(first[2], second[2]) and max(first[1], second[1]) < min(first[3], second[3]):
            raise ValueError("Panel rectangles overlap")
    ordered = sorted(boxes, key=lambda key: (boxes[key][1], -boxes[key][0]))
    if len(storyboard["panels"]) != len(ordered) or [panel["id"] for panel in storyboard["panels"]] != ordered:
        raise ValueError("The storyboard must list all layout panels in right-to-left order")

    cast = {name: read_yaml(ROOT / path) for name, path in style["continuity"].items()}
    by_panel = {panel_id: [] for panel_id in ordered}
    seen = set()
    for item in lettering["items"]:
        if item["id"] in seen or item["kind"] not in {"speech", "sfx", "screen"}:
            raise ValueError(f"Invalid lettering item {item['id']}")
        seen.add(item["id"])
        point(item["at"], (1, 1))
        if item["kind"] == "speech":
            point(item["tail"], (1, 1))
        by_panel[item["panel"]].append(item)

    panels = {}
    for entry in storyboard["panels"]:
        panel_id = entry["id"]
        panel = read_yaml(ROOT / entry["brief"])
        if panel["id"] != panel_id or panel["dialogue_ids"] != [item["id"] for item in by_panel[panel_id]]:
            raise ValueError(f"{panel_id}: panel or lettering IDs do not match")
        if any(item["kind"] == "speech" and item["speaker"] not in panel["characters"] for item in by_panel[panel_id]):
            raise ValueError(f"{panel_id}: speaking character is absent")
        asset_key = {"default_manga": "model_sheet", "chibi": "chibi_sheet"}.get(panel.get("style_variant", "default_manga"))
        if asset_key is None:
            raise ValueError(f"{panel_id}: unknown style_variant {panel.get('style_variant')!r}")
        references = [cast[name]["reference_assets"][asset_key] for name in panel["characters"]]
        if panel["references"] != references or any(not (ROOT / path).is_file() for path in references):
            raise ValueError(f"{panel_id}: references must match the cast in order")
        point(panel["crop_center"], (1, 1))
        panels[panel_id] = panel
    return layout["page"], boxes, panels, by_panel, style


def wrapped(text, draw, font, limit):
    lines = [""]
    for word in text.split():
        trial = f"{lines[-1]} {word}".strip()
        if lines[-1] and draw.textlength(trial, font=font) > limit:
            lines.append(word)
        else:
            lines[-1] = trial
    return "\n".join(lines)


def letter(panel, item, speech_font, label_font):
    draw = ImageDraw.Draw(panel)
    x, y = point(item["at"], panel.size)
    if item["kind"] == "sfx":
        draw.text((x, y), item["text"], font=label_font, anchor="mm",
                  fill="#fff4e3", stroke_fill="#201416", stroke_width=5)
        return
    if item["kind"] == "screen":
        half_width = round(draw.textlength(item["text"], font=label_font) / 2 + 23)
        draw.rounded_rectangle((x - half_width, y - 27, x + half_width, y + 27),
                               radius=6, fill="#0d1920", outline="#79a4a9", width=2)
        draw.text((x, y), item["text"], font=label_font, anchor="mm", fill="#d1f1ee")
        return

    text = wrapped(item["text"], draw, speech_font, panel.width * 0.40)
    bounds = draw.multiline_textbbox((0, 0), text, font=speech_font, spacing=5)
    width, height = bounds[2] - bounds[0] + 54, bounds[3] - bounds[1] + 35
    left = min(max(x - width // 2, 9), panel.width - width - 9)
    top = min(max(y - height // 2, 9), panel.height - height - 9)
    bottom = top + height
    tail = point(item["tail"], panel.size)
    base = min(max(tail[0], left + 34), left + width - 34)
    draw.polygon(((base - 13, bottom - 11), tail, (base + 13, bottom - 11)),
                 fill="white", outline="#171820", width=3)
    draw.rounded_rectangle((left, top, left + width, bottom), radius=height // 3,
                           fill="white", outline="#171820", width=3)
    # Join the tail to the balloon without an outline across its base.
    if tail[1] > bottom:
        factor = (bottom - (bottom - 11)) / (tail[1] - (bottom - 11))
        join = round(base + (tail[0] - base) * factor)
        spread = max(2, round(13 * (1 - factor)) - 2)
        draw.line((join - spread, bottom - 1, join + spread, bottom - 1), fill="white", width=4)
    draw.multiline_text((left + width / 2, top + height / 2), text, font=speech_font,
                        spacing=5, align="center", anchor="mm", fill="#171820")


def assemble(plan, source, output=None):
    size, boxes, panels, lettering, _ = source
    page = Image.new("RGB", (size["width"], size["height"]), "#fcfaf5")
    speech_font = ImageFont.load_default(size=38)
    label_font = ImageFont.load_default(size=33)
    for panel_id, (left, top, right, bottom) in boxes.items():
        brief = panels[panel_id]
        with Image.open(ROOT / brief["art"]) as raw:
            if raw.format != "PNG":
                raise ValueError(f"{panel_id}: expected a PNG panel")
            panel = ImageOps.fit(raw.convert("RGB"), (right - left, bottom - top),
                                 method=Image.Resampling.LANCZOS, centering=tuple(brief["crop_center"]))
        for item in lettering[panel_id]:
            letter(panel, item, speech_font, label_font)
        ImageDraw.Draw(panel).rectangle((0, 0, panel.width - 1, panel.height - 1),
                                        outline="#16171e", width=5)
        page.paste(panel, (left, top))
    target = output or ROOT / plan["output"]
    target.parent.mkdir(parents=True, exist_ok=True)
    page.save(target, format="PNG")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--prompt", metavar="PANEL", help="Print the exact art prompt for one panel")
    mode.add_argument("--check", action="store_true", help="Validate source and references only")
    parser.add_argument("--output", type=Path, help="Write the assembled PNG to a different path")
    parser.add_argument("--plan", type=Path, default=PLAN, help="Render plan YAML (defaults to the page-001 plan)")
    args = parser.parse_args()
    try:
        plan = read_yaml(args.plan if args.plan.is_absolute() else ROOT / args.plan)
        source = load_source(plan)
        if args.prompt:
            print(prompt_for(source[2][args.prompt], source[4]))
        elif args.check:
            print(f"Pilot source validated: {len(source[2])} panel(s), reference order, layout, and lettering.")
        else:
            print(assemble(plan, source, args.output))
    except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
