# Series bible

The [series bible](story_bible.md) defines the setting, proposed story arcs, character age portrayals, and visual continuity rules. The [character roster](../characters/INDEX.md) carries per-character identities, relationships, dialogue, and reference art. The order of story arcs is a planning outline. Add dates and chapter events here as the story establishes them.

## Style variants

Characters have one immutable identity and multiple rendering modes. [art_style.yaml](art_style.yaml) defines the variants globally (`default_manga`, `chibi`); [style_usage_policy.yaml](style_usage_policy.yaml) says where each variant may appear. Each character's `continuity.yaml` carries `supported_styles` and per-variant preserve / simplify rules under `style_variants`. A panel picks its variant with a `style_variant` field in its panel YAML (panels without the field are `default_manga`). Prompt templates for each variant live in [prompts/templates/](../prompts/templates/).
