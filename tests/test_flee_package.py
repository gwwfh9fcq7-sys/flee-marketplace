"""Regression checks for Flee's dual-platform package (standard library only)."""

import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
COMPONENT_FIELDS = {"commands", "agents", "skills", "hooks", "outputStyles", "themes"}


class FleePackageTests(unittest.TestCase):
    def setUp(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.entry = next(p for p in marketplace["plugins"] if p["name"] == "flee")
        self.package = ROOT / self.entry["source"]
        self.claude = json.loads((self.package / ".claude-plugin/plugin.json").read_text())
        self.codex = json.loads((self.package / ".codex-plugin/plugin.json").read_text())

    def test_marketplace_can_load_plugin_manifest(self):
        # Claude rejects marketplace components with strict:false plus plugin.json.
        conflicting = COMPONENT_FIELDS.intersection(self.entry)
        self.assertFalse(
            self.entry.get("strict", True) is False and conflicting,
            f"Marketplace component declarations conflict with plugin.json: {conflicting}",
        )

    def test_versions_agree(self):
        root_manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        versions = {p["version"] for p in (self.entry, self.claude, self.codex, root_manifest)}
        self.assertEqual(len(versions), 1, f"Release versions differ: {versions}")

    def test_component_directories_exist(self):
        for component in ("commands", "skills"):
            locations = self.claude[component]
            if isinstance(locations, str):
                locations = [locations]
            for location in locations:
                with self.subTest(platform="Claude", component=component, location=location):
                    self.assertTrue((self.package / location).is_dir())
        self.assertTrue((self.package / self.codex["skills"]).is_dir())

    def test_package_checksums_match(self):
        entries = (self.package / "SHA256SUMS").read_text().splitlines()
        self.assertTrue(entries, "Package checksum list is empty")
        for entry in entries:
            expected, name = entry.split("  ", 1)
            with self.subTest(file=name):
                actual = hashlib.sha256((self.package / name).read_bytes()).hexdigest()
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
