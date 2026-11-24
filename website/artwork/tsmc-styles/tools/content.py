# Curriculum content for the TSMC Style Course (website/artwork/tsmc-styles).
# Each style: name, tag (era/place), blurb (beginner-friendly), look (what to notice), wiki (article slug).

LESSONS = [
    {
        "id": "media",
        "title": "Made of What? Drawing and Painting Media",
        "bigIdea": "Before style comes stuff. Every picture is made of a material, and the material leaves fingerprints.",
        "intro": "Our model sits in the same café pose for every picture in this lesson. Only the medium changes: pencil, ink, chalk, water, oil, pixels. Watch how each material pushes the same scene toward a different mood — soft, sharp, glowing, flat. Learning to name the medium is the first skill of looking at art.",
        "exercise": "Pick two pictures of the same pose and list three things that changed besides color. Edges? Texture? How dark the darkest dark is?",
        "styles": ["graphite-drawing", "pen-and-ink", "ink-wash", "charcoal", "colored-pencil",
                   "soft-pastel", "watercolor", "gouache", "acrylic-painting", "oil-painting",
                   "egg-tempera", "buon-fresco", "digital-painting", "vector-illustration",
                   "manga-ink", "anime-cel"],
    },
    {
        "id": "print",
        "title": "Copies: Printmaking and Reproduction",
        "bigIdea": "A print is a picture made by transfer — carve it, ink it, press it, and you can make it again.",
        "intro": "Printmaking turned images into multiples centuries before photography. Each technique here — carving wood, cutting lino, etching copper, exposing a cyanotype — forces the artist to think in reversed images, layers and limited marks. Notice how the café scene survives being squeezed through each process.",
        "exercise": "Find the picture where white lines do the drawing instead of black ones. Why does carving flip the usual logic of drawing?",
        "styles": ["woodblock", "ukiyo-e", "linocut", "copperplate-etching", "lithography",
                   "screenprinting", "cyanotype", "generative-plotter"],
    },
    {
        "id": "camera",
        "title": "Fooling the Eye: Photography and Illusion",
        "bigIdea": "A picture can pretend to be a window. Photography made that pretence cheap — and artists started asking what 'real' even means.",
        "intro": "Pictorialists made photographs look like paintings; documentary photographers chased unposed truth; photorealists painted photographs by hand; trompe-l'œil painters tried to make you reach for painted objects. Same café, four different claims about reality.",
        "exercise": "Cover the labels and sort the four pictures from 'most like a dream' to 'most like evidence'. What visual clues did you use?",
        "styles": ["pictorialist-photography", "documentary-photography", "photorealism", "trompe-loeil"],
    },
    {
        "id": "craft",
        "title": "The Decorated Surface: Craft, Pattern and Material",
        "bigIdea": "Not every picture hangs in a frame. Some are built from stone, glass, cloth and clay — and pattern is their language.",
        "intro": "Mosaics, stained glass, batik cloth, quilts, carved stone and glazed porcelain: these arts decorate useful or sacred surfaces, and their materials dictate their geometry. Edges become lead lines, grout lines, seams and glazes. Compare how each craft breaks the café scene into pieces — and why.",
        "exercise": "Choose one craft picture and imagine touching it. Where is it rough, smooth, heavy, fragile? How did the material decide the shapes?",
        "styles": ["byzantine-mosaic", "stained-glass", "paper-collage", "batik",
                   "narrative-story-quilts", "carved-relief", "ceramic-vessel"],
    },
    {
        "id": "world",
        "title": "World Traditions: Many Ways to Make a Picture",
        "bigIdea": "Realistic perspective is one culture's choice, not a law. Every tradition in this lesson solves 'how to show a person' differently.",
        "intro": "Egyptian painters combined profile heads with frontal eyes; Maya artists painted stories around vases; Persian and Mughal miniaturists packed gardens into pages; Korean chaekgeori painters celebrated books themselves. As you compare, ask what each culture valued enough to draw carefully — and what it happily flattened or ignored.",
        "exercise": "Find a picture where space is shown by stacking things upward instead of shrinking them with distance. Which tradition is it, and what does that choice make clearer?",
        "styles": ["egyptian-wall-painting", "greek-vase-painting", "maya-painted-ceramics",
                   "medieval-illumination", "persian-manuscript", "mughal-album", "mithila",
                   "rinpa", "chinese-ink-landscape", "chaekgeori", "kalighat", "wayang-kulit",
                   "ayacucho-retablo"],
    },
    {
        "id": "canon",
        "title": "The Western Canon: Order, Drama and Feeling",
        "bigIdea": "From 1400 to 1900, European painting swung like a pendulum: reason, then emotion, then reason again — each swing reacting to the last.",
        "intro": "Renaissance artists built space with geometry. Baroque artists flooded it with drama. Neoclassicists demanded noble order, Romantics answered with storms and feelings, and Realists pointed at ordinary workers. Walk the pendulum swing by swing and you can read most museum walls in Europe.",
        "exercise": "Stand back from the nine pictures and sort them into 'calm and ordered' versus 'stormy and emotional'. Does the historical order alternate?",
        "styles": ["renaissance-perspective", "baroque", "neoclassicism", "rococo", "romanticism",
                   "pre-raphaelite", "tonalism", "dutch-vanitas", "french-realism"],
    },
    {
        "id": "public",
        "title": "Art in Public: Walls, Nations and Movements",
        "bigIdea": "Some art is made to persuade crowds, not decorate rooms — it gets big, legible and ideological.",
        "intro": "Mexican muralists painted national history on public walls; Harlem Renaissance artists forged a visual identity; Soviet Socialist Realism glorified the worker; the New Objectivity stared at Weimar Germany without blinking. Ask of every picture here: who paid for it, who was meant to see it, and what were they supposed to feel?",
        "exercise": "Pick the picture you would put on a public building to make people proud, and the one you would put in a newspaper to make them think. Defend both choices.",
        "styles": ["mexican-muralism", "harlem-renaissance", "american-regionalism",
                   "soviet-socialist-realism", "new-objectivity", "arts-and-crafts"],
    },
    {
        "id": "modernism",
        "title": "Modernism Breaks the Picture",
        "bigIdea": "Between 1870 and 1940 artists dismantled the window-illusion piece by piece: light, color, form, then reality itself.",
        "intro": "Impressionists painted light instead of things. Fauvists freed color from nature. Cubists showed several viewpoints at once. Surrealists and Dada artists attacked logic itself. Each style in this lesson breaks one rule the canon lessons taught you — see if you can name the rule being broken in each picture.",
        "exercise": "For each picture, complete the sentence: 'This artist cares more about ___ than about making it look real.' Compare your answers with a partner's.",
        "styles": ["impressionism", "pointillism", "symbolism", "fauvism", "expressionism",
                   "cubism", "futurism", "orphism", "surrealism", "dada-photomontage"],
    },
    {
        "id": "systems",
        "title": "Systems and Geometry: Art as Design",
        "bigIdea": "Twentieth-century artists and designers tried to build pictures from systems: grids, pure shapes, primary colors, optical laws.",
        "intro": "The Bauhaus, De Stijl and the Constructivists wanted a universal visual language. Op artists weaponized optical illusion; Abstract Expressionists did the opposite — huge, unsystematic gesture. Art Nouveau and Art Deco remind us that 'design' also means ornament, luxury and the curve. Notice how many of these styles still shape the apps and posters around you.",
        "exercise": "Find the picture with the fewest elements that still reads as 'TSMC at a café'. What is the minimum a picture needs?",
        "styles": ["art-nouveau", "art-deco", "bauhaus", "constructivism", "de-stijl",
                   "op-art", "abstract-expressionism", "minimalism", "swiss-style", "precisionism"],
    },
    {
        "id": "pop",
        "title": "Pop and After: Art in the Age of Mass Media",
        "bigIdea": "After 1960, art absorbed advertising, television, comics and consumer products — and started designing futures of its own.",
        "intro": "Pop Art held a mirror to supermarket culture. Psychedelic posters melted lettering into pure sensation. Memphis designers made furniture deliberately silly, Space Age designers sold tomorrow, and Afrofuturism claimed the future for Black imagination. The café scene keeps up with every one of these costumes.",
        "exercise": "Which picture here could be an advertisement, and what would it be selling? What makes the others resist being ads?",
        "styles": ["pop-art", "psychedelic-poster", "memphis-design", "space-age-design", "afrofuturism"],
    },
    {
        "id": "beyond",
        "title": "Beyond the Frame: Space, Light and Performance",
        "bigIdea": "Eventually artists left the rectangle entirely: art became landscape, architecture, light, movement and action.",
        "intro": "Land artists rearranged deserts. Light and Space artists made perception itself the artwork. Gutai painters attacked canvas with their bodies; kinetic sculptors set art spinning; stage designers and stop-motion animators built worlds that exist only in time. Our model still poses — but the 'picture' now surrounds her.",
        "exercise": "For each work, answer: if you stood inside it, where would you be and what would move? Which work would change most if you visited on a windy day?",
        "styles": ["land-art", "light-and-space", "brutalist-architecture",
                   "deconstructivist-architecture", "kinetic-sculpture", "gutai",
                   "ballets-russes", "stop-motion"],
    },
    {
        "id": "games",
        "title": "The Pixel Ladder: Video Game Graphics",
        "bigIdea": "Game graphics are art styles dictated by hardware. Every era's look is a negotiation between imagination and memory chips.",
        "intro": "Climb the ladder one console at a time. The NES could show only a handful of colors per sprite; the SNES multiplied them; the PlayStation split into lush 2D and wobbly low-polygon 3D; each generation since added polygons, light and physics. Because the pose never changes, you can watch pure rendering evolve — the same lesson as Lesson 1, played on machines.",
        "exercise": "Cover the labels and arrange the nine pictures oldest to newest by look alone. Then check: which single visual cue (pixels? polygons? reflections?) was most reliable?",
        "styles": ["pixel-art", "nes-8bit", "snes-16bit", "ps1-2d", "ps1-3d-lowpoly",
                   "ps1-3d-refined", "ps3-ps4-3d", "ps5-raytraced", "stylized-3d"],
    },
]

