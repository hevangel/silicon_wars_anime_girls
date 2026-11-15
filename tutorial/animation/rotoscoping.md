# Rotoscope timing and redraw comparison (#75)

**Actual contents:** rights-safe synthetic human pose proxy; no actor performance footage or genuine traced video. The review board is newly authored vector image art. This proof of technique deliberately leaves existing Intel/AMD production artwork intact.

## Run and verify

```sh
python -m unittest tools.test_animation_rotoscoping -v
python -m http.server 8000
# Open http://localhost:8000/chapters/pilot-001/video/rotoscoping/preview.html
```

Editable controls: [scene.json](../../chapters/pilot-001/video/rotoscoping/scene.json). [Reference storyboard](../../chapters/pilot-001/video/rotoscoping/reference-board.svg).

## Three pilot beats

1. Synthetic turn pose (frames 0–47, at 24fps).
2. AMD stylized redraw (frames 48–95, at 24fps).
3. Overlay timing comparison (frames 96–143, at 24fps).

## Required follow-up / manual QA

Record a willing actor under written consent; preserve frame timecode, rights ledger and source hashes; actually draw onto the footage before exporting a before/after movie. Verify at 1× speed, original-character identity, source provenance, timing, screen-safe areas and clip/alpha occlusions. No human approval or full tool-specific render is claimed. Technical checks do not certify art quality.
