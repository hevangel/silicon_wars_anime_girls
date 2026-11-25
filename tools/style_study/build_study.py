#!/usr/bin/env python3
"""Build the Arm cross-era art-style study: prompt library + plate manifest.

Writes art/style-study/prompts.json and art/style-study/PLATES.md.

Every plate is the same character (Arm, characters/arm/continuity.yaml) in the
walking-away pose of the user's reference image, rendered in one art-historical
medium. Styles whose point is a medium are held to the reference pose; styles
whose point is a visual language are allowed to restructure the composition
around the same subject and motifs.
"""

from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "art" / "style-study"

# --------------------------------------------------------------------------
# Immutable character block (characters/arm/continuity.yaml + art_prompt.md)
# --------------------------------------------------------------------------
ARM = (
    "Arm, the Pocket Architect: a petite 19-year-old British engineering apprentice, "
    "cool blue eyes, a long wavy silver ash-blonde high side ponytail tied with a "
    "blue-teal ribbon, layered bangs, a brass mechanical pencil tucked behind her "
    "right ear beside the ponytail, one eyebrow slightly raised and a wry half-smile. "
    "She wears a cropped blue-teal workshop jacket with brass hardware, stitched chest "
    "pockets and rolled cream cuffs, a small cream patch above her right chest pocket, "
    "a cream button-front shirt, a charcoal knee-length pleated skirt with a "
    "brass-buckled belt, and dark ankle-height lace-up work boots."
)

POSE = (
    "Her back is to the viewer: she is walking away down the path, seen entirely from "
    "behind at a three-quarter back angle, so the viewer sees her back, the back of her "
    "head and one cheek as she turns to look over her right shoulder toward the viewer. "
    "She is mid-stride on a pale stone footpath between black iron railings; her right "
    "hand carries a folded black umbrella low at her side, a tan shoulder bag hangs "
    "from her left shoulder, her left arm is lifted slightly. Beyond her: pale European "
    "stone roofs with chimneys and a small domed tower, autumn trees in orange and "
    "ochre, a broad pale sky. Tall thin vertical accents frame both edges. Do not turn "
    "her to face the camera."
)

INSPIRED = (
    "Keep the subject and motifs of the reference image — a young woman walking away "
    "with a folded umbrella, an autumn city of pale stone, iron railings, bare branches "
    "and a wide sky — but let this style's own grammar reorganise the picture space, "
    "viewpoint, scale and surface as that style demands."
)

PRESERVE = (
    "Arm's identity: silver ash-blonde side ponytail and blue-teal ribbon, cool blue "
    "eyes, brass pencil behind the ear, blue-teal cropped jacket with the cream chest "
    "patch, cream shirt, charcoal pleated skirt, dark lace-up boots."
)

FORBID = (
    "no other characters, no speech balloons, no caption or panel text, no signature, "
    "no watermark, no gallery frame, no colour swatch strip, no character-sheet "
    "turnaround or multiple views of the figure"
)

# Plates that must NOT be pulled back toward anime cel shading: the named medium has
# to be legible at a glance, or the whole study collapses into one look.
NO_GUARD = {"anime-cel-shading", "manga-ink-and-screentone", "pixel-art"}
GUARD = (
    "Medium fidelity: the plate must read as the named medium at a glance. Do not fall "
    "back on anime cel shading, glossy digital rendering or clean uniform line art "
    "unless that is the medium being studied."
)

# --------------------------------------------------------------------------
# Variant axes. Every four-variant style gets the same four moves so the four
# plates read as one study rather than four unrelated pictures.
# --------------------------------------------------------------------------
AXES = [
    (
        "canonical",
        "straight, textbook application of the medium; clear daylight, full figure, "
        "the reference staging held intact",
    ),
    (
        "re-keyed",
        "the same staging and the same medium, re-keyed to late-afternoon rain: "
        "cooler shadows, deeper saturated darks, wet stone",
    ),
    (
        "re-framed",
        "the same medium and mood, re-framed three-quarter from the waist up so the "
        "street compresses behind her and the surface handling can be read closely",
    ),
    (
        "material-extreme",
        "the same subject and pose with the medium's signature artifacts pushed to the "
        "front: the surface, edge behaviour and texture become the subject",
    ),
]

# --------------------------------------------------------------------------
# Styles. mode: "pose" holds the reference pose; "language" lets the style
# restructure the composition around the same subject.
# --------------------------------------------------------------------------
S = []
def st(slug, label, family, count, mode, medium, extra=""):
    S.append(dict(slug=slug, label=label, family=family, count=count,
                  mode=mode, medium=medium, extra=extra))

# --- Manga panel -----------------------------------------------------------
F = "Manga panel"
st("anime-cel-shading", "Anime cel shading", F, 4, "pose",
   "Japanese animation cel art: clean tapered ink line art, flat matte colour fills, "
   "hard two-tone cel shadows with crisp boundaries, small white specular highlights "
   "on hair and boots, painted background in a slightly softer hand than the figure.")
st("manga-ink-and-screentone", "Manga ink and screentone", F, 4, "pose",
   "Black-and-white manga: brush-and-pen line art with varying line weight, hatching "
   "for shadow, dot screentone and tone-on-tone gradient screen for the skirt, sky and "
   "stonework; pure black solids, no colour, white paper ground.")
