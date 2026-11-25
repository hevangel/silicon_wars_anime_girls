#!/usr/bin/env python3
"""Save one rendered plate: download the remote image, write the sidecar record.

Usage: python tools/style_study/save_plate.py <plate-id> <image-url> [provider]

The sidecar `<plate-id>.json` sits beside the render and records the accepted
generation inputs (prompt, reference sheet, provider) plus content hashes, so a
later build can prove which prompt produced which file.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "art" / "style-study"
MANIFEST = OUT / "plates.json"
SHEET = "characters/arm/character_sheet.png"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    pid, url = sys.argv[1], sys.argv[2]
    provider = sys.argv[3] if len(sys.argv) > 3 else "autoglm/seedream"

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    plate = next((p for p in data["plates"] if p["id"] == pid), None)
    if plate is None:
        print(f"unknown plate id: {pid}")
        return 1

    target = ROOT / plate["file"]
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "silicon-wars-style-study/1"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        blob = resp.read()
    if len(blob) < 10_000 or not blob.startswith((b"\xff\xd8\xff", b"\x89PNG")):
        print(f"unexpected payload ({len(blob)} bytes); not saved")
        return 1
    # normalise to real PNG so the extension never lies about the payload
    from io import BytesIO
    from PIL import Image
    with Image.open(BytesIO(blob)) as im:
        im.convert("RGB").save(target, format="PNG", optimize=True)

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    prompt_sha = hashlib.sha256(plate["prompt"].encode("utf-8")).hexdigest()
    image_sha = sha256(target)
    sidecar = {
        "plate": pid,
        "style": plate["style_label"],
        "family": plate["family"],
        "variant": f"{plate['variant']}/{plate['variant_count']} {plate['variant_axis']}",
        "mode": plate["mode"],
        "provider": provider,
        "rendered_utc": now,
        "reference": SHEET,
        "reference_sha256": sha256(ROOT / SHEET),
        "prompt": plate["prompt"],
        "prompt_sha256": prompt_sha,
        "file": plate["file"],
        "image_sha256": image_sha,
        "bytes": target.stat().st_size,
    }
    (target.with_suffix(".json")).write_text(
        json.dumps(sidecar, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    plate["status"] = "rendered"
    plate["prompt_sha256"] = prompt_sha
    plate["image_sha256"] = image_sha
    plate["rendered"] = now
    plate["reference"] = SHEET
    MANIFEST.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print(f"saved {plate['file']} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
