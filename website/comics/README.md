# Season One Comics

Serve the repository root with a static HTTP server and open /website/comics/. The reader uses plain HTML, CSS, JavaScript, and JSON and has no build step.

Edit comics.json to add a comic or a model version. The order of comics controls Previous and Next, defaultComic controls the landing comic, and each comic's defaultVariant controls its initial artwork.

- Save each comic render in art/ and set its image path, pixel dimensions, alt text, label, and model ID in the variant. Add the model label to models. Set thumbnail to an optional lightweight preview in art/.
- List the references for each variant. Reference paths are relative to paths.references, which points to the repository root by default. Link the sheets from their production locations.
- Link to a specific version with #comic-id/variant-id.
