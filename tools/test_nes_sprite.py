"""Offline tests for 3-color-per-tile NES-inspired source validation."""
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from nes_sprite import NesSpriteError, read_manifest, pack


class NesSpriteTests(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.dir = Path(t.name)
        self.file = self.dir / "frames.json"
        im = Image.new("RGBA", (48, 64), (0, 0, 0, 0))
        for x in range(8, 40):
            for y in range(8, 56):
                im.putpixel((x, y), (200, 59, 53, 255))
        im.save(self.dir / "frame.png")
        self.data = {
            "schema": 1, "style": "pixel_8bit_nes", "mode": "creative_budget",
            "status": "unapproved", "character": "amd",
            "canvas": {"width": 48, "height": 64},
            "palettes": {"main": ["#18151D", "#C83B35", "#F2C7A2"]},
            "default_palette": "main", "tile_palettes": {},
            "frames": [{"id": "idle-1", "file": "frame.png",
                        "anchor": [24, 60], "hitbox": [8, 8, 40, 56]}]
        }
        self.save()

    def save(self):
        self.file.write_text(json.dumps(self.data), encoding="utf-8")

    def test_valid_pack_and_false_hardware_claim(self):
        data, images = read_manifest(self.file)
        self.assertEqual(images[0].size, (48, 64))
        out = self.dir / "build" / "demo"
        result = pack(self.file, out)
        self.assertFalse(result["hardware_verified"])
        with Image.open(str(out) + "-3x.png") as image:
            self.assertEqual(image.size, (144, 192))
            self.assertEqual(image.getpixel((9*3, 9*3)), (200, 59, 53, 255))

    def test_reject_fourth_tile_color(self):
        with Image.open(self.dir / "frame.png") as src:
            image = src.copy()
        image.putpixel((9, 9), (12, 34, 56, 255))
        image.save(self.dir / "frame.png")
        with self.assertRaisesRegex(NesSpriteError, "palette bank"):
            read_manifest(self.file)

    def test_reject_alpha(self):
        with Image.open(self.dir / "frame.png") as src:
            image = src.copy()
        image.putpixel((9, 9), (200, 59, 53, 190))
        image.save(self.dir / "frame.png")
        with self.assertRaisesRegex(NesSpriteError, "Antialiased"):
            read_manifest(self.file)

    def test_reject_unknown_bank(self):
        self.data["tile_palettes"] = {"2,1": "missing"}
        self.save()
        with self.assertRaisesRegex(NesSpriteError, "unknown"):
            read_manifest(self.file)

    def test_strict_mode_does_not_self_certify(self):
        self.data["mode"] = "hardware_candidate"
        self.save()
        result = pack(self.file, self.dir / "hardware")
        self.assertFalse(result["hardware_verified"])

    def test_reject_approved_with_no_visual_review(self):
        self.data["status"] = "approved"
        self.save()
        with self.assertRaisesRegex(NesSpriteError, "independent"):
            read_manifest(self.file)


if __name__ == "__main__":
    unittest.main()
