import pathlib,json,unittest
R=pathlib.Path(__file__).resolve().parents[1]
D=R/"chapters/pilot-001/video/ai_performance_transfer"
class Contracts(unittest.TestCase):
 def test_scene(self):
  d=json.loads((D/"scene.json").read_text());self.assertEqual(d["issue"],80);self.assertEqual(d["delivery"]["fps"],24);self.assertIsNone(d["approved_output"]);self.assertEqual(len(d["shots"]),3)
 def test_assets(self):
  self.assertTrue((D/"reference-board.svg").exists());self.assertTrue((D/"preview.html").exists());self.assertTrue((R/"characters/amd/continuity.yaml").exists())
if __name__=="__main__":unittest.main()
