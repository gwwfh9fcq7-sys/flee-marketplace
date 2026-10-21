"""Verify the complete 3-style x 12-method Book sample library (stdlib only)."""

import hashlib
import json
from pathlib import Path
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]


def png_dimensions(data):
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("Not a PNG")
    offset = 8
    dimensions = None
    ended = False
    while offset < len(data):
        if len(data) - offset < 12:
            raise ValueError("Truncated PNG chunk")
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(data):
            raise ValueError("Truncated PNG payload")
        payload = data[offset + 8:offset + 8 + length]
        checksum = struct.unpack(">I", data[offset + 8 + length:end])[0]
        if zlib.crc32(kind + payload) & 0xffffffff != checksum:
            raise ValueError("PNG chunk checksum differs")
        if kind == b"IHDR":
            dimensions = struct.unpack(">II", payload[:8])
        offset = end
        if kind == b"IEND":
            ended = True
            break
    if not ended or offset != len(data) or not dimensions:
        raise ValueError("Invalid or incomplete PNG")
    return dimensions


def validate(root=ROOT):
    gallery = root / "examples/book/the-creating-brain"
    manifest = json.loads((gallery / "manifest.json").read_text())
    presets = json.loads((root / "plugins/book/skills/book-visualizer/references/styles.json").read_text())
    styles = presets["all_order"]
    if len(styles) < 3 or len(set(styles)) != len(styles):
        raise ValueError("At least three distinct style presets are required")
    expected = {(style, number) for style in styles for number in range(1, 13)}
    records = manifest["samples"]
    actual = {(r["style"], r["format_number"]) for r in records}
    if len(records) != len(expected) or actual != expected:
        raise ValueError("Incomplete or duplicate style/method coverage")
    if len({r["sha256"] for r in records}) != len(records):
        raise ValueError("Samples must be distinct image files, not repeated placeholders")
    paths = set()
    for record in records:
        path = gallery / record["file"]
        if not path.resolve().is_relative_to(gallery.resolve()) or path.is_symlink():
            raise ValueError(f"Unsafe sample path: {path}")
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError(f"Sample hash differs: {path}")
        dimensions = png_dimensions(data)
        if dimensions != (record["width"], record["height"]) or min(dimensions) < 1024:
            raise ValueError(f"Invalid sample dimensions: {path}")
        if record["language"] != "English" or not record["learning_method"]:
            raise ValueError(f"Missing language/method metadata: {path}")
        paths.add(path.relative_to(gallery).as_posix())
        if record["style"] == "illustrated" and record.get("original_sha256") != record["sha256"]:
            raise ValueError(f"Reused original differs: {path}")
    actual_paths = {p.relative_to(gallery).as_posix() for p in gallery.rglob("*.png")}
    if actual_paths != paths:
        raise ValueError("Gallery contains missing or untracked image files")
    for name in ("README.md", "index.html"):
        text = (gallery / name).read_text()
        if not all(path in text for path in paths):
            raise ValueError(f"Gallery does not link every sample: {name}")
    return manifest


if __name__ == "__main__":
    result = validate()
    print(f"PASS: {len(result['samples'])} English PNGs; complete 3 x 12 coverage, hashes, PNG CRCs, dimensions and gallery links")
