# Interactive presenter state machine (#84)

**Demonstrated:** Deterministic input validation, safe gesture/expression queue, reset/cancel and scripted replay.

## Run

```sh
python -m unittest tools.test_animation_interactive_rive_presenter -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/interactive_rive_presenter/preview.html
```

The [review board](../../chapters/pilot-001/video/interactive_rive_presenter/reference-board.svg) and technique-specific SVG artwork are original. The canonical character reference cards in `characters/intel` and `characters/amd` remain untouched.

The browser prototype imports `controller.js` as an ES module. Use preset buttons or `replay.json`; controller validates all commands, bounds duration and queue size, supports cancellation/reset and falls back to idle. Run `node --test chapters/pilot-001/video/interactive_rive_presenter/controller.test.mjs`. Native Rive .riv state machine and editor source still need to be authored and imported.

**Release gate:** The browser controller is real, but no exported .riv artboard or Rive runtime session exists. Review the motion/interaction on a phone and desktop, verify source licenses and hashes, and obtain human approval before merging as complete.
