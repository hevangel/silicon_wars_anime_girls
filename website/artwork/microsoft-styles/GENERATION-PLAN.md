# Microsoft style atlas — generation plan

Keep the 105 existing studies and five lesson tracks. Start with how a mark is made, then move to objects and visual traditions, composition and public life, design and performance, and game graphics. Insert the comparisons in their matching topic. Keep the introductory anime and manga sequence and existing links. Make each example searchable.

Of 368 requested terms, 365 receive new illustrations. Reuse three illustrated examples with searchable aliases: **impasto** (oil board, upper right), **3D CGI render** (stylized 3D rendering), and **1-bit art** (pixel board, upper left). Give related traditions their own examples even when they share a medium. Etching uses acid, for instance, whereas engraving uses a cutting tool.

Generate one image per comparison. Read four squares across then down. For smaller sets keep examples large and specify positions. Preserve the Microsoft character and adapt her role. For sacred, community-specific or nonfigurative work, show her encountering or studying it where appropriate. Label the results as contemporary teaching studies. Give each example a visible clue and historical context, and distinguish what a still can demonstrate from what depends on movement.

## Reading routes

The busiest topics split into smaller galleries. In **Read surfaces and patterns**, compare fiber and cloth, assembled surfaces, carved and cast figures, and designs in everyday use. In **Read across an image**, start with walls, then devotional images, then pages and narrative settings. Search opens an individual example directly. The guided questions pair older studies with the new boards.

## Maintaining the galleries

The board order and requested terms live in [atlas/plan.json](atlas/plan.json). Each numbered record contains image dimensions, a caption, notes on when and why to use each approach, and historical sources. The generation prompt is stored with the corresponding record. After editing records or adding a finished board, run `python atlas/build_atlas.py` from this folder (Python 3.10 or later). The script updates the marked galleries in [index.html](index.html). The resulting page and its images work as static files.

## Board assignments

