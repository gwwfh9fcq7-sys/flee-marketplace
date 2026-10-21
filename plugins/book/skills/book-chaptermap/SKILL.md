---
name: book-chaptermap
description: Generate only the chaptermap visual for a book. Use for $book-chaptermap, /chaptermap, or a request for this single book-learning format.
---

# Book chaptermap

Read the shared `book-visualizer` skill from this same plugin before producing the visual. Its filesystem path is `../book-visualizer/SKILL.md` relative to this skill directory. For provider-backed skills, use the provider's skill reader and the exact shared skill resource in this plugin; do not treat a resource URI as a filesystem path.

Selection: ONLY `chaptermap` (format 9). Generate only this one format, not the complete pack. Keep its original format number.
Use the supplied book title or cover, or reuse the book when unambiguous. Follow the shared evidence, language, production, and review requirements. English is the default for conversation and deliverables unless the user explicitly requests or confirms another language.
