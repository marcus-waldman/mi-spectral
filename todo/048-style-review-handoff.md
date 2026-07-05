# todo/048 — session handoff: critical style review of the manuscript (statistics-journal register, Rubin exemplar)

**STATUS: OPEN (written 2026-07-04, immediately after the Lemma P derivation section landed
@ `4e93aaf`).** Marcus's directive, captured at decision time: the manuscript does not read
like the statistics journal articles he is familiar with. He wants a critical review of the
writing — readability AND adherence to the standards and conventions of academic writing in
statistics — with Donald Rubin's writing style as the exemplar he likes. The session should
demonstrate, concretely, that the model can write in a register consistent with the
discipline. This file is the self-contained spec + resume prompt for that session.

## Recommended model / effort

**Fable 5, effort HIGH.** This is a writing-quality and judgment task, and the demonstration
rewrites (Phase C) are the deliverable Marcus will judge the session by. No new mathematics;
no cross-model derivation gate applies unless a rewrite changes a technical claim (it must
not — see the invariants below).

## The mismatch hypothesis (to be tested, not assumed)

The current prose is not accidental: it is the product of deliberate house rules
(CLAUDE.md "Manuscript prose style": plain expository structure, punctuation budget v2,
one-idea-per-sentence bias, "keep the reading level low" with the corpus pushed to FK ≈ 10,
the "We show that..." results formula). Those rules were optimized for "an applied researcher
with quantitative training." A plausible diagnosis — TO BE VERIFIED against exemplars, not
asserted — is that exactly these rules produce a register that reads as non-native to
JASA / Biometrika / JRSS-B / Statistical Science: statistics prose runs longer, more
subordinated sentences with disciplined hedging, parenthetical qualification, motivating
material before formalism, and a higher reading level than FK 10. The session's first job is
diagnosis grounded in the owned corpus; rewriting comes only after Marcus ratifies the
direction.

## Ground rules (non-negotiable, carried over)

1. **Locked decisions are not relitigated without a dated amendment** (`manuscript/plan/
   decisions.md`). Any style-rule change = a dated amendment row + the CLAUDE.md prose-style
   section updated + the enforcement machinery recalibrated **in the same commit** (else the
   new register gets auto-flagged): the `check_plan.py` punctuation gate (em-dashes banned,
   rhetorical colons, 2+ semicolons) and the scouts (`cadence_flag.py`,
   `color_commentary_flag.py`, `fluff_flag.py`, `mechanism_flag.py`, `overclaim_flag.py`).
2. **Accuracy invariants survive any rewrite untouched:** the data-quantity rule (models
   never "lose data"; candidate differences are missing information / RIV), mechanism
   accuracy, typed claims (T-06), trust-ordering (T-04/D-05), banned vocabulary (T-03), the
   no-color-commentary rule, D-17 (no verbatim quotation of other work in manuscript prose),
   and citation discipline (every `@citekey` backed by a `literature/` file read in-session).
   A style pass changes HOW things are said, never WHAT is claimed, hedged, or cited.
3. **The qmd is derived (D-21).** All prose changes go through
   `manuscript/plan/level3-paragraphs.json` via atomic scripts in
   `manuscript/plan/updates/`, `check_plan` green, rebuild with
   `py scripts/build_manuscript_apa.py`, render `quarto render manuscript/mi-spectral-apa.qmd`.
4. **Human-gated rewriting.** The validated method is the per-paragraph human-gated pass
   (todo/036/037); an ungated wholesale sweep was previously SHELVED by Marcus as
   not-worth-the-risk. Nothing sweeps until Phase C is ratified.

## Phase plan

