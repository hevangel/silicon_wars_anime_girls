"""Blender 4.x procedural blocking scene for #78. Proxy mannequins only, no canon 3D model."""
import bpy, math, os
from mathutils import Vector
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)
def material(name,color,metallic=0.0,roughness=0.6):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 p=m.node_tree.nodes.get("Principled BSDF");p.inputs["Base Color"].default_value=(*color,1);p.inputs["Metallic"].default_value=metallic;p.inputs["Roughness"].default_value=roughness
 return m
blue=material("Intel royal blue",(.10,.30,.70),.3,.4)
red=material("AMD crimson",(.68,.09,.15),.2,.5)
skin=material("neutral proxy skin",(.76,.57,.48))
gold=material("gold detailing",(.72,.52,.24),.4,.32)
floor_mat=material("foundry floor",(.08,.12,.19),.4,.35)
def block(name,loc,scale,mat,kind="cube"):
 if kind=="sphere":bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=12,location=loc)
 elif kind=="cone":bpy.ops.mesh.primitive_cone_add(vertices=7,radius1=1,radius2=.12,location=loc)
 else:bpy.ops.mesh.primitive_cube_add(size=1,location=loc)
 o=bpy.context.object;o.name=name;o.scale=scale;o.data.materials.append(mat);return o
def figure(name,x,coat,crown):
 body=block(name+" Body",(x,0,1.25),(.78,.37,1.3),coat)
 head=block(name+" Face",(x,0,2.25),(.38,.38,.47),skin,"sphere")
 arm=block(name+" PointingArm",(x-.52,0,1.55),(.26,.32,.94),coat)
 arm.rotation_euler.y=-.2
 for frame,a in [(1,-.2),(36,-.75),(72,-1.4),(112,-.4),(170,.15),(240,-.2)]:
  arm.rotation_euler.y=a;arm.keyframe_insert(data_path="rotation_euler",frame=frame)
 if crown:block(name+" Crown",(x,0,2.85),(.26,.26,.25),gold,"cone")
 else:
  braid=block(name+" RedBraid",(x+.46,.12,2.36),(.19,.19,.71),red,"cone")
  braid.rotation_euler.y=.7
 return body
intel=figure("IntelProxy",-1.6,blue,True)
amd=figure("AMDProxy",1.6,red,False)
block("Ground",(0,0,-.15),(12,12,.25),floor_mat)
for xx in (-4,4):
 block("FoundryColumn",(xx,2,1.7),(.6,.6,3.6),floor_mat)
bpy.ops.object.camera_add(location=(0,-9,3.3))
camera=bpy.context.object;camera.name="WideCamera";target=Vector((0,0,1.4));camera.rotation_euler=(target-camera.location).to_track_quat("-Z","Y").to_euler();bpy.context.scene.camera=camera
camera.data.lens=50
def area(name,loc,energy,color):
 bpy.ops.object.light_add(type="AREA",location=loc);o=bpy.context.object;o.name=name;o.data.energy=energy;o.data.color=color;o.data.shape="DISK";o.data.size=4
area("Key",(-3,-4,7),1100,(1,.9,.79))
area("Rim",(4,2,5),1500,(.55,.73,1))
scene=bpy.context.scene;scene.frame_start=1;scene.frame_end=240;scene.render.fps=24;scene.render.resolution_x=1920;scene.render.resolution_y=1080;scene.render.resolution_percentage=50
scene.render.image_settings.file_format="PNG"
scene.render.filepath="//preview-frames/"
camera.location=(0,-7.2,2.9);camera.data.lens=65
for frame,loc in [(1,(0,-7.2,2.9)),(120,(-1.2,-5.6,2.7)),(240,(.4,-6.2,2.8))]:
 camera.location=loc;camera.keyframe_insert(data_path="location",frame=frame)

scene.world.color=(.13,.17,.23)
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"blocking_scene.blend")
bpy.ops.wm.save_as_mainfile(filepath=out)
print("Created original blocking scene (not an approved actor):",out)
