# Animatic production: Pilot 001 (#66)

This is a **30-second timed storyboard** built from the *existing* six manga panels. It does not create new actor likenesses or replace approved art. The source images, identity constraints, and SHA-256 values are tracked by the existing Pilot 001 manifest.

## Rebuild

From the repository root, with Python 3.11+ and FFmpeg (libx264, AAC, mov_text) available:

```bash
python -m pip install "Pillow>=10.1" "PyYAML>=6.0"
python -m unittest discover -s tools -p test_animatic.py -v
python tools/animatic.py --check
python tools/animatic.py --no-video --out /tmp/silicon-wars-animatic
python tools/animatic.py --out /tmp/silicon-wars-animatic
```

Default output: **1920×1080, 24 fps, 720 frames / 30 seconds**. For a smaller preview pass `--size 640x360`; this changes resolution, not shot timing. The builder generates `animatic.mp4` with selectable timed-text subtitles, `subtitles.srt`, an editable shot CSV, generated click-only WAV, contact sheet, per-shot stills and a provenance manifest with source hashes and tool versions. Output binaries are build artifacts rather than hand-edited source.

## Interactive preview and source

[Timeline JSON](../../chapters/pilot-001/video/animatic/timeline.json) is the editable source. The [browser preview](../../chapters/pilot-001/video/animatic/preview.html) offers frame scrubbing, play/pause, cue text and preview-only shot labels. To use it, run `python -m http.server` at the repository root and navigate to `/chapters/pilot-001/video/animatic/preview.html`.

All shot timing is **integer, half-open frames** `[start_frame,end_frame)`: s01 0–72 (Citadel), s02 72–192 (Intel challenges), s03 192–312 (AMD replies), s04 312–384 (Nvidia offers help), s05 384–480 (chiplets lock), s06 480–720 (compatibility 1%, Intel and AMD punchline). This preserves the six-panel right-to-left reading order. The artwork stills are adapted into slow camera movements without altering the characters' appearances.

The editable `chapters/pilot-001/pages/page-001/lettering.yaml` is authoritative: if a caption in the timeline differs, validation fails rather than silently changing dialogue. The original art SHA-256 must match the page manifest. Generated audio deliberately contains *only* locally synthesized mechanical click effects and otherwise silence because no temporary voice files were provided. The MP4 contains selectable captions; viewers may need to enable them in the player. The browser preview draws the captions and the 1% status separately.

## Review and validation

GitHub Actions runs offline unit tests and hash checks, exports a sample 1080p MP4 and contact sheet, and attaches them as a workflow artifact. The source and generated preview are **not** automatically artist-approved. Before release, compare Intel's light-blue hair and sapphire crown, AMD's red braided ponytail and headphones, and Nvidia's emerald braid against current `characters/<id>/continuity.yaml`. Check cuts, shot pacing, readability, caption timing, crop safety and sound.

Common failures: wrong source SHA → review source changes first; FFmpeg missing libx264 → install FFmpeg or use `--no-video`; video slow to encode → use `--size 640x360` for iterative edits; subtitle not visible → enable the embedded subtitle track or use the SRT sidecar; no spoken voice → intentional placeholder, not a bug. If adding recorded voices later, record voice consent/rights, WAV hashes and frame offsets in a separate follow-up; no false lip-sync claims.

References: [FFmpeg docs](https://ffmpeg.org/ffmpeg.html), [Blender VSE](https://docs.blender.org/manual/en/latest/video_editing/index.html), [Remotion](https://www.remotion.dev/).
