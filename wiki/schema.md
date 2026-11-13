---
type: WikiSchema
title: Wiki schema & conventions
description: How this wiki is structured, why it is derived-not-canonical, and the rules every page follows.
sources:
  - ".prometheus/charter.md (Decisions made — canon)"
updated: "2026-11-13"
---

# Wiki schema & conventions

This page is the **backbone** of the wiki. Read it before editing any page. It defines what
the wiki is, the rules every page obeys, and the loop that keeps it current. It governs
itself: it is a derived page, it names its `sources:`, and it links rather than restates.

## 1. What this wiki is — and is not

`wiki/` is a **lightweight, LLM-maintained briefing bundle** for mi-spectral: a knowledge
base a newcomer — human **or a cold LLM** — can be pointed at to get an accurate briefing and
chat about the project. It is deliberately **not** an app: no retrieval engine, no vector
store, no server. The delivery mechanism is: open an LLM session in this repo (or hand the
LLM `wiki/`), and `index.md` plus this schema do the rest.

The format is **OKF v0.1 essentials**: markdown pages + YAML front-matter + cross-links, with
reserved `index.md` (catalog + entry point) and `log.md` (append-only history).

### 1.1 Derived, not canonical (the load-bearing rule)

**The canon is `.prometheus/charter.md` (above all its "Decisions made" log) plus whatever
repo documents a page cites. This wiki is a *derived, re-generable briefing layer* over
them — never a competing source of truth.** When the wiki and the canon disagree, the canon
wins and the wiki is the defect. Drift is a bug, not a stylistic nit.

Consequences, binding on every page:

- **Every page names its `sources:` in front-matter** (repo-relative paths, section anchors
  where useful). A claim with no traceable source does not belong on the page.
- **Do not restate ratified numbers or decisions from memory.** Pull them from the cited
  source; if you cannot cite it, do not assert it.
- **Never edit the canon to match the wiki.** Fixes flow one way: canon → wiki.

## 2. How to brief yourself from this wiki

1. Read **[overview](/overview.md)** — the one-screen briefing (what / why / status).
2. Traverse **by need** using the catalog in **[index](/index.md)** and the prose links in
   each page. A page's `type` (§3) tells you what kind of answer it holds.
3. Answer with **citations to wiki pages** (and, through their `sources:`, to the canon).

## 3. Page-type vocabulary (`type` front-matter)

Every concept document carries a non-empty `type`. This wiki uses a small, closed vocabulary
so a knowledge-graph consumer can group pages — extend it here first when a new kind of page
is genuinely needed:

| `type` | Meaning | Pages |
|---|---|---|
| `WikiSchema` | This conventions/backbone page | `schema.md` |
| `Overview` | The start-here briefing | `overview.md` |
| `Concept` | A conceptual idea in the design | `concepts/*` |
| `Architecture` | A design/mechanism/contract page | `architecture/*` |
| `DecisionLog` | The single canonical decisions page | `decisions/decisions.md` |
| `Glossary` | The term list | `glossary/glossary.md` |

`index.md` and `log.md` are **reserved** and are *not* concept documents — they carry no
`type`.

## 4. Front-matter contract

Concept documents (everything except `index.md`/`log.md`):

```yaml
---
type: Concept                  # REQUIRED, non-empty. From the vocabulary in §3.
title: Short name              # recommended
description: One-line summary  # recommended — becomes the catalog one-liner in index.md
sources:                       # REQUIRED (the derived-not-canonical rule, §1.1)
  - ".prometheus/charter.md (Decisions made)"
updated: "2026-11-13"            # recommended, ISO-8601 YYYY-MM-DD; set on every edit
---
```

Quote `sources:` entries — section markers like `§6` and paths keep YAML unambiguous. The
bundle-root `index.md` carries `okf_version: "0.1"`.

## 5. Cross-link style

- **Relationships are untyped markdown links in prose.** Convey the *kind* of link in the
  surrounding sentence.
- Prefer **bundle-relative absolute links**: `[overview](/overview.md)`. The validator lints
  these — a dangling absolute link fails validation.
- A *relative* link out into the canon (e.g. `[charter](../.prometheus/charter.md)`) is fine
  *in addition to* naming the source in `sources:`; only intra-wiki absolute links are linted.

## 6. Tone & altitude

- **Newcomer-first, one screen where possible.** Lead with the answer; push detail into the
  cited source. A page should brief, not exhaustively reproduce.
- **Accurate over comprehensive.** Prefer the exact ratified fact with a citation over a
  hand-waved paraphrase. If unsure, cite and quote.
- **Status must be current.** A page that implies stale project status is wrong — fix it at
  the next sync.

## 7. Consolidation discipline — "link, don't repeat"

**Each topic has exactly one canonical page; every other page links to it rather than
restating it.** In particular, [decisions](/decisions/decisions.md) is the single canonical
list of settled calls (including supersessions); other pages link there.

## 8. The sync loop

This wiki stays current through the Prometheus post-wrap hook (`.prometheus/post-wrap.md`):
every `/prometheus:wrap` re-reads the freshly-committed charter, fixes what the wiki now gets
wrong, adds what it misses, validates, and commits `wiki/` only. A no-op sync (everything
already accurate) is a good outcome. Between wraps, anyone may run the lint by hand:

```
py "C:/Users/marcu/git-repositories/prometheus/scripts/wiki_validate.py" wiki
```

## 9. Validation rules (what the command above enforces)

Errors (must be fixed before committing): every non-reserved page has a front-matter fence;
every concept document has a non-empty `type` and at least one `sources:` entry; reserved
files carry no `type`; bundle-relative absolute links resolve. Warnings: missing `updated`
on a concept page, missing `okf_version` on the root `index.md`.
