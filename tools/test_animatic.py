"""Offline animatic tests: source, frame ranges, cues, and preview output."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from animatic import AnimaticError, build, load, timecode


class AnimaticTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        panel_dir = self.root / "chapters/test/pages/page-001/art"
        panel_dir.mkdir(parents=True)
        self.paths = []
        for i in (1, 2):
            p = panel_dir / f"panel-0{i}.png"
            Image.new("RGB", (80, 80), (80*i, 30, 80)).save(p)
            self.paths.append(p)
        hashes = [hashlib.sha256(p.read_bytes()).hexdigest() for p in self.paths]
        sources = {
            "storyboard.yaml": "panels:\n  - id: panel-01\n  - id: panel-02\n",
            "lettering.yaml": "items:\n  - id: speech1\n    panel: panel-02\n    text: Hello.\n    kind: speech\n",
            "manifest.yaml": "panels:\n" + "".join(
                f"  - id: panel-0{i}\n    output: chapters/test/pages/page-001/art/panel-0{i}.png\n    image_sha256: {hashes[i-1]}\n"
                for i in (1, 2)),
        }
        for name, content in sources.items():
            (self.root / name).write_text(content, encoding="utf-8")
        self.data = {
            "schema": 1, "technique": "animatic", "episode": "test",
            "art_style": "default_manga", "reading_direction": "rtl",
            "fps": 24, "frames": 48, "resolution": [160, 90],
            "source_storyboard": "storyboard.yaml",
            "source_lettering": "lettering.yaml",
            "source_manifest": "manifest.yaml",
            "shots": [
                {"id": f"s0{i}", "panel_id": f"panel-0{i}",
                 "art": f"chapters/test/pages/page-001/art/panel-0{i}.png",
                 "art_sha256": hashes[i-1], "characters": [],
                 "start_frame": (i-1)*24, "end_frame": i*24,
                 "camera": {"center": [.5, .5], "zoom_from": 1, "zoom_to": 1.03},
                 "cues": ([{"id": "speech1", "offset_frames": 2,
                           "duration_frames": 15, "text": "Hello."}] if i == 2 else []),
                 "screen_overlays": []}
                for i in (1, 2)]
        }
        self.timeline = self.root / "timeline.json"
        self.save()

    def save(self):
        self.timeline.write_text(json.dumps(self.data), encoding="utf-8")

    def test_validation_and_still_build(self):
        data, details, _ = load(self.timeline, root=self.root)
        self.assertEqual(len(details), 2)
        result = build(self.timeline, self.root / "build", root=self.root,
                       video=False, size_override=(160, 90))
        self.assertEqual(result["duration_seconds"], 2.0)
        for name in ("contact-sheet.jpg", "subtitles.srt", "placeholder-audio.wav",
                     "edit-decision-list.csv", "build-manifest.json",
                     "stills/s01.png", "stills/s02.png"):
            self.assertTrue((self.root / "build" / name).is_file(), name)
        srt = (self.root / "build/subtitles.srt").read_text(encoding="utf-8")
        self.assertIn("00:00:01,083 --> 00:00:01,708", srt)

    def test_overlap_or_gap_rejected(self):
        self.data["shots"][1]["start_frame"] = 23
        self.save()
        with self.assertRaisesRegex(AnimaticError, "contiguous"):
            load(self.timeline, self.root)

    def test_art_change_rejected(self):
        Image.new("RGB", (80, 80), (2, 2, 2)).save(self.paths[0])
        with self.assertRaisesRegex(AnimaticError, "SHA-256"):
            load(self.timeline, self.root)

    def test_dialogue_drift_rejected(self):
        self.data["shots"][1]["cues"][0]["text"] = "Different."
        self.save()
        with self.assertRaisesRegex(AnimaticError, "editable lettering"):
            load(self.timeline, self.root)

    def test_panel_order_rejected(self):
        self.data["shots"][1]["panel_id"] = "panel-01"
        self.save()
        with self.assertRaisesRegex(AnimaticError, "source panel order"):
            load(self.timeline, self.root)

    def test_timecode(self):
        self.assertEqual(timecode(24, 24), "00:00:01,000")
        self.assertEqual(timecode(1, 24), "00:00:00,042")


if __name__ == "__main__":
    unittest.main()
