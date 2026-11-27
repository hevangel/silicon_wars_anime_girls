# Series bible

The [series bible](story_bible.md) defines the world of the Great Compute War, its tone, the interdependence power system, the three artistic rules, the two generations, the core relationships, character age portrayals, and visual continuity rules. The [character roster](../characters/INDEX.md) carries per-character identities, relationships, dialogue, and reference art. The order of story arcs is a planning outline. Add dates and chapter events here as the story establishes them.

## Style variants

Characters have one immutable identity and multiple rendering modes. [art_style.yaml](art_style.yaml) defines the variants globally (`default_manga`, `chibi`, `loose_ink_fashion`, `polished_anime_key_art`); [style_usage_policy.yaml](style_usage_policy.yaml) says where each variant may appear. Each character's `continuity.yaml` carries `supported_styles` and per-variant preserve / simplify rules under `style_variants`. A panel picks its variant with a `style_variant` field in its panel YAML (panels without the field are `default_manga`). Prompt templates for each variant live in [prompts/templates/](../prompts/templates/).

## Editorial / anti-style comparison

[Loose ink fashion](../prompts/templates/loose_ink_fashion.txt) and [polished anime key art](../prompts/templates/polished_anime_key_art.txt) are independent opt-in rendering variants. The latter is the deliberately opposite aesthetic (anti-style), not a prohibited style. See [comparison and review guide](editorial_style_comparison.md). Both are enabled for Intel, AMD, and Nvidia; other characters need their own continuity entries before use. The default manga style remains unchanged.
