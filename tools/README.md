# Tools

- `render_pilot.py` validates the [pilot](../chapters/pilot-001/README.md), prints individual generation prompts, and assembles lettered pages from panel PNGs. It defaults to the page-001 plan; pass `--plan chapters/pilot-001/render-page-002.yaml` for the single-panel page 002. Install Pillow 10.1+ and PyYAML.
- `build_site.py` packages the [root character gallery](../index.html), reference cards, and available character, expression, and chibi sheets into a new output directory using Python 3.9+ and the standard library.
- `make_character_template_layouts.py` redraws the blank model sheet, expression sheet, and reference card layout guides in [characters/_template/layout/](../characters/_template/layout/). Install Pillow 10.1+.
