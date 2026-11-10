# 8-bit NES-inspired sprite production (issue #61)

**Status:** Visual-production scaffold only. No master has been approved. Keep all outputs under `characters/<id>/references/pixel_8bit_nes/`, never overwrite Season 1 reference cards.

## Compare styles at the correct pixel size

| Rule | NES-inspired creative style | Arcade 1990s style |
| --- | --- | --- |
| Native master | 32×48 or 48×64 | 96×128 or 128×160 |
| Color | 3 visible colors + transparency per assigned 8×8 tile palette | 16–32 colors total, nuanced material ramps |
| Sprite silhouette | Simple, symbolic and highly contrasted | More anatomy, selective outlines and highlights |
| Source | deliberate tile-scale pixel clusters | deliberate hand-directed pixel clusters |
| Movement | 4-frame walk/idle, symbol/face-tile changes | detailed per-frame or modular layers |
| Stage preview | 256×240, optionally 3× pixel zoom | 1× plus 4× zoom |
| Hardware authenticity | Not implied; emulator qualification required | Not aimed at NES hardware |

**Before/after artwork comparison** uses the approved [AMD](../../characters/amd/character_sheet.png) and [Intel](../../characters/intel/character_sheet.png) manga designs as identity references; after master production, show both same-stance variants at true 1× and integer zoom. Those comparison images are **not yet produced**.

## Steps

1. Select the character's documented identity, silhouette lock and a specific palette allocation from `characters/<id>/styles/pixel_8bit_nes.yaml`.
2. Sketch AMD and Intel directly at 48×64 native pixels; plan tile borders as 8×8, keep a baseline/anchor shared by every frame and distinct AMD/Intel poses.
3. Draw one clean **AMD master**. Within each tile, use a chosen 3-color bank and transparency; no automatic shrinking/quantization as final art. Review tiny face and distinctive hair/prop first.
4. Build a reduced-detail model sheet with front, side, back, face/eye/mouth tiles, visible swatches, a tile/palette bank table and at least one pose. Labels live outside pixel art.
5. Repeat for Intel, keep sapphire crown/hair/coats with different silhouette. Only after both pass human approval, draw two expressions × two angles and four idle frames.
6. Create `frames.json` alongside actual PNG source. Example (do **not** commit as a real manifest before the files exist):

```json
{
  "schema": 1,
  "style": "pixel_8bit_nes",
  "character": "amd",
  "mode": "creative_budget",
  "canvas": {"width": 48, "height": 64},
  "status": "unapproved",
  "palettes": {
    "main": ["#18151D", "#C83B35", "#F2C7A2"],
    "face": ["#18151D", "#F2C7A2", "#E7A045"]
  },
  "default_palette": "main",
  "tile_palettes": {"2,1": "face"},
  "frames": [
    {"id": "idle-01", "file": "idle-01.png", "anchor": [24, 60], "hitbox": [10, 7, 38, 62]}
  ]
}
```

7. Run (after `python -m pip install "Pillow>=10.1"`):

```sh
python tools/nes_sprite.py validate characters/amd/references/pixel_8bit_nes/frames.json
python tools/nes_sprite.py pack characters/amd/references/pixel_8bit_nes/frames.json --out /tmp/amd_nes
python -m unittest discover -s tools -p test_nes_sprite.py
```

Packer outputs a native PNG sheet, a 3× nearest-neighbour review preview, and per-frame JSON anchors/hitboxes. Tile/palette checks are **format checks**, not a judgment of attractiveness.

## NES hardware candidate mode

`mode: hardware_candidate` means **only** that the validator checks selected plausible constraints. It does *not* emulate the NES PPU. Real NES hardware uses 8×8 or 8×16 object sprites, 4 three-color sprite subpalettes plus transparency, 64 OAM slots and a practical 8-sprites-per-scanline limit (with priority and sprite-zero behavior). The validator's 8×8 tile occupancy approximation is not a complete sprite/OAM renderer; layered metasprites, palette memory, attribute priorities and flickering must be tested on an emulator. Never label a mock-up 'hardware accurate' absent those tests.

## Troubleshooting

- **Character seems like an anonymous blob:** preserve AMD's rearward red ponytail and headset arc; Intel's tall crown and separate blue hair curtain. Compare at 1×.
- **Fourth color in tile:** split the shade into a separate 8×8 tile or use an intentional palette reassignment; do not add antialiasing.
- **Sprite flicker:** check which 8×8 tiles overlap scanlines; then validate metasprite assembly in emulator, not merely in this tool.
- **Game copy / copyright:** original source shapes and moves only; NES inspiration is technical, not a license to copy sprites or music.
- **Wrong pose:** choose different foot placement, head tilt and arm shape, not merely a palette recolor.
- **No approved render:** explicit art-director signoff is required before making preview public or marking style as canonical.

References: [NESdev PPU sprites](https://www.nesdev.org/wiki/PPU_sprites), [NESdev palettes](https://www.nesdev.org/wiki/PPU_palettes), [Aseprite](https://www.aseprite.org/).
