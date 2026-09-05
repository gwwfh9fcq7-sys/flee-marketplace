# Governance assurance rubric

Score each dimension 0–5 with evidence. Freeze the rubric and weights before round 0. Weighted score is advisory; mission fit and critical gates control admissibility.

| Dimension | Weight | What good looks like |
| --- | ---: | --- |
| Authority and precedence | 15 | Sources verified; conflicts and exceptions resolve deterministically |
| Scope and applicability | 10 | Boundaries, assets, actors, environments and exclusions are explicit |
| Control completeness | 15 | Material risks and lifecycle stages have preventive/detective/corrective coverage |
| Enforceability | 15 | Mandatory controls map to real mechanisms or accountable procedures |
| Traceability and records | 10 | Bidirectional links, stable UIDs, versioning and append-only decisions exist |
| Security, privacy and identity | 10 | Threats, data duties and authorization boundaries are tested |
| Resilience and recovery | 10 | Failure, fallback, rollback, backup and restore paths are proven |
| Testability and evidence | 10 | Measures, thresholds, tests, owners and durable evidence are defined |
| Operability and usability | 5 | Defaults, modes, notifications, troubleshooting and ownership are usable |

## Critical gates

Reject or hold the harness when any applicable gate fails:

- unresolved authority conflict affecting a mandatory control;
- critical asset, data flow, privileged identity, or external dependency unaccounted for;
- mandatory control claimed as enforced without a mechanism or accountable procedure;
- no safe failure, rollback, recovery, or restore path for a critical operation;
- acceptance criteria lack an executable test or review method;
- material legal, regulatory, contractual, certification, license, security, or privacy claim is unverified;
- exception lacks authority, compensating control, expiry, or revocation condition;
- records can be silently overwritten or UIDs reused.

## Mission-drift gate

Reject the round when it improves its numeric score by changing the mission, success criteria, applicable scope, authority hierarchy, scoring weights, acceptance thresholds, or definition of a mandatory requirement without an explicit authorized decision. Also reject unapproved scope expansion and loss of any previously satisfied mandatory control.

Scores are comparable only when they use the same frozen rubric and mission lock. Record uncertainty; do not manufacture precision where evidence is qualitative.

## Readiness verdicts

- `ACCEPT`: all critical gates pass, score ≥ 85%, and no dimension is below 3.
- `CONDITIONAL`: critical gates pass, score 70–84%, with owned, dated corrections.
- `REJECT`: any critical gate fails, score < 70%, or the evidence is insufficient to evaluate.

For every failed test record expected result, observed result, impact, owner, correction, retest condition, and status. Re-score after correction and preserve both results.
