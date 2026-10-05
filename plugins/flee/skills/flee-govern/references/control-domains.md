# Governance control domains

Cover each applicable domain; mark non-applicable items with a reason and approver rather than silently omitting them.

1. **Purpose and scope:** mission, outcomes, boundaries, assumptions, applicability, exclusions, priorities.
2. **Authority:** rule hierarchy, mandatory vs advisory language, overruling rules, conflicts, exceptions, waivers, expiry.
3. **Identity and ownership:** users, roles, service identities, authentication, authorization, separation of duties, delegations, accountable owners.
4. **Architecture and interfaces:** components, trust boundaries, internal/third-party services, dependencies, data flows, compatibility, adoption and deprecation.
5. **Information:** classification, collection, minimization, privacy, storage, encryption, retention, deletion, residency, access logs, backup and restore.
6. **Security:** threats, secure defaults, secrets, vulnerability/change management, incident response, supply chain, external access.
7. **Lifecycle and operations:** design, build, update, migration, preflight, execution, post-operation, maintenance, troubleshooting, recovery, reset, restart, shutdown and retirement.
8. **Decision and change control:** proposals, impact/risk review, approvals, rejection, correction, versioning, rollback, emergency change and post-hoc review.
9. **Assurance:** requirements, measures, thresholds, tests, benchmarks, acceptance, validation, clearance, certification evidence and license compliance.
10. **Resilience:** failure modes, degradation modes, fallbacks, recovery objectives, backup integrity, restore drills, continuity and disaster recovery.
11. **Observability and communication:** logs, records, audit trail, metrics, alerts, notifications, escalation, modes, recipients, acknowledgement and noise control.
12. **Standardization:** naming, UIDs, schemas, formats, outputs, listings, defaults, templates, terminology, structural and functional priorities.

For every material control define: UID, requirement, rationale/source, applicability, owner, mechanism, mode, trigger, limit/threshold, default, fallback, evidence, test, pass/fail criteria, failure action, exception path, review interval, dependencies and status.
