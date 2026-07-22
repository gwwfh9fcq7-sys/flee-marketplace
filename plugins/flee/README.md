# FLEE

**Privacy-first planner that scores your plan and improve-loops it to its peak.**

Structured planning, scheduling, execution, and review for real projects, working from
plain Markdown plan files in a folder you choose.

## Components

**Skills**

- `planning-method` — clarify the outcome, decompose into milestones and next actions,
  sequence and schedule, drive execution, review and re-plan. Includes the plan-file
  guide and the scheduling/privacy rules.
- `improvement-loop` — scored improvement cycles on the active plan or project:
  scan, rank gaps by impact, fix functionality first, re-score, repeat to convergence,
  bounded by the project's own mission.

**Commands**

- `/plan [idea]` — turn an idea or brain-dump into a plan file.
- `/schedule [plan]` — lay the plan onto a timeline; reminders are created only after
  you approve exactly what will run.
- `/next [plan]` — the single next action to work on right now.
- `/review [plan]` — set honest statuses, diagnose what slipped, re-plan.
- `/improve [project]` — run improvement cycles on the active plan until it plateaus.

## Setup

No external services or API keys. On first use, pick a working folder when prompted —
plans are read and written only there.

## Usage

Start with `/plan`. Use `/next` when you sit down to work, `/review` to keep the plan
honest, `/schedule` for a timeline and optional reminders, `/improve` to refine the
active plan. Describing a goal in plain language also engages the planning method.

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
