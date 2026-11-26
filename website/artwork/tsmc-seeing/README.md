# The TSMC Seeing Course

A single-page art course for college students with no previous art training,
the companion to the [TSMC Style Course](../tsmc-styles/). The Style Course
held the pose constant and changed the style; this course runs the experiment
in reverse: the character (TSMC from Silicon Wars), the café scene and one
neutral digital-painting style are held constant, and every card changes
**exactly one visual decision** — light direction, color temperature,
viewpoint, composition. **15 lessons, 120 cards, 188 pictures** plus one
approved **control image**, which is shown beside every card so the single
change is the only difference a student can see.

Pedagogy notes:

- Lessons 1–2 (line, value) are derived from the control so pose and layout
  match it exactly. Lesson 10 changes the pose on purpose (the figure is its
  subject); Lesson 14 changes several settings at once (mood recipes);
  Lesson 15 has no images — it covers sketchbook, critique and portfolio
  practice for AI-made work.
- Grids, arrows, rulers, swatches and labels are **overlays drawn by the
  page** (inline SVG in `app.js`), never baked into the images. Twenty cards
  have one; each has a "Show overlay" button.
- Lesson completion is tracked in the browser (localStorage) with a
  progress bar. All study images are AI-generated illustrations of a
  fictional character, and the page says so.

## Files

- `index.html`, `style.css`, `app.js` — the app (no build step; plain
  HTML/CSS/JS, fetches `seeing.json`).
- `seeing.json` — the curriculum data: lessons → cards → images, plus the
  Lesson 15 prose as HTML.
- `art/<card-slug>/` — web-sized images (`1.webp`… full view ≤1200px wide,
  `t1.webp`… thumbnails ≤480px wide) and `art/control.webp`, the control.
- `tools/build_seeing.py` — regenerates `seeing.json` and `art/` from the
  study in `~/workspace/tsmc_seeing_study/` (manifest parsed from Horace's
  syllabus, the generated images, and the approved control).

## Regenerating

```sh
TSMC_SEEING_DIR=~/workspace/tsmc_seeing_study python3 tools/build_seeing.py
```

The builder validates the course totals: 15 lessons, 120 cards, 188 images,
20 overlays, and that every card with overlay text in the syllabus has a
page-drawn renderer.

## Serving

Serve the folder over HTTP (the page fetches `seeing.json`):

```sh
python3 -m http.server --directory website/artwork/tsmc-seeing
```
