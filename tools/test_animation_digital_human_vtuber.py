import json, pathlib, unittest
R=pathlib.Path(__file__).resolve().parents[1]
D=R/"chapters/pilot-001/video/digital_human_vtuber"
class Tests(unittest.TestCase):
 def test_controls(self):
  x=json.loads((D/"scene.json").read_text());self.assertEqual(x["issue"],73);self.assertIsNone(x["model_export"]);self.assertEqual(len(x["states"]),3)
  for p in x["params"]:self.assertLess(p["min"],p["max"])
 def test_preview(self):
  self.assertIn('fetch("scene.json")',(D/"preview.html").read_text());self.assertTrue((D/"reference-board.svg").exists());self.assertTrue((R/"characters/intel/continuity.yaml").exists())
if __name__=="__main__":unittest.main()
