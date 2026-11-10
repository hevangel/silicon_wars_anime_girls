# Hyperreal fantasy key art compositing (#64)

**Status:** Style/specification, original VFX layers and compositing tool. The true AMD and Intel photographic casting masters are **not yet generated or approved**.

## Pipeline

1. **Reuse actors, don't recast:** take approved casting face and wardrobe neutral shots from `live_action_cinematic`. Compare the original [AMD](../../characters/amd/character_sheet.png) / [Intel](../../characters/intel/character_sheet.png) identity cues; actor IDs stay immutable under all FX levels.
2. **Separate physical/simulated:** explicitly mark wearable seam/crown/armor vs projected architecture and effects. Build a neutral actor+costume plate without glow. Photograph/model contact shadows, pose and eyeline.
3. **VFX atlas:** Intel sapphire Citadel geometry with blue light spill, AMD crimson discrete chiplets with directional kinetic arcs. Render each as cropped/lossless transparent RGBA with consistent resolution and camera registration.
4. **Opacity and shadows:** place VFX behind/in front of person with masks; include contact-light and atmosphere passes. A face may not be replaced by effects and then judged “same actor.”
5. **Create a nonapproved source manifest** after plates exist, with canvas, ordered image paths/roles, actor ID, wardrobe ID, and source SHA-256 (example below). Render `--clean` and `--all` comparisons.
6. **Review hero/duel views:** same actor identity at close-up, full body and dramatic action; compare clean base with effects on/off and light-source direction. Require human approval of actor, costume, shadows, layer occlusion and fan-fiction disclosure.
7. Archive layered sources, model version, prompt, seed, rights and effects provenance; export web-sized preview separately. Original sources should use Git LFS if large.

## Deterministic compositor

```sh
python -m pip install "Pillow>=10.1"
python tools/compose_fantasy_fx.py manifest.json --out /tmp/silicon_wars_duel
python -m unittest discover -s tools -p test_compose_fantasy_fx.py
```

Create `manifest.json` only when these **actual files** exist:

```json
{
  "schema": 1,
  "style": "live_action_hyperreal_fantasy",
  "status": "unapproved",
  "actor_id": "amd-fictional-cast-v1",
  "wardrobe_id": "amd-cinematic-wardrobe-v1",
  "canvas": [1920, 1080],
  "plates": [
    {"id": "base", "role": "actor", "file": "base.png"},
    {"id": "costume", "role": "costume", "file": "costume.png"},
    {"id": "chiplets", "role": "fx", "file": "chiplets.png"}
  ]
}
```

The tool emits `-clean.png` (actor and costume), `-all.png` (all plates) and `.json` hashes/ordered layers; source plates remain editable. It checks file existence, dimensions, RGBA and role ordering, **not** whether emitted light is physically correct or whether two portraits show the same actor. The generated review comparison is not an approved key art.

## QA and troubleshooting

- **Identity drifts across FX-on:** compare the clean plate with source casting master; avoid recoloring or reconstructing eyes/nose.
- **Glow incorrectly lit:** infer the FX light vector and add a controlled matching ground/armor bounce pass, never hand-wave inconsistent shadow directions.
- **Floating armor:** label it as simulation or provide visible support to clothing underneath.
- **Compositing halos:** preserve premultiplied/straight-alpha handling and avoid rescaling; use identical frame sizes and alpha geometry.
- **Crossover in two-actor scene:** separate each actor ID's base and silhouette mask to prevent AMD hair/gear being transferred to Intel.
- **False documentary look:** visible fictional-personification disclaimer on public releases.

Tools: [Blender](https://www.blender.org/) for blocking/light passes, [Krita](https://krita.org/) for alpha and paintover. This is a **style**, not a complete video/VFX shot pipeline.
