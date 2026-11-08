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
EXPR_PLAQUE_W = 200  # locked expression label plaque width (cell is 332 wide)
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
    """Title lockup shared by the model, chibi and expression sheets: logo box beside
    the name bar, a title bar, then the printed sub-title. Mirrors sheet_title_lockup.svg."""
    x0, x1 = cx - w // 2, cx + w // 2
    d.line([x0, top, x1, top], fill=GOLD, width=1)
    diamond(d, cx, top, 6)
    d.rounded_rectangle([x0 + 10, top + 20, x0 + 62, top + 72], radius=6, fill=(200, 196, 189), outline=GOLD)
    d.rounded_rectangle([x0 + 74, top + 24, x1 - 10, top + 68], radius=4, fill=(200, 196, 189))
    d.rounded_rectangle([x0 + 10, top + 82, x1 - 10, top + 102], radius=3, fill=(214, 210, 203))
    # sub-title sits inside the bottom rule, which ends in a diamond at each end
    by = top + 118
    f = font(13)
    tw = d.textlength("SILICON WARS", font=f) + 12
    d.line([x0 + 6, by, cx - tw / 2, by], fill=GOLD, width=1)
    d.line([cx + tw / 2, by, x1 - 6, by], fill=GOLD, width=1)
    d.text((cx, by), "SILICON WARS", font=f, fill=(140, 124, 90), anchor="mm")
    diamond(d, x0, by, 6)
    diamond(d, x1, by, 6)
    return by


def title_lockup_svg() -> str:
    g, bar, bar2 = "#b09868", "#c8c4bd", "#d6d2cb"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="312" height="140" viewBox="-6 0 312 140">
  <title>Silicon Wars sheet title lockup (locked): logo, name, title, sub-title</title>
  <line x1="0" y1="10" x2="300" y2="10" stroke="{g}"/>
  <path d="M150 4L156 10L150 16L144 10Z" fill="{g}"/>
  <rect id="logo" x="10" y="30" width="52" height="52" rx="6" fill="{bar}" stroke="{g}"/>
  <rect id="name" x="74" y="34" width="216" height="44" rx="4" fill="{bar}"/>
  <rect id="title" x="10" y="92" width="280" height="20" rx="3" fill="{bar2}"/>
  <!-- bottom rule: sub-title embedded in the line, a diamond at each end -->
  <line x1="6" y1="128" x2="82" y2="128" stroke="{g}"/>
  <line x1="218" y1="128" x2="294" y2="128" stroke="{g}"/>
  <text id="subtitle" x="150" y="132.5" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="13" letter-spacing="3" fill="#8c7c5a">SILICON WARS</text>
  <path d="M0 128L6 122L12 128L6 134Z" fill="{g}" transform="translate(-6 0)"/>
  <path d="M288 128L294 122L300 128L294 134Z" fill="{g}" transform="translate(6 0)"/>
