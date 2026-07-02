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

- *(pending Phase 1)* DA replication engine + cells — amendment to be recorded when the Phase-1
  engine and cell list are locked, before the production run.
- *(pending Phase 2)* MI-BIC block — amendment to record the complete-data-n penalty choice and
  whether the phase2 cache is re-aggregated or a focused rerun is needed (depends on whether the
  cell RDS stored raw per-repetition `ell_com/barL/npar/trRIV` or only selection labels — CHECK
  before running).

---

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
