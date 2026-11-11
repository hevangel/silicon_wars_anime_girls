import json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
HERE=ROOT/"chapters/pilot-001/video/photoreal_3d_cinematic"
class Contract(unittest.TestCase):
 def test_manifest(self):
  d=json.loads((HERE/"scene.json").read_text());self.assertEqual(d["issue"],78);self.assertEqual(d["delivery"]["fps"],24);self.assertEqual(len(d["shots"]),3);self.assertEqual(sum(x["duration_frames"] for x in d["shots"]),360)
 def test_art(self):
  self.assertTrue((HERE/"reference-board.svg").exists());self.assertTrue((HERE/"preview.html").exists());self.assertTrue((ROOT/"characters/intel/continuity.yaml").exists())
if __name__=="__main__":unittest.main()
