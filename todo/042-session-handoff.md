# todo/042 — session handoff (2026-07-02 → next session)

**STATUS: OPEN.** Written at the end of a session that closed the DA-engine provenance thread
and drafted Phase 1 of the v1-review response. This file is the resume prompt for whoever
(or whichever session) picks this up next.

## Recommended model / effort

**Sonnet 5, effort high.** This matches what ran the session that produced this handoff (set via
`/effort high`, the user's saved default). Task 1 (presenting the draft for review) is light.
Task 2 (MI-BIC) is moderate R/aggregation work plus one real scoping decision, but the *penalty
transfer itself* is already decided (see "BIC APPROACH" in the charter, 2026-07-01) — this is
not a new derivation that needs the cross-model xhigh protocol
(`feedback_crossmodel_derivation_protocol`). Escalate to that protocol only if Phase 2 surfaces
a genuine new analytic question (e.g., the effective-sample-size point turns out not to be a
simple scoping sentence).

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be
`da-engine-phase0-todo040`, in sync with origin — everything is pushed as of `780d4e3`). Read
`.prometheus/charter.md` first for full current-state context.

**Where things stand:** the DA-engine thread (todo/040/040b/041) is fully closed, including
provenance verification for all three newly-acquired references (von Hippel-Bartlett 2021, Efron
1979, von Hippel 2016 — all `verified → cited` in `todo/003`). Phase 1 of the v1-review response
(todo/040's phase table) produced a draft response-letter entry for reviewer1's data-augmentation
comment (r1#8) at `manuscript/reviews/v1/response/r1-8-data-augmentation.md`.

**Task 1 — get Marcus's review of the r1#8 draft.** Read
`manuscript/reviews/v1/response/r1-8-data-augmentation.md` and present it to Marcus (or ask him
to read it directly) before treating Phase 1 as closed. It uses a confirmation-with-
characterization framing: Amelia's EMB (the engine the paper's simulations actually use)
converges to the +½·tr(RIV) headline as N→∞ and is *confirmed*, not undermined; genuine Bayesian
posterior draws carry a derived, disclosed correction; recentred-DA is offered as a constructive
remedy. If Marcus wants changes, iterate on the file directly (it's plain markdown with
`@citekey` cites already resolving against `literature/`).

**Task 2 — Phase 2, MI-BIC.** This is the next substantive piece of work (todo/040 §2, table row
"Phase 2"). Before writing any code: CHECK whether the existing `phase2` cell RDS cache (under
`verification/cache/run_all-prod/phase2/` or similar — locate it) stored raw per-repetition
`ell_com`/`barL`/`npar`/`trRIV` values, or only final selection labels. That decides whether
MI-BIC can be computed by re-aggregating the existing cache or needs a focused rerun. Then add a
corrected-vs-uncorrected MI-BIC block to the sweep aggregation (the correction transfers verbatim
from AIC — both use $-2\bar Q_\infty$ as the deviance numerator, so the trace correction lands on
the numerator, not the penalty; use the complete-data $n$ in the BIC penalty per the "BIC
APPROACH" decision in the charter, dated 2026-07-01). This either earns the title's BIC claim
(reviewer r3#1, D-19) or means dropping BIC from the title — a real decision, not pre-solved.

**Constraints carried forward:** frozen preregistered originals (`W1-bias-decomposition.R`,
`W2-lrt-power.R`, `W3-model-selection.R` @ SHA ddc9037) are untouched, not re-run. Edit level3
prose, never the rendered qmd directly (D-21). The citation hook misfires on Edit/Write of files
under `manuscript/` subdirectories or when cwd sits in one — use Bash for those writes instead.
Preregistration discipline applies: write the MI-BIC penalty/cell-list decision down (as a
registration amendment in `todo/040-v1-review-response-registration.md`, following the existing
dated-amendment pattern) before running anything, not after.
