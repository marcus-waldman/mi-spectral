# Todo 040 — REGISTRATION + PLAN: v1 AI-review response (paper 88)

**Status:** REGISTERED 2026-07-01, **before any Phase-0 engine code was written**. This
document records the phased plan, the two data-augmentation (DA) engines, and the Phase-0
gates *and their pass criteria fixed before running*, per the paper's own preregistration
discipline (doc-before-code). Source of the review: `manuscript/reviews/v1/ai-review-paper-88.md`
(Reviewer3.com, 15 comments across 5 personas). Triage of record: the charter
(`.prometheus/charter.md`, "Current milestone" + Decisions "v1 AI-REVIEW RESPONSE PLAN",
"DA ENGINE STRATEGY", "BIC APPROACH", "NON-NORMAL SCOPE").

Predictions and pass criteria written here precede the code. If reality differs, the
manuscript framing and the response letter modify to match reality — a failed spike is
reported, not re-run away. Any amendment to this file after the first run is dated and labelled.

The frozen preregistered originals (`W1-bias-decomposition.R`, `W2-lrt-power.R`,
`W3-model-selection.R`, cited at SHA ddc9037) are **not touched and not re-run**. All new
work is a NEW script or a `run_all.R` module. Each empirical answer gets a one-line dated
registration amendment (below), not an edit to a frozen file.

---

## 1. What the review actually asks (triage, 4 tiers)

Full triage lives in the charter. Compressed here so this file stands alone.

