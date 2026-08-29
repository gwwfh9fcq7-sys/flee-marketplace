---
name: flee-schedule
description: Put a Flee plan on a realistic timeline and optionally create explicitly approved reminders. Use when the user invokes $flee-schedule, asks Flee to schedule a plan, or requests the former /schedule command.
---

# Flee schedule command

Apply the `planning-method` skill and its scheduling/privacy reference.

1. Load the named plan from the working folder; ask which one only when ambiguous. If none exists, use `$flee-plan` first.
2. Confirm actual hours, working days, and fixed commitments. Never invent availability.
3. Sequence by dependency and leverage, protect the critical path, add buffer, and confirm milestone and finish dates.
4. Treat reminders as optional. Before creating any automation, state cadence, time, prompt, end condition, local-folder access needs, and require an explicit yes. Use the host's automation tools only after approval.
5. Record the confirmed schedule and any reminders in the plan file.

Reminder prompts must contain no confidential details. Keep the plan local and de-identify external calls.