- **atlas-001 · How four drawing tools leave a line** (drawing-paint-and-paper) — silverpoint / red chalk / conté / ballpoint drawing.
- **atlas-002 · Covering and uncovering a surface** (drawing-paint-and-paper) — oil pastel / airbrush art / scratchboard / marker rendering.
- **atlas-003 · What holds pigment in place** (drawing-paint-and-paper) — encaustic / casein painting / distemper / fresco secco.
- **atlas-004 · Building a painted surface** (drawing-paint-and-paper) — palette knife painting / grisaille / spray paint / mixed media.
- **atlas-005 · Four ways to ink a metal plate** (prints-photographs-and-camera-vision) — engraving / drypoint / aquatint / mezzotint.
- **atlas-006 · Block, stencil and single impression** (prints-photographs-and-camera-vision) — wood engraving / monotype / chiaroscuro woodcut / pochoir stencil.
- **atlas-007 · Making editions for many readers** (prints-photographs-and-camera-vision) — letterpress / halftone printing / CMYK offset printing / risograph.
- **atlas-008 · Pictures circulated on paper** (prints-photographs-and-camera-vision) — shin-hanga / Chinese New Year prints / calavera prints / sōsaku-hanga.
- **atlas-009 · An image made by light and chemistry** (camera-and-evidence) — daguerreotype / wet-plate photography / tintype / photogram.
- **atlas-010 · Choosing what a camera records** (camera-and-evidence) — straight photography / street photography / color photography / Düsseldorf School photography.
- **atlas-011 · Directing a photograph** (camera-and-evidence) — staged photography / fashion photography / double exposure.
- **atlas-012 · Tricking the eye and the lens** (stage-a-figure-or-a-room) — hyperrealism / illusionistic ceiling painting / anamorphosis / matte painting.
- **atlas-013 · Pattern built with thread** (pattern-craft-and-objects) — tapestry / Bayeux-style embroidery / Persian carpet / goldwork.
- **atlas-014 · Assembling a tiled surface** (pattern-craft-and-objects) — Islamic tilework / Iznik tilework / zellige / azulejo.
- **atlas-015 · Inlay, enamel and polished layers** (pattern-craft-and-objects) — lacquerware / cloisonné enamel / pietra dura / marquetry.
- **atlas-016 · Sculpture in the round** (pattern-craft-and-objects) — freestanding marble sculpture / cast bronze sculpture / wood sculpture / terracotta sculpture.
- **atlas-017 · Constructing a surface from units** (pattern-craft-and-objects) — blown glass / beadwork / basketry / featherwork.
- **atlas-018 · Cut, carve and float a design** (pattern-craft-and-objects) — papercutting / ivory carving / paper marbling.
- **atlas-019 · Figures across rock, plaster and time** (stories-on-walls-and-pages) — Paleolithic cave painting / Saharan rock art / San rock art / Minoan fresco.
- **atlas-020 · Power along a processional route** (stories-on-walls-and-pages) — Mesopotamian art / Assyrian relief / Ishtar Gate / Achaemenid relief.
- **atlas-021 · Bodies in the ancient Mediterranean** (stories-on-walls-and-pages) — Cycladic sculpture / Classical Greek sculpture / Fayum mummy portraits / Etruscan tomb painting.
- **atlas-022 · Rooms, floors and early Christian walls** (stories-on-walls-and-pages) — Roman wall painting / Roman mosaic / catacomb painting.
- **atlas-023 · Painting for devotion** (stories-on-walls-and-pages) — Byzantine icon / Russian icon painting / Ethiopian Christian painting / Armenian manuscript illumination.
- **atlas-024 · How a manuscript commands attention** (stories-on-walls-and-pages) — Insular art / Book of Kells style / Carolingian art / Ottonian art.
- **atlas-025 · Medieval figures and courtly gestures** (stories-on-walls-and-pages) — Romanesque art / Gothic art / International Gothic.
- **atlas-026 · Writing, geometry and branching ornament** (pattern-craft-and-objects) — Islamic calligraphy / geometric pattern / arabesque.
- **atlas-027 · Court portraits and painted stories** (stories-on-walls-and-pages) — Ottoman miniature / Qajar painting / Rajput miniature / Pahari miniature.
- **atlas-028 · Painting devotion across South Asia** (stories-on-walls-and-pages) — Ajanta mural / Tibetan thangka / Tibetan mandala / Tanjore painting.
- **atlas-029 · Figures made for a place** (pattern-craft-and-objects) — Chola bronze / South Asian temple sculpture / Khmer relief / Angkor art.
- **atlas-030 · Line, rhythm and the painted cloth** (pattern-craft-and-objects) — Pattachitra / Warli / Gond / Kalamkari.
- **atlas-031 · Schools and settings in southern Asia** (stories-on-walls-and-pages) — Company painting / Bengal School / Thai temple mural / Balinese Kamasan painting.
- **atlas-032 · Print, lacquer, mural and cast vessel** (pattern-craft-and-objects) — Đông Hồ print / Vietnamese lacquer painting / Dunhuang Buddhist murals / Chinese ritual bronze.
- **atlas-033 · Four uses of a Chinese brush** (light-weather-and-landscape) — Chinese calligraphy / gongbi painting / bird-and-flower painting / literati painting.
- **atlas-034 · Reworking the ink tradition** (light-weather-and-landscape) — Shanghai School / Lingnan School / contemporary Chinese ink.
- **atlas-035 · Japanese pictures for rooms and readers** (light-weather-and-landscape) — Yamato-e / Kanō school / Zen ink painting / Nanga.
- **atlas-036 · Painting, folk craft and everyday wishes** (pattern-craft-and-objects) — Nihonga / Mingei / minhwa.
- **atlas-037 · Three approaches in Korean art** (light-weather-and-landscape) — true-view landscape / Goryeo Buddhist painting / Dansaekhwa.
- **atlas-038 · Heads and figures in metal and clay** (pattern-craft-and-objects) — Ife bronze / Benin bronze / Nok terracotta.
- **atlas-039 · Carving and performance in context** (performance-puppetry-and-kinetic-art) — Dan mask / Fang mask / Pende mask.
- **atlas-040 · Woven, painted and resisted pattern** (pattern-craft-and-objects) — Kuba cloth / kente / Ndebele house painting / adire.
- **atlas-041 · Marks and collective identity** (graphic-design-and-public-messages) — uli / nsibidi / Asafo flag.
- **atlas-042 · Workshops and reused materials** (work-and-public-life) — Tinga Tinga / Oshogbo School / El Anatsui-style metal tapestry.
- **atlas-043 · Painting place and tracing a curve** (pattern-craft-and-objects) — Aboriginal bark painting / Western Desert dot painting / kōwhaiwhai / tapa cloth.
- **atlas-044 · Carved and assembled Pacific forms** (pattern-craft-and-objects) — Māori carving / Sepik carving / Rapa Nui art / Hawaiian featherwork.
- **atlas-045 · Mesoamerican monuments and painted books** (stories-on-walls-and-pages) — Olmec sculpture / Teotihuacan mural / Aztec codex / Mixtec codex.
- **atlas-046 · Andean textiles and painted vessels** (pattern-craft-and-objects) — Paracas textile / Inca textile / Moche ceramic / Nazca ceramic.
- **atlas-047 · Four ways of recording a living world** (stories-on-walls-and-pages) — Northwest Coast formline / Plains ledger art / Kinngait print / Woodlands School.
- **atlas-048 · Building pattern in the Americas** (pattern-craft-and-objects) — Mimbres pottery / Pueblo pottery / Navajo weaving / Huichol yarn painting.
- **atlas-049 · Pictures under colonial rule and after** (work-and-public-life) — amate / Cuzco School / casta painting / Haitian painting.
- **atlas-050 · Layers of cut cloth** (pattern-craft-and-objects) — mola.
- **atlas-051 · Making sacred figures inhabit space** (stage-a-figure-or-a-room) — Proto-Renaissance / Early Netherlandish painting / Northern Renaissance / High Renaissance.
- **atlas-052 · Color, gesture and staged light** (stage-a-figure-or-a-room) — Venetian colorism / Mannerism / Dutch Golden Age painting / Spanish Golden Age painting.
- **atlas-053 · Composing status and civic space** (stage-a-figure-or-a-room) — French classicism / Academic art / vedute / Grand Manner portrait.
- **atlas-054 · Intimacy, invention and the imagined past** (emotion-dreams-and-metaphor) — Goya's art / Chardin's art / Orientalism / Nazarenes.
- **atlas-055 · What a landscape emphasizes** (light-weather-and-landscape) — English landscape painting / Hudson River School / Barbizon School / Luminism.
- **atlas-056 · Painting observed life** (work-and-public-life) — American Realism / Macchiaioli / Peredvizhniki / Naturalism.
- **atlas-057 · Whose work fills the city?** (work-and-public-life) — Ashcan School / Social Realism / New Deal mural / Chicano muralism.
- **atlas-058 · Posters competing for public attention** (graphic-design-and-public-messages) — New Deal poster / wartime propaganda poster / Chinese revolutionary poster / Cuban OSPAAAL poster.
- **atlas-059 · Print collectives and political messages** (graphic-design-and-public-messages) — Polish Poster School / May '68 poster / Taller de Gráfica Popular / AfriCOBRA.
- **atlas-060 · Who gets to speak on a wall?** (graphic-design-and-public-messages) — graffiti / street art / feminist art / Black Arts Movement.
- **atlas-061 · Landscape and national narratives** (light-weather-and-landscape) — Group of Seven / Heidelberg School / Brazilian Modernism / Indigenismo.
- **atlas-062 · Art schools and independent voices** (work-and-public-life) — Nigerian modernism / Zaria Art Society.
- **atlas-063 · Brushwork, structure and the flat print** (emotion-dreams-and-metaphor) — Cézanne's art / Van Gogh's art / Synthetism / Japonisme.
- **atlas-064 · Line across a poster, room and painting** (graphic-design-and-public-messages) — Toulouse-Lautrec poster / Les Nabis / Vienna Secession.
- **atlas-065 · From a motif toward abstraction** (abstraction-geometry-and-optical-motion) — Der Blaue Reiter / Suprematism / early pure abstraction / Synchromism.
- **atlas-066 · Four approaches to an imagined scene** (emotion-dreams-and-metaphor) — Metaphysical painting / School of Paris / Abstract Surrealism / Kahlo and Mexican modernism.
- **atlas-067 · Who decides what counts as art?** (emotion-dreams-and-metaphor) — Naïve art / Art Brut / outsider art.
- **atlas-068 · Fracturing the machine age** (abstraction-geometry-and-optical-motion) — Vorticism / Rayonism / Cubo-Futurism / Purism.
- **atlas-069 · Figuration after upheaval** (emotion-dreams-and-metaphor) — Magic Realism / CoBrA / School of London.
- **atlas-070 · Painting as a physical event** (abstraction-geometry-and-optical-motion) — Art Informel / Tachisme / Color Field painting / stain painting.
- **atlas-071 · Edges and the viewer in space** (abstraction-geometry-and-optical-motion) — hard-edge painting / Neo-Concrete.
- **atlas-072 · Designing an immediately legible sign** (graphic-design-and-public-messages) — Plakatstil / Isotype pictograms / Wiener Werkstätte / Japanese postwar graphic design.
- **atlas-073 · Products and their interfaces** (objects-and-imagined-futures) — Streamline Moderne / mid-century modern / flat design / skeuomorphism.
- **atlas-074 · Type as a visual voice** (graphic-design-and-public-messages) — New Wave typography / grunge typography.
- **atlas-075 · A building teaches you how to enter** (buildings-sites-and-installations) — Classical orders / Gothic cathedral architecture / Islamic architecture / muqarnas.
- **atlas-076 · Planning a building around a body** (buildings-sites-and-installations) — Baroque architecture / Beaux-Arts architecture / International Style architecture / organic architecture.
- **atlas-077 · Structure as a public statement** (buildings-sites-and-installations) — postmodern architecture / high-tech architecture / Metabolism / parametric architecture.
- **atlas-078 · An ordinary object becomes an artwork** (objects-and-imagined-futures) — Dada readymade / Neo-Dada / Nouveau Réalisme / Arte Povera.
- **atlas-079 · An artwork as an instruction or an action** (performance-puppetry-and-kinetic-art) — Fluxus / Conceptual art / performance art / Happening.
- **atlas-080 · Looking at consumer societies** (work-and-public-life) — Capitalist Realism / Pictures Generation / Sots Art / Chinese Political Pop.
- **atlas-081 · Reinventing the figure** (emotion-dreams-and-metaphor) — Neo-Expressionism / Young British Artists / contemporary figuration / Chicago Imagists.
- **atlas-082 · Pictures from popular culture** (objects-and-imagined-futures) — Superflat / Lowbrow / Pop Surrealism.
- **atlas-083 · Decoration, geometry and the screen** (abstraction-geometry-and-optical-motion) — Pattern and Decoration / Neo-Geo / post-internet art / glitch art.
- **atlas-084 · Invented futures and remembered screens** (objects-and-imagined-futures) — vaporwave / cyberpunk / synthwave / Y2K.
- **atlas-085 · Two alternatives for tomorrow** (objects-and-imagined-futures) — steampunk / solarpunk.
- **atlas-086 · A room or site becomes the work** (buildings-sites-and-installations) — installation art / site-specific wrapping / Mono-ha / immersive projection.
- **atlas-087 · Duration, matter and accumulation** (performance-puppetry-and-kinetic-art) — video art / assemblage / process art.
- **atlas-088 · Four ways to model a body in space** (pattern-craft-and-objects) — Rodin-style sculpture / Brâncuși-style sculpture / Giacometti-style sculpture / Moore-style sculpture.
- **atlas-089 · How a drawn figure moves** (performance-puppetry-and-kinetic-art) — classic hand-drawn animation / 1930s rubber-hose animation / mid-century limited animation / silhouette cut-out animation.
- **atlas-090 · From photographed movement to cinematic shadow** (performance-puppetry-and-kinetic-art) — rotoscope / German Expressionist cinema / film noir.
- **atlas-091 · Reading an actor from a distance** (performance-puppetry-and-kinetic-art) — Noh / Kabuki / Chinese opera.
- **atlas-092 · Arcade lines, handheld pixels and sprites** (console-graphics-timeline) — vector arcade graphics / Game Boy four-shade graphics / isometric pixel art / pre-rendered CG sprites.
- **atlas-093 · Four real-time console looks** (console-graphics-timeline) — N64-era 3D / PS2-era 3D / Dreamcast-era 3D / GameCube-era 3D.
- **atlas-094 · Choosing a visual constraint** (console-graphics-timeline) — cel-shaded 3D / voxel art / ASCII art / modern low-poly indie.
- **atlas-095 · Giving digital worlds depth** (console-graphics-timeline) — hand-painted textures / HD-2D.
- **atlas-096 · Four graphic voices on the page** (make-a-manga-panel) — American comic book / ligne claire / caricature / editorial cartoon.
- **atlas-097 · Who is the illustration for?** (make-a-manga-panel) — Golden Age illustration / children's picture book / underground comix / pulp cover.
- **atlas-098 · Drawing to explain or propose** (drawing-paint-and-paper) — botanical illustration / scientific illustration / fashion illustration / concept art.
- **atlas-099 · Two kinds of working drawing** (drawing-paint-and-paper) — technical drawing / architectural drawing.
- **atlas-100 · A design that follows the body** (pattern-craft-and-objects) — tattoo flash / American traditional tattoo / irezumi.
