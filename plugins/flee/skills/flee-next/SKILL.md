---
name: flee-next
description: Select the single highest-value next action from a Flee plan. Use when the user invokes $flee-next, asks what to do next, or requests the former /next command.
---

# Flee next command

Apply the execution section of the `planning-method` skill.

1. Load the named plan or ask which plan when ambiguous.
2. Confirm the time available if it was not supplied.
3. Return exactly one verb-first action that fits the time and has no open decisions. Split oversized work in the plan; if blocked, return the unblocking action.
4. Give only enough context to begin immediately and offer to help with the first piece.
5. When the user confirms completion, mark it done in the plan and offer the next action.

The output is one clear action, not a status report. Keep plan content local.
