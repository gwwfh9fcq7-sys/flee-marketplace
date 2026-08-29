---
name: flee-review
description: Review a Flee plan, set honest statuses, diagnose slippage, and re-plan. Use when the user invokes $flee-review, asks Flee to review progress, or requests the former /review command.
---

# Flee review command

Apply the review and re-plan section of the `planning-method` skill.

1. Load the target plan. For an all-plans review, scan `plan-*.md` and flag approaching dates and stale reviews.
2. Set every milestone/action to done, in progress, not started, or blocked. Ask rather than guessing. Split partial work into completed and remaining actions.
3. Classify stuck work as no time, external blocker, or wrong scope.
4. Re-estimate, re-sequence, cut scope, or move dates honestly. Re-run the approval gate before changing reminders.
5. Update the plan, schedule, and dated append-only log entry.
6. End with one next action.

Keep plan content local and de-identify external calls.
