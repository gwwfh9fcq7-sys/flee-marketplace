---
name: flee-improve
description: Run scored improvement cycles on the active plan or project until it reaches a confirmed plateau. Use when the user invokes $flee-improve, asks Flee to optimize a plan, or requests the former /improve command.
---

# Flee improve command

Apply the `improvement-loop` skill in full.

1. Identify the target plan/project; ask only if ambiguous.
2. Lock its mission and explicit success criteria.
3. Repeat full scan, impact-ranked scoreboard, dominance test, mission-checked edits, and re-scoring. Show the scoreboard and one-line change summary each pass.
4. Continue one pass beyond the apparent peak. If that pass does not improve the score, roll back to the best version.
5. Keep the peak recoverable and report the peak score, trajectory, rollback status, changes, and unresolved items.

Scheduling and external/sensitive-data actions retain their approval gates.
