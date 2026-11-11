# The Anime ED Walk — full-cast parade

A processional frieze (パレード構図) of all 32 Silicon Wars characters marching
right-to-left — the forward direction in Japanese visual grammar — on one flat
ground plane over a plain white background (the figures' own source field, so
the cutouts sit naturally), built with the modular compositing pipeline rather
than a single crowd generation, so no character's traits bleed into another's.

![The ED Walk](ed-walk-full.png)

## Files

- `ed-walk-full.png` — the full panorama (about 20096x1820).
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
- Heights (the frieze doubles as a height chart; the portfolio itself has
  no height data — roster.json carries only coarse age labels — so the
  ladder is set explicitly per character in tools/build_ed_walk.py):
  adults 1.00, Nvidia 1.06 as the cast's strongest presence, the AI Lab
  elementary kids (Anthropic, OpenAI, xAI, Mistral, DeepSeek) 0.55, the
  middle-schoolers (Hugging Face, Cerebras) 0.66, Arm/Qualcomm/Marvell
  0.94 as 19–20-year-old young adults, the grandmothers 0.96, Bell Labs
  0.80 seated. (The first build's kids at 0.68 read too big at review,
  and an age-string substring bug had shrunk the young adults to kid
  size; both are fixed.)
- Figures overlap slightly, painted rear-of-march first so the front of the
  march layers on top.

## Recorded notes

- Intel and Huawei initially produced no image with the standard walker
  prompt. A text-combination test found the fix: scrub the brand name from
  the prompt and explicitly require plain unmarked panels with no text,
  logo or emblem — all six tested combinations (full sheet reference /
  text-only / cropped-figure reference, for both characters) then succeeded.
  Their filed walkers are the full-sheet-reference generations from that
  test, so Intel marches without her skirt logo and Huawei without her
  shoulder-armor logo, by design. (Earlier builds used SIDE views cropped
  from their model sheets as stand-ins.)
- Anthropic keeps her painted contact shadow (part of her generated ground
  shadow). ASML's walker source also has a painted contact shadow under
  her feet.
- AMD's walker re-styles her jacket off-shoulder with a crop top (a take
  Horace saw in the proof of concept).
- Direction pass: eleven generated walkers came out stepping toward frame
  right despite the left-facing brief — Samsung, Oracle, Xerox PARC, OpenAI,
  Anthropic, Meta, Google, Apple, Mistral, DeepSeek, Sun Microsystems. Their
  walker and cutout files are stored mirror-flipped so the whole parade
  strides left; on those eleven, small printed logos and text render reversed
  (Google's G, Anthropic's CLASS MONITOR armband, Samsung's sash patch,
  Oracle's name tag, Xerox's badge, Sun's Java mug).
- The backdrop is a plain white field with a single ground line (switched
  from the first build's dark ED field at review).

Status: review draft, human approval pending.