STYLES = {}

def S(name, tag, blurb, look, wiki):
    STYLES[len(STYLES)] = (name, tag, blurb, look, wiki)

# --- Lesson 1: media ---
STYLES["graphite-drawing"] = ("Graphite Drawing", "Pencil on paper",
    "The humblest medium: a pencil. Everything is built from gray — light grays for silk and skin, deep grays for shadow — with no color to hide behind.",
    ["Shading is blended smoothly, like breath on glass", "Edges are soft where light wraps around the figure", "The whole scene fits in one family of grays"], "Drawing")
STYLES["pen-and-ink"] = ("Pen and Ink", "Nib and black ink",
    "A pen cannot erase and cannot do gray directly — grays are faked with hatching, thousands of tiny parallel lines. The result is crisp, decisive and a little nervous.",
    ["Look for cross-hatched shadows on the skirt and chair", "Lines get denser where things get darker", "Highlights are just paper left empty"], "Pen_and_ink")
STYLES["ink-wash"] = ("Ink Wash", "Diluted ink, East Asian manner",
    "Ink thinned with water into a ladder of grays, laid down in flowing washes. One brushstroke must do the work of a whole shadow — there is no going back.",
    ["Big soft pools of gray form the background", "A few dry-brush strokes snap the details into focus", "The mood is quiet, like the moment before rain"], "Ink_wash_painting")
STYLES["charcoal"] = ("Charcoal Drawing", "Charcoal on paper",
    "Burnt willow ground into sticks: charcoal gives the blackest blacks and the smudgiest edges of any drawing medium. Artists smear it with fingers and lift it with erasers.",
    ["Deep velvety darks behind the figure", "Edges dissolve where the artist smudged", "Bright highlights were erased back into the paper"], "Charcoal_(art)")
STYLES["colored-pencil"] = ("Colored Pencil", "Layered pencil pigment",
    "Color built from dozens of transparent layers of pencil. Slower than paint, more controlled than pastel — every hair and thread can be placed exactly.",
    ["Fine grain from the paper shows through the color", "Colors are mixed by layering, not on a palette", "Edges stay sharp and deliberate everywhere"], "Colored_pencil")
STYLES["soft-pastel"] = ("Soft Pastel", "Pure pigment sticks",
    "Pastel sticks are almost pure pigment, so colors glow with a powdery, light-scattering softness. It is drawing and painting at the same time.",
    ["A velvety bloom softens every surface", "Colors sit on top of each other like dust", "Skin and cloth share the same chalky light"], "Pastel")
STYLES["watercolor"] = ("Watercolor", "Transparent pigment in water",
    "Water does half the work. Pigment pools, blooms and dries lighter than it looks wet, and the white of the paper becomes the light in the picture.",
    ["Transparent washes let the paper shine through", "Edges bloom where wet paint met wet paper", "Nothing is fully opaque — even shadows glow"], "Watercolor_painting")
STYLES["gouache"] = ("Gouache", "Opaque watercolor",
    "Watercolor's matte, opaque cousin — designers loved it because it photographs flat and covers mistakes. Colors dry chalky, even and poster-like.",
    ["Flat, even color areas with little shine", "Light colors sit cleanly on top of dark ones", "The finish looks like a printed illustration"], "Gouache")
