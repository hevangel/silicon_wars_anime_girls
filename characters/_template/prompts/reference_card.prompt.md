# Reference card prompt template

**Output:** `characters/<id>/reference_card.jpg` · portrait 2:3 (1024 x 1536 for the Compute Triad, 1280 x 1920 later)

**Inputs**

| Image | File | Role |
|---|---|---|
| Image 1 | `characters/<id>/character_sheet.png`, the current model sheet | Strict identity, costume, and proportions |
| Image 2 | [reference_card_layout.png](../layout/reference_card_layout.png) (chrome source: [reference_card_chrome.svg](../layout/reference_card_chrome.svg)) | Frame and nameplate only. Always this file, never another character's card |

Always use the blank guide as Image 2. Another character's card brings its palette and finish along with its border, which is how the cards drifted apart. To revise an existing card, make the old card Image 1 and the model sheet Image 2, as Nvidia's final card did, and keep the locked chrome text below in the prompt.

## Locked card chrome (do not edit per character)

Paste this block into every card prompt unchanged. Only the character fields below vary. The border is the same gold for every character; a character's color goes in the scene and lighting, not in the frame.

> **CHROME (locked):** Match Image 2's frame and nameplate exactly. Frame: a thin gold outer border with a fine darker-gold inner hairline, one small gold diamond at top center, uniform on all four sides, with no art crossing it. Nameplate: a dark charcoal hexagon-ended plate across the bottom with a thin gold outline, a gold diamond at each end and one centered below it, holding exactly two centered lines of serif capitals in cream: the name large, the title smaller between two short gold rules. **LOGO RULE (locked):** no company logo, emblem or brand mark anywhere outside the character's own costume and props as described in the model sheet. None in the frame, none in the nameplate, none as a header, and no watermark, tagline, banner, profile panel or any display text beyond the two nameplate lines. A wordmark embroidered on the character is part of the costume. **ON-CHARACTER LOGO (required):** Give the character at least one recognizable company logo or wordmark on a garment or worn accessory. Use the real mark or the character's approved period version. Preserve its exact design, color, side, and placement. Render it in the main figure and each view where that part of the outfit is visible. Use the angle and crop to show it on the card and on the expression sheet's standing figure. A header mark or a logo on a detached prop does not satisfy this requirement.

---

Create a polished portrait-oriented 2:3 anime character reference card for {{NAME_UPPER}}, {{TITLE_UPPER}}, {{AGE_PHRASE}} in Silicon Wars. Image 1 is her model sheet and the only reference for the character's identity and clothing. Match {{IDENTITY_LIST}}. Image 2 is a framing reference only: match its frame and bottom nameplate, but do not draw its gray mannequin or placeholder bars. Show a large three-quarter portrait from {{CROP}}, with {{FRAMING_PRIORITY}} well framed, {{EXPRESSION}}, and {{PROP_OR_FEAT}}. The character occupies most of the card, against {{SETTING}}. {{CHROME_BLOCK}} Render exactly two lines in the nameplate: "{{NAME_UPPER}}" and "{{TITLE_UPPER}}". Match the model sheet's precise manga linework and detailed cel shading.

---

## Fields

| Field | Example |
|---|---|
| `{{IDENTITY_LIST}}` | Eyes, hair, build, every costume piece and accessory, and the company mark with its placement, copied from the model sheet prompt |
| `{{CROP}}` | "about the hips up" (Intel, AMD); "the knees up, at a low angle" (Nvidia) |
| `{{FRAMING_PRIORITY}}` | "the crown tips fully visible"; "the ponytail and face" |
| `{{EXPRESSION}}` | "a composed commanding gaze"; "a bold confident smirk" |
| `{{PROP_OR_FEAT}}` | The one signature prop or power. Intel: "a gloved hand holding a small wafer-shaped heirloom low in the frame." For a held object, describe the contact (palm, fingers, which shoulder) |
| `{{SETTING}}` | "understated blue circuitry and dark architecture"; "understated crimson circuitry in a dark fabrication lab" |
| `{{CHROME_BLOCK}}` | The locked CHROME and LOGO RULE paragraph above, pasted verbatim. Not a per-character field |

## Known failure modes

- Hands and held props need explicit anatomy. Nvidia's I-beam took a second pass that described exactly where the palm, fingers, and shoulder touch the beam.
- Hair color drifts toward the background lighting. Restate it ("keep the hair visibly light blue").
- The caption title must be the canonical one from `roster.json`; Microsoft's old card had a stale title.
- Border, nameplate, and logo drift. Before 2026-11-08 the border color, nameplate style and logo rule were free per-character fields, so cards ended up with different frames, tagline plates and logos in the plate. Do not reintroduce them; record any intentional exception (such as a tagline) in the character's `character_sheet.prompt.md`.
