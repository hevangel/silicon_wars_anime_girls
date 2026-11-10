# True 8-bit / early-console inspired sprite prompt

**Independence:** `pixel_8bit_nes` is distinct from `pixel_arcade_sf2`, `chibi` and `default_manga`. Every prompt is assembled as identity (approved reference and continuity), style (below), editable pose/scene and reproducible output. Do not replicate copyrighted NES game characters.

## Identity block (never edit to fit pose)

- AMD: adult red high **braided** ponytail, amber-eye impression, black/crimson chiplet jacket and headphones. Compact forward-leaning fighter.
- Intel: adult long light-blue hair, pointed unbranded sapphire crown, royal-blue/cream military coat, gold epaulettes, wafer heirloom and left front skirt-hem logo. Tall regal figure.

## Style block

Original *hand-constructed* 48×64 pixel figure (32×48 alternative), hard 8×8 tile grid, 3 opaque RGB colors plus transparent **per assigned sprite palette** (different tiles may select different declared palettes), thick high-contrast flat clusters, 1× native review, nearest-neighbour 3× display only, no gradients and no antialiasing. 256×240 stage preview is an optional **creative composition** and NOT proof that this source will run on a real NES.

## Editable scene block

Stance, camera (front / side / back), 4-frame breathing/walk timing, tile-level eye and mouth expressions, held wafer/chiplet and scene composition; keep hair and costume identity locked. Give AMD a low active pose and Intel a distinctly upright pose. When changing emotion, edit tiny face tiles only.

### AMD master reference prompt

Draw an original 8-bit console **source sprite** at 48×64 true pixels, adult AMD Crimson Challenger. Red braided high ponytail facing back-left, black/crimson jacket and a visible headphone loop, forward fighter stance with a compact chiplet emblem. Use deliberate solid pixel clusters and transparent hard edges, with per-tile color banks, no anti-aliased rendering. Deliver one static source frame for hand-cleanup before any animation.

### Intel master reference prompt

Draw an original 48×64 true-pixel Intel Blue Empress, upright with crown silhouette, long ice-blue hair, royal-blue/cream costume and a wafer charm; keep proportions mature, remove unnecessary coat trim only after reviewing what identifies her. Distinct stance from AMD; flat tile clusters, 3 colors plus transparency per tile palette.

## Negative block

NO 1990s high-detail fighting-game sprite, no Street Fighter poses, no automated downsample of anime PNGs, no smooth shading, no soft edges, no photorealism, no gradient, no generic red-and-blue recolor, no wrong hair color, no child proportions, no unapproved logo redesign, no invented "hardware accurate" label.

## Workflow caveats

Image models usually output high-resolution pixel-*looking* images, not indexed editable 8×8-tile source. Use the output **only as reference**, then manually author or repair every native pixel in Aseprite/LibreSprite. Verify palette and tiles with `tools/nes_sprite.py`; actual NES production additionally needs OAM, palette indexing, 8-sprites-per-scanline and emulator evaluation. Master source precedes animation batches.
