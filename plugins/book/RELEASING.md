# Releasing Book Visualizer

Keep Book changes, bugs, and feature requests in this repository. Use issue titles beginning with `[book]` and link implementation commits or pull requests to the issue.

## Version policy

Use Semantic Versioning, independently of the other marketplace plugins:

- Patch: fixes that preserve the commands and output contract.
- Minor: backward-compatible additions.
- Major: incompatible command, behavior, or output-contract changes.

For every release, update the same version in:

1. `plugins/book/.claude-plugin/plugin.json`
2. `plugins/book/.codex-plugin/plugin.json`
3. The `book` entry in `.claude-plugin/marketplace.json`

Record the date, behavior changes, and issue links in `plugins/book/CHANGELOG.md`. Update the README's displayed version. Recompute `plugins/book/SHA256SUMS` after edits using `python scripts/package_book.py --refresh-checksums --check`.

## Validate and package

Run from the repository root:

```bash
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_book.py --check
python scripts/package_book.py --output-dir /tmp/book-releases
```

When Claude Code is available, validate both the marketplace and plugin:

```bash
claude plugin validate .
claude plugin validate plugins/book
```

Then use a clean host profile to install `book@flee`, confirm that `/book:book` and all twelve format commands load, and exercise a single format with an image-capable host. For Codex, import the plugin and check that `$book-visualizer` and the twelve `$book-<format>` skills appear. Confirm English output even when a cover is in another language. Record the host, version, and results in the release issue. Do not claim that static checks alone prove host installation or image generation.

## Publish

Commit the release files. Use a pull request if required by branch protection. Tag the accepted commit `book-vX.Y.Z` and create a GitHub Release with the same tag, release notes, the versioned ZIP, and its SHA-256 sidecar. Do not overwrite an existing version or tag. Tags and GitHub Releases are separate from updating source and are not created by the local packager.

Installers refresh the Claude-compatible marketplace with `/plugin marketplace update flee` and use the host's plugin update mechanism to obtain the new version. Installing in one host does not install it into another app.

## Current release evidence

The initial package is tracked in [issue #4](https://github.com/gwwfh9fcq7-sys/flee-marketplace/issues/4). The source includes both host manifests, but target-host runtime smoke checks must be reported separately if those hosts are unavailable in the publishing environment.
