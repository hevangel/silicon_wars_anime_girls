# AMD model sheet generation record

- Output: [Illustrated model sheet](character_sheet.png)
- Input: [Original painted character reference](https://github.com/hevangel/silicon_wars_anime_girls/blob/d75dd93d8dbd2589fa7fe947df27eb1396df94b1/characters/amd/reference_card.jpg), cropped from the final Compute Triad datasheet
- Generator: Built-in image generation

## Prompt

Create a production-ready illustrated manga character model sheet for AMD, the adult Crimson Challenger in Silicon Wars. The supplied painted card is the identity and art-style reference. Match her athletic build, recognizable anime face with amber eyes, bright red high ponytail with braid and black band, crimson-and-black cropped tactical jacket, modular chiplet plating, fingerless gloves, and heavy boots. Keep the face, clothes, proportions, and accessories consistent across the drawing. Landscape 3:2 sheet on a plain warm light-gray background with professional anime linework and color shading. Across the upper area show four large, complete, neutral standing turnarounds at the same scale and baseline, front, three-quarter, true side profile, and back. Keep hands and boots in frame. Below, show three same-identity close-ups with clearly different expressions (smug, focused, surprised) and a small row of palette swatches. Use only these clear, small printed labels: "AMD", "FRONT", "THREE-QUARTER", "SIDE", "BACK", "SMUG", "FOCUSED", "SURPRISED". Give the drawings priority and enough separation for individual crops. No marketing copy, card UI, company logos, watermark, or background props. This is a practical model sheet for keeping character identity consistent across manga panels.

## Current reference card

- Output [Painted reference card](reference_card.jpg)
- Inputs [AMD model sheet](character_sheet.png) for identity and [Intel reference card](../intel/reference_card.jpg) for framing
- Generator: Built-in image generation

Create a polished portrait-oriented 2:3 anime character reference card for AMD, the adult Crimson Challenger in Silicon Wars. Image 1 (the red-haired AMD model sheet) is the only reference for the character's identity and clothing. Match her athletic build, amber eyes, intense red high ponytail with braid and dark hairband, crimson-and-black cropped tactical jacket, chiplet armor accents, gold hardware, headphones around the neck, and fingerless gloves. Show a large three-quarter portrait from the hips up, with the ponytail and face well framed, a bold confident smirk and a small glowing modular chiplet assembly near her raised hand. Image 2 (Intel's blue reference card) is only a layout and polish reference. Match its large portrait, narrow decorative frame and bottom nameplate, with a red, charcoal and gold palette suitable for AMD. Use understated crimson circuitry in a dark fabrication lab behind her. Render exactly two lines in the nameplate: "AMD" and "THE CRIMSON CHALLENGER". Keep the rest of the card free of company logos, watermarks, marketing and additional text. Match the character sheet's precise manga linework and color shading.

## Expression sheet

The built-in image generator used the [current model sheet](character_sheet.png) for identity and the user’s attached example for layout and acting. The output is [expressions.png](expressions.png).

Create a production-ready colored manga EXPRESSION SHEET for AMD, THE CRIMSON CHALLENGER, in Silicon Wars. Image 1 is this adult character's current model sheet. Follow it closely for the exact facial proportions, eyes, hairstyle, accessories, outfit, colors and body build. Image 2 is the user's layout and acting reference only. Use its one-full-body-plus-twelve-faces structure and range of expressions. Adult woman with a vivid red high ponytail and braided lock, amber eyes, gold drop earrings, black-and-red headphones around her neck, cropped crimson-and-black tactical jacket, black cargo trousers with gold hardware, fingerless gloves and heavy boots. Palette accents are crimson and warm gold. Her default expression is scrappy and alert. Let her grin and anger be energetic; smugness is an asymmetric competitive smirk; excitement is an open, triumphant grin.

Compose a landscape reference sheet on a plain warm off-white background with a tasteful thin border in the character's accent colors. Reserve the left 30 percent for the two-line nameplate "AMD" / "THE CRIMSON CHALLENGER" and exactly one complete standing front or slight three-quarter figure in a neutral pose, with all hair and boots inside the margin. On the right, place exactly 12 separately bordered head-and-shoulder cells in a precise 3-column, 4-row grid, with identical camera angle, head scale and lighting. Leave room for hair and head accessories in each cell. Keep character identity and outfit details fixed, changing only facial acting. Each cell has its single legible English label above the face. The complete exact row order is:

NEUTRAL | SMILING | EYES CLOSED
ANGRY | CRYING | SURPRISED
SMUG | FLUSTERED | SERIOUS
BLUSHING | EXCITED | OMINOUS

Distinguish all 12 clearly. Neutral is relaxed with open eyes; smiling is warm; eyes closed is calmly resting; angry has tight brows and an open sharp retort; crying has visible tears; surprised has wide eyes and a small open mouth; smug has one corner of the mouth raised; flustered has anxious brows and a small sweat drop; serious is alert with a level mouth; blushing is visibly flushed with a shy look; excited is an energetic delighted expression with bright eyes; ominous is quiet and shadowed, with a steady intimidating gaze. Use detailed colored anime linework and cel shading that match Image 1. Use only the nameplate and 12 exact English labels, with a crisp simple typeface. Keep every cell and label separate and readable. No other characters, layout panels, logos, watermark, or scenery.

## Chibi sheet (style variant)

- Output [Chibi sheet](chibi_sheet.png) (1920 x 1280)
- Input the current [model sheet](character_sheet.png) for identity; style rules from `bible/art_style.yaml` (`chibi`) and the `style_variants.chibi` block in her continuity.yaml

Create a polished landscape 3:2 anime CHIBI character sheet for AMD, THE CRIMSON CHALLENGER, an adult woman in Silicon Wars, in the chibi style variant. Image 1 is her approved model sheet and the strict identity and costume blueprint. Preserve her identity: bright red braided high ponytail with a black band, amber eyes, energetic grin, crimson-and-black cropped tactical jacket, modular chiplet plating with one strong chiplet emblem, headphones around her neck, fingerless gloves, and heavy boots. Render her as a super-deformed chibi character: large head, tiny energetic body, head-to-body ratio about 1:2.5, short simplified limbs, small rounded hands and feet, reduced armor segmentation, simplified boots, rounded cute shapes, clean manga line art, minimal shading, large simplified eyes and highly exaggerated expressions. Put four complete standing chibi turnarounds in a row on a pale neutral background, feet and ponytail fully in frame with comfortable outer margins: FRONT, THREE-QUARTER, SIDE, BACK, all at the same scale and proportions, the FRONT view leaning forward with a mischievous grin and a tiny fist-pump, with small floating chiplet motifs around her. Below them, include three chibi close-up expressions of the same face: SMUG, EXCITED, and POUTING, plus a small palette strip in crimson, black, charcoal, amber, and white. Use clear restrained labels, with only the text "AMD", "THE CRIMSON CHALLENGER", "CHIBI", "FRONT", "THREE-QUARTER", "SIDE", "BACK", "SMUG", "EXCITED", and "POUTING". Crisp cute manga linework matching Image 1's colors. Keep the sheet free of other characters, scenery, and technical marketing copy.