st("digital-painting", "Digital painting", F, 4, "pose",
   "Digital painting in the modern conceptual-illustration manner: soft opaque brush "
   "strokes, lost-and-found edges, layered atmospheric depth, warm rim light against "
   "cool ambient shadow, deliberate overpainting at the silhouette.")
st("pixel-art", "Pixel art", F, 4, "pose",
   "Hand-placed pixel art on a strict grid with a limited indexed palette, one-pixel "
   "dark outlines, ordered dithering for gradients, no anti-aliasing, no sub-pixel "
   "detail; readable silhouette at thumbnail size.")

# --- Drawing, paint, and paper -------------------------------------------
F = "Drawing, paint, and paper"
st("watercolor", "Watercolour", F, 4, "pose",
   "Transparent watercolour on cold-pressed cotton paper: wet-in-wet blooms and "
   "backruns, pigment pooling at the edges, reserved white paper for the brightest "
   "lights, soft graphite underdrawing left visible, muted earth-and-teal palette.")
st("oil-painting", "Oil painting", F, 4, "pose",
   "Oil on stretched linen: loaded opaque brushwork, scumbled half-tones, glazed "
   "shadow passages, visible impasto ridges in the light, warm-cool colour vibration, "
   "soft feathered edges against crisp accents.")
st("gouache", "Gouache", F, 4, "pose",
   "Opaque gouache: flat matte blocks of colour laid over one another, dry-brush "
   "passages where the paper tooth shows, crisp shapes with soft chalky edges, "
   "slightly chalk-lightened pastel palette, no glossy highlights.")
st("colored-pencil", "Coloured pencil", F, 4, "pose",
   "Waxy coloured pencil on fine tooth paper: layered crosshatched strokes, visible "
   "individual pencil marks, burnished areas where the wax is pressed smooth, paper "
   "tooth catching light in the open passages, gentle tonal build rather than flat fill.")
st("charcoal-drawing", "Charcoal drawing", F, 4, "pose",
   "Vine and compressed charcoal on toned paper: smudged soft masses, dragged and "
   "lifted highlights with a kneaded eraser, sharp compressed-charcoal accents, "
   "dusty halos around the darks, a few white chalk touches.")
st("soft-pastel", "Soft pastel", F, 4, "pose",
   "Soft pastel on tinted pastel paper: powdery blended passages, sticks laid on their "
   "side for broad strokes, crisp edges cut with the tip, the paper's colour breathing "
   "through the gaps, velvety luminous light.")
st("paper-collage", "Paper collage", F, 4, "pose",
   "Cut-paper collage: shapes torn and scissor-cut from coloured and printed paper, "
   "layered with visible edges and soft drop shadows, misregistered overlaps, a few "
   "halftone and map fragments, glue sheen, no drawn line where paper can do the work.")
st("acrylic-painting", "Acrylic painting", F, 1, "pose",
   "Acrylic on canvas: fast-drying flat opaque strokes with crisp plastic edges, "
   "a hard matte film, some thin translucent washes over dry paint, uniform "
   "non-yellowing surface, brighter and flatter than oil.")
st("egg-tempera", "Egg tempera", F, 1, "pose",
   "Egg tempera on gessoed panel: tiny parallel hatched strokes layered over a "
   "white ground, luminous translucent colour, hard eggshell-smooth surface, "
   "crisp dry edges, the light seeming to come from inside the paint.")
st("buon-fresco", "Buon fresco", F, 1, "pose",
   "Buon fresco: pigment in lime plaster while it is still wet, matte chalky colour "
   "fused into the wall, broad decisive strokes, faint giornata joins between "
   "sections of plaster, slight lime bloom, the wall's texture under everything.")
st("graphite-drawing", "Graphite drawing", F, 1, "pose",
   "Graphite on smooth Bristol board: silver-grey tonal range built from hatching "
   "and smudging, sharp 2H detail against soft 6B masses, erased highlights, "
   "a whisper of graphite dust, no colour at all.")
st("pen-and-ink-illustration", "Pen and ink illustration", F, 1, "pose",
   "Pen-and-ink illustration: flexible nib line of swelling and tapering weight, "
   "dense crosshatching and stipple for tone, deliberate hatching direction, "
   "pure black ink on white, every value made of line.")
st("ink-wash", "Ink wash", F, 1, "pose",
   "Ink wash on sized paper: single ink diluted through many greys, wet blooms and "
   "tide marks, dry brush dragged over texture, one dark calligraphic accent, "
   "a large unpainted breathing space.")

# --- Prints, photographs, and camera vision -------------------------------
F = "Prints, photographs, and camera vision"
st("woodblock-inspired-print", "Woodblock-inspired print", F, 4, "pose",
   "Woodblock print: flat areas of unmodulated colour from separate blocks, a firm "
   "keyblock outline that thins and swells, visible woodgrain and goma-zuri speckle, "
   "bleed of the water-based ink into the paper edge, a small registry margin.")
