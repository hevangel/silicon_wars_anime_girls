"""Check art style registry consistency and unapproved production refs."""
from pathlib import Path
import unittest
import yaml


ROOT = Path(__file__).resolve().parents[1]


class StyleRegistryTests(unittest.TestCase):
    def test_all_registered_styles_have_usage_policy(self):
        with (ROOT / "bible/art_style.yaml").open(encoding="utf-8") as f:
            art = yaml.safe_load(f)["style_system"]["variants"]
        with (ROOT / "bible/style_usage_policy.yaml").open(encoding="utf-8") as f:
            policy = yaml.safe_load(f)["style_usage_policy"]
        self.assertIn("default_manga", art)
        self.assertIn("chibi", art)
        self.assertEqual(set(art), set(policy))

    def test_intel_amd_style_overrides_are_valid(self):
        for char in ("intel", "amd"):
            with (ROOT / "characters" / char / "continuity.yaml").open(encoding="utf-8") as f:
                canon = yaml.safe_load(f)
            self.assertEqual(canon["id"], char)
            for style in canon["supported_styles"]:
                self.assertIn(style, yaml.safe_load((ROOT / "bible/art_style.yaml").read_text())["style_system"]["variants"])
                if style in ("chibi", "default_manga"):
                    continue
                override_ref = canon["style_variants"][style].get("override_file")
                self.assertTrue(override_ref, (char, style))
                file = ROOT / override_ref
                self.assertTrue(file.is_file(), file)
                with file.open(encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                self.assertEqual(data["style_id"], style)
                self.assertEqual(data["character_id"], char)
                self.assertFalse(data.get("human_approved"), (char, style))
                self.assertTrue((ROOT / "prompts/templates" / (style + ".md")).is_file())
                self.assertTrue((ROOT / "tutorial/styles" / (style + ".md")).is_file())


if __name__ == "__main__":
    unittest.main()
