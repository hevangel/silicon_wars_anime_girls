# Cel-shaded 3D manga rendering (#65)

**Stage:** style YAML + per-character identity contracts + material swatch shader generator. No AMD/Intel mesh, skeletal rig, VRM asset or finished render is claimed approved.

## Reference and 3D pipeline

1. Audit [AMD](../../characters/amd/character_sheet.png) and [Intel](../../characters/intel/character_sheet.png) approved model sheets. Record logo-free hair/face/shoulder/prop silhouette and adult proportions as 3D constraints.
2. Model a simple proxy, then a properly topology-mapped model for each. Test 0°, 90°, 180°, 270° at orthographic neutral light. AMD's braided ponytail must have volume and avoid intersecting her shoulders/headphones; Intel crown must clear long hair and epaulette support must be plausible.
3. Define material-specific dark/mid/light ramps, never interpolate between bands for the standard shader. `workflows/cel_shaded_3d/material_presets.json` holds proposal swatches, not approved materials.
4. Use Eevee-only Shader-to-RGB + constant three-stop ColorRamp to create flat shading. Explicitly choose **separate** outline method and pixel width at 256,512,1024 target render sizes. Outline width that works at 1024 may vanish in a mobile preview.
5. Create rig-friendly seams and silhouette deformation; blendshapes for neutral/grin/skeptical/anger as needed. Do not conflate art style with skeleton animation, VRM capture or output video.
6. Compose a neutral and dramatic light pair with **unchanged** geometry/material identities. Test expression and camera variations independently. Show before/after manga vs 3D screenshots and all four angles in a review PR.
7. Export glTF or VRM **only** when real model topology, bone layout, humanoid mapping, license metadata and target runtime support have been tested; document the Blender version and generator/tool revision.
8. Apply human review for face, crown/headphone position, adult body shape, color ramps, camera-dependent outlines, outfit continuity, and age-appropriate depiction.

## Reproducible swatch project

The script creates a **Blender material-preview scene**, not an Intel/AMD model:

```sh
python -m unittest discover -s tools -p test_toon_profile.py
blender --background --python tools/blender_toon_shader.py -- \
  --character amd --output /tmp/amd-toon-materials.blend
```

The scene contains material swatch spheres with a neutral lighting rig, three-step color bands and a camera. Replace with actual approved mesh only after review. Blender Eevee required for Shader-to-RGB; Cycles will not match. `material_presets.json` defines the ramp budget, thresholds and per-character material slots. Blender version and render engine are recorded in the source .blend.

## Quality checks

| Test | What can fail | Gate |
| --- | --- | --- |
| 0/90/180/270° | braid/crown/coat silhouette disappears | art director |
| Model topology | crown intersects hair or headphones clip | modeler |
| Cell shading | soft gradient creeping into materials | shader reviewer |
| Pixel outline | line weight inconsistent across camera distance | target-resolution screenshots |
| Expressions | face changes or loses adult design | character continuity reviewer |
| Exports | glTF/VRM loses materials or humanoid rig | explicit runtime test |

**Troubleshooting:** if Shader-to-RGB is missing, switch Blender engine to Eevee; if bands are uneven, adjust thresholds and key light; if outlines wobble, test mesh-normals and camera-scaled thickness; if material highlights look metallic on skin, use independent skin ramp. Neither palette JSON tests nor a generated shader demo count as human visual approval.

Resources: [Blender](https://www.blender.org/), [glTF 2.0](https://www.khronos.org/gltf/), [VRM](https://vrm.dev/en/).
