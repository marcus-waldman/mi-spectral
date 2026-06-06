# Manuscript plan system

Strategic, goal-oriented AI–human collaboration on `manuscript/mi-spectral.qmd`, designed
to span many sessions while keeping memory and coherence toward the submission goal.
Adapted from the leveled-reconstruction workflow of `~/git-repositories/SAMPLE-STRATEGY-ECD`
(four JSON levels, per-level gates, recorded decisions, per-section human review), with
that project's lag metric dropped (it served a persuasion-essay structure) and its
evidence layer replaced by this repo's stronger one (sourced derivation, verification
cache, citation-disciplined literature corpus).

**Source-of-truth rule.** Once Level 3 is populated, all manuscript prose lives in
`level3-paragraphs.json` and `manuscript/mi-spectral.qmd` is COMPILED from it
(`scripts/compile_manuscript.py`). Edits go to the JSON, never to the compiled qmd.
Until then, the existing qmd remains the working draft ("drafted_pre_system" in
`status.json`).

## The four levels

| Level | File | Holds | Gate |
|---|---|---|---|
| 1 | `level1-thesis.json` | Primary/secondary/tertiary thesis, JAIGP venue alignment, persuasion arc, strategic decision blocks (chosen + rejected + rationale) | 5–8 arc moves, every move serves a thesis component, every decision records rejected options |
| 2 | `level2-sections.json` | Per-section goal statement, super-propositions with evidence pointers, depends_on / feeds_forward, dependency graph | every super-proposition has ≥1 evidence pointer; graph acyclic; no orphaned sections |
| 3 | `level3-paragraphs.json` | SOURCE OF TRUTH: per-paragraph proposition, draft_prose, review object, audit object | every paragraph has a proposition (or a declared rhetorical goal); every number carries a verif pointer; every citekey backed and read; review object complete |
| 4 | `level4-evidence.json` | Proposition → evidence join table across the four evidence classes | every non-derivation proposition has ≥1 evidence entry; no `cited` status without a verified literature file; every pointer resolves |

## Evidence pointer grammar (used at every level)

All structured evidence references are strings with one of four prefixes. The validator
(`scripts/check_plan.py`) resolves each one mechanically:

| Pointer | Meaning | Validator check |
|---|---|---|
| `lit:<citekey>` | literature corpus | `literature/<citekey>.md` exists |
| `deriv:<anchor>` | sourced derivation | `{#<anchor>` occurs in `manuscript/derivation.qmd` |
| `verif:<relpath>` | committed verification artifact | file exists at repo-relative path |
| `xmodel:<relpath>` | cross-model audit record | file exists at repo-relative path |

Inside `draft_prose`, citations use ordinary Quarto `@<citekey>` form (the PreToolUse
hook checks those). `@TODO:slug` remains the deliberate-placeholder bypass. New
references follow the existing ladder (`todo/003`): proposed → queued → acquired →
verified → cited; a Level-4 entry's `evidence_status` tracks the same ladder.

## Enforcement (three points, one logic)

1. **PreToolUse hook** (`.claude/hooks/check_citations.py`) — fires on direct Edit/Write
   under `manuscript/`, checks `@<citekey>` tokens and `lit:` pointers in the fragment.
2. **Full-file lint** (`scripts/check_plan.py`) — authoritative; resolves every pointer,
   every `@<citekey>`, and the per-level structural gates. Must pass green before any
   commit phase of the review loop, and after any scripted JSON mutation (scripted
   mutations bypass the hook — the lint is what closes that hole).
3. **Pre-commit hook** (`scripts/git-hooks/pre-commit`, wired via `core.hooksPath`) —
   runs the lint when plan files are staged; nothing reaches history unchecked.

## The review loop (per section or per level)

Run as `/section-review <target>` (target = `level1`, `level2`, or a section id like `S4`).

- **Phase 1 — Annotation.** Claude extracts the target into
  `manuscript/plan/annotate-<target>.md` (numbered units). Marcus annotates inline with
  `#[COMMENTS]`. `status.json` flips to `blocked_on: marcus`.
- **Phase 2 — Task planning.** Claude parses the comments into per-unit tasks plus
  cross-cutting tasks, ordered by dependency.
- **Phase 3 — Unit-by-unit iteration.** For each unit: Claude drafts the revision; Marcus
  iterates until satisfied; citations verified against `literature/` (read-in-session
  rule); numbers verified against `verif:` pointers; new references logged to `todo/003`
  and Level 4 as `proposed`.
- **Phase 4 — Atomic update.** All approved changes applied to the JSON by a one-time
  script under `manuscript/plan/updates/`, then `check_plan.py` must pass green.
- **Phase 5 — Document and commit.** Update `status.json` and `decisions.md`, recompile
  the qmd (when Level 3 is live), commit the JSON + update script + status together,
  mirror section states to ClickUp.

Decisions ratified during review land in `decisions.md` — dated, with rejected options —
and are not relitigated without an explicit, dated amendment (same discipline as the
pre-registration amendments in `todo/004`/`todo/029`).

## Project-manager view

`/status` derives (never recalls) the dashboard: section states and the global cursor
from `status.json`, drift against git (uncommitted plan changes, compiled qmd older than
Level 3), open decisions, the citation-acquisition backlog from Level 4, and what is
blocked on whom. `status.json` is updated in the same commit as the work it describes,
so status and reality cannot diverge silently.

## Current bootstrap state (2026-06-05)

The manuscript was drafted before this system existed (commit `180e2b5`). Entry path:
Level 1 drafted for Marcus's annotation (the first review exercise) → Level 2 drafted
under the approved Level 1 → the existing qmd decomposed into Level 3 paragraph by
paragraph (prose imported as `draft_prose` with status `needs_review`) → Level 4
populated as part of the decomposition → section-by-section review loop begins.
