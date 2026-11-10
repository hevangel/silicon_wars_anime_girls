# VRM 1.0 capture mapping prototype — #72

This first slice exercises neutral, speaking, and reaction parameter mappings and exposes an editable JSON state contract. **2D control-space mock-up; no VRM mesh, 3D skeleton or real camera tracking.**

## Run

```sh
python -m unittest tools.test_animation_vrm_vtuber -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/vrm_vtuber/preview.html
```

Adjust `scene.json` ranges, rebuild the page, and test every slider endpoint; compare reference against `characters/amd/continuity.yaml`. The [review board](../../chapters/pilot-001/video/vrm_vtuber/reference-board.svg) is new original vector art, not a finished capture. Target requirements: authored humanoid mesh and VRM 1.0 export, ARKit facial expressions, capture/OBS. Verify license and input rights, implement a native editable rig and export, reimport it into the selected runtime, record at least 30 seconds, log real capture latency/hardware, and request human visual approval before checking off issue acceptance.
