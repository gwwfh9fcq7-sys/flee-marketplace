---
name: book-visualizer
description: Generate a visual learning pack from a book title or uploaded cover. Use for /book or the individual commands /mindmap, /sketchnotes, /flashcards, /comicbook, /visualnotes, /cheatsheet, /poster, /roadmap, /chaptermap, /themes, /mentalmodels, and /action.
---

# Book visualizer

When the user invokes `/book` with a book title or cover, identify the title and author and create all twelve formats below, in order. For a single-format command, create only that format. Reuse the most recently identified book when the context is clear. If no book is supplied or identifiable, ask for a title or cover. Ask for an author or edition only when needed to disambiguate.

## Language policy

- Default to English for all conversation, progress updates, questions, final responses, and deliverables for `/book` and every individual-format command.
- Write all generated visual text, captions, labels, flashcards, summaries, action plans, export notes, and filenames in English by default. Include this language requirement explicitly in every image-generation brief.
- Use another language only when the user explicitly requests or confirms it. Do not infer a language preference from a book cover, title, source language, user locale, or an earlier pack's language. Do not ask for language confirmation when English can be used by default.
- Scope a confirmed language override to the current request or pack unless the user explicitly asks to change the ongoing default. Follow any explicit scope the user gives.
- Preserve author names and bibliographic accuracy. Use a verified English book title where available; an original-language title may appear as a bibliographic identifier without changing the English output language. Label translated titles or quotations accurately rather than inventing an official English wording.
- Check the language of both visual text and accompanying responses before delivery.

## Ground the content

Use reliable knowledge, available sources, and any user-supplied book material. Do not pretend that a cover provides access to the book's contents. Verify chapter titles and order against an available contents page or reliable source before claiming an exhaustive chapter map. If unavailable, request the contents page or clearly label a provisional thematic outline. Do not invent quotations, frameworks, chapters, or mental models; label paraphrases and original implementation exercises. Use only brief, verified quotations. Explain any limits to comprehensive coverage rather than claiming completeness without evidence.

## Deliverables

1. **MINDMAP** (`/mindmap`): A colorful hierarchical mind map with a central title, branches, icons, and examples.
2. **SKETCHNOTES** (`/sketchnotes`): Hand-drawn doodle-style notes on paper texture, with 7–9 key takeaways and icons.
3. **FLASHCARDS** (`/flashcards`): Ten clean Q&A flashcards for active recall; present as a legible numbered visual sheet with distinct cards.
4. **COMICBOOK** (`/comicbook`): A six-panel educational comic explaining the core argument or story. Label illustrative scenarios as adaptations when needed.
5. **VISUALNOTES** (`/visualnotes`): A one-page minimalist infographic containing the Big Idea, five lessons, brief verified quotes or labeled paraphrases, and action steps.
6. **CHEATSHEET** (`/cheatsheet`): A dense but readable one-page reference with the book's verified frameworks and checklists. Label newly devised checklists.
7. **POSTER** (`/poster`): A minimalist aesthetic printable poster with one big idea and three principles.
8. **ROADMAP / FLOWCHART** (`/roadmap`): A step-by-step implementation flowchart from Start to Result, including decision points where useful.
9. **CHAPTERMAP** (`/chaptermap`): A visual map of every verified chapter, with an idea, example, and lesson for each. Follow the grounding requirements above.
10. **THEMES** (`/themes`): A thematic network showing recurring themes and how they connect.
11. **MENTALMODELS** (`/mentalmodels`): The verified mental models from the book, each with a definition and example. Distinguish models explicitly taught by the author from interpretive connections.
12. **ACTION PLAN / BOOKTOACTION** (`/action`): A practical 30-day plan based on the book, with daily actions, weekly milestones, and reflection prompts. Label the schedule as an original application of the book.

## Visual production

- Put Book Title + Author in the header of every visual.
- Number each visual 1–12 using its position above, even for a single-format request.
- Make each format visually distinct, using purposeful colors, icons, doodles, diagrams, and whitespace rather than plain text blocks.
- Generate each requested format as a separate high-resolution image with the available image generation tool; follow that tool's current instructions. Do not substitute text prompts for completed images or claim images were generated when they were not.
- Plan concise, accurate content before rendering. Prioritize readable labels and text. Use the highest suitable supported resolution and aspect ratio; do not promise unsupported dimensions or instant generation.
- Provide individual downloadable images, clearly named in sequence, where the tool supports downloads. A full pack has twelve separate primary images. Offer additional individual card files only if requested.
- Inspect returned visuals when possible and repair substantive text, layout, cropping, and numbering errors before delivery. If generation is blocked or incomplete, state which outputs remain.
- After the requested outputs are generated, ask exactly: "Want me to export this pack as PDF or generate wallpapers from it?"

## Host invocation and portability

This is the shared workflow for the `book` plugin. In Claude-compatible hosts, the command adapter `/book:book` requests the complete pack; `/book:mindmap` and the other namespaced commands request one format. In Codex, use `$book-visualizer` for the complete pack and the `$book-<format>` skills for one format. Conversational `/book` aliases work only when the current workspace or host routes them; do not claim account-wide native slash-command registration.

A single-format adapter supplies the selected format explicitly. Honor that selection even if the user's text includes the book title or a reference to the full-pack command. Follow host image-generation and source-access tools; do not assume an image-generation capability exists. If the host cannot generate images, explain the blocker and offer clearly labeled content briefs only as a fallback, without claiming the requested visual pack is complete.

## Maintenance

Source of truth: https://github.com/gwwfh9fcq7-sys/flee-marketplace/tree/main/plugins/book
Report bugs and feature requests in the repository's Issues with the plugin version and host. Track changes in `CHANGELOG.md` and keep the two plugin manifest versions and marketplace entry synchronized. Do not claim an upload also installed the plugin in a user's app.
