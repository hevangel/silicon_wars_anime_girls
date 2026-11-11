# Branching Intel vs AMD visual novel (#85)

**Demonstrated:** Playable browser story graph, save/resume and two endings plus Ren'Py script.

## Run

```sh
python -m unittest tools.test_animation_interactive_visual_novel -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/interactive_visual_novel/preview.html
```

The [review board](../../chapters/pilot-001/video/interactive_visual_novel/reference-board.svg) and technique-specific SVG artwork are original. The canonical character reference cards in `characters/intel` and `characters/amd` remain untouched.

Use the choice buttons and Save / Resume / Restart. `story.json` drives the browser renderer; Python tests verify every target, two unique endings, no dangling nodes and canonical character assets. The Ren'Py `.rpy` contains the same branching logic but requires tested project packaging and art imports.

**Release gate:** The browser game is playable; native Ren'Py packaging, approved portrait export and cross-device deployment have not been tested. Review the motion/interaction on a phone and desktop, verify source licenses and hashes, and obtain human approval before merging as complete.
