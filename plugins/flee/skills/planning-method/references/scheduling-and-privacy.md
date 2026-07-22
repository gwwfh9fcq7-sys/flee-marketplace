# Scheduling gate and privacy rules

## Scheduling gate — run before creating any scheduled task

1. **Confirm intent.** The person must actually want recurring reminders, not just a
   timeline on paper. Unclear → ask; never default to automation.
2. **State exactly what will run:**
   - cadence and time (e.g. every weekday at 9am, every Monday, in 3 days)
   - what each reminder prompts
   - when it ends and how it is stopped
   - how reminders execute: each one starts a fresh session with no memory of this
     one; it asks for access to the plan folder before reading anything; the desktop
     app must be running for it to reach the plan.
3. **Get an explicit yes.** No yes → nothing is created.
4. **Create it, then confirm back** what was set up and how to change or cancel it.

Re-run this gate whenever a plan change makes an existing reminder stale.

## Reminder prompt rules — mandatory

Write every reminder prompt self-contained and non-sensitive:

- name the plugin and the plan filename (e.g. "flee: work the plan in
  plan-booking-page.md")
- instruct the session to request access to the plan folder before proceeding
- state the check-in action (e.g. "surface the next action and ask whether the last
  planned item got done")
- include no names, contact details, financials, or any personal or confidential
  content.

Default cadences: a daily nudge each working morning; a weekly review; a
deadline-relative check-in a set number of days before the target finish.

## Privacy rules — mandatory

- Plan files live in the person's working folder only. Do not copy or send their
  contents anywhere they don't need to go.
- Before any web search or external-service call: remove identifying and sensitive
  data — names, emails, phone numbers, account numbers, addresses, confidential
  specifics — and query the generic substance. Example: research "how to structure a
  Series A data room," not the company's own deal details.
- Do not repeat sensitive details where they are not needed — not in reminders, file
  names, or logs.
- A step that would send sensitive data off the machine: halt and get confirmation
  first.
- Process personal data in line with GDPR/KVKK principles: minimize what is processed,
  keep it local, prefer de-identified handling at every step.
- Unsure whether something is sensitive → treat it as sensitive.
