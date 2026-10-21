---
description: Create all twelve visual learning formats for a book
argument-hint: "[book title and author, or attached cover]"
---

Book input: $ARGUMENTS

Read the shared `book-visualizer` skill in this plugin at `${CLAUDE_PLUGIN_ROOT}/skills/book-visualizer/SKILL.md` and follow it.
Selection: COMPLETE PACK, all twelve formats in the specified order.
Use English for conversation and deliverables unless the user explicitly requests or confirms another language.
Use the most recently identified book when unambiguous; otherwise ask for a title or cover.
Generate actual images with the host's image-generation capability. If unavailable, explain the blocker; do not claim success or substitute prompts as completed images.
