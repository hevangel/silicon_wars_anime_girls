# Editorial ink fashion versus polished anime key art

Two reusable rendering modes inspired by the user's three fashion illustrations and the subsequent Intel, AMD and Nvidia comparison experiments. The term anti-style means the deliberate visual opposite, not an inferior or forbidden style.

| Axis | loose_ink_fashion | polished_anime_key_art |
| --- | --- | --- |
| Ink | Variable, searching, overlapping, incomplete | Controlled, continuous, precise |
| Color | Irregular washes, open paper, slight misregistration | Fully filled regions and saturated accents |
| Lighting | Sparse, suggestive | Coherent directional lighting, cel shadows and controlled gradients |
| Detail | Selective; fabric expressed through a few gestures | Carefully resolved hair, fabric, material and environment |
| Space | Airy white negative space; abstract accents | Designed scene with readable depth and perspective |
| Mood | Quiet fashion editorial, relaxed lifestyle | High-finish promotional anime, cinematic confidence |

## Identity is not style

Use the current canonical model sheet and continuity file as identity references. The exploratory comparison renders used alternate café outfits and sometimes changed hairstyles, props, poses or body builds. They demonstrate rendering only and must not supersede canonical references. Intel retains light-blue hair, sapphire crown and wafer; AMD retains a red braided high ponytail, amber eyes, headphones and chiplets; Nvidia retains her long green braid, goggles, athletic build and black leather jacket-dress. Casual wardrobe requires explicit scene-level art direction.

## Controlled comparison protocol

1. Freeze the character identity, model sheet, pose, expression, outfit, camera, crop, aspect ratio and scene content. Use the same seed if supported and meaningful.
2. Assemble each prompt from the same identity and scene blocks plus the corresponding template's style block and negative block. Use the appropriate reference images for each style, not as identity sources.
3. Save the exact prompt, model/version, reference paths and hashes, seed if exposed, and accepted render beside the generation manifest. If a field is unavailable, mark it as such.
4. Review the pair side by side at full size and intended publication size. Reject identity drift, changed ages, costume substitutions, extra characters, malformed hands or lettering, and rendering that collapses the distinction.
5. Accept loose ink only when gestural contours, irregular color patches and white paper are plainly visible. Accept polished anime only when line control, full color fills, directional shading and resolved detail are plainly visible. Avoid excessive bloom or background clutter even in the polished version.

The comparison experiments are exploratory, not controlled accepted plates. The source images were generated in the chat and are not currently committed here; a follow-up can archive them separately as noncanonical references and generate matched canonical pairs.

## Templates

- [Japanese ink and watercolor fashion sketch](../prompts/templates/loose_ink_fashion.txt)
- [Polished modern anime key art (anti-style)](../prompts/templates/polished_anime_key_art.txt)
