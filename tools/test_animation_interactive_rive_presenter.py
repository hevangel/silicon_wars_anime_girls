import json,pathlib,unittest
R=pathlib.Path(__file__).resolve().parents[1];D=R/"chapters/pilot-001/video/interactive_rive_presenter"
class TestContract(unittest.TestCase):
 def test_replay(self):
  d=json.loads((D/"replay.json").read_text());self.assertIsNone(d["model_export"]);self.assertGreaterEqual(len(d["commands"]),4)
  for x in d["commands"]:self.assertGreater(x["duration_frames"],0);self.assertLessEqual(x["duration_frames"],240)
 def test_runtime(self):
  self.assertIn("export class PresenterMachine",(D/"controller.js").read_text());self.assertTrue((D/"controller.test.mjs").exists())
if __name__=="__main__":unittest.main()
