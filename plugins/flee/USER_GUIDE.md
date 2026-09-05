# Flee User Guide for Codex

Flee is a privacy-first planner that stores plans as Markdown files in a folder you choose.

## Commands

| Command | Purpose | Example |
| --- | --- | --- |
| `$flee-plan` | Create or update a structured plan | `$flee-plan Launch a portfolio site by October` |
| `$flee-schedule` | Build a realistic timeline and propose optional reminders | `$flee-schedule plan-portfolio-site.md` |
| `$flee-next` | Choose one immediately startable action | `$flee-next plan-portfolio-site.md; I have 30 minutes` |
| `$flee-review` | Review statuses, diagnose slippage, and re-plan | `$flee-review plan-portfolio-site.md` |
| `$flee-improve` | Score and iteratively improve a plan or project | `$flee-improve plan-portfolio-site.md` |
| `$flee-govern` | Review or redesign a system as a persistent governance harness | `$flee-govern Review the operating structure of this repository` |
| `$flee-user-guide` | Display usage help | `$flee-user-guide` |

You can also ask naturally: “Use Flee to plan this,” “Use Flee to schedule my active plan,” or “What should I do next?”

## Workflow

1. Create a plan with `$flee-plan`.
2. Schedule it with `$flee-schedule` after confirming your real availability.
3. Begin each work session with `$flee-next`.
4. Run `$flee-review` when progress changes or at a regular review point.
5. Run `$flee-improve` for a scored refinement loop.
6. Run `$flee-govern` when a system needs reusable rules, control architecture, enforcement mapping, assurance, and persistent governance records.

## Governance harness

`$flee-govern` inventories the current structure, maps authority and rule precedence, chooses between improvement and ground-up rebuild, and proposes a versioned governance package. It covers controls, procedures, identity, security, privacy, storage, third parties, operations, testing, benchmarking, acceptance, failure/recovery, records, naming and UID conventions, notifications, defaults, fallbacks, exceptions, licenses, and applicable certification obligations.

The function distinguishes actual enforcement from human procedure, advice, and unapproved proposals. It will not claim compliance or certification without evidence and will not activate a harness without approval.

Governance design runs as a convergence loop. Every round branches from the current peak, is fully tested, scored, frozen, and snapshotted. Flee continues while the admissible peak improves, runs one confirmation round beyond the apparent peak, and automatically restores the highest-scoring state if a candidate drops, plateaus, fails a critical gate, or drifts from the locked mission. It then retests useful ideas from non-peak rounds on top of the peak so their potential can be retained without inheriting regressions.

## Files and privacy

Flee writes `plan-<short-name>.md` files only in your selected working folder. Reminder creation is optional and requires explicit approval of the exact schedule and prompt. External queries should be de-identified, and sensitive information must not leave the machine without confirmation.
