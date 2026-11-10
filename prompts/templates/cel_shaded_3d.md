# Cel-shaded 3D art-direction prompt

This template creates a **3D rendering style specification**, not an animation rig. It must not rewrite approved identity. Key inputs are `characters/<id>/continuity.yaml`, a real approved 2D model sheet, the per-character style override and `workflows/cel_shaded_3d/material_presets.json`.

## Blocks

**Identity fixed:** AMD = adult, red braided high ponytail, amber eyes, headphones, red/black chiplet gear, athletic body language. Intel = adult, long ice-blue hair, sapphire eyes and pointed *unbranded* sapphire crown, royal-blue/cream imperial military uniform, gold epaulettes, white gloves, wafer and skirt hem logo.

**Model fixed after approval:** orthographic neutral 0/90/180/270° turnaround, hair volume and silhouette read at 1×, clean face and hand topology, support for crown, gloves, coats, armored panels and physical props. Version model and rig separately.

**Shader adjustable:** three discrete bands (shadow, midtone, lit), deliberate per-material ramps, cel-edge 1.5–3 px *at actual final resolution*, stable rim highlights, coherent ambient floor shadow. Do not fall back to smooth photoreal gradient. Shader change must not alter face geometry.

**Scene adjustable:** camera orthographic or calibrated perspective, lens, character pose, expression blendshapes, key/fill, color grade and background, but separate from the shader palette definition.

### AMD 3D model-turnaround prompt

Design an original adult anime 3D AMD Crimson Challenger preserving her high braided *red* ponytail silhouette and amber eyes, with matte black/crimson segmented chiplet jacket, headphones at collar, fingerless gloves, practical boots and unambiguously athletic stance. A model-ready clean mesh; cloth and armor have independent deformation zones. Flat three-step shadow ramps with separate red material highlights and stable 2-pixel target outline. Show 0°,90°,180°,270° with neutral orthographic camera and one expressive face/hand detail, no full-scene FX.

### Intel 3D model-turnaround prompt

Original adult anime 3D Intel Blue Empress with long **light-blue** hair, sapphire-eyed face, clear blue crown above hair, royal-blue/cream military coat, gold epaulettes and wafer heirloom, one small Intel Inside emblem on lower left front skirt, none on crown. Model standing dignified with solid boots and supported coat panels. Three-band toon ramp for blue fabric/ice hair, gold and skin; silhouette stable from all 4 angles.

## Negative constraints

No chibi proportions, no photo realism, no semitransparent manga eye geometry swap, no reused AMD/Intel pose, no identical face models, no crown text, no blue-haired AMD, no red-haired Intel, no smoothing of lighting bands, no visually important geometry as floating shader hallucination, no VRM claim absent export tests, no 3D character approval from shader swatch alone.

## Workflows

Use Blender Eevee Shader-to-RGB + constant ColorRamp for material preview, explicit outline method (inverted hull mesh or image-space compositing), versioned shader preset, then test real character geometry at close-up and full body. Separate Blender source, shader definitions, optional rig and glTF/VRM exports. Blender script creates **material swatches only**, never fake approved character meshes.
