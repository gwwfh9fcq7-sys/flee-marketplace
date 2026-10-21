"""Book package integration, routing, and reproducible-release regression checks."""

import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import package_book


class BookPackageTests(unittest.TestCase):
    def test_marketplace_and_both_hosts_resolve_complete_package(self):
        package, version = package_book.validate(ROOT)
        self.assertEqual(package, ROOT / "plugins/book")
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def temporary_repository(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        root = Path(scratch.name)
        shutil.copytree(ROOT / "plugins/book", root / "plugins/book")
        (root / ".claude-plugin").mkdir()
        shutil.copy2(ROOT / ".claude-plugin/marketplace.json", root / ".claude-plugin/marketplace.json")
        return root

    def test_rejects_version_drift(self):
        root = self.temporary_repository()
        path = root / "plugins/book/.codex-plugin/plugin.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = "0.1.1"
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "versions differ"):
            package_book.validate(root)

    def test_rejects_wrong_single_format_dispatch(self):
        root = self.temporary_repository()
        path = root / "plugins/book/commands/flashcards.md"
        path.write_text(path.read_text().replace("ONLY `flashcards`", "COMPLETE PACK"))
        with self.assertRaisesRegex(ValueError, "single-format routing"):
            package_book.validate(root)

    def test_detects_unrecorded_prompt_change(self):
        root = self.temporary_repository()
        path = root / "plugins/book/skills/book-visualizer/SKILL.md"
        path.write_text(path.read_text() + "\nChanged without checksum refresh.\n")
        with self.assertRaisesRegex(ValueError, "checksums differ"):
            package_book.validate(root)

    def test_archive_is_complete_and_reproducible(self):
        package, _ = package_book.validate(ROOT)
        first = package_book.archive_bytes(package)
        self.assertEqual(first, package_book.archive_bytes(package))
        with ZipFile(io.BytesIO(first)) as archive:
            self.assertIsNone(archive.testzip())
            expected = {"book/" + p.relative_to(package).as_posix() for p in package_book.package_files(package)}
            self.assertEqual(set(archive.namelist()), expected)
            self.assertIn("book/.claude-plugin/plugin.json", expected)
            self.assertIn("book/.codex-plugin/plugin.json", expected)
            self.assertFalse(any(".." in Path(name).parts for name in expected))

    def test_existing_release_cannot_be_replaced(self):
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "book-0.1.0.zip"
            package_book.write_once(path, b"first")
            package_book.write_once(path, b"first")
            with self.assertRaises(FileExistsError):
                package_book.write_once(path, b"different")
            self.assertEqual(path.read_bytes(), b"first")


if __name__ == "__main__":
    unittest.main()
