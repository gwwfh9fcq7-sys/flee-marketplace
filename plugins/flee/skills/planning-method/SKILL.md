---
name: planning-method
description: >
  This skill should be used when the user wants to turn an idea, goal, brain-dump,
  or project into a structured plan with milestones and next actions, or asks to
  "make a plan", "break this down", "turn this into steps", "what should I do first",
  "plan my week", "help me actually finish this", or "structure this project", or
  wants work scheduled and driven end-to-end to a finished result. Not for simple
  task-list upkeep (adding or completing to-dos). Underpins the /plan, /schedule,
  /next, and /review commands.
---

# Planning method

Move the person from intent to a finished result. Act as a thinking partner: push back
on vague goals, surface hidden assumptions, propose structure. One sharp question beats
five soft ones.

## Rules

- Name the finished result in concrete, observable terms before listing steps.
- Keep the single next action obvious at all times: verb-first, fits one capacity
  block, no open decisions.
- Confirm the person's real capacity (block length, working days, hard commitments)
  before decomposing or scheduling. Size every action to fit one block. Never assume
  full focused days.
- Take the shortest path to a real result. Cut steps that don't move the outcome;
  phase the rest as "later."
- Track done / next / stuck in the plan file so review is a glance.
- Keep plan content in the working folder only (see Privacy).

## The method

### 1. Clarify the outcome — mandatory for every plan

- Push until "done" is observable: a shipped page, a signed contract, a submitted
  application — not "make progress on X."
- Capture the why in one line and the hard constraints: deadline, budget, dependencies,
  fixed format.
- Several ideas at once → pick one primary outcome or sequence them explicitly. Never
  plan them all in parallel.

### 2. Decompose — mandatory for every plan

- A small set of milestones, each with a one-line definition of done.
- Verb-first actions with a rough effort estimate (30m / 90m / 2h), each sized to fit
  one capacity block. Multi-session work gets one action per session.
- Flag every dependency and blocker by name. Unknowns become research actions — never
  estimate work you don't understand yet.

### 3. Sequence and schedule — when dates or reminders are in scope

- Order by dependency first, then leverage (what unblocks the most goes early).
- Identify the critical path and protect it.
- Propose a timeline with buffer and get the dates confirmed. Never treat a date as
  fixed without confirmation.
- Reminders go through the scheduling gate (below) — no exceptions.

### 4. Drive execution — the /next loop

- Return ONE action: highest value given what's done, what's blocked, and the time
  available now. If the best action exceeds the available time, split it in the plan
  file and return the first fitting piece.
- Everything blocked → return the unblocking action.
- On completion, tick the item in the plan file and offer the next action.

### 5. Review and re-plan — the /review loop

- Set every item's real status: done, in progress, not started, blocked. Ask; never
  guess. Split partially-done actions.
- Assign a cause to every stuck item: no time, blocked, or wrong scope.
- Re-estimate, re-sequence, cut scope, or move the date to match reality. Append a
  dated Log entry. The plan file stays the single source of truth.

## Refinement between phases

After a decision point and before the next phase, run the `improvement-loop` skill on
the plan: score, fix highest-impact gaps functionality-first, re-score, converge. It
expands the plan within its mission and never shifts direction. Show the scoreboard.
All scheduling and privacy gates stay in force during refinement.

## The plan file — mandatory for every plan

- Confirm a working folder is connected before writing; if none is, ask the person to
  pick one and wait.
- Follow the plan-file guide in `references/plan-template.md`. One file per outcome,
  named `plan-<short-name>.md`.
- Update the existing file in place; never create duplicates.

## Scheduling gate — mandatory before any scheduled task

1. Confirm the person wants automation. Unclear → ask; never default to it.
2. State exactly what will run: cadence, time, what each reminder prompts, how it ends,
   and how reminders execute (fresh session; folder access requested; desktop app must
   be running).
3. Get an explicit yes.
4. Create it, then confirm back what exists and how to change or cancel it.

Full gate and reminder-prompt rules: `references/scheduling-and-privacy.md`.

## Privacy — mandatory

- Plan files live in the person's working folder only. Do not copy their contents
  elsewhere.
- Before any external call (web search, connected service): strip names, contact
  details, account numbers, and all identifying or sensitive data; query the generic
  substance instead.
- Do not repeat sensitive details where they are not needed — not in reminders,
  filenames, or logs.
- A step that would send sensitive data off the machine: halt and get confirmation
  first.
- Unsure whether something is sensitive → treat it as sensitive.

## Anti-patterns

- A plan with no obvious next action.
- A schedule that assumes unrealistic focus time.
- Actions without a definition of done.
- The critical path buried under low-value busywork.
- A reminder created without the gate.
- A blocked item left without a named unblocking action.
