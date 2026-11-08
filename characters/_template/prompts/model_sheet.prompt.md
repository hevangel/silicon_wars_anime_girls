# Model sheet prompt template

**Output:** `characters/<id>/character_sheet.png` · landscape 3:2 (1536 x 1024 for the Compute Triad, 1920 x 1280 later)

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | The design source: a cropped poster figure, an earlier card, or a previous sheet | Identity and costume blueprint |
| Image 2 | [model_sheet_layout.png](../layout/model_sheet_layout.png) | Layout and chrome only. Always this file, never another character's sheet |

Intel's sheet came from the Compute Triad poster alone. AMD's came from its earlier painted card alone. Nvidia's added Intel's sheet as a layout reference. With the blank guide, the model can't borrow another character's hair, costume, or colors. Do not substitute another sheet: the accepted sheets differ in background, frame, nameplate and logos because that part was never locked.

**Size:** 1920 x 1280 for every new sheet (the earlier 1536 x 1024 sheets stay as they are).

## Locked sheet chrome (do not edit per character)

Paste this block into every model-sheet prompt unchanged, in place of {{SHEET_CHROME_BLOCK}}.

> **SHEET CHROME (locked):** Warm off-white paper background (#F4F1EC) for the whole sheet, never gray or tinted. A thin charcoal outer frame with a fine gold inner hairline on all four sides, the same on every character. **TITLE LOCKUP (locked, identical on the model, chibi and expression sheets):** at the top left, left-aligned, exactly four elements in this order. (1) The company's real logo, about the height of the name, immediately to the left of (2) the company name in large dark serif capitals. Beneath them, (3) the character's canonical title from roster.json in smaller dark serif capitals, and (4) the sub-title "SILICON WARS" in small, letter-spaced gold-gray serif capitals, set inside the bottom gold rule (rule, text, rule) instead of on its own line. A short gold rule with a centered diamond sits above the group, and the bottom rule ends in a small gold diamond at each end. No tagline and no other text in the lockup. **Wordmark exception (locked):** if the company's logo already spells the full company name (IBM, Oracle, Intel, Google, Samsung and similar), draw only the logo, at the same visual size as the logo-plus-name pair, and do not draw the name a second time. The lockup is then logo, title, sub-title. Use a symbol-only logo (Apple, Nvidia and similar) with the name beside it as in (1) and (2). Record which form each character uses in `continuity.yaml`. Each view label sits on a small dark charcoal plaque with cream capitals and a short gold rule on each side. A thin gold divider with a small centered diamond separates the turnarounds from the close-ups. Close-ups are head-and-shoulders crops directly on the paper, not circles, bubbles or boxes. The palette strip is a row of six plain square swatches at the lower right, with no title or captions. **LOGO RULE (locked):** no company logo, emblem or brand mark except the one in the title lockup and those that are part of the costume or props described above; no other header logo, no logo in the frame, labels or palette, no watermark, tagline or marketing copy.

Fill each `{{FIELD}}`, delete the bracketed notes, and paste the result into the character's `character_sheet.prompt.md`.

---

Create a polished landscape 3:2 anime character model sheet for {{NAME_UPPER}}, {{TITLE_UPPER}}, {{AGE_PHRASE}} in Silicon Wars. Image 1 is {{IDENTITY_SOURCE}} and the strict identity and costume blueprint. Image 2 is a layout guide ONLY: follow its arrangement of nameplate, four standing views, three close-ups, and palette strip, but do not draw its gray mannequins, placeholder bars, or empty plaques. Preserve {{FACE}}, and {{HAIR}}. Her full costume, identical in every view: {{COSTUME}}. {{VIEW_NOTES}} Put four complete standing turnarounds in a row on a pale neutral background, feet and {{TOPMOST_FEATURE}} fully in frame with comfortable outer margins: FRONT, THREE-QUARTER, SIDE, BACK, all at the same scale and baseline, with the same hairstyle, accessories, costume construction, and proportions in every angle. {{BUILD}}, about seven and a half head-heights tall. Below them, include three close-up expressions of the same face{{ALWAYS_ON}}: {{EXPR_1}}, {{EXPR_2}}, and {{EXPR_3}}, plus a small palette strip in {{PALETTE}}. {{SHEET_CHROME_BLOCK}} Use only the text "{{NAME_UPPER}}" (omitted when the logo already spells it), "{{TITLE_UPPER}}", "SILICON WARS", "FRONT", "THREE-QUARTER", "SIDE", "BACK", "{{EXPR_1}}", "{{EXPR_2}}", and "{{EXPR_3}}". Crisp high-end manga linework and detailed cel shading matching Image 1. Give the figures room to breathe and enough separation for individual crops. Keep the sheet free of other characters and scenery.

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
| `{{SHEET_CHROME_BLOCK}}` | The locked SHEET CHROME and LOGO RULE paragraph above, pasted verbatim. Not a per-character field. A costume logo is allowed only if the `{{COSTUME}}` sentence names it |

## Known failure modes

- Garbled or extra text, such as "EXPRESSALETTE:" on Microsoft's first take. Keep the label whitelist exact.
- Front-only accessories drawn on the back view.
- Short, stocky figures after a reframing pass. Keep the head-height phrase, and supply an earlier sheet as a proportion reference if it recurs.
- Crowns, buns, or boots cropped at the edge. That is why `{{TOPMOST_FEATURE}}` is named.
- If a dense costume fails in one pass, split it: turnarounds only, then an extension pass for close-ups and palette, then a reframing pass. Microsoft's dress sheet needed this.
- Frame, nameplate, background and logo drift. Before 2026-11-08 these were free, so some sheets got gray backgrounds, no frame, or a big company logo header. Do not reintroduce them.
- The lockup logo is redrawn wrongly or invented. Supply the company logo as an extra input image (Image 3, used for the lockup logo only) and say so in the prompt.
