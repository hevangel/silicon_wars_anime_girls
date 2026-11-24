# The TSMC Style Course

A single-page art course for college students with no previous art training,
built from the TSMC art-style study: one character (TSMC from Silicon Wars) in
one café pose, rendered in **105 styles / 240 pictures**, grouped into
**12 lessons** that walk from raw media (graphite, fresco, ink) through print,
photography, craft, world traditions, the Western canon, public art,
modernism, design systems, pop, installation — and finally the video-game
graphics ladder from NES 8-bit to PS5 ray tracing.

Pedagogy: because the pose and character are held constant, style itself is
the only variable — students learn to see medium, composition and cultural
convention instead of subject matter. Every style card carries a
plain-language blurb, a "What to look for" list and a Wikipedia link; every
lesson ends with a short looking exercise. Lesson completion is tracked in
the browser (localStorage) with a progress bar. All study images are
AI-generated illustrations of a fictional character, and the page says so.

## Files

- `index.html`, `style.css`, `app.js` — the app (no build step; plain
  HTML/CSS/JS, fetches `artwork.json`).
- `artwork.json` — the curriculum data: lessons → styles → images.
- `art/<style-slug>/` — web-sized images (`1.webp`… full view ≤1100px,
  `t1.webp`… thumbnails ≤440px).
- `tools/content.py` — the curriculum copy (lessons, blurbs, look-for lists,
  Wikipedia targets) and `tools/build_atlas.py` — regenerates `artwork.json`
  and `art/` from the original full-size study.

## Regenerating

```sh
TSMC_STUDY_DIR=~/workspace/tsmc_style_study python3 tools/build_atlas.py
```

The builder validates that every style is assigned to exactly one lesson and
that the content covers every style folder in the study.

## Serving

Any static server from the repo root, e.g. `python3 -m http.server`, then
open `/website/artwork/tsmc-styles/`. (Opening `index.html` via `file://`
will not work — browsers block the `artwork.json` fetch.)
