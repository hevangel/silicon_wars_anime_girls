#!/usr/bin/env python3
"""Build the TSMC Seeing Course data + art from the seeing study.

Reads  $TSMC_SEEING_DIR/manifest.json   (lessons/cards parsed from the syllabus)
       $TSMC_SEEING_DIR/SYLLABUS-source.md (Lesson 15 prose)
       $TSMC_SEEING_DIR/images/<slug>/<slug>-<i>.webp  (generated card images)
       $TSMC_SEEING_DIR/control/control.webp          (the approved control)
Writes website/artwork/tsmc-seeing/seeing.json and art/ (web-sized copies:
full <=1200px wide, thumbs <=480px wide).
Validates: 15 lessons, 120 cards, 188 images, 20 page-drawn overlays.
"""
import json, os, re, shutil, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.dirname(HERE)
SRC = os.environ.get("TSMC_SEEING_DIR", os.path.expanduser("~/workspace/tsmc_seeing_study"))

# slug -> overlay renderer type in app.js (overlays are drawn by the page,
# never baked into the images)
OVERLAYS = {
    "implied-line": "gaze",
    "big-medium-small": "bms",
    "grayscale": "graystrip",
    "light-side-and-shadow-side": "families",
    "highlight": "highlights",
    "halftone-and-terminator": "terminator",
    "core-shadow": "coreshadow",
    "dominant-secondary-accent": "bar603010",
    "horizon-line-and-vanishing-point": "vp1",
    "one-point-perspective": "vp1",
    "two-point-perspective": "vp2",
    "proportion-in-heads": "heads",
    "body-landmarks": "landmarks",
    "gesture-and-line-of-action": "action",
    "weight-and-balance": "plumb",
    "tilt-and-twist": "tilt",
    "worms-eye-view": "vp3",
    "rule-of-thirds": "thirds",
    "triangle": "triangle",
    "eye-path": "eyepath",
}


def variant_items(claude_raw, n):
    """Split a variant card's Muse line into its (1)...(n) item texts."""
    body = re.sub(r"^(\d+ variants|Study)\b[.,]?\s*", "", claude_raw)
    body = re.sub(r"\s*Overlay: .*$", "", body).strip()
    if n == 1:
        return [body]
    parts = re.split(r"\((\d)\)\s*", body)
    items = {}
    for i in range(1, len(parts), 2):
        items[int(parts[i])] = parts[i + 1].strip().rstrip(".")
    return [items[k] for k in range(1, n + 1)]


def label_for(item, lead):
    text = item.strip()
    if lead and text.lower().startswith(lead.lower()[:18]):
        text = text[len(lead):].strip(" ,.")
    # variant lists in the syllabus are comma-separated and sometimes followed
    # by an extra instruction sentence; a caption wants only the item itself
    text = text.split(". ")[0].rstrip(",.;: ")
    text = text[:1].upper() + text[1:]
    return text if len(text) <= 64 else text[:61].rstrip() + "…"


def web_copy(src_path, dst_full, dst_thumb):
    im = Image.open(src_path).convert("RGB")
    for dst, maxw in ((dst_full, 1200), (dst_thumb, 480)):
        out = im
        if im.width > maxw:
            out = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        out.save(dst, "WEBP", quality=82)


def inline_md(text):
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)


