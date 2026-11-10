#!/usr/bin/env python3
"""Validate and assemble original pixel-native arcade sprite frames.

Source frame images and manifests remain editable; only reviewed sources should
be marked approved. Requires Pillow >=10.1. No generated sprite is art-approved.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


class SpriteError(ValueError):
    """Invalid or inconsistent source sprite metadata/pixels."""


def read_manifest(path: Path):
    path = path.resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != 1 or data.get("style") != "pixel_arcade_sf2":
        raise SpriteError("Expected schema 1 and style pixel_arcade_sf2")
    canvas = data.get("canvas", {})
    size = (canvas.get("width"), canvas.get("height"))
    if size not in ((96, 128), (128, 160)):
        raise SpriteError("Canvas must be 96x128 or 128x160 native pixels")
    palette_limit = data.get("palette_limit", 32)
    if type(palette_limit) is not int or not (16 <= palette_limit <= 32):
        raise SpriteError("Palette limit must be an integer 16..32")
    if data.get("status") == "approved":
        raise SpriteError("An approved status requires a separate human review record; do not infer from this manifest")
    frames = data.get("frames", [])
    if not isinstance(frames, list) or not frames:
        raise SpriteError("Frames must be a nonempty list")
    ids = set()
    images = []
    color_set = set()
    base = path.parent
    for frame in frames:
        fid = frame.get("id")
        if not isinstance(fid, str) or not fid or fid in ids:
            raise SpriteError("Frame IDs must be unique nonempty strings")
        ids.add(fid)
        rel = frame.get("file")
        if not isinstance(rel, str) or not rel.lower().endswith(".png"):
            raise SpriteError(fid + ": file must be a relative PNG path")
        source = (base / rel).resolve()
        if not source.is_relative_to(base) or not source.is_file():
            raise SpriteError(fid + ": missing or disallowed frame " + rel)
        anchor = frame.get("anchor")
        hitbox = frame.get("hitbox")
        if (not isinstance(anchor, list) or len(anchor) != 2
                or any(type(v) is not int for v in anchor)
                or not 0 <= anchor[0] < size[0] or not 0 <= anchor[1] < size[1]):
            raise SpriteError(fid + ": invalid integer anchor")
        if (not isinstance(hitbox, list) or len(hitbox) != 4
                or any(type(v) is not int for v in hitbox)
                or not (0 <= hitbox[0] < hitbox[2] <= size[0])
                or not (0 <= hitbox[1] < hitbox[3] <= size[1])):
            raise SpriteError(fid + ": hitbox must be [x0,y0,x1,y1] within canvas")
        with Image.open(source) as src:
            if src.size != size:
                raise SpriteError(fid + ": dimensions " + str(src.size) + " differ from " + str(size))
            image = src.convert("RGBA")
        pixels = image.getdata()
        for rgba in pixels:
            if rgba[3] not in (0, 255):
                raise SpriteError(fid + ": transparent pixel has antialiased alpha")
            if rgba[3] == 255:
                color_set.add(rgba[:3])
                if len(color_set) > palette_limit:
                    raise SpriteError("Animation exceeds palette limit of " + str(palette_limit))
        images.append(image)
    return data, images, len(color_set)


def pack(manifest: Path, output_prefix: Path, columns: int):
    data, images, colors = read_manifest(manifest)
    if columns <= 0 or columns > len(images):
        raise SpriteError("columns must be between one and frame count")
    w, h = data["canvas"]["width"], data["canvas"]["height"]
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * w, rows * h), (0, 0, 0, 0))
    tags = {"schema": 1, "character": data.get("character"),
            "style": data["style"], "canvas": data["canvas"], "palette_colors": colors,
            "frames": []}
    for idx, (frame, image) in enumerate(zip(data["frames"], images)):
        x, y = idx % columns * w, idx // columns * h
        sheet.paste(image, (x, y))
        tags["frames"].append({"id": frame["id"],
                               "rect": [x, y, w, h],
                               "anchor": frame["anchor"],
                               "hitbox": frame["hitbox"]})
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(str(output_prefix) + ".png", optimize=False)
    sheet.resize((sheet.width * 4, sheet.height * 4), Image.Resampling.NEAREST).save(
        str(output_prefix) + "-4x.png", optimize=False)
    (Path(str(output_prefix) + ".json")).write_text(
        json.dumps(tags, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return tags


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate", help="Check frames, palette and anchors")
    check.add_argument("manifest", type=Path)
    out = sub.add_parser("pack", help="Build lossless PNG grid, 4x preview and frame tags")
    out.add_argument("manifest", type=Path)
    out.add_argument("--out", type=Path, required=True)
    out.add_argument("--columns", type=int, default=2)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            data, images, count = read_manifest(args.manifest)
            print("VALID", data.get("character"), len(images), "frames,", count, "opaque colors")
        else:
            tags = pack(args.manifest, args.out, args.columns)
            print("PACKED", len(tags["frames"]), "frames ->", args.out)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(1, "pixel_arcade: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
