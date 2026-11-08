# Expression sheet prompt template

**Output:** `characters/<id>/expressions.png` · landscape 3:2, same size as the model sheet

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | `characters/<id>/character_sheet.png`, the current model sheet | Identity, costume, and body build |
| Image 2 | [expressions_layout.png](../layout/expressions_layout.png), or [Intel's expression sheet](../../intel/expressions.png) | Layout and acting range only |

Intel, AMD, and Nvidia used an example sheet the user attached; that file isn't saved in the repo. Google, Apple, and Microsoft used Intel's sheet in its place. The blank guide carries the same grid and labels without Intel's crown and hair.

Only the first paragraph is per-character. Keep the second and third paragraphs, the row order, and the definitions word for word: they are identical across all six accepted sheets.

---

Create a production-ready colored manga EXPRESSION SHEET for {{NAME_UPPER}}, {{TITLE_UPPER}}, in Silicon Wars, {{AGE_PHRASE}}. Image 1 is this character's current model sheet. Follow it closely for the exact facial proportions, {{EYES}}, {{ALWAYS_ON_WITH_COMMA}}hairstyle, accessories, outfit, colors and body build. Image 2 is a layout and acting reference only. Use its one-full-body-plus-twelve-faces structure and range of expressions, but do not draw its gray mannequins or placeholder bars. {{IDENTITY_SENTENCE}} Palette accents are {{ACCENTS}}. {{DEMEANOR}}

Compose a landscape reference sheet on a plain warm off-white background with a tasteful thin border in the character's accent colors. Reserve the left 30 percent for the two-line nameplate "{{NAME_UPPER}}" / "{{TITLE_UPPER}}" and exactly one complete standing {{FULL_BODY_POSE}}, with all hair and {{FOOTWEAR}} inside the margin. On the right, place exactly 12 separately bordered head-and-shoulder cells in a precise 3-column, 4-row grid, with identical camera angle, head scale and lighting{{ALWAYS_ON_CELLS}}. Leave room for hair and head accessories in each cell. Keep character identity and outfit details fixed, changing only facial acting. Each cell has its single legible English label above the face. The complete exact row order is:

NEUTRAL | SMILING | EYES CLOSED
ANGRY | CRYING | SURPRISED
SMUG | FLUSTERED | SERIOUS
BLUSHING | EXCITED | OMINOUS

Distinguish all 12 clearly. Neutral is relaxed with open eyes; smiling is warm; eyes closed is calmly resting; angry has tight brows and an open sharp retort; crying has visible tears; surprised has wide eyes and a small open mouth; smug has one corner of the mouth raised; flustered has anxious brows and a small sweat drop; serious is alert with a level mouth; blushing is visibly flushed with a shy look; excited is an energetic delighted expression with bright eyes; ominous is quiet and shadowed, with a steady intimidating gaze. Use detailed colored anime linework and cel shading that match Image 1. Use only the nameplate and 12 exact English labels, with a crisp simple typeface. Keep every cell and label separate and readable. No other characters, layout panels, {{LOGO_RULE}}, watermark, or scenery.

---

## Fields

| Field | Example |
|---|---|
| `{{AGE_PHRASE}}` | "an adult woman"; "a 30-year-old woman" |
| `{{EYES}}` | "emerald eyes" |
| `{{ALWAYS_ON_WITH_COMMA}}` | "black-rimmed rectangular glasses worn in every cell, " or empty |
| `{{IDENTITY_SENTENCE}}` | One sentence repeating the model sheet's identity and costume, head to boots. AMD: "Adult woman with a vivid red high ponytail and braided lock, amber eyes, gold drop earrings, black-and-red headphones around her neck, cropped crimson-and-black tactical jacket, black cargo trousers with gold hardware, fingerless gloves and heavy boots." Add explicit negatives for drift you've seen ("NO sunglasses and NO headphones anywhere on the sheet") |
| `{{ACCENTS}}` | "crimson and warm gold" |
| `{{DEMEANOR}}` | Default demeanor plus how anger, smugness, excitement, and ominous play for her. Intel: "Her default demeanor is composed and regal. In anger she issues a sharp command; in smugness she lifts one brow; in excitement she gives a rare delighted grin." |
| `{{FULL_BODY_POSE}}` | "front or slight three-quarter figure in a neutral pose"; Microsoft: "figure in a composed three-quarter pose, holding her white coffee mug" |
| `{{FOOTWEAR}}` | "boots", "shoes", "pumps" |
| `{{ALWAYS_ON_CELLS}}` | ", glasses on in every cell" or empty |
| `{{LOGO_RULE}}` | "logos" or "logos besides her costume pins and mug logo" |

## Known failure modes

- Accessories that are always worn get dropped from some cells. Microsoft's first take lost her glasses in 7 of 12 cells. Repeat the item in `{{ALWAYS_ON_*}}` and check every cell.
- Labels misspelled or out of order. Compare against the row order above before accepting.
- Fix individual cells with [edit_pass.prompt.md](edit_pass.prompt.md) rather than regenerating the sheet.
