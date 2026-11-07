# Generation workflows

Copy the [generation manifest template](generation-manifest.template.yaml) beside an accepted panel and fill in the actual inputs. Reference paths are relative to the repository root. Keep the seed where the generator exposes it, and record the checkpoint, LoRA and strength, masks, and exact prompt as applicable.

Store reviewed ComfyUI graph JSON under `workflows/comfyui/` as workflows are adopted. Record custom nodes and model identifiers in a companion note. Save the API-format graph separately when rendering through an API. Keep keys and model weights in local configuration.

At review, compare the selected render with the source references and inspect the assembled page at reading size. See the [production tutorial](../tutorial/README.md) for PR and lettering practices.

[Pilot 001](../chapters/pilot-001/README.md) demonstrates the complete path from panel prompts to separate lettering and a rendered page. Its manifest records the actual generation inputs for all six panels.
