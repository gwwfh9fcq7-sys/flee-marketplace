# Plan file guide

A plan file is a working document that `/next` and `/review` read and edit. One file
per outcome, named `plan-<short-name>.md`, stored in the working folder, always updated
in place.

## Required sections, in order

- **Title and header** — outcome name; then Status (Not started / In progress /
  Blocked / Done), Created, Last reviewed, Target finish.
- **Outcome** — one or two sentences describing an observable "done."
- **Why** — one line; the tiebreaker for scope decisions.
- **Constraints** — deadline, dependencies on people or events, and other hard limits.
- **Milestones** — numbered, each with its own status, a one-line definition of done,
  and checkbox actions (`- [ ]` / `- [x]`). Every action is verb-first, carries a rough
  estimate, and fits one work block; multi-session work gets one action per session;
  blocked actions name what they wait on.
- **Critical path** — the chain of items that sets the finish date.
- **Blocked / waiting** — every blocked item with what it waits on and its unblocking
  action.
- **Schedule** — proposed or confirmed dates, and every reminder created via
  `/schedule`.
- **Log** — append-only dated entries recording what changed.

## Example

```markdown
# Ship the workshop booking page

**Status:** In progress
**Created:** 2026-07-01   **Last reviewed:** 2026-07-15
**Target finish:** 2026-08-01

## Outcome
A live booking page taking paid reservations, verified by a completed test booking.

## Why
Bookings happen over email today and get lost.

## Constraints
- Deadline: 2026-08-01
- Depends on: photographer's shots (due 07-20)
- Other: budget 200 EUR

## Milestones

### 1. Content ready — In progress
Definition of done: copy and photos final.
Actions:
- [x] Draft page copy  · est: 90m
- [ ] Select 6 photos  · est: 45m  · blocked by photographer (due 07-20)

### 2. Page live — Not started
Definition of done: test booking and refund completed.
Actions:
- [ ] Build page in site builder  · est: 2h  · after photos
- [ ] Connect payments and run test booking  · est: 1h  · after build

## Critical path
Photos → build page → test booking.

## Blocked / waiting
- Photo selection — waiting on photographer — unblocking action: confirm delivery date
  by message today.

## Schedule
M1 by 07-22 · M2 by 07-29 · buffer to 08-01. No reminders set up.

## Log
- 2026-07-01: Plan created.
- 2026-07-15: Review — copy done; photos slipped to 07-20; finish date holds.
```

## Rules of use

- Tick checkboxes as work completes; `/next` and `/review` parse state from them.
- Keep the header Status honest — it is the at-a-glance signal.
- Estimates stay rough; realism over precision.
- The Log is append-only.
- Keep finished plans; do not delete them.