**Phase A — build the style rubric from the owned corpus (read in-session; training-weight
impressions of "how Rubin writes" are not evidence).** Rubin-authored/coauthored exemplars
already in `literature/`: `rubinInferenceMissingData1976b` (Biometrika 1976),
`rubinMultipleImputationNonresponse1987` (the 1987 book — the sustained-prose exemplar),
`Meng01121991` (Meng & Rubin 1991), `mengPerformingLikelihoodRatio1992b` (Meng & Rubin,
Biometrika 1992), `barnardMiscellaneaSmallsampleDegrees1999` (Barnard & Rubin, Biometrika),
`dempsterMaximumLikelihoodIncomplete1977a` (DLR, JRSS-B), `littleStatisticalAnalysisMissing2019`.
Discipline-register controls (non-Rubin, top venues): `mengMultipleImputationInferencesUncongenial1994a`
(Statistical Science), `kenwardLikelihoodBasedFrequentist1998`, `coxGeneralDefinitionResiduals1968`
(JRSS-B), `firthBiasReductionMaximum1993` (Biometrika), `efronBootstrapMethodsAnother1979`
(Annals). Extract CONCRETE, checkable features with quoted passages and `:line` refs (quotes
live in the rubric document, not the manuscript — D-17): how results are announced and
motivated; "we" usage; sentence length/subordination profile (measure it, e.g. mean words per
sentence and clause depth on a sample, against the same stats for the current manuscript);
hedging conventions; how notation enters prose; the definition→result→remark→example rhythm;
section and paragraph openers; how limitations are stated; abstract conventions. Deliverable:
a written rubric that says which current house rules CONFLICT with the discipline register
(prime suspects: the FK-10 target, the short-declarative bias, the mandatory "We show that"
formula, the em-dash ban vs. the discipline's parenthetical style) and which must stay
(all of ground-rule 2).

**Phase B — critical review of the current manuscript (flag-only).** Read
`manuscript/mi-spectral-apa.qmd` (the rendered prose Marcus reads) end to end against the
rubric. Per-section findings: paragraph id (level3), the convention violated, a short
exemplar contrast. Honest symmetric grading — also record what already conforms; the point
is a diagnosis Marcus can trust, not a demolition. Deliverable: a report committed under
`manuscript/reviews/` (suggested: `manuscript/reviews/style/style-review-<date>.md`).

**Phase C — the demonstration (the "show me" deliverable; the session is judged on this).**
Select 4–6 representative paragraphs spanning registers — suggested: the S1 opener, one S1
contributions-adjacent paragraph, one S2 background paragraph, one S4 theorem-adjacent
paragraph, one S5 results paragraph, one S6 discussion paragraph — and rewrite each in the
proposed register. Present side-by-side (current | proposed), each annotated with (a) the
rubric features exercised, (b) a line-by-line confirmation that every fact, number, hedge,
and citation is unchanged. Marcus ratifies, amends, or rejects the direction FROM THESE
EXAMPLES. Do not touch level3 in this phase; the side-by-sides live in the review document.

**Phase D — only after ratification: amend, recalibrate, sweep.** (i) Dated amendment(s) in
`decisions.md` + rewrite the CLAUDE.md "Manuscript prose style" section to the new register +
recalibrate the check_plan punctuation gate and scouts, one commit. (ii) The sweep itself, in
Marcus-gated batches (default: section-sized batches, S1→S6, one ratification gate per
section — the per-paragraph gate of todo/036 was for a riskier pass on a less mature corpus;
Marcus can tighten this). Each batch: level3 update script → check_plan → rebuild → render →
scouts clean. The abstract counts as a unit. (iii) A closing whole-document read for register
consistency (a half-rewritten corpus is worse than either register).

## Scope

- **IN:** the manuscript body — level3, currently 87 paragraphs + the tracked abstract.
- **OUT unless Marcus extends:** `manuscript/derivation.qmd` (separate sourced-audit
  artifact; its register is intentionally technical and its own), the v1 response letter
  (15/15 drafted in its own voice), figure captions (cheap to fold in if Phase B flags them).
- **Sequencing:** this pass PRECEDES Marcus's per-paragraph annotation and
  compile-enablement — he should annotate the post-review text once, not the pre-review text
  twice. The submission tail after it is unchanged: annotation → compile-enablement →
  derivation-audit 0/0 → Zenodo deposit → JAIGP.

## Defaults on open choices (act on these unless Marcus says otherwise)

1. **Batch size for Phase D:** section-sized batches with a Marcus gate per section.
2. **S3 (AI-collaboration section):** reviewed like everything else — the discipline register
   is compatible with its JAIGP-specific content.
3. **The FK-10 rule:** replaced by "match the exemplar register" (the rubric becomes the
   standard), not merely loosened.
4. **"Rubin style" operationalization:** the rubric IS the operationalization; where
   Rubin-the-author and modern-journal convention diverge (1987-book informality vs. current
   JASA norms), prefer the modern convention and note the divergence in the rubric.

## Known gotchas (from memory, all previously bitten)

- The citation hook resolves against cwd — write manuscript files from the repo root; if
  Edit/Write misfires on a `manuscript/` path, fall back to a Python script (NOT a Bash
  heredoc — heredocs eat a backslash level and corrupt LaTeX macros).
- Verify `git branch --show-current` (= `main`) before any rebuild/render; a concurrent
  session can switch the tree.
- A slow first `quarto render` is tinytex updating packages — let it finish (background it);
  do not build bypasses.
- `check_plan.py` runs from pre-commit when plan files are staged; run it manually before
  every commit anyway.

## Marcus prerequisites: NONE blocking

All exemplar sources are already owned in `literature/`. No acquisitions needed; no new
references proposed by this handoff.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be `main`, in sync
with `origin`; last substantive commit `4e93aaf`, the Lemma P derivation section). Read
`.prometheus/charter.md` for current state.

Task — the critical style review of the manuscript, per `todo/048-style-review-handoff.md`
(read it in full first; it is the spec of record): build a checkable style rubric from the
Rubin-authored and top-venue exemplars in `literature/` (read in-session, quoted with line
refs); run a flag-only critical review of `manuscript/mi-spectral-apa.qmd` against it,
naming which house style rules conflict with the discipline register; then produce 4–6
side-by-side demonstration rewrites (current vs. proposed register, facts/numbers/hedges/
citations provably unchanged) for Marcus's ratification. No level3 edits, no decisions.md
amendments, and no sweep until Marcus ratifies the direction from the demonstrations; after
ratification, follow the handoff's Phase D (dated amendments + guard/scout recalibration in
one commit, then section-batched sweep, check_plan green, rebuild + render per batch). The
accuracy invariants and citation discipline are untouchable throughout.
