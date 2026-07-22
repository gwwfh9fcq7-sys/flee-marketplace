---
description: Run self-directed improvement cycles on the active project until it plateaus
argument-hint: [project/plan in focus, optional]
allowed-tools: Read, Write, Edit, Glob
---

Run scored improvement cycles on the active project, raising it against its own mission
and success criteria until no further gain is possible with current tools.
Focus: $ARGUMENTS

Apply the `improvement-loop` skill in full.

Steps — all mandatory, in order:

1. **Identify the active project.** If "$ARGUMENTS" names one, use it. Otherwise use
   the active plan file in the working folder. Ask if ambiguous.

2. **Set the mission lock.** In flee plan files, read the mission from the Outcome
   and Why sections, and the success criteria from the Outcome plus each milestone's
   definition of done; halt and ask only if those sections are missing or empty. For
   any other artifact, halt and ask unless mission and success criteria are explicitly
   stated. Keep both anchors visible throughout.

3. **Run cycles** per the skill: full scan → impact-ranked scoreboard → top-5 dominance
   test → improve, functionality first, each change checked against the mission lock →
   re-assess. Print the scoreboard and a one-line change summary every pass.

4. **Loop to convergence; confirm the plateau.** Pass after pass without prompting,
   tracking the peak (best) version. Do not stop at the first small gain — take one pass
   past the apparent peak: when that pass yields no gain or declines, the visible drop
   confirms the plateau. Then roll back to the peak. Also stop on tool ceiling or
   mission lock. Expansion within the mission is allowed; a direction shift is rejected,
   not scored.

5. **Apply every change to the artifact in place, keeping the peak recoverable.** On
   stop, report: the peak score (what ships), the full trajectory including the
   confirming non-improving pass, whether a rollback occurred, what changed, and each
   open item with why it cannot be closed now.

Gates — mandatory: the loop edits the local artifact freely, but every scheduling
action and every external or sensitive-data action still passes its gate. De-identify
before any external call. Never send sensitive data off the machine without explicit
confirmation.
