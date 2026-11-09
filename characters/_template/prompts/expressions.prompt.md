# Expression sheet prompt template

**Output:** `characters/<id>/expressions.png` · landscape 3:2, same size as the model sheet

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | `characters/<id>/character_sheet.png`, the current model sheet | Identity, costume, and body build |
| Image 2 | [expressions_layout.png](../layout/expressions_layout.png) | Layout, chrome and acting range only. Always this file |

Intel, AMD, and Nvidia used an example sheet the user attached; that file isn't saved in the repo. Google, Apple, and Microsoft used Intel's sheet in its place. The blank guide carries the same grid and labels without Intel's crown and hair. Do not substitute another sheet.

**Size:** 1920 x 1280 for every new sheet.

## Locked sheet chrome (do not edit per character)

Paste this block into every expression-sheet prompt unchanged, in place of {{SHEET_CHROME_BLOCK}}.

> **SHEET CHROME (locked):** Plain warm off-white paper background (#F4F1EC). A thin charcoal outer frame with a fine gold inner hairline, identical for every character; the character's accent colors appear only in the character, never in the frame. **TITLE LOCKUP (locked, identical on the model, chibi and expression sheets):** at the top left, left-aligned, exactly four elements in this order. (1) The company's real logo, about the height of the name, immediately to the left of (2) the company name in large dark serif capitals. Beneath them, (3) the character's canonical title from roster.json in smaller dark serif capitals, and (4) the sub-title "SILICON WARS" in small, letter-spaced gold-gray serif capitals, set inside the bottom gold rule (rule, text, rule) instead of on its own line. A short gold rule with a centered diamond sits above the group, and the bottom rule ends in a small gold diamond at each end. No tagline and no other text in the lockup. **Wordmark exception (locked):** if the company's logo already spells the full company name (IBM, Oracle, Intel, Google, Samsung and similar), draw only the logo, at the same visual size as the logo-plus-name pair, and do not draw the name a second time. The lockup is then logo, title, sub-title. Use a symbol-only logo (Apple, Nvidia and similar) with the name beside it as in (1) and (2). Record which form each character uses in `continuity.yaml`. It sits at the top of the left column. **EXPRESSION LABEL BOX (locked):** each of the 12 cells is a square-cornered rectangle with a thin gold border and a pale cream fill (#FAF8F4). Its label sits in a dark charcoal (#3A3D44) rounded-corner plaque with a thin gold outline. All 12 plaques are the same size, about 60 percent of the cell width and one-eighth of the cell height, centered horizontally on the cell's top edge so the cell border passes behind the plaque. The label is one line of bold cream serif capitals, centered, at the same size in every plaque. Labels never sit on the face, on bare paper, or in an unfilled box, and no plaque has an icon, color accent, shadow or different width. **LOGO RULE (locked):** no company logo, emblem or brand mark except the one in the title lockup and those that are part of the costume or props already on the model sheet; no other header logo, no watermark, tagline or marketing copy. **ON-CHARACTER LOGO (required):** Give the character at least one recognizable company logo or wordmark on a garment or worn accessory. Use the real mark or the character's approved period version. Preserve its exact design, color, side, and placement. Render it in the main figure and each view where that part of the outfit is visible. Use the angle and crop to show it on the card and on the expression sheet's standing figure. A header mark or a logo on a detached prop does not satisfy this requirement.

Only the first paragraph is per-character. Keep the second and third paragraphs, the row order, and the definitions word for word: they are identical across all six accepted sheets.

---

Create a production-ready colored manga EXPRESSION SHEET for {{NAME_UPPER}}, {{TITLE_UPPER}}, in Silicon Wars, {{AGE_PHRASE}}. Image 1 is this character's current model sheet. Follow it closely for the exact facial proportions, {{EYES}}, {{ALWAYS_ON_WITH_COMMA}}hairstyle, accessories, outfit, colors and body build. Image 2 is a layout and acting reference only. Use its one-full-body-plus-twelve-faces structure and range of expressions, but do not draw its gray mannequins or placeholder bars. {{IDENTITY_SENTENCE}} Palette accents are {{ACCENTS}}. {{DEMEANOR}}

Compose a landscape reference sheet using the locked chrome. {{SHEET_CHROME_BLOCK}} Reserve the left 30 percent for the title lockup (logo, "{{NAME_UPPER}}" unless the logo already spells it, "{{TITLE_UPPER}}", "SILICON WARS") and exactly one complete standing {{FULL_BODY_POSE}}, with all hair and {{FOOTWEAR}} inside the margin. On the right, place exactly 12 separately bordered head-and-shoulder cells in a precise 3-column, 4-row grid, with identical camera angle, head scale and lighting{{ALWAYS_ON_CELLS}}. Leave room for hair and head accessories in each cell. Keep character identity and outfit details fixed, changing only facial acting. Preserve the approved company mark in each crop that includes its placement. Each cell has its single legible English label above the face. The complete exact row order is:

NEUTRAL | SMILING | EYES CLOSED
ANGRY | CRYING | SURPRISED
SMUG | FLUSTERED | SERIOUS
BLUSHING | EXCITED | OMINOUS

Distinguish all 12 clearly. Neutral is relaxed with open eyes; smiling is warm; eyes closed is calmly resting; angry has tight brows and an open sharp retort; crying has visible tears; surprised has wide eyes and a small open mouth; smug has one corner of the mouth raised; flustered has anxious brows and a small sweat drop; serious is alert with a level mouth; blushing is visibly flushed with a shy look; excited is an energetic delighted expression with bright eyes; ominous is quiet and shadowed, with a steady intimidating gaze. Use detailed colored anime linework and cel shading that match Image 1. Use only the title lockup and 12 exact English labels. Keep every cell and label separate and readable. No other characters, layout panels or scenery.

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
| `{{SHEET_CHROME_BLOCK}}` | The locked SHEET CHROME and LOGO RULE paragraph above, pasted verbatim. Not a per-character field |

## Known failure modes

- Accessories that are always worn get dropped from some cells. Microsoft's first take lost her glasses in 7 of 12 cells. Repeat the item in `{{ALWAYS_ON_*}}` and check every cell.
- Labels misspelled or out of order. Compare against the row order above before accepting.
- Fix individual cells with [edit_pass.prompt.md](edit_pass.prompt.md) rather than regenerating the sheet.
- Label box drift. Plaque color, shape and width varied between sheets (plain text, colored pills, different widths). Check that all 12 plaques match the locked box.
- Border color, nameplate and logo drift. The border used to follow the character's accent colors and the logo rule was free, which produced red, gold and multicolor frames and logo headers. Both are now locked.
- The lockup logo is redrawn wrongly or invented. Supply the company logo as an extra input image (Image 3, used for the lockup logo only).
