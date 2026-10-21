# Book Visualizer

**Version 0.2.0** · A plugin in the **Flee** marketplace.

Turn a book title or cover into twelve separate visual learning images. Conversation and deliverables default to English. A different language requires an explicit request or confirmation.

## Install in a Claude-compatible host

```text
/plugin marketplace add gwwfh9fcq7-sys/flee-marketplace
/plugin install book@flee
```

Then invoke the full pack with:

```text
/book:book The Creating Brain by Nancy C. Andreasen
```

Plugin commands are namespaced. A bare `/book` is a conversational alias only where the current host or workspace routes it.

## Commands and Codex skills

| Format | Claude-compatible command | Codex skill |
| --- | --- | --- |
| Complete pack | `/book:book` | `$book-visualizer` |
| 01 Mindmap | `/book:mindmap` | `$book-mindmap` |
| 02 Sketchnotes | `/book:sketchnotes` | `$book-sketchnotes` |
| 03 Ten Q&A flashcards | `/book:flashcards` | `$book-flashcards` |
| 04 Six-panel comic | `/book:comicbook` | `$book-comicbook` |
| 05 Visualnotes | `/book:visualnotes` | `$book-visualnotes` |
| 06 Cheatsheet | `/book:cheatsheet` | `$book-cheatsheet` |
| 07 Poster | `/book:poster` | `$book-poster` |
| 08 Roadmap / flowchart | `/book:roadmap` | `$book-roadmap` |
| 09 Chaptermap | `/book:chaptermap` | `$book-chaptermap` |
| 10 Themes | `/book:themes` | `$book-themes` |
| 11 Mental models | `/book:mentalmodels` | `$book-mentalmodels` |
| 12 Action plan | `/book:action` | `$book-action` |

Attach a cover or append a title and author. Single-format commands generate only the selected format. An unambiguous book from the current conversation can be reused.

Codex packaging follows this repository's existing `.codex-plugin/plugin.json` convention. Import the `plugins/book` directory through your host's supported plugin mechanism. This repository upload does not install a plugin into ChatGPT or register account-wide slash commands.

## Styles and samples

Choose `--style illustrated` (default), `--style ink`, or `--style editorial`. Add `--styles all` only when you want all three styles. A full pack then produces 36 images; a single-format command produces 3. Without that option the counts remain 12 and 1.

```text
/book:book The Creating Brain by Nancy C. Andreasen --style ink
/book:mindmap The Creating Brain by Nancy C. Andreasen --styles all
```

The [sample gallery](../../examples/book/the-creating-brain/README.md) demonstrates **12 learning methods × 3 visual styles**, using 12 reused illustrated originals plus 24 newly rendered variants. The gallery and downloadable samples live outside the installable plugin. See the [style guide](skills/book-visualizer/references/styles.md) for learning-method differences and preserved structures.

## Requirements and output

A host with image generation is required for finished images. Source access or supplied book material is needed to verify detailed contents and quotations. Tool names, permissions, available resolutions, and download behavior depend on the host. The plugin bundles instructions, not an image service, API key, or provider subscription.

A full run produces twelve numbered images, each headed with book title and author. Flashcards contain ten Q&A pairs; sketchnotes contain seven to nine takeaways; the comic contains six panels; the action plan covers thirty days. Generation takes time.

A title or cover is not the full book. The workflow verifies chapter order before claiming full coverage, labels paraphrases and original exercises, and explicitly identifies missing evidence or incomplete model coverage. It does not invent author quotations or promise exhaustive coverage without sources.

## Versions and issues

This repository is the source of truth. [Report an issue](https://github.com/gwwfh9fcq7-sys/flee-marketplace/issues/new/choose), including **book**, plugin version, host, invocation, and expected versus actual output. Remove private book uploads and sensitive material from public reports.

See [CHANGELOG.md](CHANGELOG.md) for versions and [RELEASING.md](RELEASING.md) for the release procedure. The user-approved public sample library is versioned under `examples/book`; other generated packs and private uploads are excluded. The sample images are not bundled in the plugin installation archive.

## Validation

From the repository root:

```bash
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_book.py --check
python scripts/package_book.py --output-dir /tmp/book-releases
```

The packager creates a versioned ZIP with `book/` as its root and writes a SHA-256 sidecar. Static checks verify packaging and routing; they do not establish that a host can generate images. Run the documented host smoke checks before claiming runtime compatibility.
