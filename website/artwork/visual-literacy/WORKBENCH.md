# Visual Literacy Workbench

An interactive companion to the three existing courses. The course data remains the source of truth; the graph is rebuilt in the browser from the published manifests and registry.

- Open `website/artwork/visual-literacy/workbench.html` through a static HTTP server rooted at the repository (for example, `python3 -m http.server 8000`).
- Search or filter the ontology, inspect examples and typed relationships, and add concepts to the prompt composer. Export the graph as JSON for reuse by other tools.
- For image analysis, upload an image locally. Either copy the generated analysis instruction into Muse or another vision-capable assistant and paste its JSON response back, or explicitly configure a compatible vision chat-completions endpoint. The latter requires a model, a provider that permits browser CORS, and a key if required by that provider. Prefer a trusted local proxy. No key is stored by the page; an entered key and uploaded image are sent only when you confirm the configured endpoint. Model-reported confidence is not calibrated; the importer validates IDs, not whether the evidence is accurate.
- Recognition quizzes and an art-direction rubric form the initial assessment set. They are practice activities, not a validated examination.

## Machine-readable ontology
Node IDs are namespaced (`style:`, `decision:`, `group:`, `plate:`, `concept:`). Edges carry a relation and evidence string. `same_label_review` and legacy links are candidates for review, not synonym declarations. Curated `can_support` and `often_uses` links are contextual tendencies. Reused plate IDs are deduplicated while preserving group references.

To validate and export without a browser, run `node website/artwork/visual-literacy/check-graph.mjs` from any directory. Pass `--export` to print the graph JSON to stdout.

## Limitations
Initial curriculum audit is in [CURRICULUM-AUDIT.md](CURRICULUM-AUDIT.md). Image-by-image adjudication, historical reference checking, coverage of the recommended new lessons, browser end-to-end testing and live vision endpoint testing remain outstanding. No artwork has been changed or generated. The graph is a catalog plus typed links, not a complete formal ontology or a reasoner.
