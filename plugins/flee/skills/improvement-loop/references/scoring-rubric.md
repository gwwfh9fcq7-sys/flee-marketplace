# Scoring rubric — worked example

One improvement loop on an example project. Numbers are illustrative; derive real
weights from the project's mission and success criteria.

## Mission lock (anchors)

- **Mission:** ship a working onboarding email sequence that activates new signups.
- **Success criteria:** 5 emails drafted, reviewed, scheduled in the tool, and
  measurably tied to an activation metric.

Anything outside this — e.g. "also build a referral program" — is a direction shift
and is rejected, regardless of score impact.

## Criteria table (pass 1 scan)

| Criterion | Weight | Score | Improvement potential (w × (100−s)) |
|---|---|---|---|
| Functional completeness (all 5 emails exist) | 30 | 40 | 1800 |
| Activation metric wired | 25 | 20 | 2000 |
| Copy clarity / correctness | 20 | 60 | 800 |
| Sequence timing logic | 15 | 50 | 750 |
| Brand/tone consistency | 5 | 70 | 150 |
| Formatting polish | 3 | 80 | 60 |
| Accessibility of templates | 2 | 75 | 50 |

**Overall score (pass 1)** = Σ(w×s)/Σw = 4390 / 100 = **43.9**

## Dominance test

Top 5 by potential: Activation metric (2000) + Functional completeness (1800) + Copy
clarity (800) + Sequence timing (750) + Brand/tone (150) = **5500**.
Rest: Formatting (60) + Accessibility (50) = **110**.

5500 > 110 → the top 5 dominate. Focus the cycle on them; leave formatting and
accessibility for a later pass.

## Improve — functionality first

Order within the top 5:

1. Activation metric wired — define and connect the metric.
2. Functional completeness — draft the 2 missing emails.
3. Sequence timing logic — fix the send-day spacing.
4. Copy clarity — tighten the 3 weakest emails.
5. Brand/tone — align voice.

Each change is checked against the mission lock before applying. A tempting "add a
referral email" is rejected — direction shift.

## Re-assess (pass 1 → pass 2 scan)

| Criterion | Weight | Score after |
|---|---|---|
| Functional completeness | 30 | 95 |
| Activation metric wired | 25 | 90 |
| Copy clarity / correctness | 20 | 85 |
| Sequence timing logic | 15 | 90 |
| Brand/tone consistency | 5 | 90 |
| Formatting polish | 3 | 80 |
| Accessibility of templates | 2 | 75 |

**Overall score (pass 2)** = 8990 / 100 = **89.9** — delta **+46.0**.

## Convergence trajectory — confirm, then roll back to the peak

- Pass 1 → 43.9
- Pass 2 → 89.9  (+46.0)
- Pass 3 → 94.2  (+4.3)
- Pass 4 → 94.8  (+0.6) — a small gain, but not yet confirmed; take one pass more
- Pass 5 → 94.5  (−0.3) — the confirming pass **declines**. The visible drop proves
  pass 4 (94.8) was the peak.

**Stop:** plateau confirmed. Roll back to the pass-4 version; **94.8** is the delivered
score. No mission-lock violations occurred. The remaining gap to 100 is a tool ceiling —
true activation measurement needs analytics that are not connected. The loop reports the
full trajectory (including the pass-5 decline), the rollback, the changes made, and the
open item (connect analytics).
