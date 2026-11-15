import json,pathlib,unittest,csv
R=pathlib.Path(__file__).resolve().parents[1];D=R/"chapters/pilot-001/video/stop_motion"
class TestStopMotion(unittest.TestCase):
 def test_exposures(self):
  s=json.loads((D/"scene.json").read_text());self.assertTrue(s["digital_simulation"]);self.assertFalse(s["physical_camera_recording"]);self.assertEqual(s["fps"],24)
  rows=list(csv.DictReader((D/"frame-exposure.csv").open()));self.assertEqual(len(rows),64)
  for row in rows:self.assertEqual(int(row["output_frame_end"])-int(row["output_frame_start"])+1,3);self.assertTrue((D/row["pose"]).is_file())
if __name__=="__main__":unittest.main()
