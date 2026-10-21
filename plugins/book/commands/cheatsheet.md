---
description: Generate only format 06 (cheatsheet) for a book
argument-hint: "[book title and author, or attached cover]"
---

Book input: $ARGUMENTS

Read the shared `book-visualizer` skill in this plugin at `${CLAUDE_PLUGIN_ROOT}/skills/book-visualizer/SKILL.md`.
Selection: ONLY `cheatsheet` (format 6). Generate only this one format, not the complete pack. Keep its original format number.
Follow the shared grounding, language, image-generation, and review requirements. Default to English unless explicitly requested otherwise. Reuse an unambiguous book from the current conversation or ask for a title or cover.