st("ukiyo-e", "Ukiyo-e", F, 4, "pose",
   "Ukiyo-e woodblock print in the manner of the floating world: elegant flowing "
   "keyblock line, flat Prussian-blue and beni-e reds with bokashi sky gradation, "
   "patterned textile detail, a cartouche panel left empty, the figure stylised to the "
   "kanzōshi silhouette.")
st("pictorialist-photography", "Pictorialist photography", F, 1, "pose",
   "Pictorialist photograph circa 1900: soft-focus gum-bichromate or bromoil printing, "
   "hazy diffusion, warm sepia-to-platinum tonality, visible paper texture and brush "
   "marks in the emulsion, a vignetted frame.")
st("photorealism", "Photorealism", F, 1, "pose",
   "Photorealistic rendering: 50 mm lens at eye level, shallow depth of field, "
   "physically accurate skin, wool, denim and wet stone, natural overcast light, "
   "fine film grain, absolutely no visible brushwork.")
st("linocut", "Linocut", F, 1, "pose",
   "Linocut relief print: bold gouge marks, large uncut black or single-colour masses, "
   "white lines where the block was cut away, slight ink squash at the edges, visible "
   "linoleum texture in the flat areas.")
st("copperplate-etching", "Copperplate etching", F, 1, "pose",
   "Copperplate etching: bitten lines of varying fineness, dense crosshatching in the "
   "shadows, occasional foul-biting, plate mark around the image, warm off-white laid "
   "paper.")
st("lithography", "Lithography", F, 1, "pose",
   "Stone lithography: greasy crayon-and-tusche drawing, granular crayon texture on "
   "the stone, soft wash-like tonal passages, faint stone grain in the flats, printer's "
   "registration, slightly grey-black ink on cream paper.")
st("screenprinting", "Screenprinting", F, 1, "pose",
   "Screenprint: a few flat spot-colour layers, hard-edged misregistration, ink pushed "
   "through the mesh leaving a faint squeegee streak, opaque colour over colour, no "
   "gradients except where a halftone dot is visible.")
st("cyanotype", "Cyanotype", F, 1, "pose",
   "Cyanotype contact print: monochrome Prussian-blue image on textured watercolour "
   "paper, white where objects blocked the light, brush-stroked emulsion border, "
   "sun-bleached tonal range, one or two faint chemical stains.")
st("documentary-photography", "Documentary photography", F, 1, "pose",
   "Black-and-white documentary photograph: 35 mm reportage, available light, grainy "
   "high-contrast print, caught mid-gesture, the street's real clutter left in, "
   "a slight tilt and no staging.")

# --- Stories on walls and pages ------------------------------------------
F = "Stories on walls and pages"
st("persian-manuscript-painting", "Persian manuscript painting", F, 4, "pose",
   "Persian manuscript painting: flattened tilted ground, mineral pigments — lapis, "
   "vermilion, gold — fine brush outlines, stylised cloud bands and blossoming trees, "
   "a carpet-like field of pattern, gold-flecked margin, no cast shadow.")
st("byzantine-mosaic", "Byzantine-inspired mosaic", F, 4, "pose",
   "Byzantine mosaic: tesserae of glass and stone set in mortar, gold-ground field, "
   "frontal hieratic placement, dark contour lines around forms, grout lines visible "
   "between every tile, slight irregular setting, a shallow banded border.")
st("stained-glass", "Stained glass", F, 4, "pose",
   "Stained glass window: thick lead cames dividing the image into jewel-coloured "
   "panes, cathedral reds, cobalt and amber, painted grisaille detail fired onto the "
   "glass, bubbles and streaks in the glass, backlit with light pouring through.")
st("ancient-egyptian-wall-painting", "Ancient Egyptian wall painting", F, 1, "pose",
   "Ancient Egyptian tomb painting: fresco secco on plaster, figures in composite view, "
   "strict registers, red-ochre and Egyptian-blue and green mineral pigments, black "
   "contour line, flat fill, a band of hieroglyph-like marks left abstract, chipped "
   "plaster at the edges.")
st("greek-vase-painting", "Greek black-figure and red-figure vase painting", F, 1, "pose",
   "Greek vase painting: black-figure silhouette with incised detail on one side of "
   "the design and red-figure reserve line on the other, meander border, added white "
   "and purple accents, the image wrapped across the curve of a ceramic body.")
st("mughal-album-painting", "Mughal album painting", F, 1, "pose",
   "Mughal album painting: fine opaque watercolour and gold on paper, delicate "
   "single-hair brushwork, a jewel-like border of gold rules and floral margins, "
   "softly modelled but flattened space, a flowering terrace and a marble balustrade.")
st("maya-painted-ceramics", "Classic Maya painted ceramics", F, 1, "pose",
   "Classic Maya painted ceramic: slip-painted calligraphic line in red and black on "
   "a cream ground, the image wound around a cylindrical vessel, a band of glyph-like "
   "blocks at the rim, warm terracotta and iron-oxide palette, slight erosion.")
st("medieval-manuscript-illumination", "Medieval European manuscript illumination", F, 1, "pose",
   "Medieval illumination: egg-tempera and gold leaf on vellum, a framed miniature "
   "with a burnished gold ground, diaper pattern in the border, Gothic script-like "
   "rubric marks left decorative, flat bright colour, punched gold tooling.")

