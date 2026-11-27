"""Validate provenance and map rights-safe synthetic driver keyposes to AMD coordinates."""
import json,pathlib,sys
D=pathlib.Path(__file__).resolve().parents[1]/"chapters/pilot-001/video/ai_performance_transfer"
p=json.loads((D/"driver-poses.json").read_text())
c=json.loads((D/"consent-ledger.json").read_text())
assert p["source_type"]=="synthetic_original_nonrecorded"
assert c["source_recording"] is None and c["release_eligible"] is False
frames=p["keyposes"];assert all(frames[i]["frame"]<frames[i+1]["frame"] for i in range(len(frames)-1))
mapped=[{"frame":f["frame"],"AMD_head_yaw":f["yaw"],"AMD_arm_pitch":f["arm_pitch"],"AMD_mouth_open":f["mouth_open"]} for f in frames]
print(json.dumps({"status":"PROCEDURAL_DEMO_ONLY","mapped":mapped},indent=2))
