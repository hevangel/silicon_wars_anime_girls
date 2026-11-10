# Photorealistic 3D cinematic staging — #78

This branch begins with an **executable, honest blocking / storyboard prototype** for: Intel walks into a laboratory through two camera setups. New visual artwork is saved at [reference-board.svg](../../chapters/pilot-001/video/photoreal_3d_cinematic/reference-board.svg). The preview uses existing canonical portrait cards, unmodified.

## Run

```sh
python -m unittest tools.test_animation_photoreal_3d_cinematic -v
python -m http.server 8000
# browse http://localhost:8000/chapters/pilot-001/video/photoreal_3d_cinematic/preview.html
```

The editable [scene.json](../../chapters/pilot-001/video/photoreal_3d_cinematic/scene.json) declares three 120-frame beats at 24fps. The preview can be scrubbed and paused and demonstrates the editorial sequence, not final production frames.

Use `blender -b -P chapters/pilot-001/video/photoreal_3d_cinematic/blender/block_scene.py` with Blender 4.x to create a native scene with proxy mannequin geometry, keyframes, lighting and camera. **This command was not run here (Blender unavailable).** No skinned character model or finished render is claimed.

## Production gap and QA

No photoreal actor, high-fidelity face materials or rig, wardrobe simulation or finished cinematic render; this is camera/lighting blocking. Preserve fictional actor identities only, verify source rights, record exact tool versions and approved assets, and inspect a real 1080p exported or captured sequence before acceptance. Unit tests cover JSON contracts only, not appeal, physical realism or continuity.