# --- Pattern, craft, and objects -----------------------------------------
F = "Pattern, craft, and objects"
st("art-nouveau", "Art Nouveau", F, 4, "pose",
   "Art Nouveau poster and panel: whiplash sinuous contour, a heavy decorative "
   "outline, muted sage-olive and dusty violet with gold accents, hair and drapery "
   "resolved into ornamental tendrils, stylised foliage framing the figure, flat "
   "colour inside the line, lithographic texture.")
st("mithila-painting", "Mithila painting", F, 1, "pose",
   "Mithila (Madhubani) painting: fine double-line outlines, dense filling of every "
   "shape with hatching, dots and comb patterns, natural pigments — lampblack, "
   "turmeric yellow, indigo, vermilion — on handmade paper, no empty space.")
st("rinpa", "Rinpa", F, 1, "pose",
   "Rinpa school painting: tarashikomi pooled-ink bloom, gold-leaf cloud fields, "
   "bold simplified natural forms, a few confident strokes, generous empty space, "
   "decorative seasonal motifs, quiet luxury.")
st("korean-chaekgeori", "Korean chaekgeori", F, 1, "pose",
   "Korean chaekgeori still-life: trompe-l'oeil bookshelf arrangement seen from a high "
   "frontal viewpoint, screen-painting flatness, mineral pigments on paper, objects of "
   "scholarship stacked and overlapping, decorative patterned covers, no cast shadow.")
st("carved-relief", "Carved relief", F, 1, "pose",
   "Bas-relief carving: the figure and street cut in shallow relief from a single "
   "stone or plaster block, undercut edges, chisel marks, raking light from one side "
   "so the forms read only through shadow, a flat uncarved ground.")
st("ceramic-vessel-glazing", "Ceramic vessel and glazing", F, 1, "pose",
   "Ceramic vessel: the image painted in glaze on a thrown porcelain or stoneware "
   "body, celadon and iron-slip palette, crazing and kiln variation, glossy highlights "
   "following the curve of the pot, a foot ring and throwing rings visible.")
st("ayacucho-retablo", "Ayacucho retablo", F, 1, "pose",
   "Ayacucho retablo: a small wooden portable altar box with painted plaster figures "
   "in shallow niches, bright Andean pigments, gold-painted arches and a gabled roof, "
   "hand-carved and slightly crude, warm candlelight, cast shadow inside the box.")
st("narrative-story-quilts", "Narrative story quilts", F, 1, "pose",
   "Narrative story quilt: appliqued and pieced cotton, visible running-stitch quilting "
   "in fan and grid patterns, bold printed fabrics for the sky and foliage, figure "
   "built from sewn shapes, slightly irregular seam lines, a bound edge.")
st("batik", "Batik", F, 1, "pose",
   "Batik: wax-resist dye on cotton, characteristic crackle veining where the wax "
   "cracked, layered waxing and dyeing, indigo and soga-brown palette, a canting-drawn "
   "fine line, soft bleeding at the colour boundaries.")
st("rococo", "Rococo", F, 1, "pose",
   "Rococo painting: pastel rose, celadon and pearl palette, feathery loaded brushwork, "
   "gilded C-scroll and shellwork ornament, an airy park or salon setting, flirtatious "
   "light, everything weightless and in motion.")
st("arts-and-crafts", "Arts and Crafts", F, 1, "pose",
   "Arts and Crafts movement design: hand-printed flat pattern, muted vegetable-dye "
   "palette, a strong repeating motif of leaves and grain, honest visible craft, "
   "hand-set lettering-like ornament, slight ink irregularity from hand printing.")

# --- Stage a figure or a room -------------------------------------------
F = "Stage a figure or a room"
st("renaissance-perspective", "Renaissance perspective", F, 4, "pose",
   "Italian Renaissance: one-point linear perspective with a measurable vanishing "
   "point, architectural stage set, balanced pyramidal grouping, sfumato modelling, "
   "earth pigments with azurite sky, tempera-and-oil smoothness, a calm rational light.")
st("baroque", "Baroque", F, 4, "pose",
   "Baroque painting: a single raking light source, deep tenebrous shadow swallowing "
   "half the picture, diagonal composition and twisting movement, warm ochre flesh "
   "against cold dark, loose loaded brushwork, theatrical drama.")
st("neoclassicism", "Neoclassicism", F, 4, "pose",
   "Neoclassical painting: severely clear contour, restrained cool palette, "
   "archaeological Roman detail, shallow frieze-like staging, even sculptural light, "
   "smooth invisible brushwork, moral gravity.")
st("trompe-loeil", "Trompe-l'oeil", F, 4, "pose",
   "Trompe-l'oeil: the scene painted to fool the eye as a physical object — a torn "
   "poster or a print pinned to a board, painted nails and their cast shadows, a "
   "painted curling corner and a painted fold, hyper-precise detail, the wall's own "
   "surface continuing around the illusion.")
st("stylized-3d-rendering", "Stylised 3D rendering", F, 1, "pose",
   "Stylised 3D render: toon-shaded or hand-painted-texture game character shading, "
   "clean normal-mapped surfaces, soft ambient occlusion, a rim light, subtle "
   "subsurface warmth in the skin, physically plausible but non-photoreal materials.")

