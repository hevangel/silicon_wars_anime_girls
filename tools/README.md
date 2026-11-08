# Tools

- `render_pilot.py` validates the [pilot](../chapters/pilot-001/README.md), prints individual generation prompts, and assembles lettered pages from panel PNGs. It defaults to the page-001 plan; pass `--plan chapters/pilot-001/render-page-002.yaml` for the single-panel page 002. Install Pillow 10.1+ and PyYAML.
- `build_site.py` packages the [gallery](../site/README.md) into a new output directory using Python 3.9+ and the standard library. The gallery includes the character cards, pilot page, and rough storyboard.
