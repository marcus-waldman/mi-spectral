# Todo 005 — Pre-registered hypotheses for the comprehensive sweep

**Status:** Pre-registration draft. Predictions written *before* the sweep runs. When reality differs, the framing modifies, not the data. Once the user signs off this file is frozen and the sweep executes against it.

**Last updated:** 2026-05-23.

**Scope.** A comprehensive robustness sweep extending the preregistered W1/W2/W3 results (todo/004, frozen at SHA ddc9037) to assess generality of the bias-correction framework across:
- Sample size N
- Number of imputations M
- Missingness mechanism (MAR vs MNAR)
- Missingness pattern (non-monotone "swiss-cheese" vs monotone)
- Congeniality of the imputation model (Amelia `empri = 0` vs `empri = 0.5 N`)

**Primary witness for the sweep:** W3 (model-selection accuracy), the headline empirical claim. W1 (theorem) is run across the sweep cheaply as confirmation. W2 (LRT power) stays at the preregistered cell + 2 spot-check cells (one MNAR, one uncongenial).

**Why this sweep.** The preregistered W1/W2/W3 results land cleanly at one DGP cell (N=200, MAR, ~32% miss rate, M=200, congenial Amelia, non-monotone). A skeptic correctly asks: "does the headline (11pp recovery, 100% directional concordance) survive under different conditions, or is it specific to that cell?" This sweep answers that question across the dimensions most likely to matter for an MI methodology reviewer.

---

## 0. Shared infrastructure (new pieces relative to todo/004)

### 0.1 Missingness via `mice::ampute`

Replace the bespoke `apply_mar` for the sweep with `mice::ampute()` (Schouten, Lugtig, Vink 2018 — the canonical R reference for amputation). This:
- Standardizes the missingness generation across MCAR / MAR / MNAR and pattern types.
- Is what reviewers will recognize.
- Validates our results against an established package.

**Validation step (required before running the sweep):** smoke test confirming `mice::ampute` with MAR settings tuned to our `apply_mar` parameters (`a = -0.5`, `b = 0.4` proxy mechanism) produces statistically equivalent missingness rates and conditional patterns. Stored in `verification/00-test-ampute-vs-apply-mar.R`. Must pass before sweep execution.

### 0.2 Missingness rate

Held fixed at **40%** marginal missingness on the tested-partition variables (X_1, X_2), achieved via `mice::ampute(..., prop = 0.40)`. The X_3, X_4 nuisance partition stays fully observed.

(The existing `apply_mar` produced ~32% with the literal preregistered formula — see todo/004 §0.2 "Note on `~40% missing`". The new sweep moves to 40% as the round-number target via `mice::ampute`.)

### 0.3 Monotone vs non-monotone pattern

- **Non-monotone** (current preregistered): X_1 and X_2 missing independently; X_3, X_4 always observed.
- **Monotone**: variables ordered X_1, X_2, X_3, X_4 with monotone deletion — X_1 always observed; X_2 sometimes missing; if X_2 missing then X_3 missing; if X_3 missing then X_4 missing. Approximately 40% prevalence target (the marginal rate on the "deepest" variable X_4).

Implemented via `mice::ampute` with explicit pattern matrix `rbind(c(1,1,1,1), c(1,1,1,0), c(1,1,0,0), c(1,0,0,0))` and frequencies chosen to hit the 40% target.

### 0.4 MNAR mechanism

For MNAR cells: missingness depends on the *missing* variable itself:
$$P(R_j = 1 \mid X_j) = \Phi(\alpha_j + \beta_j X_j), \quad \beta_j > 0$$

Implemented via `mice::ampute(mech = "MNAR")` with weights matrix specifying that pattern-assignment is driven by each variable's own value. Strength tuned so MNAR is meaningfully different from MAR (specifically, the variables that drive missingness in MAR vs MNAN differ).

### 0.5 Uncongeniality via Amelia `empri`

