# Proposal under defense — Section 5 (Simulation studies) of *mi-spectral*

## The proposition

**Every claim Section 5 draws from the simulation data is earned by that data, and no claim overreaches what the numbers support.** Each figure or table demonstrates the specific statistical mechanism it is asserted to demonstrate; each headline number reproduces from its committed data artifact; each pre-registered prediction that was not met is reported as a failure in the main text rather than smoothed over.

This is the proposition the defender argues under oath. The examiners test whether it holds, claim by claim, against the data inlined in the appendix below.

## What this section is

*mi-spectral* is a theory paper. Its core result is a deviance-bias correction for the averaged log-likelihood (the "Q-function") under congenial multiple imputation, with two applications: a likelihood-ratio model comparison and information-criterion model selection. Section 5 is the paper's complete empirical account. Every quantitative claim elsewhere in the paper points here.

The candidate-model families, missingness mechanisms, estimands, and pass criteria were fixed before each study's code was written (pre-registration documents `todo/004`, `todo/027`, `todo/029`, with dated amendment histories). Two reporting rules hold throughout: failed predictions appear in the main text beside the successes, and quantitative claims are stated for totals and paired differentials rather than for individual components.

Key terms used below:
- **tr(RIV)** — trace of the relative increase in variance from missing data; the larger it is, the more information is missing. It is the size of the deviance bias the paper corrects.
- **Deterministic / analytic arm** — the Q-function evaluated in closed form at the observed-data MLE, free of Monte Carlo error.
- **Proper arm** — imputations drawn by expectation-maximization with bootstrapping (Amelia).
- **Oracle** — the complete-data reference an analyst would use if nothing were missing. "Perfect" for each study.

---

## The claim inventory (verbatim from the manuscript)

Each block is the exact prose the manuscript commits, followed by the data artifact it cites.

### Study 1 — Theorem validation (S5-P12)
> The net deviance bias tracks the analytic half-trace across every sample size, and the inverse-variance pooled estimate confirms the completed theorem at **2.43 ± 0.26** against the order-one-augmented prediction **2.42 to 2.55**. One cell is a genuine miss. At N = 1000 the estimate falls **2.6 standard errors below** the preregistered target, a consequence of the heavy-tailed per-repetition statistic, whose standard deviation grows with the sample size and leaves the larger cells unable to resolve an order-one offset at fixed repetition count. The component terms separately miss their targets by roughly **9 to 20 percent**, which is why the grading reports only totals and paired differentials.

Design (S5-P4): four-variate normal, correlations 0.6/0.3/0.5 on three pairs, tr(RIV) ≈ 5.55. Non-monotone MAR ~1/3 per coordinate. N ∈ {200, 500, 1000, 2000}, R = 1000, analytic arm. **The pre-registered target was one half the trace, near 2.77, refined during analysis to the band 2.42–2.55 once the missing-at-random term was derived.** Backing: `verification/cache/W1-prod-fiml.rds`.

### Study 2 — Known scale and sign regime (S5-P13)
> The deterministic arm returns **0.025 ± 0.018** against a target of zero and the proper arm returns **−0.536 ± 0.018** against −½tr(RIV) = **−0.561**, both within Monte Carlo error and differing by exactly the posterior-draw imputation variance. Imputing from the true model rather than the fitted model reverses the sign of the total, as the fitted-versus-oracle distinction requires.

Design (S5-P5): four-variate normal, N = 200, R = 2×10⁵. Backing: `rederivation-knownvar-N200-R200000.rds`.

### Study 3 — Likelihood-ratio absorption / Type I error (S5-P14)
> The uncorrected numerator rejects at **0.042** and the additionally corrected numerator at **0.034**, both near the nominal 0.05 and the corrected one slightly conservative as double-counting predicts. ... One scope note travels with this study. Its committed correction arm used the naive trace difference, which differs from the projected-trace formula by about **5 percent** in this near-invariance design and is immaterial here.

Design (S5-P6): H₀: σ₁₂ = 0 in the four-variate normal, N = 200, M = 200, R = 1000. Backing: `W2-prod-amelia.rds`.

### Study 4 — Discrimination of the two formulas (S5-P15)
> The observed differential is **2.64 ± 0.11** at N = 500 and **2.70 ± 0.11** at N = 1000, on the projected-trace prediction of **2.64** and **52 standard errors** from the naive trace difference. The naive difference always overstates the correct value, and this design makes the gap large enough to rule it out outright.

Design (S5-P7): H₀: μ₁ = 0, coordinate 1 heavily missing (~70–79%), one tested direction. Naive prediction ≈ 8.5. Backing: `w2-paired-differential-mu1-cell.rds`.

### Study 5 — Pairing (S5-P16)
> At the null the paired-differential standard deviation stays near **1.5** across N = 500, 1000, and 2000, while the single-model figure grows from **18.4 to 36.5**. At a fixed alternative the square-root-of-n growth returns, to **12.4, 16.8, and 24.9**, exactly the failure mode the result specifies.

