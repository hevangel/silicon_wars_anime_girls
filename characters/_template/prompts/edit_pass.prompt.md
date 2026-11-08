# Correction pass prompt template

Use this to fix one flaw in an accepted image without regenerating it: Intel's crown badge, Nvidia's leg anatomy, Microsoft's missing glasses. The image being fixed is always Image 1. Add an Image 2 only to supply something specific, such as a logo or a proportion reference, and say what it is for.

---

Edit this exact {{NAME_UPPER}} / {{TITLE_UPPER}} {{ASSET_KIND}}. Image 1 is the actual artwork to edit. {{IMAGE_2_ROLE}} Make one targeted adjustment: {{CHANGE}}. Apply it to {{SCOPE}}. Preserve the face, hair, accessories, outfit construction, art style, exact sheet arrangement, frame, palette, expressions, and every existing label in place and correctly spelled. Everything except the requested change should stay faithful to Image 1. Retain the same {{ASPECT}} composition.

---

## Fields

| Field | Example |
|---|---|
| `{{ASSET_KIND}}` | "character turnaround sheet", "12-expression sheet", "2:3 reference card" |
| `{{IMAGE_2_ROLE}}` | "Image 2 is the archived card for the logo ONLY." / "Image 2 is the earlier sheet for figure proportions ONLY." Empty if there is no Image 2 |
| `{{CHANGE}}` | Describe the result, not the defect. Nvidia: "redraw her thighs, knees and calves as naturally proportioned, strong athletic adult legs" |
| `{{SCOPE}}` | "all four full-body standing views"; "the ANGRY and SMUG cells"; "all twelve close-ups and the full-body figure on the left" |
| `{{ASPECT}}` | "landscape 3:2"; "portrait 2:3" |

Record every pass in the character's `character_sheet.prompt.md` under a "Correction history" note, including passes that didn't fully work. Microsoft's record is an example.