STYLES["acrylic-painting"] = ("Acrylic Painting", "Modern polymer paint",
    "Invented in the 20th century, acrylic dries in minutes and can imitate oil, watercolor or plastic-smooth flatness. The café scene gets crisp edges and a modern, satin finish.",
    ["Clean edges mixed with smoothly blended passages", "Colors stay bright and slightly synthetic", "No canvas glow — the surface is calm and matte-satin"], "Acrylic_paint")
STYLES["oil-painting"] = ("Oil Painting", "Pigment in linseed oil",
    "The prestige medium of European art for 500 years: slow-drying, blendable, and capable of glowing translucent layers called glazes. Skin and silk were its specialties.",
    ["Soft, seamless blending on the face and hands", "Deep colors glow as if lit from inside", "Brushwork disappears into polished finish"], "Oil_painting")
STYLES["egg-tempera"] = ("Egg Tempera", "Pigment bound with egg yolk",
    "The panel painter's medium before oil: fast, matte and precise, built from thousands of tiny hatched strokes. It gives the scene a pale, luminous, early-Renaissance stillness.",
    ["Fine hatched strokes model every form", "Colors are pale, dry and luminous", "A faint gold warmth hangs over the scene"], "Tempera")
STYLES["buon-fresco"] = ("Buon Fresco", "Painting into wet plaster",
    "True fresco is painted into wet lime plaster, so the image becomes part of the wall itself — which is why Giotto's work survives 700 years later. Our version even has the cracks.",
    ["Matte, mineral colors with no shine at all", "Hairline cracks cross the surface", "It reads as a wall, not a page — flat and architectural"], "Fresco")
STYLES["digital-painting"] = ("Digital Painting", "Pixels and pressure-sensitive brushes",
    "Painting with software: infinite undo, perfect gradients, brushes that imitate everything in this lesson. The challenge flips — with no material resistance, the artist must invent their own limits.",
    ["Airbrush-smooth gradients with painterly accents", "Lighting is polished and cinematic", "No paper grain, no cracks — a surface that never existed physically"], "Digital_painting")
STYLES["vector-illustration"] = ("Vector Illustration", "Mathematical curves",
    "Not pixels but equations: every shape is a clean curve that can scale forever without blurring. The café becomes a diagram of itself — all signal, no texture.",
    ["Perfectly smooth edges at any size", "Flat color shapes with a few clean gradients", "Details are simplified into symbols"], "Vector_graphics")
STYLES["manga-ink"] = ("Manga Ink and Screentone", "Japanese comics technique",
    "Black ink plus screentone — printed dot patterns that fake gray. Manga artists turn economy into style: a few tones, bold blacks, and speed of reading above all.",
    ["Dot-pattern tones shade the skirt and background", "Solid blacks anchor hair, chair and shadows", "The drawing stays light and quick to read"], "Manga")
STYLES["anime-cel"] = ("Anime Cel Shading", "Animation cel style",
    "Classic TV animation painted characters on clear cels: flat color, one shadow tone, bold outlines. Zero blending — every form is a decision about where light stops.",
    ["Exactly two tones per surface: lit and shadow", "Thick, confident outlines", "The background is softer than the character, so she pops forward"], "Traditional_animation")

# --- Lesson 2: print ---
STYLES["woodblock"] = ("Woodblock Print", "Carved wood, relief printing",
    "The image is carved into wood in reverse; what is not carved prints black. Bold shapes and knife marks are not flaws — they are the medium thinking out loud.",
    ["Thick black shapes carry the composition", "White lines are carved, not drawn", "The texture of the wood grain peeks through"], "Woodblock_printing")
STYLES["ukiyo-e"] = ("Ukiyo-e", "Japanese woodblock, Edo period",
    "Japan's 'pictures of the floating world': separate carved blocks for each color, printed in perfect registration. Flat color, elegant line, and design sense that later stunned Paris.",
    ["Flat color areas bounded by a key-block line", "Patterned textiles and screens fill the background", "Four variants show different print moods — dark mica, pattern, actor-print boldness"], "Ukiyo-e")
STYLES["linocut"] = ("Linocut", "Carved linoleum",
    "Linoleum is softer than wood, so lines swing in bold curves. The 20th-century favorite for posters and protest art: cheap, fast, unmistakable.",
    ["Sweeping carved curves instead of fine detail", "High black-and-white contrast", "One accent color — wine red — does the storytelling"], "Linocut")
STYLES["copperplate-etching"] = ("Copperplate Etching", "Acid-bitten copper lines",
    "The artist draws through wax on copper; acid bites the lines; ink hides in the grooves. Rembrandt's medium — capable of spiderweb delicacy and deep, warm darks.",
    ["Everything is built from fine line networks", "Tones are warm and antique, like old book plates", "The longer you look, the more lines you find"], "Etching")
STYLES["lithography"] = ("Lithography", "Drawing on stone",
    "A greasy crayon draws on limestone; water and ink do the rest. Uniquely among print methods, it preserves the exact feel of a crayon or brush stroke.",
    ["Soft, grainy crayon texture in the shading", "Tones feel drawn, not carved or etched", "The mood is of a 19th-century Paris poster"], "Lithography")
STYLES["screenprinting"] = ("Screenprinting", "Ink through mesh stencils",
    "Each color is pushed through its own stenciled screen, so images arrive in flat, separable layers — the technique of Warhol and of every band T-shirt since.",
    ["Color arrives in flat, even layers", "Slight misregistration charm at the edges", "It looks printed, bold and reproducible"], "Screen_printing")
STYLES["cyanotype"] = ("Cyanotype", "Sun-printed blueprint blue",
    "Iron salts and sunlight: expose, rinse, and everything turns Prussian blue. Anna Atkins used it for the first photographically illustrated book in 1843.",
    ["Only blue and white exist in this world", "Edges are soft, like shadows of real objects", "The café feels like a blueprint of a memory"], "Cyanotype")
STYLES["generative-plotter"] = ("Generative and Plotter Art", "Algorithm-drawn pen lines",
    "A computer writes the rules; a pen plotter draws them — thousands of precise lines whose density becomes shading. The artist's hand moves from drawing to designing the system that draws.",
    ["Shading is made only of line density", "Lines are perfectly regular, faintly mechanical", "A single wine-red ink breaks the monochrome"], "Generative_art")

# --- Lesson 3: camera ---
STYLES["pictorialist-photography"] = ("Pictorialist Photography", "Soft-focus photography, c. 1900",
    "Early art photographers fought for photography's status by making it dreamy: soft focus, hand-worked prints, painterly haze. Proof, they argued, that a camera could make art.",
    ["Focus melts at the edges of the frame", "Sepia-platinum tones, like an old photograph", "Mood matters more than information"], "Pictorialism")
STYLES["documentary-photography"] = ("Documentary Photography", "Reportage, black and white",
    "The opposite claim: the camera tells the truth. Grain, available light, an unposed instant — the café as evidence of a real afternoon.",
    ["Grain and imperfect light feel honest", "Nothing seems arranged for your benefit", "Black and white strips the scene to fact"], "Documentary_photography")