# --- Work and public life ------------------------------------------------
F = "Work and public life"
st("mexican-muralism", "Mexican muralism", F, 4, "pose",
   "Mexican muralism: monumental public fresco, strong dark contour, earthy reds and "
   "ochres with turquoise accents, compressed crowded space, workers' hands and tools "
   "enlarged, a shallow architectural frame, matte lime-plaster surface.")
st("kalighat-painting", "Kalighat painting", F, 1, "pose",
   "Kalighat pat painting: sweeping bold brush outline, flat colour washes, large "
   "almond eyes, abbreviated features, a plain ground with a single prop, cheap "
   "watercolour on mill paper, confident and quick.")
st("french-realism", "French Realism", F, 1, "pose",
   "French Realism: sober earth palette, honest unidealised observation, visible but "
   "restrained brushwork, ordinary daylight, a contemporary street or workplace, "
   "no theatrical lighting, deep quiet greys.")
st("harlem-renaissance-mural", "Harlem Renaissance mural and illustration", F, 1, "pose",
   "Harlem Renaissance illustration: graphic flat shapes with rhythmic repetition, "
   "warm brown, gold and deep blue palette, stylised profiles and hands, "
   "jazz-like syncopated pattern, linocut and gouache hybrid, dignified and modern.")
st("new-objectivity", "New Objectivity", F, 1, "pose",
   "New Objectivity (Neue Sachlichkeit): hard precise draughtsmanship, acid cool "
   "palette, unsentimental sharp focus on every surface, still, eerie clarity, "
   "a faintly menacing evenness of light.")
st("american-regionalism", "American Regionalism", F, 1, "pose",
   "American Regionalism: rounded sturdy forms, warm local colour, rolling rural or "
   "small-town setting, clear narrative legibility, tempera smoothness with a "
   "handmade warmth, optimistic plain-spoken light.")
st("soviet-socialist-realism", "Soviet Socialist Realism", F, 1, "pose",
   "Socialist Realism: heroic low viewpoint, sunlit optimism, polished academic "
   "finish, industrious props and banners, a bright confident palette, monumental "
   "scale implied, unambiguous narrative.")
# --- Light, weather, and landscape ----------------------------------------
F = "Light, weather, and landscape"
st("chinese-ink-landscape", "Chinese ink landscape", F, 4, "pose",
   "Chinese ink landscape (shan shui) on paper or silk: monochrome ink with a few "
   "mineral accents, angular axe-cut texture strokes, wet ink bleeding into dry, "
   "misty void between near and far, a vertical hanging-scroll format, sealed and "
   "inscribed in an empty corner.")
st("impressionism", "Impressionism", F, 4, "pose",
   "Impressionist painting: broken flickering strokes of pure colour laid side by side, "
   "violet-blue shadows instead of black, light as the real subject, edges dissolved, "
   "a wet street reflecting a high-key sky, plein-air immediacy.")
st("romanticism", "Romanticism", F, 4, "pose",
   "Romantic painting: a small figure against an overwhelming sky, storm light "
   "breaking through cloud, sublime scale, deep glazed darks, warm sunlit accent "
   "against cold blue-grey, emotional weather.")
st("pointillism", "Pointillism", F, 1, "pose",
   "Pointillism: the whole image built from small separate dots of pure colour, "
   "optical mixture at a distance, a luminous vibrating surface, complementary dots "
   "in the shadows, a pointillist dotted border.")
st("tonalism", "Tonalism", F, 1, "pose",
   "Tonalism: a narrow range of muted greys, browns and slates, soft atmospheric veil, "
   "mist swallowing the middle distance, low tonal contrast, quiet twilight, "
   "almost monochrome.")

# --- Emotion, dreams, and metaphor --------------------------------------
F = "Emotion, dreams, and metaphor"
st("symbolism", "Symbolism", F, 4, "language",
   "Symbolist painting: dreamlike stillness, ambiguous allegorical props, muted "
   "mystic palette of violet, verdigris and gold, flattened decorative space, "
   "figures suspended between waking and sleep, an unreadable symbolic object "
   "replacing a literal one.")
st("expressionism", "Expressionism", F, 4, "language",
   "Expressionist painting: violent distorted contour, raw unmixed colour, slashed "
   "and scraped brushwork, warped perspective, the city leaning in, emotional "
   "distortion of anatomy rather than description.")
st("surrealism", "Surrealism", F, 4, "language",
   "Surrealist painting: hyper-clear dream logic, impossible juxtapositions, objects "
   "rendered with photographic exactness in an illogical arrangement, long impossible "
   "shadows, a still unnerving emptiness.")
st("fauvism", "Fauvism", F, 4, "language",
   "Fauvism: arbitrary non-naturalistic colour at full saturation, raw brushstrakes "
   "straight from the tube, colour doing the work of light and shadow, "
   "a flattened vibrating surface, complementary clashes left unresolved.")
