# Pilot 004 · The Memory Plea

A single 4:3 comedy panel. OpenAI begs Micron, Samsung, and SK hynix for memory allocation and collects three polite refusals.

![Rendered single-panel page 001](pages/page-001/final/page-001.png)

- [Script](script.md) and [chapter record](chapter.yaml)
- [Panel brief](pages/page-001/panels/panel-01.yaml), [storyboard](pages/page-001/storyboard.yaml), and [editable lettering](pages/page-001/lettering.yaml)
- [Render plan](render-page-001.yaml), [generation manifest](pages/page-001/manifest.yaml), and [review checklist](qa.yaml)

The art is generated text-free on the [4:3 single-panel layout](../../layouts/single-panel-4x3.yaml); the balloons are composited from `lettering.yaml` at assembly time. The four reference cards were cropped above their name plates into one [cast reference sheet](pages/page-001/refs/cast-reference.jpg), the single image passed to the generator; the manifest records that reference, every model sheet, the selected take, and why two earlier takes were dropped.

## Reassemble

```sh
python tools/render_pilot.py --plan chapters/pilot-004/render-page-001.yaml --check
python tools/render_pilot.py --plan chapters/pilot-004/render-page-001.yaml
```

Print the exact art prompt with `python tools/render_pilot.py --plan chapters/pilot-004/render-page-001.yaml --prompt panel-01`. To change a line, edit `pages/page-001/lettering.yaml` and reassemble; the panel art is untouched.