Backing: `w2-paired-differential-spotcheck.rds`.

### Study 6 — Selection sweep (S5-P17)
> At N = 500 on the deterministic arm the oracle selects the true model at **0.90**, the uncorrected criterion at **0.67**, and the corrected criterion at **0.82**. In every congenial cell, **all of the uncorrected criterion's errors land on the saturated, largest-missing-information candidate.** The recovery is substantial and visibly short of the oracle.

Design (S5-P9): four nested MVN covariance models (diagonal → saturated), truth = compound symmetry. 60 cells. ~40% missing, R = 2000. Backing: `run_all-prod/phase2-w3/summary.csv`.

### Study 7 — Distribution-matching ladder (S5-P18, P19, P20)
> At correlation 0.40 the two-moment and equating arms reach **0.904 and 0.903** against the oracle's **0.899**, statistically indistinguishable, and the junk cell closes **90 percent** of the uncorrected-to-oracle gap. In the weak-signal cell the oracle itself drops to **0.820** and no arm passes **0.650**, because the stronger arms' null-side gains are offset by underfit retention. That residual is information loss rather than calibration error.

Selection-rate table (S5-P18):

| Cell | oracle | uncorrected | mean | two-moment | equating |
|---|---|---|---|---|---|
| ρ = 0.40 | 0.899 | 0.678 | 0.814 | 0.904 | 0.903 |
| ρ = 0.10 | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 |
| ρ = 0 (junk) | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 |

Internals (S5-P19):
> On the true model's anchored statistic the distance to the paired complete-data statistic falls from **0.281** under the uncorrected deviance to **0.019** under equating, and the variance ratio falls from **3.18** to near one. ... the noncentral statistic shrinks by the predicted factors, about **0.57** under the two-moment match and **0.40** under equating. The internal validity checks held on every repetition, with the spectrum-trace identity to **3×10⁻¹⁵** and no failure of the reference inversion in **18,000** evaluations.

Structural limits (S5-P20):

| Structural limit | perfect | achieved |
|---|---|---|
| block-diagonal family, naive vs projected trace | exact equality | agree to **3.6×10⁻¹⁵** |
| off-equality moment map, main-cell rate | oracle 0.899 | naive input **0.824**, correct input **0.904** |
| per-model map, equated difference mean and sd | complete-data 10.00 and 7.10 | **6.10 and 5.99** |

> The naive trace difference is exact only on the block-diagonal case and overstates the projected trace elsewhere, and a per-model marginal map cannot calibrate the joint difference distribution.

Backing: `verification/cache/ic-ladder-summary.csv`.

### Study 8 — Non-nested measurement (S5-P21)
> Each candidate's order-one level is large under missing-at-random data, near **+2.6 and +2.9** deviance units for the two candidates, and it collapses under the completely-at-random twin. For the dissimilar diagonal-versus-autoregressive pair the isolated differential resolves at **−1.2**, three and a half standard errors from zero and stable across sample sizes. For the similar compound-symmetry-versus-autoregressive pair the differential sits below Monte Carlo resolution, and **a pilot's apparent value of −2 dissolved in the full run. We report that failure as the discipline requires.** A byproduct supplied the first measured case off the equality condition, where the naive trace difference overstates the exact projected trace by about **9 percent**.

Design (S5-P11): truth = four-variate AR(1) at ρ = 0.5. Similar pair (CS vs AR(1)) and dissimilar pair (diagonal vs AR(1)). N ∈ {500, 1000, 2000}, R = 20,000, each paired with an MCAR twin. Backing: `w4-nonnested-summary.csv`, `w4-dissimilar-summary.csv`.

### Study 9 — Engine sensitivity (S5-P22)
> On non-monotone missing-at-random cells with samples as small as N = 200 ... the sample relative-increase-in-variance trace from the imputation draws matches the observed-data value within **2 to 3 percent**, with no widening as the sample grows, and selection agrees between the analytic arm and the imputation arm within **0.011** on the recovery gap.

Caveat (verbatim): the bootstrap sampler is only approximately Bayesian, data augmentation was not run, and a fully Bayesian sampler remains the conservative choice when the fraction of missing information is large.

---

## Data appendix — the actual numbers behind the figures

The panel can verify the headline claims against the committed CSVs. The relevant rows and columns are transcribed verbatim below.

### A. Selection sweep — `run_all-prod/phase2-w3/summary.csv` (selected columns)

Columns: cell · oracle · uncorrected · corrected · W3C_high_RIV_frac (fraction of misclassifications landing on the saturated/highest-RIV candidate) · W3C_n_miscl (count of misclassifications) · W3B_oracle_minus_corr.