st("dada-photomontage", "Dada photomontage", F, 4, "language",
   "Dada photomontage: cut newspaper and photographic fragments pasted at absurd "
   "angles, hard scissor edges, mismatched print halftones and paper tones, "
   "typographic scraps torn mid-word, deliberate bad registration, black-and-white "
   "with one or two flat colour accents.")
st("pre-raphaelite", "Pre-Raphaelite painting", F, 1, "language",
   "Pre-Raphaelite painting: hard even detail across the whole canvas, jewel-bright "
   "colour over white ground, literary medievalising props, a dense tapestry of "
   "leaf and flower, melancholy stillness.")
st("dutch-vanitas", "Dutch vanitas still life", F, 1, "language",
   "Dutch vanitas still life: a table-top arrangement lit from the left, a skull, "
   "an hourglass, an overturned glass, a snuffed candle, a book and a peeled lemon, "
   "velvet darkness behind, microscopic realism, one moralising glint.")
# --- Abstraction, geometry, and optical motion ---------------------------
F = "Abstraction, geometry, and optical motion"
st("orphism", "Orphism", F, 1, "language",
   "Orphism: overlapping translucent discs and prismatic colour planes, pure colour "
   "as structure, simultaneous contrast, a light-filled rhythmic composition, "
   "form dissolved into colour chords.")
st("generative-plotter-art", "Generative and plotter art", F, 1, "language",
   "Generative plotter drawing: thousands of uniform pen lines on paper, moire and "
   "interference patterns from algorithmic hatching, a single ink colour on white, "
   "the ghost of the algorithm visible, plotter pen texture at line ends.")
st("de-stijl", "De Stijl", F, 1, "language",
   "De Stijl: a strict grid of black lines of even weight, rectangles of primary red, "
   "yellow and blue plus white and grey, asymmetrical balance, no diagonals, no "
   "texture, the subject reduced to its rhythmic structure.")
st("minimalism", "Minimalism", F, 1, "language",
   "Minimalist art: the subject reduced to a few industrial, identical forms in a "
   "neutral space, matte uniform surface, no gesture, no detail, meaning carried by "
   "placement and interval alone.")
st("cubism", "Cubism", F, 4, "language",
   "Analytic and synthetic Cubism: the subject broken into faceted planes shown from "
   "several viewpoints at once, monochrome ochre-and-grey palette, stencilled "
   "letterforms, a collage element of newsprint or woodgrain, shallow tipped-up space.")
st("futurism", "Futurism", F, 4, "language",
   "Futurist painting: everything in simultaneous motion, multiplied overlapping "
   "phases of the figure, force lines and velocity vectors, fractured luminous planes, "
   "a machine-age palette of steel grey, orange and electric blue.")
st("abstract-expressionism", "Abstract Expressionism", F, 4, "language",
   "Abstract Expressionism: a large all-over field of poured, dripped and slashed "
   "paint, the figure only a ghost inside the gesture, unstretched-canvas rawness, "
   "layered skeins of colour, the whole surface equally important.")
st("op-art", "Op Art", F, 4, "language",
   "Op Art: black-and-white geometric pattern engineered to vibrate, concentric "
   "lines warping across a bulging form, high-contrast moire, no shading except "
   "what the pattern does to the eye, perfectly hard edges.")
# --- Graphic design and public messages ----------------------------------
F = "Graphic design and public messages"
st("constructivism", "Constructivism", F, 4, "language",
   "Constructivist design: red, black and off-white only, diagonal dynamic axis, "
   "photographic fragment cut against flat geometric form, heavy sans-serif blocks "
   "set on the diagonal, industrial facture, the whole poster built like a machine part.")
st("art-deco", "Art Deco", F, 4, "language",
   "Art Deco: stepped geometric silhouette, symmetrical fan and chevron ornament, "
   "lacquered black and gold with jade and cream, sleek elongated streamlining, "
   "metallic sheen, a sunburst halo behind the figure.")
st("bauhaus-graphic-design", "Bauhaus graphic design", F, 4, "language",
   "Bauhaus graphic design: elementary geometric forms, a strict asymmetric grid, "
   "primary palette plus black, lowercase sans-serif type set flush and rotated, "
   "photographic element reduced to a circle or rectangle, generous white field.")
st("pop-art", "Pop Art", F, 4, "language",
   "Pop Art: commercial screenprint look, flat saturated primaries, thick black "
   "contour, Ben-Day dot shading, deliberate misregistration, repetition of the "
   "image in a grid, mass-produced sheen.")
st("swiss-style", "Swiss Style", F, 1, "language",
   "Swiss Style (International Typographic Style): an objective photographic image "
   "cropped on a strict grid, Helvetica-like lowercase type flush left, massive "
   "negative space, two colours plus black, no ornament, rational hierarchy.")
st("vector-illustration", "Vector illustration", F, 1, "language",
   "Vector illustration: perfectly smooth Bezier curves, flat fills with hard-edged "
   "shadow shapes, uniform stroke weights, geometric simplification, a limited brand "
   "palette, no texture at all.")
st("psychedelic-poster-art", "Psychedelic poster art", F, 1, "language",
   "Psychedelic concert-poster art: melting warped letterforms, acid complementary "
   "colour on dark ground, organic liquid line that swells and thins, symmetry "
   "radiating from a centre, offset ink layers, a vibrating optical buzz.")
