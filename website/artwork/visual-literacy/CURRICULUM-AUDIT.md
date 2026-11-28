# Curriculum audit — initial review (2026-11-27)

Scope: structured lesson/card data for all three volumes and visual spot checks, not a full historical or image-by-image audit. No images deleted or regenerated. Counts refer to the published JSON at review time; the workbench recomputes them.

## Findings

- I: 15 lessons, 419 styles, 554 plates. Media, techniques, movements, genres and technology are intentionally overlapping; preserve the multi-label classes. The Baroque thumbnail visibly changes framing, setting and costume details in addition to style; the claim that pose/scene are strictly fixed across every style is too strong. Label as a style reinterpretation rather than a single-variable experiment. Similar risk applies to installation, architecture, performance and historical craft simulations.
- II: 15 lessons, 120 cards, 188 plates plus control. The side-light thumbnail shows a hard directional beam and darker ambient fill/exposure as well as direction; relabel as a lighting recipe or regenerate a matched pair with fixed hardness and fill. The control already uses left window light. Validate direction with shadow geometry. Existing figure and mood lessons intentionally break single-variable isolation.
- III: 25 lessons, 80 groups. Published coverage reports 313 accepted generated studies, 20 reused slots, no pending. There are 337 accepted image records including caption/context records; don't confuse rendered slots with unique assets. README still describes one pending frame; reconcile generated metadata, manifest and README. A loneliness thumbnail successfully depicts isolation via empty seating but can also read as peaceful solitude (the lesson already acknowledges this). Inner-brow-raise thumbnail looks subtle/near neutral; compare to C01 and the other brow variants at full size before declaring a failure.
- Existing registry: 377 nodes; 120 decision, 251 meaning, four narrative, two context; zero artistic-language nodes. 344 link to two courses, four to all three, 29 to one. Authority has only Part I references despite Part III's explicit authority lesson. "Aged texture" points to Side Light, an approximate association rather than an equivalent concept. Keep original refs as legacy evidence, distinguish exact teaching links from proposed tendencies. Do not treat substring/keyword matches as validated semantics.

## Gaps and proposed additions (prioritize after human review)

| Priority | Concept | Why | Suggested controlled study |
|---|---|---|---|
| P0 | AI output fidelity / control isolation | Core method needs reproducible validation | same prompt, different seeds; intended edit vs incidental drift |
| P0 | Denotation vs inference | Prevent treating meaning as ground truth | reuse neutral cafe; observed facts vs three possible readings |
| P0 | Audience and purpose | Pragmatics needs explicit practice | same fact as warning, invitation, explanation, editorial |
| P1 | Typography, lettering, legibility | Visual communication crosses image and text | same poster with hierarchy/contrast/kerning changes; browser-render lettering |
| P1 | Icon/index/symbol; convention and cultural variation | Distinguish resemblance, trace and learned convention | same object as depiction, footprint, sign; source-specific cultural examples |
| P1 | Cropping, occlusion, salience and misleading context | AI images may hide evidence or imply false causality | same scene with omitted context vs full scene |
| P1 | Art direction and consistency across a set | Practical AI generation requires repeatable identity, palette and camera | 3-shot contact sheet, intentional vs accidental variations |
| P2 | Accessibility / color-vision differences | Meaning must not depend on hue alone | same warning with hue only vs shape and text cues |
| P2 | Sequential staging / screen direction | Part III covers sequencing but continuity needs its own checks | consistent eyeline, 180-degree rule, deliberate violation |
| P2 | Negative prompts, reference strength, inpainting, iteration | Transfer from visual literacy to actual AI control | same desired edit with competing prompt specifications; model-specific limitations |

## Overlap policy

Keep Part II figure/open-closed poses vs III acting; II mood recipes vs III mood and semantic experiments; I genre vs III narrative intent. These are productive reuse across abstraction levels. III loneliness/mood and same-smile/context recur; retain complementary exercises but reference identical accepted images rather than copying them. Do not delete near-synonyms without checking definitions. Explicitly record exact aliases vs related concepts, and curated cross-layer tendencies.

## Illustration review rubric

For each plate independently compare with its stated control (if applicable): identity/costume, requested visual variable, incidental drift, legibility at thumbnail and full view, factual/cultural plausibility, and interpretation ambiguity. Record evidence and verdict: pass / needs review / misleading / regenerate. A semantic ambiguity is not automatically a defect; a missing requested cue is. Spot checks are not a blanket signoff. Historical styles are AI approximations, not reproductions of authentic artifacts; verify against museum sources before making strong historical claims.

Review queue: all remaining plates, especially subtle facial-action units, multi-variable lighting, historically specific sacred/cultural art, typography, sequential continuity. Full-image review and duplicate hashes across the actual binary corpus remain outstanding.