STYLES["photorealism"] = ("Photorealism", "Painting that imitates photographs",
    "Painters in the 1970s copied photographs so exactly that the painting disappears into the photo — including the photo's blur, glare and accidents. It asks: if it looks identical, what is the difference?",
    ["Every reflection and texture is accounted for", "Even the camera's depth-of-field blur is painted", "You keep forgetting it is not a photograph"], "Photorealism")
STYLES["trompe-loeil"] = ("Trompe-l'œil", "French: 'fools the eye'",
    "Painting that tries to escape its own frame: painted flies, peeling corners, objects that beg to be touched. The four variants stage different tricks — a letter board, a marble ledge, a pinned note.",
    ["Painted shadows make objects seem to lift off the surface", "One detail (a fly, a peeling corner) sells the illusion", "The frame itself becomes part of the joke"], "Trompe-l'œil")

# --- Lesson 4: craft ---
STYLES["byzantine-mosaic"] = ("Byzantine-Inspired Mosaic", "Stone and glass tesserae",
    "Thousands of small cubes — tesserae — set into mortar, often against gold. Byzantine mosaics flatten figures on purpose: these are icons, not windows, meant to glow by candlelight.",
    ["You can see the individual cubes up close", "Gold or deep color fills the background, not air", "Four variants run from jewel-fine to rustic and aged"], "Byzantine_art")
STYLES["stained-glass"] = ("Stained Glass", "Colored glass and lead",
    "A picture made of light itself: pieces of colored glass held by lead strips, designed to be read from inside a dark building with the sun behind it.",
    ["Black lead lines are the drawing", "Colors glow instead of reflecting", "Variants range from Gothic jewel tones to a minimal modern window"], "Stained_glass")
STYLES["paper-collage"] = ("Paper Collage", "Cut and pasted paper",
    "Scissors as a drawing tool. Matisse, too ill to paint late in life, called it 'drawing with scissors' — shapes are cut first and arranged until they sing.",
    ["Every shape has a cut edge, not a drawn one", "Flat papers overlap like leaves", "The composition feels playful and movable"], "Collage")
STYLES["batik"] = ("Batik", "Wax-resist dyed cloth, Indonesia",
    "Hot wax is drawn onto cloth to resist dye; crack the wax and the dye bleeds into fine veins. Repeat for every color. The café becomes cloth — pattern is not decoration here, it is structure.",
    ["Fine crackle lines vein the colored areas", "Indigo, wine and brown dominate the dye palette", "Motifs repeat the way cloth patterns do"], "Batik")
STYLES["narrative-story-quilts"] = ("Narrative Story Quilts", "Appliqué fabric storytelling",
    "Cloth pieces stitched into scenes — a tradition carried to brilliance by African American quilters like Harriet Powers and Faith Ringgold. Seams are the outlines; patterned fabrics do the shading.",
    ["Visible stitches outline every shape", "Different cloth patterns stand in for light and shade", "The surface feels warm, soft and handmade"], "Quilt")
STYLES["carved-relief"] = ("Carved Relief", "Stone carving",
    "The scene is not drawn but excavated: figures rise a few centimeters from a stone panel, and raking light does the modeling. All color is gone — only depth remains.",
    ["One gray material makes the whole world", "Shadows in the carving create the shading", "Chisel texture survives in the background"], "Relief")
STYLES["ceramic-vessel"] = ("Ceramic Vessel and Glazing", "Painted porcelain",
    "The picture wraps around a vase, bending with its belly. Glaze painting must predict the kiln: colors go in dull and come out glossy and transformed.",
    ["The scene curves around the vessel's body", "Cobalt blue and enamel colors shine under glaze", "The vase itself is part of the artwork, not a frame"], "Ceramic_art")

# --- Lesson 5: world ---
STYLES["egyptian-wall-painting"] = ("Ancient Egyptian Wall Painting", "Tomb and temple walls",
    "Egyptian figures combine the most recognizable view of each body part: head in profile, eye frontal, shoulders frontal, legs in profile. Not a mistake — a 3,000-year information system.",
    ["Profile head with a frontal eye", "Flat mineral colors inside firm outlines", "Hieroglyph-like signs and register lines organize the wall"], "Ancient_Egyptian_art")
STYLES["greek-vase-painting"] = ("Greek Vase Painting", "Black-figure and red-figure pottery",
    "Athenian painters told myths on wine vessels: first as black silhouettes with scratched details, later reversed — red figures reserved against a black ground, allowing painted interior lines.",
    ["Figures wrap around the curve of an amphora", "Black silhouettes carry incised detail", "The red of the clay is one of the 'colors'"], "Pottery_of_ancient_Greece")
STYLES["maya-painted-ceramics"] = ("Classic Maya Painted Ceramics", "Codex-style vase painting",
    "Maya artists painted palace scenes and myths around cylindrical vases in a calligraphic line, with glyph blocks that actually write names and events — pictures and text in one band.",
    ["The scene unrolls like a scroll around the pot", "Cream, red and black carry the palette", "Glyph blocks sit inside the picture as captions"], "Maya_ceramics")
STYLES["medieval-illumination"] = ("Medieval Manuscript Illumination", "Gold leaf on parchment",
    "Monks and court artists lit up books with gold: miniature paintings inside decorated letters and margins crawling with vines, beasts and jokes. The page, not the wall, was Europe's picture gallery for centuries.",
    ["Real gold areas catch the light first", "Borders teem with plants and tiny creatures", "Decorative script lines complete the page"], "Illuminated_manuscript")
STYLES["persian-manuscript"] = ("Persian Manuscript Painting", "Miniatures for epic poetry",
    "Illustrations for the Shahnameh and court poetry: jewel colors, gold skies, architecture cut open like a dollhouse, and gardens in eternal spring. Space stacks upward in tiers instead of receding.",
    ["A gold or midnight sky ignores natural light", "Figures are small, refined and numerous", "Pattern covers every surface — tile, textile, garden"], "Persian_miniature")
STYLES["mughal-album"] = ("Mughal Album Painting", "Court miniature, India",
    "Persian technique meets Indian observation at the Mughal court: exquisitely fine miniatures, mounted in albums with floral borders, recording court life, hunts and nature with jewelers' precision.",
    ["Hair-thin lines model faces and fabrics", "A wide floral margin frames the scene", "Colors are soft jewels — refined, never loud"], "Mughal_painting")
STYLES["mithila"] = ("Mithila Painting", "Madhubani folk art, India and Nepal",
    "Painted by women of Mithila on walls and paper for weddings and festivals: double outlines, hatched color fills, and no empty space anywhere — nature abhors a vacuum here.",
    ["Every area is filled with pattern or creatures", "Double outlines give shapes a stitched energy", "Faces often appear in profile with one large eye"], "Madhubani_art")
