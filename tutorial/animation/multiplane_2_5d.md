# Multiplane parallax camera (#76)

**Actual contents:** three original vector plates with individual depths; actual manga artwork not yet cut and repainted. The review board is newly authored vector image art. This proof of technique deliberately leaves existing Intel/AMD production artwork intact.

## Run and verify

```sh
python -m unittest tools.test_animation_multiplane_2_5d -v
python -m http.server 8000
# Open http://localhost:8000/chapters/pilot-001/video/multiplane_2_5d/preview.html
```

Editable controls: [scene.json](../../chapters/pilot-001/video/multiplane_2_5d/scene.json). [Reference storyboard](../../chapters/pilot-001/video/multiplane_2_5d/reference-board.svg).

## Three pilot beats

1. Citadel approach (frames 0–47, at 24fps).
2. Foreground arch (frames 48–95, at 24fps).
3. Character reveal (frames 96–143, at 24fps).

## Required follow-up / manual QA

Isolate approved manga foreground, midground and background images with transparency; paint missing hidden regions, open a Blender camera scene, export MP4 and depth diagnostic. Verify at 1× speed, original-character identity, source provenance, timing, screen-safe areas and clip/alpha occlusions. No human approval or full tool-specific render is claimed. Technical checks do not certify art quality.
