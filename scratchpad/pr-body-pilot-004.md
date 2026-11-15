Adds Pilot 004, a single 4:3 comedy panel: OpenAI kneels on the floor of a memory warehouse and begs Micron, Samsung and SK hynix for allocation. Three polite refusals, one desperate plea.

![The Memory Plea](https://raw.githubusercontent.com/hevangel/silicon_wars_anime_girls/art/openai-memory-plea/chapters/pilot-004/pages/page-001/final/page-001.png)

## Before / after

This is new art, so there is no previous render of the scene to compare. The "before" side is the source identity art; the panel was drawn from a single composite of the four painted reference cards, cropped above their name plates so no poster chrome leaks into the frame:

![Cast reference sheet](https://raw.githubusercontent.com/hevangel/silicon_wars_anime_girls/art/openai-memory-plea/chapters/pilot-004/pages/page-001/refs/cast-reference.jpg)

Three takes were generated. The two rejected ones are described in the manifest with their failure modes (child reading as cheering; suppliers losing the height advantage). Only the accepted render is retained, matching Pilot 001 practice.

## Reading order

Right to left, at the reading size of the assembled page:

1. **SK hynix** — "Every stack is spoken for."
2. **Samsung** — "All of it reserved, darling."
3. **Micron** — "Contract first, partner."
4. **OpenAI** — "I'll take NAND! I'll take DRAM! Just give me SOMETHING!"

Balloons were measured against the renderer's wrap width and checked for collisions before assembly; no balloon covers a face. Lettering avoids em dashes and ellipsis glyphs, which the renderer font cannot set.

## Costume continuity

- **OpenAI** — silver-white side ponytail, navy knot ribbon with the white knot, white sailor blouse, teal tie, navy skirt, robot backpack.
- **Micron** — cream hat with iridescent band, honey-blonde braid, fringed cream vest with the chip-shaped star, violet neckerchief, holstered DIMM, glowing lasso.
- **Samsung** — near-black waist-length hair with sapphire ribbons, white and ice-silver hanbok, circuit hem, SAMSUNG sash, gadget norigae.
- **SK hynix** — violet-black updo with gold pin and crystal cubes, red-orange jeogori, red-to-charcoal column skirt with stacked hem, copper norigae, glowing HBM stack.

## Files

- `chapters/pilot-004/` — chapter record, script, `qa.yaml`, render plan, and `pages/page-001/` with the storyboard, panel brief, lettering, generation manifest, cast reference, art, and final page.
- `layouts/single-panel-4x3.yaml` — 2000 × 1500 panel on a 2080 × 1560 page, so the deliverable is exactly 4:3.
- `layouts/README.md`, `chapters/README.md` — index entries for the new layout and chapter.

Art and lettering stay separate: the render is text-free and every balloon comes from `lettering.yaml` through `tools/render_pilot.py`, so a dialogue change never requires regenerating the art.

```sh
python tools/render_pilot.py --plan chapters/pilot-004/render-page-001.yaml --check
python tools/render_pilot.py --plan chapters/pilot-004/render-page-001.yaml
```

## Review notes

- Sash and shirt wordmarks read correctly at page size but are not letter-accurate at 1:1. Flagged in `qa.yaml`; say if you want a targeted edit before merge.
- The scarcity is played as fiction; no real product or performance claims.
- Pillow version used for assembly is recorded in the manifest.