STYLES["rinpa"] = ("Rinpa", "Japanese decorative school",
    "Rinpa artists distilled nature into design: gold-leaf grounds, bold silhouettes of plum, maple and waves, and tarashikomi — pigments pooled wet into each other for soft, lucky edges.",
    ["Gold ground replaces sky and air", "Natural motifs are simplified into emblems", "Pooled pigment blurs some edges on purpose"], "Rinpa_school")
STYLES["chinese-ink-landscape"] = ("Chinese Ink Landscape", "Shan shui tradition",
    "For a thousand years, China's scholar-painters held landscape — shan shui, 'mountain-water' — as the highest art. Our model keeps a seat, but the café becomes a pavilion among cliffs, mist and waterfalls: humans are guests in nature, not its owners.",
    ["Mist and empty paper do as much work as ink", "Mountains stack in receding veils", "The figure is small inside a vast world"], "Shan_shui")
STYLES["chaekgeori"] = ("Chaekgeori", "Korean books-and-objects painting",
    "Joseon-dynasty screens celebrating scholarship: books, brushes, ceramics and curios stacked on shelves in playful near-trompe-l'œil. A still life that is really a portrait of a mind.",
    ["Shelves of books and objects fill the picture", "Objects are painted with loving, slightly impossible precision", "Our model sits inside the library like one of its treasures"], "Chaekgeori")
STYLES["kalighat"] = ("Kalighat Painting", "Bazaar art, 19th-century Kolkata",
    "Painters outside Kolkata's Kalighat temple sold quick, bold watercolors to pilgrims: sweeping single-stroke outlines, flat washes, figures modeled with a few confident shadows. A souvenir that became a school.",
    ["One sweeping brush line defines each form", "Flat washes with minimal shading", "The figure feels sculptural despite the flatness"], "Kalighat_painting")
STYLES["wayang-kulit"] = ("Wayang Kulit", "Indonesian shadow theatre",
    "The picture is a shadow: a perforated leather puppet, gilded and painted, performed behind a lit screen with rods at its joints. You are seeing the puppet itself — profile is not a style here, it is physics.",
    ["The figure is a flat silhouette with pierced patterns", "Articulated rods attach at the joints", "Warm flame-light glows behind the screen"], "Wayang")
STYLES["ayacucho-retablo"] = ("Ayacucho Retablo", "Peruvian portable altar box",
    "Andean artists pack whole worlds into wooden boxes: tiers of small painted figures acting out festivals, markets and daily life behind opening doors. Our café joins a fab scene inside the box.",
    ["The scene lives inside an open wooden box", "Small modeled figures, brightly painted", "Multiple tiers tell several stories at once"], "Retablo")

# --- Lesson 6: canon ---
STYLES["renaissance-perspective"] = ("Renaissance Perspective", "Italy, 1400s",
    "Brunelleschi and Alberti turned space into mathematics: one vanishing point, receding floor tiles, architecture like a proof. The four variants place our model in loggias, halls and piazzas built by the rule.",
    ["Floor lines and arches converge to one point", "Space feels measurable and calm", "Figures are placed like pieces in the geometry"], "Perspective_(graphical)")
STYLES["baroque"] = ("Baroque", "Europe, 1600s",
    "The Renaissance room explodes: candlelight, swirling drapery, diagonals, drama. Baroque art is theatre that refuses to sit still — Caravaggio's spotlight, Rubens' motion.",
    ["Strong light-dark contrast (chiaroscuro)", "Diagonals and billowing cloth create motion", "Everything feels one second before climax"], "Baroque")
STYLES["neoclassicism"] = ("Neoclassicism", "Late 1700s, after David",
    "A stern correction to Baroque excess: clean outlines, marble surfaces, Roman virtue. Our variants include an oath-taking scene that turns cleanroom engineers into Roman citizens.",
    ["Sculptural figures with crisp contours", "Marble, columns and restrained color", "Poses quote Roman statues and reliefs"], "Neoclassicism")
STYLES["rococo"] = ("Rococo", "France, early 1700s",
    "The aristocracy at play: pastel silk, shell curves, garden swings and flirtation. Fragonard's swing hangs in this lesson's DNA — froth with world-class technique underneath.",
    ["Powdery pastels and golden light", "Curves everywhere — no straight line survives", "The mood is a garden party, slightly unreal"], "Rococo")
STYLES["romanticism"] = ("Romanticism", "Early 1800s",
    "Feeling against reason: lone figures before fog, storms, ruins and the sublime — nature big enough to make humans tremble. Friedrich's wanderer and Turner's tempests lead the variants.",
    ["Vast weather dwarfs the figure", "Light breaks through cloud like revelation", "Ruins and cliffs stand for time and fate"], "Romanticism")
STYLES["pre-raphaelite"] = ("Pre-Raphaelite Painting", "England, from 1848",
    "Young rebels painted with jeweler's detail and jewel color: every leaf counted, literary heroines in real landscapes, intensity bordering on obsession.",
    ["Botanical, almost photographic detail", "Saturated jewel colors in sharp focus", "A melancholy, storybook stillness"], "Pre-Raphaelite_Brotherhood")
STYLES["tonalism"] = ("Tonalism", "America, late 1800s",
    "Nearly one color: dusk, mist and hush. Tonalists traded detail for mood, painting the moment when the world goes quiet and forms melt into a single chord.",
    ["One dominant tone veils the whole scene", "Details dissolve into mist", "It feels like a memory, not a view"], "Tonalism")
STYLES["dutch-vanitas"] = ("Dutch Vanitas Still Life", "Netherlands, 1600s",
    "Beautiful objects with a warning label: wilting flowers, hourglasses, snuffed candles — worldly pleasures are brief. Our café table is restaged as a memento mori, the wafer as a golden disc among the props.",
    ["Deep darkness with a single raking light", "Every object is a symbol of time passing", "Rich textures: glass, petal, metal, crumb"], "Vanitas")
STYLES["french-realism"] = ("French Realism", "Courbet and Millet, mid-1800s",
    "Paint what you see, at life size, without mythology: workers, stone-breakers, gleaners. Scandalous in 1850, it is now the ancestor of documentary everything. Our model joins fab workers at shift change.",
    ["Earthy, unglamorous palette", "Labor is shown with dignity, not pity", "No halos, no costumes — the present day"], "Realism_(arts)")

# --- Lesson 7: public ---
STYLES["mexican-muralism"] = ("Mexican Muralism", "Rivera, Orozco, Siqueiros, 1920s-40s",
    "After the Mexican Revolution, the state handed its walls to painters: history, labor and identity at architectural scale, readable by a crowd that might not read words. The variants channel Rivera's registers, Orozco's fire and Siqueiros' dynamism.",
    ["Figures are monumental, bigger than life", "Stories unfold in stacked registers", "Workers and machines are the heroes"], "Mexican_muralism")
