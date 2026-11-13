---
okf_version: "0.1"
title: mi-spectral wiki
updated: "2026-11-13"
---

# mi-spectral — wiki

This is a **derived, cross-linked briefing bundle** for `mi-spectral`: a knowledge base a
newcomer — human **or a cold LLM** — can be pointed at to get an accurate briefing and chat
about the project.

> **Canon vs. this wiki.** The source of truth is `.prometheus/charter.md` (the "Decisions
> made" log) plus whatever repo documents a page cites. This wiki is a *re-generable layer*
> over them; where they disagree, the canon wins. Every page names its `sources:` in
> front-matter. See **[schema](/schema.md)** for the full contract.

## How to brief yourself from this wiki

1. Read **[overview](/overview.md)** — the one-screen briefing (what / why / current status).
2. Traverse **by need** using the catalog below and the prose links in each page.
3. Answer **with citations to wiki pages** (and, through their `sources:`, to the canon).

## Catalog

**Start here**
- [overview](/overview.md) — what the project is, why it exists, and where it stands.
- [schema](/schema.md) — the wiki's own conventions: page types, the front-matter contract,
  the derived-not-canonical rule, the link style, and the sync loop.

**Concepts & architecture**
- [core result](/concepts/core-result.md) — the +½·tr(RIV) theorem, its LRT and
  information-criterion applications, and its settled scope.
- [reproducibility](/architecture/reproducibility.md) — the three evidence layers, the
  `run_all.R` pipeline, the manuscript plan system and build, and citation discipline.

**Decisions**
- [decisions](/decisions/decisions.md) — the single canonical list of settled calls,
  including supersessions.

## History

See **[log](/log.md)** for this bundle's append-only change history.
