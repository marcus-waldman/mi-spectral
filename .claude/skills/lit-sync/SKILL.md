---
name: lit-sync
description: Sync the Better BibTeX export to mi-spectral/literature/<citekey>.md files (citation-discipline bridge). Use when the user asks to "sync the literature", "refresh literature files", "lit-sync", or after exporting a new BibTeX from Zotero. Parses literature/mi-spectral-better-bibTeX.bib, finds each PDF in the MI-SPECTRAL drive folder by author/year, looks up cached Mathpix conversions by SHA256, and writes per-citekey markdown with YAML frontmatter. Idempotent.
---

# lit-sync

Bridge between Better BibTeX (which produces the citekeys we cite) and the citation-discipline hook (which checks `literature/<citekey>.md` exists before allowing an `@<citekey>` in `manuscript/`).

## What it does

For each entry in `literature/mi-spectral-better-bibTeX.bib`:

1. Read citekey from the entry header (`@type{citekey,`)
2. Find the migrated PDF in `~/Google Drive/Literature/MI-SPECTRAL/`
   - Try `<citekey>.pdf` directly first
   - Fall back to `<firstauthor-surname>` + `<year>` filename match
3. SHA-256 the PDF, look up `~/Google Drive/Literature/.litrev/mathpix_cache/<sha256>.md`
4. Write `mi-spectral/literature/<citekey>.md` with YAML frontmatter + Mathpix markdown
5. Scan `mi-spectral/manuscript/` for `@citekey` tokens, warn on any unsynced

Skips entries whose existing markdown already has a matching `pdf_sha256` in its frontmatter — re-runs are cheap. Skips entries whose citekey has invalid characters (e.g., `;` from a malformed Zotero author field) with a clear "fix the underlying Zotero entry" message.

## When to run it

- After exporting a fresh BibTeX from Zotero (right-click collection → Export Collection → Better BibTeX → save to `literature/mi-spectral-better-bibTeX.bib`)
- After dropping new PDFs into Zotero and running `migrate_zotero_attachments` + `index_papers.py`
- Before adding a new `@citekey` to `manuscript/` (the PreToolUse hook needs the file to exist)
- Whenever the citation-discipline hook complains about a missing `literature/<citekey>.md`

## How to invoke

```
py scripts/lit_sync.py
```

Or via the `/lit-sync` slash command (this skill).

## Prerequisites

1. **BibTeX export at** `literature/mi-spectral-better-bibTeX.bib` — refresh by right-click on the `mi-spectral` Zotero collection → Export Collection → Better BibTeX → save with that filename.
2. **PDFs in the drive folder** — `mcp__litrev__migrate_zotero_attachments(project='MI-SPECTRAL')` writes them as `<litrev-key>.pdf`.
3. **Mathpix cache populated** by `index_papers.py` (requires the `_estimate_tokens` patch from litrev_mcp issue #21 for long math-heavy books).
4. **Python deps:** `bibtexparser` (already installed).

## Output frontmatter

```yaml
---
citekey: cavanaughAkaikeInformationCriterion1998a
item_type: article
authors: Cavanaugh, Joseph E. and Shumway, Robert H.
year: '1998'
title: An Akaike information criterion for model selection in the presence of incomplete data
venue: Journal of Statistical Planning and Inference
volume: '67'
issue: '1'
pages: 45--65
doi: 10.1016/S0378-3758(97)00115-8
source_pdf: 'C:\Users\marcu\Google Drive\Literature\MI-SPECTRAL\cavanaugh_akaike_information_criterion_1998.pdf'
pdf_sha256: <64-hex>
converted_via: mcp__litrev__convert_pdf (Mathpix)
last_synced: 2026-05-22T17:30:00Z
---
```

Followed by the full Mathpix markdown body.

## Failure modes and what to do

| Symptom | Cause | Fix |
|---|---|---|
| `ERROR: BibTeX export not found` | No `.bib` file at the expected path | In Zotero: right-click collection → Export Collection → Better BibTeX → save to `literature/mi-spectral-better-bibTeX.bib` |
| `SKIP: citekey has invalid characters [';']` | Malformed Zotero author field collapses multiple authors into one literal name with semicolons | In Zotero: edit the item, replace the single author entry with multiple separate author entries (one Last/First per author); then re-export BBT |
| `SKIP: PDF not found` | PDF still attached to Zotero, not migrated to drive folder | Run `mcp__litrev__migrate_zotero_attachments(project='MI-SPECTRAL')` |
| `SKIP: Mathpix cache miss` | PDF was migrated but never indexed | Run `py "Google Drive/Literature/MI-SPECTRAL/index_papers.py"` |
| Snake_case key persists despite BBT default being camelCase | Litrev's `zotero_add_paper` set a `Citation Key:` line in the item's `extra` field; BBT inherits it on export | In Zotero: right-click the item → Better BibTeX → Refresh BibTeX key (overwrites with BBT's camelCase default) |

## Related infrastructure

- `scripts/lit_sync.py` — the implementation this skill invokes
- `todo/001-literature-and-hooks.md` — Phase 3 specifies the PreToolUse hook that enforces citation discipline at edit time
- `IDEAS.md` — "Citation discipline" section explains why this whole pipeline exists
- `CLAUDE.md` — load-bearing rule: every `@citekey` in `manuscript/` needs `literature/<citekey>.md` to exist and have been read in-session

## Citekey convention (locked 2026-05-22)

Better BibTeX default: `<firstauthor-lowercase><TitleWord1Word2Word3-camelCase><year>[a|b|...]`. Examples:

- `cavanaughAkaikeInformationCriterion1998a`
- `mengPerformingLikelihoodRatio1992b`
- `vaartAsymptoticStatistics1998a`

The `a`/`b` disambiguator suffix appears when BBT detects multiple library-wide items that would otherwise collide. Don't strip it — it's part of the citekey.
