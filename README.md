# Flee marketplace

A GitHub-hosted plugin marketplace. Plugin source, versions, and issue tracking live in this repository.

| Plugin | Purpose | Claude-compatible install |
| --- | --- | --- |
| [Flee](plugins/flee/README.md) | Planning, improvement loops, and governance | `/plugin install flee@flee` |
| [Context Preload Audit](plugins/context-preload-audit/README.md) | Inspect startup context loading | `/plugin install context-preload-audit@flee` |
| [Book Visualizer](plugins/book/README.md) | Twelve book-learning visual formats; English by default | `/plugin install book@flee` |

First add the marketplace in a Claude-compatible host:

```text
/plugin marketplace add gwwfh9fcq7-sys/flee-marketplace
```

Book Visualizer v0.1.0 uses `/book:book` for the full pack and `/book:mindmap` (or another format) for one visual. Codex entrypoints and host requirements are documented in the [Book guide](plugins/book/README.md).

Report Book problems or improvements through [GitHub Issues](https://github.com/gwwfh9fcq7-sys/flee-marketplace/issues/new/choose). Include the plugin version and host. Follow the [Book release procedure](plugins/book/RELEASING.md) for version changes.
