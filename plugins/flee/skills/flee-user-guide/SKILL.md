---
name: flee-user-guide
description: Explain how to use the Flee plugin, its commands, plan files, privacy model, and recommended workflow. Use when the user invokes $flee-user-guide or asks for Flee help, instructions, commands, setup, examples, or a user guide.
---

# Flee user guide

Flee is a local-first planning workflow. Plans are Markdown files in a folder chosen by the user.

## Commands

- `$flee-plan <idea>` creates or updates a structured plan.
- `$flee-schedule <plan>` lays the plan onto a realistic timeline and can propose optional reminders.
- `$flee-next <plan and time available>` returns one immediately startable action.
- `$flee-review <plan>` updates statuses, diagnoses slippage, and re-plans.
- `$flee-improve <plan or project>` scores and iteratively improves the artifact to a confirmed plateau.
- `$flee-govern <system or project>` reviews or redesigns it through frozen, scored governance rounds, then restores and selects the highest admissible peak.
- `$flee-user-guide` shows this guide.

Natural-language requests work too, such as “Use Flee to plan my product launch” or “What should I do next from plan-launch.md if I have 30 minutes?”

## Recommended flow

1. Start with `$flee-plan` and choose a working folder.
2. Use `$flee-schedule` after the plan and capacity are known.
3. Run `$flee-next` at the start of a work block.
4. Use `$flee-review` regularly or when work slips.
5. Use `$flee-improve` when the plan needs a rigorous refinement pass.
6. Use `$flee-govern` when the system needs reusable rules, enforcement mapping, control testing, recovery, and persistent governance records.

Reminders are never created without explicit approval. Plan content stays in the chosen local folder; external queries should be de-identified, and sensitive data must not leave the machine without confirmation.
