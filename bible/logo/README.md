# Silicon Wars logo

[silicon_wars_logo.svg](silicon_wars_logo.svg) is a clean black-line wordmark on a white background: **SILICON** over **WARS**, in an angular italic display style with chamfered corners, a pointed W, and a double outline (heavy outer line, thin inner line) that stands in for the neon tube look of the stage version.

- Pure vector: no stage, photo, or glow. The sponsor mark in the stage photo is not part of it.
- Both lines are the same width. Stroke weight is the same across all letters.
- The letterforms are drawn from scratch to match the style of the stage title; they are not an exact copy of any font.
- [build_logo.py](build_logo.py) regenerates the SVG (needs `shapely`): `python build_logo.py silicon_wars_logo.svg`. Change `T` for stroke weight, `SHEAR` for slant, `H2` for line-2 height.
