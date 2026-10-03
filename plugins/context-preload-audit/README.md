# context-preload-audit

**Measure what Claude Code preloads at startup and propose trims that lose no functionality.**

Every session pays for enabled plugins, user skills, SessionStart hooks, and desktop
extensions before the first message. This plugin measures that cost, tracks drift against
a baseline, and verifies that a trim did not break anything. It proposes; it never edits
your config.

## Components

**Skills**

- `context-preload-audit` — the audit procedure, backup layout, functionality
  preservation rule, trim recipes, and where each preload source lives on macOS,
  Windows, and Linux. Ships `measure.py` (Python 3.9+, standard library only).

**Commands**

- `/context-preload-audit:preload [flags]` — run the measurement and get a ranked
  proposal. Flags pass straight to `measure.py`.

## Usage

```bash
python3 measure.py                 # measure; hook commands listed but NOT executed
python3 measure.py --run-hooks     # also execute SessionStart hooks to size their output (asks consent)
python3 measure.py --baseline      # write baseline.json on first run; later runs report drift
python3 measure.py --verify --backup <dir>   # no-regression check of a trim against your backup
python3 measure.py --json          # machine-readable object appended to the report
```

Tokens are estimated as characters / 4.

## Safety

- Reads config only. Writes nothing except `baseline.json` next to the script when you
  pass `--baseline`.
- No network. No dependencies.
- Executes commands only with `--run-hooks`, and only the SessionStart hook commands
  already configured in your own `settings.json`.

## Not measured

claude.ai connectors, MCP server instructions, the built-in tool list, and per-tool
descriptions of desktop extensions. The report says so every time.
