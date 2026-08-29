---
name: flee-govern
description: Review a system from a governance and enforceability perspective, then propose or build a ground-up or improved reusable governance harness. Use when the user invokes $flee-govern or asks for governance architecture, operating controls, standards, assurance, lifecycle enforcement, or persistent workflow structure. Do not use for an ordinary plan review or a narrow policy rewrite.
---

# Flee governance harness

Design a contained, persistent governance workflow around the target system. Apply Flee's planning discipline and improvement-loop logic, but optimize for authority, repeatability, traceability, enforceability, assurance, and safe recovery.

The harness must distinguish:

- **binding controls** actually enforced by a system, contract, law, configuration, or authorized operator;
- **required procedures** that depend on accountable human execution;
- **recommended guidance** that is advisory;
- **proposed controls** not yet approved or implemented.

Never describe a document as enforcement when no enforcement mechanism exists. Do not invent legal, regulatory, certification, licensing, privacy, security, or vendor requirements. Verify authoritative requirements when the task allows research; otherwise label them `UNVERIFIED` and block acceptance where material.

## Workflow

1. **Frame the governed system.** Establish purpose, owners, users, assets, data classes, environments, lifecycle, dependencies, third parties, jurisdictions, threat/failure assumptions, and out-of-scope areas. Ask only for omissions that would materially change the harness.
2. **Map authority and precedence.** Identify applicable system/developer/user instructions, law/regulation, contracts, licenses, certifications, organizational policy, product standards, local conventions, and temporary exceptions. Record source, owner, scope, effective date, expiry/review date, verification state, and conflict rule. Higher authority overrules lower authority; a specific applicable rule beats a general peer rule unless its source says otherwise. Unresolved conflicts fail closed.
3. **Review the current structure.** Inventory existing rules, workflows, controls, artifacts, tests, records, naming/UID schemes, approvals, notifications, recovery paths, defaults, fallbacks, and enforcement points. Trace each requirement to implementation, evidence, and owner. Mark absent, ambiguous, duplicated, conflicting, unenforced, untested, stale, or orphaned elements.
4. **Choose the intervention.** Select `IMPROVE` only when the current structure has a coherent authority model, stable identifiers, usable traceability, and recoverable change control. Select `REBUILD` when foundations are contradictory, non-auditable, unsafe, or structurally incomplete. Explain the decision and migration risk.
5. **Design the harness.** Cover the domains and minimum controls in [control domains](references/control-domains.md). Use the canonical artifacts, identifiers, states, and traceability model in [harness format](references/harness-format.md). Define prevention, detection, response, recovery, evidence, ownership, measures, tests, acceptance, rejection, correction, and exception handling for every material control.
6. **Lock and baseline.** Freeze the mission, success criteria, scope, authority hierarchy, critical gates, and scoring weights. Score and snapshot the initial proposal as round `RND-0000`; this baseline is immutable.
7. **Loop to convergence.** Run the cumulative [convergence loop](references/convergence-loop.md) on top of the highest-scoring admissible frozen round. Each round must be tested, scored, frozen, snapshotted, and either promoted or rejected. Continue while the peak improves, then run one confirmation round past the apparent peak. Mission drift or any critical-gate failure rejects a round regardless of score.
8. **Restore and synthesize the peak.** When a round drops, plateaus, drifts, or fails, automatically restore the highest-scoring admissible frozen state. Inspect non-peak rounds for useful ideas and retest each worthwhile idea as a clean candidate on top of the peak; never merge a regression merely to retain a feature.
9. **Propose before applying.** Present the peak architecture, full score trajectory, decisions, unresolved questions, migration/rollback plan, enforcement gaps, and acceptance evidence. Do not modify the governed system, activate controls, contact third parties, schedule notifications, or claim certification without explicit authority.
10. **Persist approved output.** With approval, write the harness under `governance/<system-slug>/`; preserve stable UIDs, frozen round snapshots, append-only decisions/change records, versioned artifacts, status transitions, evidence links, and a last-reviewed date. Re-run the convergence loop after every material update.

## Required final report

Return: intervention (`IMPROVE` or `REBUILD`), readiness verdict, critical gaps, proposed hierarchy, harness components, enforcement map, every round and score delta, selected peak, rollback status, recovered non-peak ideas, assurance scorecard, rejected items and reasons, stopping condition, decisions needed, migration/rollback outline, and the single next action.

Keep sensitive system details local. External research and third-party actions require the normal privacy and authorization gates.
