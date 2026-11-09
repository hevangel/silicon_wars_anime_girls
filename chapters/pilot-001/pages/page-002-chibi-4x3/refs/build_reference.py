"""Build a text-free chibi cast reference from the three chibi sheets.

The sheets carry a title block, view labels, and a second expression row. This
script keeps only the turnaround figures: it detects each figure as a connected
shape, which excludes the loose title text, then takes the front and
three-quarter views and lays them out on the sheet background.

Top row: front views. Bottom row: three-quarter views.
Left to right: Intel, AMD, Nvidia (the panel's reference order).
"""
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[5]
OUT = ROOT / "chapters/pilot-001/pages/page-002-chibi-4x3/refs/cast-chibi-reference.jpg"
CAST = ["intel", "amd", "nvidia"]
BAND_TOP, BAND_BOTTOM = 120, 822
SCALE = 4
PAD = 14
CELL_HEIGHT = 640
GAP = 26
BACKGROUND = (247, 241, 230)


def blocks(mask):
    height, width = mask.shape
    height, width = height // SCALE * SCALE, width // SCALE * SCALE
    block = mask[:height, :width]
    return block.reshape(height // SCALE, SCALE, width // SCALE, SCALE).any(axis=(1, 3))


def figure_box(sheet, seed_x):
    pixels = np.asarray(sheet).astype(int)
    background = pixels[5, 5]
    band = np.abs(pixels[BAND_TOP:BAND_BOTTOM] - background).sum(axis=2) > 45
    grid = blocks(band)

    seed = (grid.shape[0] // 2, seed_x // SCALE)
    while not grid[seed]:
        seed = (seed[0] + 1, seed[1])
    seen = np.zeros_like(grid, dtype=bool)
    seen[seed] = True
    queue = deque([seed])
    while queue:
        y, x = queue.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < grid.shape[0] and 0 <= nx < grid.shape[1] and grid[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True
                queue.append((ny, nx))
    rows, cols = np.where(seen)
    return (cols.min() * SCALE, BAND_TOP + rows.min() * SCALE,
            (cols.max() + 1) * SCALE, BAND_TOP + (rows.max() + 1) * SCALE)


def clear_title_fragments(cell, band=72):
    """Erase stray title text that floats above the figure inside the crop.

    Only components that sit entirely inside the top band are cleared, so hair,
    crowns, and goggles that continue downward survive untouched.
    """
    pixels = np.asarray(cell).copy()
    background = np.array(BACKGROUND)
    busy = np.abs(pixels.astype(int) - background).sum(axis=2) > 45
    top = busy[:band]
    seen = np.zeros_like(top, dtype=bool)
    for y in range(band):
        for x in range(cell.width):
            if not top[y, x] or seen[y, x]:
                continue
            queue, component = deque([(y, x)]), []
            seen[y, x] = True
            while queue:
                cy, cx = queue.popleft()
                component.append((cy, cx))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < band and 0 <= nx < cell.width and top[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        queue.append((ny, nx))
            if max(py for py, _ in component) < band - 1:
                rows = [py for py, _ in component]
                cols = [px for _, px in component]
                pixels[min(rows):max(rows) + 1, min(cols):max(cols) + 1] = background
    return Image.fromarray(pixels)


def views(path):
    sheet = Image.open(path).convert("RGB")
    pixels = np.asarray(sheet).astype(int)
    background = pixels[5, 5]
    band = np.abs(pixels[BAND_TOP:BAND_BOTTOM] - background).sum(axis=2) > 45
    columns = band.sum(axis=0) > 3
    runs, start = [], None
    for x, filled in enumerate(list(columns) + [False]):
        if filled and start is None:
            start = x
        elif not filled and start is not None:
            if x - start > 300:
                runs.append((start, x))
            start = None

    cells = []
    for left, right in runs[:2]:
        box = figure_box(sheet, (left + right) // 2)
        figure = sheet.crop(box)
        cell = Image.new("RGB", (figure.width + PAD * 2, figure.height + PAD * 2), BACKGROUND)
        cell.paste(figure, (PAD, PAD))
        cells.append(clear_title_fragments(cell))
    return cells


def main():
    columns = [views(ROOT / f"characters/{name}/chibi_sheet.png") for name in CAST]
    columns = [[cell.resize((round(cell.width * CELL_HEIGHT / cell.height), CELL_HEIGHT),
                            Image.Resampling.LANCZOS) for cell in column] for column in columns]
    width = max(cell.width for column in columns for cell in column)
    sheet_width = len(columns) * (width + GAP) + GAP
    sheet_height = 2 * (CELL_HEIGHT + GAP) + GAP
    canvas = Image.new("RGB", (sheet_width, sheet_height), BACKGROUND)
    for row in range(2):
        for index, column in enumerate(columns):
            canvas.paste(column[row], (GAP + index * (width + GAP), GAP + row * (CELL_HEIGHT + GAP)))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, format="JPEG", quality=92)
    print(OUT, canvas.size)


if __name__ == "__main__":
    main()
