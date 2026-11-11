import pathlib,json,unittest
R=pathlib.Path(__file__).resolve().parents[1]
D=R/"chapters/pilot-001/video/rotoscoping"
class Contract(unittest.TestCase):
 def test_scene(self):
  d=json.loads((D/"scene.json").read_text());self.assertEqual(d["issue"],75);self.assertEqual(d["fps"],24);self.assertEqual(len(d["stages"]),3)
  for i,s in enumerate(d["stages"]):self.assertEqual(s["end_frame"]-s["start_frame"],48);self.assertEqual(s["start_frame"],i*48)
 def test_media(self):
  self.assertTrue((D/"preview.html").exists());self.assertTrue((D/"reference-board.svg").exists())
  self.assertTrue((R/"characters/intel/continuity.yaml").exists());self.assertTrue((R/"characters/amd/continuity.yaml").exists())
if __name__=="__main__":unittest.main()
