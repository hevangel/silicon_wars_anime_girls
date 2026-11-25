# Digital-human expression mapping prototype — #73

This first slice exercises neutral, speaking, and reaction parameter mappings and exposes an editable JSON state contract. **2D control-space mock-up; no photoreal 3D actor or facial video.**

## Run

```sh
python -m unittest tools.test_animation_digital_human_vtuber -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/digital_human_vtuber/preview.html
```

Adjust `scene.json` ranges, rebuild the page, and test every slider endpoint; compare reference against `characters/intel/continuity.yaml`. The [review board](../../chapters/pilot-001/video/digital_human_vtuber/reference-board.svg) is new original vector art, not a finished capture. Target requirements: rights-cleared original fictional digital-human mesh, FACS rig, facial capture and OBS. Verify license and input rights, implement a native editable rig and export, reimport it into the selected runtime, record at least 30 seconds, log real capture latency/hardware, and request human visual approval before checking off issue acceptance.
