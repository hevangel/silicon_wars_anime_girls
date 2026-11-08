# Model sheet prompt template

**Output:** `characters/<id>/character_sheet.png` · landscape 3:2 (1536 x 1024 for the Compute Triad, 1920 x 1280 later)

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | The design source: a cropped poster figure, an earlier card, or a previous sheet | Identity and costume blueprint |
| Image 2 | [model_sheet_layout.png](../layout/model_sheet_layout.png), or [Intel's sheet](../../intel/character_sheet.png) | Layout only |

Intel's sheet came from the Compute Triad poster alone. AMD's came from its earlier painted card alone. Nvidia's added Intel's sheet as a layout reference. With the blank guide, the model can't borrow another character's hair, costume, or colors. Use Intel's sheet when you want its finished ornament and polish too.

Fill each `{{FIELD}}`, delete the bracketed notes, and paste the result into the character's `character_sheet.prompt.md`.

---

Create a polished landscape 3:2 anime character model sheet for {{NAME_UPPER}}, {{TITLE_UPPER}}, {{AGE_PHRASE}} in Silicon Wars. Image 1 is {{IDENTITY_SOURCE}} and the strict identity and costume blueprint. Image 2 is a layout guide ONLY: follow its arrangement of nameplate, four standing views, three close-ups, and palette strip, but do not draw its gray mannequins, placeholder bars, or empty plaques. Preserve {{FACE}}, and {{HAIR}}. Her full costume, identical in every view: {{COSTUME}}. {{VIEW_NOTES}} Put four complete standing turnarounds in a row on a pale neutral background, feet and {{TOPMOST_FEATURE}} fully in frame with comfortable outer margins: FRONT, THREE-QUARTER, SIDE, BACK, all at the same scale and baseline, with the same hairstyle, accessories, costume construction, and proportions in every angle. {{BUILD}}, about seven and a half head-heights tall. Below them, include three close-up expressions of the same face{{ALWAYS_ON}}: {{EXPR_1}}, {{EXPR_2}}, and {{EXPR_3}}, plus a small palette strip in {{PALETTE}}. Use clear restrained labels, with only the text "{{NAME_UPPER}}", "{{TITLE_UPPER}}", "FRONT", "THREE-QUARTER", "SIDE", "BACK", "{{EXPR_1}}", "{{EXPR_2}}", and "{{EXPR_3}}". Crisp high-end manga linework and detailed cel shading matching Image 1. Give the figures room to breathe and enough separation for individual crops. Keep the sheet free of other characters, scenery, {{LOGO_RULE}}, and technical marketing copy.

---

## Fields

| Field | Example (from the accepted sheets) |
|---|---|
| `{{AGE_PHRASE}}` | "an adult woman"; "a 30-year-old woman" |
| `{{IDENTITY_SOURCE}}` | "the original Compute Triad painting. Use only Intel, the crowned woman on the FAR LEFT,"; "her approved reference card" |
| `{{FACE}}` | "her poised, mature face, sapphire eyes" |
| `{{HAIR}}` | "long, voluminous flowing hair in unmistakably pale icy sky blue from roots through tips" |
| `{{COSTUME}}` | One sentence listing every garment, its color, and every accessory, head to boots |
| `{{VIEW_NOTES}}` | Items that appear only in some views. Microsoft: "In the FRONT and THREE-QUARTER views she holds a white coffee mug." Name what the BACK view must not show (a badge or pendant that hangs in front). Empty if none |
| `{{TOPMOST_FEATURE}}` | "crown tips", "hair", "ponytail", "bun" |
| `{{BUILD}}` | "Draw her tall and slender"; Nvidia: "a statuesque, visibly powerful heavyweight athlete with broad shoulders" |
| `{{ALWAYS_ON}}` | ", glasses on" for anything worn in every view; otherwise empty |
| `{{EXPR_1..3}}` | Three expressions matched to her personality. Intel: COMPOSED, STERN, SURPRISED. AMD: SMUG, FOCUSED, SURPRISED. Nvidia: CONFIDENT, FOCUSED, DEFIANT |
| `{{PALETTE}}` | "emerald, jade, charcoal and black" |
| `{{LOGO_RULE}}` | "product logos" or, when the design carries one, "logos other than her lapel pin" |

## Known failure modes

- Garbled or extra text, such as "EXPRESSALETTE:" on Microsoft's first take. Keep the label whitelist exact.
- Front-only accessories drawn on the back view.
- Short, stocky figures after a reframing pass. Keep the head-height phrase, and supply an earlier sheet as a proportion reference if it recurs.
- Crowns, buns, or boots cropped at the edge. That is why `{{TOPMOST_FEATURE}}` is named.
- If a dense costume fails in one pass, split it: turnarounds only, then an extension pass for close-ups and palette, then a reframing pass. Microsoft's dress sheet needed this.
