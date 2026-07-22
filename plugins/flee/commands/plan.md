---
description: Turn an idea or brain-dump into a structured, actionable plan
argument-hint: [idea or goal]
allowed-tools: Read, Write, Edit, Glob
---

Turn the following into a structured, actionable plan:
$ARGUMENTS

Apply the `planning-method` skill. Push back on vagueness; surface unstated assumptions.

Steps — all mandatory, in order:

1. **Clarify the outcome.** If "$ARGUMENTS" is empty or the goal is not observable, ask
   one sharp clarifying question and wait for the answer. Capture: what "done" looks
   like in observable terms, the why in one line, and hard constraints (deadline,
   dependencies, budget, fixed format).

2. **Confirm capacity.** Ask for the person's real available time — block length and
   days — unless already stated. Size every action to fit one block.

3. **Decompose.** Milestones, each with a one-line definition of done. Verb-first
   actions with rough effort estimates. One action per work session for multi-session
   work. Flag every dependency, blocker, and unknown; unknowns become research actions.

4. **Identify the critical path** — the chain that sets the finish date.

5. **Write the plan file.** Confirm a working folder is connected before writing; if
   none is, ask the person to pick one and wait. Follow the plan-file guide in
   `references/plan-template.md`. Name the file `plan-<short-name>.md`. If a plan file
   for this outcome already exists, update it in place.

6. **Close.** Summarize in a few lines, state the single next action, and offer
   `/schedule` or `/next`.

Privacy — mandatory: keep the plan file in the working folder only; de-identify before
any external search or call; halt and get confirmation before any step that would send
sensitive data off the machine.
