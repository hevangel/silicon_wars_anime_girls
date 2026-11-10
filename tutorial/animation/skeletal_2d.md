# 2D skeletal rig — Pilot 001 (#70)

**Goal:** Joint pivots and reusable point, idle and facepalm gestures. The initial change contains executable browser choreography plus a new editable technique scene JSON and original visual board. It is an engineering prototype; **not a finished 2d skeletal rig production**.

## Run from a fresh checkout

```sh
python -m unittest tools.test_animation_skeletal_2d -v
python -m http.server 8000
# Open http://localhost:8000/chapters/pilot-001/video/skeletal_2d/preview.html
```

## Technical design

This isolated prototype keeps `visual.art_style: default_manga`, `animation.technique: skeletal_2d`, and `delivery.format: browser_preview` distinct. Frame time is integer 24fps with half-open holds. It demonstrates **relative shoulder/elbow pivot rotation and pose limits**. Scene input: [scene.json](../../chapters/pilot-001/video/skeletal_2d/scene.json); visual [reference board](../../chapters/pilot-001/video/skeletal_2d/reference-board.svg). The stage is a code-drawn vector rig schematic with newly authored geometry: it is *not* a cut-up official character sheet. The page separately shows unmodified canonical Intel/AMD cards. No existing image overwritten.

### Beat-by-beat

1. AMD points to chiplet — 96 frames at 24 fps.
2. Intel turns to address AMD — 96 frames at 24 fps.
3. AMD and Intel return to idle — 96 frames at 24 fps.

**Source input contract:** separated body/arm/hair layers with hidden paint, Godot 2D rig. Control fields: `shoulder_angle`, `elbow_angle`, `pose`, `pivot_location`, `layer_order`. The parameter slider changes stage motion for manual inspection; it does not feed a third-party live capture service. The timeline player supports pause, frame scrub and shot seeking.

## Reproduction and editorial review

Run the stdlib test to validate source fields and the presence of Intel/AMD continuity files. Compare Intel's sapphire crown/light-blue hair and AMD's red braided ponytail/headphones against the real reference cards. Pause on extremes and check eye placement, pose range, clipping, hand/prop consistency, captions and timing. Test with 1920×1080 viewport and mobile width. Write down a human reviewer and decision before production use; tests do **not** imply visual acceptance.

## What is deliberately missing

Schematic pivot animation only. Godot skeletal/mesh scene and 30-second render remain outstanding.

No recorded voices, licensed actor performance, hosted AI output, Blender render or OBS capture is invented. To complete issue #70, acquire/verify assets, implement the tool-specific project/export, render a video or live recording with manifest and source hashes, and obtain human approval. For troubleshooting, serve from the repository root (opening via `file://` blocks `fetch`); check browser console for invalid JSON and use the frame slider to isolate timing defects.