STYLES["harlem-renaissance"] = ("Harlem Renaissance", "New York, 1920s-30s",
    "Aaron Douglas's silhouettes and murals gave the Harlem Renaissance its graphic voice: flat forms, radiating light, African motifs and jazz-age rhythm, asserting identity and modernity at once.",
    ["Flattened, silhouette-like figures", "Radiating arcs and rhythmic pattern", "Gold, black and earth tones carry pride and energy"], "Harlem_Renaissance")
STYLES["american-regionalism"] = ("American Regionalism", "Grant Wood's America, 1930s",
    "Midwestern painters answered European modernism with rolling farmland, small towns and curved, rhythmic clarity — our fab rises from the prairie like a grain elevator.",
    ["Rolling, rhythmic landscape curves", "Clean modeling with a storybook clarity", "Local pride as subject matter"], "Regionalism_(art)")
STYLES["soviet-socialist-realism"] = ("Soviet Socialist Realism", "USSR, from 1934",
    "The mandated style of the Soviet state: academic realism put to heroic optimism — workers, engineers and collective triumphs, idealized and sunlit. Study it as both painting and persuasion. (Our version keeps the banners wordless.)",
    ["Heroic scale and confident poses", "Bright, optimistic academic realism", "Machinery and banners stage the message"], "Socialist_realism")
STYLES["new-objectivity"] = ("New Objectivity", "Neue Sachlichkeit, Weimar Germany",
    "After Expressionism's fever, a cold eye: Dix and Schad painted cafés, portraits and streets with crystalline precision and quiet irony. Nothing is exaggerated, and that is what stings.",
    ["Razor-sharp, almost photographic detail", "Cool, detached emotional temperature", "Modern life observed without comfort"], "New_Objectivity")
STYLES["arts-and-crafts"] = ("Arts and Crafts", "William Morris and the movement, from 1860s",
    "A rebellion against factory goods: honest materials, visible handwork, medieval-revival pattern. Morris's workshops wove, printed and built the café around our model — art you live inside.",
    ["Pattern drawn from plants, honestly stylized", "Wood, textile and print textures everywhere", "Nothing pretends to be another material"], "Arts_and_Crafts_movement")

# --- Lesson 8: modernism ---
STYLES["impressionism"] = ("Impressionism", "France, 1870s",
    "Paint the light, not the thing: broken brushstrokes of pure color that fuse in the viewer's eye. The variants quote Renoir's terraces, Monet's riverbanks and Pissarro's boulevards — afternoons you can almost feel.",
    ["Visible, broken brushstrokes", "Shadows are blue and violet, never black", "The scene sparkles and breathes"], "Impressionism")
STYLES["pointillism"] = ("Pointillism", "Seurat's dots, 1880s",
    "Impressionism made systematic: thousands of distinct dots of pure color, mixed by your eye, not the palette. Stand close — confetti. Stand back — a sunny café.",
    ["The image is built only from dots", "Colors vibrate where complements touch", "Stillness and order beneath the shimmer"], "Pointillism")
STYLES["symbolism"] = ("Symbolism", "Dream and myth, 1880s-1900s",
    "Against realism, a art of suggestion: jeweled palaces, crescent moons, peacocks and beautiful melancholy. Moreau, Klimt and Redon haunt the four variants — pictures that behave like dreams and poems.",
    ["Gold, jewel tones and moonlight", "Ornament swallows the figure into pattern", "Everything feels symbolic of something unnamed"], "Symbolism_(arts)")
STYLES["fauvism"] = ("Fauvism", "'Wild beasts' of color, 1905",
    "Matisse and Derain let color off the leash: green skies, orange floors, pink light — chosen for feeling and harmony, not description. Critics called them fauves, wild beasts; they kept the name.",
    ["Colors are arbitrary and high-key", "Forms simplify so color can lead", "Even a cleanroom turns into a sunflower field"], "Fauvism")
STYLES["expressionism"] = ("Expressionism", "Germany, 1905-1920s",
    "Distort the world to match the feeling: jagged streets, acid color, anxious crowds. Kirchner's tilted Berlin and Munch's unease drive these variants — the café as a state of mind.",
    ["Forms tilt, stretch and sharpen", "Colors clash on purpose — acid green, blood red", "Brushwork is agitated, never calm"], "Expressionism")
STYLES["cubism"] = ("Cubism", "Picasso and Braque, from 1907",
    "Break the object into facets and show several viewpoints at once. The café table, cup and sitter shatter into interlocking planes — then, in the synthetic variant, reassemble as bright flat shapes.",
    ["One object, several viewpoints, same canvas", "Ochre and gray dominate the analytic variant", "Glasses become twin circles; planes overlap like glass shards"], "Cubism")
STYLES["futurism"] = ("Futurism", "Italy, from 1909",
    "Speed as beauty: repeated limbs, motion echoes, city light streaking past. Boccioni and Balla painted what a photograph of movement feels like — our model multiplied across the boulevard.",
    ["The figure repeats in motion phases", "Diagonal speed lines cut the scene", "Machines and lights share the stage as equals"], "Futurism")
STYLES["orphism"] = ("Orphism", "Delaunay's color discs, 1910s",
    "Abstraction you can dance to: concentric discs and arcs of simultaneous color, named for Orpheus and music. Our model is woven into the swirl — present, but rhythm first.",
    ["Color arrives in discs and arcs", "Complements vibrate against each other", "The figure emerges from pure rhythm"], "Orphism_(art)")
STYLES["surrealism"] = ("Surrealism", "Dream logic, from 1924",
    "Paint the unconscious: melting wafers in a desert, cups orbiting a dream room, a sea inside a teacup. Dalí's precision, Magritte's calm absurdity and Ernst's forests animate the variants — impossible things, rendered believably.",
    ["Impossible events painted with total conviction", "Familiar objects misbehave quietly", "Horizons and skies feel too clear, like dreams"], "Surrealism")
STYLES["dada-photomontage"] = ("Dada Photomontage", "Berlin Dada, 1918-1920s",
    "Hannah Höch and John Heartfield weaponized scissors and newspapers: photographs cut apart and recombined into absurd, satirical machines. Our model is quite literally assembled from clippings.",
    ["Visible scissor edges and halftone textures", "Newspaper, gears and advertisements collide", "Scale makes no sense, deliberately"], "Dada")

# --- Lesson 9: systems ---
STYLES["art-nouveau"] = ("Art Nouveau", "1890s-1910s",
    "The whiplash line: Mucha's posters turned hair, stems and smoke into one flowing system of ornament. The variants give our model the full treatment — halo, café terrace, allegory panel, theatre poster.",
    ["Sinuous, plant-like curves organize everything", "A circular halo frames the figure like a jewel", "Muted gold, sage and peach harmonize"], "Art_Nouveau")
