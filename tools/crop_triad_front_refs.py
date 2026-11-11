"""Crop one clean front-view figure per Tier 1 character.

Fixes applied after the first pass:
  - the sheet's inset gold border rule sits at ~14px, so crops start below it
  - Intel's title lockup overlaps the figure's column range, so it is erased
    with the sheet background colour instead of being cropped away
  - Nvidia keeps its full margin so the fists are not clipped; only the corner
    fragment of the lockup is erased, well clear of the hair

Read-only against characters/*; writes new files under the ensemble refs folder.
"""
import os
import numpy as np
from PIL import Image

OUT = "characters/_ensemble/compute-triad-idol-stage/refs"

# cid: (source, crop_box or None for auto, title_rect to fill or None)
PLAN = {
    "intel": ("characters/intel/character_sheet.png", (100, 26, 668, 807), (55, 20, 322, 205)),
    "amd":   ("characters/amd/character_sheet.png", (363, 29, 624, 737), None),
    "nvidia": ("characters/nvidia/character_sheet.png", (332, 27, 641, 789), (332, 60, 360, 190)),
}


def bg_color(a):
    edges = np.concatenate([
        a[0:8, 0:8].reshape(-1, 3), a[0:8, -8:].reshape(-1, 3),
        a[-8:, 0:8].reshape(-1, 3), a[-8:, -8:].reshape(-1, 3),
    ])
    return tuple(int(v) for v in np.median(edges, axis=0))


os.makedirs(OUT, exist_ok=True)

for cid, (path, box, title_rect) in PLAN.items():
    im = Image.open(path).convert("RGB")
    W, H = im.size
    bg = bg_color(np.asarray(im).astype(int))

    if title_rect:
        # erase the lockup on a copy, leaving the figure untouched
        im = im.copy()
        im.paste(Image.new("RGB", (title_rect[2] - title_rect[0], title_rect[3] - title_rect[1]), bg),
                 (title_rect[0], title_rect[1]))

    crop = im.crop(box)
    dst = os.path.join(OUT, f"{cid}-front.png")
    crop.save(dst)
    print(f"{cid}: box={box} size={crop.size} bg={bg} title_erased={bool(title_rect)} -> {dst}")
