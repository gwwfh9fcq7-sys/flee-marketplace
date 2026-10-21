# Marketplace maintenance

For Book Visualizer changes, use `plugins/book` as the canonical source. Track bugs and requested improvements in this repository's GitHub Issues with a `[book]` title prefix and the affected version. Link changes to an issue.

Keep the Book versions in both plugin manifests and its marketplace entry synchronized. Record release changes in `plugins/book/CHANGELOG.md`; follow `plugins/book/RELEASING.md` for packaging and publication. Book versions are independent of the other plugins.

Preserve the English default, all twelve format selections, evidence requirements, and honest host capability reporting. Do not claim that a repository upload installs a plugin in an app. Do not commit generated book packs, credentials, or private user uploads.

Run `python -m unittest discover -s tests -p 'test_*.py'` and `python scripts/package_book.py --check` before publishing Book changes. Report target-host smoke tests separately from static package checks.
