# literature/

Markdown copies of cited papers. One file per citekey.

**Convention:** `<citekey>.md` matches the `@<citekey>` used in `manuscript/`. E.g., `chanmeng2022.md` is the markdown copy of Chan & Meng (2022); citations in the manuscript appear as `@chanmeng2022`.

**Purpose.** Every claim in the manuscript about a prior work must be grounded in this directory. The PreToolUse hook (specified in `todo/001-literature-and-hooks.md`) enforces that `literature/<citekey>.md` exists before a citation can be written.

**Source of files.** PDFs come from Zotero. Conversion via `mcp__litrev__convert_pdf` (or pandoc fallback). Convert at section granularity; preserve equations as LaTeX where possible.

**Workflow:** see `todo/001-literature-and-hooks.md`.
