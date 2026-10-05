"""Check actual Claude loading with temporary settings and a local marketplace.

Run: python3 tests/smoke_claude_marketplace.py
Requires Claude Code on PATH; never invokes a Flee workflow.
"""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    claude = shutil.which("claude")
    if not claude:
        raise SystemExit("Claude Code is required for the marketplace smoke test.")
    root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory(prefix="flee-marketplace-smoke-") as scratch:
        scratch = Path(scratch)
        source = scratch / "marketplace"
        shutil.copytree(root, source, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        cwd = scratch / "empty-cwd"
        cwd.mkdir()
        env = dict(os.environ)
        env.pop("CLAUDE_CODE_PLUGIN_DIRS", None)
        env.pop("CLAUDE_CODE_PLUGIN_SEED_DIR", None)
        env.update(
            CLAUDE_CONFIG_DIR=str(scratch / "claude-config"),
            CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1",
            DISABLE_AUTOUPDATER="1",
        )

        def run(*args):
            result = subprocess.run(
                [claude, "--bare", "--setting-sources", "user", *args],
                cwd=cwd, env=env, capture_output=True, text=True, timeout=30,
            )
            if result.returncode:
                raise RuntimeError(f"{args}: {result.stdout}\n{result.stderr}")
            return result.stdout

        run("plugin", "marketplace", "add", str(source))
        run("plugin", "install", "flee@flee")
        installed = json.loads(run("plugin", "list", "--json"))
        flee = next(p for p in installed if p["id"] == "flee@flee")
        if flee.get("errors") or flee.get("errorDetails"):
            raise RuntimeError(f"Flee failed to load: {flee.get('errors') or flee.get('errorDetails')}")
        manifest = json.loads((source / "plugins/flee/.claude-plugin/plugin.json").read_text())
        if flee["version"] != manifest["version"] or not flee["enabled"]:
            raise RuntimeError("Installed Flee version or enabled state differs from the package")
        details = run("plugin", "details", "flee")
        component_line = next(line for line in details.splitlines() if line.strip().startswith("Skills ("))
        names = {name.strip() for name in component_line.split(")", 1)[1].split(",")}
        expected = {p.stem for p in (source / "plugins/flee/commands").glob("*.md")}
        expected.update(p.parent.name for p in (source / "plugins/flee/skills").glob("*/SKILL.md"))
        if names != expected:
            raise RuntimeError(f"Unexpected component inventory: expected {sorted(expected)}, got {sorted(names)}")
        print(f"PASS: isolated marketplace install loads Flee {flee['version']} with all {len(names)} components.")


if __name__ == "__main__":
    main()
