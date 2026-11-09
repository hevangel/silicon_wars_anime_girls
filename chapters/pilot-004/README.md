# Pilot 004 · More Memory, Please

A single-panel comic in landscape 4:3. OpenAI kneels begging in the Citadel courtyard while the three memory houses — Micron, Samsung, and SK hynix — look down at her, unimpressed.

![Rendered single-panel page](pages/page-001/final/page-001.png)

OpenAI's next model needs more memory than anyone can supply. Read right to left: SK hynix is deadpan, Samsung is grand, OpenAI pleads, and Micron delivers the verdict.

- [Script](script.md) and [review checklist](qa.yaml)
- [Panel brief](pages/page-001/panels/panel-01.yaml) and [editable lettering](pages/page-001/lettering.yaml)
- [Panel order](pages/page-001/storyboard.yaml) on the [4:3 single-panel layout](../../layouts/single-panel-4x3.yaml), [render plan](render.yaml), and [generation manifest](pages/page-001/manifest.yaml)

Assemble it with its render plan:

```sh
python tools/render_pilot.py --plan chapters/pilot-004/render.yaml --check
python tools/render_pilot.py --plan chapters/pilot-004/render.yaml
```

---

The page is a review draft.

## Wafer roundtable alternate

In this 4:3 review draft, OpenAI asks for more memory across a giant silicon wafer while her robot catches the end of the requisition.

[Corrected panel](pages/page-001/alternates/wafer-roundtable/c-wafer-roundtable-draft-02.png) · [Composition sketch](pages/page-001/alternates/wafer-roundtable/c-memory-request.png) · [Generation notes](pages/page-001/alternates/wafer-roundtable/c-wafer-roundtable-draft-01.prompt.md) · [Wordmark edits](pages/page-001/alternates/wafer-roundtable/c-wafer-roundtable-draft-02.prompt.md)

The dialogue is part of this preview image.
