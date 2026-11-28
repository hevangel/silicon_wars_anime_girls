# The TSMC Storytelling Course

Part III of the **TSMC Visual Literacy Series** — *Visual Semantics and Pragmatics*.
Part I (the [Style Course](../tsmc-styles/)) changed the style and kept the pose;
Part II (the [Seeing Course](../tsmc-seeing/)) kept the style and changed one visual
decision at a time. This course starts from an intended meaning and chooses the
visual decisions that carry it: expressions, gestures, symbols, sequences and
captions, taught through controlled comparisons against six control images.

- 25 lessons in six modules (the face; the body; people together; signs, scenes
  and symbols; stories; semantic experiments), 80 comparison groups.
- 313 generated study plates, all accepted (the Lesson 18 sequence frame whose
  elbow contact never rendered is published with its deviation stated on the
  page: the frame shows the moment just after the nudge) plus 20 deliberate
  reuses of earlier plates, cross-referenced instead of duplicated.
- Layouts: side-by-side comparisons (control first), intensity ladders,
  reorderable sequences, a caption experiment (same picture, three stories)
  and an intended-vs-perceived quiz lesson.

## Files

- `index.html`, `style.css`, `app.js` — the static page (no framework).
- `storytelling.json` — generated public course data; do not edit by hand.
- `generation-manifest.json` — the canonical generation manifest (v2.0-supplement).
- `art/` — web derivatives (full ≤1200 px, thumbs ≤480 px, native aspect).
  Control C00 is referenced from Part II, not duplicated.
- `tools/build_storytelling.py` — builds `storytelling.json` and `art/` from the
  study workspace (`$TSMC_STORYTELLING_DIR`, default `~/workspace/tsmc_storytelling_study`):
  the manifest, the acceptance ledger and the course copy. A plate is published
  only when the ledger marks it accepted.
- `tools/validate_storytelling.py` — validates the built data against the files
  on disk (ids, dimensions, coverage, captions, quiz pairs).

Original renders, rejected takes and review history live in the study
workspace, not in this repository. All images are AI-generated studies of a
fictional character, made for education; intended meanings are prompts, not
proven audience responses.