# --- Objects and imagined futures ----------------------------------------
F = "Objects and imagined futures"
st("memphis-design", "Memphis design", F, 1, "language",
   "Memphis design: clashing brights, black squiggles and grids over pastel grounds, "
   "asymmetric pattern fields, laminate and terrazzo, deliberately 'bad' taste, "
   "1950s-kitsch motifs blown up.")
st("space-age-design", "Space Age design", F, 1, "language",
   "Space Age design: white and silver with orange and clear acrylic, molded capsule "
   "and dome shapes, seamless plastic, orbiting-ring motifs, optimistic futurism of "
   "the 1960s, glossy vacuum-formed surfaces.")
st("afrofuturism", "Afrofuturism", F, 1, "language",
   "Afrofuturist image: ornate futuristic regalia fusing West African textile pattern "
   "with tech, deep indigo and gold, glowing circuitry woven into cloth, a cosmic sky "
   "over an imagined city, proud frontal presence.")
# --- Buildings, sites, and installations ---------------------------------
F = "Buildings, sites, and installations"
st("precisionism", "Precisionism", F, 1, "language",
   "Precisionism: crisp hard-edged industrial forms, smooth impersonal surfaces, "
   "raking geometric light and long clean shadow, cool grey-blue palette, no people "
   "in the way, a factory or grain elevator as cathedral.")
st("brutalist-architecture", "Brutalist architecture", F, 1, "language",
   "Brutalist architecture: board-marked raw concrete masses, deep shadow under "
   "cantilevers, repetitive window cells, monolithic scale dwarfing the figure, "
   "monochrome grey with one warm accent, overcast light.")
st("deconstructivist-architecture", "Deconstructivist architecture", F, 1, "language",
   "Deconstructivist architecture: shards and skewed planes colliding, non-Euclidean "
   "folding surfaces, titanium and glass, gravity apparently violated, fractured "
   "reflections, a controlled chaos of competing axes.")
st("land-art", "Land Art", F, 1, "language",
   "Land Art: a vast earthwork cut into a desert or salt flat, aerial or distant "
   "viewpoint, the figure a tiny measure of scale, raw excavated earth, "
   "documentary photograph of the site, huge sky.")
st("light-and-space", "Light and Space", F, 1, "language",
   "Light and Space art: a minimal translucent installation, resin and frosted glass, "
   "colour existing only as glow, soft gradient of ambient light, no hard edges, "
   "the figure dissolving at the boundary, immersive haze.")
# --- Performance, puppetry, and kinetic art ------------------------------
F = "Performance, puppetry, and kinetic art"
st("wayang-kulit", "Wayang kulit", F, 1, "language",
   "Wayang kulit shadow puppet: flat articulated leather figure with elaborately "
   "pierced filigree, painted gold and red on the puppet side, its black silhouette "
   "cast on a backlit cotton screen, the puppet rod visible, warm lamp glow.")
st("stop-motion", "Stop-motion", F, 1, "language",
   "Stop-motion puppet still: a physical armature puppet of cloth, silicone and resin "
   "on a built miniature set, visible seam lines and fabric weave, practical lighting, "
   "shallow depth of field, slight frame-to-frame imperfection in the pose.")
st("ballets-russes-stage-design", "Ballets Russes stage design", F, 1, "language",
   "Ballets Russes stage design: a painted backcloth in vivid Orientalist colour, "
   "steep raked stage, figured costume in bold flat pattern, dramatic coloured "
   "footlights, decorative border masking the wings, the whole image a theatrical flat.")
st("gutai", "Gutai", F, 1, "language",
   "Gutai performance painting: paint hurled, poured and dragged across the surface "
   "by the body in motion, footprints and handprints, torn paper, raw violent colour "
   "against bare ground, the record of an action rather than a picture.")
st("kinetic-sculpture", "Kinetic sculpture", F, 1, "language",
   "Kinetic sculpture: suspended polished metal elements turning in air, reflected "
   "light thrown across the room, motion blur on the moving parts, engineering "
   "hardware visible, cool industrial palette, the figure standing among them.")

# --- Video game eras -----------------------------------------------------
F = "Video game eras"
st("nes-era", "NES-era sprite", F, 1, "pose",
   "Authentic 8-bit NES game art: the whole picture drawn on a 256x240 logical grid and "
   "then enlarged with hard nearest-neighbour squares, so a single pixel is a big visible "
   "block; the fixed 54-colour NES palette, at most three colours plus black for the "
   "figure, no gradients anywhere, black used for outline and flat shadow, a repeating "
   "16x16 tiled background and a flat sky band.")
st("snes-era", "SNES-era sprite", F, 1, "pose",
   "Authentic 16-bit SNES game art: 256x224 logical resolution enlarged with hard "
   "nearest-neighbour blocks; 15 colours per palette row respected, three-to-four step "
   "shading ramps, dithering only where a gradient is unavoidable, two parallax "
   "background layers with paler distant rooftops, a Mode-7-style receding path, a "
   "crisp black sprite outline.")
