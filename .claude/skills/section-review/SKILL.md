---
name: section-review
description: Run one cycle of the human-in-the-loop manuscript review protocol on a target (level1, level2, level3-decomposition, or a section id like S4). Use when the user says "/section-review <target>", "review section X", "let's do the level 1 annotation", "start the review loop", or returns an annotated extract containing #[COMMENTS]. The protocol spans sessions; always rehydrate from manuscript/plan/status.json first.
---

# section-review

One review cycle of the manuscript plan system (`manuscript/plan/README.md` is the
protocol of record; this skill executes it). Adapted from the SAMPLE-STRATEGY-ECD
five-phase loop. A cycle may span several sessions — the phase lives in `status.json`,
not in memory.

## Rehydrate first (every invocation)

1. Read `manuscript/plan/status.json` — confirm the target and find which phase the
   cycle is in. If a different cycle is mid-flight, say so and ask before switching.
2. Read `manuscript/plan/decisions.md` — locked decisions bind every phase; do not
   relitigate any of them without an explicit, dated amendment Marcus approves.
3. Read the target's level file(s). For section targets also read the section's Level-2
   blueprint and its Level-4 entries.

## Phase 1 — Annotation extract

1. Extract the target into `manuscript/plan/annotate-<target>.md`: numbered units
   (paragraphs for sections; thesis components, arc moves, and decision blocks for
   level1), each followed by a blank annotation line. Header explains: annotate inline
   with `#[COMMENTS: ...]`; mark approvals with `#[OK]`; unmarked units are treated as
   approved-by-silence only after Marcus confirms that reading.
2. Update `status.json`: phase = `awaiting_annotation`, `blocked_on` = marcus with the
   extract path. Tell Marcus the extract is ready and stop — do not draft ahead of the
   annotations.

## Phase 2 — Comments to tasks

When the annotated file comes back (or Marcus annotates in-chat): parse every
`#[COMMENTS]` into per-unit tasks (TaskCreate), plus cross-cutting tasks (terminology,
notation, hedging) that unblock downstream units. Order: cross-cutting first, then
largest rewrites, then minor fixes. Confirm the task list with Marcus before Phase 3.

## Phase 3 — Unit-by-unit iteration

For each task, in order:

1. Draft the revision (prose for Level 3 targets; goal statements / claims / decision
   text for Level 1–2 targets). Show before/after. Marcus iterates until satisfied.
2. **Citations:** every `@<citekey>` or `lit:` pointer added must have
   `literature/<citekey>.md` present AND read in this session (read it before relying on
   it — the existence hook cannot check reading). New references: log to
   `todo/003-references-to-acquire.md` AND `level4-evidence.json` as `proposed` in the
   same response; use `@TODO:slug` in prose until acquired and verified.
3. **Numbers:** every quantitative claim added or changed gets a `verif:` pointer in the
   audit object, checked against the artifact (open the CSV/RDS or run log).
4. **Derivation claims:** every analytic claim gets a `deriv:` anchor, checked against
   `manuscript/derivation.qmd`.
5. Record any decision Marcus makes (chosen + rejected options + rationale) for Phase 5.

## Phase 4 — Atomic update

1. Write a one-time script `manuscript/plan/updates/update-<target>-<YYYYMMDD>.py` that
   applies ALL approved changes to the level JSON(s) in one run, with a header comment
   per unit describing the change (the script is the minutes of the cycle). R-style
   rules do not apply to these Python scripts; keep them flat and explicit like
   SAMPLE-STRATEGY-ECD's `update_s4.py`.
2. Run it; spot-check the JSON; run `py scripts/check_plan.py` — must be green.
3. If the target was a section with structural changes (split/merged/reordered
   paragraphs), re-check `depends_on` of downstream paragraphs and fix back-references
   (the audit-fix lesson: corrections propagate along the dependency graph).

## Phase 5 — Document, compile, commit

1. Update `decisions.md` (new/amended decisions, dated) and `status.json` (section
   state, phase, `blocked_on`, `next_actions`, `last_updated`).
2. Rebuild the canonical render: `py scripts/build_manuscript_apa.py` then
   `quarto render manuscript/mi-spectral-apa.qmd`; a render failure blocks the commit.
3. Commit together: level JSON(s) + update script + `status.json` + `decisions.md` +
   rebuilt qmd. Message: `Review <target>: <one-line summary of the human decisions>`
   with per-unit bullets in the body. (Pre-commit re-runs the lint.)
4. If `status.json.clickup.list_id` is set, mirror the new section state.
5. State plainly what the next cycle is and what it is blocked on.

## Special targets

- **level1** — first exercise: thesis, arc, decision blocks. Ratifying D-03/D-04/D-05/
  D-08 (or amending them) is the main outcome; flips `status.json.open_decisions`.
- **level2** — drafted under the approved Level 1; Marcus annotates goal statements and
  super-propositions before any Level-3 work.
- **level3-decomposition** — import the existing qmd (commit `180e2b5`) into Level 3:
  one paragraph per entry, prose verbatim as `draft_prose`, review.status
  `imported_needs_review`, propositions and dependencies reconstructed, Level-4 entries
  created per proposition. Ends by setting `compile_enabled: true` and verifying the
  rebuilt apaquarto qmd renders cleanly before the commit.
