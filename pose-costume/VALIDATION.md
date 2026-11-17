# Version 1 validation

- Production build passes with strict TypeScript checks, including unused code.
- Seven backend tests pass with a simulated Codex process: catalog replacement,
  untrusted reference rejection, CLI image arguments, provenance, concurrency,
  cancellation before launch, missing output, and costume upload/extraction.
- HTTP smoke checks passed for the app, catalog, all 32 character sheets and
  sample original/thumbnail pairs from the built-in and custom pose/costume
  libraries. Cross-origin job submission returns 403, missing job tokens return
  404, and an identity outside the roster returns 400.
- Installed CLI: `codex-cli 0.169.0`. A read-only `codex exec --ephemeral`
  preflight reported the available image generation tool as
  `image_gen.imagegen` (`tools.image_gen__imagegen`). The `image_generation`
  feature is enabled in this installation.
- No live image was generated during dashboard implementation. The tests verify
  job orchestration, not the visual quality or delivery of an actual Codex render.
- The index now features the subsequent successful AMD snow test from job
  `fef3c556-d379-4122-a167-a6c4c8b242bc`, alongside its recorded pose, costume and
  character inputs. The rendered PNG and generation manifest were inspected.
- Browser visual QA could not run because the browser access host was unavailable.
  Responsive layout, visual comparison, reading-size rendering, downloads and
  browser history still need an interactive browser check.
- Upstream submodule files, assets and revision were left unchanged.
