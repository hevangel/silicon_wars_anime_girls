# Live2D parameter prototype — #71

This first slice exercises neutral, speaking, and reaction parameter mappings and exposes an editable JSON state contract. **Control-space mock-up only; no valid Cubism rig, deformer or physics export.**

## Run

```sh
python -m unittest tools.test_animation_live2d_vtuber -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/live2d_vtuber/preview.html
```

Adjust `scene.json` ranges, rebuild the page, and test every slider endpoint; compare reference against `characters/amd/continuity.yaml`. The [review board](../../chapters/pilot-001/video/live2d_vtuber/reference-board.svg) is new original vector art, not a finished capture. Target requirements: .cmo3/.moc3 model from layered PSD, VTube Studio tracking and OBS live test. Verify license and input rights, implement a native editable rig and export, reimport it into the selected runtime, record at least 30 seconds, log real capture latency/hardware, and request human visual approval before checking off issue acceptance.
