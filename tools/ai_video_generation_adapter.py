"""Offline, model-agnostic AI-video shot validator and provider payload preparation (#79)."""
import argparse,json,pathlib,hashlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
HERE=ROOT/"chapters/pilot-001/video/ai_video_generation"
def check():
 shot=json.loads((HERE/"shot.json").read_text())
 assert 3<=shot["duration_seconds"]<=8
 assert shot["width"]>0 and shot["height"]>0
 assert len(shot["characters"])>=1 and len(set(shot["characters"]))==len(shot["characters"])
 assert shot["first_keyframe"] != shot["last_keyframe"]
 assert "provider_model" in shot and shot["provider_model"] is None, "provider not connected"
 for key in ("first_keyframe","last_keyframe"):
  path=HERE/shot[key];assert path.is_file(), f"Missing keyframe: {path}"
 for ref in shot["canonical_refs"]:
  assert (ROOT/ref).is_file(), f"Missing continuity reference: {ref}"
 ledger=json.loads((HERE/"candidates.json").read_text())
 assert all(x["status"] in ("planned","generated","rejected","accepted") for x in ledger["candidates"])
 assert not any(x["status"]=="accepted" for x in ledger["candidates"]),"There is no reviewed generated footage"
 return shot
def main():
 p=argparse.ArgumentParser();p.add_argument("--prepare",action="store_true");a=p.parse_args()
 shot=check()
 print("OK: shot schema, assets, provider-neutral request and honest candidate ledger")
 if a.prepare:
  request={key:shot[key] for key in ("description","duration_seconds","width","height","negative_constraints","camera_movement","characters")}
  request.update({"first_image":str(HERE/shot["first_keyframe"]),"last_image":str(HERE/shot["last_keyframe"]),"provider_model":shot["provider_model"]})
  print(json.dumps(request,indent=2))
if __name__=="__main__":main()
