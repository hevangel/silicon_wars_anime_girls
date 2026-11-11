# Arcade pixel style — production recipe (issue #60)

**Status:** Technical scaffold, not visual approval. Approved Intel/AMD default manga images are the canonical identity. This style creates new files in `characters/<id>/references/pixel_arcade_sf2/`; it does NOT replace them.

## Reference vs pixel-native final

| Reference | Use | Must not be mistaken for |
| --- | --- | --- |
| `characters/amd/character_sheet.png` | identity, clothing and silhouette comparison | 96×128 pixel master |
| `characters/intel/character_sheet.png` | crown/hair/hem-lock continuity | 96×128 pixel master |
| Hand-corrected native PNG in style folder | source for idle, turnarounds and motion | human approval (until formally signed off) |
| Nearest-neighbour 4× preview | review visible pixel clusters | editable master or art quality proof |

To compare **before/after**, view the original approved sheet at 1× and the native 96×128 master at 1×; then show the same master at 4× with nearest-neighbour scaling. Put both characters side by side and explicitly evaluate hair/eye/prop and stance distinctiveness.

## Step by step

1. Read `bible/art_style.yaml`, `style_usage_policy.yaml` and character `continuity.yaml`. Follow the identity override in `characters/{amd,intel}/styles/pixel_arcade_sf2.yaml`.
2. Author **one AMD idle/attack master** at native 96×128 (or choose 128×160 and stick with it). In Aseprite/LibreSprite/Piskel, draw bold silhouette, lock baseline and foot pivot, then place intentional clusters and material ramps. 16–32 opaque colors including outline, no smoothed AA.
3. Manually fix anatomical breaks, metallic ramp direction, ponytail outline continuity and hair/face identity. Export lossless RGBA, transparent outside (alpha only 0 or 255).
4. Create a native *pixel* model sheet: separately arranged front, 3/4, profile, back, close-up and attack stance, with labels outside the sprite regions. Crop with nearest-neighbour only. **Do not** scale down the existing manga sheet.
5. Repeat with Intel, preserving light-blue hair, crown, cream/blue coat, wafer heirloom and Intel Inside skirt hem. Give her a regal wide command stance, not AMD's low lunge.
6. Make two expressions × two camera angles **after** each master is approved. Store variants as individual equally sized frame files. Create a `frames.json` manifest with anchor/hitbox, record pose and expression, and run the validator/packer below.
7. Check at real 1× size and 4× pixel zoom, plus visual proof against both Season 1 approved sheets. Request explicit human visual approval **before** changing `human_approved` or using in chapter/public gallery.
8. Only after signoff, make 4-frame breath/ponytail test loop. Use independent frame art or documented optional limb layers; preserve stationary foot pivots.

## Manifest format and tools

Run from repository root after `python -m pip install "Pillow>=10.1"`:

```sh
python tools/pixel_arcade.py validate characters/amd/references/pixel_arcade_sf2/frames.json
python tools/pixel_arcade.py pack characters/amd/references/pixel_arcade_sf2/frames.json --out /tmp/amd_arcade
python -m unittest discover -s tools -p test_pixel_arcade.py
```

`frames.json` near the editable frame PNGs, in this shape (the files shown are **examples**; do not commit this manifest until they actually exist):

```json
{
  "schema": 1,
  "style": "pixel_arcade_sf2",
  "character": "amd",
  "canvas": {"width": 96, "height": 128},
  "palette_limit": 32,
  "status": "unapproved",
  "frames": [
    {"id": "idle-01", "file": "idle-01.png", "anchor": [47, 121], "hitbox": [20, 12, 74, 126]},
    {"id": "idle-02", "file": "idle-02.png", "anchor": [47, 121], "hitbox": [20, 12, 74, 126]}
  ]
}
```

The tool verifies frame IDs, file existence, size, palette count, hard alpha, anchors and hitboxes. It outputs a uniform grid sheet, per-frame tags JSON and integer-scale nearest-neighbor review PNG. Frame metadata uses **x0,y0,x1,y1** for hitboxes (exclusive high edges). Input paths are relative to the manifest's directory. `pack` is deterministic for identical frames and inputs; it is not an image generator or art-quality adjudicator.

## Problems and fixes

- **Ugly, blown-up sprite:** likely high-res art shrunk into pixels. Rebuild at true native resolution and manually clean clusters, no automated palette hack.
- **Muddy face / lost headphones:** reserve small readable color/geometry clusters and match the approved portrait at 1×.
- **Jittering boots:** all frames share exactly the same anchor; inspect feet at 1× and review 4× nearest-neighbour side by side.
- **Ghost edges:** alpha contains 1–254 from antialiasing; re-ink pixel boundaries and re-export hard-alpha PNG.
- **Palette explosion:** count opaque RGBA colors across the entire animation set and consolidate deliberate ramps, not image dithering.
- **License/IP:** use original character design, original source PNGs and period-correct company marks; no copying third-party fighter frames, textures or game sounds.
- **Unreviewed art:** tool validation only checks format; the art-director must approve real master poses, expressions and identity.
