"""Build the Anime ED Walk parade: cut out the solo walkers and composite the frieze.

Pipeline (modular, per the parade-composition method):
  1. Each character is generated individually from her model sheet as a solo
     left-facing walking figure on a plain white background (walkers/).
  2. Cutout: a low-threshold flood fill from the image border decides what is
     background (connectivity); edge-adjacent foreground pixels get a soft
     distance-based alpha. Interior background-colored regions (white coats,
     pale hair) are not connected to the border and stay opaque.
  3. Composite: roster order left to right (the march heads left), one flat
     ground plane, slight overlap painted rear-first, heights scaled by age
     class from characters/roster.json (adults 1.00, Nvidia 1.06, kids 0.68,
     tweens 0.76, grandmothers 0.96, Bell Labs seated 0.80).
  4. Outputs: ed-walk-full.png plus six posting slices cut at figure
     boundaries so X/Facebook carousels stitch seamlessly.

Intel and Huawei would not generate as fresh walkers; their figures are the
SIDE views cropped from their model sheets (boxes below), already in profile.

Usage: python3 tools/build_ed_walk.py [--cutouts-only | --composite-only]
"""
import json, sys
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / 'art' / 'ed-walk'
BACKGROUND = (18, 20, 28, 255)
BASE_HEIGHT = 1500
TOP_PAD = 130
BOTTOM_PAD = 190
STEP = 0.82

SHEET_CROPS = {'intel': (1085, 55, 1405, 790), 'huawei': (1100, 8, 1395, 778)}


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


def scale_for(slug, age):
    if '9' in age or '10' in age:
        return 0.68
    if '12' in age or '13' in age:
        return 0.76
    if slug == 'nvidia':
        return 1.06
    if slug == 'bell-labs':
        return 0.80
    if 'senior' in age or 'elder' in age:
        return 0.96
    return 1.00


def build_composite():
    roster = json.loads((ROOT / 'characters' / 'roster.json').read_text())
    figures, xs = [], []
    x = 60
    for entry in roster:
        slug = entry['slug']
        im = Image.open(ART / 'cutouts' / f'{slug}.png')
        h = int(BASE_HEIGHT * scale_for(slug, entry.get('age', 'adult')))
        w = int(im.width * h / im.height)
        figures.append((slug, im.resize((w, h)), w, h))
        xs.append(x)
        x += int(w * STEP)
    width = xs[-1] + figures[-1][2] + 60
    height = TOP_PAD + BASE_HEIGHT + BOTTOM_PAD
    ground = TOP_PAD + BASE_HEIGHT
    canvas = Image.new('RGBA', (width, height), BACKGROUND)
    ImageDraw.Draw(canvas).line([(0, ground), (width, ground)], fill=(90, 96, 110, 255), width=5)
    for (_, im, _, h), fx in reversed(list(zip(figures, xs))):
        canvas.alpha_composite(im, (fx, ground - h))
    canvas.convert('RGB').save(ART / 'ed-walk-full.png')
    print('panorama', canvas.size)
    bounds = [0, 6, 12, 18, 24, 29, 32]
    for i in range(6):
        a, b = bounds[i], bounds[i + 1]
        x0 = 0 if i == 0 else xs[a] - 30
        x1 = width if i == 5 else xs[b] - 30
        canvas.crop((x0, 0, x1, height)).convert('RGB').save(ART / f'ed-walk-slice-{i + 1}.png')
        print(f'slice {i + 1}: x {x0}-{x1}')


if __name__ == '__main__':
    if '--composite-only' not in sys.argv:
        build_cutouts()
    if '--cutouts-only' not in sys.argv:
        build_composite()
