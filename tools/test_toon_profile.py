"""Offline validation of Blender toon presets, no Blender dependency."""
import json
from pathlib import Path
import re
import unittest


CONFIG = Path(__file__).resolve().parents[1] / "workflows/cel_shaded_3d/material_presets.json"


class ToonPresetTests(unittest.TestCase):
    def test_ramp_catalog(self):
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.assertEqual(data["style"], "cel_shaded_3d")
        self.assertEqual(data["shader_bands"], 3)
        self.assertEqual(len(data["thresholds"]), 2)
        self.assertLess(data["thresholds"][0], data["thresholds"][1])
        self.assertGreater(data["thresholds"][0], 0)
        self.assertLess(data["thresholds"][1], 1)
        self.assertEqual(set(data["characters"]), {"intel", "amd"})
        for char, specs in data["characters"].items():
            self.assertGreaterEqual(len(specs["materials"]), 3, char)
            for name, colors in specs["materials"].items():
                self.assertEqual(len(colors), 3, (char, name))
                for color in colors:
                    self.assertRegex(color, r"^#[0-9a-fA-F]{6}$")


if __name__ == "__main__":
    unittest.main()