def lesson15_html():
    """Convert Lesson 15 of the syllabus to HTML. The email paste wraps
    paragraphs across lines and puts list markers ('-', '1.') on their own
    lines, so this is a small line-based state machine."""
    lines = open(os.path.join(SRC, "SYLLABUS-source.md")).read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("**Lesson 15:"))
    out, mode, buf, rows, skipped = [], None, [], [], 0

    def flush():
        nonlocal mode, buf, rows
        if mode == "para" and buf:
            out.append(f"<p>{inline_md(' '.join(buf))}</p>")
        elif mode in ("ul", "ol") and buf:
            items = "".join(f"<li>{inline_md(t)}</li>" for t in buf)
            out.append(f"<{mode}>{items}</{mode}>")
        elif mode == "table" and rows:
            head, rest = rows[0], rows[1:]
            th = "".join(f"<th>{inline_md(c)}</th>" for c in head)
            trs = "".join("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in r) + "</tr>"
                          for r in rest)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
        mode, buf, rows = None, [], []

    item_open = False  # a list marker was seen; following lines are its text
    for raw in lines[start + 1:]:
        l = raw.strip()
        if not l:
            if not item_open:
                flush()
            continue
        if re.fullmatch(r"\*\*.+\*\*", l):
            flush(); item_open = False
            out.append(f"<h3>{inline_md(l[2:-2])}</h3>")
            continue
        if l.startswith("|"):
            if mode != "table":
                flush(); mode = "table"
            rows.append([c.strip() for c in l.strip("|").split("|")])
            item_open = False
            continue
        if l == "-" or re.fullmatch(r"\d+\.", l):
            want = "ul" if l == "-" else "ol"
            if mode != want:
                flush(); mode = want; buf = [""]
            else:
                buf.append("")
            item_open = True
            continue
        # plain text line: continuation of the current construct
        if mode in ("ul", "ol") and buf:
            buf[-1] = (buf[-1] + " " + l).strip()
        elif mode == "table":
            flush(); mode = "para"; buf = [l]
        elif mode == "para":
            buf.append(l)
        else:
            mode = "para"; buf = [l]
        item_open = False
    flush()
    # drop the thesis / intro / try-this paragraphs (already lesson fields)
    kept, dropped = [], 0
    for b in out:
        if dropped < 3 and b.startswith("<p>"):
            dropped += 1
            continue
        kept.append(b)
    return "\n".join(kept)


def main():
    manifest = json.load(open(os.path.join(SRC, "manifest.json")))
    art = os.path.join(PAGE, "art")
    if os.path.exists(art):
        shutil.rmtree(art)
    os.makedirs(art)

    web_copy(os.path.join(SRC, "control", "control.webp"),
             os.path.join(art, "control.webp"), os.path.join(art, "control-t.webp"))

    lessons, n_cards, n_images, n_overlays = [], 0, 0, 0
    for les in manifest:
        out_les = {"n": les["n"], "id": les["id"], "title": les["title"],
                   "thesis": les["thesis"], "intro": les["intro"],
                   "exercise": les["exercise"], "cards": []}
        for cd in les["cards"]:
            n = cd["images"]
            items = variant_items(cd["claude_raw"], n)
            lead = re.sub(r"\s*\(1\).*$", "", re.sub(
                r"^(\d+ variants|Study)\b[.,]?\s*", "", cd["claude_raw"])).strip()
            slug_dir = os.path.join(art, cd["slug"])
            os.makedirs(slug_dir)
            images = []
            for i in range(1, n + 1):
                src = os.path.join(SRC, "images", cd["slug"], f"{cd['slug']}-{i}.webp")
                assert os.path.exists(src), f"missing image {src}"
                web_copy(src, os.path.join(slug_dir, f"{i}.webp"),
                         os.path.join(slug_dir, f"t{i}.webp"))
                label = "Study" if n == 1 else f"Variant {i} — {label_for(items[i - 1], lead)}"
                images.append({"src": f"art/{cd['slug']}/{i}.webp",
                               "thumb": f"art/{cd['slug']}/t{i}.webp", "label": label})
            overlay = OVERLAYS.get(cd["slug"])
            if cd.get("overlay"):
                assert overlay, f"card {cd['slug']} has overlay text but no renderer"
                n_overlays += 1
            out_les["cards"].append({
                "slug": cd["slug"], "name": cd["name"], "subtitle": cd["subtitle"],
                "explanation": cd["explanation"], "look": cd["look"],
                "images": images, "overlay": overlay})
            n_cards += 1
            n_images += n
        if les["n"] == 15:
            out_les["prose"] = lesson15_html()
        lessons.append(out_les)

    assert len(lessons) == 15, len(lessons)
    assert n_cards == 120, n_cards
    assert n_images == 188, n_images
    assert n_overlays == 20, n_overlays
    data = {"title": "The TSMC Seeing Course",
            "control": {"src": "art/control.webp", "thumb": "art/control-t.webp"},
            "lessons": lessons}
    with open(os.path.join(PAGE, "seeing.json"), "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"OK: 15 lessons, {n_cards} cards, {n_images} images, {n_overlays} overlays")


if __name__ == "__main__":
    main()
