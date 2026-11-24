// Variants follow the board in reading order, from top left to bottom right.
// Each variant references one of its style’s examples by zero-based index.
const styleGuide = {
  "cel": {
    history: "Animation studios spent much of the twentieth century painting moving figures on transparent sheets called cels, laid over reusable backgrounds. Digital cel shading keeps the look of that process.",
    effect: "A few separate patches of light and dark make a figure easy to read in motion. Hard shadow edges can make a scene feel crisp and decisive.",
    use: "Use it for animated action or recurring comic characters. Keep the shadows simple enough for the outfit and expression to read even in a small panel.",
    why: "The same shadow shapes can be repeated from panel to panel, so the reader can follow motion without having to decipher a new lighting scheme each time.",
    period: "Studio cel animation and Japanese television anime, 1930s–1960s",
    examples: [
      { label: "Disney studio cel for Snow White and the Seven Dwarfs (1937), Library of Congress", href: "https://www.loc.gov/item/2001698003/" },
      { label: "Astro Boy television series (1963), Tezuka Productions", href: "https://tezukaosamu.net/en/anime/30.html" },
    ],
    variants: [
      {
        detail: "Compare the two sides of the bent sleeve. One shadow shape explains the elbow before you count a single fold.",
        when: "Use classic cel for dialogue and action that need to cut together cleanly. The hard edges keep the lighting consistent from panel to panel.",
        why: "A reader can follow the body from frame to frame even while the mouth or hands change.",
        connection: "The Snow White cel shows how painted color stays inside a clean figure outline. Compare the separation of figure and surroundings with the clean shapes on this board.",
        example: 0,
      },
      {
        detail: "Look at the gradual change across one knee and then at the crisp glasses. Two kinds of edge can coexist in the same face-and-body treatment.",
        when: "Use soft cel for a gentle conversation or a close-up. The softer change in light makes the same graphic silhouette feel less severe.",
        why: "The transition makes skin or cloth feel rounder while preserving the clear outline needed across a sequence.",
        connection: "Use the Snow White cel as a historical baseline for flat paint on a transparent sheet. The soft transition here is a modern variation on that baseline.",
        example: 0,
      },
      {
        detail: "Cover the face with a finger. The dark triangle of the blazer and the gap under the elbow still locate the pose.",
        when: "Use this for reaction shots, icons, or wide panels. The pose has to communicate on its own, which makes a clear gesture especially effective.",
        why: "Saving detail for selected frames lets the audience feel a change when a later close-up adds it back.",
        connection: "Compare the clear outlines of the 1963 television Astro Boy. The comparison is about economy and readable character shapes.",
        example: 1,
      },
      {
        detail: "In this square, the strip of light on the jacket separates the shoulder from the dark interior of the sleeve.",
        when: "Use it for a confrontation or a sharp change in mood. A few bright accents in deep shadow make the audience look for the face.",
        why: "A sudden jump in contrast makes a change in attention feel immediate, even in a still frame.",
        connection: "Compare a historic cel’s even areas of color with the sharp shift to deep shade in this digital study. The shared principle is the isolated shape.",
        example: 0,
      },
    ],
  },
  "manga": {
    history: "Japanese manga grew from print culture into a major twentieth-century publishing industry. Ink and adhesive patterns called screentone let artists create a wide range of effects on black-and-white pages.",
    effect: "Solid ink gives a panel force, while patterns and pen strokes add gray, texture, and atmosphere. The same character can feel funny, ordinary, or threatening through the balance of black and white.",
    use: "Use it when a story needs to read quickly, reproduce clearly in monochrome, or shift tone without changing the color palette.",
    why: "A limited range of darks and lights lets you shift from clarity to suspense while keeping the page readable in monochrome.",
    period: "Postwar Japanese manga and monochrome print, from the 1950s",
    examples: [
      { label: "Osamu Tezuka, Mighty Atom manga (1952), Tezuka Productions", href: "https://tezukaosamu.net/en/manga/291.html" },
      { label: "Frank Miller, Sin City: The Hard Goodbye (serialized 1991–92), Dark Horse via Penguin Random House", href: "https://prhcomics.com/book/?isbn=9781506722825" },
    ],
    variants: [
      {
        detail: "Squint at the jacket and the white seat together. The connected black areas organize the page before the face comes into focus.",
        when: "Use solid blacks for a fast sequence or an imposing reveal. Large connected shadows carry more weight than lots of small marks.",
        why: "A large black shape changes how long a panel holds the eye, useful just before a turn or reveal.",
        connection: "Compare the crisp black-and-white outlines reproduced in Tezuka’s official manga archive with the larger connected shadows here.",
        example: 0,
      },
      {
        detail: "Enlarge the panel and compare a dotted area with a clean ink line. One makes gray by spacing marks, the other stays black as it recedes.",
        when: "Use screentone to separate a gray suit from a white seat or to give a recurring location a consistent mood in monochrome.",
        why: "A repeatable pattern can give different scenes a common gray without sacrificing line clarity on a printed page.",
        connection: "Mighty Atom supplies the historical context for serialized monochrome manga. Look at the reproduction scale, then inspect how this study introduces a repeatable middle gray.",
        example: 0,
      },
      {
        detail: "Notice where the lines change direction around the sleeves. That change is a surface cue even if both patches look equally dark.",
        when: "Use crosshatching for close-ups of rumpled cloth or a character under pressure. The direction and density of the marks can add a nervous rhythm.",
        why: "A line can tell readers how fabric turns or pulls, information a flat middle gray would leave implicit.",
        connection: "Compare Tezuka’s economical contours with the additional strokes here. Both come from a monochrome print vocabulary and allocate detail differently.",
        example: 0,
      },
      {
        detail: "Track the lit path from the cheek to the glasses. Much of the suit drops away, leaving a short visual trail.",
        when: "Use noir lighting for secrecy or suspicion. Let just enough of the face catch light for viewers to read the expression.",
        why: "Letting a detail disappear changes how much readers know about a character and can make a harmless setting feel suspicious.",
        connection: "Miller’s Sin City is a later American comics comparison. Its large black fields make noir lighting a feature of the page as well as the setting.",
        example: 1,
      },
    ],
  },
  "watercolor": {
    history: "Water-based color has a long history across many cultures. Transparent watercolor became especially important in European travel sketches and landscape painting in the eighteenth and nineteenth centuries.",
    effect: "Light reflects back through thin color from the paper. Soft edges can make a scene feel fleeting, while deliberately crisp edges tell you where to look.",
    use: "Use it for changing weather, a travel diary, or a quiet memory. Leave the paper showing where you want light to seem to come through.",
    why: "A wash can make changing weather or a passing impression feel fleeting, with a few crisp edges to hold the viewer’s attention.",
    period: "British watercolor tradition, early to mid-nineteenth century",
    examples: [
      { label: "J. M. W. Turner, The Lake of Zug (1843), The Met", href: "https://www.metmuseum.org/art/collection/search/337499" },
      { label: "The Met’s watercolor technique guide, including Turner’s The Lake of Zug (1843)", href: "https://www.metmuseum.org/pt/perspectives/materials-and-techniques-drawing-watercolor" },
    ],
    variants: [
      {
        detail: "Compare how complete the glasses look with how little paint describes the chair. Your eye carries the unfinished edge across the gap.",
        when: "Use loose washes for a fleeting impression, such as someone passing through a station. A few clear marks let viewers supply the rest.",
        why: "Selective omission makes a scene feel recalled or glimpsed. Viewers help complete it instead of inspecting every object equally.",
        connection: "In Turner’s lake, small foreground marks share the page with expanses of light wash. Compare where detail stops carrying the image.",
        example: 0,
      },
      {
        detail: "Along a lapel, follow the boundary between a pale passage and a firmer dark patch. That boundary is what a wash on dry paper can preserve.",
        when: "Use controlled washes for a costume study or an observed location where you want identifiable details and still want the paper to glow.",
        why: "Sharp placement helps communicate material or construction in a study where soft color alone would blur the design.",
        connection: "The Met’s guide shows how layers of washes change color and density as well as how artists recover lights.",
        example: 1,
      },
      {
        detail: "Try viewing the drawing first as an outline and then as a pool of color. The glasses belong to both, so the two systems meet there.",
        when: "Use ink with watercolor for illustrated notes or travel comics. The line holds the drawing together even when a wash crosses its edge.",
        why: "A fixed line lets you change the color or lighting without redrawing the essentials, useful for quick narrative sketches.",
        connection: "The Met documents watercolor combined with other media, including drawn underlayers. Compare their roles with the visibly separate line and wash here.",
        example: 1,
      },
      {
        detail: "Follow the faint edge of the shoulder into the paper. Its soft border makes the firmer features seem nearer.",
        when: "Use wet-on-wet for fog, a dream, or a remembered face. Keep the one feature that matters on drier paper so it stays distinct.",
        why: "Soft edges offer a way to build distance or memory even when there is little perspective in the composition.",
        connection: "Turner’s water and surrounding light show how edges can fade into atmosphere. This portrait applies a similar edge hierarchy to a person.",
        example: 0,
      },
    ],
  },
  "digital": {
    history: "Digital painting developed alongside computer graphics and drawing tablets. Layers, undo, and brushes that respond to pressure expanded what artists could change while working.",
    effect: "Digital painting can look soft, graphic, textured, or photographic. Its signature strength is how readily you can adjust the color, light, and layout independently.",
    use: "Use it for concept art or a comic that needs several lighting passes. Decide how sharp or tactile the image should feel before choosing brushes.",
    why: "Separate layers let you revise the lighting or color while keeping a pose consistent across related illustrations.",
    period: "Desktop image editing and digital illustration, from the 1980s–1990s",
    examples: [
      { label: "Adobe Photoshop, launched in 1990, Computer History Museum", href: "https://www.computerhistory.org/makesoftware/exhibit/photoshop/" },
    ],
    variants: [
      {
        detail: "Compare the blended cheek with the harder edge of the glasses. That small edge change is a stronger focus cue than a new color would be.",
        when: "Use this for a reflective portrait or warm exchange. Smooth modeling slows the eye down and a few sharp features give it a destination.",
        why: "A soft portrait can feel attentive and close while preserving a reliable point of entry for the eye.",
        connection: "The museum traces the rise of desktop image editing. That workflow made it practical to refine broad blends and tiny edges independently.",
        example: 0,
      },
      {
        detail: "Look at patches with similar brightness in the jacket and hair. The scale and direction of the marks are what make the surfaces read differently.",
        when: "Use texture when fabric, glass, and hair have to feel different under the same light. Pick a few marks appropriate to each surface.",
        why: "Different texture scales help a viewer distinguish materials even after a panel is reduced or printed in gray.",
        connection: "The history of desktop image manipulation helps explain how texture, color, and light became separately adjustable elements. These marks simulate physical materials.",
        example: 0,
      },
      {
        detail: "Inspect the narrow change from clear outline to modeled hair. The artist can keep the face graphic and add depth only at the edges that matter.",
        when: "Use it for a recurring comic character who needs a recognizable silhouette with more volume in the illustration close-ups.",
        why: "A clean underlying design survives different lighting passes, a practical choice for repeating a character throughout a series.",
        connection: "The Photoshop timeline gives the production context for mixing sharply defined drawing with locally blended paint in a single file.",
        example: 0,
      },
      {
        detail: "Imagine moving the strongest highlight onto the chair. The scene’s apparent center would shift, even though the pose stayed put.",
        when: "Use cinematic light for an entrance or chapter cover. Let one strong light tell the audience where the event is happening.",
        why: "Separating light from pose lets a storyteller test which moment or emotion an audience reads first.",
        connection: "Desktop image editing made a lighting revision a routine production choice. That is the historical connection here, and makes this a useful production-history example.",
        example: 0,
      },
    ],
  },
  "oil": {
    history: "Artists in Europe used oil-bound pigments long before the fifteenth century. Early Netherlandish painters showed how far slow-drying layers could take rich color and fine detail.",
    effect: "Oil can hold a smoothly blended face, deep transparent shadows, or raised brush marks. Those choices can convey stillness, solidity, or the energy of the painter’s hand.",
    use: "Use this look for a portrait with physical presence, or for a scene where the surface of the paint should be part of the experience.",
    why: "Oil’s workable time gives an artist room to blend gently, keep strokes distinct, or build up a surface the viewer can almost feel.",
    period: "Early Netherlandish oil painting, Baroque lighting, and nineteenth-century brushwork",
    examples: [
      { label: "Jan van Eyck, The Arnolfini Portrait (1434), National Gallery", href: "https://www.nationalgallery.org.uk/paintings/jan-van-eyck-the-arnolfini-portrait" },
      { label: "Vincent van Gogh, Cypresses (1889), The Met", href: "https://www.metmuseum.org/art/collection/search/437980" },
      { label: "Caravaggio, The Supper at Emmaus (1601), National Gallery", href: "https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus" },
    ],
    variants: [
      {
        detail: "Look for the point where a cheek turns from warm light to cooler shadow. The face seems solid before any outline tells you where it ends.",
        when: "Use the classical approach for a portrait meant to feel measured and lasting. Gradual color changes make the sitter feel physically present.",
        why: "Subtle transitions give a quiet portrait time and physical presence. Viewers can linger on the face instead of rushing to the pose.",
        connection: "Van Eyck’s oil technique makes surfaces hold very different kinds of detail under shared light. Compare how material and volume carry authority.",
        example: 0,
      },
      {
        detail: "Trace the direction of a simulated raised mark on the jacket. Several strokes can point your eye along a form.",
        when: "Use impasto for urgency or physical energy. A stroke that looks thick and directional makes the surface part of the story.",
        why: "A visible ridge gives a painted surface its own energy, even if the sitter stays still.",
        connection: "Van Gogh’s thickly marked Cypresses makes brush direction visible at the scale of the entire tree.",
        example: 1,
      },
      {
        detail: "Find the edge of a fold where adjacent colors appear to meet in a single stroke. The change feels like one decision made quickly.",
        when: "Use the direct approach for a lively sitting or a quick impression of someone. The wet strokes retain the energy of the first decisions.",
        why: "A direct, wet-into-wet approach can preserve the urgency of a sitting and make a gesture feel unpolished in a useful way.",
        connection: "Van Gogh offers a comparison for visible direct strokes. Compare the look of the strokes. Alla prima specifically describes a wet-into-wet working process.",
        example: 1,
      },
      {
        detail: "Compare the face with the torso as two separate masses. Light reveals a piece of the gesture and lets the rest remain implied.",
        when: "Use a pronounced light-dark contrast for a revelation or an intimate exchange. Keep the surrounding shadow simple so one lit feature has room to work.",
        why: "Restricting what an audience can see creates anticipation and gives even ordinary gestures an event-like quality.",
        connection: "In Caravaggio’s Baroque supper, strong light makes the participants’ reactions legible at the moment of recognition.",
        example: 2,
      },
    ],
  },
  "gouache": {
    history: "Gouache is opaque water-based paint, sometimes called bodycolor. It has a long history in illustration and became a practical choice for twentieth-century posters and design artwork.",
    effect: "Its matte color covers the surface, so one shape can sit cleanly over another. It can make an image feel direct, carefully arranged, and handmade at the same time.",
    use: "Use it for a book cover, poster, or graphic character study where broad shapes need to read before fine shading.",
    why: "Light shapes can be placed late in the painting. That makes it easier to adjust a graphic silhouette without starting over.",
    period: "Opaque watercolor and twentieth-century design",
    examples: [
      { label: "Henri Matisse, Jazz (1947), The Met", href: "https://www.metmuseum.org/art/collection/search/353770" },
      { label: "The Met’s watercolor technique guide, including nineteenth-century examples of bodycolor", href: "https://www.metmuseum.org/pt/perspectives/materials-and-techniques-drawing-watercolor" },
    ],
    variants: [
      {
        detail: "Look at where the broad dark jacket takes a bite out of the light seat. The boundary itself draws the pose.",
        when: "Use flat blocks for a cover or small graphic. Large unbroken shapes communicate posture and clothing without needing a rendered background.",
        why: "A simple join carries through a small reproduction, which is why the approach can work for a cover or poster.",
        connection: "The plates in Jazz were printed from designs made with gouache-colored cut paper. Compare how equal attention to edges and color makes the shapes carry the action.",
        example: 0,
      },
      {
        detail: "Find two neighboring planes that are close in brightness but opposite in warmth. They can still separate at a glance.",
        when: "Use contrasting warm and cool patches for sunny indoor scenes or when you want to build volume with color as well as shade.",
        why: "Warm and cool shifts supply a second way to describe volume when you want the flatness of a graphic image.",
        connection: "The saturated colors in Jazz show how strongly neighboring areas can register without soft shading. This portrait uses the principle to turn a form.",
        example: 0,
      },
      {
        detail: "Pick one blue and look for its relatives elsewhere in the square. A few recurring mixtures make disconnected shapes feel related.",
        when: "Use a limited palette for a recurring location or a coordinated set of illustrations. Repeated mixtures give separate pictures a family resemblance.",
        why: "A small palette supplies continuity across a sequence and leaves room for one new color to mark a change.",
        connection: "Compare repeated colors across the pages of Jazz. A recurring set of colors can hold different compositions together.",
        example: 0,
      },
      {
        detail: "Inspect the lighter gaps in a broken stroke. The ground interrupts the paint along one edge while the larger block still reads.",
        when: "Use dry brush when a location or garment should feel worn or tactile. Localize the broken marks so the surrounding planes keep their graphic punch.",
        why: "That slight interruption can suggest paper, friction, or age and make an otherwise flat surface feel handled.",
        connection: "The Met’s guide distinguishes opaque bodycolor from transparent wash. The dry mark here gets its broken appearance from incomplete coverage of the ground.",
        example: 1,
      },
    ],
  },
  "pencil": {
    history: "Colored pencils became common in commercial art and classrooms in the twentieth century. Their colored cores let artists draw thin lines and build up broad areas with repeated strokes.",
    effect: "The marks show how the artist moved around a form. A light touch feels tentative or intimate, while densely layered color makes an object feel solid.",
    use: "Use it for a sketchbook, costume study, or close observation where seeing the marks helps the reader share the artist’s attention.",
    why: "You can use mark direction to explain form while leaving separate colors visible in the same shadow.",
    period: "Colored-pencil drawing and twentieth-century architectural presentation",
    examples: [
      { label: "Frank Lloyd Wright, Designs for an American Landscape, 1922–1932, Library of Congress", href: "https://www.loc.gov/exhibits/flw/" },
    ],
    variants: [
      {
        detail: "Follow the marks from the shoulder down the bend of the elbow. The changes in angle tell you where the fabric turns.",
        when: "Use hatching that follows form for a hair or garment study. The visible motion of the pencil can clarify how something bends.",
        why: "Directional marks give readers information about shape even in parts of the drawing with little contrast.",
        connection: "Compare the way directional drawn marks organize Wright’s architectural renderings with the way this study organizes cloth.",
        example: 0,
      },
      {
        detail: "Zoom into the suit where the strokes meet at an angle. Several light layers can build a rich dark and leave traces of both colors.",
        when: "Use crossing marks for deep shadows in a close-up. Slowly accumulating two colors makes dark material feel layered.",
        why: "A dark area still gives the reader something to discover up close. That helps dense clothing feel like material rather than a blank silhouette.",
        connection: "The architectural drawings give historical context for building a presentation with layers of drawn color. The crossing strokes here are a specific way to accumulate depth.",
        example: 0,
      },
      {
        detail: "Compare a smoother patch with the surrounding visible paper. Pressure changes the finish even where the hue stays similar.",
        when: "Use burnishing when an object should feel glossy or deliberate. Dense color can make a focal patch stand out against rougher paper grain.",
        why: "A polished area can create focus or suggest a different surface without introducing another color.",
        connection: "Wright’s presentations show that drawn color can range from a light suggestion to a finished surface. Here, pressure changes the apparent polish of one area.",
        example: 0,
      },
      {
        detail: "Notice how few marks it takes to locate a light patch beside the glasses. The bare paper does some of the drawing.",
        when: "Use open paper for a sketch, a quiet portrait, or a suggestion of strong light. A few concentrated marks give the viewer enough to finish the image mentally.",
        why: "Leaving space feels tentative, fast, or intimate and lets a viewer notice the artist’s choices one by one.",
        connection: "Compare the economical areas around architectural details in Wright’s drawings. Bare ground can be part of a reading order, even when the subject is different.",
        example: 0,
      },
    ],
  },
  "woodblock": {
    history: "Woodblock printing has a long history across East Asia and Europe. A carved block prints from the raised surface, and multicolor prints can use separate blocks aligned on the page.",
    effect: "Carved edges and broad ink shapes give the image a clear silhouette. Repeated cuts can feel rhythmic, while small irregularities suggest a print made by hand.",
    use: "Use this look for a strong emblem, a limited-palette illustration, or an image where silhouettes matter more than smooth modeling.",
    why: "Planning the dark and light shapes before cutting gives the print a silhouette that stays legible across repeated impressions.",
    period: "East Asian relief printing and Edo-period color woodcuts",
    examples: [
      { label: "Utagawa Hiroshige, Sudden Shower at Shōno (1834–35), The Met", href: "https://www.metmuseum.org/art/collection/search/36521" },
    ],
    variants: [
      {
        detail: "Notice how the dark boundary makes broad pools of hair and clothing function as separate pieces of the print.",
        when: "Use several flat inks for a character print where each color has a clear role. The outline helps the figure survive small alignment shifts.",
        why: "A key outline keeps a portrait legible after color has been simplified or slightly shifted in printing.",
        connection: "Hiroshige’s print makes a dramatic scene from clearly organized shapes and ink. Compare that economy with the simulated key line here.",
        example: 0,
      },
      {
        detail: "See where the cream paper meets both inks. The same empty patch reads as highlights in one place and a gap between objects in another.",
        when: "Use two inks for a compact poster or motif with an economical feel. The paper gives the two colors space and acts as the lightest tone.",
        why: "Using the sheet as a third value makes a small palette feel broader and gives a printed page air.",
        connection: "Hiroshige’s print is a multicolor comparison. Isolate its light paper or pale ground to see how a surface can support several ink shapes.",
        example: 0,
      },
      {
        detail: "At the join between the suit and seat, a small pale shape marks an opening. That cut keeps two dark forms from merging.",
        when: "Use interlocking shapes for bold silhouettes or visual puzzles. Place a few cut-looking highlights where a dark object would otherwise disappear.",
        why: "Leaving a deliberate gap can clarify a pose even when smooth shading is unavailable.",
        connection: "In Hiroshige’s relief print, clear separations between figures and scenery let the rain cross both without consuming the silhouettes.",
        example: 0,
      },
      {
        detail: "Find where the pale background appears to deepen in color. The outline in front stays firm while the distance recedes.",
        when: "Use a gradation for a misty backdrop or a calm shift in time of day. Set it behind firm edges so the print retains its graphic structure.",
        why: "A graded area can establish weather or depth without making a crisp figure feel soft.",
        connection: "Hiroshige used gradation in his landscapes. The treatment in this digital study recalls bokashi, a way to produce graded color in a print.",
        example: 0,
      },
    ],
  },
  "charcoal": {
    history: "Charcoal is one of the oldest drawing materials. Artists have used it for both preparatory studies and finished drawings because the powder can be smudged, lifted, or laid down in deep blacks.",
    effect: "A stick can make a fast, fragile line or a dense shadow. That range gives a portrait an immediate quality, as though you can see the decisions being made.",
    use: "Use it to study lighting and pose, or for a finished scene that should feel raw, atmospheric, or tactile.",
    why: "Broad marks let you test the basic light and dark arrangement quickly while the drawing is easy to revise.",
    period: "European drawing practice and nineteenth-century tonal studies",
    examples: [
      { label: "The Met’s charcoal guide, including Odilon Redon’s Armor (1891)", href: "https://www.metmuseum.org/pt/perspectives/materials-and-techniques-drawing-charcoal" },
      { label: "Georges Seurat’s 1880s Conté crayon drawings, MoMA exhibition checklist", href: "https://www.moma.org/interactives/exhibitions/2007/seurat/checklist.pdf" },
    ],
    variants: [
      {
        detail: "Look for a change in line pressure at a joint. A darker short mark can show where the pose carries weight.",
        when: "Use this to capture a stance or work out whether a pose reads before committing to shading. A light exploratory line can also feel spontaneous in finished art.",
        why: "A small number of decisive marks makes the viewer sense a gesture before the figure has been finished.",
        connection: "The Met shows how a charcoal stick can make a fine line or a broad passage depending on how it touches the sheet.",
        example: 0,
      },
      {
        detail: "Forget the fingers for a moment and read the light, middle, and dark masses. See which of those masses makes the head stand out.",
        when: "Use three values for a storyboard or to check the lighting in a busy scene. The arrangement should still read when the details disappear.",
        why: "A three-value test reveals whether a composition will survive a small panel or difficult reproduction.",
        connection: "Seurat’s 1880s Conté crayon drawings are a tonal parallel, made in a different dry medium. Their broad masses establish form before detail.",
        example: 1,
      },
      {
        detail: "Compare the slow fade of a cheek with the sharp edge at the glasses. The two speeds of transition determine what comes forward.",
        when: "Use blended charcoal for a quiet portrait or soft light. Preserve a few crisp accents around the eyes or glasses so the figure still feels present.",
        why: "Soft transitions can feel private or atmospheric. The hard accent keeps that atmosphere from erasing the subject.",
        connection: "Look at how Seurat’s dark drawings allow edges to appear and disappear through tone. Conté crayon is a comparison for edge control, distinct from charcoal.",
        example: 1,
      },
      {
        detail: "The dark and light marks meet on a paper that already has a middle brightness. Look for places where the paper makes the form by itself.",
        when: "Use a toned ground for a lamplit scene. Starting in the middle lets a few light marks feel as deliberate as the shadows.",
        why: "A toned sheet makes it possible to build the image out from the center and let both a black and a white mark feel equally deliberate.",
        connection: "The Met’s technique examples show artists using paper tone and white heightening alongside charcoal.",
        example: 0,
      },
    ],
  },
  "collage": {
    history: "People have assembled pictures from paper for centuries. In the 1910s, artists including Georges Braque and Pablo Picasso made pasted paper part of modern painting.",
    effect: "A fragment brings its own texture and associations. Put it next to an unexpected piece and the join can feel playful, handmade, or unsettling.",
    use: "Use collage when a story is assembled from scraps of evidence, memories, or found objects, or when bold cut shapes should lead the eye.",
    why: "Paper edges give you a fast way to test what belongs together and which pieces of a scene deserve emphasis.",
    period: "Cubist pasted paper, modernist cut-outs, and twentieth-century photomontage",
    examples: [
      { label: "Picasso: Guitars, 1912–1914, MoMA", href: "https://www.moma.org/calendar/exhibitions/1088" },
      { label: "Romare Bearden, The Block (1971), The Met", href: "https://www.metmuseum.org/art/collection/search/481891" },
      { label: "Henri Matisse, Jazz (1947), The Met", href: "https://www.metmuseum.org/art/collection/search/353770" },
    ],
    variants: [
      {
        detail: "Track a straight cut across the lapel and notice when it starts reading as part of the seat. Shared edges make pieces fit tightly.",
        when: "Use clean cuts for an editorial illustration or a notice that needs a quick silhouette. Precise joins make the composition feel intentional.",
        why: "A clean cut turns an everyday pose into an image people can understand quickly, even if they never notice the individual pieces.",
        connection: "Picasso’s Cubist constructions and pasted pieces show how an assembled edge can stand for a contour or an object.",
        example: 0,
      },
      {
        detail: "Zoom into the boundary of a paper layer. An irregular edge can be carrying a shadow and a hint of fiber at the same time.",
        when: "Use torn edges for a memory, handmade letter, or something unsettled. Uneven fibers give the same shapes a softer emotional edge.",
        why: "An imperfect seam can suggest a memory made from fragments or a letter handled by someone.",
        connection: "Bearden combines paper and printed materials in The Block. Study how the joins remain visible and help suggest a neighborhood full of different surfaces.",
        example: 1,
      },
      {
        detail: "Look where one texture begins to cover another. The overlap tells you which surface is near before you interpret the objects.",
        when: "Use layered textures when accumulated objects or traces of making matter. Each surface helps the viewer read what is in front of what.",
        why: "Physical-looking layers can make two parts of a story feel accumulated at different times or drawn from different places.",
        connection: "In The Block, patterns, printed images, and drawn passages give the neighborhood several kinds of surface at once.",
        example: 1,
      },
      {
        detail: "Cover the smallest details and look at the opening around the raised arm. The gap can carry as much pose information as the cut piece.",
        when: "Use two colors for a tiny illustration, sign, or silhouette-based gag. The negative spaces around hands and props do much of the storytelling.",
        why: "A two-color treatment leaves very little to compete with a gesture or a small visual joke.",
        connection: "Matisse’s Jazz uses spare, sharply recognizable silhouettes within brighter palettes. Isolate one cut shape to see the economy this variant takes further.",
        example: 2,
      },
    ],
  },
  "pastel": {
    history: "Dry pastel sticks hold pigment with little binder. They became popular for eighteenth-century portraits and later let artists such as Edgar Degas combine drawing and painting in the same work.",
    effect: "Pastel can leave velvety color, dusty transitions, or sharp little marks. Its surface often makes light feel close and touchable.",
    use: "Use it for a quiet portrait or a light study where small changes in warmth and edge matter more than a clean outline.",
    why: "Visible touches keep the image lively up close, while softer areas can suggest distance or give an expressive detail more attention.",
    period: "Eighteenth-century pastel portraiture and nineteenth-century French modernism",
    examples: [
      { label: "The Met’s pastel guide, including Maurice Quentin de La Tour’s Louis XV portrait study (ca. 1745)", href: "https://www.metmuseum.org/ko/perspectives/materials-and-techniques-drawing-pastel" },
      { label: "Edgar Degas, Dancer (1880–85), The Met", href: "https://www.metmuseum.org/art/collection/search/438518" },
    ],
    variants: [
      {
        detail: "Look for the longest transition in the cheek and the shorter one beside the glasses. Softness has a direction, set by the round form.",
        when: "Use gentle blends for an intimate portrait or hazy afternoon. Leave a harder edge where the viewer should stop and look.",
        why: "A quiet transition asks the viewer to spend longer looking and can make a portrait feel intimate.",
        connection: "The Met’s pastel guide connects the soft pigment and subtle shading to the historical popularity of pastel portraits.",
        example: 0,
      },
      {
        detail: "Find individual touches that are warmer or cooler than the patch they create when you step back.",
        when: "Use broken color for changing daylight or moving fabric. Individual marks make a surface feel alive as the colors merge from farther away.",
        why: "Keeping colors separate lets a surface appear to flicker, useful for a turn of the body or shifting light.",
        connection: "Compare the persistent marks in Degas’s Dancer. Pastel strokes can remain visible while still contributing to a unified figure.",
        example: 1,
      },
      {
        detail: "Look for the shade of the sheet reappearing between lighter and darker areas of the figure. It quietly links them.",
        when: "Use a toned ground for scenes that should feel unified by the surrounding air. Leave bits showing so highlights and darks seem to belong in the same light.",
        why: "A common ground can make separately marked objects feel surrounded by the same light.",
        connection: "The Met’s historical examples show the interaction of colored ground and dry pigment. Look at the support as part of the palette.",
        example: 0,
      },
      {
        detail: "Read the image at thumbnail size, then look for the few places where a narrow edge holds up close. Those details set the focus in a soft field.",
        when: "Use sharp accents when the scene should feel soft but one expression or prop has to read first. Keep those accents scarce.",
        why: "Saving hard accents allows a single glance, hinge, or prop to anchor a scene with diffuse light.",
        connection: "Degas’s pastel lets distinct strokes coexist with much softer surrounding marks. The contrast makes sharp accents do more work.",
        example: 1,
      },
    ],
  },
  "pixel": {
    history: "Early video games and home computers had tight limits on resolution and colors. Artists turned those limits into a language that is still used by choice in contemporary games.",
    effect: "Each visible square does work. A handful of pixels can imply an eye or a hand, creating an economical look that can feel playful, nostalgic, or sharply modern.",
    use: "Use it for sprites, icons, or a game-like comic. Check the image at its intended size because a tiny adjustment can change the whole gesture.",
    why: "A readable pose at small scale gives the viewer a visual anchor while a game screen or comic panel gets busier.",
    period: "Arcade and graphical interface design, late 1970s–1980s",
    examples: [
      { label: "Susan Kare, Graphic icon sketch (1982–83), MoMA", href: "https://www.moma.org/collection/works/188393" },
      { label: "Toru Iwatani, Pac-Man (1980), MoMA", href: "https://www.moma.org/collection/works/164917" },
    ],
    variants: [
      {
        detail: "Toggle between the white gaps at the hand and glasses. At this scale, a missing pixel can tell you which direction something points.",
        when: "Use one-bit for a very small sprite, a dramatic silhouette, or a deliberately spare display. Check that the important gaps survive at the intended size.",
        why: "A sturdy silhouette can stay readable on a tiny display or during motion.",
        connection: "Kare plotted early Macintosh icons on a grid. Her sketches show how a recognizable object can survive in very few squares.",
        example: 0,
      },
      {
        detail: "Count how many different roles the dark blue plays. Its job changes depending on what touches it.",
        when: "Use a four-color palette when an image needs a readable face and enough room for a distinct background. Reuse colors so the whole sprite belongs together.",
        why: "Palette reuse lets a small picture carry face, clothing, and setting while remaining legible.",
        connection: "Pac-Man gives individual colors strong roles in a simple environment. This portrait uses a tighter palette to keep character and background distinguishable.",
        example: 1,
      },
      {
        detail: "Find a checker-like half tone in the shadow and compare it with the same colors in unbroken areas. Spacing creates an apparent third value.",
        when: "Use dithering for a curved surface or faded light when you cannot add another color. Keep the pattern away from critical outlines if it competes with the silhouette.",
        why: "A pattern supplies depth when you cannot introduce another shade, as long as the image is viewed at the right scale.",
        connection: "Kare’s graph-paper archive shows the grid as a decision-making tool. Dithering addresses a related problem on limited displays by alternating the color of neighboring pixels.",
        example: 0,
      },
      {
        detail: "At small size, see whether you can recognize the raised hand before the buttons or eyes. The largest clusters do most of the work.",
        when: "Use the arcade approach for a game-like action panel or sprite selection. Bold clusters make characters identifiable before the reader sees details.",
        why: "Clear clusters make a moving figure quickly distinguishable from the field around it.",
        connection: "Pac-Man’s instantly readable characters offer a working arcade example of identity conveyed by very few forms.",
        example: 1,
      },
    ],
  },
  "art-nouveau": {
    history: "Around 1890–1910, artists in Europe and elsewhere applied Art Nouveau to posters, furniture, architecture, and everyday objects. They sought a design language suited to modern life.",
    effect: "Long curves often seem to grow from plants, hair, or fabric into the frame. The line links the subject and decoration into one flowing design.",
    use: "Use it for a decorative portrait or invitation when you want elegance and a slow, continuous path for the eye.",
    why: "A continuous curve can guide attention through a poster, linking an ordinary gesture to the design around it.",
    period: "Art Nouveau and the Paris illustrated poster, 1890s–1900s",
    examples: [
      { label: "Alphonse Mucha, Gismonda poster (1894), Mucha Foundation timeline", href: "https://muchafoundation.org/en/timeline/alphonse-mucha-timeline" },
      { label: "Alphonse Mucha, Job (ca. 1897–98), LACMA", href: "https://collections.lacma.org/object/57059" },
    ],
    variants: [
      {
        detail: "Compare the curve above the head with the curve at the shoulder. They turn the portrait and its frame into a single design.",
        when: "Use a botanical arch for a formal introduction or bookplate. It makes the person feel as though she belongs to the setting’s decorative pattern.",
        why: "An arch can make someone feel formally presented while still belonging to a living, growing environment.",
        connection: "The tall format and overhead ornament in Gismonda frame an actress as part of the poster’s decoration.",
        example: 0,
      },
      {
        detail: "Trace the blue strap from the neck toward the desk. It moves attention between two areas that would otherwise sit apart.",
        when: "Use an S-shaped ribbon at a desk when a work gesture should feel graceful. Carry the eye from her hand to the rest of the scene with the lanyard.",
        why: "A curved accessory can direct readers through an ordinary task without adding arrows or explanatory text.",
        connection: "In Job, Mucha uses long lines in the hair and smoke to move the eye through an advertisement. The lanyard performs a comparable job here.",
        example: 1,
      },
      {
        detail: "Notice the curved border and the repeated fan-like leaf shapes. They contain the gesture without making the square feel static.",
        when: "Use a medallion for a cover emblem or repeated chapter ornament. Its compact circle turns one small gesture into a memorable sign.",
        why: "A circular boundary isolates one useful gesture for a bookplate, emblem, or repeating chapter marker.",
        connection: "Gismonda uses a decorated round form behind the head. The study brings that framing principle into a much tighter portrait.",
        example: 0,
      },
      {
        detail: "The sitter turns out of the picture while the stems sweep back across it. Look at where those movements meet.",
        when: "Use the reverse portrait for a farewell or an invitation to follow. Flowers and shoulders turning together make the viewer feel motion beyond the frame.",
        why: "Opposing curves suggest a departure or invitation without giving the composition a lopsided weight.",
        connection: "Job ties the tilt of the head to its restless curving lines. The over-the-shoulder study changes the pose but uses a similar exchange with the surrounding ornament.",
        example: 1,
      },
    ],
  },
  "art-deco": {
    history: "Art Deco took shape in the 1910s and 1920s. A major Paris exhibition in 1925 helped bring related approaches to luxury objects, interiors, and buildings to international attention.",
    effect: "Stepped forms, symmetry, and polished surfaces turn the shapes of the machine age into glamour. The result can convey confidence, authority, and spectacle.",
    use: "Use it for a grand entrance, a formal invitation, or a character poster that should feel sophisticated and commanding.",
    why: "Stylized geometry can make a poster feel polished and monumental while keeping even a cropped figure recognizable.",
    period: "International Art Deco in 1920s–1930s design and architecture",
    examples: [
      { label: "William Van Alen’s Chrysler Building (1930), NYC Landmarks Preservation Commission", href: "https://s-media.nyc.gov/agencies/lpc/lp/0992.pdf" },
      { label: "Émile-Jacques Ruhlmann and Art Deco Paris, including the 1925 exposition, The Met", href: "https://www.metmuseum.org/de/press-releases/ruhlmann-genius-of-art-decoart-deco-paris-2003-exhibitions" },
    ],
    variants: [
      {
        detail: "The rays and stepped buildings rise from behind the figure, letting the skyline act like part of her silhouette.",
        when: "Use the upright sunburst for an announcement or a character’s first entrance. The skyline makes her feel as ambitious as the city.",
        why: "Joining the character to a big vertical form borrows some of the city’s scale and ambition for an entrance.",
        connection: "The Chrysler Building’s stepped crown and fan-like forms are a built example of the Art Deco shapes echoed here.",
        example: 0,
      },
      {
        detail: "Compare the angle of the bands with the straight line of her glasses. The face stays stable while the surrounding pattern feels fast.",
        when: "Use strong diagonals for a quick departure or a fashion-like profile. Their direction adds momentum even when the person stands still.",
        why: "One stable identifier lets you push a layout toward speed and excitement without losing the subject.",
        connection: "The Chrysler crown repeats curved sections and triangular details. This study uses a more directional arrangement to turn comparable geometry into movement.",
        example: 0,
      },
      {
        detail: "Read the side panels before the center. Their regular spacing makes the seat at the middle seem reserved for someone important.",
        when: "Use symmetry for a meeting where ritual or power matters. Repeating architecture makes the central seat feel like a position of authority.",
        why: "Symmetry can communicate authority through the room itself, leaving the sitter free to make a small gesture.",
        connection: "Ruhlmann’s 1925 exposition designs treated furniture and fittings as parts of a coordinated interior. This variant uses that coordination to stage hierarchy.",
        example: 1,
      },
      {
        detail: "The face is cropped tightly against an angled border. Only a few lines need to bridge the gap between a person and an emblem.",
        when: "Use a geometric close-up for a cover or badge that needs to read at a glance. A few plain face planes and recognizable glasses carry the identity.",
        why: "A concentrated frame keeps a close-up readable on a small cover or invitation while retaining a polished formality.",
        connection: "The Met’s Ruhlmann exhibition places precise geometric furniture and luxurious finish in the same Art Deco tradition. This study applies that precision to a graphic portrait.",
        example: 1,
      },
    ],
  },
  "cubism": {
    history: "Pablo Picasso and Georges Braque developed Cubism in the years before World War I. They broke familiar subjects into overlapping flat shapes and experimented with pasted paper.",
    effect: "A face or table can show several views in the same picture. The viewer has to reconstruct the subject, which can suggest complexity or competing perspectives.",
    use: "Use it for a character with several sides, a puzzle about perception, or an environment where figure and furniture should feel built from the same forms.",
    why: "Several viewpoints let a still image show what you normally discover by looking at an object from different angles.",
    period: "Analytic and Synthetic Cubism, Paris, ca. 1907–1914",
    examples: [
      { label: "Pablo Picasso, Ma Jolie (winter 1911–12), MoMA", href: "https://www.moma.org/collection/works/79051" },
      { label: "Picasso: Guitars, 1912–1914, MoMA", href: "https://www.moma.org/calendar/exhibitions/1088" },
    ],
    variants: [
      {
        detail: "Try following the nose from one angle and the cheek from another. The two routes need not agree to suggest the same person.",
        when: "Use overlapping views to present competing sides to a character or an ambiguous encounter. Both faces can be present in the same moment.",
        why: "Simultaneous viewpoints let you show ambiguity without assigning each interpretation a separate panel.",
        connection: "Ma Jolie asks viewers to reconstruct a figure and instrument from intersecting clues. The study makes the competing views of a face more explicit.",
        example: 0,
      },
      {
        detail: "Pick one corner of the eyeglass frame and trace it across the adjacent planes. The object keeps its identity while the surrounding space changes.",
        when: "Use a cue across the fragments when you want viewers to reconstruct an image without losing the subject. The glasses act as a guide through the separate surfaces.",
        why: "One recurring signal gives readers permission to explore a complex image without losing their bearings.",
        connection: "The letters and recognizable fragments in Ma Jolie offer footholds among the angular forms. The glasses play that anchoring role here.",
        example: 0,
      },
      {
        detail: "Notice how a flat piece of color can be read as part of a shoulder in one direction and an independent shape in another.",
        when: "Use the cut-paper approach to turn a person into a handful of recognizable signals. It suits a graphic about identity and how little it takes to suggest it.",
        why: "A few broad pieces can turn recognition into a participatory act without requiring a complicated or crowded image.",
        connection: "Picasso’s paper and cardboard guitar projects show how a few assembled surfaces can evoke a recognizable object.",
        example: 1,
      },
      {
        detail: "Switch your attention from the face to the desk. Each appears to offer a different view of the same compressed space.",
        when: "Use several views of a desk when you want person and environment to feel inseparable. The viewer assembles the room and the figure together.",
        why: "Adjusting the viewpoint for each object can tell a story about how closely a person and their work fit together.",
        connection: "Ma Jolie combines fragments of a figure and instrument in a field of shared planes. Here that relationship is translated into office furniture.",
        example: 0,
      },
    ],
  },
  "pop-art": {
    history: "Pop Art emerged in Britain in the 1950s and took distinct forms in the United States in the 1960s. Artists borrowed from advertising, comics, packaging, and celebrity photography.",
    effect: "Enlarging or repeating something familiar makes it newly visible. Bright colors can feel celebratory while the repetition raises questions about how mass media sells images to us.",
    use: "Use it for satire about brands, products, or public image, or for a bold graphic that should register immediately.",
    why: "Taking a familiar sign out of ordinary scale can make a viewer think about why commercial images are so memorable.",
    period: "British and American Pop Art, 1950s–1960s",
    examples: [
      { label: "Roy Lichtenstein, Drowning Girl (1963), MoMA", href: "https://www.moma.org/collection/works/80249" },
      { label: "Andy Warhol, Campbell’s Soup Cans (1962), MoMA", href: "https://www.moma.org/collection/works/79809" },
    ],
    variants: [
      {
        detail: "The close crop gives the eyes and mouth the scale ordinarily reserved for a headline. Test how much expression survives if you ignore the background.",
        when: "Use the comic close-up to give a small reaction the force of a headline. The crop and bright colors make it read immediately.",
        why: "Enlargement gives a routine response a public, almost promotional intensity.",
        connection: "Lichtenstein enlarged and reworked comic-book imagery in Drowning Girl. Look at how much dramatic weight the cropped expression carries.",
        example: 0,
      },
      {
        detail: "Scan from one repeated portrait to the next and watch where color changes the apparent mood even though the pose repeats.",
        when: "Use repetition to question how a familiar portrait becomes a brand image. Small color shifts also make a strong rhythm across a series.",
        why: "Repeating the image gives a viewer a chance to notice how design can manufacture different impressions of the same person.",
        connection: "Warhol’s 32 soup-can canvases make small changes stand out through a repeating commercial format.",
        example: 1,
      },
      {
        detail: "The badge is treated as large enough to compete with the sitter. Follow the layout from the prop back to the person who uses it.",
        when: "Enlarge a badge to make status, access, or work identity the subject of the joke. Its size gives an ordinary object surprising authority.",
        why: "Changing scale turns a tiny symbol of rank into a visible joke about institutional power.",
        connection: "Warhol shifted a common product label into the scale and context of paintings. This study gives an office object similarly disproportionate attention.",
        example: 1,
      },
      {
        detail: "Pick out the glasses, mug, and computer before the portrait. The whole set feels readable even if the objects are viewed out of order.",
        when: "Use a handful of enlarged props for a character introduction or visual glossary. Their repetition makes everyday office objects feel like brand icons.",
        why: "A set of familiar props can carry identity like a brand, which is useful when you want to make branding itself the joke.",
        connection: "Warhol’s soup-can paintings show how recognizable packaging can become a picture’s principal subject.",
        example: 1,
      },
    ],
  },
  "impressionism": {
    history: "In the 1870s, French artists including Claude Monet and Berthe Morisot exhibited outside the official Salon. They painted modern life and the way light changes across a scene.",
    effect: "Separate touches of color make a surface feel alive. A scene can feel like a particular moment you caught just before the weather or light changed.",
    use: "Use it when a time of day, a season, or the air of a place tells more of the story than the details of its furniture.",
    why: "Making light part of the subject helps a reader feel the time of day or weather before the story states it.",
    period: "French Impressionist exhibitions and modern life, 1870s–1880s",
    examples: [
      { label: "Claude Monet, Woman with a Parasol (1875), National Gallery of Art", href: "https://www.nga.gov/artworks/61379-woman-parasol-madame-monet-and-her-son" },
      { label: "Gustave Caillebotte, Paris Street; Rainy Day (1877), Art Institute of Chicago", href: "https://publications.artic.edu/caillebotte/reader/paintingsanddrawings/section/574/p-42" },
    ],
    variants: [
      {
        detail: "Look for patches that appear both on the plants and the blazer. The changing light makes them feel as if they occupy the same moment.",
        when: "Use mottled sunlight for a passing outdoor moment. Color patches link the person to the shifting light around her.",
        why: "Shared flecks of color connect people to the weather and turn the setting into part of the experience.",
        connection: "Monet lets blue sky, wind, and sunlight affect the dress and landscape alike. Compare the way the paint carries atmosphere across both.",
        example: 0,
      },
      {
        detail: "Read the wet street upward from the near reflections to the storefronts. Light joins places separated by distance.",
        when: "Use rainy blue hour for a city that should feel alive and a little distant. Reflections join nearby puddles and faraway shopfronts in the same mood.",
        why: "Moving reflections lead the eye through a figure scene with less need for rigid outlines or explanatory detail.",
        connection: "Caillebotte’s rainy Paris street makes wet pavement and umbrellas essential to how modern life feels. Compare his more taut construction with this looser treatment.",
        example: 1,
      },
      {
        detail: "Notice one warm lit mark on the face beside a cool one just across its edge. You can locate the off-frame window from that relationship.",
        when: "Use window light for private routines. The temperature change across a face says more about the hour and the room than a detailed backdrop would.",
        why: "Small color shifts supply a sense of hour and place without pulling attention from an ordinary private gesture.",
        connection: "In Monet’s outdoor portrait, cool notes in a light dress help locate the daylight around the person. This is an indoor application of that observational approach.",
        example: 0,
      },
      {
        detail: "Compare the outline of the near figure with the much less distinct skyline. Reduced contrast lets the horizon feel far off.",
        when: "Use a pale skyline at dawn to give a character space to pause. Softer forms make the distance and the early light feel connected.",
        why: "A soft distance gives the audience time to settle into a quiet opening or pause between events.",
        connection: "Monet’s plein-air portrait balances near forms against a sky with very different edges. This study uses the contrast to stretch the apparent distance to the city.",
        example: 0,
      },
    ],
  },
  "fauvism": {
    history: "Henri Matisse, André Derain, and others drew attention in Paris in 1905 for their bold use of color. A critic’s nickname for them, wild beasts, gave the movement its name.",
    effect: "Color follows the needs of the picture. An orange room or green face can convey warmth, excitement, or unease through the way colors react to one another.",
    use: "Use it when a mood should be unmistakable from across the room. Keep a few clear light and dark shapes so the color still has structure.",
    why: "Strong color relationships can quickly set an emotional temperature and separate shapes without elaborate shading.",
    period: "Fauvism and the 1905 Salon d’Automne",
    examples: [
      { label: "Henri Matisse, Woman with a Hat (1905), SFMOMA", href: "https://www.sfmoma.org/artwork/91.161/" },
    ],
    variants: [
      {
        detail: "Look at how the green and pink relate around the nose and across the background. Their boundaries carry the expression more than believable flesh color does.",
        when: "Use the green and pink face for an expression that needs to feel immediate. Let the effect of the color relationship guide the choice of hues.",
        why: "Unexpected hues let the audience feel intensity without making the pose theatrically exaggerated.",
        connection: "Matisse builds a recognizable face out of surprising colors in Woman with a Hat. Compare how small dark accents hold it together.",
        example: 0,
      },
      {
        detail: "Count where orange takes over the room and where a patch of violet pushes back. The interior feels active even without detail.",
        when: "Use a dominant orange room when an environment’s energy should reach viewers first. A cool figure still gives them a stable place to look.",
        why: "One dominant color can make a setting speak first, while a smaller contrasting shape keeps the person legible.",
        connection: "Woman with a Hat uses large color contrasts as a structure. Here the principle expands from the head to an entire office.",
        example: 0,
      },
      {
        detail: "The cobalt figure reads as one weight against the brighter surroundings. Notice where a single edge makes the stance visible.",
        when: "Use a cobalt mass for strong stance or confidence. The outline remains easy to read while the background color gives it force.",
        why: "A large color silhouette gives a controlled or confident pose more immediate force than modeled fabric would.",
        connection: "Look at the dark, legible notes that anchor Matisse’s painted sitter. This study pushes that anchoring role into a single broad silhouette.",
        example: 0,
      },
      {
        detail: "Watch the yellow leak into areas away from the window. It creates a conversation with violet across the inside and outside.",
        when: "Use violet and yellow for a charged transition between inside and outside. Carry a little of each color across the boundary to connect the two areas.",
        why: "Repeating a pair of strong hues connects parts of a complicated scene while leaving each with a different emotional charge.",
        connection: "Matisse’s adjacent patches use color relationships to unify a face and setting. The window study applies that approach across an architectural boundary.",
        example: 0,
      },
    ],
  },
  "expressionism": {
    history: "Expressionist approaches flourished in early twentieth-century Europe, including in German groups such as Die Brücke and Der Blaue Reiter. The artists used distortion in different ways to express felt experience.",
    effect: "Jagged edges, compressed spaces, and strained colors can make the whole room seem to share the character’s emotion.",
    use: "Use it when anxiety, alienation, defiance, or exhaustion should reach viewers before they have time to read the expression.",
    why: "Distorting a recognizable setting can make pressure or isolation feel present even before the reader sees a face.",
    period: "Early twentieth-century German Expressionism and Die Brücke",
    examples: [
      { label: "Ernst Ludwig Kirchner, Street, Dresden (1908, reworked 1919), MoMA", href: "https://www.moma.org/collection/works/78426" },
    ],
    variants: [
      {
        detail: "Follow the leaning sides of the desk and walls toward the sitter. Directions that normally feel stable start to squeeze the scene.",
        when: "Use inward-leaning lines when pressure should feel as if it comes from the whole room. Crowding a desk can make a mundane deadline feel physical.",
        why: "Distorting the room can express stress even if the character is trying to look composed.",
        connection: "Kirchner uses a crowded arrangement and forceful color to make a city street feel psychologically charged.",
        example: 0,
      },
      {
        detail: "Look at the gap between the person and the edges of the corridor. The extremity of the space makes her feel more isolated than her expression alone.",
        when: "Use the stretched empty hall for isolation. Giving the corridor most of the picture makes an ordinary walk feel lonely.",
        why: "An exaggerated distance can turn ordinary work architecture into an emotional experience.",
        connection: "Kirchner’s Street, Dresden produces unease through crowded space. This variant compares the opposite spatial strategy, making emptiness feel just as active.",
        example: 0,
      },
      {
        detail: "Notice how the upright pose meets the strongest slant around her. The strokes seem to reinforce the stance.",
        when: "Use a low viewpoint and strong slants in a moment of refusal. The stance feels firm while the marks around it carry the argument.",
        why: "A forceful environment makes refusal feel like an action even when the body is nearly still.",
        connection: "In Kirchner’s painting, angular figures share the thrust of the surrounding marks. This study assigns that tension to one body holding its ground.",
        example: 0,
      },
      {
        detail: "Follow the unsteady line of the shoulders into the surrounding green and blue. The rest of the room seems to slump with the figure.",
        when: "Use an awkward crop for the end of a long shift. The bent body and uneven brushwork let the setting share the fatigue.",
        why: "Letting the room share fatigue makes it possible to show burnout with subtle acting.",
        connection: "Kirchner’s charged palette shows how color can make ordinary public space feel subjective. The quieter, bent version here tunes that principle toward exhaustion.",
        example: 0,
      },
    ],
  },
  "surrealism": {
    history: "Surrealism took shape in the 1920s around writers and artists exploring dreams, chance, and the unconscious. It grew into an international movement.",
    effect: "Careful rendering can make impossible events feel momentarily believable. Familiar objects in strange relationships can produce comedy, unease, or a sense of discovery.",
    use: "Use it to make readers experience a dream or an absurd rule. Anchor the impossible event in enough ordinary detail for the contradiction to register.",
    why: "Familiar objects give the reader a starting point for imagining a dream, contradiction, or impossible workplace rule.",
    period: "Interwar European Surrealism, 1920s–1930s",
    examples: [
      { label: "Salvador Dalí, The Persistence of Memory (1931), MoMA", href: "https://www.moma.org/momaorg/shared/flattened_pages/moma_learning/salvador-dali-the-persistence-of-memory-1931/" },
      { label: "René Magritte, The False Mirror (1929), MoMA", href: "https://www.moma.org/collection/works/78938" },
    ],
    variants: [
      {
        detail: "Read the desk as solid office furniture before looking for what supports it. The delay is what makes the floating object unsettling.",
        when: "Use the flooded office for a metaphor about being overwhelmed. Ordinary furniture makes the impossible water feel unexpectedly familiar.",
        why: "An impossible event feels more surprising when surrounding details encourage the audience to trust the scene first.",
        connection: "Dalí places objects with impossible behavior in a carefully modeled landscape. The desk applies the same kind of tension to office furniture.",
        example: 0,
      },
      {
        detail: "Compare the daylight in one lens with the other. A familiar object makes two incompatible scenes fit in the space of a single glance.",
        when: "Use two skies for conflicting moods or two experiences of the same moment. One pair of glasses makes the contradiction easy to notice.",
        why: "A contradiction inside a small object lets a story hold two emotional truths without resolving them.",
        connection: "In The False Mirror, a sky appears inside an eye. The glasses transfer that merger of inside and outside to two different skies.",
        example: 1,
      },
      {
        detail: "Follow the repeated desktop edges upward. Ordinary spatial clues make the route readable before its absurd construction sinks in.",
        when: "Use impossible repeated furniture when a routine should feel endless or absurd. Familiar perspective helps people accept the strange structure long enough to explore it.",
        why: "Using a plausible path through an implausible object lets satire emerge slowly as the viewer follows it.",
        connection: "Dalí gives strangely transformed objects believable rendering and placement. The stacked desks make the same bargain with the viewer through perspective.",
        example: 0,
      },
      {
        detail: "The near wall remains mundane. Look at how much of the implied world changes once the horizon appears in a small opening.",
        when: "Use a tiny door onto a vast sea for escape or longing. Make the room believable so the contrast lands the instant the door opens.",
        why: "A sharp change of scale can communicate longing or a sudden mental escape without exposition.",
        connection: "Magritte puts a wide exterior sky inside a bounded form. Compare the shift in scale when the office wall opens onto the sea here.",
        example: 1,
      },
    ],
  },
  "constructivism": {
    history: "Russian Constructivism developed around the 1917 revolution. Artists approached work as something to build for a social purpose, and related approaches spread through posters, books, and design.",
    effect: "Strong diagonals, blocks of type, and cut photographs can organize information and make it feel like a call to act.",
    use: "Use it for a campaign, a public message, or a story about institutions and collective energy. Give the reading order a strong direction.",
    why: "A clear organizing axis gives a public message a direction that a reader can feel before reading the words.",
    period: "Russian avant-garde and Constructivist design, ca. 1917–1920s",
    examples: [
      { label: "El Lissitzky, Proun 19D (1920 or 1921), MoMA", href: "https://www.moma.org/collection/works/79040" },
      { label: "El Lissitzky, For the Voice (1923), MoMA", href: "https://www.moma.org/collection/works/14473" },
    ],
    variants: [
      {
        detail: "Follow one angled line from the steps through the body. The person’s motion and the layout point the same way.",
        when: "Use an upward diagonal for a rally or a sense of rising effort. Repeated forms make an individual gesture feel part of a larger push.",
        why: "A shared direction makes private effort feel joined to a public or collective movement.",
        connection: "Proun 19D builds a sense of dynamic space from angled forms. This study extends a comparable arrangement through a figure.",
        example: 0,
      },
      {
        detail: "Notice how the circular crop and the wedge shapes pull the face in different directions. The open ground keeps them readable.",
        when: "Use a clipped profile and wedges for a public-facing notice or urgent instruction. The shape of the layout makes the portrait feel directed outward.",
        why: "A few directional forms can make a small poster feel like an instruction or an urgent address.",
        connection: "For the Voice uses geometric elements and bold type to direct readers. Compare the way shape can move attention even before you read any words.",
        example: 1,
      },
      {
        detail: "Switch between the photo-like fragment and a flat red shape. Their difference makes the cutout feel pasted into a public message.",
        when: "Use cut photos for a message about industry or administration. The change in scale makes office objects active parts of a public argument.",
        why: "Contrasting printing textures lets office objects take on the force of evidence or instructions.",
        connection: "For the Voice shows constructive page design through contrasting graphic elements. The desk study uses photomontage as a related Soviet design method.",
        example: 1,
      },
      {
        detail: "Look at the gap around one block in the grid. Its spacing changes how long the portrait holds your attention.",
        when: "Use the modular arrangement for a collective or institutional identity. Regular pieces make a portrait feel assembled from parts of a system.",
        why: "A modular portrait can suggest an institution made of parts, while giving a central face somewhere to hold the design together.",
        connection: "Proun 19D organizes simple forms into an abstract construction. This variant applies a related building-block logic to a recognizable portrait.",
        example: 0,
      },
    ],
  },
  "baroque": {
    history: "From around 1600, Baroque approaches developed across Europe and spread through trade, religion, and empire. Churches and courts used dramatic art and architecture to draw viewers into public experiences.",
    effect: "Directional light, sweeping movement, and gestures bring a moment to a climax. They can make it feel urgent, intimate, or grand.",
    use: "Use it to stage a revelation, arrival, or shift in power. Decide where the strongest light and gestures should lead the audience.",
    why: "A dramatic arrangement gives one arrival or gesture the feeling of a turning point and makes the viewer wonder what follows.",
    period: "Seventeenth-century Baroque painting in Italy and the Dutch Republic",
    examples: [
      { label: "Caravaggio, The Supper at Emmaus (1601), National Gallery", href: "https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus" },
      { label: "Rembrandt, The Night Watch (1642), Rijksmuseum", href: "https://www.rijksmuseum.nl/en/stories/10-things/story/10-things-about-rembrandt-s-night-watch" },
    ],
    variants: [
      {
        detail: "Find the instant where the bright doorway joins the person’s outline and makes it break free of the surrounding dark.",
        when: "Spotlight the threshold when a character’s arrival changes the room. Darkness elsewhere makes the doorway feel like a stage.",
        why: "Making arrival visible through light gives a single figure the weight of a turning point.",
        connection: "Rembrandt uses selective light and uneven grouping to animate a civic gathering. The doorway study applies that principle to one arrival.",
        example: 1,
      },
      {
        detail: "Read along the table toward the extended arm, then let the arm send you back across the room. The layout choreographs the reaction.",
        when: "Use a sweeping table and gesture for a speech that gathers people into the same moment. The movement tells the audience where to look next.",
        why: "A diagonal route lets a reader experience the timing of a speech through the sequence of things they see.",
        connection: "Caravaggio’s supper uses foreshortened arms and an advancing table edge to bring the event towards the viewer.",
        example: 0,
      },
      {
        detail: "Look at the small warm reflections and what lies beyond them in darkness. This is a deliberate limit on how much of the room feels present.",
        when: "Use candlelight for a private confidence, a secret, or an uneasy alliance. A small amount of warm light limits the meeting to what the characters can see.",
        why: "A restricted light source can make a conversation seem confidential without a written cue.",
        connection: "Caravaggio’s strong directional light is a Baroque precedent for selective visibility. The variant narrows the light to the scale of a candle.",
        example: 0,
      },
      {
        detail: "Follow the railing toward the sitter. Your eye climbs while the low viewpoint makes her seem high above the room.",
        when: "Use a rising staircase for a ceremonial portrait or a shift in power. Seeing the figure from below makes even a still pose feel commanding.",
        why: "A rising view gives the building a role in staging power and can turn a stationary pose into a dramatic encounter.",
        connection: "The figures and active diagonals in The Night Watch create a sense of emergence. The staircase variant uses architecture to supply the climb.",
        example: 1,
      },
    ],
  },
  "futurism": {
    history: "Italian Futurism announced itself in a 1909 manifesto. It glorified speed and modern machinery and also embraced violence and nationalism, a troubling part of its history.",
    effect: "Repeated outlines and fragmented shapes fit different instants into a single image. The results can feel exhilarating, relentless, or both.",
    use: "Use its visual methods for motion, mechanical pace, or an overstimulating city. Repeating the direction of movement helps readers sense the speed.",
    why: "Repeating a pose communicates direction and speed in one image, which can make a still scene feel hurried.",
    period: "Italian Futurism, launched in 1909",
    examples: [
      { label: "Giacomo Balla, Dynamism of a Dog on a Leash (1912), Buffalo AKG Art Museum", href: "https://buffaloakg.org/artworks/196416-dinamismo-di-un-cane-al-guinzaglio-dynamism-dog-leash" },
      { label: "Umberto Boccioni, Unique Forms of Continuity in Space (1913), MoMA", href: "https://www.moma.org/collection/works/81179" },
    ],
    variants: [
      {
        detail: "Read the ghosted glasses and hand as a sequence. The space between traces is part of how fast the gesture feels.",
        when: "Repeat the hand or glasses to make a split-second gesture feel fast. A reader sees its path without a second panel.",
        why: "The audience can see an entire small action in one still image, which is useful for a quick interruption or a nervous habit.",
        connection: "Balla’s repeated paws and leash make several positions visible at once. The glasses are a smaller version of that motion problem.",
        example: 0,
      },
      {
        detail: "The station lines and the moving figure share a destination. Look at how the air around her seems to point there too.",
        when: "Use the station approach for crowds or a commute under pressure. Receding architecture makes the rush seem to pull the whole city with it.",
        why: "A shared direction makes a crowd feel swept into a pace larger than any one commuter.",
        connection: "Boccioni’s sculpture uses surrounding forms to make a stride seem connected to the space around it.",
        example: 1,
      },
      {
        detail: "Follow the traces around the chair and find where they seem to curve back toward one point.",
        when: "Use repeated curves for a spin or dizzy comic beat. A center of rotation makes the motion legible even if only parts of the chair appear.",
        why: "Curved echoes can make viewers feel the absurdity or dizziness of a spin without showing a before-and-after pair.",
        connection: "Balla’s repeated arcs around the leash show how an object can map a changing position. The chair describes a wider arc.",
        example: 0,
      },
      {
        detail: "Focus only on the fingertips. Their short repeated paths turn typing into a unit of rhythm.",
        when: "Use repeated hands for repetitive work that is getting out of control. A close crop makes the rhythm of the keyboard fill the scene.",
        why: "Repeating a small action makes its pace, effort, or absurd persistence the center of the story.",
        connection: "Balla gives attention to a dog’s tiny moving paws. The typing study scales that insight to a movement as ordinary as office work.",
        example: 0,
      },
    ],
  },
  "symbolism": {
    history: "Late nineteenth-century Symbolist painters and writers used myths, dreams, and charged objects to suggest inner experiences. They often left the meaning open to the audience.",
    effect: "A badge, flower, or window can carry an idea beyond its everyday use. A single recurring image can invite readers to consider duty, desire, or fear.",
    use: "Use it when you want a theme to surface through an object or setting. Build meaning through context so readers have something to interpret.",
    why: "A familiar prop gives an abstract question a shape that a reader can remember and interpret in more than one way.",
    period: "Late nineteenth-century Symbolism (1880s–1890s) and its French precursors",
    examples: [
      { label: "Gustave Moreau, Oedipus and the Sphinx (1864), The Met", href: "https://www.metmuseum.org/art/collection/search/437153" },
      { label: "The Met’s Symbolism essay, with late nineteenth-century works", href: "https://www.metmuseum.org/it/essays/symbolism" },
    ],
    variants: [
      {
        detail: "Count how an ordinary badge turns into a long succession of badges. The extra pieces change the weight of the lanyard, visually and in meaning.",
        when: "Use a chain of badges for an obligation the character cannot easily put into words. The everyday object carries the idea of weight.",
        why: "A prop can hold an idea such as obligation before a character is ready to say it aloud.",
        connection: "The Met traces how Symbolists used objects and figures to suggest ideas that reach beyond the literal scene. The badge chain translates that method into an office.",
        example: 0,
      },
      {
        detail: "Look for the divide between scattered and ordered marks in the two lenses. The face gives both equal room.",
        when: "Use contrasting lenses when someone must balance conflicting instincts. One face holds both ways of seeing without resolving the choice.",
        why: "One recurring prop can expose a split in the way a character thinks without forcing viewers to choose a side.",
        connection: "Moreau’s stare between Oedipus and the Sphinx gives an outward encounter an inner meaning. Here the encounter between viewpoints happens behind one pair of glasses.",
        example: 0,
      },
      {
        detail: "Compare the outsize desk with the relatively simple balance beneath it. You read the act of weighing before you read what is being weighed.",
        when: "Use the balanced desk for a decision about what work costs or what deserves attention. The scale makes an abstract judgment visible.",
        why: "A physical action can make an abstract question about priorities easy to grasp and still leave the answer open.",
        connection: "The Met’s examples show how ideas were conveyed through charged objects or figures. The scales are this study’s own visual metaphor for judgment.",
        example: 1,
      },
      {
        detail: "Notice what is missing around the one lit opening. The office supplies a trace of the person even when the figure is small.",
        when: "Use a single glowing window for loneliness or work that persists after others have gone. Its meaning grows if the image recurs later in the story.",
        why: "An ordinary setting can carry a private feeling through repetition. That gives a comic a quiet motif it can revisit later.",
        connection: "The Symbolism essay presents settings and forms as vehicles for an inner world. Read the window as a clue to feeling rather than a description of the office.",
        example: 1,
      },
    ],
  },
  "ukiyo-e": {
    history: "Ukiyo-e flourished in Japan’s Edo period and continued into the nineteenth century. Paintings and collaboratively made woodblock prints depicted actors, city life, and famous landscapes.",
    effect: "Flat colors, cropped forms, and layered views give an ordinary gesture or slice of weather a striking presence. A strong near edge can suggest depth without realistic shading.",
    use: "Use its compositional methods for an everyday encounter, a journey, or a city view that should feel carefully framed.",
    why: "A decisive crop lets the reader feel like a passerby who has arrived at a particular place and moment.",
    period: "Edo-period ukiyo-e print culture, including nineteenth-century landscape series",
    examples: [
      { label: "Utagawa Hiroshige, Sudden Shower at Shōno (1834–35), The Met", href: "https://www.metmuseum.org/art/collection/search/36521" },
      { label: "Katsushika Hokusai, Under the Wave off Kanagawa (ca. 1830–32), The Met", href: "https://www.metmuseum.org/art/collection/search/45434" },
    ],
    variants: [
      {
        detail: "Track the direction of the rain across the cut-off umbrella. The crop makes the weather feel as if it continues beyond the page.",
        when: "Use weather and a cropped umbrella when a commute should feel like an observed instant. The diagonal rain keeps the open space active.",
        why: "A cropped element can put the reader in the middle of everyday movement instead of setting them at a distance.",
        connection: "Hiroshige uses slanting rain and moving travelers to make one moment on a familiar route memorable.",
        example: 0,
      },
      {
        detail: "Notice how the near doorway obscures part of the room. The frame establishes where the viewer stands, even with little shading.",
        when: "Use a near doorway for an overheard or private moment. Partly hiding the room makes the viewer feel positioned just outside it.",
        why: "A partially blocked view can make an ordinary scene feel private, overheard, or only briefly available.",
        connection: "The Great Wave uses an enormous near shape to frame a smaller distant view. Both compositions create depth by letting the closest form occupy part of the view.",
        example: 1,
      },
      {
        detail: "The sleeve and glasses take up attention normally held by a face. Follow the partial shapes at the edges to imagine the rest of the gesture.",
        when: "Use a close view of hands for a small decision or a habitual movement. An everyday gesture can take over the whole picture.",
        why: "A small routine becomes significant when the crop removes almost every competing cue.",
        connection: "Hiroshige chooses a handful of gestures to describe travelers in bad weather. This panel concentrates that selective attention into a detail.",
        example: 0,
      },
      {
        detail: "Find the first roof edge that overlaps another. The city gets deeper as you count the layers, long before you inspect individual windows.",
        when: "Use stacked roofs to establish a city before returning to the characters. Overlap makes the space clear without changing the flatness of the colors.",
        why: "Clear bands of near and far forms make an establishing view immediately legible.",
        connection: "In The Great Wave, boats, the curling wave, and Mount Fuji sit at strikingly different scales. The roof study uses similar layering with calmer horizontal forms.",
        example: 1,
      },
    ],
  },
  "neoclassicism": {
    history: "In the late eighteenth century, finds at sites such as Pompeii and renewed study of Greece and Rome encouraged Neoclassical art. Artists adapted ancient forms to express modern civic and moral ideals.",
    effect: "Clear contours, balanced groups, and restrained gestures can communicate deliberation, duty, or public authority.",
    use: "Use it for a formal debate, declaration, or portrait of responsibility. Give each gesture enough space to be read clearly.",
    why: "A stable arrangement can convey ceremony and self-control. It helps an audience see who holds authority and how that role is performed.",
    period: "European Neoclassicism, late 1700s to early 1800s",
    examples: [
      { label: "Jacques-Louis David, Oath of the Horatii (1784, exhibited 1785), Louvre", href: "https://collections.louvre.fr/en/ark%3A/53355/cl010062239" },
    ],
    variants: [
      {
        detail: "Connect the raised gesture to the repeating architectural uprights. The room gives the speaker a stable frame for the address.",
        when: "Use centered order when a speech should feel civic or formal. Give the speaker one clear gesture to convey the decision.",
        why: "Formal order makes the decision seem public and considered even before anyone speaks.",
        connection: "Compare how Jacques-Louis David uses arches and outstretched arms to make a civic oath immediately readable.",
        example: 0,
      },
      {
        detail: "Compare the clean line of the nose with the straight column. A human curve comes into focus against the simple architectural form.",
        when: "Use profile with a column for restraint or resolve. A clean edge and vertical form give the sitter a poised quality.",
        why: "An uncluttered profile can suggest restraint, a decision held in reserve, or readiness to act.",
        connection: "David’s clear figure contours and spare classical architecture offer a precedent for isolating a pose in a measured setting.",
        example: 0,
      },
      {
        detail: "Read the three figures in succession, as if following a story along a strip carved onto a wall.",
        when: "Use a horizontal row for an argument with several participants. A frieze-like arrangement lets readers compare each gesture as they move across it.",
        why: "A side-by-side arrangement lets viewers compare roles or points of view without introducing a complex room.",
        connection: "David separates the key groups laterally across a shallow architectural stage, a useful comparison for the frieze-like layout.",
        example: 0,
      },
      {
        detail: "The ledger lies where the arms meet. Look at the long pauses of empty space around that small concentrated gesture.",
        when: "Use the ledger as a symbol of stewardship or duty. A balanced pose makes the document feel important to the sitter.",
        why: "An object can suggest stewardship when the composition gives it the same deliberate attention as the sitter.",
        connection: "The central swords in David’s oath are a public object of duty. The ledger is a quieter modern counterpart, used in a portrait rather than a historical scene.",
        example: 0,
      },
    ],
  },
  "romanticism": {
    history: "Around the late eighteenth and early nineteenth centuries, Romantic artists gave strong feeling, imagination, and the power of nature a central role. They worked across many national traditions.",
    effect: "A small person against a storm, mountain, or vast interior can suggest awe, vulnerability, or longing. This mixture of wonder and fear is often called the sublime.",
    use: "Use it when the setting should feel larger than the character’s ability to control it, or when solitude matters more than action.",
    why: "A strong change in scale can communicate awe, isolation, or uncertainty even when a face is too far away to read.",
    period: "European Romanticism and the sublime, early nineteenth century",
    examples: [
      { label: "Caspar David Friedrich, Wanderer Above the Sea of Fog (ca. 1817), Hamburger Kunsthalle", href: "https://www.hamburger-kunsthalle.de/en/news/wanderer-above-sea-fog-caspar-david-friedrich" },
    ],
    variants: [
      {
        detail: "Look at how far the dark cloud extends past the outline of the figure. A person supplies a familiar scale to a sky that otherwise has none.",
        when: "Use the storm before it breaks for dread or anticipation. The figure’s small scale keeps attention on forces she cannot direct.",
        why: "That mismatch makes anticipation feel physical, as if the weather could overwhelm a person’s plans.",
        connection: "Friedrich uses a lone observer to help the viewer measure a landscape that remains obscured by fog.",
        example: 0,
      },
      {
        detail: "Trace the repeating arches until their edges lose clarity. The building starts to feel far too large to see in one glance.",
        when: "Use a deep interior for an encounter with something immense or unknown. The distant light gives the viewer a destination without resolving the feeling.",
        why: "An interior can communicate awe normally associated with landscape if the audience cannot comfortably take in its full scale.",
        connection: "Friedrich’s visible traveler and hard-to-measure distance give the same experience of scale using mountains rather than a built interior.",
        example: 0,
      },
      {
        detail: "Follow the bridge out into the sky, then look for one unruly edge on the clothing or hair. That edge connects the person to the forces around her.",
        when: "Use an exposed bridge for a decision made in uncertain conditions. Wind and openness let the surroundings express the risk.",
        why: "Small bodily clues keep a vast setting from becoming an empty view. They let risk and exposure register personally.",
        connection: "The elevated position in Friedrich’s painting makes a place feel both commanding and precarious. A windy bridge creates a related physical relationship.",
        example: 0,
      },
      {
        detail: "Start at the only bright window and then pull back to the dark skyline. The occupied space seems much smaller the longer you look.",
        when: "Use a single office window for late-night longing or resolve. The warm square makes solitude visible against an otherwise immense city.",
        why: "Giving solitude a visible scale lets a large city express longing rather than merely indicate a location.",
        connection: "Friedrich’s painting makes one person a center for a much greater surrounding space. The lit window performs that role without a foreground silhouette.",
        example: 0,
      },
    ],
  },
  "op-art": {
    history: "Op Art gained wide attention in the 1960s, including through MoMA’s 1965 exhibition The Responsive Eye. Artists such as Bridget Riley explored the way repeated marks affect vision.",
    effect: "Precise stripes and grids can seem to pulse, tilt, or bend even when the image is still. The viewer’s own perception completes the effect.",
    use: "Use it to suggest instability or draw attention to the act of looking. Test strong patterns at their final display size.",
    why: "Repeated contrasts can describe an apparent curve or pulse without drawing an object that actually moves.",
    period: "Op Art, particularly MoMA’s The Responsive Eye exhibition (1965)",
    examples: [
      { label: "Bridget Riley, Current (1964), MoMA", href: "https://www.moma.org/collection/works/79998" },
      { label: "The Responsive Eye exhibition (1965), MoMA archive", href: "https://www.moma.org/calendar/exhibitions/2914" },
    ],
    variants: [
      {
        detail: "Look for the part of the grid where the gaps start to narrow. Compare it with the still figure to catch the apparent shift.",
        when: "Use a warped grid when a stable world should briefly appear unstable. Keep a still reference shape so the viewer can sense the change.",
        why: "A bend in an expectantly regular pattern gives a safe, readable way to imply that a stable world is becoming unreliable.",
        connection: "Riley’s Current makes slight variations in repeated lines feel like movement. In this square the shift happens inside a grid.",
        example: 0,
      },
      {
        detail: "Let your attention move from the dense stripes to the plain figure and back. The sensation changes even while the image is still.",
        when: "Use vibrating stripes to suggest noise or agitation without a depicted event. Leave a quiet solid area and check the effect at display size.",
        why: "A vibrating area can suggest noise or tension, with a plain area that allows the viewer to recover.",
        connection: "Current uses black and white lines to make an apparent vibration without any physical motion.",
        example: 0,
      },
      {
        detail: "Watch how your eye returns to the center as ring spacing changes. Direction is built into the pattern rather than supplied by a gesture.",
        when: "Use rings for concentration or disorientation. Their shared center gives the gaze a pull that can point toward an eye or a prop.",
        why: "Concentric forms are useful for drawing attention toward one detail or showing a character’s narrowed attention.",
        connection: "The Responsive Eye exhibition surveyed how repeating patterns prompt active perception. The ring version applies that question to a single center.",
        example: 1,
      },
      {
        detail: "Compare one apparent corner of the square field with the still pose. Changes in cell shape make a flat area seem to bend.",
        when: "Use a bending checkerboard for a floor that seems to flex. An ordinary seated figure fixes the scale and makes the distortion easier to detect.",
        why: "Optical distortion can make the viewer feel instability directly and judge it against an ordinary object or body.",
        connection: "The 1965 exhibition gathered works with several kinds of optical effect. The checkerboard applies that experimental tradition to the appearance of a surface.",
        example: 1,
      },
    ],
  },
  "persian-manuscript": {
    history: "From the medieval period onward, workshops in Iran and elsewhere in the Persianate world made illustrated books of poetry, epic, and history. Calligraphers, painters, and other artisans worked together on these pages.",
    effect: "Layered rooms, clear outlines, and dense pattern can show several people or events in one scene. The eye travels through the page and discovers connections.",
    use: "Use this approach for a layered ensemble or a building with several activities visible at once. Give each area a clear center of attention.",
    why: "Showing multiple places clearly at once gives readers room to explore an event and follow relationships between people.",
    period: "Persianate book arts and Safavid manuscript painting, early sixteenth century",
    examples: [
      { label: "Attributed to Sultan Muhammad, The Court of Kayumars (ca. 1524–25), Aga Khan Museum", href: "https://collections.agakhanmuseum.org/collection/artifact/court-of-kayumars-akm165" },
      { label: "The Shahnama of Shah Tahmasp (sixteenth century), The Met", href: "https://www.metmuseum.org/es/learn/educators/curriculum-resources/art-of-the-islamic-world/unit-five/chapter-three/the-shahnama-of-shah-tahmasp" },
    ],
    variants: [
      {
        detail: "Find the stair landing and see how many separate tasks you can reach from it with your eye.",
        when: "Use stacked rooms when several activities matter at once. A staircase or corridor lets the reader trace how the people and actions connect.",
        why: "A cutaway lets the audience keep several simultaneous actions in mind while still understanding how the people can meet.",
        connection: "The Court of Kayumars arranges groups on several levels around a central person. The office translates that readable layering into rooms.",
        example: 0,
      },
      {
        detail: "Follow the pool from one group toward another. The open space between them makes their relationship visible without a hard panel border.",
        when: "Use the courtyard layout to stage a shared discussion. The pool and arcade can separate groups without making the scene feel divided into panels.",
        why: "An organizing surface can make an ensemble scene navigable and still leave people enough room to act separately.",
        connection: "The Shahnama manuscript contains complex scenes organized with architecture and landscape. The pool here acts as a modern guide through a similarly layered picture.",
        example: 1,
      },
      {
        detail: "Notice how plants and surfaces change with height. You can look down into more than one area without finding a single fixed eye level.",
        when: "Use elevated terraces for an overview with several points of interest. Pattern makes each level recognizable as viewers move across it.",
        why: "A layered viewpoint rewards exploration and reveals actions that a ground-level portrait would hide.",
        connection: "The Court of Kayumars layers rock formations, animals, and figures vertically. This variant preserves the idea of several vantage points in a garden setting.",
        example: 0,
      },
      {
        detail: "Look for the quiet shape made by the open ledger and hands. Denser decoration elsewhere gives the small action its own breathing room.",
        when: "Use a richly patterned study for private reading or concentrated work. Set aside enough quiet space around the book for the central action to remain clear.",
        why: "Detail can hold a viewer in a room while a quieter space keeps the narrative action easy to find.",
        connection: "Compare the patterned surfaces and legible figures in the Shahnama pages. Their relationship is the historical model for attention here.",
        example: 1,
      },
    ],
  },
  "byzantine-mosaic": {
    history: "Many churches in the Eastern Roman Empire and its cultural sphere used mosaics. Artists set small pieces of colored stone and glass, called tesserae, into walls, vaults, and floors.",
    effect: "Light changes as it strikes different pieces. Gold can make a wall seem luminous, while aligned rows of tiles give portraits a strong, formal presence.",
    use: "Use the visual language to evoke ceremony, endurance, or a light-filled interior. Let the scale and direction of the pieces do some of the drawing.",
    why: "Placing individual tiles by color and direction makes a recognizable form at a distance and varied light close up.",
    period: "Early Byzantine monumental and domestic mosaic, fifth to sixth centuries",
    examples: [
      { label: "San Vitale imperial mosaics, Ravenna (consecrated in 547), Smarthistory", href: "https://smarthistory.org/san-vitale/" },
      { label: "Floor Mosaic with a Personification of Ktisis (500–550), The Met", href: "https://www.metmuseum.org/art/collection/search/469960" },
    ],
    variants: [
      {
        detail: "Look at the contour where dark tiles interrupt the bright surrounding field. The face remains easy to find even with light seemingly coming from all directions.",
        when: "Use a gold field for a ceremonial or commemorative image. The frontal pose and reflected light make a portrait feel like a permanent presence.",
        why: "A luminous backdrop and stable frontal pose can make someone feel continually present in a ceremonial space.",
        connection: "San Vitale places imperial figures against a shimmering field. The study borrows the visual relationship while replacing the historical religious and imperial subject.",
        example: 0,
      },
      {
        detail: "Notice how the arched border wraps the figure and separates the blue interior from the gold outside it.",
        when: "Use the cobalt niche when one person should look sheltered or formally set apart. The arch holds the silhouette and gives the figure a scale.",
        why: "An architectural frame makes a person feel formally set apart, even if viewers see the image from a distance.",
        connection: "San Vitale’s figures are inseparable from the shaped surfaces on which they sit. Here a niche gives one figure a similar relationship to the building.",
        example: 0,
      },
      {
        detail: "Trace the border like someone approaching from the side. It still tells you where to look without a fixed wall viewpoint.",
        when: "Use a floor medallion for a room navigated on foot. A center and strong border make the design readable from more than one approach.",
        why: "A strong center keeps a floor image legible for people moving around it.",
        connection: "The Ktisis mosaic shows that Byzantine figural images could also occupy floors. Compare the legibility of the head and border from above.",
        example: 1,
      },
      {
        detail: "Find where a row of tiles changes direction near the cheek. The orientation helps establish volume without any soft blend.",
        when: "Use tile rows and a close crop to show how small pieces can create an expression. Changing their direction is enough to turn a cheek or frame an eye.",
        why: "Tiled portraiture lets tiny pieces communicate a face. A close crop makes the craft visible as well as the expression.",
        connection: "Ktisis shows how individual pieces can model face and adornment. Compare the way the rows negotiate the portrait’s edges.",
        example: 1,
      },
    ],
  },
  "dada": {
    history: "Dada took shape during World War I in Zurich and other cities. Artists questioned cultural authority and used absurdity, chance, and ordinary materials. Berlin Dadaists became known for photomontage.",
    effect: "Cut-up photographs and labels retain traces of their old meanings. Their new arrangement can turn official language or familiar pictures into a joke or a critique.",
    use: "Use it for institutional satire, or to show that a news image, chart, or rule can be taken apart and made to say something else.",
    why: "Rearranging everyday images can make routine rules seem strange enough to question.",
    period: "World War I and Weimar-era Dada photomontage, 1910s–1920s",
    examples: [
      { label: "Hannah Höch, Indian Dancer: From an Ethnographic Museum (1930), MoMA", href: "https://www.moma.org/collection/works/37360" },
    ],
    variants: [
      {
        detail: "Try reading the calendar as a face before reading the dates. The glasses encourage both readings at once.",
        when: "Swap a face for a calendar to make a joke about a schedule taking over someone’s identity. Keeping the glasses makes the substitution readable.",
        why: "A familiar fragment can turn a literal portrait into a joke about the systems that define a person.",
        connection: "Höch assembled faces and bodies from printed fragments. Her combinations are a precedent for making an unexpected new identity from recognizable parts.",
        example: 0,
      },
      {
        detail: "Follow the arrows until they take you back where you started. The diagram’s visual authority outlasts its logic.",
        when: "Use a circular chart to satirize a process that keeps pointing back at itself. Unexpected characters make its official-looking logic feel absurd.",
        why: "A convincingly official format sets up a stronger joke when its contents refuse to act official.",
        connection: "Höch recut material from mass print culture and exposed the assumptions carried by those images. The office diagram applies that tactic to a different kind of printed authority.",
        example: 0,
      },
      {
        detail: "Compare the size of the stamp handle with the scale of the person and desk. The picture gives a tool more visual power than the people using it.",
        when: "Use a stamp that dwarfs the people for a gag about bureaucratic power. Viewers feel the imbalance before they read the label.",
        why: "An absurd change of size turns an invisible administrative hierarchy into a joke the reader sees immediately.",
        connection: "Höch’s montages break the original proportions of their sources. The stamp variant concentrates that freedom into one object.",
        example: 0,
      },
      {
        detail: "Look for a scrap you can still recognize as paperwork after it becomes a facial feature. That double role is the punch line.",
        when: "Use scraps of forms and photos for a portrait about the labels an office gives someone. Let some pieces retain their earlier meanings.",
        why: "Mixed sources can make a portrait feel assembled out of the ways a workplace measures or labels a person.",
        connection: "Compare how Höch lets her photographic fragments keep visible traces of their original context. Those traces drive the reading of the new portrait here.",
        example: 0,
      },
    ],
  },
  "abstract-expressionism": {
    history: "Abstract Expressionism took shape in the United States in the 1940s and 1950s. Its artists explored approaches ranging from visible physical gestures to broad fields of color.",
    effect: "A stroke can feel quick or forceful, and a large unbroken color can feel absorbing or tense. Paint itself carries the mood with only a few clues to recognizable objects.",
    use: "Use it when an emotional state, a rhythm, or a sense of scale should come through before the viewer identifies a scene.",
    why: "Scale and physical-looking marks can communicate force or duration even when the subject becomes hard to identify.",
    period: "Postwar American Abstract Expressionism, 1940s–1950s",
    examples: [
      { label: "Jackson Pollock, One: Number 31, 1950 (1950), MoMA", href: "https://www.moma.org/collection/works/78386" },
      { label: "Mark Rothko, No. 10 (1950), MoMA", href: "https://www.moma.org/collection/works/78594" },
    ],
    variants: [
      {
        detail: "Follow the sweep to where it thins out. The change in speed is legible before the hints of glasses.",
        when: "Use one broad gesture for a sharp outburst or a moment of momentum. A fleeting identity cue keeps it connected to the character.",
        why: "Making the mark feel made in real time gives an emotional outburst physical energy.",
        connection: "Pollock’s sweeping paint traces give clues to motion. This study puts that energy into one main gesture.",
        example: 0,
      },
      {
        detail: "Give the navy area a moment before chasing the warm accent. As your eye adjusts, the edges start to feel less fixed.",
        when: "Use a large quiet color field when you want tension to build from subtle changes. A small accent can feel powerful against an otherwise slow scene.",
        why: "A field of color can slow a page down and let a small shift in mood become the event.",
        connection: "Rothko’s soft boundaries between large areas of color reward long looking. The navy study tests a similar relationship with one small accent.",
        example: 1,
      },
      {
        detail: "Scan from corner to corner and see how hard it is to settle on a single focal point.",
        when: "Use marks across the whole surface to suggest restless energy with no single center. The reader’s wandering attention becomes part of the effect.",
        why: "An all-over rhythm can make a feeling of noise or motion fill a picture instead of belonging to one object.",
        connection: "Pollock’s network of marks crosses most of the canvas. It offers a historical example of attention distributed throughout a composition.",
        example: 0,
      },
      {
        detail: "Look at the gaps between the color blocks and the dark mass. The surrounding pressure can make simple shapes look crowded.",
        when: "Crowd familiar colors with a scraped dark area to convey strain. The logo-like fragments hint at identity under pressure without spelling out an event.",
        why: "Viewers can sense strain without being shown its cause. The recognizable colors keep the idea tied to a character or identity.",
        connection: "Rothko helps show how size and placement govern the effect of neighboring colors. The scraped surface here adds an abrasive note to that relationship.",
        example: 1,
      },
    ],
  },
  "chinese-ink-landscape": {
    history: "Landscape developed into an independent painting genre in China by the late Tang dynasty. Song painters and later scholar-artists used mountains, water, and paths to explore ideas about nature and human life.",
    effect: "Diluted ink makes mist and distance, and open paper gives the eye places to rest. Tiny figures and structures can make a landscape feel spacious and contemplative.",
    use: "Use it for a retreat, journey, or quiet interval. Let the scenery set the pace and use a small human detail to establish scale.",
    why: "A small landmark gives viewers a measure of distance. Open areas also let the eye move at a slower pace through a landscape.",
    period: "Northern Song landscape painting and the Chinese handscroll tradition",
    examples: [
      { label: "Attributed to Qu Ding, Summer Mountains (ca. 1050), The Met", href: "https://www.metmuseum.org/art/collection/search/39915" },
      { label: "Landscape Painting in Chinese Art, including Song-dynasty landscapes (960–1279), The Met", href: "https://www.metmuseum.org/zh/essays/landscape-painting-in-chinese-art" },
    ],
    variants: [
      {
        detail: "Notice how much water seems to exist around the small ferry, even where there are very few painted marks.",
        when: "Use a small boat to make distance and silence feel tangible. The passenger’s scale lets the water hold most of the scene.",
        why: "A tiny traveler can make stillness and distance palpable without filling the scene with signs of travel.",
        connection: "In Summer Mountains, small features measure the broad landscape and open areas give the eye breathing room.",
        example: 0,
      },
      {
        detail: "Trace the near path to a much paler mountain. The gap in paint defines an interval of air between the two.",
        when: "Use the mountain composition to put a data center in perspective. Natural forms dwarf the structure while the path gives viewers a way into the setting.",
        why: "Putting a technical structure against a large landscape changes the story’s sense of importance and scale.",
        connection: "Summer Mountains uses successive landscape masses to organize a world much larger than its people and buildings.",
        example: 0,
      },
      {
        detail: "Compare the dark edge of the shelter with the distant washes. The limited contrast outdoors makes you feel the weather from the protected side.",
        when: "Use a dark shelter and pale hills for being indoors while weather passes outside. The contrast lets viewers feel both shelter and rain.",
        why: "Hard and soft edges can convey the bodily experience of shelter rather than just depict rain.",
        connection: "The Met’s survey describes landscapes as places of retreat and reflection. This variant uses a shelter to make the viewer feel that threshold.",
        example: 1,
      },
      {
        detail: "Move your eye along the shore in stages, stopping at denser clusters. The open intervals are part of the rhythm.",
        when: "Use a scroll-like composition for a journey the viewer discovers in stages. Break up clusters of detail with open stretches of water.",
        why: "A horizontal journey gives readers time to discover a setting at their own pace.",
        connection: "Summer Mountains is a handscroll: viewers traditionally encounter its scenes in sections. The square adapts that sequential way of looking.",
        example: 0,
      },
    ],
  },
  "mexican-muralism": {
    history: "In the 1920s, after the Mexican Revolution, public commissions gave muralists such as Diego Rivera, José Clemente Orozco, and David Alfaro Siqueiros large walls for political and historical storytelling.",
    effect: "Strong gestures and broad groups help people read a wall from a distance. Shared work becomes visible through the relationship among figures, tools, and setting.",
    use: "Use it to tell a public story about labor, contested history, or collective action. Give several people meaningful roles in the composition.",
    why: "Enlarging collective work for a public audience makes the relationship between people and tasks readable across a room.",
    period: "Post-revolutionary Mexican Muralism, from the early 1920s",
    examples: [
      { label: "Diego Rivera, Detroit Industry Murals (1932–33), Detroit Institute of Arts", href: "https://dia.org/collection/detroit-industry-murals/58537" },
      { label: "Diego Rivera, Agrarian Leader Zapata (1931), MoMA", href: "https://www.moma.org/collection/works/80682" },
    ],
    variants: [
      {
        detail: "Follow the cable from one worker to another and see who holds what. The task is understandable as a chain of contributions.",
        when: "Use this for a public story about who actually builds a system. Give tools and plans to several people so each contribution is visible.",
        why: "A shared diagonal makes labor visible across the whole picture and gives more than one person agency.",
        connection: "Rivera organizes workers and machinery into interconnected sequences in Detroit Industry. The cable is a contemporary equivalent for that visual relationship.",
        example: 0,
      },
      {
        detail: "Notice which hands and tools point at the repair. Their converging directions make the cause of the group’s urgency clear.",
        when: "Use the repair scene when shared skill and urgency matter. Gestures converging on one machine show the work continuing beyond a single hero.",
        why: "The audience can understand cooperation before being able to identify every worker.",
        connection: "In Detroit Industry, the positions of workers and tools tell a story about organized work on a large scale.",
        example: 0,
      },
      {
        detail: "Look at where the teaching gesture meets a book or screen. The exchange becomes visible as something happening between people.",
        when: "Use the library approach for knowledge passing from person to person. Several exchanges let the audience see learning as a public activity.",
        why: "Staging several exchanges makes public knowledge feel like an activity rather than a backdrop.",
        connection: "Agrarian Leader Zapata defines its public subject through grouped people and purposeful objects. The library variant redirects a similarly readable grouping toward education.",
        example: 1,
      },
      {
        detail: "Read the line of workers as a continuous row, then compare the tools in their hands. Repetition signals continuity as details mark change.",
        when: "Use a continuous row to connect stages of history. Changes in tools let viewers compare generations without breaking the sense of shared labor.",
        why: "A single wall-like composition can connect generations without turning the story into isolated portraits.",
        connection: "Detroit Industry spreads related scenes across multiple walls. The four-generation strip applies that linked reading to different moments in time.",
        example: 0,
      },
    ],
  },
  "stained-glass": {
    history: "Colored glass windows became a major part of medieval European church architecture, especially in the Gothic period. Strips of lead joined the pieces and helped define the image.",
    effect: "Light passes through the picture, so color changes with the time of day and can fall onto the surrounding walls and floor. The effect can feel ceremonial or intimate.",
    use: "Use it when light should change a room’s atmosphere or turn an emblem into part of the architecture. Think about where the colored light will land.",
    why: "A window can organize a picture on the wall and tint the room people are standing in, giving light a role in the whole space.",
    period: "Medieval Gothic glazing, especially the 1100s–1200s",
    examples: [
      { label: "Chartres Cathedral and its medieval windows (rebuilt from 1194), cathedral archive", href: "https://www.cathedrale-chartres.org/en/visite/decouvrir/la-cathedrale/" },
      { label: "The Met’s historical stained-glass collection bulletin, with medieval windows", href: "https://resources.metmuseum.org/resources/metpublications/pdf/Stained_Glass_Windows_The_Metropolitan_Museum_of_Art_Bulletin_v_30_no_3_December_1971_January_1972.pdf" },
    ],
    variants: [
      {
        detail: "Find where a dark joint reads as both a piece of lead and the edge of her glasses. The material supplies the drawing.",
        when: "Use this for portraits about devotion or memory. Let the glass joins define identity cues instead of drawing a separate outline around them.",
        why: "Making the design out of structural lines gives a portrait a sense of belonging to the building.",
        connection: "At Chartres, the dark divisions between pieces help preserve figures and motifs at a considerable distance.",
        example: 0,
      },
      {
        detail: "Start at the emblem and notice which repeated bands lead your eye back to it. Even from the side, the center stays obvious.",
        when: "Use a rose window when a shared emblem should draw the eye inward. Repetition of colored segments makes the center feel purposeful.",
        why: "A radial plan can make a shared symbol the center of attention without enlarging it at the expense of everything around it.",
        connection: "The medieval rose windows of Chartres show how repeated segments divide an elaborate design into a readable circular field.",
        example: 0,
      },
      {
        detail: "Follow the patch of light down the steps. It breaks at each stair edge and makes the outline of each step visible.",
        when: "Use projected patches of color for a journey through a building. The light shifts as it hits each step, making the architecture part of the image.",
        why: "Projected color can turn an ordinary walk through a building into a gradual change of mood.",
        connection: "The Met’s examples rely on transmitted light. This variant follows the color beyond the glass and into the architecture.",
        example: 1,
      },
      {
        detail: "Read the colored patch before you look for whose desk it is. A pair of glasses and a badge answer the question with very little else.",
        when: "Use colored light on an empty desk for a scene about an absent person. A recognizable prop gives the light somewhere meaningful to land.",
        why: "Indirect light and familiar objects can evoke someone’s absence without a figure or a speech bubble.",
        connection: "Medieval windows change with illumination. The desk applies that same behavior to a quieter, modern scene.",
        example: 1,
      },
    ],
  },
  "trompe-loeil": {
    history: "Trompe-l’œil is French for deceive the eye. Painters have used convincing shallow depth and painted architecture for centuries, including in seventeenth-century European still lifes and interiors.",
    effect: "A painted object appears to occupy the viewer’s space for a moment. The pleasure comes from testing the illusion against the frame and shadows.",
    use: "Use it for a playful reveal, a convincing prop, or a scene about what can be trusted. Small shadows and believable edges make the illusion work.",
    why: "A shallow illusion can make a viewer look twice at the boundary of a page, cabinet, or doorway.",
    period: "European illusionistic painting and nineteenth-century American trompe-l’œil",
    examples: [
      { label: "William Michael Harnett, The Old Violin (1886), National Gallery of Art", href: "https://www.nga.gov/artworks/79531-old-violin" },
      { label: "Deceptions and Illusions, including John Haberle’s Imitation (1887), National Gallery of Art", href: "https://www.nga.gov/exhibitions/deceptions-and-illusions" },
    ],
    variants: [
      {
        detail: "Look where the frame fails to stop the spectacles. Their narrow shadow makes them appear to occupy space in front of the portrait.",
        when: "Use spectacles crossing a frame for a small surprise. Their shadow can turn a flat portrait into something that appears to sit on the wall.",
        why: "A small breach of the frame makes viewers check where the real surface ends and the picture begins.",
        connection: "Harnett paints a violin and other objects as if hung from a real door. Compare the shadows that make the objects look detachable.",
        example: 0,
      },
      {
        detail: "Find the corner of the badge that appears to leave the page first. You can still see the flat paper behind it.",
        when: "Use a lifted badge as a visual reveal in an invitation or prop illustration. The viewer briefly feels they could pick it up.",
        why: "Tempting someone to pick up an object gives a printed prop a playful or uncanny effect.",
        connection: "Harnett’s painted scraps and objects use a similar near-surface illusion. The badge exaggerates the shallow gap above the support.",
        example: 0,
      },
      {
        detail: "Look for the darkest point where a tool appears to touch its support. That tiny patch sells the nearest bit of depth.",
        when: "Use a shallow cabinet for a painted display that looks reachable. You only need enough depth to explain which surface supports each object.",
        why: "Shallow space can be more immediately believable because viewers only have to understand a few overlaps and contacts.",
        connection: "In The Old Violin, the objects sit very close to the apparent wooden surface. The cabinet adds a small amount of depth without losing the effect.",
        example: 0,
      },
      {
        detail: "Use the doorframe as a measuring line. Compare what stays inside it with the file that appears to pass in front.",
        when: "Use a projecting hand for an unexpected invitation or interruption. A clear doorway edge helps the viewer see exactly where the figure appears to break through.",
        why: "Breaking an established boundary turns an ordinary handoff into an invitation toward the audience.",
        connection: "The exhibition collects works that test the boundary between picture and viewer. This version gives that test to a gesture at a threshold.",
        example: 1,
      },
    ],
  },
  "bauhaus": {
    history: "The Bauhaus was a German school active from 1919 to 1933. It brought art, craft, and industry together, and its designers explored how type, images, and simple shapes could serve everyday communication.",
    effect: "Clear alignment and strong differences in size let viewers decide where to start. Geometry can feel orderly while still leaving room for an unexpected accent.",
    use: "Use it for wayfinding, instruction, or a poster where a viewer needs to find the message quickly. Give visual order to the information itself.",
    why: "A clear hierarchy helps a viewer decide what matters and where to go while moving through a building or page.",
    period: "Bauhaus school in Germany, 1919–1933",
    examples: [
      { label: "Joost Schmidt, Staatliches Bauhaus Ausstellung poster (1923), MoMA", href: "https://www.moma.org/collection/works/6235" },
      { label: "Bauhaus 1919–1933: Workshops for Modernity, MoMA", href: "https://www.moma.org/calendar/exhibitions/303" },
    ],
    variants: [
      {
        detail: "Ask which words you can still read from across the room. The title’s size makes it survive before the portrait does.",
        when: "Use a clear title and simple supporting shape for a lecture notice. People should see the event name first and the illustration second.",
        why: "An event poster can announce the practical information first and then reward a closer look with character or atmosphere.",
        connection: "Schmidt’s 1923 exhibition poster lets geometry and typography share one surface. Compare how differences in size guide a viewer’s approach.",
        example: 0,
      },
      {
        detail: "Look at the empty area around the arrow. That space keeps the arrow and destination from competing with the portrait.",
        when: "Use strong type and an uncluttered arrow for people on the move. Negative space makes the direction readable before they stop to think.",
        why: "A short instruction feels immediate when nothing nearby can be mistaken for a second direction.",
        connection: "The Bauhaus exhibition traces design across everyday systems as well as art objects. The wayfinding square applies that practical emphasis.",
        example: 1,
      },
      {
        detail: "Notice where the lettering and profile touch the same imagined vertical. Their alignment unifies two things of very different sizes.",
        when: "Use a well-aligned title and cropped profile to make a cover feel unified. Size differences tell readers which parts to notice first.",
        why: "A common alignment makes a new issue feel part of a series while leaving room for a fresh crop or character.",
        connection: "Schmidt aligns lettering with geometric forms. The cover uses that same underlying order to carry a portrait.",
        example: 0,
      },
      {
        detail: "Follow the pointing hand and stop at the diagram it leads to. The gesture tells you where to start reading.",
        when: "Use diagrams and one directing gesture when someone needs to learn a procedure. The picture shows where to start without relying on a long paragraph.",
        why: "Readers can learn in the right order even if they see the picture before the instructions.",
        connection: "Bauhaus design brought typography and images into practical communication. The training square turns that aim into a short visual lesson.",
        example: 1,
      },
    ],
  },
  "renaissance-perspective": {
    history: "In fifteenth-century Italy, artists and architects including Brunelleschi and Alberti demonstrated or described ways to represent depth consistently on a flat surface.",
    effect: "Lines that are parallel in the room can appear to meet at a point in the picture. That meeting place can send the eye to a figure or carry it past them into the distance.",
    use: "Use it to stage a formal room, make a space easy to navigate, or aim attention at a reveal. Choose the viewer’s position before drawing the room.",
    why: "A shared vanishing point can steer attention toward a character while making the room’s distances convincing.",
    period: "Italian Early Renaissance linear perspective, 1400s",
    examples: [
      { label: "Masaccio, Holy Trinity (ca. 1427), Smarthistory", href: "https://smarthistory.org/masaccio-holy-trinity/" },
      { label: "Pietro Perugino, Christ Giving the Keys of the Kingdom to St. Peter (1481–82), Smarthistory", href: "https://smarthistory.org/perugino-christ-giving-the-keys-of-the-kingdom-to-st-peter/" },
    ],
    variants: [
      {
        detail: "Extend the two receding sides of the table in your mind. Check which part of the room matters most near their meeting point.",
        when: "Use a centered meeting point for a formal entrance or a room with a clear hierarchy. The architecture guides attention to the same place as the action.",
        why: "The room can announce who holds authority before a character speaks.",
        connection: "Perugino’s paved square leads toward a centered building. The boardroom uses a similar convergence to establish a different kind of center.",
        example: 1,
      },
      {
        detail: "Follow the arcade away from the sitter first. The room pulls one way and a foreground body holds your attention elsewhere.",
        when: "Use an off-center meeting point when a foreground person should interrupt the space. The eye can travel with the room and then return to the person.",
        why: "An off-center meeting point gives a still composition two directions to read, which suits a pause or interruption.",
        connection: "Masaccio builds an illusion from a chosen viewpoint. This variant explores what happens when the room’s visual center shifts away from the person.",
        example: 0,
      },
      {
        detail: "Compare two identical tiles at different distances. Their shrinking size tells you how far the viewer has yet to go.",
        when: "Use repeating tiles and doors for a long approach or a slow reveal. The change in their apparent size makes the distance feel measurable.",
        why: "Repeating scale cues can give a long approach a visible pace without adding panels.",
        connection: "Perugino’s pavement provides a comparable set of units. Look at how the apparent spaces between them narrow across the square.",
        example: 1,
      },
      {
        detail: "Start at a near edge of the window and then look at the city. One boundary separates two spaces you can see at once.",
        when: "Use a frame within the picture for someone looking beyond their current situation. Near and far edges make the separation between the room and world feel real.",
        why: "The frame can turn a distant place into a visible goal or give it a sense of being out of reach.",
        connection: "Masaccio’s painted architecture seems to open depth beyond a real wall. The study applies that sensation to a familiar window.",
        example: 0,
      },
    ],
  },
  "de-stijl": {
    history: "De Stijl formed in the Netherlands in 1917 around a journal and a group including Theo van Doesburg and Piet Mondrian. Members pursued a common visual language in art, architecture, and design.",
    effect: "Straight bars, open areas, and primary colors can create balance with deliberately unequal shapes. This study lets a few pieces of the figure emerge from that order.",
    use: "Use it for a compact identity or a scene about order and relationships. Move a single block and notice how it changes the balance.",
    why: "Reducing a scene to rectangles helps you see how proportion and spacing alone can guide the eye.",
    period: "Dutch De Stijl, founded in 1917, and Mondrian’s later development",
    examples: [
      { label: "Piet Mondrian, Broadway Boogie Woogie (1942–43), MoMA", href: "https://www.moma.org/collection/works/78682" },
    ],
  },
  "precisionism": {
    history: "Precisionism appeared in the United States in the 1910s and 1920s. Artists including Charles Sheeler organized factories, silos, and city views into clearly edged forms.",
    effect: "Smooth planes and sharp transitions make industry look designed and legible. The order can seem impressive, eerily quiet, or indifferent to people.",
    use: "Use it when infrastructure should be the subject. Let one recognizable figure establish the scale of the machinery or architecture.",
    why: "Simplifying industrial shapes lets a viewer see how they fit together and feel their scale against a small figure.",
    period: "American Precisionism and industrial imagery, 1910s–1930s",
    examples: [
      { label: "Charles Sheeler, American Landscape (1930), MoMA", href: "https://www.moma.org/collection/works/79032" },
    ],
  },
  "brutalism": {
    history: "Brutalism grew in postwar architecture, especially from the 1950s onward. Many examples use exposed concrete, though the wider approach also emphasizes visible structure and materials.",
    effect: "Thick forms and rough surfaces make a building’s weight feel immediate. A small person can make the space feel civic and monumental or severe and imposing.",
    use: "Use it for a public complex or infrastructure scene where the building should have a strong physical presence. Show a stair, joint, or surface that explains how it is built.",
    why: "Showing the structure openly makes weight and construction part of the experience of entering a building.",
    period: "Postwar architecture and early precedents for Brutalism, 1940s–1960s",
    examples: [
      { label: "Le Corbusier, Unité d’Habitation, Marseille (1945–52), Fondation Le Corbusier", href: "https://www.fondationlecorbusier.fr/oeuvre-architecture/realisations-unite-dhabitation-marseille-france-1945-1952/" },
    ],
  },
  "minimalism": {
    history: "In the 1960s, American artists including Donald Judd explored simple objects, industrial materials, and regular repetition. The room, the objects, and the person looking at them were all part of the experience.",
    effect: "Gaps and surface changes become noticeable when there are few objects. Repetition can suggest calm, strict order, or distance.",
    use: "Use it when placement, scale, or material should hold attention. Keep enough empty room for each interval to register.",
    why: "Removing extra variation makes small changes in interval or height visible and gives the viewer time to notice their own position.",
    period: "American Minimalism and serial sculpture, 1960s",
    examples: [
      { label: "Donald Judd, Untitled (1967), MoMA", href: "https://www.moma.org/collection/works/81324" },
    ],
  },
  "psychedelic-poster": {
    history: "In the 1960s, psychedelic concert posters flourished in places such as San Francisco. Designers borrowed decorative curves and made lettering stretch, curl, and nearly vanish into the image.",
    effect: "Saturated colors and difficult-to-read letters make the eye work and can give a still surface a sense of motion. The poster offers an experience alongside the announcement.",
    use: "Use it for a gig poster or a scene about sensory overload. Keep essential event details easy to find if the poster has a practical job.",
    why: "Lettering that takes time to untangle can make a poster feel immersive and share the mood of a music or performance scene.",
    period: "San Francisco psychedelic concert posters, 1960s",
    examples: [
      { label: "Wes Wilson, Wonderland concert poster (1966), Smithsonian American Art Museum", href: "https://americanart.si.edu/artwork/wonderland-grass-roots-daily-flash-avalon-ballroom-san-francisco-california-7166-7366-76545" },
    ],
  },
  "memphis": {
    history: "The Memphis group began in Milan in 1981 around designers including Ettore Sottsass. Its furniture and objects played with pattern, color, and materials such as decorative laminate.",
    effect: "Jumpy silhouettes and clashing surfaces make an ordinary lamp or desk feel mischievous. The room can tell you that someone is willing to break decor rules.",
    use: "Use it when furniture should carry visual humor or personality. Choose a few strong objects with distinct shapes and let them interact.",
    why: "Playful colors and uneven angles can give furniture a strong personality and make a room memorable without a grand scale.",
    period: "Italian postmodern design and the Memphis group, founded in 1981",
    examples: [
      { label: "Ettore Sottsass, Carlton Room Divider (1981), The Met", href: "https://www.metmuseum.org/art/collection/search/486989" },
    ],
  },
  "afrofuturism": {
    history: "Afrofuturism brings together a long history of Black speculative work in music, literature, film, design, and art. Writers, musicians, and artists have used it to imagine Black agency and freedom across past, present, and future.",
    effect: "The visual language varies. In this study, the orbital setting asks who designs the future, and the Black librarian leads a project centered on public knowledge.",
    use: "Use the approach to explore futures shaped by Black people and cultures. Show who makes decisions and who benefits so that technology has a human purpose.",
    why: "Placing community knowledge at the center makes the future a story about people and priorities, with technology serving that story.",
    period: "Black speculative arts, including 1970s space jazz and film",
    examples: [
      { label: "Poster for Sun Ra’s Space Is the Place (1974), Smithsonian", href: "https://www.si.edu/object/space-place%3Anmaahc_2012.46.59" },
    ],
  },
  "space-age": {
    history: "During the late 1950s and 1960s, the Space Race influenced furniture, product design, advertising, and buildings. Designers brought spacecraft-like curves and new materials into familiar objects.",
    effect: "Rounded plastic shells, chrome, and visible analog controls make space travel look sleek and knowable. The look can convey optimism or nostalgia for an earlier idea of the future.",
    use: "Use it for an inviting station or a scene about what the future once promised. Put an object viewers recognize beside the futuristic hardware to make the idea accessible.",
    why: "Borrowing shapes from engineering can make an everyday object express optimism about a possible future.",
    period: "Space Race–era furniture and product design, late 1950s–1960s",
    examples: [
      { label: "Eero Aarnio, Ball Chair (designed 1963), LACMA", href: "https://collections.lacma.org/object/286614" },
    ],
  },
  "rococo": {
    history: "Rococo flourished in eighteenth-century Europe, especially in French interiors and decorative arts. Shell-like ornament, gilded curves, and asymmetrical arrangements appeared in furniture and rooms designed for social life.",
    effect: "Curves carry the eye around an intimate room, and pale colors soften its richness. The effect can feel gracious, playful, or indulgent.",
    use: "Use it for salon conversation, flirtation, or a gentle satire of luxury. Let the ornament lead to a person or an object that matters to the scene.",
    why: "Curving ornament can make an interior feel playful and intimate while directing attention to a person or small object.",
    period: "French Rococo interiors and furniture, eighteenth century",
    examples: [
      { label: "Boiserie from the Hôtel de Varengeville (ca. 1736–52), The Met", href: "https://www.metmuseum.org/art/collection/search/202996" },
    ],
  },
  "pre-raphaelite": {
    history: "The Pre-Raphaelite Brotherhood formed in Britain in 1848. Its artists looked to earlier European painting, close study of nature, and literature to challenge the conventions they were taught.",
    effect: "Sharp plants, fabrics, and small objects reward slow looking. A flower or letter can carry part of the story, giving a scene emotional tension beneath a calm pose.",
    use: "Use it for a literary moment, a portrait with clues, or a scene where the smallest prop should change how viewers understand the character.",
    why: "Specific details can make a reader linger and piece together the emotional stakes of a quiet scene.",
    period: "British Pre-Raphaelite Brotherhood, founded in 1848",
    examples: [
      { label: "John Everett Millais, Ophelia (1851–52), Tate", href: "https://www.tate.org.uk/art/artworks/millais-ophelia-n01506" },
    ],
  },
  "pointillism": {
    history: "In the 1880s, French Neo-Impressionists such as Georges Seurat experimented with building images from separate touches of color. Pointillism names the dot-based technique associated with that work.",
    effect: "Up close, neighboring dots stay separate. Farther back, they combine into a color impression that can feel luminous or gently vibrating.",
    use: "Use it when the act of seeing color is part of the idea. Side-by-side warm and cool dots are particularly effective in a bright landscape or park scene.",
    why: "Placing marks side by side keeps color varied where a single blended stroke might feel too uniform.",
    period: "French Neo-Impressionism and optical color mixing, 1880s",
    examples: [
      { label: "Georges Seurat, A Sunday on La Grande Jatte — 1884 (1884–86), Art Institute of Chicago", href: "https://www.artic.edu/artworks/27992/a-sunday-on-la-grande-jatte-1884" },
    ],
  },
  "tonalism": {
    history: "American Tonalism flourished in the late nineteenth and early twentieth centuries. Painters such as George Inness and James McNeill Whistler made quiet scenes from closely related colors and values.",
    effect: "Soft edges and a narrow range of light and dark let the scene gather around a single mood. A small warm reflection matters because its surroundings are so restrained.",
    use: "Use it for dusk, fog, remembrance, or a pause after a busy scene. Keep one shape or light distinct enough to give viewers a place to begin.",
    why: "A narrow range of tones makes a quiet scene feel unified and gives a small interruption the power to hold the eye.",
    period: "American Tonalism, late nineteenth to early twentieth century",
    examples: [
      { label: "George Inness, Sundown (1884), Smithsonian American Art Museum", href: "https://americanart.si.edu/artwork/sundown-11100" },
    ],
  },
  "egyptian-wall-painting": {
    history: "New Kingdom tomb chapels used wall painting to show offerings, rituals, and work. Artists often placed scenes in horizontal bands called registers. In Nakht’s chapel, one wall shows several stages of farming, from preparing the soil to separating the grain. The scenes were connected to the offerings that would sustain Nakht in the afterlife.",
    effect: "Each band gives the figures a shared ground line. A profile head and forward-facing eye can be combined so both are legible. The office study uses the bands to let one person recur at three different moments without confusing the order.",
    use: "Use registers to show a routine or work that happens in stages. Repeat a recognizable figure or object and give each band a distinct change, such as an open door becoming a closed one.",
    why: "Repeating one character in separate registers lets a single surface organize several moments of a story.",
    period: "Ancient Egyptian New Kingdom, late Eighteenth Dynasty. Nakht’s chapel dates to ca. 1410–1370 BCE.",
    examples: [
      { label: "East wall of Nakht’s offering chapel (ca. 1410–1370 BCE), recorded in a 1908–10 facsimile, The Met", href: "https://www.metmuseum.org/art/collection/search/548438" },
    ],
  },
  "mithila": {
    history: "Mithila painting, often called Madhubani painting, is a living tradition from the Mithila region of present-day India and Nepal. It was traditionally painted by women on the walls of homes for occasions such as weddings. In the 1960s many artists began working on paper for sale, and artists including Pushpa Kumari have used the tradition to address contemporary life.",
    effect: "Patterned borders, fine lines, and symbolic details can make several parts of a story readable at once. In the meal scene, repeating food shapes in the border sends the eye back to the table and makes sharing feel central to the image.",
    use: "Use patterns that carry information about a gathering, place, or set of relationships. Choose a few objects from the scene to repeat so the viewer can discover their connection to the subject.",
    why: "Pattern can bind a community scene together and make the relationships around a shared action feel as important as any single face.",
    period: "Mithila and Madhubani painting, historic domestic wall painting and twentieth- and twenty-first-century work on paper and textiles.",
    examples: [
      { label: "Pushpa Kumari and Pradyumna Kumar, Village Life (2015), QAGOMA", href: "https://collection.qagoma.qld.gov.au/objects/22104" },
      { label: "QAGOMA on Pushpa Kumari and the history of Mithila painting", href: "https://collection.qagoma.qld.gov.au/stories/15854" },
    ],
  },
  "rinpa": {
    history: "Rinpa is a Japanese tradition in painting and decorative arts that arose in the early seventeenth century. It takes its name from Ogata Kōrin, a later artist who painted flowers and other natural forms in boldly simplified shapes. His iris screens use mineral colors and gold leaf and refer to a classical Japanese tale about a traveler.",
    effect: "A small number of strong natural shapes can feel expansive against an open metal-leaf ground. In this study the iris clusters mark a rhythm along the lower edge, while the open gold lets you imagine a garden beyond the few visible flowers.",
    use: "Use a repeated natural shape for a quiet passage, a seasonal transition, or a pause in a story. The gaps between clusters can slow the eye down and leave a character room to move.",
    why: "The gaps make the repeated plants feel deliberate and give a viewer a way to follow the figure across a broad surface.",
    period: "Rinpa in Japan, from the early 1600s. Ogata Kōrin worked during the Edo period.",
    examples: [
      { label: "Ogata Kōrin, Irises at Yatsuhashi (Eight Bridges), after 1709, The Met", href: "https://www.metmuseum.org/art/collection/search/39664" },
      { label: "Designing Nature: The Rinpa Aesthetic in Japanese Art, The Met", href: "https://www.metmuseum.org/exhibitions/listings/2012/rinpa-aesthetic" },
    ],
  },
  "photorealism": {
    history: "American Photorealism took shape in the late 1960s and 1970s. Artists such as Richard Estes used photographs to plan carefully rendered paintings of everyday urban scenes. Shop windows interested Estes because a camera could record the objects inside and the reflection of the street at the same time.",
    effect: "Crisp details reward sorting out the scene slowly. Reflections can hold several layers of space in one spot, turning an ordinary office window into a puzzle about who is looking at whom and from where.",
    use: "Use this approach when an ordinary place should feel observed closely. A window or mirror can show an interior and its surroundings in one frame, or suggest distance between a character and the street.",
    why: "Carefully layered reflections make a viewer inspect how a scene is seen, which can be as interesting as the objects themselves.",
    period: "American Photorealism, late 1960s and 1970s.",
    examples: [
      { label: "Richard Estes, Double Self-Portrait (1976), MoMA", href: "https://www.moma.org/collection/works/80047" },
      { label: "Richard Estes, Smithsonian American Art Museum", href: "https://americanart.si.edu/artist/richard-estes-1461" },
    ],
  },
  "harlem-renaissance": {
    history: "The Harlem Renaissance was a flourishing of Black art, writing, music, and intellectual life in the 1920s and 1930s. Aaron Douglas became known for murals and book illustrations that used silhouettes, layered bands of color, and references to African history, including ancient Egypt. His art is one approach within a much wider movement.",
    effect: "Overlapping arcs of light connect people who are doing different things. In the reading-room study, the open book anchors the composition. As the light reaches the students and the musician, learning starts to feel like something the whole neighborhood makes together.",
    use: "Use repeated silhouettes and a connected band of color for a scene about collective action. Give each person a distinct gesture so the audience can see both the group and its individual contributions.",
    why: "Linking scenes of study and performance can make creative life feel like a shared activity rooted in a community.",
    period: "The Harlem Renaissance, especially New York’s Black cultural life in the 1920s and 1930s.",
    examples: [
      { label: "Aaron Douglas, Let My People Go (ca. 1935–39), The Met", href: "https://www.metmuseum.org/art/collection/search/676458" },
      { label: "Reclaiming Ancient Egypt in Harlem, The Met", href: "https://www.metmuseum.org/de/perspectives/reclaiming-ancient-egypt-in-harlem" },
    ],
  },
  "manuscript-illumination": {
    history: "Medieval European book makers used paint, ink, and sometimes gold leaf to decorate handwritten pages. An opening letter with a scene inside is called a historiated initial. A law book made around 1290–1310, now at the Getty, opens one section with a courtroom inside the letter D and a playful musician in the surrounding decoration.",
    effect: "The large letter tells you where to start and gives the main scene a frame. The coffee pot sits along the margin, so it can reward a closer look. The page can carry two story beats at different levels of importance.",
    use: "Use a picture inside a letter for a chapter opening or an illustration that also has to mark the start of a text. A small incident in the margin gives readers a second discovery after they understand the main scene.",
    why: "An illustrated initial can establish the hierarchy of a page and make its border part of the story.",
    period: "Medieval European manuscript arts, with the Getty example from around 1300.",
    examples: [
      { label: "Initial D: Three Men before a Judge (ca. 1290–1310), Getty", href: "https://www.getty.edu/art/collection/object/103SAP" },
      { label: "How to Break Down a Page Like a Medievalist, Getty", href: "https://www.getty.edu/news/breaking-down-a-page-like-a-medievalist/" },
    ],
  },
  "vanitas": {
    history: "Seventeenth-century Dutch painters developed vanitas as a kind of still life that invited reflection on mortality and the limits of possessions and achievement. Objects that measure time or visibly decay could carry the idea. Pieter Claesz paired a skull with objects including a watch and an extinguished lamp in his 1630 example.",
    effect: "The desk objects are larger and closer than the person, so you meet the hourglass and wilted flower first. The closed laptop and removed badge bring the theme into a modern office. Together the objects invite you to think about the time spent working and what remains when work stops.",
    use: "Use a small group of objects to slow down the end of a scene and give it a second meaning. Choose one object that shows time passing and another that tells the reader what mattered to the character.",
    why: "Arranging meaningful objects can make a reader feel the end of a day or an obligation through evidence left on a table.",
    period: "Dutch still-life painting in the seventeenth century, especially vanitas.",
    examples: [
      { label: "Pieter Claesz, Vanitas Still Life (1630), Mauritshuis", href: "https://www.mauritshuis.nl/en/our-collection/artworks/943-vanitas-still-life" },
      { label: "Still-Life Painting in Northern Europe, 1600–1800, The Met", href: "https://www.metmuseum.org/essays/still-life-painting-in-northern-europe-1600-1800" },
    ],
  },
  "kalighat": {
    history: "Kalighat painters worked near the Kali temple in nineteenth-century Kolkata, where workshops sold paintings on paper. Their subjects included religious imagery as well as scenes of fashion, scandal, and social life. In the V&A’s example of a fashionable Bengali babu playing a sitar, a single seated pose carries much of the figure’s character.",
    effect: "The brush line around the bowed back gives the gesture weight. The unoccupied seat stays clear against the bare ground, and Microsoft’s calm pose gives viewers a second reaction to compare. The joke is about the deference given to a position of power.",
    use: "Use an open background and a few expressive poses when a social joke needs to read in one panel. Cover any dialogue and check that the poses and one shared prop still tell you what happened.",
    why: "A clear gesture and an oversized prop can make a social observation land quickly, like one panel of a comic.",
    period: "Kalighat painting in Kolkata, with surviving examples from the 1830s through the early twentieth century.",
    examples: [
      { label: "A babu seated on a chair, playing the sitar (ca. 1870), featured in the V&A’s Kalighat collection guide", href: "https://www.vam.ac.uk/articles/kalighat-painting" },
    ],
  },
  "chaekgeori": {
    history: "In late eighteenth-century Joseon Korea, a still-life genre called munbangdo developed around books and objects associated with scholarly life. Chaekgeori is a term for the bookshelf type, in which a painted case can continue across a folding screen. Books could share the shelves with ceramics, writing tools, or objects brought from elsewhere.",
    effect: "The compartments make it easy to read many small objects in one view. The shelf edges tilt enough to show what rests on them. In this study the worn notebook suggests frequent use, while the ceramics and boxed software give clues to different kinds of collecting.",
    use: "Use a shelf or cabinet to introduce a character through belongings. Give each compartment a visual job and make one object look handled or worn so readers can tell what the person uses most.",
    why: "A carefully chosen object can tell a reader about someone’s interests without a line of speech or a facial close-up.",
    period: "Late Joseon Korea. Scholar’s study painting was established by the 1780s and continued through the nineteenth century.",
    examples: [
      { label: "Books and Scholarly Accoutrements (nineteenth century), The Met", href: "https://www.metmuseum.org/art/collection/search/853896" },
      { label: "Korean Munbangdo Paintings, The Met", href: "https://www.metmuseum.org/essays/korean-chaekgeori-paintings" },
    ],
  },
  "new-objectivity": {
    history: "New Objectivity, or Neue Sachlichkeit, emerged in Germany in the 1920s. The name came from a 1925 exhibition in Mannheim. Painters such as Otto Dix made direct, often unsentimental portraits in which a sitter’s clothes, work, habits, and surroundings offered clues about city life in the Weimar Republic.",
    effect: "Clear contours make the clutter and the sitter equally available to inspect. Microsoft’s gaze still meets yours, but the weight on her hand and the left-behind papers suggest fatigue. The surrounding details let you infer what it costs to look composed at work.",
    use: "Use an exact, restrained portrait when the setting should help tell the truth about a character’s day. Put one detail of posture beside one telling object, then let readers work out what happened.",
    why: "Clear observation and everyday props allow a portrait to register fatigue or tension without a dramatic pose.",
    period: "Weimar-era Germany, especially the 1920s. The New Objectivity exhibition opened in Mannheim in 1925.",
    examples: [
      { label: "Otto Dix, Portrait of the Journalist Sylvia von Harden (1926), Centre Pompidou", href: "https://www.centrepompidou.fr/en/ressources/oeuvre/cjyXKB7" },
      { label: "New Objectivity, MoMA", href: "https://www.moma.org/s/ge/curated_ge/styles/new_objectivity.html" },
    ],
  },
  "wayang-kulit": {
    history: "Wayang is a living Indonesian theatre tradition with several forms. In wayang kulit, a puppeteer moves flat leather figures using rods against a lit screen. Music and storytelling are part of the performance. The British Museum’s twentieth-century example shows the kind of detailed leatherwork a figure can carry.",
    effect: "With the figures reduced to profiles, the position of an arm or a hand becomes easy to read. Small cutouts let light pass through the dark shapes. The folder joins the puppets in the middle so you can understand the handoff from the overall gesture.",
    use: "Use a clear outline and visible gaps to test a comic gesture. Give each figure a distinct profile, then check that the shared object and position of the hands explain the action when the figures are seen only in shadow.",
    why: "A strong outline and a readable prop help a gesture carry across a screen, while tiny holes add decoration inside the shadow.",
    period: "Indonesian wayang shadow theatre is a living tradition. The collection example dates to the 1970s.",
    examples: [
      { label: "Shadow puppet (1970s), British Museum", href: "https://islamicworld.britishmuseum.org/collection/RRM186551" },
      { label: "Wayang puppet theatre, UNESCO", href: "https://ich.unesco.org/en/RL/wayang-kulit-00063" },
    ],
  },
  "orphism": {
    history: "In the 1910s, artists associated with Orphism in Paris explored how color and form could make a still painting feel alive. Sonia Delaunay’s Electric Prisms (1914) takes electric light as a starting point and builds movement from arcs and neighboring colors.",
    effect: "Bright warm colors keep reappearing between cooler passages, which lets your eye feel a rhythm across the square. The street and figure remain recognizable, but the view is organized by what the light feels like as it repeats in the puddles.",
    use: "Use recurring shapes and deliberately spaced color changes when a panel should convey the pace of walking, music, or city light. Keep a few recognizable cues so the reader has an entry point into the more abstract parts.",
    why: "Repeating colors and shapes can suggest movement while the objects they came from recede into the composition.",
    period: "Orphism and related experiments with simultaneous color contrasts in Paris, especially the 1910s.",
    examples: [
      { label: "Sonia Delaunay, Electric Prisms (1914), Centre Pompidou", href: "https://www.centrepompidou.fr/fr/ressources/oeuvre/zS28bfR" },
      { label: "Harmony and Dissonance: Orphism in Paris, 1910–1930, Guggenheim", href: "https://www.guggenheim.org/exhibition/harmony-and-dissonance-orphism-in-paris-1910-1930" },
    ],
  },
  "american-regionalism": {
    history: "American Regionalism gained prominence in the 1930s, when painters including Grant Wood portrayed rural and small-town life, particularly in the Midwest. They often used clearly ordered compositions and recognizable local details. In American Gothic, the house, clothing, and pitchfork help define the people and the place together.",
    effect: "The repair bench and tools make the sitter legible as someone who does a specific job. The houses, telephone poles, and grain elevators connect that job to the town. Hard outlines and repeating shapes give the scene a deliberate, slightly formal quality.",
    use: "Use a local building and a few work objects when place should shape how we understand a character. Choose details the person actually uses or sees every day, then let a wider view show who shares the place.",
    why: "Giving a task a recognizable setting can show how work and community depend on one another.",
    period: "American Regionalism, especially Depression-era painting of the 1930s.",
    examples: [
      { label: "Grant Wood, American Gothic (1930), exhibited at the Whitney Museum of American Art", href: "https://whitney.org/exhibitions/grant-wood" },
      { label: "American Gothic, Getty’s Cultural Objects Name Authority", href: "https://www.getty.edu/cona/CONAFullSubject.aspx?subid=700009447" },
    ],
  },
  "arts-and-crafts": {
    history: "The Arts and Crafts movement took shape in Britain in the later nineteenth century. Designers and makers including William Morris wanted well-made useful objects and valued the skills and labor involved in making them. Morris conceived his first wallpaper, Trellis, in 1862 after a climbing rose in his garden. The printed pattern joins plants and birds to a repeating wooden framework.",
    effect: "The lattice gives the eye a route across the room, while the vines bend and link one repeat to the next. Woods, textiles, and book decoration carry nearby colors and forms. These repeated choices make separate ordinary objects feel as though they belong together.",
    use: "Use a handmade-looking repeating pattern when the way a room is furnished says something about the people who live there. Draw one repeat that can extend past the frame and echo just part of it on a smaller object.",
    why: "A coordinated repeat can make a room feel planned by a maker and connect objects that have different functions.",
    period: "British Arts and Crafts, late nineteenth century, with William Morris’s Trellis conceived in 1862.",
    examples: [
      { label: "William Morris, Trellis wallpaper design (conceived 1862), The Met", href: "https://www.metmuseum.org/art/collection/search/384020" },
      { label: "Arts and Crafts: an introduction, V&A", href: "https://www.vam.ac.uk/articles/arts-and-crafts-an-introduction" },
    ],
  },
  "ballets-russes": {
    history: "Serge Diaghilev launched his Paris ballet season in 1909. The Ballets Russes brought choreographers, composers, and visual artists together, and the clothes and painted scenery helped tell the story along with the dancing. For Parade (1917), Pablo Picasso designed costumes that brought experimental visual art onto the stage.",
    effect: "The opposing poses carry your eye to where the dancers meet. Strong shapes in the costumes echo shapes in the set, while the red folder remains distinct from both. The layout gives a small office task the clarity and excitement of a stage event.",
    use: "Use a clear stage picture when a comic moment needs to read at a distance or in a small panel. Design the costume, backdrop, and prop together, then check whether a reader can still recognize the gesture if the faces are too small to see.",
    why: "Bold stage forms help spectators far from the performers follow a movement as quickly as those near the stage.",
    period: "Ballets Russes design, 1909–1929, including the experimental production Parade in 1917.",
    examples: [
      { label: "Diaghilev and the Ballets Russes, including Picasso’s costume design for Parade (1917), V&A", href: "https://www.vam.ac.uk/articles/diaghilev-and-the-ballets-russes" },
      { label: "Documents concerning Parade, The Met", href: "https://www.metmuseum.org/art/collection/search/752609" },
    ],
  },
  "socialist-realism": {
    history: "Socialist Realism became the official artistic doctrine of the Soviet Union in the 1930s. It used recognizable figures and settings to present an idealized account of society, with workers and collective effort often placed at the center. Vera Mukhina’s Worker and Collective Farm Woman was created for the Soviet pavilion at the 1937 Paris exhibition.",
    effect: "The low viewpoint, large figures, and warm light give routine work a heroic scale. Gestures lead viewers along the racks and imply that everyone is working toward the same end. The composition gives little space to uncertainty, fatigue, or disagreement, which is part of how an idealized image persuades.",
    use: "Use this approach to depict how an institution wants work to be seen, such as a public mural within a story. Compare it with a later scene of the same work from the workers’ viewpoint and ask what the public image selected or left out.",
    why: "A shared direction makes a public message feel assured, which is also a clue that the image emphasizes an ideal.",
    period: "Soviet Socialist Realism after its adoption as official doctrine in the 1930s.",
    examples: [
      { label: "Vera Mukhina, model for Worker and Collective Farm Woman (1937, cast 1965), State Russian Museum", href: "https://rusmuseumvrm.ru/data/collections/sculpture/20/so-797/index.php?lang=en" },
      { label: "Reflections: Socialist Realism and Russian Art, Guggenheim", href: "https://www.guggenheim.org/exhibition/reflections-socialist-realism-and-russian-art" },
    ],
  },
  "pictorialism": {
    history: "Around the turn of the twentieth century, Pictorialist photographers argued that a photograph could be shaped as deliberately as a painting or print. In The Flatiron, Edward Steichen worked color into the print in layers. The Met connects its composition to Japanese woodcuts and its twilight color to Whistler’s Nocturnes.",
    effect: "The lamp and the edge of Microsoft’s profile stay readable, while rain and soft focus let the buildings recede. The restricted amber and blue-gray palette makes waiting feel quiet and suspended. This generated study evokes the look of an early photographic print.",
    use: "Use selective softness and tint when a photograph or photo-like scene should convey the quality of a memory or time of day. Keep one edge clear enough to anchor the viewer as the rest of the scene fades.",
    why: "Soft focus can draw attention to the feeling of a place and make small background distractions recede.",
    period: "Pictorialist photography, especially the late nineteenth and early twentieth centuries.",
    examples: [
      { label: "Edward Steichen, The Flatiron (1904, printed 1909), The Met", href: "https://www.metmuseum.org/art/collection/search/267803" },
    ],
  },
  "deconstructivist-architecture": {
    history: "The 1988 Deconstructivist Architecture exhibition at MoMA brought several architects together around experiments with breaking, shifting, and overlapping familiar building forms. Frank Gehry’s Vitra Design Museum, completed in 1989, gives a built example of a silhouette made from intersecting sculptural forms.",
    effect: "The angled walls, braces, and glass give the lobby several directions at once. Microsoft’s upright stance helps you judge how much the architecture departs from that vertical. A winding red rail gives the otherwise unsettled space a legible path through it.",
    use: "Use competing directions when a room should feel restless, unfamiliar, or challenging to navigate. Give readers a reliable point of reference, such as a person or a continuous railing, so they can still understand the space.",
    why: "Changing the expected angles can turn walking through a lobby into an experience of movement and uncertainty.",
    period: "Deconstructivist architecture in the late twentieth century, including MoMA’s 1988 exhibition.",
    examples: [
      { label: "Deconstructivist Architecture exhibition (1988), MoMA", href: "https://www.moma.org/calendar/exhibitions/1813" },
      { label: "Frank Gehry, Vitra Design Museum (1989), Vitra Campus", href: "https://www.design-museum.de/en/information/vitra-campus.html" },
    ],
  },
  "gutai": {
    history: "Gutai formed in Japan in 1954. Artists in the group explored what happens when bodies, materials, and chance shape the finished work together. At a 1956 Gutai exhibition, Saburō Murakami ran through a series of wooden frames covered with paper. The encounter included the motion, the sound of tearing, and the marks it left behind.",
    effect: "The stretched paper records where the body passed through. Its creases and loose edges keep the action visible even in a still image. The intact wood frame makes the change in the paper easier to see.",
    use: "Use a changed material to tell readers about an action they may not see directly. A torn screen, broken surface, or dragged mark can show where a body went and how forcefully it moved.",
    why: "A change left behind by an action can let a viewer reconstruct an event that is already over.",
    period: "The Gutai Art Association in postwar Japan, active from 1954 to 1972.",
    examples: [
      { label: "Saburō Murakami’s paper-breaking performance (1956), documented in the Artcourt Gallery exhibition guide", href: "https://www.artcourtgallery.com/eng/wp-content/uploads/sites/2/Murakami_Press_en_ss.pdf" },
      { label: "Gutai: Splendid Playground, Guggenheim", href: "https://www.guggenheim.org/exhibition/gutai-splendid-playground" },
    ],
  },
  "ayacucho-retablo": {
    history: "Ayacucho retablos are painted wooden boxes with modeled figures. The tradition grew from portable devotional boxes in the Peruvian Andes. Twentieth-century makers such as Joaquín López Antay became known for retablos that also depict work, celebrations, and everyday life.",
    effect: "The shelves set two moments apart without breaking the link between them. Repeating the computers and the organizer helps the eye recognize that one scene follows the other. The decorated doors turn looking into the box into part of the experience.",
    use: "Use stacked spaces to tell a two-part story in one image. Repeat a person, object, or color across the compartments so viewers can infer what changed without a caption.",
    why: "A box with compartments can hold separate moments that the viewer connects by noticing a recurring prop.",
    period: "Ayacucho retablo making in the Peruvian Andes, including twentieth-century scenes of community life.",
    examples: [
      { label: "Joaquín López Antay, Retablo (ca. 1965–75), Museo de Arte de Lima auction archive", href: "https://lotes.subasta.mali.pe/en/online-auctions/mali--museo-de-arte-de-lima/joaqu-n-l-pez-antay-retablo-ca-1965---1975-8826214" },
      { label: "Peruvian Retablo, Smithsonian Folklife", href: "https://festival.si.edu/storied-objects/peruvian-retablo" },
    ],
  },
  "kinetic-sculpture": {
    history: "Kinetic sculpture uses actual motion as part of the artwork. In the 1930s Alexander Calder began making mobiles, including works that turn with air currents. His large Untitled (1976) hangs in the National Gallery of Art’s East Building, where people can see it from several levels.",
    effect: "A hanging arm balances around its pivot. A lighter piece farther from that point can balance a heavier piece closer to it. Because the parts can turn, the spaces and overlaps between them change as you watch. The wall shadow offers a second pattern.",
    use: "Use a mobile when a quiet scene needs a small sign of movement. Draw the pivot and what hangs from each arm so viewers can imagine the object turning. In a comic, show its shadow shifting across two panels to make the motion visible.",
    why: "A movable sculpture gives viewers a different arrangement each time they return or change their position.",
    period: "Twentieth-century kinetic sculpture, including Calder’s mobiles from the 1930s onward.",
    examples: [
      { label: "Alexander Calder, Untitled (1976), National Gallery of Art", href: "https://www.nga.gov/artworks/56517-untitled" },
      { label: "Calder’s Balancing Acts, National Gallery of Art", href: "https://www.nga.gov/educational-resources/counting-art/calders-balancing-acts" },
    ],
  },
  "land-art": {
    history: "Land Art emerged as a prominent approach in the late 1960s and 1970s. Artists made works whose location and surroundings helped determine how they were experienced. Nancy Holt’s Sun Tunnels uses four concrete cylinders in the Utah desert. The tunnels are aligned with sunrise and sunset at the solstices.",
    effect: "The stone walkway and low horizon guide the view toward the illuminated opening. The effect depends on where the viewer stands and where the sun is. At another hour, the alignment and the shape of the light on the ground would change.",
    use: "Use a site-specific composition when a location itself should tell the story. Choose one event, such as a shadow crossing a threshold, that could only occur at that spot and time.",
    why: "Using a site’s own light or terrain creates an artwork that a viewer experiences through movement and changing conditions.",
    period: "Land Art in the late 1960s and 1970s, with Nancy Holt’s Sun Tunnels completed in 1976.",
    examples: [
      { label: "Nancy Holt, Sun Tunnels (1973–76), Dia Art Foundation", href: "https://www.diaart.org/exhibition/exhibitions-projects/nancy-holt-sun-tunnels-site" },
    ],
  },
  "light-and-space": {
    history: "Light and Space artists working in Southern California in the 1960s and later used light, surfaces, and enclosed rooms to study perception. James Turrell’s early projection Afrum (White) uses light in a corner to create the appearance of a solid white form.",
    effect: "The doorway and floor provide familiar edges that help the viewer gauge nearby space. At the far wall, the violet light softens the joins and makes its apparent depth less certain. The central event is the viewer trying to decide what the light is doing to the room.",
    use: "Use soft light and a few firm edges when a room should feel deeper, calmer, or less measurable. Anchor the near space with something familiar and let the distant edges fade so the audience experiences the difference.",
    why: "When a room gives you few stable edges, noticing how you judge distance can become the subject of the work.",
    period: "Southern California Light and Space art from the 1960s onward.",
    examples: [
      { label: "James Turrell, Afrum (White) (1966), LACMA", href: "https://collections.lacma.org/object/140816" },
      { label: "James Turrell: A Retrospective, LACMA", href: "https://www.lacma.org/art/exhibition/james-turrell-retrospective" },
    ],
  },
  "story-quilt": {
    history: "Quilts have long carried family and community histories through fabric and pattern. In the 1980s, Faith Ringgold developed story quilts that brought painting, cloth, and written narrative together. Tar Beach (1988) places a story about a Black family’s rooftop gathering and a child’s flight within a patterned fabric border.",
    effect: "The large center gives viewers the shared meal at a glance. The small scenes in the border show the week that led up to it. Stitches and repeated star shapes connect moments that otherwise happen in separate places.",
    use: "Use a central image and a narrative border when one event matters most but gains meaning from earlier moments. Repeat a fabric color or small shape to link the side scenes, so readers can recognize a single story even as they look around the edges.",
    why: "A large central scene makes the main event legible while the border can hold smaller stories and memories.",
    period: "Narrative quilting and Faith Ringgold’s painted story quilts of the 1980s onward.",
    examples: [
      { label: "Faith Ringgold, Tar Beach (1988), Guggenheim", href: "https://www.guggenheim.org/learning-through-art/art-investigation/community" },
      { label: "The Reach of Faith Ringgold, Guggenheim", href: "https://www.guggenheim.org/audio/playlist/collection-in-focus-the-reach-of-faith-ringgold" },
    ],
  },
  "acrylic": {
    "history": "Acrylic paints became widely used in the twentieth century. Water-based artist acrylics generally dry quickly, which lets a painter stack passes and revise an edge soon after applying color.",
    "effect": "The dense cobalt covers the color underneath. In a thinner passage, the earlier paint can remain visible. You can use both effects in a single picture.",
    "use": "Use opaque layers to repair a silhouette or change a sign. Use thinner color to connect areas while keeping the earlier marks visible.",
    "why": "Fast-drying layers let an artist alternate between building bold shapes and adjusting their colors with thinner paint.",
    "period": "Twentieth-century acrylic painting.",
    "examples": [
      {
        "label": "Helen Frankenthaler, Mauve District (1966), MoMA",
        "href": "https://www.moma.org/collection/works/80712"
      }
    ]
  },
  "graphite": {
    "history": "Graphite pencils have long served for studies and finished drawings. Graphite can be laid down with ordered strokes, smoothed, or lifted to recover a light.",
    "effect": "Changing stroke density creates value without color. Drawing the darkest tones around the badge gives the white edge somewhere to stand out.",
    "use": "Use graphite when a drawing needs revisions or precise tonal changes. Plan the dark surroundings before adding a bright reflection.",
    "why": "Controlling values lets the same pencil suggest both a dark jacket and a bright object that needs to stand out.",
    "period": "Graphite portrait drawing in nineteenth-century Europe.",
    "examples": [
      {
        "label": "Ingres, Madame Alexandre Lethière and Her Daughter Letizia (ca. 1815), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/337431"
      }
    ]
  },
  "linocut": {
    "history": "In a linocut, a maker removes parts of a linoleum block and inks the surface that remains. The cut areas leave the paper exposed. Picasso used the method for complex layered prints as well as bold shapes.",
    "effect": "The pale lines act like gaps between dark shapes. A strong outer contour still explains the handoff when the image is small.",
    "use": "Use it for posters or decisive comic gestures. Check whether the handoff makes sense before adding small cuts and texture.",
    "why": "A bold carve makes hand gestures and edges easy to read without relying on fine shading.",
    "period": "Twentieth-century relief printmaking, linoleum cut.",
    "examples": [
      {
        "label": "Pablo Picasso, Woman at the Spring, state three (1962, published 1963), MoMA",
        "href": "https://www.moma.org/collection/works/76616"
      }
    ]
  },
  "screenprinting": {
    "history": "Screenprinting pushes ink through open parts of a mesh stencil. A multicolor print can use a different stencil for each color. Registration is how the printer keeps those layers aligned.",
    "effect": "Red and cyan read as a limited palette, with a third look where the layers overlap. Offsets show how even small shifts alter an edge.",
    "use": "Use repeated flat colors for a poster or edition. Decide which overlaps are intentional and which edges need precise alignment for the design to read.",
    "why": "Separate passes make a restrained palette go further. Overlapping two inks can create a third visual accent.",
    "period": "Twentieth-century screenprint editions and Pop Art.",
    "examples": [
      {
        "label": "Andy Warhol, Marilyn Monroe (1967), MoMA",
        "href": "https://www.moma.org/collection/works/61240/"
      }
    ]
  },
  "cyanotype": {
    "history": "Cyanotype is a light-sensitive process known for its deep blue. A contact print can be made by placing objects directly against sensitized paper. Anna Atkins and Anne Dixon used the method to record ferns.",
    "effect": "The same exposure can render an opaque object as a silhouette and a more translucent object as a pale blue form. Overlap changes which details are visible.",
    "use": "Use the contact-print idea to draw attention to an object’s outline or transparency. Arrange items so a reader can tell which shapes overlap.",
    "why": "A contact print records a thing’s outline and translucency together, which can make a small object feel like a specimen.",
    "period": "Nineteenth-century cameraless photography, including British botanical cyanotypes.",
    "examples": [
      {
        "label": "Anna Atkins and Anne Dixon, Cyanotypes of British and Foreign Ferns (1853), Getty",
        "href": "https://www.getty.edu/art/collection/object/107QHX"
      }
    ]
  },
  "egg-tempera": {
    "history": "Egg tempera typically binds pigment with egg yolk. It dries quickly and is often painted over a prepared surface in thin strokes. Andrew Wyeth used tempera for Christina’s World.",
    "effect": "Small neighboring marks build color and light while retaining their edges. Compare the even, matte appearance with the much thicker strokes in the acrylic study.",
    "use": "Use this look when a scene should feel precise and still. Build a transition by changing the density and tint of small strokes.",
    "why": "Separate small marks give a painter close control over changes in tone, which helps when tiny details matter.",
    "period": "Egg tempera on panel, from historical European practice to twentieth-century painting.",
    "examples": [
      {
        "label": "Andrew Wyeth, Christina’s World (1948), MoMA",
        "href": "https://www.moma.org/collection/works/78455/"
      }
    ]
  },
  "etching": {
    "history": "In etching, a needle exposes metal through a protective coating. Acid bites the exposed lines, which then hold ink for printing. Rembrandt’s The Three Trees also uses engraving and drypoint, so it shows how several metal-plate techniques can work together.",
    "effect": "Dark lines can remain fine and freely drawn. They accumulate into shade, while unprinted sections keep bright surfaces separate.",
    "use": "Use etched line where machinery, branches, or architecture need fine detail. Save the densest hatching for places that need particular depth or weight.",
    "why": "Thin grooves can give a print the precision of a drawing, with enough independent marks to describe machinery or cloth.",
    "period": "European intaglio printmaking, including seventeenth-century Dutch etching.",
    "examples": [
      {
        "label": "Rembrandt, The Three Trees (1643), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/354633"
      }
    ]
  },
  "lithography": {
    "history": "Traditional lithography uses a flat surface such as limestone. A greasy drawing attracts printing ink, and dampened blank areas repel it. Nineteenth-century artists such as Honoré Daumier used the medium to publish prints.",
    "effect": "Broad black areas, grainy gray, and untouched paper can all appear in one impression. The gray can look rubbed or drawn rather than built up from individual lines.",
    "use": "Use a crayon lithography look when you want a printed scene to preserve broad, soft marks. Reserve sharper edges for the places where the reader should look first.",
    "why": "It keeps subtle drawn textures visible across an edition of prints, which is useful when an even gray would feel too flat.",
    "period": "Lithography in nineteenth-century French print culture.",
    "examples": [
      {
        "label": "Honoré Daumier, Rue Transnonain, April 15, 1834 (1834), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/359156"
      }
    ]
  },
  "buon-fresco": {
    "history": "In buon fresco, the painter applies pigments to fresh lime plaster. As the plaster sets, it binds the pigments into the wall. Because the surface must stay wet, painters can plan the work in separate sections called giornate.",
    "effect": "Large forms and matte colors remain legible on a wall. The order in which the painter applies plaster can also affect where shapes and edges meet.",
    "use": "Use the fresco comparison for a scene designed around a particular wall. Plan large forms from a distance, then consider where you would divide the work into sections.",
    "why": "Planning one wet area at a time helps an artist coordinate a large scene that will be read at a distance.",
    "period": "Wall painting on wet lime plaster, including twentieth-century murals.",
    "examples": [
      {
        "label": "Diego Rivera, Detroit Industry Murals (1932–33), Detroit Institute of Arts",
        "href": "https://dia.org/collection/detroit-industry-murals/58537"
      }
    ]
  },
  "pen-and-ink": {
    "history": "Pen and ink can range from fine lines made with a narrow pen to broader marks made with a reed pen or brush. Rembrandt’s ink drawings show how a few lines can carry both detail and movement.",
    "effect": "Line thickness helps separate a figure from the background. Parallel or crossed strokes can add shadow without the dark patch swallowing the handoff.",
    "use": "Use strong outlines for a prop or action that must read quickly. Reserve finer lines for fingertips and other details that would feel heavy in solid black.",
    "why": "A few heavy marks establish the action quickly, leaving fine marks available to show touch, texture, or detail.",
    "period": "Pen and ink drawing across periods, with a seventeenth-century Dutch example.",
    "examples": [
      {
        "label": "Rembrandt, Cottage among Trees (ca. 1650), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/337491"
      }
    ]
  },
  "ink-wash": {
    "history": "Brush painters across East Asia used diluted ink to build a range of tones. Sesshū Tōyō studied painting in China and carried forward Japanese Muromachi ink traditions. In his 1495 landscape, pooled and broken marks suggest terrain with few enclosing outlines.",
    "effect": "A dark wash anchors the figure. Paler washes let the window and distant buildings emerge gradually, and gaps in the brushwork let the paper supply light.",
    "use": "Use wash when changes in light or distance should carry the mood. Keep the darkest ink near the gesture you want the reader to notice first.",
    "why": "A small change in the amount of water lets one ink suggest weight, translucency, and distance.",
    "period": "East Asian brush painting, with an example from Muromachi Japan, 1495.",
    "examples": [
      {
        "label": "Sesshū Tōyō, Landscape in Broken Ink (1495), Tokyo National Museum",
        "href": "https://www.tnm.jp/modules/r_collection/index.php?colid=A282&controller=dtl&lang=en&t=now"
      }
    ]
  },
  "documentary-photography": {
    "history": "During the Great Depression, Dorothea Lange photographed agricultural workers for a U.S. government relief program. She moved closer across several exposures of Florence Owens Thompson and her children. Thompson later disputed parts of Lange’s account, showing how a caption can shape the meaning of a photograph.",
    "effect": "A camera at bench height gives the tools and hands room in the frame. The people near its edges suggest a shared workspace. A caption can supply verified context that the photograph alone cannot establish.",
    "use": "Use documentary photography when the conditions around an event matter to the story. Check who, where, and when for the caption, and label staged or generated studies clearly so readers can judge what the image establishes.",
    "why": "A carefully chosen frame can show how work happens, while a verified caption supplies the time, place, and circumstances a viewer cannot infer.",
    "period": "Documentary practice across periods, with a U.S. Depression-era example from 1936.",
    "examples": [
      {
        "label": "Dorothea Lange, Migrant Mother, Nipomo, California (1936), MoMA",
        "href": "https://www.moma.org/collection/works/50989"
      }
    ]
  },
  "greek-vase-painting": {
    "history": "Athenian vase painters worked with both techniques in the late sixth century BCE. Some vessels used both on opposite sides. The Boston amphora gives viewers two versions of the same scene, Achilles and Ajax playing a game.",
    "effect": "Black figures make the handoff read as two dark silhouettes. The red-figure rendering leaves more room for interior brush lines to describe knees, fingers, and folds.",
    "use": "Use this paired study to see what changes when you keep a gesture fixed and reverse where dark and light sit. A clear silhouette helps a small image read quickly, while interior lines help describe a complicated pose.",
    "why": "Reversing which shapes are dark changes what a viewer sees first. It also changes how easily the artist can show a bend in fabric or a small gesture.",
    "period": "Archaic Greek pottery, Athens, late sixth century BCE.",
    "examples": [
      {
        "label": "Two-handled jar with Achilles and Ajax (ca. 525–520 BCE), Museum of Fine Arts, Boston",
        "href": "https://collections.mfa.org/objects/153408"
      }
    ]
  },
  "mughal-album-painting": {
    "history": "The Shah Jahan Album began under the Mughal emperor Jahangir and grew under Shah Jahan. Its folios brought together individual portraits, studies of plants and animals, and calligraphy. Nanha’s portrait of Maharaja Bhim Kanwar sets an identifiable profile amid delicate flowers.",
    "effect": "The profile makes the sitter’s attention legible. The plain field gives the sprig space at the center, and the ornament draws the eye around the margins at a slower pace.",
    "use": "Use an album-page composition for a portrait the reader should study at close range, especially when a specimen or personal object reveals what the sitter cares about.",
    "why": "A small held object can characterize a sitter, while the border gives the portrait a slower rhythm.",
    "period": "Mughal court culture in South Asia, early seventeenth century.",
    "examples": [
      {
        "label": "Nanha, Portrait of Maharaja Bhim Kanwar (ca. 1615–29), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/451265"
      }
    ]
  },
  "french-realism": {
    "history": "Mid-nineteenth-century French Realists made contemporary life and ordinary labor subjects for serious painting. Jean-François Millet showed three women gathering leftover grain in The Gleaners, exhibited at the Paris Salon in 1857.",
    "effect": "Two bent figures and a crowded bench keep the viewer close to the work. The muted colors and rough textures make the chipped wall and worn sleeves part of the story.",
    "use": "Use this approach when a character’s skill or effort should define the scene. Show the tools, gestures, and wear that tell the reader what the task costs in time or attention.",
    "why": "Putting ordinary labor at the center gives skill and physical effort the attention a formal portrait might give rank.",
    "period": "French Realism, mid-nineteenth century.",
    "examples": [
      {
        "label": "Jean-François Millet, The Gleaners (1857), Musée d’Orsay",
        "href": "https://www.musee-orsay.fr/en/artworks/des-glaneuses-342"
      }
    ]
  },
  "swiss-style": {
    "history": "The International Typographic Style took shape in mid-century Switzerland. Designers such as Josef Müller-Brockmann and Armin Hofmann used grids, sans serif lettering, and photography. In Der Film, Müller-Brockmann makes scale and the crop of the title carry the poster.",
    "effect": "A shared alignment connects pieces that sit far apart. Large type tells you what the event is, while smaller type gives you the details to act on it.",
    "use": "Use the grid for a public notice, map, or schedule people need to scan. Assign a size and position to each level of information so a glance can tell readers where to start.",
    "why": "A common alignment helps unfamiliar readers scan a schedule or notice and quickly decide what to do next.",
    "period": "International Typographic Style, Switzerland, 1950s–60s.",
    "examples": [
      {
        "label": "Josef Müller-Brockmann, Der Film (1960), MoMA",
        "href": "https://www.moma.org/collection/works/4882"
      }
    ]
  },
  "carved-relief": {
    "history": "Carved relief appears across many cultures. Sculptors at the Northwest Palace at Nimrud cut figures into gypsum alabaster panels and incised tiny details in their clothing. The Met notes that the panels originally carried paint, very little of which survives.",
    "effect": "Shallow edges catch bright light on one side and cast short shadows on the other. A groove can suggest a fold or finger without needing the whole form to project.",
    "use": "Use low relief for a scene that should read across a wall or object while preserving its surface. Try lighting the panel from the side to make slight changes of depth easier to see.",
    "why": "Shallow carving lets a scene belong to a wall or object. Side lighting can make even a small step in depth readable.",
    "period": "Sculptural method with a Neo-Assyrian example from ninth-century BCE Nimrud.",
    "examples": [
      {
        "label": "Northwest Palace relief panel (ca. 883–859 BCE), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/321613"
      }
    ]
  },
  "ceramic-glazing": {
    "history": "Korean Goryeo potters developed refined blue-green celadon glazes and used them over incised and carved decoration. The Met’s twelfth-century stoneware jar shows how a pattern can remain visible beneath a translucent glaze.",
    "effect": "Glaze is a coating that fuses to the clay in firing. A translucent glaze can emphasize a groove where it gathers more thickly, while the broad reflection on the shoulder reveals the vessel’s curve.",
    "use": "Use a translucent glaze when you want a vessel’s surface to reveal small carved details as it turns. Plan the lip, shoulder, and foot alongside the pattern because each draws light differently.",
    "why": "A translucent glaze lets the shape of the vessel and the depth of its carved lines both contribute to the finished color.",
    "period": "Glazed ceramics across periods, with a twelfth-century Korean Goryeo example.",
    "examples": [
      {
        "label": "Incised stoneware jar with celadon glaze (first half of the 12th century), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/57405"
      }
    ]
  },
  "vector-illustration": {
    "history": "Commercial tools such as Adobe Illustrator, released publicly in 1987, helped bring scalable digital paths into everyday design and illustration. In a vector file, points and curves define a shape so it can be redrawn at different sizes.",
    "effect": "Crisp joins and flat fills separate the figure and tools. Reusing a curve or circle makes shapes feel related even when they represent different things.",
    "use": "Choose vectors when a drawing needs reusable parts or must work at several sizes, such as a comic’s recurring props or a set of icons. Reusing paths keeps the edges and proportions consistent.",
    "why": "A motif built from reusable curves stays clear at several sizes, which helps icons, props, and lettering stay consistent.",
    "period": "Digital illustration, with a desktop publishing milestone in 1987.",
    "examples": [
      {
        "label": "Adobe Illustrator public release (1987), Adobe",
        "href": "https://blog.adobe.com/en/publish/2015/03/23/adobe-explains-it-all-illustrator"
      }
    ]
  },
  "stylized-3d": {
    "history": "Computer animation separates the model, the camera, surfaces, and lighting. Pixar’s Luxo Jr., shown at SIGGRAPH in 1986, used modeled desk lamps and light to make a simple cast read as characters.",
    "effect": "Rounded geometry makes the forms easy to read from an angle. Highlights suggest what each surface is made of, and contact shadows help objects feel as though they have weight.",
    "use": "Use stylized 3D when you want to revisit a set from several angles or show the same objects under different light. A consistent model helps readers recognize the objects from shot to shot.",
    "why": "The same model and props can stay recognizable across camera angles while the light changes the mood of a scene.",
    "period": "Computer graphics and animation, with a 1986 example from early Pixar.",
    "examples": [
      {
        "label": "Pixar, Luxo Jr. (1986)",
        "href": "https://www.pixar.com/luxo-jr/"
      }
    ]
  },
  "batik": {
    "history": "In Indonesian batik, makers apply hot wax to reserve areas of cloth from dye and repeat the process for additional colors. Patterns have different uses and meanings across communities and occasions. UNESCO inscribed Indonesian Batik in 2009.",
    "effect": "Tiny reserved marks let the pattern flow across larger color fields. The repeat makes the cloth readable even when a garment folds or partly covers the design.",
    "use": "Use wax resist when you want the cloth itself to shape the design, for example when a repeat should stay recognizable as the fabric moves. For an Indonesian reference, look at a specific textile and its context before interpreting its pattern.",
    "why": "A repeated pattern can remain recognizable as fabric folds or moves, while fine reserved marks reward a closer look.",
    "period": "Living Indonesian textile tradition. The linked cloth is from Java, nineteenth to early twentieth century.",
    "examples": [
      {
        "label": "Javanese batik cloth (19th to early 20th century), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/771332"
      },
      {
        "label": "Indonesian Batik (inscribed 2009), UNESCO",
        "href": "https://ich.unesco.org/en/RL/indonesian-batik-00170"
      }
    ]
  },
  "maya-painted-ceramics": {
    "history": "Classic Maya potters painted drinking vessels with figures and ornaments in colored slip, a mixture based on clay. A Chamá-style vessel at The Met shows a court scene framed by bands and was made in what is now Guatemala. Such vessels took part in feasting, gift exchange, and burial.",
    "effect": "A shared baseline joins the figures, while a glance or reaching hand pulls your eye into the next part of the scene. An unwrapped view lets you follow those connections across the surface.",
    "use": "Use a wraparound layout when turning an object should reveal the story in stages. Give the end and the beginning a shared line or repeated shape so the join reads smoothly.",
    "why": "A wraparound design can let a viewer discover a story physically, one exchange at a time.",
    "period": "Classic Maya, with a Chamá-style example from ca. 600–900 CE.",
    "examples": [
      {
        "label": "Chamá artist(s), Vessel with throne scene (600–900 CE), The Met",
        "href": "https://www.metmuseum.org/art/collection/search/318662"
      }
    ]
  },
  "stop-motion": {
    "history": "Stop-motion animators move a physical puppet or object in small steps and photograph the result one frame at a time. For Coraline, LAIKA used different-sized puppets and printed replaceable faces to get a range of poses and expressions.",
    "effect": "A fixed view keeps attention on what moved. Small pose changes suggest continuous motion, while repeating a pose over several frames makes a pause feel intentional.",
    "use": "Use stop-motion when a puppet’s fabric, tools, or surroundings should feel tangible. Plan the spacing between poses to control whether a reach feels hesitant, quick, or deliberate.",
    "why": "Controlling the spacing between poses, and choosing when to hold one, gives a small movement a sense of hesitation or purpose.",
    "period": "Frame-by-frame puppet animation, with an American feature-film example from 2009.",
    "examples": [
      {
        "label": "LAIKA, Coraline production materials (2009)",
        "href": "https://www.laikahiddenworlds.com/coraline"
      }
    ]
  },
  "plotter-art": {
    "history": "Early computer artists such as Vera Molnár used rules and controlled changes to explore visual order. A plotter follows commands to move a real pen across paper. Molnár’s Molndrian is a plotter drawing from 1974.",
    "effect": "Lines close together appear darker and accentuate the curve of a face or a lens. Repeated paths make small deviations clear because you have a pattern to compare them with.",
    "use": "Use a repeatable drawing rule when you want to explore how a single change alters the whole image. Adjust one input, such as the distance between lines, to see where the effect is strongest.",
    "why": "A repeatable rule lets you change spacing or direction in a controlled way and see exactly what it does to the image.",
    "period": "Algorithmic drawing and early computer art, with a 1974 pen plotter example.",
    "examples": [
      {
        "label": "Vera Molnár, Molndrian (1974), MoMA",
        "href": "https://www.moma.org/collection/works/417832"
      }
    ]
  },
  "game-nes": {
    "history": "Nintendo’s Famicom arrived in Japan in 1983, and the NES reached North America in 1985. Artists composed worlds from repeating tiles and built characters from small movable images called sprites. A single hardware sprite had three visible colors, with layering available to add more.",
    "effect": "A few contrasting pixel clusters make the bun, jacket, and hands legible at a glance. Repeated tiles and sparse color give the room a strong rhythm.",
    "use": "Use an 8-bit approach for tiny characters or a deliberately spare arcade look. Test the sprite at its intended size. A distinctive outline survives when facial details disappear.",
    "why": "A small sprite with a clear outline can keep its identity even when it has very little screen space.",
    "period": "1980s home consoles. Nintendo’s Super Mario Bros. was part of the North American NES launch in 1985.",
    "examples": [
      {
        "label": "Nintendo of America, NES launch history",
        "href": "https://press.nintendo.com/CompanyHistory"
      }
    ]
  },
  "game-snes": {
    "history": "The Super Famicom launched in Japan in 1990 and the Super NES in North America in 1991. Its richer palette and multiple background layers gave artists more ways to separate scenery, characters, and effects.",
    "effect": "Steps from dark blue to mid-blue and pale highlights round off a sleeve while keeping the pixel grid visible. A quieter palette on distant scenery gives the foreground more contrast.",
    "use": "Use this look for a side-view scene where the eye should pick out detailed props and characters quickly. Keep the strongest color contrast around the action.",
    "why": "Extra shades let a designer show more of a place while keeping the controls, character, and path visible at a glance.",
    "period": "Early to mid-1990s console pixel art. Super Mario World was bundled with the North American Super NES in 1991.",
    "examples": [
      {
        "label": "Nintendo of America, Super NES launch history",
        "href": "https://press.nintendo.com/CompanyHistory"
      }
    ]
  },
  "game-playstation-2d": {
    "history": "2D sprite games continued on the original PlayStation even as the console made real-time 3D common. Konami’s Castlevania: Symphony of the Night (1997) is a prominent example of detailed 2D character art and atmospheric environments from that period.",
    "effect": "A larger sprite can show a clearer expression and more specific hand gestures. Separate foreground and background layers create depth and provide room for lighting effects.",
    "use": "Use this look when drawn poses and carefully composed backgrounds matter, especially in a side-scrolling game where you want the character to read against busy scenery.",
    "why": "Detailed drawn poses can make small movements and expressions readable while keeping the view of a game world easy to follow.",
    "period": "Original PlayStation, mid-to-late 1990s. Castlevania: Symphony of the Night was released in 1997.",
    "examples": [
      {
        "label": "Konami, Castlevania: Symphony of the Night (1997)",
        "href": "https://www.konami.com/games/castlevania/us/en-us/page/history_1997_ps"
      }
    ]
  },
  "game-playstation-low-poly": {
    "history": "Final Fantasy VII (1997) paired simple real-time character models with detailed pre-rendered backgrounds in many exploration scenes. A pre-rendered background is an image made ahead of time and displayed behind the moving model.",
    "effect": "Big geometric shapes make elbows, hair, and boots readable from a distance. The backdrop can establish the place with more detail because the camera angle is fixed.",
    "use": "Use this look for a fixed-camera adventure where a small cast moves through carefully composed rooms. Put visual detail in the places the player needs to notice.",
    "why": "A fixed view lets artists put detail into scenery and guide a player’s eye while keeping the moving figure economical to render.",
    "period": "Original PlayStation role-playing games, late 1990s.",
    "examples": [
      {
        "label": "PlayStation, Final Fantasy VII (1997) and the original PlayStation",
        "href": "https://www.playstation.com/en-us/playstation-history/1994-ps-one/"
      },
      {
        "label": "Hironobu Sakaguchi on pre-rendered backgrounds in Final Fantasy VII (2023 interview)",
        "href": "https://fullfrontal.moe/hironobu-sakaguchi-magic/"
      }
    ]
  },
  "game-fighting-3d": {
    "history": "Tecmo’s original Dead or Alive debuted in arcades in 1996 and came to PlayStation in 1998. Fighting games gave full-body poses and readable motion a large share of the screen.",
    "effect": "Full-body framing makes weight shifts visible. Smooth shading softens the surfaces between polygon vertices, while angular outlines still show how the figure is built.",
    "use": "Use this look when stance, timing, and spacing tell the story. Favor clear silhouettes and keep both feet visible at key moments so a pose is easy to read.",
    "why": "When action depends on stance and timing, the viewer needs a clear view of limbs and balance as much as detail in the face.",
    "period": "Mid-to-late 1990s arcade and console 3D. This branch of game art overlapped with low-poly RPGs.",
    "examples": [
      {
        "label": "Koei Tecmo, history of the original Dead or Alive (1996 arcade debut)",
        "href": "https://www.koeitecmo.co.jp/e/ir/docs/ird1_20250212e.pdf"
      }
    ]
  },
  "game-ps3-ps4": {
    "history": "PlayStation 3 launched in 2006. Across the PS3 and PS4 generations, artists could make denser models and layer more surface information into textures. Normal maps are one common way to make small bumps and scratches respond to light without modeling each one.",
    "effect": "More geometry helps round the face, hands, and upholstery. Painted or mapped details help materials read at close range, while lighting baked into a scene can preserve its atmosphere at lower rendering cost.",
    "use": "Use this approach when the character must hold up in medium shots and the environment needs to run smoothly. Put geometry into the silhouette and finer detail into surface maps.",
    "why": "Modeling a clear outline and mapping smaller marks onto surfaces can give a scene detail while leaving more resources for the action.",
    "period": "HD console 3D from the PS3 and PS4 generations, beginning in 2006 and 2013.",
    "examples": [
      {
        "label": "PlayStation, PlayStation 3 and the HD console era",
        "href": "https://www.playstation.com/en-us/playstation-history/2007-ps3-ps-vita/"
      },
      {
        "label": "PlayStation, PlayStation 4 (2013)",
        "href": "https://www.playstation.com/en-us/playstation-history/2013-ps4-ps-vr/"
      }
    ]
  },
  "game-ps5-ray-tracing": {
    "history": "PlayStation 5 launched in 2020. Some games used ray tracing to calculate particular light effects. For Marvel’s Spider-Man Remastered, Insomniac highlighted ray-traced reflections and ambient shadows.",
    "effect": "Tracing rays through a scene can account for objects beyond the camera frame when they appear in a reflection. Rough surfaces spread the reflection, while smooth surfaces keep it sharper.",
    "use": "Use this look when reflected objects, metal, glass, or changing light carry information about the scene. Compare what the reflection reveals with what the camera can see directly.",
    "why": "Reflections help players judge what objects are made of and can reveal parts of a space outside the camera’s current view.",
    "period": "2020s console graphics. Insomniac documented ray-traced effects for its 2020 PS5 remaster.",
    "examples": [
      {
        "label": "Insomniac Games, Marvel’s Spider-Man Remastered graphics (2020)",
        "href": "https://blog.playstation.com/2020/09/30/marvels-spider-man-remastered-detailed/"
      }
    ]
  },
};
