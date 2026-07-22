---
name: improvement-loop
description: >
  This skill should be used to run scored, self-directed improvement cycles on the
  active project or plan currently in focus. Trigger when the user asks to run an
  improvement pass, "score and refine", "optimize the plan", or make the active
  project or plan as good as it can be, or when the planning method calls for
  refinement between phases. Not for ordinary editing, rewording, or shortening
  requests. Underpins the /improve command.
version: 0.3.0
---

# Improvement loop

Raise the active project against its own mission and success criteria through repeated
score → improve → re-score cycles, prioritized by impact, until no further gain is
possible with current tools. Sharpen what the project already is; never invent new
directions.

## Mission lock — set before any cycle

Fix two anchors and keep them visible throughout:

- **Mission** — what the project is for.
- **Success criteria** — what "good" and "done" mean, concretely.

In flee plan files, read the mission from the Outcome and Why sections, and the
success criteria from the Outcome plus each milestone's definition of done. Halt and
ask only if those sections are missing or empty. For any other artifact, halt and ask
unless mission and success criteria are explicitly stated.

Test every proposed change against the anchors:

- Expansion within the mission — doing the defined job more completely or more
  robustly — is allowed.
- A direction shift — moving toward a goal the mission did not contemplate — is
  rejected and noted, regardless of score impact.

## Scoring model

Define measurable criteria bound to the project. Each criterion has a name, a one-line
measurable definition, a weight (0–100, its impact on the outcome), and a current
score (0–100). Criteria must cover at minimum: functionality/correctness,
completeness, robustness, clarity, and alignment to the success criteria.
Functionality criteria carry the highest weights.

Two derived numbers:

- **Overall score** = Σ(weight × score) / Σ(weight).
- **Improvement potential** per criterion = weight × (100 − score). This ranks the
  scoreboard.

## One cycle

1. **Full scan.** Score every criterion. No skipping.
2. **Scoreboard.** Rank all criteria by improvement potential, highest first. Present
   as a table: criterion, weight, score, potential.
3. **Top-5 dominance test.** Sum the top 5 potentials against the sum of all the rest.
   Top 5 greater → focus the cycle entirely on them. Not greater → still work them
   first, and state that more passes will be needed.
4. **Improve — functionality first.** Within the prioritized set: functional
   correctness and completeness, then robustness, then clarity and polish. Check every
   change against the mission lock before applying it to the artifact.
5. **Re-assess.** Re-score what changed, recompute the overall score, record the delta.

## Run to convergence — confirm the plateau, keep the peak

Track the **peak**: the highest-scoring version so far. Before a pass edits the
artifact, retain the current version so it can be restored.

Start the next cycle automatically after each one. **Do not stop at the first small
gain.** Keep going until a full pass fails to beat the peak — it produces no net gain,
or the score declines. That non-improving pass is the proof: the visible flatline or
decline confirms the peak is already behind you, so the plateau is observed, not
guessed.

When that confirming pass comes in at or below the peak, **roll back** the artifact to
the peak version — discard the confirming pass's changes — then stop. The peak is what
ships.

Stop conditions:

- **Plateau confirmed** — the pass taken one past the peak yields no gain or a decline;
  roll back to the peak.
- **Tool ceiling** — remaining gains need capabilities not available; name them.
- **Mission lock** — only direction shifts remain.

On stop, report: the peak overall score (what ships), the full trajectory across passes
**including the confirming non-improving pass, so the decline is visible as proof**,
whether a rollback occurred, what changed, and every open item with the reason it cannot
be closed now.

## Autonomy and gates

Run cycles back-to-back without prompting. Print the scoreboard and a one-line change
summary every pass. Halt at any stop condition and report. The loop edits the local
artifact freely, but every scheduling action and every external or sensitive-data
action still passes its gate (see the planning-method rules). Never send sensitive
data off the machine without explicit confirmation.

Worked example: `references/scoring-rubric.md`.

## Anti-patterns

- Polishing while functionality is broken.
- Counting a direction shift as an improvement.
- Stopping at the first small gain instead of taking one pass past the peak to confirm
  the plateau.
- Shipping a regressed final pass instead of rolling back to the peak.
- Failing to recognize the tool ceiling.
- Editing the artifact without a scoreboard and change summary.
- Running without mission and success criteria set.
