# The Anime ED Walk — full-cast parade

A processional frieze (パレード構図) of all 32 Silicon Wars characters marching
right-to-left — the forward direction in Japanese visual grammar — on one flat
ground plane over a plain white background (the figures' own source field, so
the cutouts sit naturally), built with the modular compositing pipeline rather
than a single crowd generation, so no character's traits bleed into another's.

![The ED Walk](ed-walk-full.png)

## Files

- `ed-walk-full.png` — the full panorama (21602x2019 after height correction).
- `ed-walk-slice-1..6.png` — seamless segments cut at figure boundaries, for
  X/Facebook carousels that stitch into the continuous parade:
  1 Intel–Apple · 2 Meta–Hugging Face · 3 Mistral–Micron ·
  4 SK hynix–Huawei · 5 Cerebras–Bell Labs · 6 Fairchild–Xerox PARC.
- `walkers/` — the 32 solo walking figures as generated (plain white
  background), one per character, each from her own model sheet.
- `cutouts/` — the 32 transparent figures used in the composite.
- Rebuild or adjust with `tools/build_ed_walk.py`.

## Method

- Order: roster order, grouped by faction — Silicon Kingdoms lead, the
  Grandmother Generation brings up the rear; Bell Labs rolls in her wheelchair.
- Heights: `characters/roster.json` gives barefoot standing stature.
  `height-calibration.json` records inspected anatomical crown and supporting
  sole landmarks, estimated footwear lifts, and source-cutout hashes. The
  compositor uses 1500 pixels per 168 cm for this span, preserving aspect ratio;
  headwear and props extend beyond it instead of shrinking the body. All
  supporting soles share a ground plane; shadows may extend below it.
  Bell Labs retains a separately specified 134.85 cm seated crown-to-floor
  span, an art-directed pose estimate rather than a measured standing ratio.
  Source changes require reinspecting the landmarks. The canvas grows to
  accommodate crowns and hats without clipping.
- `ed-walk.render.json` records the roster, calibration, builder and cutout
  hashes, each figure's placement/scale, output size and six slice boundaries.
- [Height-correction review](reviews/height-correction/REVIEW.md) contains the
  previous heights, before/after comparison art and verification notes.
- Figures overlap slightly, painted rear-of-march first so the front of the
  march layers on top.

## Recorded notes

- Height correction (2026-11-14): reviewed all 32 cutouts. Replaced the
  entire-cutout bounding-box scaling with crown/sole calibration. Corrected
  the five elementary-school characters from 100–107 cm to 130–140 cm and
  the two middle-school characters from 116–118 cm to 150–151 cm. Adult and
  elder canonical heights remain unchanged. Existing walkers, cutouts,
  costumes, direction and lettering were preserved. Rebuilt the full panorama,
  all six slices and the website derivative. These are art-direction choices
  grounded in the character profiles, not heights recoverable from pixels.

- V2 regeneration (2026-11-11): all 32 walkers were regenerated with
  scale and direction in the prompt itself — each prompt states her
  canonical height_cm and her proportions in heads (elementary kids
  about 4.5 heads with true child proportions, Arm petite at 5.5,
  adults 6.5–7), and requires a STRICT side profile facing left (face
  in profile, both feet pointing left, no three-quarter view, no
  looking back at the viewer). A zoom audit of the v2 cutouts finds
  all 32 striding or rolling left in true profile, and every printed
  logo and text reads correctly — no mirror flips anywhere in v2.
  (Microsoft's batch attempt returned no image; a fresh attempt
  succeeded. Amazon's v2 take was then caught at review with her
  upper body twisted 180 degrees against her legs — head and torso
  facing right while her hips and feet walked left — and was
  regenerated with the whole body aligned in one left-facing
  profile; verified in slice 2.) The v1 notes below are kept as
  build history.
- Intel and Huawei initially produced no image with the standard walker
  prompt. A text-combination test found the fix: scrub the brand name from
  the prompt and explicitly require plain unmarked panels with no text,
  logo or emblem — all six tested combinations (full sheet reference /
  text-only / cropped-figure reference, for both characters) then succeeded.
  Their filed walkers are the full-sheet-reference generations from that
  test, so Intel marches without her skirt logo and Huawei without her
  shoulder-armor logo, by design. (Earlier builds used SIDE views cropped
  from their model sheets as stand-ins.)
- V1 history: Anthropic and ASML kept painted contact shadows; AMD's
  walker re-styled her jacket off-shoulder with a crop top (a take
  Horace saw in the proof of concept); eleven v1 walkers came out
  stepping toward frame right and were stored mirror-flipped, which
  reversed their small printed logos. All superseded by the v2
  regeneration above. (OpenAI's v2 walker keeps a faint painted
  contact shadow.)
- The backdrop is a plain white field with a single ground line (switched
  from the first build's dark ED field at review).

Status: review draft, human approval pending.
