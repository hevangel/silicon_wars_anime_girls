# Chibi sheet prompt template

**Output:** `characters/<id>/chibi_sheet.png` · landscape 3:2, 1920 x 1280

Chibi sheets had no template. Each character's prompt was written by hand, so the "CHIBI" tag moved around, the sizes differed, and some sheets carried company logos. This template fixes the format on top of the model-sheet chrome.

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | `characters/<id>/character_sheet.png`, the approved model sheet | Strict identity and costume |
| Image 2 | [chibi_sheet_layout.png](../layout/chibi_sheet_layout.png) | Layout and chrome only. Always this file |

Style rules come from `bible/art_style.yaml` (`chibi`) and the `style_variants.chibi` block in the character's `continuity.yaml`.

---

Create a polished landscape 3:2 anime CHIBI character sheet for {{NAME_UPPER}}, {{TITLE_UPPER}}, {{AGE_PHRASE}} in Silicon Wars, in the chibi style variant. Image 1 is her approved model sheet and the strict identity and costume blueprint. Image 2 is a layout guide ONLY: follow its arrangement, but do not draw its gray mannequins, placeholder bars or empty plaques. Preserve her identity: {{IDENTITY_LIST}}. Render her as a super-deformed chibi: large head, tiny body, head-to-body ratio about 1:2.5, short simplified limbs, small rounded hands and feet, reduced costume segmentation that keeps every major motif, clean rounded manga linework, minimal shading, large simplified eyes. {{VIEW_NOTES}} Put four complete standing chibi turnarounds in a row: FRONT, THREE-QUARTER, SIDE, BACK, all at the same scale and baseline, feet and {{TOPMOST_FEATURE}} fully in frame. {{FRONT_POSE}} Below them, three chibi head-and-shoulders close-ups of the same face: {{EXPR_1}}, {{EXPR_2}}, and {{EXPR_3}}, plus a small palette strip in {{PALETTE}}. {{CHIBI_CHROME_BLOCK}} Use only the text "{{NAME_UPPER}}" (omitted when the logo already spells it), "{{TITLE_UPPER}}", "SILICON WARS", "CHIBI", "FRONT", "THREE-QUARTER", "SIDE", "BACK", "{{EXPR_1}}", "{{EXPR_2}}", and "{{EXPR_3}}". Keep the sheet free of other characters and scenery.

---

## Locked sheet chrome (do not edit per character)

Same as the [model sheet chrome, including the title lockup](model_sheet.prompt.md#locked-sheet-chrome-do-not-edit-per-character), plus this paragraph. Paste both as `{{CHIBI_CHROME_BLOCK}}`.

> **CHIBI TAG (locked):** a small dark charcoal plaque with cream capitals reading "CHIBI", at the top right inside the frame, in the same plaque style as the view labels. It is the only place the word appears. No other badge, sticker or banner.

## Fields

Same as the model sheet, plus:

| Field | Example |
|---|---|
| `{{IDENTITY_LIST}}` | Hair, eyes, build, every costume motif and accessory, copied from the model sheet prompt |
| `{{FRONT_POSE}}` | One cute pose for the FRONT view only, such as "The FRONT view leans forward with a mischievous grin and a tiny fist-pump." Keep THREE-QUARTER, SIDE and BACK neutral standing |

## Known failure modes

- The tag moves or is repeated. Keep the locked wording, and check there is exactly one "CHIBI".
- Realistic proportions creep back. Restate "1:2.5" and "avoid realistic anatomy".
- Costume motifs get dropped in the simplification. List them in `{{IDENTITY_LIST}}`.
