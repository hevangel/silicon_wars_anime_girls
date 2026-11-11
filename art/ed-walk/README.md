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
- `walkers/` — the 30 solo walking figures as generated (plain white
  background), one per character, each from her own model sheet.
- `cutouts/` — the 32 transparent figures used in the composite.
- Rebuild or adjust with `tools/build_ed_walk.py`.

## Method

- Order: roster order, grouped by faction — Silicon Kingdoms lead, the
  Grandmother Generation brings up the rear; Bell Labs rolls in her wheelchair.
- Heights (the frieze doubles as a height chart): adults 1.00, Nvidia 1.06 as
  the cast's strongest presence, the 9–10-year-old Academy kids 0.68, the
  12–13-year-olds 0.76, Arm/Qualcomm/Marvell 0.94 as 19–20-year-old young
  adults (an earlier build misread their age strings as '1'-leading and shrank
  them to kid size), the grandmothers 0.96, Bell Labs 0.80 seated.
- Figures overlap slightly, painted rear-of-march first so the front of the
  march layers on top.

## Recorded notes

- Intel and Huawei are the two figures NOT freshly generated: their walker
  generations produced no image on repeated attempts, so their parade figures
  are the SIDE views cropped from their own model sheets — true profiles,
  static stance instead of mid-stride. Regenerate-and-swap is a one-line
  change in `tools/build_ed_walk.py` whenever a fresh walker succeeds.
- Anthropic keeps her painted contact shadow (part of her generated ground
  shadow), visible against the dark backdrop. ASML's walker source also has a
  painted contact shadow under her feet.
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
