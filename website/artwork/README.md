# Artwork portfolio

Serve the repository root and open `/website/artwork/`. The index links to independent artwork pages, each free to use its own theme below the shared Silicon Wars masthead. No build or JavaScript is required to browse; the ED Walk adds optional scroll buttons and the style index adds optional info dialogs.

## Sources

- `assets/ed-walk.webp`: web-sized derivative of `art/ed-walk/ed-walk-full.png`, resized to 10,000 × 935, WebP quality 88. The detail page also links to the untouched original.
- `assets/key-art.jpg`: JPEG derivative of the regenerated [concert key art](../../art/key-art/key-art.png), matching the AMD, Intel, and Nvidia model sheets. [Prompt, provenance, and before/after review](../../art/key-art/reviews/REVIEW.md). The earlier `导出/key-art.jpg` remains preserved.
- `assets/cyber-circuit-grid.webp` and `assets/cyber-circuit-{intel-fx01,amd-ax02,nvidia-nv09}.webp`: full-resolution WebP derivatives of `scratchpad/Silicon Wars Cyber Circuit Grid.png` (1672 × 941) and the three `scratchpad/ChatGPT Image Nov 19, 2026, 06_49_*.png` machine setting sheets (1448 × 1086) added to the [Key art](key-art/) showcase.
- `microsoft-styles/images/`: 16 original 784 × 1168 JPEGs from `scratchpad/microsoft-painting-styles.zip`. These are the imported source portraits.
- `microsoft-styles/images/*-studies.png`: One hundred and five ChatGPT ImageGen entries for the [style index](microsoft-styles/). Thirty-eight have four variants and sixty-seven use one study image each. The art appears in a lesson sequence, with guided questions that link to each study. The twelve technique boards use the classic cel portrait as a pose and costume reference. Most artistic-style entries use it as a character reference for new compositions. Memphis design, Rococo, Pointillism, Minimalism, Space Age design, Tonalism, and the studies on the Story, pattern, and perception, How pictures carry meaning, Objects, gesture, and rhythm, Work, craft, and spectacle, Space, atmosphere, and action, and Art you move around boards use the canonical [Microsoft reference card](../../characters/microsoft/reference_card.jpg) for character identity. The new Space Age scene pairs a rounded console and orange analog controls with a view of Earth. Tonalism uses a narrow blue-gray palette and a faint warm reflection on a river at dusk. The Story, pattern, and perception prompts show an office day in Egyptian registers, a shared meal with Mithila linework and borders, a walk among irises against a gold Rinpa screen, and a Photorealist view through reflective office glass. How pictures carry meaning shows a Harlem reading room linked by bands of light, an office opening inside an illuminated M, a vanitas arrangement at closing time, and a Kalighat-inspired joke about an empty executive chair. Objects, gesture, and rhythm shows a worn notebook on a chaekgeori shelf, the aftermath of a meeting through New Objectivity portraiture, a folder passed between wayang kulit puppets, and an Orphist walk among repeating electric lights. Work, craft, and spectacle uses a small-town radio repair shop, a reading nook with a climbing rose trellis pattern, a stage duet over a folder, and an idealized data-center crew. Space, atmosphere, and action shows a softly tinted street at twilight, a lobby with competing angles, a torn performance screen, and a painted box with two levels of a community computer fair. Art you move around shows a hanging mobile in a sunlit atrium, sandstone openings that frame sunrise, an ambiguous violet-lit room, and a rooftop meal at the center of a narrative quilt. The nine final roadmap images use the Microsoft reference card with built-in ImageGen. They show a repair clinic notice on a Swiss grid, a radio-part handoff in shallow stone, an incised vessel under celadon glaze, a repair scene made of repeated vector-like shapes, the workshop lit as a stylized 3D scene, a profile in a wax-resist textile repeat, a cup passed across an unwrapped Maya-inspired painted band, four puppet poses at a radio dial, and a portrait organized by the spacing of plotter-like contours. The seven video game graphics studies use the same Microsoft radio repair scene to compare NES sprite palettes, SNES color and layers, PlayStation 2D sprites, fixed-camera low-poly RPGs, arcade fighting models, HD-era surface detail, and a simulation of PS5-era ray-traced reflections.

The ED Walk was recomposited after the [height correction](../../art/ed-walk/reviews/height-correction/REVIEW.md); its source walkers, costumes, and lettering remain unchanged. The ED Walk index thumbnail intentionally shows a central excerpt; its detail page offers the complete panorama and an uncropped overview.

The catalog groups studies by shared visual lessons. Acrylic, graphite, linocut, screenprinting, and cyanotype use generated interpretations of their respective media and link to dated physical works in their info dialogs. The next five ImageGen studies show a mug examined in egg tempera, a mechanical street in etching, a train platform in lithography, a maintenance mural in buon fresco, and a badge handoff in pen and ink. The printmaking comparison reuses one woodblock quadrant and three full studies.

## Arm style course

`arm-styles/` is a 17-lesson course that teaches visual language from one character
in one pose. Every plate redraws Arm, the Pocket Architect, walking away with her
folded umbrella — the pose of the supplied reference — so only the medium changes:
105 styles, 219 plates planned, 38 of the styles with four variants each (canonical,
re-keyed, re-framed, material-extreme) and the rest as single studies, plus seven
video-game eras from NES to PS5 ray tracing.

- Style declares a mode: `pose` holds the reference staging, `language` lets a
  movement rebuild the composition around the same girl and street.
- Every plate is generated with Seedream from
  [`characters/arm/character_sheet.png`](../../characters/arm/character_sheet.png);
  the page header and colophon say so.
- Sources live in [`art/style-study/`](../../art/style-study/README.md): `plates.json`
  holds every prompt, each render carries a sidecar with its prompt hash, reference
  hash and image hash, and `sheets/` holds per-family contact sheets.
- `data.js` is generated by `tools/style_study/build_web.py` from that manifest;
  `assets/*.jpg` are 780 px web derivatives. Re-run the script after adding renders.
- Coverage is shown honestly rather than hidden: 65 of 219 plates are rendered
  (29.7%) and unfinished styles show a labelled pending slot. The image account hit
  its generation limit mid-build, so the remaining plates are specced but undrawn.
- Reference links point to Wikipedia and Smarthistory so students can go past the
  plates; no third-party artwork is copied into this directory.

## Broadcom style field guide

`broadcom-styles/` is a 9-chapter beginner field guide teaching 105 art styles and video game eras through one constant autumn walk featuring Broadcom (`characters/broadcom/character_sheet.png`).

- **Curriculum:** Nine progressive chapters (`data/chapters.js`, `data/styles-1.js`, `data/styles-2.js`, `data/styles-3.js`) covering Line & Print, Paint & Collage, Light & Camera, Flat Worlds & Gold, Emotion & Public Voices, Abstraction, Graphic Design & Futures, Craft & Architecture, and Video Game Eras (8-bit NES through PS5 ray tracing).
- **Plates:** 219 WebP images (`images/*.webp`, max width 780 px) covering all 38 four-variant styles (Daylight, Mood, Close-up, Material) and 67 single-study styles, plus two reference anchors (`ref-character-sheet.webp` and `ref-baseline-walk.webp`). Sources come from the Broadcom style studies in `scratchpad/Gemini_Generated_Image*.jpeg` and `scratchpad/broadcom-*.jpg`.

To add work, create a directory with an `index.html`, add an index entry with descriptive alt text, and record its source here. Keep page-specific styles scoped to a body class in `style.css` (or a separate stylesheet).