STYLES["art-deco"] = ("Art Deco", "1920s-30s glamour",
    "Nouveau's curves grow up into geometry: sunbursts, chevrons, symmetry, gold on black. The style of skyscrapers, ocean liners and movie palaces — our model's natural habitat, honestly.",
    ["Strict symmetry and stepped forms", "Gold, black and emerald luxury", "Everything looks engineered and elegant"], "Art_Deco")
STYLES["bauhaus"] = ("Bauhaus Graphic Design", "Germany, 1919-1933",
    "A school that redesigned the world from first shapes: circle, triangle, square; red, yellow, blue. The variants build our model from pure geometry, Kandinsky's circles, Klee's play and Schmidt's typographic grids.",
    ["Primary shapes and colors do the drawing", "Composition follows a visible grid or diagonal", "Playfulness survives inside the system"], "Bauhaus")
STYLES["constructivism"] = ("Constructivism", "Rodchenko and Lissitzky, 1920s",
    "Art as engineering for a new society: bold diagonals, red-black-cream photomontage, figures thrust forward like pistons. Text is banished in our variants — wafer discs carry the message instead.",
    ["Diagonals dominate; nothing sits level", "Red, black and cream only", "Photomontage scale shifts: giant profile, small figure"], "Constructivism_(art)")
STYLES["de-stijl"] = ("De Stijl", "Mondrian's grid, 1917-1930s",
    "The strictest system of all: black lines, white ground, red-yellow-blue rectangles — and, hidden in our study, a seated figure. Proof that a person can survive total abstraction, barely.",
    ["Only horizontals, verticals and primaries", "Balance is achieved without symmetry", "The figure is a guest inside the grid"], "De_Stijl")
STYLES["op-art"] = ("Op Art", "Optical painting, 1960s",
    "Bridget Riley and Victor Vasarely turned retinal physics into art: stripes that bend, grids that swell, moiré that hums. Our model's profile appears as a shift in the pattern in one variant — find her in all four.",
    ["Patterns vibrate, warp or bulge", "Black-and-white does most of the work", "Your eyes feel the picture before your mind does"], "Op_art")
STYLES["abstract-expressionism"] = ("Abstract Expressionism", "New York, 1940s-50s",
    "Painting as event: Pollock's dripped webs, de Kooning's fierce women, Rothko's glowing fields, Kline's black architecture. Our figure emerges from, dissolves into, and finally becomes four giant brushstrokes.",
    ["Gesture and scale replace description", "The figure is found inside the paint, not under it", "Each variant quotes a different giant of the movement"], "Abstract_expressionism")
STYLES["minimalism"] = ("Minimalism", "1960s, reduction as meaning",
    "What remains when you remove almost everything? One figure, immense quiet, space doing the talking. Minimalism trusts the viewer to complete the work.",
    ["Vast emptiness is the main element", "A single quiet figure anchors the void", "Nothing decorative survives"], "Minimalism")
STYLES["swiss-style"] = ("Swiss Style", "International Typographic Style, 1950s",
    "Grids, sans-serif type, asymmetry and objectivity: the design language that still runs every transit map and app. Our poster folds the café into red-black-white order, words replaced by pure shapes.",
    ["A strict grid organizes the layout", "Red, black and white only", "Asymmetry feels balanced and inevitable"], "International_Typographic_Style")
STYLES["precisionism"] = ("Precisionism", "Machine-age America, 1920s-30s",
    "Sheeler and Demuth painted factories like cathedrals: immaculate geometry, sharp light, no people, no dirt. Our fab machinery gets the same reverent, crystalline treatment.",
    ["Industrial forms simplified to pure geometry", "Immaculate surfaces and hard light", "Stillness — the machines seem to be holding their breath"], "Precisionism")

# --- Lesson 10: pop ---
STYLES["pop-art"] = ("Pop Art", "1950s-60s, Britain and America",
    "Soup cans, comics and advertisements, enlarged until they become icons. Lichtenstein's Ben-Day dots and Warhol's repeated portraits lead the variants — our model as comic heroine and as silkscreen grid.",
    ["Dots, flat ink and commercial color", "Repetition turns a portrait into a brand", "Speech balloons and product shots invade fine art"], "Pop_art")
STYLES["psychedelic-poster"] = ("Psychedelic Poster Art", "San Francisco, 1966-1970s",
    "Fillmore concert posters melted Art Nouveau lettering into liquid, vibrating color — legibility sacrificed to sensation. Letterforms survive in our version as pure shapes inside the swirl.",
    ["Complementary colors vibrate at maximum volume", "Shapes flow like liquid or smoke", "The figure dissolves into the trip"], "Psychedelic_art")
STYLES["memphis-design"] = ("Memphis Design", "Milan, 1981 onwards",
    "Ettore Sottsass's Memphis Group declared war on good taste: squiggles, terrazzo, pastel clashes, shapes that refuse to behave. Design as a joke that turned out to be liberation.",
    ["Squiggles, zigzags and terrazzo patterns", "Pastel collides with black and primary brights", "Nothing matches, on purpose, joyfully"], "Memphis_Group")
STYLES["space-age-design"] = ("Space Age Design", "Atomic-age futurism, 1950s-60s",
    "Starbursts, boomerangs and orbital rings: the future as imagined from a 1962 kitchen. Our café becomes a retro-future lounge, glossy white and orange under a ringed planet.",
    ["Atomic starbursts and boomerang shapes", "Glossy white, orange and teal optimism", "Everything looks like a toy rocket's interior"], "Space_Age")
STYLES["afrofuturism"] = ("Afrofuturism", "Black futures, from the 1970s",
    "African heritage projected into cosmic technology: regal gold, adinkra-like motifs, starfields and advanced cities — a corrective to futures that left Black people out. Our model takes the throne under the stars.",
    ["Gold regality meets high technology", "Starfields and cosmic scale", "Traditional motifs redesigned as future insignia"], "Afrofuturism")

# --- Lesson 11: beyond ---
STYLES["land-art"] = ("Land Art", "Earthworks, from the late 1960s",
    "Robert Smithson spiraled a jetty into the Great Salt Lake; our version spirals stones and wafers across a desert flat, with the artist tiny inside her own drawing. The landscape is the canvas, and weather is a collaborator.",
    ["The artwork is visible fully only from the air", "Materials come from the site itself", "The human figure is a speck in the work"], "Land_art")
STYLES["light-and-space"] = ("Light and Space", "Perceptual installation, California 1960s-",
    "Turrell and Irwin made light itself the material: rooms of haze and color where edges vanish and your own perception becomes the exhibit. Our model softens into wine-red and amber atmosphere.",
    ["Color has no visible source or edge", "The figure dissolves into atmosphere", "Seeing itself is the subject"], "Light_and_Space")
