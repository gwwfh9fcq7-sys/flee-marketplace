# Persistent harness format

Create only the artifacts needed for the governed system, but preserve this canonical topology and identifiers.

```text
governance/<system-slug>/
  GOVERNANCE.md          charter, scope, authority hierarchy, roles
  CONTROL-CATALOG.md     requirements and enforcement/evidence map
  OPERATIONS.md          preflight, run, post-op, failure and recovery procedures
  ASSURANCE.md           measures, tests, benchmarks, acceptance and validation
  REGISTRY.md            components, services, data, dependencies, licenses/certifications
  DECISIONS.md           append-only decision and exception records
  CHANGELOG.md           append-only harness changes and review history
  PEAK.md                selected peak round, score, hashes and selection reason
  rounds/
    RND-0000/            immutable baseline snapshot and round manifest
    RND-0001/            immutable cumulative candidate snapshot
```

Each frozen round contains the complete candidate harness or an independently restorable snapshot, plus `ROUND.md` recording UID, parent round, timestamp, status, mission-lock version, rubric version, dimension scores, weighted total, critical-gate results, content hashes when available, changes, evidence, and rejection/promotion reason.

Round states are `CANDIDATE`, `PEAK`, `REJECTED`, and `SELECTED`. Frozen snapshots are append-only. `PEAK.md` is a pointer and verification record; it may move to a newer peak, but the referenced snapshot never changes.

## Identifier convention

Use immutable, case-insensitive UIDs:

- control: `CTL-<DOMAIN>-<NNNN>`
- procedure: `PRC-<DOMAIN>-<NNNN>`
- test: `TST-<DOMAIN>-<NNNN>`
- decision: `DEC-<YYYYMMDD>-<NNNN>`
- exception: `EXC-<YYYYMMDD>-<NNNN>`
- evidence: `EVD-<YYYYMMDD>-<NNNN>`
- change: `CHG-<YYYYMMDD>-<NNNN>`
- improvement round: `RND-<NNNN>`

Never recycle a retired UID. Names may change; UIDs do not. Cross-reference by UID, not heading text.

## Lifecycle states

`DRAFT → PROPOSED → APPROVED → ACTIVE → SUSPENDED → RETIRED`

Rejection is recorded as `REJECTED`, with reason and decision UID. Correction creates a new version or change record; it does not erase history. Exceptions must identify the exact controls affected, compensating controls, approver, start, expiry, review condition, and revocation trigger.

## Authority hierarchy

Record actual sources, not assumed ones. Default conflict handling:

1. applicable law/regulation and binding legal orders;
2. binding contracts, licenses, and formally adopted certification obligations;
3. authorized organizational governance and security/privacy policy;
4. system/product architecture and operating controls;
5. team procedures and local standards;
6. temporary approved exceptions;
7. guidance, style, and preferences.

This is a classification aid, not legal advice. A source-specific precedence rule overrides this default. System/developer/tool constraints of the active execution environment remain binding on the agent and cannot be weakened by the generated harness.

## Traceability invariant

Every mandatory requirement must trace both directions:

`source → control → mechanism/procedure → test → evidence → decision/status → owner`

A missing link is a governance gap. A control without an authorized source or rationale is orphaned. A test without pass/fail criteria is not a validation test.
