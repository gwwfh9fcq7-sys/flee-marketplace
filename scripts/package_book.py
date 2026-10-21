"""Validate and package the Book plugin using only the Python standard library."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
FORMATS = (
    "mindmap", "sketchnotes", "flashcards", "comicbook", "visualnotes",
    "cheatsheet", "poster", "roadmap", "chaptermap", "themes", "mentalmodels", "action",
)


def package_files(package):
    files = sorted(p for p in package.rglob("*") if p.is_file())
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(package.resolve()):
            raise ValueError(f"Unsafe package path: {path}")
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            raise ValueError(f"Unexpected generated file: {path}")
    return files


def checksum_text(package):
    return "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(package).as_posix()}\n"
        for path in package_files(package) if path.name != "SHA256SUMS"
    )


def validate(root=ROOT):
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = [p for p in marketplace["plugins"] if p["name"] == "book"]
    if len(entries) != 1:
        raise ValueError("Marketplace must contain exactly one Book entry")
    entry = entries[0]
    if entry["source"] != "./plugins/book" or entry.get("strict") is not True:
        raise ValueError("Book must load its own plugin manifest from ./plugins/book")
    if {"commands", "skills", "hooks", "agents"}.intersection(entry):
        raise ValueError("Keep Book components in the plugin manifest, not the marketplace")
    package = root / "plugins/book"
    claude = json.loads((package / ".claude-plugin/plugin.json").read_text())
    codex = json.loads((package / ".codex-plugin/plugin.json").read_text())
    if {p["name"] for p in (entry, claude, codex)} != {"book"}:
        raise ValueError("Book package names differ")
    versions = {p["version"] for p in (entry, claude, codex)}
    if len(versions) != 1:
        raise ValueError(f"Book versions differ: {versions}")
    version = versions.pop()
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
        raise ValueError("Use a stable X.Y.Z release version")
    for name, manifest in (("Claude", claude), ("Codex", codex)):
        for field in ("skills", "commands"):
            locations = manifest.get(field, [])
            if isinstance(locations, str):
                locations = [locations]
            for location in locations:
                target = (package / location).resolve()
                if not target.is_relative_to(package.resolve()) or not target.is_dir():
                    raise ValueError(f"Invalid {name} {field} path: {location}")
    commands = {p.stem for p in (package / "commands").glob("*.md")}
    skills = {p.parent.name for p in (package / "skills").glob("*/SKILL.md")}
    if commands != {"book", *FORMATS}:
        raise ValueError(f"Unexpected Book command inventory: {commands}")
    if skills != {"book-visualizer", *(f"book-{f}" for f in FORMATS)}:
        raise ValueError(f"Unexpected Book skill inventory: {skills}")
    if commands.intersection(skills):
        raise ValueError("Command and skill names must not collide")
    for number, name in enumerate(FORMATS, 1):
        for path in (package / f"commands/{name}.md", package / f"skills/book-{name}/SKILL.md"):
            text = path.read_text()
            if f"Selection: ONLY `{name}` (format {number})" not in text or "book-visualizer" not in text:
                raise ValueError(f"Incorrect single-format routing: {path}")
    changelog = (package / "CHANGELOG.md").read_text()
    if f"## [{version}]" not in changelog:
        raise ValueError("Release version missing from changelog")
    if f"Version {version}" not in (package / "README.md").read_text():
        raise ValueError("README version differs from manifests")
    if (package / "SHA256SUMS").read_text() != checksum_text(package):
        raise ValueError("Package checksums differ; review changes before refreshing")
    return package, version


def archive_bytes(package):
    buffer = io.BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_DEFLATED) as archive:
        for path in package_files(package):
            info = ZipInfo("book/" + path.relative_to(package).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    return buffer.getvalue()


def write_once(path, data):
    if path.exists():
        if path.read_bytes() == data:
            return
        raise FileExistsError(f"Refusing to overwrite a different release: {path}")
    with path.open("xb") as stream:
        stream.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without creating an archive")
    parser.add_argument("--refresh-checksums", action="store_true", help="Record reviewed package changes")
    parser.add_argument("--output-dir", type=Path, help="Destination for a versioned ZIP and SHA-256 sidecar")
    args = parser.parse_args()
    if args.check and args.output_dir:
        parser.error("Use --check or --output-dir, not both")
    package = ROOT / "plugins/book"
    if args.refresh_checksums:
        (package / "SHA256SUMS").write_text(checksum_text(package))
    package, version = validate()
    print(f"PASS: book {version}; 13 commands, 13 skills, synchronized manifests and checksums")
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        name = f"book-{version}.zip"
        data = archive_bytes(package)
        sidecar = f"{hashlib.sha256(data).hexdigest()}  {name}\n".encode()
        write_once(args.output_dir / name, data)
        write_once(args.output_dir / f"{name}.sha256", sidecar)
        print(args.output_dir / name)


if __name__ == "__main__":
    main()
