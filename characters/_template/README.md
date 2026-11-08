# Character template

Templates for a character's written profile and for the three design assets each main character gets: a **model sheet**, a **reference card**, and an **expression sheet**. They are built from how [Intel](../intel/character_sheet.prompt.md), [AMD](../amd/character_sheet.prompt.md), and [Nvidia](../nvidia/character_sheet.prompt.md) were generated, with fixes learned from [Microsoft](../microsoft/character_sheet.prompt.md). This folder is not a character, and it is not listed in the roster.

## Contents

| File | Use |
|---|---|
| [profile.md](profile.md) | Character profile (README): short roster fields plus character depth |
| [prompts/model_sheet.prompt.md](prompts/model_sheet.prompt.md) | Four-view turnaround, three close-ups, palette |
| [prompts/reference_card.prompt.md](prompts/reference_card.prompt.md) | 2:3 painted portrait with a two-line nameplate |
| [prompts/expressions.prompt.md](prompts/expressions.prompt.md) | One full body plus 12 labeled faces |
| [prompts/edit_pass.prompt.md](prompts/edit_pass.prompt.md) | Targeted correction of an accepted image |
| [layout/](layout/) | Blank layout guides to pass as Image 2 (see below) |
| [character_sheet.prompt.md](character_sheet.prompt.md) | Skeleton of the generation record |
| [continuity.yaml](continuity.yaml) | Skeleton of the continuity lock |

### Layout guides

| Guide | Size | Matches |
|---|---|---|
| ![Model sheet layout](layout/model_sheet_layout.png) [model_sheet_layout.png](layout/model_sheet_layout.png) | 1536 x 1024 | [Intel sheet](../intel/character_sheet.png) |
| ![Expression sheet layout](layout/expressions_layout.png) [expressions_layout.png](layout/expressions_layout.png) | 1536 x 1024 | [Intel expressions](../intel/expressions.png) |
| ![Reference card layout](layout/reference_card_layout.png) [reference_card_layout.png](layout/reference_card_layout.png) | 1024 x 1536 | [AMD card](../amd/reference_card.jpg) |

The guides use gray mannequins drawn at about 7.5 head-heights, empty nameplates, and neutral charcoal and gold trim. They pass on structure without another character's face, costume, or palette. Fixed labels (view names and the 12 expressions) are printed; labels that vary per character are left as blank plaques for the prompt to fill. To change a guide, edit [tools/make_character_template_layouts.py](../../tools/make_character_template_layouts.py) and run `py tools/make_character_template_layouts.py` rather than editing the PNGs.

Intel's finished sheets remain a valid Image 2 when you want their polish and ornament. They also tend to bring Intel's look along with them.

## Workflow

Generate the assets in this order, because each one is the identity input for the next:

1. **Model sheet.** Image 1 is the design source: a figure cropped from an archived poster, or the character's existing card. Image 2 is the model sheet guide. This sheet becomes the identity reference for everything after it.
2. **Reference card.** Image 1 is the model sheet; Image 2 is the card guide.
3. **Expression sheet.** Image 1 is the model sheet; Image 2 is the expression guide.
4. **Correction passes**, one flaw at a time, with the edit-pass template.

When the design source is a painted card that has already been approved, as with Microsoft and Google, revise the card first. Then build the model sheet from it.

## Writing the profile

[profile.md](profile.md) becomes the character's `README.md`. Its short fields mirror [roster.json](../roster.json). The **Character depth** sections cover look and presence, core contradiction, personality, background, company culture, brand image, relationships, dependencies, private side, voice samples, Season 1 arc, and how her power works in the story. The eight characters with model sheets are filled-in examples, starting with [Intel](../intel/README.md).

- Read the [series bible](../../bible/story_bible.md) first: tone, the interdependence power system, and the three artistic rules.
- Build the background from documented company history, culture, and brand image. Refer to real founders and executives by role, never by name, and don't invent product specs or numbers.
- Describe only what the approved art shows. Characters without a model sheet are draft stand-ins and keep their draft text until their sheet is made.
- Mirror every relationship in the other character's profile.

## Setting up a character

1. Copy `character_sheet.prompt.md` and `continuity.yaml` into `characters/<id>/` and fill in the `{{FIELDS}}`. Take the name, title, and design from the character's `README.md`, `art_prompt.md`, and [roster.json](../roster.json).
2. Fill each prompt template and paste the exact prompt text that was sent into the record, along with the input links.
3. Save outputs as `character_sheet.png`, `reference_card.jpg`, and `expressions.png` in the character folder. Don't overwrite files under `scratchpad/originals/`.
4. Before accepting each image, check it at reading size:
   - Every label is spelled correctly and in order, and there is no extra text.
   - Accessories that are always worn appear in every view and every cell.
   - Front-only items are absent from the back view.
   - Hair, headwear, and footwear are inside the frame.
   - Proportions match between the turnarounds and the card.
5. Update the character's README asset links and the artwork line in [INDEX.md](../INDEX.md).
6. Open a PR from a branch, with before/after images.
