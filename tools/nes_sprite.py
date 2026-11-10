#!/usr/bin/env python3
"""Validate and pack original 8-bit NES-inspired tile-constrained sprites.

Creative constraints are not full NES PPU emulation. Requires Pillow >=10.1.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from PIL import Image


class NesSpriteError(ValueError):
    """Inconsistent sprite frame or palette allocation."""


def read_manifest(path: Path):
    path = path.resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != 1 or data.get("style") != "pixel_8bit_nes":
        raise NesSpriteError("Expected schema 1 and pixel_8bit_nes style")
    if data.get("status") == "approved":
        raise NesSpriteError("Visual approval is independent; cannot self-approve")
    mode = data.get("mode", "creative_budget")
    if mode not in ("creative_budget", "hardware_candidate"):
        raise NesSpriteError("mode must be creative_budget or hardware_candidate")
    canvas = data.get("canvas") or {}
    size = (canvas.get("width"), canvas.get("height"))
    if size not in ((32, 48), (48, 64)):
        raise NesSpriteError("Canvas must be 32x48 or 48x64")
    w, h = size
    palettes = data.get("palettes")
    if not isinstance(palettes, dict) or not palettes:
        raise NesSpriteError("A palette bank dictionary is required")
    if mode == "hardware_candidate" and len(palettes) > 4:
        raise NesSpriteError("NES PPU hardware candidates permit at most four sprite subpalettes")
    parsed = {}
    for name, raw in palettes.items():
        if not isinstance(name, str) or not isinstance(raw, list) or not 1 <= len(raw) <= 3:
            raise NesSpriteError("Each bank requires 1..3 opaque RGB colors")
        try:
            values = {tuple(bytes.fromhex(v[1:])) for v in raw
                      if isinstance(v, str) and len(v) == 7 and v.startswith("#")}
        except ValueError as exc:
            raise NesSpriteError("Invalid bank hex colors") from exc
        if len(values) != len(raw):
            raise NesSpriteError("Palette colors must be unique #RRGGBB values")
        parsed[name] = values
    default = data.get("default_palette")
    if default not in parsed:
        raise NesSpriteError("default_palette must refer to a palette bank")
    tile_banks = data.get("tile_palettes", {})
    if not isinstance(tile_banks, dict):
        raise NesSpriteError("tile_palettes must be a mapping")
    for key, name in tile_banks.items():
        try:
            xs, ys = key.split(",")
            tx, ty = int(xs), int(ys)
        except (AttributeError, TypeError, ValueError) as exc:
            raise NesSpriteError("tile coordinate must be x,y") from exc
        if not (0 <= tx < w // 8 and 0 <= ty < h // 8) or name not in parsed:
            raise NesSpriteError("tile palette assignment is out of bounds or unknown")
    frames = data.get("frames")
    if not isinstance(frames, list) or not frames:
        raise NesSpriteError("At least one frame is required")
    ids, images = set(), []
    for frame in frames:
        fid, rel = frame.get("id"), frame.get("file")
        if not isinstance(fid, str) or not fid or fid in ids:
            raise NesSpriteError("Frame IDs must be unique and nonempty")
        ids.add(fid)
        if not isinstance(rel, str) or not rel.lower().endswith(".png"):
            raise NesSpriteError("Frame file must be a relative PNG")
        fpath = (path.parent / rel).resolve()
        if not fpath.is_relative_to(path.parent) or not fpath.is_file():
            raise NesSpriteError("Missing or disallowed frame file: " + rel)
        anchor, hitbox = frame.get("anchor"), frame.get("hitbox")
        if (not isinstance(anchor, list) or len(anchor) != 2
                or any(type(v) is not int for v in anchor)
                or not (0 <= anchor[0] < w and 0 <= anchor[1] < h)):
            raise NesSpriteError("Invalid frame foot anchor")
        if (not isinstance(hitbox, list) or len(hitbox) != 4
                or any(type(v) is not int for v in hitbox)
                or not (0 <= hitbox[0] < hitbox[2] <= w
                        and 0 <= hitbox[1] < hitbox[3] <= h)):
            raise NesSpriteError("Invalid hitbox")
        with Image.open(fpath) as source:
            if source.size != size:
                raise NesSpriteError("Wrong native image size")
            image = source.convert("RGBA")
        for y in range(0, h, 8):
            active = 0
            for x in range(0, w, 8):
                bank = parsed[tile_banks.get(str(x//8) + "," + str(y//8), default)]
                opaque = False
                for pixel in image.crop((x, y, x+8, y+8)).getdata():
                    if pixel[3] not in (0, 255):
                        raise NesSpriteError("Antialiased alpha is forbidden")
                    if pixel[3] == 255:
                        opaque = True
                        if pixel[:3] not in bank:
                            raise NesSpriteError("Pixel color not assigned to its 8x8 palette bank")
                active += int(opaque)
            if mode == "hardware_candidate" and active > 8:
                raise NesSpriteError("More than eight 8x8 tile objects in a scanline band")
        images.append(image)
    return data, images


def pack(manifest: Path, output_prefix: Path, columns: int = 4):
    data, images = read_manifest(manifest)
    if columns < 1:
        raise NesSpriteError("columns must be positive")
    columns = min(columns, len(images))
    w, h = data["canvas"]["width"], data["canvas"]["height"]
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new("RGBA", (columns * w, rows * h), (0, 0, 0, 0))
    frames = []
    for index, (entry, image) in enumerate(zip(data["frames"], images)):
        x, y = index % columns * w, index // columns * h
        sheet.paste(image, (x, y))
        frames.append({"id": entry["id"], "rect": [x, y, w, h],
                       "anchor": entry["anchor"], "hitbox": entry["hitbox"]})
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(str(output_prefix) + ".png", optimize=False)
    sheet.resize((sheet.width*3, sheet.height*3), Image.Resampling.NEAREST).save(
        str(output_prefix) + "-3x.png", optimize=False)
    tags = {"schema": 1, "style": "pixel_8bit_nes", "character": data.get("character"),
            "mode": data.get("mode", "creative_budget"), "frames": frames,
            "hardware_verified": False}
    (Path(str(output_prefix) + ".json")).write_text(json.dumps(tags, indent=2) + "\n", encoding="utf-8")
    return tags


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("manifest", type=Path)
    pack_command = sub.add_parser("pack")
    pack_command.add_argument("manifest", type=Path)
    pack_command.add_argument("--out", required=True, type=Path)
    pack_command.add_argument("--columns", default=4, type=int)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            data, images = read_manifest(args.manifest)
            print("VALID", data.get("character"), len(images), "frames; mode", data.get("mode", "creative_budget"))
        else:
            result = pack(args.manifest, args.out, args.columns)
            print("PACKED", len(result["frames"]), "frames; hardware_verified=false")
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, "nes_sprite: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
