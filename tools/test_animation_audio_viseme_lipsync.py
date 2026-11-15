"""Contract smoke tests for issue #69 (prototype data; not visual QA)."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCENE = ROOT / "chapters/pilot-001/video/audio_viseme_lipsync" / "scene.json"

class TestAudioVisemeLipsync(unittest.TestCase):
    def test_scene_contract(self):
        data = json.loads(SCENE.read_text(encoding="utf-8"))
        self.assertEqual(data["technique"], "audio_viseme_lipsync")
        self.assertEqual(data["delivery"]["fps"], 24)
        self.assertEqual(data["delivery"]["resolution"], [1920, 1080])
        self.assertEqual(data["review_status"], "draft_human_review_required")
        self.assertGreaterEqual(len(data["shots"]), 2)
        self.assertEqual(len({shot["id"] for shot in data["shots"]}), len(data["shots"]))
        for shot in data["shots"]:
            self.assertIsInstance(shot["duration_frames"], int)
            self.assertGreater(shot["duration_frames"], 0)
            self.assertTrue(shot["description"].strip())

    def test_preview_and_art(self):
        folder = SCENE.parent
        self.assertIn('fetch("scene.json")', (folder / "preview.html").read_text())
        self.assertTrue((folder / "reference-board.svg").read_text().startswith("<svg"))
        self.assertTrue((ROOT / "characters/amd/continuity.yaml").is_file())
        self.assertTrue((ROOT / "characters/intel/continuity.yaml").is_file())

if __name__ == "__main__":
    unittest.main()
