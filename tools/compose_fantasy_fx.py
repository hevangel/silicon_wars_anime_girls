#!/usr/bin/env python3
"""Deterministic RGBA plate compositor for the fantasy style.

Source PNG layers are never modified. Output is not automatically art approved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image


class PlateError(ValueError):
    pass


def compose(manifest: Path, prefix: Path):
    manifest = manifest.resolve()
    meta = json.loads(manifest.read_text(encoding="utf-8"))
    if meta.get("schema") != 1 or meta.get("style") != "live_action_hyperreal_fantasy":
        raise PlateError("Expected fantasy style schema 1")
    if meta.get("status") == "approved":
        raise PlateError("Human approval cannot be self-declared by a source manifest")
    canvas = meta.get("canvas", [])
    if (not isinstance(canvas, list) or len(canvas) != 2
            or any(type(x) is not int or x <= 0 for x in canvas)):
        raise PlateError("Canvas must be positive integer [width,height]")
    if not meta.get("actor_id") or not meta.get("wardrobe_id"):
        raise PlateError("Stable actor_id and wardrobe_id required")
    plates = meta.get("plates")
    if not isinstance(plates, list) or len(plates) < 3:
        raise PlateError("At least actor, costume and FX plates required")
    ids, items = set(), []
    allowed = {"actor": 0, "costume": 1, "fx": 2, "atmosphere": 3}
    roles = []
    for entry in plates:
        eid, role, rel = entry.get("id"), entry.get("role"), entry.get("file")
        if not isinstance(eid, str) or not eid or eid in ids:
            raise PlateError("Plate ids must be nonempty unique strings")
        ids.add(eid)
        if role not in allowed:
            raise PlateError("Unknown plate role")
        roles.append(role)
        if not isinstance(rel, str) or not rel.lower().endswith(".png"):
            raise PlateError("Plate file must be PNG")
        fpath = (manifest.parent / rel).resolve()
        if not fpath.is_relative_to(manifest.parent) or not fpath.is_file():
            raise PlateError("Missing or unsafe plate path: " + rel)
        with Image.open(fpath) as im:
            if im.size != tuple(canvas) or im.mode != "RGBA":
                raise PlateError("Every plate must be native-size RGBA, not auto-resized: " + rel)
            rendered = im.copy()
        digest = hashlib.sha256(fpath.read_bytes()).hexdigest()
        items.append((role, rendered, {"id": eid, "role": role, "sha256": digest, "file": rel}))
    if roles[:2] != ["actor", "costume"] or any(allowed[a] > allowed[b] for a, b in zip(roles, roles[1:])):
        raise PlateError("Layer order must be actor, costume, FX and then optional atmosphere")
    if "fx" not in roles:
        raise PlateError("At least one separate FX layer required")
    clean = Image.new("RGBA", tuple(canvas), (0, 0, 0, 0))
    full = Image.new("RGBA", tuple(canvas), (0, 0, 0, 0))
    for role, image, _ in items:
        full = Image.alpha_composite(full, image)
        if role in ("actor", "costume"):
            clean = Image.alpha_composite(clean, image)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    clean.save(str(prefix) + "-clean.png", optimize=False)
    full.save(str(prefix) + "-all.png", optimize=False)
    result = {"style": meta["style"], "status": "unapproved",
              "actor_id": meta["actor_id"], "wardrobe_id": meta["wardrobe_id"],
              "canvas": canvas, "layers": [r for _, _, r in items]}
    Path(str(prefix) + ".json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    try:
        result = compose(args.manifest, args.out)
        print("COMPOSITED", len(result["layers"]), "plates; human approval pending")
    except (OSError, ValueError, KeyError) as exc:
        p.exit(1, "compose_fantasy_fx: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
