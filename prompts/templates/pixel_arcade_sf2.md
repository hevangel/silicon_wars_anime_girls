# Pixel-native 1990s arcade style — reusable prompt

This is an **original** pixel-art rendering mode, not a Street Fighter II character recreation. Source identity: `characters/<character>/continuity.yaml` + approved `character_sheet.png` + `styles/pixel_arcade_sf2.yaml`. Do not use an old chat-based description instead of the locked model.

## Prompt composition

1. **Identity block (immutable):** paste the continuity lock verbatim, including hairstyle, eye color, age, logo location, costume, signature prop.
2. **Style block (immutable):** `pixel_arcade_sf2`, 96×128 native transparent RGBA canvas (or declared 128×160), limited 16–32 opaque colors, clear clustered pixels, 1–2 px selective outlines, upper-left key light, no antialiasing; adult proportions.
3. **Scene block (editable):** exact stance, expression, camera (front, profile, back, 3/4), action, raised arm, gaze. Pose and camera never rewrite identity.
4. **Export block:** one frame only; fixed feet anchor, integer pixel coordinates; alpha in {0,255}; approved palette and cropped transparent bounding rectangle with padding.

### Master prompt: AMD

Original arcade fighting-game **pixel-native character sprite**, one adult woman in asymmetrical low forward lunge, full body on a 96×128 transparent grid. **AMD — Crimson Challenger:** fiery red *braided* high ponytail, amber eyes, headphones around neck, black/crimson segmented chiplet tactical jacket, fingerless gloves, modular chiplet design, one planted boot. Aim for collectible 1990s arcade portrait-craft: deliberately hand-placed pixel clusters, strong shoulder/boot/ponytail silhouette, 24-color controlled material ramps, 1–2 pixel outlines. Consistent upper-left lighting. Master sprite only, not a screenshot, scene, character collage, or downscaled painting.

### Master prompt: Intel

Original arcade pixel sprite, 96×128 native, adult commanding upright stance, long light-blue hair, sapphire-blue eyes, **unbranded pointed sapphire crown**, royal-blue/cream military coat, gold epaulettes, white gloves, wafer heirloom, subtle Intel Inside hem emblem. Distinct silhouette and pose from AMD; upper-left lighting and 28-color hard cluster ramps. Centered feet anchor, 1–2 px selective outlines, transparent background.

## Negative constraints

NO existing game character, recognizable Street Fighter costume, Ryu/Chun-Li likeness, pixelated high-resolution anime, blurry edges, interpolation, photographic details, gradients, excessive dithering, more than 32 visible colors, semi-transparent edge pixels, wrong hair color, mixed character outfits, missing props, unreadable silhouette, source logos on crown, floating unsupported feet, disembodied armor, repeated mirrored poses, generated sprite sheet before master approval.

## Model/tool-specific notes

Image generators often emit antialiased pictures that only *look* pixelated. Treat generator output as **draft reference**, inspect at 1× and 8× nearest-neighbor zoom, and reconstruct the true master at the intended native pixel resolution in Aseprite/LibreSprite/Piskel. Never claim numerical palette reduction alone made the result a high-quality sprite. Complete AMD master approval before animation batch, then do Intel master and side-by-side continuity.

## Sheet prompts

- **Model reference sheet:** separate panels for front, three-quarter, side, back, face close-up, identity swatches, attack stance; pixel-native at individually allocated resolutions. Text labels added *outside* sprite pixels. Do not upscale a manga turnaround.
- **Motion sheet:** derive frames from approved source only; frame IDs, identical canvas geometry, anchor and hitbox fields, no more than 32 colors, separate hand-drawn inbetweens.
- **Motion authoring:** pixel frames are source art; skeletal limb reassembly is optional and must use distinct layers; do not conflate style with animation technique.
