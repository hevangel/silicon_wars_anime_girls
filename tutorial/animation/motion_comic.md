# Motion comic: original pilot art (#67)

This proof of concept runs **on the original Pilot 001 PNG images**, with independently editable subtitle text and smooth bounded camera transforms. No original page or continuity sheet is overwritten. [Storyboard](../../chapters/pilot-001/video/motion_comic/reference-board.svg).

## Run

From repository root:

```sh
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/motion_comic/preview.html
```

Edit [scene.json](../../chapters/pilot-001/video/motion_comic/scene.json): 24 fps, integer frame lengths, a valid original image path, and separate subtitle cues. Pan coordinates are stage-relative percentages; scale ~1.01–1.12 to avoid aggressive cropping. Scrub frames or step between shots using the browser controls. For each shot review the manga reading order and character identity against `characters/intel/continuity.yaml` and `characters/amd/continuity.yaml`.

## Art and rights

All photo-panel inputs are project-owned Pilot 001 art. The source image remains its own layer; the captions are HTML independent of the PNG but the original manga lettering within the flat PNG cannot be removed. This is **not** layered character blink/mouth animation; original separations, cleanup, audio, professional 1080p MP4 export, safe-area QA and human approval remain outstanding.

## Checks and handoff

Preview gives a usable proof of pan/zoom, ordered scene timeline and selectable captions. Verify smoothness and mobile readability in browser; confirm the approved source image SHA hashes against the page manifest before production export. Generated review board shows the camera paths (not final character art). Mark review pending until an artist signs off on crop framing, subtitle placement and music/voice rights.
