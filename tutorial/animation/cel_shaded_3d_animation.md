# Cel-shaded 3D combat animation — #77

This branch begins with an **executable, honest blocking / storyboard prototype** for: AMD Chiplet Barrage vs Intel x86 Citadel. New visual artwork is saved at [reference-board.svg](../../chapters/pilot-001/video/cel_shaded_3d_animation/reference-board.svg). The preview uses existing canonical portrait cards, unmodified.

## Run

```sh
python -m unittest tools.test_animation_cel_shaded_3d_animation -v
python -m http.server 8000
# browse http://localhost:8000/chapters/pilot-001/video/cel_shaded_3d_animation/preview.html
```

The editable [scene.json](../../chapters/pilot-001/video/cel_shaded_3d_animation/scene.json) declares three 120-frame beats at 24fps. The preview can be scrubbed and paused and demonstrates the editorial sequence, not final production frames.

Use `blender -b -P chapters/pilot-001/video/cel_shaded_3d_animation/blender/block_scene.py` with Blender 4.x to create a native scene with proxy mannequin geometry, keyframes, lighting and camera. **This command was not run here (Blender unavailable).** No skinned character model or finished render is claimed.

## Production gap and QA

No approved original humanoid meshes, skinning, hair physics or rendered final fight yet; Blender proxy code is only blockout. Preserve fictional actor identities only, verify source rights, record exact tool versions and approved assets, and inspect a real 1080p exported or captured sequence before acceptance. Unit tests cover JSON contracts only, not appeal, physical realism or continuity.
