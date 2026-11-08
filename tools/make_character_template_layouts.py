"""Draw the blank layout guides in characters/_template/layout/.

The guides copy the arrangement of the Intel, AMD, and Nvidia model sheets,
expression sheets, and reference cards. They hold neutral gray mannequins and
empty plaques, so an image model takes structure from them without picking up
another character's face, costume, or colors.

Usage: py tools/make_character_template_layouts.py   (needs Pillow 10.1+)
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "characters" / "_template" / "layout"

PAPER = (244, 241, 236)
INK = (58, 61, 68)  # neutral charcoal for frames and plaques
GOLD = (176, 152, 104)
PLAQUE_TEXT = (240, 236, 228)
FIG_FILL = (214, 209, 201)
FIG_LINE = (170, 163, 153)
SHADOW = (226, 222, 215)

SHEET = (1536, 1024)
CARD = (1024, 1536)
HEADS = 7.5  # target figure height in head-heights, from the Microsoft proportion pass


def font(size: int) -> ImageFont.FreeTypeFont:
    for name in ("georgiab.ttf", "timesbd.ttf", "DejaVuSerif-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size)


def frame(d: ImageDraw.ImageDraw, w: int, h: int) -> None:
    d.rectangle([12, 12, w - 13, h - 13], outline=INK, width=2)
    d.rectangle([20, 20, w - 21, h - 21], outline=GOLD, width=1)


def diamond(d: ImageDraw.ImageDraw, cx: int, cy: int, r: int, fill=GOLD) -> None:
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=fill)


def plaque(d: ImageDraw.ImageDraw, cx: int, cy: int, w: int, h: int, text: str = "", size: int = 16) -> None:
    box = [cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2]
    d.rounded_rectangle(box, radius=4, fill=INK, outline=GOLD, width=1)
    if text:
        d.text((cx, cy + 1), text, font=font(size), fill=PLAQUE_TEXT, anchor="mm")


def ruled_plaque(d: ImageDraw.ImageDraw, cx: int, cy: int, w: int, h: int, text: str = "", size: int = 16) -> None:
    """Label plaque with the short gold rules on either side, as on the model sheets."""
    d.line([cx - w // 2 - 50, cy, cx - w // 2 - 6, cy], fill=GOLD, width=1)
    d.line([cx + w // 2 + 6, cy, cx + w // 2 + 50, cy], fill=GOLD, width=1)
    plaque(d, cx, cy, w, h, text, size)


def nameplate(d: ImageDraw.ImageDraw, cx: int, top: int, w: int) -> int:
    """Empty two-line nameplate: a heavy bar for the name, a light bar for the title."""
    d.line([cx - w // 2, top, cx + w // 2, top], fill=GOLD, width=1)
    diamond(d, cx, top, 6)
    d.rounded_rectangle([cx - w // 2 + 10, top + 22, cx + w // 2 - 10, top + 72], radius=4, fill=(200, 196, 189))
    d.rounded_rectangle([cx - w // 2 + 10, top + 84, cx + w // 2 - 10, top + 104], radius=3, fill=(214, 210, 203))
    d.line([cx - w // 2, top + 124, cx + w // 2, top + 124], fill=GOLD, width=1)
    diamond(d, cx, top + 124, 6)
    return top + 124


def figure(d: ImageDraw.ImageDraw, cx: float, top: float, height: float, view: str) -> None:
    """Standing mannequin, HEADS head-heights tall, viewed front, three-quarter, side, or back."""
    u = height / HEADS
    sx = {"front": 1.0, "back": 1.0, "three-quarter": 0.82, "side": 0.5}[view]
    base = top + height
    d.ellipse([cx - 1.4 * u, base - 0.12 * u, cx + 1.4 * u, base + 0.12 * u], fill=SHADOW)

    def poly(pts):
        d.polygon([(cx + x * u * sx, top + y * u) for x, y in pts], fill=FIG_FILL, outline=FIG_LINE)

    # legs, from the hips at 3.9 heads to the feet
    if view == "side":
        poly([(-0.55, 3.9), (0.55, 3.9), (0.4, 7.3), (0.9, 7.5), (-0.4, 7.5), (-0.35, 3.9)])
    else:
        poly([(-0.78, 3.9), (-0.06, 3.9), (-0.22, 7.35), (-0.55, 7.5), (-0.62, 7.35)])
        poly([(0.06, 3.9), (0.78, 3.9), (0.62, 7.35), (0.55, 7.5), (0.22, 7.35)])
    # torso: shoulders, waist, hips
    poly([(-0.92, 1.35), (0.92, 1.35), (0.62, 2.85), (0.82, 3.95), (-0.82, 3.95), (-0.62, 2.85)])
    # arms hang to mid-thigh
    if view != "side":
        poly([(-0.92, 1.35), (-0.7, 1.45), (-0.82, 4.55), (-1.02, 4.55), (-1.08, 1.5)])
        poly([(0.92, 1.35), (0.7, 1.45), (0.82, 4.55), (1.02, 4.55), (1.08, 1.5)])
    else:
        poly([(-0.25, 1.4), (0.25, 1.4), (0.2, 4.5), (-0.15, 4.5)])
    # neck and head
    poly([(-0.16, 0.9), (0.16, 0.9), (0.18, 1.4), (-0.18, 1.4)])
    hw = 0.36 * (0.85 if view == "side" else 1.0)
    shift = {"front": 0, "back": 0, "three-quarter": 0.08, "side": 0.12}[view]
    d.ellipse([cx + (shift - hw) * u, top, cx + (shift + hw) * u, top + u], fill=FIG_FILL, outline=FIG_LINE)
    # a nose tick shows which way the figure faces; the back view has none
    if view in ("three-quarter", "side"):
        nx = cx + (shift + hw) * u
        d.line([nx - 2, top + 0.55 * u, nx + 0.06 * u, top + 0.6 * u], fill=FIG_LINE, width=2)


def bust(d: ImageDraw.ImageDraw, cx: float, cy: float, head: float) -> None:
    """Head-and-shoulders mannequin centered on the face."""
    u = head
    d.polygon(
        [(cx - 1.3 * u, cy + 1.45 * u), (cx - 0.95 * u, cy + 0.95 * u), (cx - 0.2 * u, cy + 0.75 * u),
         (cx + 0.2 * u, cy + 0.75 * u), (cx + 0.95 * u, cy + 0.95 * u), (cx + 1.3 * u, cy + 1.45 * u)],
        fill=FIG_FILL, outline=FIG_LINE,
    )
    d.rectangle([cx - 0.17 * u, cy + 0.3 * u, cx + 0.17 * u, cy + 0.85 * u], fill=FIG_FILL)
    d.ellipse([cx - 0.38 * u, cy - 0.5 * u, cx + 0.38 * u, cy + 0.5 * u], fill=FIG_FILL, outline=FIG_LINE)


def model_sheet() -> Image.Image:
    w, h = SHEET
    im = Image.new("RGB", SHEET, PAPER)
    d = ImageDraw.Draw(im)
    frame(d, w, h)
    nameplate(d, 150, 52, 200)
    centers = (365, 705, 1015, 1335)
    views = ("front", "three-quarter", "side", "back")
    labels = ("FRONT", "THREE-QUARTER", "SIDE", "BACK")
    for cx, view, label in zip(centers, views, labels):
        figure(d, cx, 34, 600, view)
        ruled_plaque(d, cx, 662, 190 if label == "THREE-QUARTER" else 120, 26, label, 15)
    d.line([40, 703, w - 40, 703], fill=GOLD, width=1)
    diamond(d, w // 2, 703, 6)
    for cx in (230, 610, 985):
        bust(d, cx, 800, 105)
        ruled_plaque(d, cx, 984, 170, 26)  # expression label; the prompt names the text
    for i in range(6):
        x = 1180 + i * 52
        d.rectangle([x, 828, x + 44, 876], fill=(196 - i * 22,) * 3, outline=FIG_LINE)
    return im


def expression_sheet() -> Image.Image:
    w, h = SHEET
    im = Image.new("RGB", SHEET, PAPER)
    d = ImageDraw.Draw(im)
    frame(d, w, h)
    nameplate(d, 255, 30, 260)
    figure(d, 250, 180, 800, "three-quarter")
    labels = (
        ("NEUTRAL", "SMILING", "EYES CLOSED"),
        ("ANGRY", "CRYING", "SURPRISED"),
        ("SMUG", "FLUSTERED", "SERIOUS"),
        ("BLUSHING", "EXCITED", "OMINOUS"),
    )
    xs = (470, 818, 1166)
    ys = (36, 282, 526, 766)
    cw, ch = 332, 218
    for r, row in enumerate(labels):
        for c, label in enumerate(row):
            x, y = xs[c], ys[r]
            d.rectangle([x, y, x + cw, y + ch], fill=(250, 248, 244), outline=GOLD, width=2)
            bust(d, x + cw // 2, y + 100, 80)
            plaque(d, x + cw // 2, y, 180 if len(label) < 10 else 196, 28, label, 16)
    return im


def reference_card() -> Image.Image:
    w, h = CARD
    im = Image.new("RGB", CARD, (52, 55, 62))
    d = ImageDraw.Draw(im)
    # soft vignette of the background scene
    for i in range(18):
        shade = 52 + i * 2
        d.rectangle([i * 14, i * 14, w - i * 14, h - i * 14], fill=(shade, shade + 2, shade + 7))
    d.rectangle([14, 14, w - 15, h - 15], outline=GOLD, width=3)
    d.rectangle([26, 26, w - 27, h - 27], outline=(120, 106, 80), width=1)
    diamond(d, w // 2, 20, 12)
    # large three-quarter mannequin from the hips up, cropped by the nameplate
    figure(d, w // 2 - 20, 120, 1990, "three-quarter")
    d.rectangle([27, 1340, w - 28, h - 28], fill=(52, 55, 62))  # crop at the hips
    # nameplate
    d.polygon(
        [(110, 1340), (w - 110, 1340), (w - 70, 1410), (w - 110, 1480), (110, 1480), (70, 1410)],
        fill=(44, 46, 52), outline=GOLD,
    )
    d.rounded_rectangle([300, 1362, w - 300, 1420], radius=4, fill=(150, 146, 140))
    d.line([180, 1448, 300, 1448], fill=GOLD, width=1)
    d.line([w - 300, 1448, w - 180, 1448], fill=GOLD, width=1)
    d.rounded_rectangle([320, 1438, w - 320, 1458], radius=3, fill=(120, 117, 112))
    for x in (70, w - 70):
        diamond(d, x, 1410, 10)
    diamond(d, w // 2, 1490, 10)
    return im


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, make in (
        ("model_sheet_layout.png", model_sheet),
        ("expressions_layout.png", expression_sheet),
        ("reference_card_layout.png", reference_card),
    ):
        make().save(OUT / name, optimize=True)
        print(OUT / name)


if __name__ == "__main__":
    main()
