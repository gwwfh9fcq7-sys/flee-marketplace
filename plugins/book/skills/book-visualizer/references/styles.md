# Style and learning-method guide

The twelve output formats are learning methods. The three visual presets change their presentation; they do not replace the method, change the underlying book, or justify adding new claims.

Read `styles.json` in this directory for the preset definitions. In provider-backed skill storage, access both resources through the same skill provider rather than assuming filesystem access.

| Format | Learning method | Preserve in every style |
| --- | --- | --- |
| 01 Mindmap | Hierarchical synthesis | Central idea, branches and sub-branches |
| 02 Sketchnotes | Visual encoding | Seven to nine takeaways with explanatory doodles |
| 03 Flashcards | Active recall | Ten clearly paired questions and answers |
| 04 Comicbook | Narrative explanation | Six sequential educational panels |
| 05 Visualnotes | Summary and synthesis | Big Idea, five lessons, labeled quotes/paraphrases, actions |
| 06 Cheatsheet | Rapid reference | Dense, scannable concepts, frameworks and checklists |
| 07 Poster | Memorable cues | One big idea and three principles |
| 08 Roadmap | Procedural application | Start, ordered steps, relevant decisions and result |
| 09 Chaptermap | Sequential organization | Every verified chapter, idea, example and lesson |
| 10 Themes | Relational reasoning | Themes and explicitly labeled relationships |
| 11 Mental models | Concept transfer | Definitions, examples and coverage limits |
| 12 Action plan | Practice over time | Thirty daily actions and review milestones |

## Presets

- `illustrated`: expressive, colorful, format-adapted imagery. This is the default. The original sample set uses different compositions suited to each method rather than one identical page template.
- `ink`: monochrome pen-and-paper explanation, hatching and hand-drawn symbols. Keep fine text readable.
- `editorial`: precise grid, sans-serif typography, flat symbols, red-led accents and whitespace. For sketchnotes, use simple doodle-like line symbols; for comics, keep the six-panel narrative.

At least three dimensions should differ visibly between presets: mark-making, typography, palette, layout treatment, and illustrative rendering. A recolor alone does not establish a distinct style. Method-specific structure must remain recognizable.

## Selection and counts

- No option: use `illustrated` and produce twelve images for a full pack, or one for a single-format command.
- `--style illustrated`, `--style ink`, or `--style editorial`: use that preset for the requested format(s).
- `--styles all`: explicitly produce all three presets, in the order illustrated, ink, editorial. A full pack contains thirty-six images; a single-format request contains three.
- Treat these options as request metadata, not part of the book title or shell commands. Plain-language style requests have the same effect. Honor an explicit custom style without pretending it is a bundled preset. If options conflict, resolve the conflict before rendering.

Use `01-mindmap--ink.png` style-aware filenames. Keep the 01–12 method number in every image, and add a small style label to variants. For all-styles output, group by style and preserve format order within each set.

## Generation and review

Prepare the book-specific content before applying the style. Keep content separate from artistic directions. Write a brief for one selected format at a time; do not list the counts of unrelated formats in that image brief. Include English as the default language explicitly. Instruction words such as "ONLY" must not leak into headings.

Preserve item counts, Q&A pairing, chapter order, flowchart paths, attribution and scope notes across variants. Inspect every output. Reject samples that add other formats, omit required items, invent new claims or lose source caveats. State content adaptations where wording or layout changes; do not promise pixel-identical layouts.

The public repository sample gallery is at `examples/book/the-creating-brain/README.md` (outside the installable plugin). Its thirty-six English images illustrate all twelve methods in all three styles using The Creating Brain by Nancy C. Andreasen. They are thematic study companions, not exhaustive summaries or author-endorsed materials. Use them as design references, never as factual evidence about another book. Images are generated demonstration assets, not pages reproduced from the book.
