#!/usr/bin/env python3
"""Build the two human-facing views of the style study.

  art/style-study/index.html          — the whole atlas, pending plates shown as slots
  art/style-study/sheets/<family>.png — per-family contact sheets of finished plates

Run after any batch of renders:  python tools/style_study/build_atlas.py
"""

from __future__ import annotations

import html
import json
import pathlib
from collections import OrderedDict

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "art" / "style-study"
MANIFEST = OUT / "plates.json"

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\segoeui.ttf",
]
BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\georgiab.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for path in (BOLD_CANDIDATES if bold else FONT_CANDIDATES):
        if pathlib.Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def grouped(plates):
    """OrderedDict: family -> style -> [plates] preserving manifest order."""
    out: "OrderedDict[str, OrderedDict[str, list]]" = OrderedDict()
    for p in plates:
        out.setdefault(p["family"], OrderedDict()).setdefault(p["style"], []).append(p)
    return out


# --------------------------------------------------------------------------
# Contact sheets
# --------------------------------------------------------------------------
def make_sheets(plates) -> list[pathlib.Path]:
    sheets_dir = OUT / "sheets"
    sheets_dir.mkdir(exist_ok=True)
    written = []

    fam_title = font(44, bold=True)
    label_font = font(19, bold=True)
    sub_font = font(16)

    for family, styles in grouped(plates).items():
        usable = [(slug, ps) for slug, ps in styles.items()
                  if all(p["status"] == "rendered" for p in ps)]
        if not usable:
            continue

        cols = 4
        cell_w, cell_h, gap = 470, 705, 26
        pad, head = 46, 150
        rows = len(usable)
        width = pad * 2 + cols * cell_w + (cols - 1) * gap
        height = head + rows * (cell_h + gap) + pad

        sheet = Image.new("RGB", (width, height), (244, 241, 234))
        draw = ImageDraw.Draw(sheet)
        draw.text((pad, 40), family, font=fam_title, fill=(28, 27, 25))
        sub = (f"Arm · the Pocket Architect · {len(usable)} of "
               f"{len(styles)} styles finished · {len(usable) * 4} plates")
        draw.text((pad, 96), sub, font=sub_font, fill=(110, 104, 94))
        draw.line((pad, head - 24, width - pad, head - 24), fill=(196, 188, 174), width=2)

        for r, (slug, ps) in enumerate(usable):
            top = head + r * (cell_h + gap)
            for c, p in enumerate(ps):
                left = pad + c * (cell_w + gap)
                with Image.open(ROOT / p["file"]) as im:
                    im = im.convert("RGB")
                    im.thumbnail((cell_w, 640))
                    x = left + (cell_w - im.width) // 2
                    sheet.paste(im, (x, top))
                draw.text((left, top + 652), p["style_label"], font=label_font,
                          fill=(28, 27, 25))
                draw.text((left, top + 678), f"v{p['variant']} · {p['variant_axis']}",
                          font=sub_font, fill=(110, 104, 94))

        path = sheets_dir / f"{slug_family(family)}.png"
        sheet.save(path, optimize=True)
        written.append(path)
        print(f"sheet {path.relative_to(ROOT)}  {sheet.size[0]}x{sheet.size[1]}")
    return written


def slug_family(family: str) -> str:
    keep = [c.lower() if c.isalnum() else "-" for c in family]
    s = "".join(keep)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")


