"""Build the Anime ED Walk parade: cut out the solo walkers and composite the frieze.

Pipeline (modular, per the parade-composition method):
  1. Each character is generated individually from her model sheet as a solo
     left-facing walking figure on a plain white background (walkers/).
  2. Cutout: a low-threshold flood fill from the image border decides what is
     background (connectivity); edge-adjacent foreground pixels get a soft
     distance-based alpha. Interior background-colored regions (white coats,
     pale hair) are not connected to the border and stay opaque.
  3. Composite: roster order left to right (the march heads left), one flat
     ground plane, slight overlap painted rear-first. Canonical barefoot
     heights come from characters/roster.json; inspected skull/sole landmarks
     and footwear allowances live in art/ed-walk/height-calibration.json.
     Hats, crowns, hair ornaments and background shadows do not set stature.
  4. Outputs: ed-walk-full.png plus six posting slices cut at figure
     boundaries so X/Facebook carousels stitch seamlessly.

Intel and Huawei initially produced no image with the standard walker
prompt. The fix (found by testing text combinations): scrub the brand name
from the prompt and explicitly require plain unmarked panels with no text,
logo or emblem — with that wording, generation succeeds even with the full
model sheet as reference. Their walkers in walkers/ are the full-sheet-
reference, de-logoed-prompt generations. (Earlier builds used SIDE views
cropped from their model sheets as stand-ins; SHEET_CROPS is kept empty.)

The current v2 walkers face left without mirroring; see art/ed-walk/README.md
for the superseded v1 history. This script never flips the source figures.

Usage: python3 tools/build_ed_walk.py [--cutouts-only | --composite-only]
"""
import hashlib
import json, sys
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'art' / 'ed-walk'
BACKGROUND = (255, 255, 255, 255)
BASE_HEIGHT = 1500
TOP_PAD = 130
BOTTOM_PAD = 190
STEP = 0.82

SHEET_CROPS = {}  # was intel/huawei sheet side-views before the de-logoed prompts worked


def cutout(im, flood_tol=34, lo=26, hi=105):
    a = np.asarray(im.convert('RGB')).astype(np.float32)
    h, w = a.shape[:2]
    corners = np.concatenate([a[:10, :10].reshape(-1, 3), a[:10, -10:].reshape(-1, 3),
                              a[-10:, :10].reshape(-1, 3), a[-10:, -10:].reshape(-1, 3)])
    bgc = np.median(corners, axis=0)
    dist = np.abs(a - bgc).sum(axis=2)
    bg_like = dist < flood_tol
    seen = np.zeros((h, w), bool)
    q = deque()
    seeds = ([(0, x) for x in range(w)] + [(h - 1, x) for x in range(w)]
             + [(y, 0) for y in range(h)] + [(y, w - 1) for y in range(h)])
    for y, x in seeds:
        if bg_like[y, x] and not seen[y, x]:
            seen[y, x] = True
            q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not seen[ny, nx] and bg_like[ny, nx]:
                seen[ny, nx] = True
                q.append((ny, nx))
    ramp = np.clip((dist - lo) / (hi - lo), 0, 1)
    alpha = np.where(seen, 0.0, 1.0)
    adj = np.zeros((h, w), bool)
    adj[1:, :] |= seen[:-1, :]; adj[:-1, :] |= seen[1:, :]
    adj[:, 1:] |= seen[:, :-1]; adj[:, :-1] |= seen[:, 1:]
    alpha = np.where((~seen) & adj, np.maximum(ramp, 0.55), alpha)
    al = Image.fromarray((alpha * 255).astype(np.uint8), 'L')
    out = im.convert('RGBA')
    out.putalpha(al)
    return out.crop(al.getbbox())