st("ps1-2d", "PlayStation 1 era 2D", F, 1, "pose",
   "Late-1990s PlayStation 2D game art: a 320x240 logical frame scaled up, a painted "
   "sprite standing on a pre-rendered 3D background plate, visible colour banding from "
   "15-bit colour, ordered dithering in the sky gradient, soft compressed-video smear "
   "on the backdrop, hard sprite edges.")
st("ps1-3d-lowpoly", "PlayStation 1 era 3D (low polygon)", F, 1, "pose",
   "1997 PlayStation low-polygon 3D: roughly 300-800 triangles for the figure, "
   "flat-shaded or affine-textured polygons with visible warping, 256x256 textures, "
   "no dynamic lighting, vertex snapping, a pre-rendered backdrop, FF7-era fidelity.")
st("doa-era-3d", "Dreamcast / Dead or Alive era 3D", F, 1, "pose",
   "Late-1990s arcade 3D at Dead or Alive fidelity: around 10k polygons, smooth "
   "skinned character mesh, per-vertex lighting, 512px textures, hair as alpha-mapped "
   "cards, a glossy specular sheen, simple shadow blob on the floor.")
st("ps3-ps4-era-3d", "PS3 / PS4 era 3D", F, 1, "pose",
   "2010s console real-time 3D: 50-100k polygon character, normal and specular maps, "
   "physically based-ish shading, baked ambient occlusion, cloth and hair simulation, "
   "bloom and depth of field, a fully modelled environment.")
st("ps5-era-raytracing", "PS5 era 3D with ray tracing", F, 1, "pose",
   "Current-generation real-time 3D with ray tracing: path-traced reflections in wet "
   "stone and puddles, accurate global illumination bounce, subsurface skin "
   "scattering, strand-groom hair, volumetric light shafts, filmic tone mapping, "
   "photoreal materials at 4K detail.")


def build():
    plates = []
    for style in S:
        n = style["count"]
        pose_block = POSE if style["mode"] == "pose" else INSPIRED
        for i in range(n):
            if n == 1:
                axis_name, axis_text = (
                    "single study",
                    "one representative plate for this style; hold the reference "
                    "staging as closely as the medium allows",
                )
            else:
                axis_name, axis_text = AXES[i]
            pid = f"{style['slug']}-v{i + 1:02d}"
            text = (
                "Task category: Illustration, Concept Art, and Narrative Visuals\n"
                "Intended use: one plate in a cross-era art-style study sheet of the "
                "Silicon Wars character Arm; a technique reference for the project, "
                "not a story panel\n"
                f"Core request: redraw Arm, in the reference pose, as a study in "
                f"{style['label']}\n"
                f"Character, identity must not drift: {ARM}\n"
                f"Subject, pose and staging: {pose_block}\n"
                f"Style or medium: {style['medium']}\n"
                f"Variant {i + 1} of {n} — {axis_name}: {axis_text}\n"
                "Composition and orientation: portrait plate, one single figure, "
                "full figure except where the variant calls for a closer crop\n"
                "Must preserve: " + PRESERVE + "\n"
                "Must not include: " + FORBID
            )
            if style["extra"]:
                text += "\nNote: " + style["extra"]
            if style["slug"] not in NO_GUARD:
                text += "\n" + GUARD
            plates.append({
                "id": pid,
                "style": style["slug"],
                "style_label": style["label"],
                "family": style["family"],
                "variant": i + 1,
                "variant_count": n,
                "variant_axis": axis_name,
                "mode": style["mode"],
                "medium": style["medium"],
                "prompt": text,
                "file": f"art/style-study/renders/{pid}.png",
                "status": "pending",
            })
    return plates


def main():
    (OUT / "renders").mkdir(parents=True, exist_ok=True)
    plates = build()

    existing = {}
    manifest_path = OUT / "plates.json"
    if manifest_path.exists():
        for old in json.loads(manifest_path.read_text(encoding="utf-8"))["plates"]:
            existing[old["id"]] = old
    for p in plates:
        if p["id"] in existing and existing[p["id"]].get("status") == "rendered":
            p["status"] = "rendered"
            for k in ("prompt", "prompt_sha256", "image_sha256", "rendered", "reference"):
                if k in existing[p["id"]]:
                    p[k] = existing[p["id"]][k]

    manifest_path.write_text(
        json.dumps({
            "schema_version": 1,
            "character": "arm",
            "character_sheet": "characters/arm/character_sheet.png",
            "pose_reference": "scratchpad/originals/pose-reference.png",
            "plate_count": len(plates),
            "style_count": len(S),
            "plates": plates,
        }, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # human-readable checklist
    lines = ["# Arm · cross-era art-style study — plate checklist", "",
             f"{len(S)} styles · {len(plates)} plates.", ""]
    fam = None
    for p in plates:
        if p["family"] != fam:
            fam = p["family"]
            lines += ["", f"## {fam}", ""]
        mark = "x" if p["status"] == "rendered" else " "
        lines.append(f"- [{mark}] `{p['id']}` — {p['style_label']} "
                     f"({p['variant']}/{p['variant_count']}, {p['variant_axis']})")
    (OUT / "PLATES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(S)} styles, {len(plates)} plates -> {manifest_path}")


if __name__ == "__main__":
    main()