**Congenial, non-monotone MAR (the headline family):**
```
fiml  N200             oracle 0.9065  uncorr 0.6505  corr 0.806   W3C_frac 1.000  n_miscl 699  oracle-corr +0.1005
fiml  N500             oracle 0.898   uncorr 0.674   corr 0.816   W3C_frac 1.000  n_miscl 652  oracle-corr +0.082
fiml  N1000            oracle 0.899   uncorr 0.665   corr 0.810   W3C_frac 1.000  n_miscl 670  oracle-corr +0.089
amelia N500 M200 cong  oracle 0.898   uncorr 0.6685  corr 0.816   W3C_frac 1.000  n_miscl 663  oracle-corr +0.082
```

**Uncongenial, non-monotone MAR (note the contrast):**
```
amelia N200 M20  uncong  oracle 0.9065  uncorr 0.9315  corr 0.981  W3C_frac 1.000  n_miscl 137  oracle-corr -0.0745
amelia N500 M200 uncong  oracle 0.898   uncorr 0.9355  corr 0.979  W3C_frac 1.000  n_miscl 129  oracle-corr -0.081
amelia N1000 M200 uncong oracle 0.899   uncorr 0.926   corr 0.978  W3C_frac 1.000  n_miscl 148  oracle-corr -0.079
```

Observation for cross-examination: `W3C_high_RIV_frac = 1.000` in **every** cell of the 60-cell sweep, congenial and uncongenial alike. In the uncongenial cells the misclassification *count* collapses (≈130 vs ≈660), the uncorrected rate *exceeds* the oracle, and `oracle_minus_corr` goes **negative** (the correction overshoots past the oracle). The manuscript reports the "100% land on saturated" signature only for congenial cells.

### B. Distribution-matching ladder — `ic-ladder-summary.csv` (selected columns)

```
Cell  rho  oracle  r0(uncorr)  r1(mean)  r2(two-moment)  r3(equating)  frozenSB
MAIN  0.40 0.899   0.678       0.8135    0.9045          0.903         0.824
WEAK  0.10 0.8195  0.582       0.650     0.6485          0.650         0.658
JUNK  0.00 0.7265  0.4225      0.5845    0.7015          0.6955        0.5955

Internals (MAIN cell):
  ks0_MC 0.2805 -> ks3_MC 0.0185   (uncorrected -> equating null-side KS distance)
  varratio0_MC 3.178 -> varratio3_MC 0.973
  ncratio2_MA (two-moment) 1.0021 ... ncratio2_MA 0.3617 ... [index/label mapping is the defender's to confirm]
  trperp_MC_mean 2.852 vs trnaive_MC_mean 2.852  (block-diagonal equality: agree to ~3.6e-15)

Off-equality (WEAK cell):
  p8_mean_dMI 6.097   p8_sd_dMI 5.988   vs  p8_mean_dcom 10.003  p8_sd_dcom 7.105
  frozenSB(naive input) 0.824 [MAIN]  vs two-moment(correct input) 0.9045 [MAIN]
```

### C. Non-nested measurement — `w4-nonnested-summary.csv` (similar pair, CS vs AR(1)) and `w4-dissimilar-summary.csv` (diagonal vs AR(1))

```
SIMILAR pair (w4-nonnested), resid = MAR paired residual; Aprime = MCAR twin:
  A   MAR  N500  resid -0.521   N1000 resid -0.322   N2000 resid -0.096   (sd_Dpair ~30-65, se ~0.21-0.45)
  Aprime MCAR N500 resid -0.243  N1000 resid 0.271   N2000 resid -0.052
  Isolated differential (MAR - MCAR twin): -0.278, -0.593, -0.044  -> below resolution. Pilot's -2 did not survive.

DISSIMILAR pair (w4-dissimilar):
  A   MAR  N500  resid -0.233 (se 0.255)   lvl_diag +2.618   lvl_ar +2.851
  Aprime MCAR N500 resid +0.964 (se 0.228)
  Isolated differential = -0.233 - 0.964 = -1.197  ;  se = sqrt(0.255^2 + 0.228^2) = 0.342  ->  -3.5 se from zero.
  Stable across N (N1000, N2000 reproduce a similar isolated value).
  Levels +2.6 / +2.9 under MAR collapse toward 0 under the MCAR twin (lvl_ar 2.85 -> 0.43 -> 0.14 -> 0.04 across the MCAR rows).
  trperp_diag vs trnaive_diag: 6.91 vs 6.91 here, but on the AR candidate trperp 7.95 vs trnaive 8.74 -> ~9% naive overstatement.
```

---

## How to read the verdict

The proposition is a conjunction over nine studies. A single overreaching claim or a single irreproducible headline number is enough to move the verdict off "accept." The defender should concede such cases and propose the minimal rewrite that makes the claim match the data, rather than defend the prose as written. The output the human owner wants is: which claims are earned, which need softening, and whether any figure is demonstrating an artifact rather than the mechanism it names.