- **Congenial** Amelia: `empri = 0` (default Wishart, no shrinkage; imputation model matches the analysis model's unrestricted MVN).
- **Uncongenial** Amelia: `empri = 0.5 * N` (strong ridge prior shrinks the imputation-model Σ substantially toward diagonal; this misspecifies the imputation model relative to the unrestricted analysis model).

FIML has no `empri` analog (it directly maximizes the analysis-model observed-data log-likelihood — congenial-by-construction). So FIML appears only in the congenial column.

### 0.6 Sweep design — 60 cells

| Factor | Levels |
|---|---|
| Pattern | non-monotone, monotone |
| Mechanism | MAR, MNAR |
| N | 200, 500, 1000 |
| M (Amelia only) | 20, 200 |
| Congeniality (Amelia only) | empri=0, empri=0.5*N |

- Amelia cells: 2 × 2 × 3 × 2 × 2 = **48 cells**.
- FIML cells (M-independent and cong-independent): 2 × 2 × 3 = **12 cells**.
- **Total: 60 cells**, each run at **R = 2000 replicates** (doubles MCSE precision over the preregistered prod's R=1000).

### 0.7 Per-replicate seed governance

Same as preregistered: `set.seed(20260522 + r)` inside each worker. Identical X^(r) across engine, M, mechanism, congeniality, pattern variants for the same r — isolates dimension effects from RNG drift.

---

## 1. Hypotheses

Predictions for each factor's main effect. Pre-registered for the W3 outcomes (the primary sweep target). Each prediction has a quantitative pass criterion and an "informative even if it fails" reporting commitment.

### H1: Pattern effect (monotone gives stronger W3 signal)

**Prediction.** Monotone missingness has more heterogeneous RIV eigenvalues across model parameters than non-monotone, producing larger differential bias across candidate models. Therefore the bias correction recovers MORE selection accuracy under monotone than non-monotone:

$$\Delta_{\text{W3-A}}^{\text{monotone}} > \Delta_{\text{W3-A}}^{\text{non-monotone}}$$

at the same (mech, N, M, cong) combination, where $\Delta_{\text{W3-A}}$ = corrected − uncorrected true-model selection rate.

**Pass criterion (H1):** at fixed mech=MAR, cong=congenial, the median W3-A across (N, M) cells is at least 5 pp larger under monotone than non-monotone.

**Fallback if it fails.** Monotone gives same or smaller W3-A. Inform: the RIV-heterogeneity-is-the-driver intuition is wrong for this design; report transparently and discuss why (likely the candidate models don't differ enough in RIV exposure under monotone for this 4-dim setup).

### H2: Mechanism effect (MAR holds, MNAR may break)

**Prediction.** Under MAR (proper-MI assumption satisfied), the bias correction's directional finding (W3-C ≈ 1.00) and W3-A recovery hold at every (pattern, N, M, cong=congenial) cell. Under MNAR, the proper-MI assumption is violated and the imputation is no longer unbiased; the bias correction was derived under MAR and is not guaranteed under MNAR. We expect partial-to-substantial breakdown of the directional concordance and reduced recovery.

**Pass criterion (H2-MAR):** at all MAR + congenial cells, W3-C ≥ 0.80 (high-RIV misclassification fraction) AND W3-A ≥ 0.05.

**Pass criterion (H2-MNAR):** *transparent observational report only* — no required pass. We report W3-A and W3-C at every MNAR cell, document the breakdown pattern if it occurs, and acknowledge in the manuscript that "the framework's empirical guarantees are tied to the MAR assumption; MNAR is reported as a stress test."

**Fallback if MAR fails at some cell.** Means the bias correction doesn't survive that condition. Diagnose: is it a small-N convergence issue, a specific pattern interaction, or a deeper framework limitation? Report transparently in the manuscript with the implicated cells.

**Fallback if MNAR doesn't break.** Means the bias correction is more robust than the derivation requires — surprising but welcome. Report as evidence that the framework may extend beyond its derivation's stated scope.

### H3: Sample size N

**Prediction.** Directional finding (W3-C) is N-independent; the recovery magnitude (W3-A) has weak N-dependence; the gap to oracle (W3-B) SHRINKS with N (finite-N effect documented at preregistered cell).

**Pass criterion (H3):** at all MAR + congenial cells, W3-B at N=1000 < W3-B at N=200 (gap to oracle shrinks with N). W3-C ≥ 0.80 at all N.

**Fallback.** If W3-B doesn't shrink with N, the corrected rule's gap to oracle is not a finite-N artifact but a structural limitation. Report.

### H4: Imputation count M

**Prediction.** At M=20, Chan SMI's `r_hat` is noisier, slightly degrading the bias correction's signal. The recovery (W3-A) at M=20 is similar to but slightly worse than at M=200. The directional finding (W3-C) is robust across M.

**Pass criterion (H4):** at all MAR + congenial cells, W3-A at M=200 ≥ W3-A at M=20 − 0.02 (within tolerance; bias correction doesn't catastrophically degrade at applied-default M=20).

**Fallback.** If W3-A at M=20 is substantially worse than at M=200, document the M-sensitivity and recommend M=200 as a practical guideline.

### H5: Congeniality

**Prediction (most consequential of the sweep).** Under congenial Amelia (`empri=0`), the bias correction works as in the preregistered prod (W3-A passes, W3-C ≈ 1.00). Under uncongenial Amelia (`empri=0.5*N`), the imputation systematically shrinks the cross-block correlations toward zero — exactly the parameters M_C estimates. We expect:
- M_C's fit is artificially worsened.
- M_A (diagonal) becomes artificially competitive.
- Uncorrected MI-AIC may no longer over-select M_D; may instead under-select M_C.
- The bias correction cannot undo what the imputation has broken — it was derived for proper MI.

**Pass criterion (H5):** congenial cells pass W3-A and W3-C as in the preregistered prod. Uncongenial cells are observational — we expect W3-A to drop (potentially below preregistered thresholds) and W3-C to drop below the 100% concordance of the congenial case.

**Reporting commitment.** The uncongenial cells are *transparent stress-test evidence* of where the framework's safety margin ends. The paper's §6 (Discussion) acknowledges this is the practical limit and recommends diagnosing congeniality before trusting bias-corrected selection.

### H6: Cross-cutting — engine independence

**Prediction.** At matched cells (same N, mech, pattern, M=200 for both engines), FIML and Amelia-congenial agree on W3 outcomes to within ~3 pp (MCSE-bounded at R=2000).

**Pass criterion (H6):** at every (pattern, mech, N) combination, |W3-A_FIML − W3-A_Amelia_cong| ≤ 0.03.

**Fallback.** If engines disagree by more than MCSE at some cell, diagnose whether the disagreement is implementation-specific (engine bug) or a real effect of MI MC noise. Report.

---

## 2. Pass / fail outcomes

The sweep is **declared a success** if H1, H2-MAR, H3, H4, H6 all pass (≥ 4 of 5 quantitative criteria). H5 is observational regardless. H2-MNAR is observational regardless.

The sweep is **partially informative** if 2-3 of the quantitative criteria pass. We report what passed, what didn't, and discuss why.

The sweep is a **framework warning** if fewer than 2 pass. We retreat from the broad-applicability claims and restrict the paper's empirical scope to the preregistered cell.

---

## 3. Out-of-scope clarifications

- **Dimension p** stays at 4. The redesign of candidate models for p=8 is not pursued in this sweep.
- **Missingness rate** stays at 40% (one level). Sensitivity to rate is not assessed in this sweep.
- **W2 sweep** is not pursued; W2 stays at the preregistered cell (1 cell), with 2 spot-check cells added (one MNAR, one uncongenial) for transparent comparison.
- **Real-data demonstration** is deferred; the simulation evidence from this sweep is the empirical case.
- **Non-MVN DGP** is deferred to a follow-up paper.

---

## 4. Sign-off

By signing off on this document, the user (marcus.waldman) commits to the predictions in §1 as the pre-registered hypotheses for the comprehensive sweep. After sign-off:

- The sweep code is implemented per todo/006 (the operational execution checklist).
- Production runs execute against this document.
- Results are reported against the predicted values as written here. Discrepancies are described, not papered over.
- If any pass criterion fails, the response is constrained to the options in the relevant Fallback paragraph.

**Sign-off:** [PENDING — awaiting user review before sweep execution]

**Version history:**
- 2026-05-23 — Initial draft (Claude Opus 4.7). Awaiting user review.
