"""Coverage and integrity regression checks for the public Book gallery."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_book_samples


class BookSampleTests(unittest.TestCase):
    def test_complete_public_library(self):
        manifest = verify_book_samples.validate(ROOT)
        self.assertEqual(len(manifest["samples"]), 36)

    def test_missing_method_style_pair_is_rejected(self):
        manifest = json.loads((ROOT / "examples/book/the-creating-brain/manifest.json").read_text())
        manifest["samples"].pop()
        presets = json.loads((ROOT / "plugins/book/skills/book-visualizer/references/styles.json").read_text())
        with patch.object(verify_book_samples.json, "loads", side_effect=[manifest, presets]):
            with self.assertRaisesRegex(ValueError, "coverage"):
                verify_book_samples.validate(ROOT)

    def test_corrupted_png_is_rejected(self):
        path = ROOT / "examples/book/the-creating-brain/illustrated/01-mindmap.png"
        data = bytearray(path.read_bytes())
        data[20] ^= 1
        with self.assertRaisesRegex(ValueError, "checksum"):
            verify_book_samples.png_dimensions(bytes(data))


if __name__ == "__main__":
    unittest.main()
