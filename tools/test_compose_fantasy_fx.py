"""Offline compositor regression checks with tiny synthetic RGBA plates."""
import json
from pathlib import Path
import tempfile
import unittest
from PIL import Image
from compose_fantasy_fx import PlateError, compose


class CompositorTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for name, color in (
            ("actor", (60, 70, 80, 255)),
            ("costume", (170, 30, 30, 127)),
            ("fx", (255, 30, 10, 127))):
            Image.new("RGBA", (4, 4), color).save(self.root / (name + ".png"))
        self.data = {"schema": 1, "style": "live_action_hyperreal_fantasy",
                     "actor_id": "original-fiction-v1", "wardrobe_id": "wardrobe-v1",
                     "canvas": [4, 4], "status": "unapproved",
                     "plates": [{"id": name, "role": name, "file": name + ".png"}
                                for name in ("actor", "costume", "fx")]}
        self.path = self.root / "manifest.json"
        self.save()

    def save(self):
        self.path.write_text(json.dumps(self.data), encoding="utf-8")

    def test_composite_clean_and_effects_separately(self):
        result = compose(self.path, self.root / "out" / "scene")
        self.assertEqual(len(result["layers"]), 3)
        clean = Image.open(self.root / "out/scene-clean.png")
        full = Image.open(self.root / "out/scene-all.png")
        self.assertNotEqual(clean.getpixel((0, 0)), full.getpixel((0, 0)))
        self.assertTrue((self.root / "out/scene.json").is_file())
        clean.close()
        full.close()

    def test_reject_missing_plate(self):
        self.data["plates"][2]["file"] = "none.png"
        self.save()
        with self.assertRaisesRegex(PlateError, "Missing"):
            compose(self.path, self.root / "out")

    def test_reject_wrong_order(self):
        self.data["plates"].reverse()
        self.save()
        with self.assertRaisesRegex(PlateError, "Layer order"):
            compose(self.path, self.root / "out")

    def test_reject_approved_without_review(self):
        self.data["status"] = "approved"
        self.save()
        with self.assertRaisesRegex(PlateError, "approval"):
            compose(self.path, self.root / "out")

    def test_reject_opaque_rgb_input(self):
        Image.new("RGB", (4, 4), (10, 20, 30)).save(self.root / "fx.png")
        with self.assertRaisesRegex(PlateError, "RGBA"):
            compose(self.path, self.root / "out")


if __name__ == "__main__":
    unittest.main()
