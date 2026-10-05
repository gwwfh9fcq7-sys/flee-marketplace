# FLEE

**Privacy-first planner that scores your plan and improve-loops it to its peak.**

Version 0.3.1 · **now dual-platform** — runs natively on both Claude and Codex.

Structured planning, scheduling, execution, and review for real projects, working from
plain Markdown plan files in a folder you choose. 0.3.1 adds `/govern`, a skill for
designing persistent governance harnesses on top of any system you're building.

## What's new in 0.3.1

- **Dual-platform support** — ships a `.codex-plugin/plugin.json` alongside the
  existing `.claude-plugin/plugin.json`, so the same package installs on Codex or on
  Claude. Codex exposes the workflows as `$flee-*` skills (`flee-plan`, `flee-next`,
  `flee-schedule`, `flee-review`, `flee-improve`, `flee-user-guide`); Claude-compatible
  hosts keep the familiar `/plan`, `/next`, `/schedule`, `/review`, `/improve` slash
  commands. See `PLATFORM_NOTES.md`.
- **`/govern`** — a new command and `flee-govern` skill for reviewing or redesigning a
  persistent governance harness: authority hierarchy, control domains, canonical
  artifacts, stable UIDs, assurance scoring, critical acceptance gates, and a
  convergence loop with immutable round snapshots, drift rejection, and automatic
  rollback to the last peak.
- Full history in `CHANGELOG.md`.

## Components

**Skills**

- `planning-method` — clarify the outcome, decompose into milestones and next actions,
  sequence and schedule, drive execution, review and re-plan. Includes the plan-file
  guide and the scheduling/privacy rules.
- `improvement-loop` — scored improvement cycles on the active plan or project:
  scan, rank gaps by impact, fix functionality first, re-score, repeat to convergence,
  bounded by the project's own mission.
- `flee-govern` — persistent governance-harness design and review; reference material
  lives under `skills/flee-govern/references/`.
- `flee-plan`, `flee-next`, `flee-schedule`, `flee-review`, `flee-improve`,
  `flee-user-guide` — Codex-side adapters that expose the same workflows as `$flee-*`
  skills for hosts that don't read `commands/`.

**Commands**

- `/plan [idea]` — turn an idea or brain-dump into a plan file.
- `/schedule [plan]` — lay the plan onto a timeline; reminders are created only after
  you approve exactly what will run.
- `/next [plan]` — the single next action to work on right now.
- `/review [plan]` — set honest statuses, diagnose what slipped, re-plan.
- `/improve [project]` — run improvement cycles on the active plan until it plateaus.
- `/govern [system]` — review or design a persistent governance harness for a system.

## Setup

No external services or API keys. On first use, pick a working folder when prompted —
plans are read and written only there.

## Usage

Start with `/plan`. Use `/next` when you sit down to work, `/review` to keep the plan
honest, `/schedule` for a timeline and optional reminders, `/improve` to refine the
active plan, `/govern` to design or review a governance harness. Describing a goal in
plain language also engages the planning method.

On Codex, use the equivalent `$flee-*` skills instead of slash commands — see
`USER_GUIDE.md` and `PLATFORM_NOTES.md` for platform-specific details.

## Reminders

Reminders are optional and are created only after you approve the exact cadence, time,
and prompt. Each reminder runs as a fresh session: it asks for access to your plan
folder before reading anything, and the desktop app must be running for it to reach
the plan. Reminder prompts never contain personal or confidential details.

## Data handling

Plan files are stored only in your working folder. Plan content is processed by the
model to do the work. Before any web search or connected-service call, identifying and
sensitive details are removed and the query runs on the generic substance. Nothing is
scheduled, and no sensitive data leaves your machine to an external service, without
your explicit approval.

## License

MIT — see LICENSE.