</svg>
"""


def title_lockup_wordmark_svg() -> str:
    """Variant for logos that already spell the company name: wide logo, no name bar."""
    g, bar, bar2 = "#b09868", "#c8c4bd", "#d6d2cb"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="312" height="140" viewBox="-6 0 312 140">
  <title>Silicon Wars sheet title lockup, wordmark form (locked): logo, title, sub-title</title>
  <line x1="0" y1="10" x2="300" y2="10" stroke="{g}"/>
  <path d="M150 4L156 10L150 16L144 10Z" fill="{g}"/>
  <rect id="logo-wordmark" x="10" y="30" width="200" height="52" rx="6" fill="{bar}" stroke="{g}"/>
  <rect id="title" x="10" y="92" width="280" height="20" rx="3" fill="{bar2}"/>
  <!-- bottom rule: sub-title embedded in the line, a diamond at each end -->
  <line x1="6" y1="128" x2="82" y2="128" stroke="{g}"/>
  <line x1="218" y1="128" x2="294" y2="128" stroke="{g}"/>
  <text id="subtitle" x="150" y="132.5" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="13" letter-spacing="3" fill="#8c7c5a">SILICON WARS</text>
  <path d="M0 128L6 122L12 128L6 134Z" fill="{g}" transform="translate(-6 0)"/>
  <path d="M288 128L294 122L300 128L294 134Z" fill="{g}" transform="translate(6 0)"/>
</svg>
"""


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
    nameplate(d, 160, 40, 220)
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
    figure(d, 250, 215, 770, "three-quarter")
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
            plaque(d, x + cw // 2, y, EXPR_PLAQUE_W, 28, label, 16)  # one width for all 12
    return im


def chibi_figure(d: ImageDraw.ImageDraw, cx: float, top: float, height: float, view: str) -> None:
    """Chibi mannequin: big head, short body, about 2.5 head-heights tall."""
    u = height / 2.5
    sx = {"front": 1.0, "back": 1.0, "three-quarter": 0.85, "side": 0.6}[view]
    base = top + height
    d.ellipse([cx - 0.9 * u, base - 0.07 * u, cx + 0.9 * u, base + 0.07 * u], fill=SHADOW)

    def poly(pts):
        d.polygon([(cx + x * u * sx, top + y * u) for x, y in pts], fill=FIG_FILL, outline=FIG_LINE)

    poly([(-0.3, 1.9), (-0.04, 1.9), (-0.06, 2.5), (-0.34, 2.5)])
    poly([(0.04, 1.9), (0.3, 1.9), (0.34, 2.5), (0.06, 2.5)])
    poly([(-0.36, 1.2), (0.36, 1.2), (0.32, 1.95), (-0.32, 1.95)])
    poly([(-0.36, 1.25), (-0.28, 1.25), (-0.4, 1.8), (-0.5, 1.8)])
    poly([(0.28, 1.25), (0.36, 1.25), (0.5, 1.8), (0.4, 1.8)])
    d.ellipse([cx - 0.62 * u * sx, top, cx + 0.62 * u * sx, top + 1.3 * u], fill=FIG_FILL, outline=FIG_LINE)
    if view in ("three-quarter", "side"):
        nx = cx + 0.62 * u * sx
        d.line([nx - 2, top + 0.7 * u, nx + 0.05 * u, top + 0.75 * u], fill=FIG_LINE, width=2)


def chibi_sheet() -> Image.Image:
    """Model-sheet chrome plus the locked CHIBI tag at the top right."""
    w, h = SHEET
    im = Image.new("RGB", SHEET, PAPER)
    d = ImageDraw.Draw(im)
    frame(d, w, h)
    nameplate(d, 180, 40, 260)
    plaque(d, w - 110, 56, 120, 28, "CHIBI", 15)
    centers = (365, 705, 1015, 1335)
    views = ("front", "three-quarter", "side", "back")
    labels = ("FRONT", "THREE-QUARTER", "SIDE", "BACK")
    for cx, view, label in zip(centers, views, labels):
        chibi_figure(d, cx, 215, 450, view)
        ruled_plaque(d, cx, 690, 190 if label == "THREE-QUARTER" else 120, 26, label, 15)
    d.line([40, 730, w - 40, 730], fill=GOLD, width=1)
    diamond(d, w // 2, 730, 6)
    for cx in (230, 610, 985):
        bust(d, cx, 835, 100)
        ruled_plaque(d, cx, 990, 170, 26)
    for i in range(6):
        x = 1180 + i * 52
        d.rectangle([x, 850, x + 44, 898], fill=(196 - i * 22,) * 3, outline=FIG_LINE)
    return im


def reference_card() -> Image.Image:
    """Locked card chrome: gold outer frame + inner hairline, top diamond, hex-ended
    charcoal nameplate (name bar, title bar, gold rules, three diamonds). The same
    geometry is written to reference_card_chrome.svg; keep the two in step."""
    w, h = CARD
    im = Image.new("RGB", CARD, (52, 55, 62))
    d = ImageDraw.Draw(im)
    # soft vignette of the background scene
    for i in range(18):
        shade = 52 + i * 2
        d.rectangle([i * 14, i * 14, w - i * 14, h - i * 14], fill=(shade, shade + 2, shade + 7))
    # large three-quarter mannequin from the hips up, cropped by the nameplate
    figure(d, w // 2 - 20, 120, 1990, "three-quarter")
    d.rectangle([0, 1340, w, h], fill=(52, 55, 62))  # crop at the hips; also clears legs past the frame
    # frame goes on after the figure so nothing crosses it
    d.rectangle([14, 14, w - 15, h - 15], outline=GOLD, width=3)
    d.rectangle([26, 26, w - 27, h - 27], outline=(120, 106, 80), width=1)
    diamond(d, w // 2, 20, 12)
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


def reference_card_svg() -> str:
    """Chrome-only card (no mannequin): the single source of truth for border and nameplate."""
    w, h = CARD
    g, g2, plate = "#b09868", "#786a50", "#2c2e34"
    dia = lambda x, y, r: f'<path d="M{x} {y - r}L{x + r} {y}L{x} {y + r}L{x - r} {y}Z" fill="{g}"/>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <title>Silicon Wars reference card chrome (locked)</title>
  <!-- portrait window: leave transparent / fill with the scene -->
  <rect x="0" y="0" width="{w}" height="{h}" fill="#34373e"/>
  <rect x="14" y="14" width="{w - 29}" height="{h - 29}" fill="none" stroke="{g}" stroke-width="3"/>
  <rect x="26" y="26" width="{w - 53}" height="{h - 53}" fill="none" stroke="{g2}" stroke-width="1"/>
  {dia(w // 2, 20, 12)}
  <!-- nameplate: hex-ended charcoal plate, gold hairline -->
  <polygon points="110,1340 {w - 110},1340 {w - 70},1410 {w - 110},1480 110,1480 70,1410" fill="{plate}" stroke="{g}" stroke-width="1"/>
  <rect id="name-bar" x="300" y="1362" width="{w - 600}" height="58" rx="4" fill="#96928c"/>
  <line x1="180" y1="1448" x2="300" y2="1448" stroke="{g}"/>
  <line x1="{w - 300}" y1="1448" x2="{w - 180}" y2="1448" stroke="{g}"/>
  <rect id="title-bar" x="320" y="1438" width="{w - 640}" height="20" rx="3" fill="#787570"/>
  {dia(70, 1410, 10)}{dia(w - 70, 1410, 10)}{dia(w // 2, 1490, 10)}
</svg>
"""


def expression_cell_svg() -> str:
    """One expression cell with its locked label box (see EXPRESSION LABEL BOX in expressions.prompt.md)."""
    g = "#b09868"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="352" height="238" viewBox="-10 -14 352 238">
  <title>Silicon Wars expression cell and label box (locked)</title>
  <rect id="cell" x="0" y="0" width="332" height="218" fill="#faf8f4" stroke="{g}" stroke-width="2"/>
  <rect id="label-box" x="66" y="-14" width="{EXPR_PLAQUE_W}" height="28" rx="4" fill="#3a3d44" stroke="{g}"/>
  <text x="166" y="5" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="16" font-weight="bold" fill="#f0ece4">SMILING</text>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "reference_card_chrome.svg").write_text(reference_card_svg(), encoding="utf-8")
    print(OUT / "reference_card_chrome.svg")
    (OUT / "sheet_title_lockup.svg").write_text(title_lockup_svg(), encoding="utf-8")
    print(OUT / "sheet_title_lockup.svg")
    (OUT / "sheet_title_lockup_wordmark.svg").write_text(title_lockup_wordmark_svg(), encoding="utf-8")
    print(OUT / "sheet_title_lockup_wordmark.svg")
    (OUT / "expression_cell.svg").write_text(expression_cell_svg(), encoding="utf-8")
    print(OUT / "expression_cell.svg")
    for name, make in (
        ("model_sheet_layout.png", model_sheet),
        ("expressions_layout.png", expression_sheet),
        ("reference_card_layout.png", reference_card),
        ("chibi_sheet_layout.png", chibi_sheet),
    ):
        make().save(OUT / name, optimize=True)
        print(OUT / name)


if __name__ == "__main__":
    main()
