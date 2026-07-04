# todo/043 — session handoff (2026-07-03 → next session)

**STATUS: OPEN.** Written at the end of a session that executed Phase 2 (MI-BIC), landed a new
Discussion caveat (G8), and set a standing reproducibility policy. This file is the resume prompt
for whoever (or whichever session) picks this up next.

## Recommended model / effort

**Sonnet 5, effort high.** Matches the saved default (`/effort high`) that ran the session that
produced this handoff. The remaining work (folding BIC into `run_all.R`'s `aggregate.R`, adding a
CLAUDE.md Commands entry, writing unit coverage in `00-test-primitives.R`) is reproducibility
engineering against an already-decided result — no new derivation, no open analytic question, so
the cross-model xhigh protocol (`feedback_crossmodel_derivation_protocol`) does not apply. It is
a genuine multi-file engineering task (understanding `aggregate.R`'s existing H1–H6 structure,
extending it consistently, writing real test assertions), so effort should stay at high rather
than drop to a quick mechanical pass.

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be
`da-engine-phase0-todo040`, in sync with origin — everything is pushed as of `8d4bc2d`). Read
`.prometheus/charter.md` first for full current-state context.

**Where things stand:** the DA-engine thread is fully closed. Phase 2 of the v1-review response
(MI-BIC, todo/040 §2) is now EXECUTED and landed: the main-grid BIC computation (60 cells,
R=2000, `verification/cache/run_all-prod-bic/`) confirms the correction is directionally right
for BIC but much smaller in yield than AIC's, because BIC's own `npar*log(N)` penalty already
resists most of the saturated-model pull at N≥200. A Marcus-directed small-N follow-up (N=50/100,
`verification/spikes/phase2-bic-smallN-probe.R`, not pre-registered) found the ambiguous regime
directly and showed the paper's "errors concentrate on the largest-RIV candidate" claim is itself
a large-N property for BIC. This landed as a new Discussion scope-limit paragraph, G8
(`S6-P4c` in `manuscript/plan/level3-paragraphs.json`, `decisions.md` D-23), not a full new BIC
results section. `check_plan.py` is green, the qmd was rebuilt, and the PDF render was confirmed
(exit 0, text present). Committed `942eaaf`; charter wrap `8d4bc2d`.

**Task 1 — get Marcus's review of the r1#8 draft (carried over, still open).** Read
`manuscript/reviews/v1/response/r1-8-data-augmentation.md` and present it to Marcus before
treating Phase 1 as closed. Confirmation-with-characterization framing: Amelia's EMB converges to
the +½·tr(RIV) headline as N→∞ and is confirmed, not undermined; genuine Bayesian posterior draws
carry a derived, disclosed correction; recentred-DA is the constructive remedy. Iterate on the
file directly if Marcus wants changes (Bash, not Edit/Write, per the citation-hook cwd gotcha).

**Task 2 — fold the MI-BIC work into `run_all.R` (new standing reproducibility gate, must close
before resubmission).** Marcus's directive (2026-07-03, charter + `todo/040` registration): any
verification result cited in the manuscript must be reproducible through the canonical
`verification/run_all.R` pipeline, not left as a spike or scratchpad script. The main-grid BIC
computation itself is already safe — it lives inside `verification/_modules/w3-sweep.R`, which
`run_all.R` phase 2 already sources, so it reproduces via the standard documented command with no
extra work. Three things are NOT yet folded in:
  1. **The AIC-vs-BIC summary** (the headline table: recovery rates, the concentration-on-MB
     null check, the N-scaling comparison) currently exists only as a throwaway scratchpad R
     script. Promote it into `verification/_modules/aggregate.R` (phase 5) so `verdicts.md`
     carries a BIC verdict alongside the existing H1–H6 AIC verdicts — read `aggregate.R`'s
     current structure first (it aggregates `w3` from `phase2-w3/summary.csv`, which already has
     the new `pi_bic_*`/`W3A_bic_*`/`W3C_bic_*` columns from this session's `w3-sweep.R` change,
     so no new R fields are needed, just the aggregation logic).
  2. **`verification/spikes/phase2-bic-smallN-probe.R`** is a standalone script, not sourced by
     `run_all.R`, not documented in CLAUDE.md's Commands section. Either wire it into
     `run_all.R`'s phase dispatch as a new phase, or (cheaper, matches the DA-engine spike
     precedent) leave it a spike but add an explicit CLAUDE.md Commands entry so a future session
     can find and rerun it without rediscovery.
  3. **`verification/00-test-primitives.R`** has zero coverage of the BIC arithmetic (`BIC_uncorr`/
     `BIC_corrected` in `run_one_w3`) or the new `amelia-loglik` `tryCatch` error-catch path added
     this session (it only fired once in 2000 reps at N=50 — that is incidental coverage, not a
     deliberate test).
  Full detail and the exact promotion debt list: `todo/040-v1-review-response-registration.md`
  (search "open promotion debt").

**Task 3 — Phase 3 (non-normal, gated) -> Phase 4 (remaining fixes, letter, annotation +
compile-enablement).** Phase 3 gated on the MVN-scope call (Marcus). Phase 4: Tier C fixes, Tier
A rebuttals, assemble the full point-by-point letter (folding in the r1#8 draft + the earned BIC
framing), annotation + compile-enablement -> compile + derivation-audit 0/0 + Zenodo -> JAIGP.
Optional/cheap along the way: extend the E3 bootstrap-floor exact-identity arm to the same 4
N-points Amelia's original scan has (closes gate item C7); verify Mode B's candidate IMB closed
form (CAS or a numeric check against the measured -0.005/-0.0065).

**Constraints carried forward:** frozen preregistered originals (`W1-bias-decomposition.R`,
`W2-lrt-power.R`, `W3-model-selection.R` @ SHA ddc9037) are untouched, not re-run. Edit level3
prose, never the rendered qmd directly (D-21). The citation hook misfires on Edit/Write of files
under `manuscript/` subdirectories or when cwd sits in one — use Bash for those writes instead.
Preregistration discipline applies: any new empirical decision (e.g. exactly how the BIC verdict
is phrased in `aggregate.R`'s output) gets a one-line dated amendment in
`todo/040-v1-review-response-registration.md` before code, not after.
