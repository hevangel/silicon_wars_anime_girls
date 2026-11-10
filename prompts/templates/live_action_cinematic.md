# Live-action cinematic casting and photographic prompts

**Style identifier:** `live_action_cinematic`. A new photograph changes the render of the fictional *Silicon Wars* heroine, not the identity or age of the underlying character. Actor, wardrobe, emotion, lighting and camera are **separate variables**.

## Reusable prompt assembly

**Identity (locked)**: use canonical approved character sheet and `characters/<id>/continuity.yaml`; explicitly describe an **original fictional adult performer**, her specific bone structure, naturally asymmetric face, hairline, physique and pores. Hold one `actor_id` across all shots. Never imitate a particular real celebrity, corporate founder or executive.

**Wardrobe (versioned)**: specify `wardrobe_id` and actual fabrics, seams, snaps, collar supports, fastening and safe prop dimensions; logo is a removable accessory. No floating pauldrons.

**Camera (editable)**: full-frame photographic aesthetic; neutral casting portrait at eye level with 70–85mm portrait field of view, then medium/establishing on 35–50mm, consistent face identity; shot-specific depth of field and believable perspective.

**Lighting (editable)**: neutral softbox first; then plausible cool industrial key with soft practical fill and a separate subtle rim; motivate every shadow, reflection and contact light.

**Negative constraints**: no celebrity/real executive face, no anime anatomy, no giant glossy eyes, no porcelain skin, no smoothing, no extra fingers, no impossible unsupported armor, no face identity switching, no cinematic VFX layers merging with skin, no unapproved public documentary claims.

## Required three distinct sets

1. **Actor casting sheet**: neutral front, left 3/4, right profile, face closeup, flat light; minimal accessories; same actor face throughout.
2. **Wardrobe construction sheet**: same actor full body front/side/back plus labeled cloth, gold trim, seams, fasteners, footwear and physically held props.
3. **Acting sheet**: smile, command, irritation, disbelief, fatigue, confident smirk and neutral, with one actor/wardrobe version and constant lighting. (No fake facial-identity lock inferred from similarity alone.)

### AMD casting master

Original fictional adult red-haired actress playing AMD. Amber eyes, distinctive **high braided fire-red ponytail**, athletic silhouette and natural face with identifiable uneven eyebrow line, small cheek asymmetry and realistic skin texture; black/crimson physically wearable chiplet jacket, headphones around neck, fingerless gloves and practical boots. Neutral grey cyclorama, frontal film casting portrait, 85mm field of view, gentle key and soft fill, no stylized VFX. Generate consistent three-angle casting sheet only after the neutral face is approved.

### Intel casting master

Original fictional adult actress playing Intel, light-blue long hair with established hairline, natural-size sapphire eyes, unbranded pointed sapphire crown. Wearable gold-epauletted royal-blue/cream military coat, white gloves, physical wafer heirloom and small hem Intel Inside emblem. Neutral grey casting light, stable subtle facial asymmetry, realistic skin pores. Distinguished upright bearing, visually different from AMD.

## Scene test

An Intel–AMD x86 Citadel two-shot using the **same approved actor IDs and wardrobe versions**. Produce three lighting-only passes: grey neutral, blue moonlit corridor, warm forge practicals. Face shape must not drift across lighting changes. Maintain separate overlays for dialogue and sci-fi effects.

## Model and provenance

Record generator, model ID/version, seed if available, input image SHA-256, `actor_id`, `wardrobe_id`, lens/composition, lighting rig, output revision, rights and explicit `human_approved: false` until reviewed. Image-model outputs are casting suggestions, not evidence that the faces are truly identical; do human side-by-side checks and correct edits.
