# Godot machinima scene (#81)

This is an implementation milestone: **Two cameras, foundry set, proxy actors**. It has an original [visual board](../../chapters/pilot-001/video/machinima/reference-board.svg), a runnable browser concept preview, a three-beat scene JSON, pipeline YAML and smoke tests.

```sh
python -m unittest tools.test_animation_machinima -v
python -m http.server 8000
# open http://localhost:8000/chapters/pilot-001/video/machinima/preview.html
```

The stage / animation inputs remain separate from visual art style and do not alter the existing Intel/AMD character sheets.

A **Godot 4** stage source is included in `chapters/pilot-001/video/machinima/godot/`. Open `project.godot`, press Play, and use Space to switch between two cameras without changing actor movement time. Two capsule actors are purposeful proxies; user must replace with full approved rigged meshes before claiming machinima character production.

Technical validation does not certify video quality or artistic approval.

**Not complete:** 3D proxy capsules are not approved full-body Intel/AMD models; Godot runtime, OBS capture and 30-second episode are not verified.. Record source hashes, precise tool versions, rights and generated binary provenance, render and visually approve the result, then replace the draft status.
