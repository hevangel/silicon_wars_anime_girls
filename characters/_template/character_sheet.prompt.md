# {{NAME}} model sheet, expression sheet, and reference card generation record

All illustrations were generated with {{GENERATOR}}.

## Model sheet

- Output [Illustrated model sheet](character_sheet.png) ({{WIDTH}} x {{HEIGHT}})
- Input Image 1: [{{SOURCE_LABEL}}]({{SOURCE_LINK}}), the design source
- Input Image 2: [model sheet layout guide](../_template/layout/model_sheet_layout.png) for layout only
- Correction history: {{NONE_OR_NOTES}}

{{FILLED_MODEL_SHEET_PROMPT}}

## Reference card

- Output [Painted reference card](reference_card.jpg) ({{WIDTH}} x {{HEIGHT}})
- Input Image 1: [current model sheet](character_sheet.png) for identity
- Input Image 2: [reference card layout guide](../_template/layout/reference_card_layout.png) for framing only
- Correction history: {{NONE_OR_NOTES}}

{{FILLED_REFERENCE_CARD_PROMPT}}

## Expression sheet

- Output [expressions.png](expressions.png) ({{WIDTH}} x {{HEIGHT}}). All 12 labels checked for spelling and order.
- Input Image 1: [current model sheet](character_sheet.png) for identity
- Input Image 2: [expression sheet layout guide](../_template/layout/expressions_layout.png) for layout and acting
- Correction history: {{NONE_OR_NOTES}}

{{FILLED_EXPRESSION_SHEET_PROMPT}}

<!--
For a correction pass, add a dated section here:

## {{CHANGE_SUMMARY}} ({{YYYY-MM-DD}})

- Output [...](...)  Input [...](...)
- Direction: who asked for what, in their words.

{{FILLED_EDIT_PASS_PROMPT}}

Link superseded versions by commit hash, e.g.
https://github.com/hevangel/silicon_wars_anime_girls/blob/<commit>/characters/<id>/character_sheet.png
-->
