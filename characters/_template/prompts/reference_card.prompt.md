# Reference card prompt template

**Output:** `characters/<id>/reference_card.jpg` · portrait 2:3 (1024 x 1536 for the Compute Triad, 1280 x 1920 later)

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | `characters/<id>/character_sheet.png`, the current model sheet | Strict identity, costume, and proportions |
| Image 2 | [reference_card_layout.png](../layout/reference_card_layout.png), or [Intel's card](../../intel/reference_card.jpg) / [AMD's card](../../amd/reference_card.jpg) | Framing, border, and nameplate only |

AMD's card used Intel's card for framing, and Nvidia's used AMD's. A card from another character brings along its finish and border style, but also its palette. The blank guide brings only the structure. To revise an existing card, make the old card Image 1 and the model sheet Image 2, as Nvidia's final card did.

---

Create a polished portrait-oriented 2:3 anime character reference card for {{NAME_UPPER}}, {{TITLE_UPPER}}, {{AGE_PHRASE}} in Silicon Wars. Image 1 is her model sheet and the only reference for the character's identity and clothing. Match {{IDENTITY_LIST}}. Image 2 is a framing reference only: match its large portrait, narrow decorative frame and bottom nameplate, but do not draw its gray mannequin or placeholder bars. Show a large three-quarter portrait from {{CROP}}, with {{FRAMING_PRIORITY}} well framed, {{EXPRESSION}}, and {{PROP_OR_FEAT}}. The character occupies most of the card, against {{SETTING}}. Use a narrow {{BORDER_COLORS}} border and a clean bottom nameplate. Render exactly two lines in the nameplate: "{{NAME_UPPER}}" and "{{TITLE_UPPER}}". Keep the rest of the card free of {{LOGO_RULE}}, watermarks, marketing and additional text. Match the model sheet's precise manga linework and detailed cel shading.

---

## Fields

| Field | Example |
|---|---|
| `{{IDENTITY_LIST}}` | Eyes, hair, build, every costume piece and accessory, copied from the model sheet prompt |
| `{{CROP}}` | "about the hips up" (Intel, AMD); "the knees up, at a low angle" (Nvidia) |
| `{{FRAMING_PRIORITY}}` | "the crown tips fully visible"; "the ponytail and face" |
| `{{EXPRESSION}}` | "a composed commanding gaze"; "a bold confident smirk" |
| `{{PROP_OR_FEAT}}` | The one signature prop or power. Intel: "a gloved hand holding a small wafer-shaped heirloom low in the frame." For a held object, describe the contact (palm, fingers, which shoulder) |
| `{{SETTING}}` | "understated blue circuitry and dark architecture"; "understated crimson circuitry in a dark fabrication lab" |
| `{{BORDER_COLORS}}` | "elegant blue-and-gold"; "red, charcoal and gold" |
| `{{LOGO_RULE}}` | "company logos" or "branding outside the necklace" |

## Known failure modes

- Hands and held props need explicit anatomy. Nvidia's I-beam took a second pass that described exactly where the palm, fingers, and shoulder touch the beam.
- Hair color drifts toward the background lighting. Restate it ("keep the hair visibly light blue").
- The caption title must be the canonical one from `roster.json`; Microsoft's old card had a stale title.
