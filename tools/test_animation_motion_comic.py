"""Offline smoke tests for the Pilot 001 motion-comic scene (#67)."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
HERE = ROOT / "chapters/pilot-001/video/motion_comic"

class MotionComicTests(unittest.TestCase):
    def test_scene_and_original_source_panels(self):
        data = json.loads((HERE / "scene.json").read_text(encoding="utf-8"))
        self.assertEqual(data["technique"], "motion_comic")
        self.assertEqual(data["delivery"]["fps"], 24)
        self.assertEqual(data["reading_direction"], "rtl")
        self.assertEqual(data["review_status"], "draft_human_review_required")
        self.assertGreaterEqual(len(data["shots"]), 2)
        self.assertEqual(len({s["id"] for s in data["shots"]}), len(data["shots"]))
        for shot in data["shots"]:
            self.assertGreater(shot["duration_frames"], 0)
            self.assertTrue((HERE / shot["image"]).is_file())
            self.assertGreater(shot["from"]["scale"], 0)
            self.assertGreater(shot["to"]["scale"], 0)
            self.assertLessEqual(shot["to"]["scale"], 1.2)
    def test_preserves_identity_and_has_preview(self):
        self.assertTrue((ROOT / "characters/intel/continuity.yaml").is_file())
        self.assertTrue((ROOT / "characters/amd/continuity.yaml").is_file())
        self.assertIn('fetch("scene.json")', (HERE / "preview.html").read_text())
        self.assertTrue((HERE / "reference-board.svg").is_file())

if __name__ == "__main__":
    unittest.main()
