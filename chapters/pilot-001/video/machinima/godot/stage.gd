extends Node3D
# Minimal machinima proxy stage, not a complete rigged character production.
@onready var wide: Camera3D = $WideCamera
@onready var close: Camera3D = $CloseCamera
@onready var intel: MeshInstance3D = $IntelProxy
@onready var amd: MeshInstance3D = $AmdProxy
var elapsed: float = 0.0
var show_close: bool = false
func _ready() -> void:
    wide.look_at(Vector3(0, 1.0, 0))
    close.look_at(Vector3(0, 1.0, 0))
    wide.current = true
func _process(delta: float) -> void:
    # Same actors/timeline for either camera. Space toggles the camera.
    elapsed = fmod(elapsed + delta, 15.0)
    intel.position.x = -1.5 + sin(elapsed / 15.0 * TAU) * 0.25
    amd.position.x = 1.5 - sin(elapsed / 15.0 * TAU) * 0.25
    amd.rotation.y = sin(elapsed / 15.0 * TAU) * 0.2
    if Input.is_action_just_pressed("ui_accept"):
        show_close = not show_close
        close.current = show_close
        wide.current = not show_close
