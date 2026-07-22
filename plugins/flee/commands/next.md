---
description: Surface the single most useful next action right now
argument-hint: [plan name and/or time available]
allowed-tools: Read, Edit, Glob
---

Surface the single highest-value next action to work on right now. Context: $ARGUMENTS

Apply the `planning-method` skill (Drive execution).

Steps — all mandatory, in order:

1. **Load the plan.** If the person named a plan or gave a focus, select it. Otherwise
   list the plan files in the working folder and ask which one.

2. **Confirm available time** if not stated.

3. **Return ONE action.** Verb-first, fits the available time, no open decisions.
   Weigh what's done, what's blocked, and the critical path. If the best action is
   larger than the available time, split it in the plan file into session-sized actions
   and return the first one. If everything is blocked, return the unblocking action.

4. **Make it startable.** Give just enough context to begin immediately. Offer to do
   the first piece together when it is something Claude can produce.

5. **On completion,** tick the action in the plan file and offer the next one.

Output is one clear "do this next" — never a status report.
Privacy — mandatory: plan content stays in the working folder; de-identify before any
external call.
