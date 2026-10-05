# Governance convergence loop

Run successive, cumulative improvement rounds after the baseline harness is designed. A round may build on the current peak only; never build on a rejected or drifting state.

## Mission lock

Before round 0, freeze:

- governed-system mission and success criteria;
- scope and exclusions;
- authority hierarchy and non-negotiable constraints;
- critical assurance gates;
- scoring rubric and weights.

Changing the mission lock starts a new loop and requires an explicit decision. Do not improve the score by weakening tests, removing applicable scope, reclassifying mandatory controls, or changing weights.

## Round protocol

For every round `RND-<NNNN>`:

1. **Branch from peak.** Use the highest-scoring admissible frozen round, not merely the latest round.
2. **Gap scan.** Rank weaknesses and unrealized potential by mission impact, risk reduction, enforceability, assurance gain, and implementation cost. Apply a top-five dominance test: work outside the top five only when it is prerequisite or nearly free.
3. **Improve cumulatively.** Preserve validated strengths. Integrate compatible strengths discovered in any earlier candidate, including rejected rounds, only after isolating the useful change and retesting it on top of the peak.
4. **Test.** Run all critical gates plus affected regression tests. A critical failure, authority conflict, mission drift, unapproved scope expansion, or loss of a previously satisfied mandatory requirement makes the round inadmissible regardless of score.
5. **Score.** Use the frozen rubric. Record dimension scores, weighted total, critical-gate results, evidence, delta from parent, delta from peak, and uncertainty.
6. **Freeze and snapshot.** Write a new immutable round directory and manifest. Record content hashes when available. Never edit a frozen round; corrections create another round.
7. **Promote or reject.** Promote only an admissible round whose score exceeds the peak. Equal scores promote only when the candidate materially lowers risk, complexity, cost, or uncertainty without regression; record the tie-break. Otherwise retain the peak and mark the candidate `REJECTED`.

## Convergence and rollback

Continue without prompting while admissible improvement remains possible with current authority and tools. After an apparent peak, run one deliberate confirmation round targeting the strongest remaining opportunity.

Stop when the confirmation round:

- scores below the peak;
- fails to improve under the tie-break rule;
- drifts from the mission lock;
- fails a critical gate;
- exhausts actionable improvements with available evidence/tools; or
- requires new authority, sensitive external action, or a material user decision.

On stop, automatically restore the working proposal to the frozen peak. Do not delete later rounds; preserve them as evidence. Mark the peak `SELECTED`, create/update `PEAK.md`, and verify its hashes and critical gates before completion.

## Peak-potential synthesis

Before finalizing, inspect every non-peak round for independently valuable controls, tests, procedures, evidence patterns, or simplifications. Attempt each compatible high-value item as a fresh candidate based on the peak. Keep it only if it produces a new admissible peak. This fulfills the potential of explored versions without merging their regressions or drift.

## Required trajectory report

Report every round in order: UID, parent, status, score, delta, critical gates, mission-fit result, changes, and rejection reason. State the selected peak, whether rollback occurred, which ideas were recovered from non-peak rounds, the stopping condition, and unresolved opportunities.
