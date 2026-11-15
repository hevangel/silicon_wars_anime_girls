"""Offline validator/packing regression checks; run with unittest discover."""
import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from pixel_arcade import SpriteError, read_manifest, pack


class PixelArcadeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / "frames.json"
        for name in ("idle-01", "idle-02"):
            image = Image.new("RGBA", (96, 128), (0, 0, 0, 0))
            for x in range(30, 60):
                for y in range(30, 110):
                    image.putpixel((x, y), (155, 22, 38, 255))
            image.save(self.root / (name + ".png"))
        self.data = {
            "schema": 1, "style": "pixel_arcade_sf2", "character": "amd",
            "canvas": {"width": 96, "height": 128}, "palette_limit": 32,
            "status": "unapproved",
            "frames": [
                {"id": n, "file": n + ".png",
                 "anchor": [48, 120], "hitbox": [30, 30, 60, 110]}
                for n in ("idle-01", "idle-02")
            ]
        }
        self.save()

    def save(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def test_validate_and_pack_exact_nearest_neighbour(self):
        _, frames, count = read_manifest(self.manifest)
        self.assertEqual((len(frames), count), (2, 1))
        out = self.root / "export" / "amd"
        tags = pack(self.manifest, out, 2)
        self.assertEqual(tags["frames"][1]["rect"], [96, 0, 96, 128])
        with Image.open(str(out) + ".png") as sheet:
            self.assertEqual(sheet.size, (192, 128))
            self.assertEqual(sheet.getpixel((35, 50)), (155, 22, 38, 255))
        with Image.open(str(out) + "-4x.png") as zoom:
            self.assertEqual(zoom.getpixel((35*4 + 3, 50*4 + 3)),
                             (155, 22, 38, 255))
        self.assertTrue(Path(str(out) + ".json").exists())

    def test_reject_antialiased_alpha(self):
        with Image.open(self.root / "idle-02.png") as src:
            im = src.copy()
        im.putpixel((1, 1), (3, 4, 5, 80))
        im.save(self.root / "idle-02.png")
        with self.assertRaisesRegex(SpriteError, "antialiased alpha"):
            read_manifest(self.manifest)

    def test_reject_missing_frames(self):
        self.data["frames"][0]["file"] = "no.png"
        self.save()
        with self.assertRaisesRegex(SpriteError, "missing"):
            read_manifest(self.manifest)

    def test_reject_invalid_geometry(self):
        self.data["frames"][0]["anchor"] = [999, 120]
        self.save()
        with self.assertRaisesRegex(SpriteError, "anchor"):
            read_manifest(self.manifest)

    def test_reject_duplicate_ids(self):
        self.data["frames"][1]["id"] = "idle-01"
        self.save()
        with self.assertRaisesRegex(SpriteError, "unique"):
            read_manifest(self.manifest)

    def test_reject_unreviewed_approved_label(self):
        self.data["status"] = "approved"
        self.save()
        with self.assertRaisesRegex(SpriteError, "separate human review"):
            read_manifest(self.manifest)


if __name__ == "__main__":
    unittest.main()