def largest_component(im):
    al = np.asarray(im.getchannel('A'))
    fg = al > 8
    h, w = fg.shape
    seen = np.zeros((h, w), bool)
    best = None
    ys, xs = np.nonzero(fg)
    for y0, x0 in zip(ys[::7], xs[::7]):
        if seen[y0, x0] or not fg[y0, x0]:
            continue
        q = deque([(y0, x0)])
        seen[y0, x0] = True
        cells = []
        while q:
            y, x = q.popleft()
            cells.append((y, x))
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and fg[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    q.append((ny, nx))
        if best is None or len(cells) > len(best):
            best = cells
    keep = np.zeros((h, w), bool)
    for y, x in best:
        keep[y, x] = True
    a = np.asarray(im).copy()
    a[:, :, 3] = np.where(keep, al, 0).astype(np.uint8)
    out = Image.fromarray(a, 'RGBA')
    return out.crop(out.getchannel('A').getbbox())


def build_cutouts():
    (ART / 'cutouts').mkdir(parents=True, exist_ok=True)
    for path in sorted((ART / 'walkers').glob('*.png')):
        slug = path.stem
        result = cutout(Image.open(path))
        if slug in ('anthropic', 'amd', 'nvidia'):
            result = largest_component(result)  # drop detached background islands
        result.save(ART / 'cutouts' / f'{slug}.png')
        print('cutout', slug, result.size)
    for slug, box in SHEET_CROPS.items():
        sheet = Image.open(ROOT / 'characters' / slug / 'character_sheet.png')
        result = cutout(sheet.crop(box), flood_tol=28, lo=20, hi=80)
        result.save(ART / 'cutouts' / f'{slug}.png')
        print('cutout', slug, '(sheet side view)', result.size)


REFERENCE_CM = 168
CALIBRATION = ART / 'height-calibration.json'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def figure_geometry(entry, im, calibration):
    """Uniform scale from estimated anatomical crown to supporting sole.

    Coordinates refer to the unchanged source cutout, not the full canvas.
    Footwear adds visible height to barefoot stature. A seated character has
    a separate art-directed crown-to-floor span, not a standing-height ratio.
    """
    head = calibration['head_top_y']
    ground = calibration['ground_y']
    if not 0 <= head < ground < im.height:
        raise ValueError(f"Invalid head/ground landmarks for {entry['slug']}")
    if calibration['source_size'] != list(im.size):
        raise ValueError(f"Recalibrate changed cutout size for {entry['slug']}")
    target_cm = calibration.get('seated_head_height_cm')
    if target_cm is None:
        target_cm = entry['height_cm'] + calibration['footwear_cm']
    if target_cm <= 0:
        raise ValueError(f"Invalid target height for {entry['slug']}")
    target_px = BASE_HEIGHT * target_cm / REFERENCE_CM
    scale = target_px / (ground - head)
    height = round(im.height * scale)
    width = round(im.width * scale)
    return {
        'width': width, 'height': height,
        # Preserve the projected crown coordinate; rounding both landmarks
        # independently would add an unnecessary second pixel of audit error.
        'head_offset': head * height / im.height,
        'ground_offset': round(ground * height / im.height),
        'target_span_cm': target_cm, 'target_span_px': target_px,
    }


def build_composite():
    roster_path = ROOT / 'characters' / 'roster.json'
    roster = json.loads(roster_path.read_text(encoding='utf-8'))
    calibration = json.loads(CALIBRATION.read_text(encoding='utf-8'))
    figures, xs, records = [], [], []
    x = 60
    for entry in roster:
        slug = entry['slug']
        source = ART / 'cutouts' / f'{slug}.png'
        markers = calibration['characters'][slug]
        source_hash = sha256(source)
        if source_hash != markers['source_sha256']:
            raise ValueError(f"Cutout changed for {slug}; inspect and update height-calibration.json")
        with Image.open(source) as im:
            geometry = figure_geometry(entry, im, markers)
            resized = im.convert('RGBA').resize((geometry['width'], geometry['height']))
        figures.append((resized, geometry))
        xs.append(x)
        records.append({'slug': slug, 'height_cm': entry['height_cm'],
                        'source_sha256': source_hash, 'x': x, **geometry})
        x += int(geometry['width'] * STEP)
    width = xs[-1] + figures[-1][1]['width'] + 60
    ground = TOP_PAD + max(g['ground_offset'] for _, g in figures)
    below_ground = max(g['height'] - g['ground_offset'] for _, g in figures)
    height = ground + max(BOTTOM_PAD, below_ground + 1)
    canvas = Image.new('RGBA', (width, height), BACKGROUND)
    ImageDraw.Draw(canvas).line([(0, ground), (width, ground)], fill=(176, 182, 192, 255), width=5)
    for (im, geometry), fx in reversed(list(zip(figures, xs))):
        canvas.alpha_composite(im, (fx, ground - geometry['ground_offset']))
    for record in records:
        record['y'] = ground - record['ground_offset']
    canvas.convert('RGB').save(ART / 'ed-walk-full.png')
    print('panorama', canvas.size)
    bounds = [0, 6, 12, 18, 24, 29, 32]
    slices = []
    for i in range(6):
        a, b = bounds[i], bounds[i + 1]
        x0 = 0 if i == 0 else xs[a] - 30
        x1 = width if i == 5 else xs[b] - 30
        canvas.crop((x0, 0, x1, height)).convert('RGB').save(ART / f'ed-walk-slice-{i + 1}.png')
        slices.append({'file': f'ed-walk-slice-{i + 1}.png', 'x0': x0, 'x1': x1})
        print(f'slice {i + 1}: x {x0}-{x1}')
    manifest = {
        'schema_version': 1,
        'method': 'Inspected anatomical crown to supporting sole; uniform scaling; no flips or art regeneration',
        'roster_sha256': sha256(roster_path),
        'calibration_sha256': sha256(CALIBRATION),
        'builder_sha256': sha256(Path(__file__)),
        'pixels_per_cm': BASE_HEIGHT / REFERENCE_CM,
        'canvas': {'width': width, 'height': height, 'ground_y': ground},
        'figures': records, 'slices': slices,
        'render_sha256': sha256(ART / 'ed-walk-full.png'),
    }
    (ART / 'ed-walk.render.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    if '--composite-only' not in sys.argv:
        build_cutouts()
    if '--cutouts-only' not in sys.argv:
        build_composite()
