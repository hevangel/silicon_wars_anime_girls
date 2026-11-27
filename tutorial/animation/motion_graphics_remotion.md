# Remotion chiplet explainer (#82)

This is an implementation milestone: **Typed, frame-accurate 24fps compatibility story**. It has an original [visual board](../../chapters/pilot-001/video/motion_graphics_remotion/reference-board.svg), a runnable browser concept preview, a three-beat scene JSON, pipeline YAML and smoke tests.

```sh
python -m unittest tools.test_animation_motion_graphics_remotion -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/motion_graphics_remotion/preview.html
```

The stage / animation inputs remain separate from visual art style and do not alter the existing Intel/AMD character sheets.

Edit `scene.json` for timing and review the original storyboard before creating final export.

Remotion React composition source is in `chapters/pilot-001/video/motion_graphics_remotion/remotion/`, with its own package manifest and documented `npm run render`. Browser preview is separate and not the Remotion render. All benchmark-like 0.1% text is expressly a joke, not a factual measurement.

**Not complete:** Remotion project is authored but dependencies could not be installed/test-rendered here; final render, narration rights and screen QC are still pending.. Record source hashes, precise tool versions, rights and generated binary provenance, render and visually approve the result, then replace the draft status.
