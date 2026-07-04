# todo/044 — session handoff (2026-07-03 → next session)

**STATUS: OPEN.** Written at the end of a session that closed Phase 1 (r1#8 approved and
folded into a Phase-4 point-by-point letter skeleton), backfilled 293 untracked repo-hygiene
files across 12 commits, and executed Task 2 (folded MI-BIC into `run_all.R`'s reproducibility
pipeline). This file is the resume prompt for whoever (or whichever session) picks this up next.

## Recommended model / effort

**Sonnet 5, effort high.** Matches the saved default (`/effort high`). The work ahead is mostly
response-letter prose drafting (r3#1 BIC, r1#7, r1#9) and Tier C mechanical level3 fixes, plus
one scope decision (Phase 3 non-normal) that needs Marcus directly rather than analysis — no
open derivation question, so the cross-model xhigh protocol
(`feedback_crossmodel_derivation_protocol`) does not apply. Effort should stay at high rather
than drop to a quick pass, since drafting an accurate, well-scoped response-letter entry from
existing evidence is real synthesis work, not a mechanical transcription.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be
`da-engine-phase0-todo040`, in sync with origin — everything pushed as of `7999860`). Read
`.prometheus/charter.md` first for full current-state context. **Note:** the charter was last
wrapped at `b90d540` (referencing `fb7b84b`), and the MI-BIC fold-in commit `7999860` landed
after that wrap — check `git log` against the charter's `last_synced_commit` and run
`/prometheus:wrap` early in the session if it reads stale.

**Where things stand:** the v1 AI-review response milestone has three of its four phases
substantively done. **Phase 1** (r1#8 data-augmentation response) is CLOSED: Marcus approved the
draft ("Looks right"), and it is folded into `manuscript/reviews/v1/response/response-letter.md`
— a running point-by-point letter with all 15 review comments as sections, each tagged DRAFTED /
EXECUTED-PENDING-TEXT / PENDING. **Phase 2** (MI-BIC) is CLOSED including the reproducibility
fold-in: the BIC verdict now appears in `aggregate.R`'s `verdicts.md` output automatically from
any future `run_all.R` run, `verification/spikes/phase2-bic-smallN-probe.R` has a CLAUDE.md
Commands entry, and `00-test-primitives.R` covers the BIC arithmetic and the `amelia-loglik`
error-catch path (commit `7999860`; regression-verified byte-identical against the pre-refactor
cache). Separately, this session backfilled 293 untracked repo-hygiene files — a month of
unretained work-product (the todo/030 concept map, the public-release transcript scrubber, the
S5 tribunal and todo/038 text-validity tkal run records, todo/032 collab-analysis, the todo/040
DA-engine spike caches, various prose-pass/derivation-audit scout outputs) — across 12 grouped,
provenance-labeled commits plus a charter wrap (`b90d540`). The working tree is fully clean and
`da-engine-phase0-todo040` is in sync with `origin`.

**Task 1 — Phase 3 (non-normal), GATED.** Needs Marcus's explicit MVN-scope decision before any
code: does a non-normal empirical illustration (via the brms-as-imputer cross-check, ~24s/fit,
already spiked and working) enter the manuscript, or does the Discussion stay a prediction-only
paragraph? The theory already predicts the two-regime split (estimated-scale families keep
+1/2 tr(RIV); scale-free logistic/Poisson collapse to the known-scale case, 0 under FIML /
−1/2 tr under proper MI). See "NON-NORMAL SCOPE" in `.prometheus/charter.md`'s Decisions made
and `todo/040-v1-review-response-registration.md` §2's phase table. Ask directly if this
decision has not already been made — do not write code first.

**Task 2 — Phase 4, the response-letter entries that do NOT need Phase 3.**
`manuscript/reviews/v1/response/response-letter.md` has 13 PENDING / EXECUTED-PENDING-TEXT
entries. Cheapest and most valuable to close first: **r3#1 (BIC)** is EXECUTED-PENDING-TEXT —
all its evidence (G8/D-23, the `aggregate.R` BIC verdict) is already landed; it only needs
response-letter prose, following the same shape as the r1#8 entry (quote the reviewer comment,
report the measured numbers, state the framing: correction is directionally right but much
smaller in yield than AIC's, because BIC's own `npar*log(N)` penalty already resists most of the
saturated-model pull at N≥200, with the small-N follow-up showing the ambiguous regime directly).
**r1#7** (heavy-tail N=1000, a one-sentence N-vs-repetition-count clarification) and **r1#9**
(nested-confound, already answered by the existing W4 non-nested measurement + MCAR twins) are
also Tier A rebuttals needing no new evidence, just writing. **Tier C** (proof#10/11,
contra#12–15, r2#4–6) are easy level3 prose/notation fixes — rebuild via
`scripts/build_manuscript_apa.py` after each and confirm `quarto render` still exits 0.

**Task 3 — after Phase 3/4 close: annotation + compile-enablement.** Per-paragraph Marcus
annotation pass, then flip `compile_enabled`, run `/derivation-audit` (target 0 blocker / 0
warn), and move toward the Zenodo deposit + JAIGP submission per the milestone list in the
charter.

**Constraints carried forward:** frozen preregistered originals (`W1-bias-decomposition.R`,
`W2-lrt-power.R`, `W3-model-selection.R` @ SHA ddc9037) untouched, not re-run. Edit level3 prose,
never the rendered qmd directly (D-21). The citation hook misfires on Edit/Write of files under
`manuscript/` subdirectories or when cwd sits in one — use Bash for those writes instead. Any new
empirical decision (the non-normal scope call, or how a Tier C fix is worded) gets a one-line
dated amendment in `todo/040-v1-review-response-registration.md` before code, not after. The
reproducibility fold-in gate (Marcus, 2026-07-03) applies to any new cited result going forward
— promote spikes into `run_all.R`/`aggregate.R`/CLAUDE.md before citing them, not after.
