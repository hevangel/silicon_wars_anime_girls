# Live-action cinematic adaptation — reproducible process (#62)

**Current stage:** Config/prompt/continuity scaffold. No casting portraits, wardrobe photos or live-action scenes have been generated and locked yet.

## Identity, acting and camera are independent

1. Open the approved [AMD manga sheet](../../characters/amd/character_sheet.png) and [Intel manga sheet](../../characters/intel/character_sheet.png). Record recognizability signals before photoreal translation: AMD red braided high ponytail, amber eyes, headphones, black/crimson chiplets; Intel long light-blue hair, pointed sapphire crown, blue/cream military dress, wafer and hem logo.
2. Cast a **fictional adult person** per heroine and capture **neutral actor identity** from front, 3/4 and profile under flat light. Assign permanent `actor_id` per approved face. An identity change requires a new revision and review. Do not use or imply an executive/celebrity likeness.
3. Create a **separate wardrobe turnaround** with a versioned `wardrobe_id`: front, side, back, closeups of stitching, shell, crown support, buckles, headphones and actual prop. Check wearer safety and closures in poses.
4. Build an **expression sheet**, ideally 12 expressions at the same lens, light and angle before testing camera changes. Facial asymmetry/skin/hairline must remain identical across each expression.
5. Generate and inspect two expressions at front and 3/4 for AMD and Intel; verify every portrait against the same casting master, not against one another.
6. Block an x86 Citadel two-shot with real human proportions, physical contact shadows and plausible practical lighting. Repeat at neutral/cool/warm light without recasting the faces or changing costume construction.
7. Make matched before/after contact grids: *manga identity sheet* → *neutral casting* → *wardrobe* → *three scene lights*. Inspect at the actual presentation size. Request human visual approval in PR before gallery/publication.
8. Record the model, run ID, seed, prompt, negative prompt, source hashes, copyright/model release status and `actor_id`/`wardrobe_id` in `workflows/`. Store only actual files under `characters/<id>/references/live_action_cinematic/` and use Git LFS for large originals.

## Material and lens QA

| Element | Practical question | Acceptance |
| --- | --- | --- |
| Intel crown | How is it held to the actor's head? | secure light headband; no logo lettering on crown |
| Intel coat | How do gold epaulettes and split panels hang? | seam/closure detail front/back |
| AMD chiplet armor | Where do plates attach? | lightweight supported armor, visible attachments |
| AMD headphones | Can the actor move with them? | credible collar fit and cable routing |
| Face continuity | Does lighting change cheek/eye geometry? | same neutral casting fingerprint across all shots |
| Lighting | Are highlights and shadows physically motivated? | independent key/fill/rim and reflections |
| Disclosures | Could a realistic photo be mistaken for documentary? | fictional company personification label on publication |

## Debugging and limits

- **Plastic skin**: restore fine normal skin texture, subtle asymmetry and appropriate roughness; avoid generic over-sharpening.
- **Anime eyes in realistic face**: use ordinary human orbital shape and iris size, retain character color only.
- **Face changes when smiling/turning**: reset actor casting reference, model face from neutral multi-angle photos, separate expression control and re-review.
- **Costume floats**: add structural attachment, fabric weight and consistent contact shadows; avoid masking impossible construction with VFX.
- **Logo period/rights**: use a verified company mark version, keep fan-fiction disclosure; no claim of company endorsement.
- **Video**: photographic style is *not* an animation technique. Apply temporal face-lock/rigging in a later technique issue.

## Human review gate

Approve identity first, wardrobe second, expressions third, two-shot fourth; automated manifest and YAML validation cannot declare a performance or likeness safe or attractive. At present all assets remain **pending**, not approved.

Tooling: [Krita](https://krita.org/) for masked corrections, [Blender](https://www.blender.org/) for physical camera and material tests.
