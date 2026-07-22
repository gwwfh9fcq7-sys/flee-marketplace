---
description: Lay a plan onto a timeline and set up gated reminders
argument-hint: [plan name or which plan]
allowed-tools: Read, Write, Edit, Glob, mcp__claude-code-remote__create_trigger, mcp__claude-code-remote__send_later, mcp__claude-code-remote__list_triggers, mcp__claude-code-remote__update_trigger, mcp__claude-code-remote__delete_trigger
---

Schedule the work for a plan and, only with explicit approval, set up reminders that
drive it forward. Target plan: $ARGUMENTS

Apply the `planning-method` skill and `references/scheduling-and-privacy.md`.

Steps — all mandatory, in order:

1. **Load the plan** from the working folder. Ask which one if ambiguous. If no plan
   exists, run `/plan` first.

2. **Confirm real capacity.** Ask for the person's actual availability — hours per day,
   working days, fixed commitments. Never invent availability.

3. **Lay out the timeline.** Order by dependency, then leverage. Protect the critical
   path. Add buffer. Propose concrete milestone and finish dates and get them confirmed.

4. **Run the scheduling gate.** No scheduled task is created until every part passes:
   - Confirm the person wants automation at all. Unclear → ask; never default to it.
   - State exactly what will run: cadence, time, what each reminder prompts, when it
     ends, and that each reminder starts a fresh session which will ask for access to
     the plan folder (the desktop app must be running for it to read the plan).
   - Get an explicit yes.
   - Create the scheduled task(s) with the host's scheduled-task tools.
   - Confirm back what was created and how to change or cancel it.
   Write every reminder prompt per the reminder-prompt rules in
   `references/scheduling-and-privacy.md`: self-contained, names the plugin and plan
   filename, instructs the session to request the plan folder, contains no personal or
   confidential details.

5. **Record the schedule** and every created reminder in the plan file's Schedule
   section. Update the file in place.

Privacy — mandatory: reminder prompts carry no sensitive details; the plan stays in the
working folder; de-identify before any external call; halt and get confirmation before
any step that would send sensitive data off the machine.
