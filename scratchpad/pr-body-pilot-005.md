Adds Pilot 005, a single 4:3 swimsuit panel: Intel, AMD and Nvidia play beach volleyball, AMD and Intel both go for the same ball, and neither reaches it.

![Beach Volleyball](https://raw.githubusercontent.com/hevangel/silicon_wars_anime_girls/art/pilot-005-beach-volleyball/chapters/pilot-005/pages/page-001/final/page-001.png)

## Before / after

This is new art, so there is no earlier render of the scene. The "before" side is the design reference the panel was drawn from: one sheet assembled out of the three character sheets (three-quarter turnarounds) with three expression heads lifted from each expression sheet underneath, so faces, hair, build and expression language come from the approved art rather than prose.

![Cast reference sheet](https://raw.githubusercontent.com/hevangel/silicon_wars_anime_girls/art/pilot-005-beach-volleyball/chapters/pilot-005/pages/page-001/refs/cast-reference.jpg)

One take was rejected and is described in the manifest: it put shoes on AMD and Nvidia, duplicated the volleyball, and ran the net behind all three so the court sides were unreadable.

## Reading order

Right to left along the top, then down:

1. **Nvidia** — "Two against one. Still not close."
2. **Intel** — "Not the face!"
3. **AMD** — "Mine! MINE!"

Balloons were measured against the renderer's wrap width and checked for collisions; none covers a face. Lettering avoids em dashes and ellipsis glyphs, which the renderer font cannot set.

## Design continuity

- **Intel** — long light-blue waves, sapphire-and-gold crown, pale blue eyes, tall elegant build; royal-blue one-piece with white side panels and gold trim.
- **AMD** — red high ponytail with braided strands and gold beads, amber eyes, lean build; red-and-black athletic two-piece, thigh bands, choker with badge.
- **Nvidia** — thick emerald braid, goggles pushed up on her head, green eyes, strong shoulders; black one-piece with neon-green circuit traces and green wristbands.

Swimsuits carry over from the [pilot-003 beach concept](https://github.com/hevangel/silicon_wars_anime_girls/tree/main/chapters/pilot-003) rather than inventing a new wardrobe. All three are barefoot with no shoes, sandals or gloves anywhere; AMD and Nvidia show full soles and toes.

## Files

- `chapters/pilot-005/` — chapter record, script, `qa.yaml`, render plan, and `pages/page-001/` with storyboard, panel brief, lettering, generation manifest, cast reference, art and final page.
- `chapters/README.md` — index entry.

Art and lettering stay separate: the render is text-free and every balloon comes from `lettering.yaml` through `tools/render_pilot.py`, using the shared `layouts/single-panel-4x3.yaml` (2240 x 1640 panel on a 2400 x 1800 page).

```sh
python tools/render_pilot.py --plan chapters/pilot-005/render-page-001.yaml --check
python tools/render_pilot.py --plan chapters/pilot-005/render-page-001.yaml
```

## Review notes

- Intel's foot reaches the bottom edge of the generated art, so her toes are partly cut by the frame. The centered fit was chosen over a shifted crop that clipped Nvidia's raised hand; logged in `qa.yaml`.
- Intel carries a thin black neck band that is not on her sheet. It reads as a swimsuit strap at page size and is listed in the checklist rather than edited.
- The generator was told to avoid type logos, so no brand wordmark is letter-accurate in this panel, and none is claimed.
- PR #117 already adds a different beach-volleyball panel as Pilot 003 page 003. This one is an independent build made specifically from the character and expression sheets; merge whichever reading you prefer and I will retire the other.