- **Tier A — already in the paper → response-letter rebuttal, no new work.** The heavy-tail
  N=1000 remark (r1#7; reviewer conflated sample size N with repetition count R — finite
  variance, one clarifying sentence); the nested-confound (r1#9; the W4 non-nested measurement
  + MCAR twins already isolate mechanism from complexity); the DA control (r1#8) is *disclosed*
  as future work already, but Marcus's steer is to **earn evidence, not only rebut** → Phase 1.
- **Tier B — the one real decision.** BIC (r3#1) is in the title (D-19) but never formulated
  in the body → earn it or drop it → Phase 2.
- **Tier C — easy fixes (level3 → rebuild).** ± dispersion definition (r2#4); name all four
  selection-sweep models (r2#5); explicit Σ / correlation placement (r2#6); abstract
  estimated-scale qualifier (proof#10); "trace component" scoping (proof#11); α sign
  (contra#12); KS 0.019-vs-0.018 text/figure mismatch (contra#13); disambiguate k
  (param count vs model index, contra#14); standardise m vs M (contra#15) → Phase 4.
- **Tier D — modest new content.** Non-normal/GLM behaviour (r3#2; MVN is a scope decision →
  Discussion prediction, empirical illustration only if the scope decision is taken) → Phase 3;
  congeniality diagnosis has no cited method (r3#3) → reference backlog `todo/003` + a
  Discussion sentence in Phase 4.

Marcus's steer: get EVIDENCE for the two cheap gaps (DA replication, MI-BIC); "leave space" —
the forks (brms role, non-normal scope) are **gates**, decided by measurement, not pre-solved.

---

## 2. Phased order of operations

| Phase | What | Gate / output |
|---|---|---|
| 0 | De-risk the DA engines before committing. Two smoke spikes at R=100. | tr(RIV) matches shown to Marcus; brms runtime gate decided. **This file + the spikes.** |
| 1 | DA replication of the headline cells with the chosen exact-DA engine; compare to Amelia + analytic. | Converts G3 from "empirical tolerance" to tested equivalence, or surfaces a real engine difference (both reportable). |
| 2 | Add an MI-BIC block to the sweep aggregation; corrected-vs-uncorrected MI-BIC beside AIC. | Earns the title's BIC claim, or (if it does not hold) drops BIC from the title. |
| 3 | Non-normal fork — **GATED on 0b + a scope decision.** | Empirical two-regime illustration (needs Marcus + a `decisions.md` entry) *or* a Discussion-only prediction paragraph. |
| 4 | Tier-C easy fixes (level3 → rebuild) + Tier-A rebuttals + point-by-point response letter; fold in the pending per-paragraph annotation + compile-enablement. | The revision toward JAIGP submission. |

---

## 3. Two-engine DA strategy (fixed before code)

Reviewer r1#8 objects that the proper-MI validation used Amelia's EMB (approximately-Bayesian
bootstrap + EM), not *exact* posterior draws, and asks for a data-augmentation control. Two
engines answer it, and one of them also unlocks the non-normal fork:

- **(i) Hand-rolled conjugate DA — `impute_mvn_conjugate()`.** The exact-posterior MVN Gibbs
  sampler under the reference prior p(μ,Σ) ∝ |Σ|^{−(p+1)/2}:
  - **I-step (impute):** each observation's missing block given its observed block under the
    current (μ,Σ), a conditional-normal (posterior-predictive) draw.
  - **P-step (posterior):** from the current completed data (ȳ, sum-of-squares SS with the
    complete-data divisor N), Σ ~ Inverse-Wishart(N−1, SS = (N−1)S) and μ | Σ ~ N(ȳ, Σ/N).
  - Alternation **is** data augmentation (Tanner–Wong 1987; Schafer 1997 Alg. 5.2). Our
    non-monotone pattern has no one-shot closed form, so the iteration is required.
  - Cheap, exact-conjugate, auditable, and it uses **R's own Mersenne-Twister RNG**, so a
    worker that has called `set.seed(20260522 + r)` is bit-reproducible and core-count
    invariant. This is the reason we do **not** depend on `norm::da.norm`: its separate
    `rngseed()` state is fragile under the parallel cluster and single-precision-sensitive
    (Marcus recalls prior cluster issues). `norm::da.norm` is kept only as an OPTIONAL third
    cross-check, and only after a serial smoke test.
- **(ii) brms/Stan as a general-family imputer.** Multivariate-Gaussian posterior-predictive
  completions fed into our **existing** deviance / tr(RIV) analysis (`mi_fit_mvn` → `riv_sample`
  → the T/A/B decomposition). This is brms **as an imputer** — an intercept-only joint model
  whose missing cells are drawn from the posterior — NOT the one-stage `bf(y | mi())` full-Bayes
  (a different estimand that couples imputation and analysis) and NOT `brm_multiple` pooling.
  brms unifies the DA control (r1#8) with the non-normal fork (r3#2): the same imputer swapped
  to a non-Gaussian family generates the Phase-3 illustration *if* the scope decision is taken.
  Its **per-dataset runtime** is the gate that decides its role.

---

## 4. Phase-0 gates and pass criteria (fixed before running)

Both spikes run on the **W1 theorem cell** — the exact original-W1 configuration so the
comparison is apples-to-apples with the frozen headline: 4-variate MVN, `default_mu`,
`default_Sigma`, N=200, `apply_mar(X)` (non-monotone: X₁,X₂ missing, driven by X₃,X₄; the
original W1's missingness, not `ampute`), observed-data MLE θ̂_obs from EM (deterministic
`em_mvn`, not the `da.norm` sampler), M=50, R=100. Per-replicate seed `set.seed(20260522 + r)`,
identical to W1, so X^(r) and mar^(r) are bit-identical across engines. All three engines
(conjugate DA, Amelia, analytic) are evaluated on the SAME `mar$Y` per replicate — a paired
comparison that cancels per-replicate noise.

The measured per-replicate quantities mirror the frozen W1:
- T_r = barL_obs − ℓ_com(θ̂_com)  → predicted **+½ tr(RIV)**
- A_r = barL_obs − ℓ_com(θ̂_obs)  → predicted **tr(RIV)**
- B_r = ℓ_com(θ̂_obs) − ℓ_com(θ̂_com) → predicted **−½ tr(RIV)**
- sample tr(RIV) = Rubin (1+1/M) W⁻¹B trace; analytic tr(RIV) = `tr_riv_analytic`.

### Spike 0a — conjugate DA. Pass criteria (all fixed here):

- **G0a-1 (tr(RIV) match).** The conjugate-DA **sample** tr(RIV), averaged over R=100, agrees
  with the **analytic** tr(RIV) within Monte-Carlo error (|Δ| ≤ 2 combined MCSE). Diagnostic,
  not headline: the sample estimator carries a known finite-M variance, so this is a
  consistency check, not an exact identity.
- **G0a-2 (headline bias).** The conjugate-DA T̂ contains **+½ · (sample tr(RIV))** in its 95%
  MC CI — the same pass rule the frozen W1 applies. (Report A and B too; A→tr(RIV), B→−½tr(RIV).)
- **G0a-3 (engine agreement).** The conjugate-DA T̂ agrees with the **Amelia** T̂ within the
  combined MCSE (paired, same `mar$Y`). This is the direct answer to r1#8: exact DA and EMB
  land the same headline. A resolved difference is equally reportable (it would mean the
  bootstrap approximation leaves a fingerprint — a real finding, not a failure).
- **G0a-4 (PSD/RNG stability across the 20 workers).** Zero non-PSD Cholesky events across all
  100 replicates × all DA sweeps on the 20-worker PSOCK cluster; and bit-identical results on a
  re-run of the same seed (reproducibility of R's RNG under the cluster, the property
  `norm::da.norm` lacks).

### Spike 0b — brms feasibility. Deliverables (a GATE, not a solve):

- **G0b-1 (does it fit).** brms builds the MVN imputer on our missing data and returns
  posterior-predictive completions of the missing cells (yes/no).
- **G0b-2 (tr(RIV) match).** On a handful of replicates, the brms-imputer sample tr(RIV) is
  consistent with analytic / conjugate (within MC error at the small R used).
- **G0b-3 (runtime).** Per-dataset wall-clock (compile-once amortised + per-fit sampling),
  measured. This decides brms's role: **workhorse** (fast enough for the full sweep) /
  **cross-check** (feasible for tens of cells) / **non-normal-only** (reserve for Phase 3) /
  **infeasible**. No target is pre-committed; the number decides.

**Phase-0 does NOT run any non-normal cell.** The 0b spike is MVN (multivariate-Gaussian
completions) and stays inside the current MVN scope. A non-normal family trips the scope
decision and requires Marcus's explicit call plus a `decisions.md` entry BEFORE it runs (§6).

---

## 5. Registration amendments (dated; one line per empirical answer)

- **2026-07-01, DA replication engine + cells.** The Phase-0 spike (§8 below) was extended past
  its original smoke scope directly into the Phase-1 evidence: two independent exact-DA engines
  (hand-rolled conjugate Gibbs + `norm::da.norm`) run to R=20000 on the W1 cell across
  N=200..2000, cross-validated to the 3rd decimal, plus a brms/Stan independent check. This
  *is* the Phase-1 empirical answer — no separate production run was needed once the spike
  surfaced a real, derivable engine effect rather than noise. See §8 for the full result.
- **2026-07-02, Phase 1 response-letter draft.** The DA-engine evidence (§8) plus its cross-model
  derivation (`todo/040-audit-response-fable5.md`, `todo/040b-gpt55-gate-package.md`) plus the
  now-verified provenance (`todo/003`: von Hippel-Bartlett 2021, Efron 1979, von Hippel 2016)
  are folded into a response-letter draft for r1#8:
  `manuscript/reviews/v1/response/r1-8-data-augmentation.md`. Framing: confirmation-with-
  characterization (Amelia's EMB converges to the headline as N->infinity and is confirmed, not
  undermined; genuine posterior draws carry the derived correction D; recentred-DA offered as the
  constructive remedy). Draft only, pending Marcus's review before folding into the Phase-4
  point-by-point letter.
- **2026-07-03, r1#8 draft approved; Phase-4 letter skeleton created.** Marcus reviewed
  `r1-8-data-augmentation.md` ("Looks right") and asked for it to go into the Phase-4 letter.
  Created `manuscript/reviews/v1/response/response-letter.md`: all 15 review comments as
  sections, each quoting the reviewer comment and tagged DRAFTED / EXECUTED-PENDING-TEXT /
  PENDING. r1#8 is the only DRAFTED entry (full approved text folded in verbatim). r3#1 (BIC)
  is tagged EXECUTED, PENDING TEXT — the Phase 2 empirical work (G8/D-23) is done but its
  response-letter prose is not yet written or reviewed; the other 13 comments remain PENDING,
  to be drafted across Phase 3 (r3#2) and Phase 4 (everything else). Written via Bash per the
  citation-hook cwd gotcha (the file contains three live @citekeys).
- **2026-07-02, Phase 2 MI-BIC — cache check + plan (before any code).** Inspected
  `verification/cache/run_all-prod/phase2-w3/*.rds` directly (`str()` on `results[[1]]`/`[[2]]`
  of a representative cell). Each per-repetition record stores only `error`, the four selection
  labels (`sel_oracle/sel_uncorr/sel_corrected/sel_sb`), and the `trRIV`/`trRIV_obs` vectors —
  **not** `barL`/`ell_com`. `AIC_uncorr`/`AIC_corrected` are computed inside `run_one_w3` but
  discarded before the return, so the per-model deviance numerator is not recoverable from the
  cache: knowing which model won under AIC's `2*npar` penalty does not determine which model
  wins under BIC's `npar*log(n)` penalty, because the relative *sizes* of the `barL` gaps between
  models are needed and are not stored. **Decision: a focused rerun is required, not a
  re-aggregation.**
  Penalty and correction (per the charter's 2026-07-01 "BIC APPROACH" decision): the
  `+tr(RIV)` correction transfers to BIC **verbatim on the numerator** (`AIC` and `BIC` both use
  `-2·barQ_∞` as the deviance numerator; only the penalty differs), so
  `BIC_uncorr = -2*barL + npar*log(N)` and `BIC_corrected = -2*barL + npar*log(N) + trRIV_obs`,
  reusing the exact same `trRIV_obs` already computed for AIC. `N` is the **complete-data** sample
  size (`cell$N`), not an MI-specific effective n — this sidesteps the effective-sample-size
  controversy per the charter decision and turns reviewer r3#1's objection into a scoping
  sentence.
  Cell list and compute plan: extend `run_one_w3` (in `verification/_modules/w3-sweep.R`, not a
  frozen original) to compute the BIC selections **in the same pass** as AIC — the expensive part
  (complete-data lavaan fits, FIML fits, Amelia imputation) is identical regardless of which
  criterion is derived from `barL`, so computing both from one set of fits costs nothing extra
  over computing AIC alone. Rerun the **same 60-cell grid** (2 patterns × 2 mechs × 3 N × 5
  engine/M/cong slots) at the **same R=2000** used for the existing AIC production numbers, so the
  BIC and AIC selection-rate tables are directly comparable cell-for-cell. Output goes to a **new**
  `out_suffix` (`prod-bic`, not `prod`) so the existing `phase2-w3` cache — already the source of
  cited W3 numbers in the landed manuscript (S5 tables, the IC ladder discussion) — is not
  clobbered; since the code change is additive (new computations appended after the existing ones,
  no change to RNG draws or data generation), the AIC-side outputs should reproduce bit-identically
  under the same seeds, but a separate directory avoids any risk to already-cited results. A smoke
  run (R=100, phase "2" only, `out_suffix=smoke-bic`) precedes the ~2.5–3h production rerun (the
  original phase2-w3 run took 9212s ≈ 2.56h total elapsed across 60 cells on 20 cores) to catch
  code errors cheaply. Aggregation: a focused summary (uncorrected-vs-corrected MI-BIC selection
  rates, analogous to the existing W3A/W3C metrics) decides whether BIC selection is
  "corrected-improves-over-uncorrected" in the same direction and magnitude as AIC — the basis for
  earning or dropping the title's BIC claim (r3#1, D-19). Not yet run as of this amendment.

- **2026-07-02, Phase 2 MI-BIC — RESULT (R=2000, 60 cells, `run_all-prod-bic/phase2-w3/`, 0
  errors, 174.9 min elapsed).** The correction is real, correctly signed, and statistically
  resolved, but its practical magnitude is much smaller for BIC than for AIC, because BIC's own
  `npar*log(N)` penalty already resists most of the saturated-model pull before any correction is
  applied — this is BIC's known consistency property, not an artifact.
  - **Headline recovery rates** (true model MC, congenial+FIML cells, n=36): AIC
    oracle=0.901/uncorrected=0.648/corrected=0.777 (correction closes about 57% of the oracle gap);
    BIC oracle=1.000/uncorrected=0.983/corrected=0.990 (uncorrected BIC is already close to
    ceiling, so the correction closes a much smaller absolute gap -- from 1.7 pp of error down to
    1.0 pp).
  - **Direction holds almost everywhere.** 55/60 cells show pi_bic_corrected >= pi_bic_uncorrected;
    the 5 exceptions are all tiny (-0.003 to -0.001) and sit at the empri_frac=0.5
    ("uncongenial") cells already at 0.998-1.000 recovery -- ceiling noise, not a reversal.
  - **W3C analogue holds.** Where uncorrected BIC does misclassify, the error still concentrates
    on the highest-RIV candidate (MD) in the same way AIC's does -- W3C_bic is about 1.000 in
    nearly every cell. The partial exceptions are the monotone_MNAR_N200 cells (W3C_bic
    0.571-0.974), where uncorrected BIC makes very few errors (5-39 out of 2000) and a nontrivial
    share land on a different over-parameterized candidate -- a small-count boundary effect at the
    point where BIC is already near-perfect, not a failure of the theorem's direction.
  - **New, theory-consistent H3-style pattern not present for AIC.** The gap-to-oracle
    (W3B_bic, median over MAR+cong/fiml cells) shrinks monotonically with N -- 0.00875 (N=200) ->
    0.00425 (N=500) -> 0.00175 (N=1000) -- while AIC's analogous gap does not shrink (0.093 ->
    0.073 -> 0.082, roughly flat/noisy). This is a corollary the theory predicts and this run
    confirms: BIC's penalty grows with N (so it becomes consistent and swamps the O(1) trace
    correction as N approaches infinity), while AIC's penalty is a fixed 2*npar (so its O(1)
    correction never vanishes). The correction's own footprint (W3A_bic, uncorrected-to-corrected
    gap) shrinks in parallel -- 0.0104 -> 0.0040 -> 0.0056 by N -- while AIC's stays flat
    (about 0.125-0.134 across N).
  - **Framing implication for the response letter / title.** This is not "BIC behaves exactly
    like AIC" -- it is a different, and arguably more informative, story: the theory correctly
    predicts *different* correction behavior for AIC (non-vanishing, O(1) forever) vs BIC
    (vanishing as N grows, tracking BIC's own consistency), and both predictions are confirmed in
    the same 60-cell grid. The correction earns its place in the BIC claim on direction,
    residual-error concentration, and this falsifiable N-scaling prediction -- but the manuscript
    should not claim a percentage-point improvement of AIC's size for BIC; it should state
    candidly that BIC's own penalty already does most of the work, with the trace correction
    closing the remainder in a way that shrinks (not disappears) as N grows.
  - **Not yet decided:** whether this reframed BIC story is written into the title/body as-is, a
    softened version, or (least likely given how consistently the direction holds) dropped. This
    is Marcus's framing call, same as the DA-engine fork.
  Cache: `verification/cache/run_all-prod-bic/phase2-w3/` (60 .rds + summary.csv); code:
  `verification/_modules/w3-sweep.R` (BIC computation added in the same pass as AIC, no new
  fitting cost). Smoke-tested first at R=100 (run_all-smoke-bic, 0 errors, consistent direction).

- **2026-07-02, Phase 2 MI-BIC follow-up — free check + small-N probe plan (before running).**
  Marcus asked for a design point where BIC is more ambiguous, since the 60-cell grid puts
  uncorrected BIC near ceiling (98.3%) almost everywhere. Two candidate levers: (a) free --
  check whether MB (equal npar to MC, both 10) is ever a live competitor in the already-collected
  `prod-bic` cache, since BIC's and AIC's penalty terms are literally identical for that pair, so
  any correction effect there would be fit-driven, not penalty-driven; (b) a rerun -- smaller N,
  since BIC's discriminating power is `Δnpar·log(N)` against a roughly-N-invariant chi-square
  deviance-noise scale, so small N is where BIC's own consistency hasn't kicked in yet.
  **(a) result: null.** Read every per-repetition `sel_uncorr/sel_corrected/sel_bic_uncorr/
  sel_bic_corrected` label across all 60 cells x R=2000 (120,000 reps total): MB was selected
  **zero times**, under any of AIC/BIC x corrected/uncorrected. MB is not a live competitor in
  this design at all (it must fit worse than MC by enough margin that no penalty scheme ever
  prefers it) -- every misclassification in the grid lands on MD, confirming there is no
  equal-penalty ambiguity to exploit here. This rules out lever (a) and motivates proceeding to
  lever (b).
  **(b) plan (Marcus approved, proceeding).** Add N=50 and N=100 to the existing
  `non_monotone`/MAR/congenial slice only (not the full 60-cell grid): one `fiml` cell +
  one `amelia` M=20 congenial cell per N, 4 new cells total. Implemented as a standalone probe
  script (`verification/spikes/phase2-bic-smallN-probe.R`), reusing `run_one_w3` from
  `w3-sweep.R` unchanged (it is already generic in `cell$N`) rather than editing the main
  60-cell grid in `run_w3_sweep`. Smoke test first at R=100 to check `lavaan`/Amelia don't
  degenerate at N=50 (untested regime for this pipeline); if stable, rerun at R=2000. Output to
  its own cache dir (`verification/cache/smallN-bic-probe*/`), not mixed into `prod-bic`.

- **2026-07-02, small-N BIC probe -- RESULT (R=2000, 4 cells, `smallN-bic-probe-prod/`).** One
  degenerate Amelia draw at N=50 (a rank-deficient imputation whose downstream `loglik_mvn` call
  had a dimension mismatch) crashed the first cluster run; fixed by wrapping that computation in
  `tryCatch` the same way the upstream `impute_mvn_amelia()` call already is
  (`verification/_modules/w3-sweep.R`), so a single bad repetition is skipped rather than halting
  the whole R=2000 job. Rerun: 3999/4000 reps ok (1 caught error at N=50 Amelia), 0 crashes.
  **This is the ambiguous BIC regime Marcus asked for, and it is genuinely different from the
  main grid, not just a smaller version of it:**
  | N | engine | pi_bic_uncorr | pi_bic_corr | pi_bic_oracle | W3A_bic | W3C_bic |
  |---|---|---|---|---|---|---|
  | 50  | fiml   | 0.745 | 0.777 | 0.929 | +0.032 | 0.624 |
  | 50  | amelia | 0.751 | 0.774 | 0.929 | +0.024 | 0.550 |
  | 100 | fiml   | 0.936 | 0.958 | 0.994 | +0.021 | 0.890 |
  | 100 | amelia | 0.930 | 0.957 | 0.994 | +0.026 | 0.878 |
  (main-grid N=200 congenial/FIML comparison point: pi_bic_uncorr ~0.978-0.983, W3A_bic ~0.011,
  W3C_bic ~1.000.)
  Two things move together as N drops from 200 to 50: (i) **the correction's absolute yield
  grows** -- W3A_bic roughly triples (0.011 at N=200 to 0.024-0.032 at N=50), the mirror image of
  the "shrinks with N" pattern documented in the main-grid result above, now confirmed from the
  other end of the N axis; and (ii) **the W3C-analogue genuinely weakens** -- only 55-62% of
  uncorrected BIC's (much more frequent, ~25% of reps) errors at N=50 land on the highest-RIV
  candidate MD, down from ~100% at N>=200. This qualifies, rather than undercuts, the paper's
  "errors concentrate on the highest-RIV model" claim: that concentration is itself something
  that strengthens with N (other, non-maximal-RIV candidates are live competitors at small N),
  not a fixed small-sample law. Both patterns are internally consistent with the same mechanism
  documented in the main-grid result: BIC's own `npar*log(N)` penalty is what suppresses both the
  overall error rate and its concentration on the highest-RIV model as N grows, so at small N,
  before that penalty has taken hold, both the correction's role and the value of tracking the
  general RIV geometry (not just the single highest-RIV candidate) are larger.
  **Not yet decided:** whether/how this small-N finding enters the response letter or manuscript
  (e.g. as a Discussion caveat scoping the "concentrates on highest-RIV" claim to N large enough
  for BIC's penalty to dominate) -- reported to Marcus for the framing call.
  Code: `verification/spikes/phase2-bic-smallN-probe.R` (new; reuses `run_one_w3` unchanged) +
  the `amelia-loglik` error-catch fix in `verification/_modules/w3-sweep.R` (also active in the
  main 60-cell grid going forward, though it never fired there at N>=200).

## 6. What trips the MVN-scope decision

MVN-only is the project default (`project_scope_keep_mvn`). A non-normal empirical cell (Phase 3)
is a real extension of scope. The theory already **predicts** the split without any new run:
estimated-scale families (e.g. Gamma, t) keep **+½ tr(RIV)**; scale-free GLMs (Bernoulli,
Poisson) collapse to the known-scale case (0 under FIML, −½ tr(RIV) under proper MI). So the
free, honest answer to r3#2 is a Discussion prediction paragraph. brms only makes an empirical
illustration tractable, and even then the analytic tr(RIV) for a GLM is optional (sample tr(RIV)
suffices for an illustration). Running a non-normal cell needs Marcus's explicit call + a dated
`decisions.md` entry first.

---

## 7. Files (new; frozen originals untouched)

```
todo/040-v1-review-response-registration.md   this file
verification/da-conjugate-engine.R            impute_mvn_conjugate() + helpers (new engine)
verification/spikes/phase0a-da-conjugate.R    spike 0a (R=100, conjugate vs Amelia vs analytic)
verification/spikes/phase0b-brms-imputer.R    spike 0b (brms feasibility + runtime gate)
verification/spikes/diag-*.R                   Phase-0a diagnostics (localizing the DA finding)
verification/cache/spikes/                     spike outputs (RDS + logs)
```

---

## 8. PHASE-0 RESULT (executed 2026-07-01, dated amendment)

**Spike 0a surfaced a material, well-characterized finding that reframes Phase 1. It is a
theory/framing fork for Marcus, not resolved here.**

**Mechanics of the engine — all validated (not the finding):**
- I-step exact: a fixed-θ (θ̂_obs) conditional draw reproduces the deterministic FITTED value
  `barQ_fiml_analytic` to −0.04 ± 0.17 (paired). The conditional-normal machinery is correct.
- θ* dispersion correct: the conjugate chain's parameter draws match the analytic
  observed-info⁻¹ (rel-Frobenius 0.145 vs I_obs⁻¹, 0.329 vs I_com⁻¹) — the right amount of
  proper-MI parameter uncertainty.
- Sample tr(RIV) agrees across engines: conjugate 6.41 ≈ Amelia 6.49 (analytic 5.61 is the
  expected lower, expected-info Efron–Hinkley reference — a known sample-vs-expected gap).
- PSD/RNG stability: 0 non-PSD Cholesky events over 100 reps × 20 workers; bit-reproducible.

**The finding — the deviance bias T diverges by engine class (100×, R=20000):**
On the W1 cell (N=200), paired against the exact FITTED value and normalized by tr(RIV):
- exact Bayesian DA — **conjugate −0.783 (se .0023, R=20000)** and **`norm::da.norm` −0.783 (se
  .0031, R=10000)** — the two independent Jeffreys engines are IDENTICAL to the third decimal
  (property of the method, not my code); **brms −1.36 (R=6, estimate)**.
- MLE-centered constructions — **Amelia −0.087 (se .0025)**, **gauss/Laplace −0.121 (se .0020)** —
  small but resolved below 0 (≈ −0.1·tr(RIV), not exactly the +½ FITTED headline).
- **Persistent, converges to ≈ −0.74:** −0.783/−0.766/−0.764/−0.746 at N=200/500/1000/2000 (R up
  to 2e4). Small resolved downward drift (~2σ); a+b/N fit gives asymptote a≈−0.74, b≈−8 — converges
  to a nonzero constant, NOT vanishing (an O(1/N) term would have fallen ~10× to ≈−0.08 by N=2000).
- **Mechanism:** the Jeffreys IW posterior mean of Σ is inflated, E[Σ|Y]=(N−1)/(N−p−2)·S. This
  inflates imputation variance O(p/N) per cell × O(N) cells = an O(tr(RIV)) downward bias.
  Deflating (IW re-centered so E[Σ|Y]=S) removes the DOMINANT ~69% (−0.783→−0.244), NOT all —
  residual −0.244 = higher-order IW shape (−0.12) + a baseline parameter-draw term (−0.12) the
  MLE-centered constructions also carry. Runs: `verification/spikes/phase0a-confirm{,-xl}.R`.

**Discriminating test EXECUTED (2026-07-01, `phase0a-calibrated.R`, paired FITTED-relative):** the
two "correctly-centered" proper engines DIVERGE as N→∞:
- **Amelia (bootstrap EMB) − FITTED: −0.099/−0.047/−0.029/−0.019 at N=200/500/1000/2000 → 0**
  (~O(1/N)). Amelia — the engine the PAPER validated with — converges to +½. Empirical validation
  asymptotically sound; its N=200 shortfall (W1 That ~0.83× pred) is the vanishing finite-N term.
- **Gaussian/Laplace draw N(θ̂_obs,I_obs⁻¹) − FITTED: −0.123/−0.104/−0.099/−0.108 → −0.106
  PERSISTENT.** No prior inflation (MLE-centered), yet persists — this is the **Jensen effect of
  imputing with a DRAWN Σ** (Schur complement Σ_{M|O} is nonlinear in Σ, so E[Σ_{M|O}(Σ*)] >
  Σ_{M|O}(Σ̂); O(1/N)/cell × O(N) cells = O(1)).

So the −0.74 (Jeffreys IW) = removable mean-inflation (−0.54) + IW-skew (−0.12) + the persistent
Jensen term (−0.11). Refines the earlier "collapses to the amelia baseline": it collapses to the
GAUSS/Jensen baseline (−0.11, persistent), and AMELIA is the outlier that vanishes. Both specs are
partly right: Spec 1 (removable prior bias) is the −0.66 IW-vs-gauss part; Spec 2 (genuine
persistent proper-vs-FITTED gap) is REAL for every Bayesian posterior draw (gauss −0.11, IW −0.74,
brms −1.36) but NOT for the bootstrap. **New open puzzle for Fable: why does the bootstrap escape
the Jensen term and converge while genuine Bayesian draws don't?** Applied consequence unchanged:
the term scales with each candidate's own tr(RIV) → REINFORCES the paper's selection direction,
changes correction magnitude not sign. Paper's validated engine (Amelia) → the theorem; a reviewer's
"standard DA" (Bayesian norm/brms/mice) sits on the persistent branch → disclose + scope.

**Reading:** this is exactly reviewer r1#8's concern realized — the choice between a canonical
exact DA engine and Amelia's EMB changes the measured Q-function deviance bias by ~0.75·tr(RIV).
It also touches the project's FITTED-vs-ORACLE sign seam (memory `project_fitted_vs_oracle_sign`):
Amelia/EMB sits at the FITTED +½ branch; the exact Bayesian posterior-predictive (which the
M→∞ DA average estimates) sits at a more-negative branch. Whether this is a separable,
prior-dependent "properness" term (headline scoped to FITTED/congenial, paper intact) or a
qualification of the proper-MI claim is a DERIVATION question — needs Marcus + the cross-model
derivation protocol (GPT-5.5 xhigh). **Phase 1 is paused on this decision.**

**Spike 0b (brms) — RAN (2026-07-01).** brms `bf(X1|mi())+…+set_rescor(TRUE)` (joint 4-var
Gaussian imputer, cmdstanr/cmdstan 2.37.0 backend) fits and returns posterior-predictive
completions (G0b-1 PASS; sample tr(RIV) within tolerance, G0b-2 PASS).
- **Runtime gate: ~108s per fit (compile+sample).** Verdict: **cross-check / non-normal-only, NOT
  a workhorse** — a full R=1000 sweep would be hundreds of hours. Fine for focused cells / the
  Phase-3 non-normal illustration.
- **Deviance-bias branch: (T_brms − FITTED)/tr(RIV) = −1.36 (se 0.15, 6 fits).** brms lands on the
  **exact-DA (negative) branch**, MORE negative than the Jeffreys IW (−0.75) — even though its
  prior is weakly-informative (LKJ + half-t), NOT Jeffreys. This answers the prior question: the
  divergence is **general to full-Bayes posterior-draw imputation** (any genuine Bayesian Σ
  posterior), with a **prior-dependent magnitude** (Jeffreys −0.75, brms weakly-informative −1.36);
  it is NOT a Jeffreys-improper-prior artifact. Only the bootstrap (Amelia) and the explicit
  MLE-centered Gaussian (the paper's Laplace construction) sit at ≈0.

- **2026-07-03, open promotion debt (not yet done).** Marcus: results that end up cited in the
  manuscript must eventually be folded into the canonical `run_all.R` pipeline, not left as
  one-off scripts. Status as of the G8 landing: the main-grid BIC computation itself is already
  safe (added directly inside `verification/_modules/w3-sweep.R`, which `run_all.R` phase 2
  already sources -- it reproduces via the standard documented command with no extra work).
  Still owed before compile-enablement: (1) the AIC-vs-BIC headline summary (the table quoted in
  chat and in this file) currently exists only as a throwaway scratchpad script -- promote to a
  committed script (e.g. `verification/_modules/w3-bic-summary.R` or folded into `aggregate.R`
  phase 5) so `verdicts.md` carries a BIC verdict; (2) `verification/spikes/phase2-bic-smallN-probe.R`
  is not sourced by `run_all.R` and not documented in CLAUDE.md's Commands section -- either wire
  it in or add an explicit Commands entry; (3) no unit test in `00-test-primitives.R` covers the
  BIC arithmetic or the new `amelia-loglik` error-catch path.

- **2026-07-03, promotion decisions (before code).** Registering the exact scope of the fold-in
  before writing it:
  1. **BIC verdict in `aggregate.R` (phase 5).** A new `verdicts$BIC` entry, tagged
     `"observational (todo/040 Phase 2, not pre-registered)"` since BIC was never part of the
     original todo/005 hypothesis set. Computed from the same MAR + (FIML or congenial) subset
     `H2_MAR` already uses, reporting median `pi_bic_[uncorrected/corrected/oracle]` alongside
     the AIC equivalents, the BIC/AIC W3A yield ratio (quantifying "much smaller yield than
     AIC's"), and min `W3C_bic_high_RIV_frac` alongside AIC's min `W3C_high_RIV_frac`. The
     "model MB never selected" null check is explicitly NOT folded in here -- it needs the raw
     per-repetition `.rds` selection labels, not anything in `summary.csv`, and it was already
     reported as a one-off exploratory finding (0/120,000), not part of the G8 headline claim.
  2. **Refactor `w3-sweep.R` for testability (behavior-preserving, no numeric change).** Extract
     the AIC/BIC arithmetic (currently inlined in `run_one_w3`, excluding the frozen
     `chi2_SB`/scaled-shift arm, which stays untouched in place) into a pure function
     `w3_aic_bic_selections(ell_com, barL, trRIV_obs, npar, N)`; extract the Amelia
     M-averaged-log-lik loop into `w3_amelia_barL(imps, theta_obs_list, model_names)`. Both are
     unit-testable with synthetic inputs, no stochastic simulation needed. Because
     `run_w3_sweep()` (and `w3-rate.R`'s analogous H3b loop) `clusterExport()` only
     `run_one_w3`/`W3_MODEL_NAMES`/`TRUE_MODEL`/`Sigma_truth_w3` by name to parallel workers
     (rather than sourcing the whole file on each worker, unlike the small-N probe script), both
     `clusterExport` calls must add the two new helper names or the R=2000 production grid would
     silently fail on every worker. Verify byte-identical output on `run_all-smoke-bic` post-
     refactor (same seeds -> same results) before trusting any new production run.
  3. **`00-test-primitives.R` gets two new blocks.** BIC arithmetic: call
     `w3_aic_bic_selections()` directly with synthetic `ell_com`/`barL`/`trRIV_obs`/`npar`/`N`,
     check the BIC penalty is `npar*log(N)` (not `2*npar`), and that
     `BIC_corrected - BIC_uncorr == AIC_corrected - AIC_uncorr == trRIV_obs` elementwise (the
     "transfers verbatim" claim, exactly, not just in the aggregate). Amelia-loglik error-catch:
     confirm `w3_amelia_barL()` throws on a dimension-mismatched completed dataset, and that the
     same tryCatch-and-flag idiom used in `run_one_w3` resolves to the error path on that input.
  4. **`phase2-bic-smallN-probe.R` gets a CLAUDE.md Commands entry**, not a `run_all.R` phase-
     dispatch wire-in -- it is explicitly exploratory/non-pre-registered by its own header
     comment, matching the DA-engine spike precedent (documented, rerunnable, not part of the
     canonical phase list).

- **2026-07-03, promotion EXECUTED and verified.** All four items above implemented as
  registered. Verification, in order: (a) `Rscript verification/00-test-primitives.R` -- all
  smoke tests pass, including the two new blocks (BIC arithmetic: penalty/correction identities
  hold exactly; amelia-loglik: `w3_amelia_barL` matches a manual computation and throws on a
  dimension-mismatched imputation, resolving through the same tryCatch idiom `run_one_w3` uses).
  (b) Regression check: re-ran `Rscript verification/run_all.R 100 smoke-bic 2 20` (the exact
  command that produced the pre-refactor `run_all-smoke-bic` cache) and diffed the new
  `summary.csv` against a backup of the old one -- every column is byte-identical except
  `elapsed_sec` (confirmed with `all.equal()` after dropping that column); the parallel
  `clusterExport` fix (adding `w3_aic_bic_selections`/`w3_amelia_barL` to the varlist in both
  `w3-sweep.R` and `w3-rate.R`) was load-bearing -- without it the R=2000 production grid would
  have errored on every Amelia cell across all 20 workers. Reverted the regenerated
  `run_all-smoke-bic` cache back to its committed state afterward (timing-only diff, no
  informational value). (c) Called `run_aggregate()` directly against
  `w3_dir = run_all-prod-bic/phase2-w3` (has the BIC columns) with
  `w1_dir`/`rate_dir`/`bias_dir` from the base `run_all-prod` cache (AIC-side results unaffected
  by BIC, so reusing them is correct) to validate the new `verdicts$BIC` block end-to-end against
  real production data: median `pi_bic[uncorr/corr/oracle]` = 0.993/0.996/1.000 vs AIC's
  0.693/0.818/0.899; median `W3A_bic`/`W3A` yield ratio = 0.02; min `W3C_bic` = 1.000. Confirms
  the G8 narrative (BIC recovers almost regardless of correction at N>=200) quantitatively.
  Deleted the ad hoc `run_all-prod-bic/phase5/` output afterward -- it came from a mixed-directory
  call, not a standard `run_all.R` CLI invocation, so it is not itself a reproducible artifact;
  the BIC verdict will appear automatically in `verdicts.md` from any future full
  `Rscript verification/run_all.R <R> <out_suffix> all <n_cores>` run, no special-casing needed,
  since `w3-sweep.R` already always computes BIC selections and `aggregate.R` now always reports
  the verdict from whatever `w3_dir` it is pointed at.
