#!/usr/bin/env python3
"""Create an EEVEE toon material *swatch* scene, not an approved character model.

Run: blender --background --python tools/blender_toon_shader.py -- --character amd --output /tmp/amd-toon.blend
"""
import argparse
import json
import sys
from pathlib import Path


def hex_to_linear_rgb(hex_color):
    values = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    return tuple(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
                 for v in values) + (1.0,)


def main():
    import bpy

    parser = argparse.ArgumentParser()
    parser.add_argument("--character", choices=["amd", "intel"], required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    source = Path(__file__).resolve().parents[1] / "workflows/cel_shaded_3d/material_presets.json"
    config = json.loads(source.read_text(encoding="utf-8"))
    if len(config["thresholds"]) != 2:
        raise ValueError("Expected two ramp thresholds")
    # The rendering nodes below require an Eevee rasterization engine.
    for engine in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"):
        try:
            bpy.context.scene.render.engine = engine
            break
        except (TypeError, ValueError):
            continue
    else:
        raise RuntimeError("Blender Eevee renderer is required for ShaderToRGB")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    materials = config["characters"][args.character]["materials"]
    for index, (name, ramp_colors) in enumerate(materials.items()):
        mat = bpy.data.materials.new(name=args.character + "_" + name + "_three_band")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        output = nodes.new("ShaderNodeOutputMaterial")
        diffuse = nodes.new("ShaderNodeBsdfDiffuse")
        diffuse.inputs["Color"].default_value = (1, 1, 1, 1)
        shader_to_rgb = nodes.new("ShaderNodeShaderToRGB")
        ramp = nodes.new("ShaderNodeValToRGB")
        ramp.color_ramp.interpolation = "CONSTANT"
        elements = ramp.color_ramp.elements
        elements[0].position = 0.0
        elements[0].color = hex_to_linear_rgb(ramp_colors[0])
        elements[1].position = config["thresholds"][0]
        elements[1].color = hex_to_linear_rgb(ramp_colors[1])
        high = elements.new(config["thresholds"][1])
        high.color = hex_to_linear_rgb(ramp_colors[2])
        emission = nodes.new("ShaderNodeEmission")
        links = mat.node_tree.links
        links.new(diffuse.outputs["BSDF"], shader_to_rgb.inputs["Shader"])
        links.new(shader_to_rgb.outputs["Color"], ramp.inputs["Fac"])
        links.new(ramp.outputs["Color"], emission.inputs["Color"])
        links.new(emission.outputs["Emission"], output.inputs["Surface"])
        bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=(index * 2.5, 0, 0))
        bpy.context.object.name = args.character + "_" + name + "_swatch_NOT_CHARACTER"
        bpy.context.object.data.materials.append(mat)
    # Broad key light reveals all three bands on source swatches.
    light_data = bpy.data.lights.new("key", "AREA")
    light_data.energy = 800
    light_data.shape = "DISK"
    light_data.size = 4
    light = bpy.data.objects.new("key", light_data)
    bpy.context.collection.objects.link(light)
    light.location = (2.5, -3.5, 6)
    bpy.ops.object.camera_add(location=(4, -13, 6))
    camera = bpy.context.object
    bpy.context.scene.camera = camera
    camera.rotation_euler = (1.15, 0, 0)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = max(10.0, len(materials) * 2.8)
    bpy.context.scene.render.resolution_x = 1280
    bpy.context.scene.render.resolution_y = 720
    bpy.context.scene.render.resolution_percentage = 100
    args.output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(args.output))
    print("MATERIAL SWATCH ONLY:", args.output, "Blender", bpy.app.version_string)


if __name__ == "__main__":
    main()
