# Traditional cel-animation flipbook (#74)

**Actual contents:** six original numbered SVG key poses; 24fps player on fours; no inbetweened hand-painted cels. The review board is newly authored vector image art. This proof of technique deliberately leaves existing Intel/AMD production artwork intact.

## Run and verify

```sh
python -m unittest tools.test_animation_traditional_frame_by_frame -v
python -m http.server 8000
# Open http://localhost:8000/chapters/pilot-001/video/traditional_frame_by_frame/preview.html
```

Editable controls: [scene.json](../../chapters/pilot-001/video/traditional_frame_by_frame/scene.json). [Reference storyboard](../../chapters/pilot-001/video/traditional_frame_by_frame/reference-board.svg).

## Three pilot beats

1. Charge and anticipation (frames 0–47, at 24fps).
2. AMD launches (frames 48–95, at 24fps).
3. Intel blocks (frames 96–143, at 24fps).

## Required follow-up / manual QA

Replace blocking poses with approved clean-up keys and breakdowns; import exposure sheet into OpenToonz/Grease Pencil, ink/colour, add backgrounds and audio, export 5–10s MP4. Verify at 1× speed, original-character identity, source provenance, timing, screen-safe areas and clip/alpha occlusions. No human approval or full tool-specific render is claimed. Technical checks do not certify art quality.
