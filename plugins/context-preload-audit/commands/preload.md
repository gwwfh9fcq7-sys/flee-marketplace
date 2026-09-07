---
description: Measure what Claude Code preloads at startup and propose safe trims
argument-hint: [--run-hooks | --baseline | --verify]
allowed-tools: Bash, Read, Glob
---

Audit the session's startup context load. Arguments: $ARGUMENTS

Apply the `context-preload-audit` skill. Steps, in order:

1. Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/context-preload-audit/measure.py $ARGUMENTS`
   and show the full table. Do not add `--run-hooks` unless the user passed it; hook
   commands are only executed with that flag and explicit consent.
2. State what is not measured (claude.ai connectors, MCP instructions, built-in tools).
3. List trim candidates ranked by tokens saved, each with what functionality it touches.
4. Propose; do not edit any config. If the user approves a trim, back up first, then
   re-run with `--verify --backup <dir>` and report PASS/FAIL.
