# Platform notes

This source package is intentionally dual-platform:

- Codex reads `.codex-plugin/plugin.json` and exposes workflows as `$flee-*` skills.
- Claude-compatible hosts read `.claude-plugin/plugin.json` and can expose the Markdown files in `commands/` as slash commands.
- Shared workflow logic lives in `skills/`; governance references live under `skills/flee-govern/references/`.

Platform tool names and permission systems differ. Scheduling, filesystem access, external calls, and other mutations must use the host platform's tools and approval model. The workflow documents do not override higher-level host instructions or permissions.

For future changes, update shared skills and commands first, record the change in `CHANGELOG.md`, update both manifest versions, validate on each target platform, and create a new versioned archive rather than overwriting an earlier export.
