# Flash-style symbol swapping — Pilot 001 (#68)

**Goal:** Reusable mouth, eye, head and arm symbols with held poses. The initial change contains executable browser choreography plus a new editable technique scene JSON and original visual board. It is an engineering prototype; **not a finished flash-style symbol swapping production**.

## Run from a fresh checkout

```sh
python -m unittest tools.test_animation_limited_cutout_flash -v
python -m http.server 8000
# Open http://localhost:8000/chapters/pilot-001/video/limited_cutout_flash/preview.html
```

## Technical design

This isolated prototype keeps `visual.art_style: default_manga`, `animation.technique: limited_cutout_flash`, and `delivery.format: browser_preview` distinct. Frame time is integer 24fps with half-open holds. It demonstrates **mouth symbol A–F, blink holds and arm rotations**. Scene input: [scene.json](../../chapters/pilot-001/video/limited_cutout_flash/scene.json); visual [reference board](../../chapters/pilot-001/video/limited_cutout_flash/reference-board.svg). The stage is a code-drawn vector rig schematic with newly authored geometry: it is *not* a cut-up official character sheet. The page separately shows unmodified canonical Intel/AMD cards. No existing image overwritten.

### Beat-by-beat

1. Intel declares compatibility — 96 frames at 24 fps.
2. AMD rebuts with a hand gesture — 96 frames at 24 fps.
3. Intel reacts with a held skeptical pose — 96 frames at 24 fps.

**Source input contract:** layered source art, overpainted occlusion, recorded dialogue, frame timings. Control fields: `mouth_symbol`, `blink`, `pivot`, `arm_angle`, `pose_hold`. The parameter slider changes stage motion for manual inspection; it does not feed a third-party live capture service. The timeline player supports pause, frame scrub and shot seeking.

## Reproduction and editorial review

Run the stdlib test to validate source fields and the presence of Intel/AMD continuity files. Compare Intel's sapphire crown/light-blue hair and AMD's red braided ponytail/headphones against the real reference cards. Pause on extremes and check eye placement, pose range, clipping, hand/prop consistency, captions and timing. Test with 1920×1080 viewport and mobile width. Write down a human reviewer and decision before production use; tests do **not** imply visual acceptance.

## What is deliberately missing

No approved separated face/arms or licensed dialogue WAV; this is an original editable vector *rig schematic*.

No recorded voices, licensed actor performance, hosted AI output, Blender render or OBS capture is invented. To complete issue #68, acquire/verify assets, implement the tool-specific project/export, render a video or live recording with manifest and source hashes, and obtain human approval. For troubleshooting, serve from the repository root (opening via `file://` blocks `fetch`); check browser console for invalid JSON and use the frame slider to isolate timing defects.
