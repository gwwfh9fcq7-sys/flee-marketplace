---
name: context-preload-audit
description: >
  This skill should be used when the user wants to measure or reduce what Claude
  Code loads into the context window at session start (plugins, user skills,
  SessionStart hooks, desktop extensions), or asks about "preload", "context
  window bloat", "startup tokens", "what is eating my context", or "trim my
  skills/plugins". Propose-only: it measures and recommends, never edits config.
---

# Context preload audit

Find out what every session pays before the first message, then propose the smallest set of trims that lose no functionality. Propose only; never edit config without the user's explicit go-ahead.

## What this does not measure
claude.ai connectors (claude.ai > Settings > Connectors), MCP server instructions, the built-in tool list, and per-tool descriptions of desktop extensions. Say so in every report; do not present the measured total as the whole picture.

## Procedure
1. Governance gate: if the environment has a session-open hook or MCP gate, call it first.
2. Measure (safe default): `python3 ${CLAUDE_PLUGIN_ROOT}/skills/context-preload-audit/measure.py` (or the skill directory path when installed as a bare user skill) (add `--json` for a machine-readable object after the report). It reads config files only and **does not execute SessionStart hook commands**; they are listed with size 0 and marked `[not run]`.
3. Hook sizes: read the commands under `hooks.SessionStart` in `~/.claude/settings.json`. Only if you trust them, re-run with `--run-hooks`; the script then executes each one through the shell (stdin closed, 25 s timeout) exactly as Claude Code would, and measures the output.
4. Baseline: run `--baseline` once on first use to write `baseline.json` next to the script. Later runs compare against it and report drift and new/gone items. `--reset` overwrites it.
5. Read the CANDIDATES list and turn each into a proposal for the user. The script never applies anything.
6. Before any trim, make a backup (layout below), apply the trim by hand, then run `--verify` (with `--run-hooks` if hooks changed).

## Backup layout (used by --verify)
```
~/.claude/skills_disabled/backup-<what>-<YYYYMMDD>/
  hook-output-before.txt          # hook context before the trim (see command below)
  <skill-name>.SKILL.md           # or <skill-name>/SKILL.md: full skill file before the trim
```
Hook snapshot: `<hook cmd> </dev/null | jq -r .hookSpecificOutput.additionalContext > <backupdir>/hook-output-before.txt`.
Pass `--backup DIR` to use a different directory. If nothing matches, `--verify` prints the exact paths and globs it looked for.

## Functionality preservation (the rule)
No tool, skill, hook, or extension may lose function or nuance for saved tokens. `--verify` checks:
- hook output is valid hook JSON, uses real newlines, and keeps every field of the snapshot;
- every backed-up user skill keeps a non-empty description, keeps all quoted trigger phrases, and has an unchanged body;
- disabled plugins and extensions are listed for explicit confirmation.
Any FAIL means revert the trim. A PASS with "nothing was compared" means no regression was detected, not that the trim is verified.

## Trim recipes (user edits the file; you propose)
- Plugin not used in this workflow: set `"<plugin>@<market>": false` under `enabledPlugins` in `~/.claude/settings.json`.
- Long user-skill description: shorten to one sentence plus quoted trigger phrases in `~/.claude/skills/<name>/SKILL.md`; keep every trigger phrase.
- Verbose SessionStart hook: reduce the hook to what a fresh session actually needs; keep the same JSON field set.
- Duplicate: a user skill also provided by an enabled plugin, or a desktop extension overlapping a plugin. Move or disable one, never both.

## Where things live
| Source | Location |
|---|---|
| Plugins on/off | `~/.claude/settings.json` → `enabledPlugins` |
| Plugin content | `~/.claude/plugins/cache/<market>/<plugin>/<version>/{agents,skills,commands}` |
| User skills | `~/.claude/skills/<name>/SKILL.md` (only the description is preloaded) |
| SessionStart hooks | `~/.claude/settings.json` → `hooks.SessionStart[].hooks[].command` |
| Desktop extensions | macOS `~/Library/Application Support/Claude/Claude Extensions Settings/*.json`; Windows `%APPDATA%\Claude\Claude Extensions Settings`; Linux `~/.config/Claude/Claude Extensions Settings` → `isEnabled` |
| Connectors | claude.ai > Settings > Connectors (not measurable locally) |

## Pitfalls
- Size estimates use chars/4 as tokens; they compare well run to run, not against billing.
- A plugin's agents count as well as its skills; disabling a plugin removes both.
- Never shorten a description by dropping the phrases users say to trigger it.
- Missing or invalid `settings.json`, or no extension directory, is reported, not fatal.
