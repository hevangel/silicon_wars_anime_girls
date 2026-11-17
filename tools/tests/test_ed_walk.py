"""Height, ground-contact and export regression checks for the ED Walk.

Run from the repository root: py -3 -m unittest discover -s tools/tests -p test_ed_walk.py
"""
import importlib.util
import json
from pathlib import Path
import unittest

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('ed_walk', ROOT / 'tools/build_ed_walk.py')
ed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ed)


class HeightCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.roster = json.loads((ROOT / 'characters/roster.json').read_text(encoding='utf-8'))
        cls.calibration = json.loads(ed.CALIBRATION.read_text(encoding='utf-8'))['characters']
        cls.render = json.loads((ed.ART / 'ed-walk.render.json').read_text(encoding='utf-8'))

    def test_every_character_has_current_landmarks(self):
        self.assertEqual({e['slug'] for e in self.roster}, set(self.calibration))
        for entry in self.roster:
            with self.subTest(slug=entry['slug']):
                path = ed.ART / 'cutouts' / (entry['slug'] + '.png')
                self.assertEqual(ed.sha256(path), self.calibration[entry['slug']]['source_sha256'])

    def test_stature_ground_and_uniform_scale(self):
        ground = self.render['canvas']['ground_y']
        self.assertEqual([e['slug'] for e in self.roster], [e['slug'] for e in self.render['figures']])
        for entry, record in zip(self.roster, self.render['figures']):
            with self.subTest(slug=entry['slug']):
                markers = self.calibration[entry['slug']]
                with Image.open(ed.ART / 'cutouts' / (entry['slug'] + '.png')) as im:
                    expected = ed.figure_geometry(entry, im, markers)
                    self.assertLess(abs(record['width'] - im.width * record['height'] / im.height), 1)
                for key, value in expected.items():
                    self.assertEqual(record[key], value)
                self.assertEqual(record['y'] + record['ground_offset'], ground)
                actual_span = ground - (record['y'] + record['head_offset'])
                self.assertLessEqual(abs(actual_span - expected['target_span_px']), 1)
                self.assertGreaterEqual(record['y'], ed.TOP_PAD)
                self.assertLessEqual(record['y'] + record['height'], self.render['canvas']['height'])

    def test_invalid_or_stale_landmarks_fail(self):
        entry = self.roster[0]
        markers = self.calibration[entry['slug']]
        with Image.open(ed.ART / 'cutouts' / (entry['slug'] + '.png')) as im:
            with self.assertRaises(ValueError):
                ed.figure_geometry(entry, im, {**markers, 'head_top_y': markers['ground_y']})
            with self.assertRaises(ValueError):
                ed.figure_geometry(entry, im, {**markers, 'source_size': [1, 1]})

    def test_render_provenance_matches_inputs(self):
        self.assertEqual(self.render['roster_sha256'], ed.sha256(ROOT / 'characters/roster.json'))
        self.assertEqual(self.render['calibration_sha256'], ed.sha256(ed.CALIBRATION))
        self.assertEqual(self.render['builder_sha256'], ed.sha256(ROOT / 'tools/build_ed_walk.py'))
        self.assertEqual(self.render['render_sha256'], ed.sha256(ed.ART / 'ed-walk-full.png'))

    def test_slices_are_lossless_contiguous_panorama_crops(self):
        with Image.open(ed.ART / 'ed-walk-full.png') as panorama:
            self.assertEqual(panorama.size, (self.render['canvas']['width'], self.render['canvas']['height']))
            previous_end = 0
            for segment in self.render['slices']:
                self.assertEqual(segment['x0'], previous_end)
                with Image.open(ed.ART / segment['file']) as actual:
                    expected = panorama.crop((segment['x0'], 0, segment['x1'], panorama.height))
                    self.assertEqual(actual.size, expected.size)
                    self.assertIsNone(ImageChops.difference(actual, expected).getbbox())
                previous_end = segment['x1']
            self.assertEqual(previous_end, panorama.width)


if __name__ == '__main__':
    unittest.main()
