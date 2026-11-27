#!/usr/bin/env python3
"""Build the data + web assets for website/artwork — the Arm style atlas course.

Reads art/style-study/plates.json, writes:
  website/artwork/assets/<plate-id>.jpg   web-size derivatives (nothing oversized)
  website/artwork/assets/arm-identity.jpg the character sheet, for lesson 0
  website/artwork/data.js                 window.STUDY = {lessons, styles, coverage}

The curriculum is written here rather than derived, so lesson order, framing and
teaching notes are editorial decisions, not an accident of file order.
"""

from __future__ import annotations

import json
import pathlib
import urllib.parse

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]
STUDY = ROOT / "art" / "style-study"
WEB = ROOT / "website" / "artwork" / "arm-styles"
ASSETS = WEB / "assets"

MAX_W = 720
QUALITY = 78

# --------------------------------------------------------------------------
# Curriculum. Each style slug belongs to exactly one lesson; the check at the
# bottom fails if a style is missing or listed twice.
# --------------------------------------------------------------------------
LESSONS = [
    dict(
        id="l00",
        number="00",
        title="How to read a plate",
        kicker="Orientation",
        lead="Before the history, the method. Every picture in this course is the same "
             "girl in the same pose, drawn by the same machine, and only the medium "
             "changes.",
        body=[
            "The character is Arm — a pocket-sized engineer in a blue-teal workshop "
            "jacket. She is always walking away from us down a stone footpath, head "
            "turned back over her shoulder, folded umbrella in hand. That fixed subject "
            "is the whole point: it turns 105 styles into a controlled experiment. When "
            "you compare two plates, you are not comparing two artists or two moods. You "
            "are comparing two sets of decisions about how a picture gets made.",
            "Most styles appear four times. The four versions are the same four moves in "
            "every style, so you can watch one variable at a time.",
        ],
        axes=[
            ("canonical", "The textbook version. Clear daylight, full figure, staging "
                          "untouched. Learn the medium here first."),
            ("re-keyed", "Same medium, same staging, re-lit for late-afternoon rain. "
                         "Watch what the medium does when the light drops."),
            ("re-framed", "Cropped to a three-quarter view. Now the surface is close "
                          "enough to read brushwork, tooth, glaze or pixel pitch."),
            ("material-extreme", "The medium's fingerprints pushed forward until the "
                                 "surface is the subject. The useful one when you are "
                                 "learning to identify a technique by eye."),
        ],
        takeaway="Ask three questions of any plate: what is the surface, what carries "
                 "the light, and what has the artist chosen not to show?",
        styles=[],
        links=[("Smarthistory · The basics of art history", "https://smarthistory.org/"),
               ("Tate · glossary of 461 art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l01",
        number="01",
        title="Four ways to draw the same page",
        kicker="Manga and its neighbours",
        lead="Start where the project lives. Four commercial illustration systems, each "
             "with its own economics of labour.",
        body=[
            "Cel animation, screentone manga, digital painting and pixel art are not a "
            "historical sequence so much as four answers to the same question: how little "
            "can you draw and still have a picture? Cel shading separates light into two "
            "hard steps because someone has to paint thousands of frames. Screentone "
            "replaces grey with a mechanical dot pattern because a magazine printed in "
            "black ink. Pixel art quantises everything to a grid because memory was "
            "counted in kilobytes.",
            "Read these four first because they set the baseline your eye will use for "
            "everything else. Then notice what the painterly media in the next lesson "
            "refuse to do.",
        ],
        takeaway="A style is often a budget made visible.",
        styles=["anime-cel-shading", "manga-ink-and-screentone", "digital-painting", "pixel-art"],
        links=[("Smarthistory · Japanese art after 1400", "https://smarthistory.org/?s=ukiyo-e"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l02",
        number="02",
        title="Wet media: water, gum and oil",
        kicker="Drawing, paint, and paper",
        lead="Seven binders, seven behaviours. The difference between watercolour and oil "
             "is not colour — it is what the paint does while it dries.",
        body=[
            "Watercolour is transparent and runs; you save the white of the paper because "
            "you cannot paint light back in. Gouache adds chalk, goes opaque, and lets you "
            "work from dark to light. Acrylic dries fast into a plastic film with hard "
            "edges. Oil stays open for days, which is why it can be blended, scumbled and "
            "glazed into softness. Egg tempera sets almost instantly, so it is built from "
            "tiny hatched strokes that never quite merge. Buon fresco is painted into wet "
            "lime plaster and becomes the wall itself. Ink wash is one pigment and water, "
            "and all its eloquence is in dilution.",
            "Look at the four variants of each and find the edge behaviour: bleeding, "
            "chalky, glossy, hatched, matte, pooled.",
        ],
        takeaway="Ask what the medium refuses to do. The refusal is the style.",
        styles=["watercolor", "gouache", "acrylic-painting", "oil-painting",
                "egg-tempera", "buon-fresco", "ink-wash"],
        links=[("Smarthistory · materials: oil, watercolour, fresco",
                "https://smarthistory.org/?s=fresco"),
               ("Tate · painterly", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l03",
        number="03",
        title="Dry media and the tooth of the paper",
        kicker="Drawing, paint, and paper",
        lead="Nothing here can be undone by a brush. Dry media record the hand moving.",
        body=[
            "Graphite is grey and slippery; charcoal is black and dust. Coloured pencil "
            "builds in translucent layers that never fully mix, so the paper's tooth shows "
            "through as white sparkle. Soft pastel is almost pure pigment with just enough "
            "binder to hold a stick shape, which is why it can be smudged into air. Pen and "
            "ink has no tone at all — every grey has to be manufactured from line. Paper "
            "collage swaps mark-making for cutting: the edge of the scissors becomes the "
            "drawing.",
            "This is the cheapest place to start practising, and the fastest place to see "
            "whether you are drawing what you see or drawing a symbol of it.",
        ],
        takeaway="Line is a decision; tone is a decision. Dry media make you choose.",
        styles=["graphite-drawing", "colored-pencil", "charcoal-drawing", "soft-pastel",
                "pen-and-ink-illustration", "paper-collage"],
        links=[("Smarthistory · drawing and prints", "https://smarthistory.org/?s=drawing"),
               ("Tate · collage", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l04",
        number="04",
        title="The multiple: how a print thinks",
        kicker="Prints, photographs, and camera vision",
        lead="A print is an image made to exist more than once. That single fact changes "
             "how it is drawn.",
        body=[
            "Relief printing (woodblock, linocut) keeps what you do not cut away, so the "
            "image is built as flat islands of ink. Intaglio (etching) is the opposite: "
            "the line is scratched into metal and holds the ink, which is why etching lines "
            "taper and swell. Lithography exploits the mutual hatred of grease and water, "
            "giving a crayon softness no relief print can manage. Screenprinting pushes "
            "opaque ink through mesh, one flat colour at a time. Cyanotype is a photographic "
            "process that happens to look like a print.",
            "Ukiyo-e is the great case study: a woodblock print produced by a team — "
            "publisher, designer, block cutter, printer — in editions of thousands, which "
            "is exactly why it could influence European painting from the other side of "
            "the world.",
        ],
        takeaway="Ask how many times the image was meant to exist, and who did the labour.",
        styles=["woodblock-inspired-print", "ukiyo-e", "linocut", "copperplate-etching",
                "lithography", "screenprinting", "cyanotype"],
        links=[("Smarthistory · ukiyo-e and woodblock printing", "https://smarthistory.org/?s=ukiyo-e"),
               ("Tate · edition", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l05",
        number="05",
        title="The camera: light as evidence",
        kicker="Prints, photographs, and camera vision",
        lead="Photography arrives with a claim no painting could make: this really "
             "happened, in front of this lens, at this moment.",
        body=[
            "Pictorialism fought to be taken seriously as art by making photographs look "
            "like paintings — soft focus, gum bichromate, visible handwork. Documentary "
            "photography went the other way, trusting the frame's raw evidence. "
            "Photorealism then closed the loop: a painting so exact that it borrows "
            "photography's authority while keeping a painter's control over every detail.",
            "For a student, these three are a lesson in credibility: what makes an image "
            "feel true, and how easily that feeling is manufactured.",
        ],
        takeaway="Realism is a set of conventions that happen to be in fashion.",
        styles=["pictorialist-photography", "documentary-photography", "photorealism"],
        links=[("Smarthistory · history of photography", "https://smarthistory.org/?s=photography"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l06",
        number="06",
        title="Stories on walls and pages",
        kicker="Narrative before the frame",
        lead="For most of history, a picture was a surface inside architecture or a page "
             "inside a book. Composition had to answer to the wall.",
        body=[
            "Egyptian tomb painting uses composite view — head in profile, eye frontal, "
            "shoulders frontal, legs in profile — because each part is drawn from its most "
            "legible angle. Greek vases wrap a continuous figure around a curve. Maya "
            "ceramics paint calligraphic line on a turning cylinder. Byzantine mosaic sets "
            "the figure frontally against gold so that it addresses you rather than "
            "depicting a room. Stained glass works in leaded compartments because glass "
            "comes in pieces. Persian and Mughal manuscripts float a tilted ground so the "
            "garden reads as a pattern.",
            "Every one of these is a solution to a physical constraint that we now "
            "experience as a style.",
        ],
        takeaway="Before perspective, pictures were designed for a surface, not a window.",
        styles=["ancient-egyptian-wall-painting", "greek-vase-painting",
                "maya-painted-ceramics", "medieval-manuscript-illumination",
                "persian-manuscript-painting", "mughal-album-painting",
                "byzantine-mosaic", "stained-glass", "kalighat-painting", "mithila-painting"],
        links=[("Smarthistory · ancient Egyptian, Greek, Maya, Byzantine",
                "https://smarthistory.org/?s=Byzantine"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l07",
        number="07",
        title="Pattern, craft, and the decorated object",
        kicker="Pattern, craft, and objects",
        lead="The decorative arts are where drawing meets making: a design has to survive "
             "being woven, fired, carved, waxed or stitched.",
        body=[
            "Batik is drawn in wax and dyed, so the line is whatever the wax prevented. "
            "Mithila painting fills every shape to the edge because empty space is "
            "considered unfinished. Rinpa uses pooled ink and gold leaf for a luxury of "
            "emptiness. Chaekgeori stacks books and tools in flat frontal trompe-l'oeil as "
            "a portrait of scholarship. Quilts build a figure from appliqued cloth, so the "
            "drawing is a seam. Art Nouveau and Arts and Crafts sit at the moment design "
            "decides it is art.",
            "Notice how often the constraint — wax, thread, clay, kiln — becomes the "
            "signature we later copy as 'style'.",
        ],
        takeaway="Craft imposes rules; style is what the maker does inside them.",
        styles=["art-nouveau", "arts-and-crafts", "rinpa", "korean-chaekgeori", "batik",
                "narrative-story-quilts", "ayacucho-retablo", "ceramic-vessel-glazing",
                "carved-relief", "rococo"],
        links=[("Smarthistory · ceramics, textile, techniques",
                "https://smarthistory.org/?s=batik"),
               ("Victoria and Albert Museum · collections", "https://www.vam.ac.uk/collections")],
    ),
    dict(
        id="l08",
        number="08",
        title="Staging a figure in space",
        kicker="Stage a figure or a room",
        lead="Once a picture pretends to be a window, the artist becomes a stage "
             "manager: where does the light come from, and who is allowed to see whom.",
        body=[
            "Renaissance perspective puts the viewer at a measurable point and builds the "
            "room to it. Baroque breaks that calm with a single raking light and a "
            "diagonal. Neoclassicism pulls back into a frieze and refuses to emote. "
            "Trompe-l'oeil abandons the window entirely and pretends the painting is an "
            "object — a torn poster, a painted nail with a painted shadow — collapsing the "
            "wall between picture and room.",
            "Then the newest one: the real-time 3D character, which is staged by a light "
            "rig and a camera, not a brush.",
        ],
        takeaway="Composition is a decision about where the viewer stands.",
        styles=["renaissance-perspective", "baroque", "neoclassicism", "trompe-loeil",
                "stylized-3d-rendering"],
        links=[("Smarthistory · Renaissance and Baroque", "https://smarthistory.org/?s=Baroque"),
               ("Tate · vanishing point", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l09",
        number="09",
        title="Work and public life",
        kicker="Work and public life",
        lead="Art as an argument about who matters. These styles were made for walls, "
             "newspapers and nations.",
        body=[
            "Mexican muralism paints at the scale of a building because the message is "
            "addressed to everyone who walks past. French Realism insists on ordinary "
            "labour at the Salon, at the size previously reserved for history painting. "
            "Harlem Renaissance illustration builds a modern, dignified Black visual "
            "language out of flat shape and rhythm. New Objectivity answers with cold "
            "precision. Regionalism and Socialist Realism each build a national story out "
            "of sunlight and work.",
            "None of these are neutral. Read them as rhetoric, and ask who the picture is "
            "flattering.",
        ],
        takeaway="When art addresses a public, style becomes politics.",
        styles=["mexican-muralism", "french-realism", "harlem-renaissance-mural",
                "new-objectivity", "american-regionalism", "soviet-socialist-realism"],
        links=[("Smarthistory · realism and modern life", "https://smarthistory.org/?s=Realism"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l10",
        number="10",
        title="Light, weather, landscape",
        kicker="Light, weather, and landscape",
        lead="Landscape is the genre where technique is most visible, because there is no "
             "face to hold the eye.",
        body=[
            "Chinese ink landscape does not describe a view; it builds a mountain from "
            "texture strokes and then leaves a misty void for the mind to cross. "
            "Impressionism dissolves contour into broken colour because light changes "
            "faster than drawing can follow. Romanticism keeps the contour and enlarges "
            "the sky until the figure is a measure of awe. Pointillism separates colour "
            "into dots and lets your eye do the mixing. Tonalism removes almost everything "
            "except a mood.",
            "Five answers to the same question: how do you paint air?",
        ],
        takeaway="Weather is a technical problem before it is an emotional one.",
        styles=["chinese-ink-landscape", "impressionism", "romanticism", "pointillism",
                "tonalism"],
        links=[("Smarthistory · landscape and Impressionism",
                "https://smarthistory.org/?s=Impressionism"),
               ("Tate · impressionism", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l11",
        number="11",
        title="Emotion, dream, metaphor",
        kicker="Emotion, dreams, and metaphor",
        lead="Around 1880 the picture stops reporting and starts meaning. Colour and "
             "distortion become arguments.",
        body=[
            "Symbolism replaces a literal object with a resonant one and refuses to explain "
            "it. Expressionism distorts anatomy and screams in unmixed colour. Fauvism lets "
            "colour be arbitrary and structural at once. Surrealism keeps the rendering "
            "photographic and makes the arrangement impossible, which is why it unsettles. "
            "Dada photomontage cuts the newspaper world apart and pastes it back as "
            "satire. The Pre-Raphaelites go the other way, drowning a moral in detail, and "
            "the Dutch vanitas makes a still life into a sermon about time.",
            "This is the lesson where 'I like it' stops being a useful sentence. Ask what "
            "the picture is claiming.",
        ],
        takeaway="Distortion is a sentence, not a mistake.",
        styles=["symbolism", "expressionism", "surrealism", "fauvism", "dada-photomontage",
                "pre-raphaelite", "dutch-vanitas"],
        links=[("Smarthistory · modernisms", "https://smarthistory.org/?s=Surrealism"),
               ("Tate · surrealism", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l12",
        number="12",
        title="Abstraction, geometry, optical motion",
        kicker="Abstraction, geometry, and optical motion",
        lead="The picture stops pointing at something in the world and starts being a "
             "thing in the world.",
        body=[
            "Cubism breaks the object into facets seen from several places at once. "
            "Futurism adds time and speed to those facets. Orphism keeps colour and drops "
            "the object. De Stijl reduces to a grid and three primaries. Minimalism reduces "
            "further, to interval and placement. Abstract Expressionism replaces drawing "
            "with the record of a body moving. Op Art engineers the eye into seeing motion "
            "that is not there. Generative and plotter art hands the drawing to a rule.",
            "The hardest lesson for a beginner: with nothing depicted, every decision is "
            "visible, and there is nowhere to hide.",
        ],
        takeaway="Abstraction does not remove content; it removes the alibi.",
        styles=["cubism", "futurism", "orphism", "de-stijl", "minimalism",
                "abstract-expressionism", "op-art", "generative-plotter-art"],
        links=[("Smarthistory · Cubism and abstraction", "https://smarthistory.org/?s=Cubism"),
               ("Tate · generative art", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l13",
        number="13",
        title="Design that persuades",
        kicker="Graphic design and public messages",
        lead="Graphic design is art with a deadline and a client. It is also the visual "
             "grammar of everything you read on a screen.",
        body=[
            "Constructivism builds a poster like a machine part: red, black, diagonal, "
            "photograph cut against geometry. Bauhaus reduces to elementary shapes on a "
            "grid and lowercase type. Art Deco streamlines the same geometry into luxury. "
            "Swiss Style adds the grid we still use. Pop Art collapses fine art and "
            "advertising by using the advert's own printing method. Psychedelic posters "
            "warp type until legibility becomes a trip. Memphis and Space Age design are "
            "period flavour, and Afrofuturism shows the same design vocabulary turned "
            "toward a future worth wanting.",
            "Learn this lesson with a ruler. Almost every rule here is arithmetic.",
        ],
        takeaway="Design is the art of deciding what to leave out on purpose.",
        styles=["constructivism", "bauhaus-graphic-design", "art-deco", "swiss-style",
                "pop-art", "psychedelic-poster-art", "vector-illustration",
                "memphis-design", "space-age-design", "afrofuturism"],
        links=[("Tate · art terms: design and movements", "https://www.tate.org.uk/art/art-terms"),
               ("Smarthistory · design and mass media", "https://smarthistory.org/?s=Bauhaus")],
    ),
    dict(
        id="l14",
        number="14",
        title="Buildings, land, light",
        kicker="Buildings, sites, and installations",
        lead="Some pictures are not of a place but about one: scale as the subject.",
        body=[
            "Precisionism paints the factory as a cathedral, all clean edges and raking "
            "shadow. Brutalism lets raw concrete be raw, and the photograph becomes the "
            "style's main distribution channel. Deconstructivism makes structure look "
            "impossible. Land Art leaves the gallery and cuts the drawing into the earth, "
            "so the work is only ever seen as a photograph or a walk. Light and Space "
            "removes the object entirely and shows you the air.",
            "When the artwork is a place, the camera is not documentation — it is the "
            "medium.",
        ],
        takeaway="Ask what you are actually looking at: a building, or a photograph of one.",
        styles=["precisionism", "brutalist-architecture",
                "deconstructivist-architecture", "land-art", "light-and-space"],
        links=[("Smarthistory · global history of architecture",
                "https://smarthistory.org/?s=architecture"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
    dict(
        id="l15",
        number="15",
        title="Performance, puppet, and machine",
        kicker="Performance, puppetry, and kinetic art",
        lead="The last escape from the frame: work that happens in time, with a body or a "
             "motor inside it.",
        body=[
            "Wayang kulit is a shadow puppet tradition where the visible artwork is the "
            "silhouette and the real craft is the moving. Stop-motion builds a physical "
            "world one frame at a time, and its charm is that you can see the hand. Ballets "
            "Russes stage design treats the whole stage as a flat, saturated picture in "
            "motion. Gutai records an action rather than a scene. Kinetic sculpture hands "
            "the composition to gravity and air.",
            "If the medium is time, the composition includes the moment you arrive.",
        ],
        takeaway="Some images are events; a still photograph is already an interpretation.",
        styles=["wayang-kulit", "stop-motion", "ballets-russes-stage-design", "gutai",
                "kinetic-sculpture"],
        links=[("Tate · performance art", "https://www.tate.org.uk/art/art-terms"),
               ("Smarthistory · performance and film", "https://smarthistory.org/?s=performance")],
    ),
    dict(
        id="l16",
        number="16",
        title="The machine image: seven eras",
        kicker="Video game eras",
        lead="Forty years of real-time graphics in seven frames. Every constraint here is "
             "a number: polygons, colours, texture memory.",
        body=[
            "The NES gives a sprite three colours and a grid. The SNES gives it fifteen per "
            "palette row and parallax. PlayStation-era 2D keeps a painted sprite over a "
            "pre-rendered plate. PlayStation 3D drops to a few hundred warping polygons and "
            "makes texture memory the real budget. The arcade 3D of the late nineties "
            "smooths the mesh and adds a specular sheen. The PS3/PS4 era adds normal maps, "
            "ambient occlusion and cloth. The current generation ray-traces the light and "
            "grows hair strand by strand.",
            "Read this lesson as a history of what artists did with not enough, which is "
            "also the history of every other style in this course.",
        ],
        takeaway="Technical limits are the most reliable style generator ever invented.",
        styles=["nes-era", "snes-era", "ps1-2d", "ps1-3d-lowpoly", "doa-era-3d",
                "ps3-ps4-era-3d", "ps5-era-raytracing"],
        links=[("Smarthistory · art and technology", "https://smarthistory.org/?s=technology"),
               ("Tate · art terms", "https://www.tate.org.uk/art/art-terms")],
    ),
]


def web_image(src: pathlib.Path, dst: pathlib.Path) -> tuple[int, int]:
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > MAX_W:
            h = round(im.height * MAX_W / im.width)
            im = im.resize((MAX_W, h), Image.LANCZOS)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        return im.size


def main() -> None:
    data = json.loads((STUDY / "plates.json").read_text(encoding="utf-8"))
    plates = {p["id"]: p for p in data["plates"]}

    ASSETS.mkdir(parents=True, exist_ok=True)

    # sanity: every style in the manifest is in exactly one lesson
    all_styles = {p["style"] for p in data["plates"]}
    listed = [s for l in LESSONS for s in l["styles"]]
    assert len(listed) == len(set(listed)), "a style is listed in two lessons"
    missing = all_styles - set(listed)
    extra = set(listed) - all_styles
    assert not missing, f"styles not in any lesson: {sorted(missing)}"
    assert not extra, f"lesson references unknown style: {sorted(extra)}"

    # labels + medium text per style, from the manifest
    style_meta = {}
    for p in data["plates"]:
        style_meta.setdefault(p["style"], {
            "slug": p["style"],
            "label": p["style_label"],
            "medium": p["medium"],
            "family": p["family"],
            "mode": p["mode"],
            "plates": [],
        })
        style_meta[p["style"]]["plates"].append(p)

    styles_out = {}
    rendered_total = 0
    for slug, meta in style_meta.items():
        plates_out = []
        for p in sorted(meta["plates"], key=lambda x: x["variant"]):
            entry = {
                "id": p["id"],
                "variant": p["variant"],
                "axis": p["variant_axis"],
                "status": p["status"],
            }
            if p["status"] == "rendered":
                src = ROOT / p["file"]
                dst = ASSETS / f"{p['id']}.jpg"
                if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                    w, h = web_image(src, dst)
                else:
                    with Image.open(dst) as im:
                        w, h = im.size
                entry.update(src=f"assets/{dst.name}", w=w, h=h)
                rendered_total += 1
            plates_out.append(entry)
        styles_out[slug] = {
            "slug": slug,
            "label": meta["label"],
            "medium": meta["medium"],
            "family": meta["family"],
            "mode": meta["mode"],
            "term": meta["label"],
            "plates": plates_out,
            "links": [
                {"label": "Wikipedia", "url":
                 "https://en.wikipedia.org/wiki/Special:Search?search="
                 + urllib.parse.quote(meta["label"])},
                {"label": "Smarthistory", "url":
                 "https://smarthistory.org/?s="
                 + urllib.parse.quote(meta["label"])},
            ],
        }

    sheet = ROOT / "characters/arm/character_sheet.png"
    with Image.open(sheet) as im:
        im = im.convert("RGB")
        im.thumbnail((1100, 1100))
        im.save(ASSETS / "arm-identity.jpg", "JPEG", quality=85, optimize=True)

    total = len(data["plates"])
    lessons_out = []
    for l in LESSONS:
        ls = [styles_out[s] for s in l["styles"]]
        done = sum(1 for st in ls for p in st["plates"] if p["status"] == "rendered")
        count = sum(len(st["plates"]) for st in ls)
        lessons_out.append({
            "id": l["id"], "number": l["number"], "title": l["title"],
            "kicker": l["kicker"], "lead": l["lead"], "body": l["body"],
            "takeaway": l.get("takeaway"), "axes": l.get("axes"),
            "styles": ls, "plates_done": done, "plates_total": count,
            "links": [{"label": a, "url": b} for a, b in l["links"]],
        })

    payload = {
        "title": "Arm in Every Style",
        "subtitle": "A first course in visual language — every image generated by Seedream",
        "character": "Arm, the Pocket Architect · Silicon Wars",
        "generated_with": "Seedream",
        "coverage": {"rendered": rendered_total, "total": total,
                     "percent": round(rendered_total / total * 100, 1)},
        "identity": "assets/arm-identity.jpg",
        "lessons": lessons_out,
    }
    (WEB / "data.js").write_text(
        "window.STUDY = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8")
    print(f"data.js written · {rendered_total}/{total} plates "
          f"({rendered_total / total * 100:.1f}%) · {len(lessons_out)} lessons")


if __name__ == "__main__":
    main()