# --------------------------------------------------------------------------
# Atlas page
# --------------------------------------------------------------------------
CSS = """
:root{--paper:#f4f1ea;--ink:#1c1b19;--muted:#6e685e;--rule:#c9c1b3;--teal:#1f6b78}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font:16px/1.55 Georgia,"Times New Roman",serif}
.wrap{max-width:1180px;margin:0 auto;padding:64px 40px 120px}
header{border-bottom:2px solid var(--ink);padding-bottom:22px;margin-bottom:8px}
h1{font-size:44px;line-height:1.1;margin:0 0 10px;letter-spacing:-.01em}
.kicker{font:600 12px/1.4 system-ui,sans-serif;letter-spacing:.18em;
 text-transform:uppercase;color:var(--teal);margin:0 0 14px}
.lede{max-width:64ch;color:#3a3733;margin:14px 0 0}
.meta{font:13px/1.6 system-ui,sans-serif;color:var(--muted);margin-top:18px}
.progress{height:4px;background:#ded7c8;margin:26px 0 0}
.progress span{display:block;height:4px;background:var(--teal)}
h2{font-size:13px;font-family:system-ui,sans-serif;text-transform:uppercase;
 letter-spacing:.16em;margin:64px 0 6px;padding-bottom:8px;
 border-bottom:1px solid var(--rule);color:var(--teal)}
.style{margin:34px 0 0}
.style h3{font-size:22px;margin:0 0 2px;font-weight:600}
.style .medium{color:var(--muted);font-size:14px;margin:0 0 14px;max-width:86ch}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.grid.solo{grid-template-columns:repeat(3,1fr)}
figure{margin:0}
figure img{width:100%;display:block;border:1px solid #d8d1c2;background:#fff}
.slot{aspect-ratio:2/3;border:1px dashed #c3bbab;display:flex;align-items:center;
 justify-content:center;text-align:center;padding:12px;color:#9b9384;
 font:12px/1.5 system-ui,sans-serif}
figcaption{font:12px/1.5 system-ui,sans-serif;color:var(--muted);margin-top:7px}
figcaption b{color:var(--ink);font-weight:600}
footer{margin-top:80px;border-top:1px solid var(--rule);padding-top:18px;
 font:12px/1.7 system-ui,sans-serif;color:var(--muted)}
"""


def make_atlas(data) -> pathlib.Path:
    plates = data["plates"]
    done = sum(1 for p in plates if p["status"] == "rendered")
    total = len(plates)
    parts = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width,initial-scale=1'>",
        "<title>Arm · cross-era art-style study</title>",
        f"<style>{CSS}</style></head><body><div class='wrap'>",
        "<header>",
        "<p class='kicker'>Silicon Wars · art direction study</p>",
        "<h1>Arm in every style</h1>",
        "<p class='lede'>One character, one pose, 105 styles. Each plate redraws Arm, "
        "the Pocket Architect, walking away with her folded umbrella — the pose of the "
        "supplied reference — so that only the medium changes. Styles whose subject is a "
        "visual language rather than a material are allowed to rebuild the composition "
        "around the same girl, street and season.</p>",
        f"<p class='meta'>{data['style_count']} styles · {total} plates · "
        f"{done} rendered · character sheet used as the identity reference for every "
        f"plate · prompts and hashes recorded beside each render.</p>",
        f"<div class='progress'><span style='width:{done / total * 100:.1f}%'></span></div>",
        "</header>",
    ]

    for family, styles in grouped(plates).items():
        parts.append(f"<h2>{html.escape(family)}</h2>")
        for slug, ps in styles.items():
            solo = len(ps) == 1
            parts.append("<section class='style'>")
            parts.append(f"<h3>{html.escape(ps[0]['style_label'])}</h3>")
            parts.append(f"<p class='medium'>{html.escape(ps[0]['medium'])}</p>")
            parts.append("<div class='grid solo'>" if solo else "<div class='grid'>")
            for p in ps:
                if p["status"] == "rendered":
                    src = p["file"].replace("art/style-study/", "")
                    cap = (f"<figcaption><b>v{p['variant']}</b> · "
                           f"{html.escape(p['variant_axis'])}</figcaption>")
                    img = (f"<img src='{src}' alt='{html.escape(p['style_label'])} "
                           f"version {p['variant']}' loading='lazy'>")
                else:
                    img = (f"<div class='slot'>v{p['variant']}<br>"
                           f"{html.escape(p['variant_axis'])}</div>")
                    cap = "<figcaption><b>v{}</b> · pending</figcaption>".format(p["variant"])
                parts.append(f"<figure>{img}{cap}</figure>")
            parts.append("</div></section>")

    parts.append(
        "<footer>Pose: reference supplied 2026-11-24, archived at "
        "scratchpad/originals/pose-reference.png. Identity: "
        "characters/arm/character_sheet.png and characters/arm/continuity.yaml. "
        "Machine-readable record: plates.json. Generated with the Seedream image model; "
        "each render's prompt, reference hash and image hash sit beside the file.</footer>")
    parts.append("</div></body></html>")

    path = OUT / "index.html"
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"atlas {path.relative_to(ROOT)}  {done}/{total} rendered")
    return path


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    make_sheets(data["plates"])
    make_atlas(data)


if __name__ == "__main__":
    main()
