# AI video generation candidate workflow — #79

This branch begins with an **executable, honest blocking / storyboard prototype** for: AMD entrance in five seconds, with Intel reaction. New visual artwork is saved at [reference-board.svg](../../chapters/pilot-001/video/ai_video_generation/reference-board.svg). The preview uses existing canonical portrait cards, unmodified.

## Run

```sh
python -m unittest tools.test_animation_ai_video_generation -v
python -m http.server 8000
# browse http://localhost:8000/chapters/pilot-001/video/ai_video_generation/preview.html
```

The editable [scene.json](../../chapters/pilot-001/video/ai_video_generation/scene.json) declares three 120-frame beats at 24fps. The preview can be scrubbed and paused and demonstrates the editorial sequence, not final production frames.

Run `python tools/ai_video_generation_adapter.py --prepare` to validate keyframes and produce a model-neutral JSON request. Do not mark any candidate as generated or accepted without real binary, provider/model version, costs, rights and review.

## Production gap and QA

No video service is connected; no real model output, cost measurement or accepted AI video is invented. Preserve fictional actor identities only, verify source rights, record exact tool versions and approved assets, and inspect a real 1080p exported or captured sequence before acceptance. Unit tests cover JSON contracts only, not appeal, physical realism or continuity.
