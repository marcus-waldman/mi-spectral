---
type: Architecture
title: How evidence and prose are produced
description: The three reproducibility layers, the run_all.R simulation pipeline, the manuscript plan system and build chain, and citation discipline.
sources:
  - "CLAUDE.md (Repo layout, Manuscript plan system, Commands, Citation discipline)"
  - ".prometheus/charter.md (Decisions made — fold-in gate, D-21, compile enablement)"
updated: "2026-11-13"
---

# How evidence and prose are produced

## Three reproducibility layers

`IDEAS.md` records *what was found and what it means*; `verification/run_all.R` is *how to
reproduce it*; per-phase `.rds` caches and summary CSVs under `verification/cache/` are *the
raw evidence*.

## Simulation pipeline

`verification/run_all.R` is the single entrypoint for the comprehensive sweep, with one
module per phase under `verification/_modules/`: smoke tests (0), the theorem-validation
sweep (1), the MI-AIC/BIC selection sweep (2), the rate side experiment (3), MNAR bias (4),
and aggregation against pre-registered pass criteria (5). The pre-registered originals
(`W1`/`W2`/`W3-*.R`, frozen at SHA `ddc9037`) are **not** routed through it and are left
untouched. Some exploratory one-offs live in `verification/spikes/` with their own Commands
entries in `CLAUDE.md`; CAS checks live in `verification/cas-wolfram/`.

Standing policy: any verification result cited in the manuscript or response letter must be
folded into `run_all.R` + `aggregate.R` + `CLAUDE.md` before it is cited.

## Manuscript plan system and build

Prose lives in `manuscript/plan/` as four leveled JSONs (thesis → sections → paragraphs →
evidence); `scripts/check_plan.py` lints pointers, citekeys, and prose guards and runs from
the pre-commit hook. `level3-paragraphs.json` is **locked as the source of record**
(`compile_enabled` = true): prose changes go through scripts in `manuscript/plan/updates/`,
then `scripts/build_manuscript_apa.py` regenerates `manuscript/mi-spectral-apa.qmd`, which
Quarto renders to the canonical PDF and HTML. Never edit the `.qmd` directly. The sourced,
executable derivation is `manuscript/derivation.qmd`.

## Citation discipline

Every `@citekey` in `manuscript/` must have a `literature/<citekey>.md` copy that was read in
the current session; a PreToolUse hook enforces this, and papers proposed in conversation are
logged in `todo/003-references-to-acquire.md`. The literature corpus is synced from Zotero
via `scripts/lit_sync.py` (`/lit-sync`).

The calls behind these rules are in [decisions](/decisions/decisions.md).