STYLES["brutalist-architecture"] = ("Brutalist Architecture", "Raw concrete, 1950s-70s",
    "Béton brut — raw concrete — raised into monumental, shadow-carved masses. Our fab complex looms like a fortress, and the café table shrinks to a human footnote.",
    ["Board-formed concrete texture everywhere", "Huge masses, deep shadow reveals", "The person is small; the building is the portrait"], "Brutalist_architecture")
STYLES["deconstructivist-architecture"] = ("Deconstructivist Architecture", "Fragmented form, from the 1980s",
    "Gehry and Hadid broke the box: titanium shards, tilted walls, colliding geometries that look mid-explosion, frozen. Our model sits calmly inside the beautiful wreckage.",
    ["Forms tilt, fracture and collide", "No wall agrees with another", "Calm figure, chaotic space"], "Deconstructivism")
STYLES["kinetic-sculpture"] = ("Kinetic Sculpture", "Art that moves",
    "Calder's mobiles turned sculpture into slow weather: balanced discs and rods rotating on air currents. Ours hangs wafer discs above our model, who has become part of the mechanism.",
    ["Balance and rotation are the composition", "Shadows move as the piece moves", "Engineering and poetry are the same act"], "Kinetic_art")
STYLES["gutai"] = ("Gutai", "Japanese avant-garde, 1954-1972",
    "'Concreteness': Gutai artists wrestled paint itself — flinging, pouring, breaking through paper — letting material act. Our model is mid-performance, wine-red paint in flight across raw canvas.",
    ["Paint is thrown, not brushed", "Raw canvas and splashes are the image", "The body of the artist is a tool"], "Gutai_group")
STYLES["ballets-russes"] = ("Ballets Russes Stage Design", "Bakst and Diaghilev, 1909-1929",
    "Diaghilev's company fused painting, music and dance into total theatre, and Bakst's sets — exotic, ornate, drenched in color — redesigned European taste. Our model takes the principal's bow.",
    ["The whole stage is one ornamental painting", "Costume and set share the same patterns", "Color is theatrical: emerald, gold, flame"], "Ballets_Russes")
STYLES["stop-motion"] = ("Stop-Motion", "Frame-by-frame puppet animation",
    "A handmade world photographed one frame at a time: clay, felt and miniature furniture, with the maker's fingerprints left in. Our café set is a tiny stage, charm included.",
    ["Visible clay and felt textures", "Miniature furniture, slightly imperfect", "It looks photographed, because the set 'exists'"], "Stop_motion")

# --- Lesson 12: games ---
STYLES["pixel-art"] = ("Pixel Art", "The digital mosaic",
    "Every pixel placed on purpose. Born from hardware limits, kept as a discipline: limited palettes, readable silhouettes, dithering for gradients. Compare the sunset variant's dithered sky with the watercolor in Lesson 1 — same problem, opposite tools.",
    ["A strict grid underlies every curve", "Dithering fakes extra colors", "Silhouette stays readable at tiny size"], "Pixel_art")
STYLES["nes-8bit"] = ("NES 8-Bit", "Nintendo Entertainment System, 1985",
    "The NES palette held 54 colors, and each sprite could use only a few — so artists became economists. Our café runs on chunky pixels, flat color and hard outlines: charm extracted from scarcity. (Rendered a little finer than real hardware sprites, honestly.)",
    ["Huge, visible pixels", "Flat colors with black outlines", "Backgrounds simplify into tiles and shapes"], "Nintendo_Entertainment_System")
STYLES["snes-16bit"] = ("SNES 16-Bit", "Super Nintendo, 1991",
    "Thousands of colors on screen, finer pixels, real shading: the 16-bit generation could finally do atmosphere. The same café gains dusk, glow and detail the NES could only imply.",
    ["Finer pixels, smoother curves", "Dithered gradients and richer palettes", "Backgrounds become places, not tiles"], "Super_Nintendo_Entertainment_System")
STYLES["ps1-2d"] = ("PS1 2D Sprites", "PlayStation, late 1990s",
    "While 3D grabbed headlines, 2D quietly peaked: high-resolution hand-drawn sprites over painted, pre-rendered backgrounds in games like Legend of Mana. Our café is lush, crisp and faintly soft with CRT warmth.",
    ["Hand-drawn sprite over a painted world", "Background detail exceeds the character's", "A slight softness, like a good CRT"], "Sprite_(computer_graphics)")
STYLES["ps1-3d-lowpoly"] = ("PS1 3D Low-Poly (FF7 Era)", "PlayStation, 1997",
    "First-generation 3D: a few hundred polygons per character, flat Gouraud shading, textures that swim and warp. Final Fantasy VII's field screens paired these blocky figures with gorgeous pre-rendered backgrounds — the contrast is the era's signature.",
    ["Angular, faceted models with chunky hands", "The background is far prettier than the model", "Textures wobble if you imagine it moving"], "Low_poly")
STYLES["ps1-3d-refined"] = ("PS1 3D Refined (DOA Era)", "Late PlayStation, 1997-2000",
    "By the original Dead or Alive, PS1 models had multiplied their polygons: rounded joints, texture-mapped faces, cleaner shading — still low-res and wobbly at heart, but unmistakably smoother. The ladder's middle rung.",
    ["Rounded, smoother silhouettes than the FF7 rung", "Faces are textures, not geometry", "Low-res softness lingers over everything"], "Dead_or_Alive_(video_game)")
STYLES["ps3-ps4-3d"] = ("PS3 / PS4 HD 3D", "High-definition era, 2006-2020",
    "HD real-time rendering: high-polygon models, normal maps faking fine detail, soft shadows and cinematic depth of field. The café is now a cutscene — polished CGI that still, visibly, comes from a game engine.",
    ["Soft shadows and shallow focus", "Fabric and skin have surface detail", "Clean, cinematic, but not yet photographic"], "PlayStation_4")
STYLES["ps5-raytraced"] = ("PS5 Ray-Traced", "Current generation, 2020-",
    "Ray tracing simulates light itself: true reflections in the window and cup, soft global illumination, skin that scatters light. The ladder tops out near photography — compare with Lesson 3's photorealism and ask what, if anything, still gives the game away.",
    ["Reflections behave physically correctly", "Individual hair strands and skin pores", "Light bounces the way it does in rooms"], "Ray_tracing_(graphics)")
STYLES["stylized-3d"] = ("Stylized 3D Rendering", "Non-photorealistic 3D",
    "Not every modern game chases realism: stylized rendering keeps 3D's freedom but paints its surfaces — soft studio light, smooth materials, a game-cinematic look that ages gracefully because it never pretended to be a photo.",
    ["Smooth, toy-like material perfection", "Lighting is soft and designed, not simulated", "It reads as '3D illustration', proudly"], "Non-photorealistic_rendering")
