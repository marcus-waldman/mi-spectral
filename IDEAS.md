# IDEAS.md

Directional anchor for drafting the JAIGP paper. Captures the load-bearing reasoning from the 2026-05-22 working session. **Reframed mid-session** after reading Chan (2022, *Annals of Statistics*) "General and feasible tests with multiply-imputed datasets"; see the *Reframing note* below and the archived material at the bottom for the original spectral-correction conception.

---

## Reframing note (2026-05-22)

The original conception of this paper centered on a finite-$M$ scaled-shifted chi-square correction using the full eigenvalue spectrum of $\text{RIV}_\perp$ — i.e., dropping the EFMI assumption that Chan & Meng (2022, *Statistica Sinica*) retained. Mid-session we acquired and read Chan (2022, *Annals of Statistics*), which presents a "stacked multiple imputation" (SMI) test that **already drops EFMI**, estimates the full OMI eigenvalue spectrum $r_{1:k}$ individually via a stacking-and-moment-inversion construction, and uses the exact limiting distribution $\mathbb{D}$ via Monte Carlo (no $\chi^2$ or $F$ approximation). Chan's §A.3 explicitly considers two-moment-projection approximations (which is what our scaled-shifted form was) and demonstrates they perform worse than his MC approach for size control.

That preempts the original C2/C3 headline. **The paper is reframed around the deviance-bias decomposition (originally Claim 1)**, with two downstream applications — likelihood-ratio testing and information criteria. Chan-Meng (2022) and Chan (2022) become *consumers* of our bias-corrected deviance, not competitors: they handle test calibration; we handle numerator centering. Both are necessary to recover complete-data inferential properties under MI.

---

## Motivation and venue choice

**Why JAIGP, not a traditional methodology journal.** The technical derivation was developed in collaboration with Claude (Anthropic, Opus 4.7). The human prompter declined to submit derivation-heavy theory to *Psychological Methods* or *Structural Equation Modeling* under standard sole-authorship norms, on the grounds that the math came from AI dialogue rather than independent human work. JAIGP — peer-reviewed, ORCID-verified human prompters, transparent AI co-authorship as the explicit norm (founded by César A. Hidalgo at Toulouse School of Economics, in collaboration with Anthropic) — fits the ethical posture.

**Tradeoff accepted.** JAIGP is new (peer review pipeline launched March 2026), not yet indexed (no DOI, Scopus, or Web of Science as of mid-2026). The trade is real: a more prestigious venue would carry more weight with traditional methodology reviewers. The trade is accepted because:

- The derivation can be validated empirically — the seven-claims-three-witnesses apparatus (now reduced to three witnesses W1/W2/W3) gives readers independent evidence of each load-bearing claim without requiring them to invest in proof verification first.
- The companion SEM methodology paper at MI-IC will cite this one for the derivation and stand on its independent empirical contributions (`miicsem` package, simulation results, congeniality empirics) — those *are* the human prompter's independent work.
- Mitigation: deposit on Zenodo in parallel for a stable DOI; cite the Zenodo DOI from the SEM paper to handle JAIGP's indexing-status concern at the receiving venue.

---

## Headline contribution (reframed; empirically validated 2026-05-23)

**The Q-function deviance bias under congenial MI decomposes as $+\tfrac{1}{2}\text{tr}(\text{RIV}) = +\text{tr}(\text{RIV}) - \tfrac{1}{2}\text{tr}(\text{RIV})$**, where the $+\text{tr}$ term is imputation bias (analogous to Cavanaugh-Shumway's AICcd penalty if the target were $\hat\theta_{\text{obs}}$) and the $-\tfrac{1}{2}\text{tr}$ term is estimation mismatch from MI's target being $\hat\theta_{\text{com}}$ rather than $\hat\theta_{\text{obs}}$.

This bias is a fundamental quantity. Any inferential tool that consumes the MI Q-function — likelihood-ratio statistics, AIC, BIC, profile likelihoods, deviance-based fit indices — silently inherits it. The paper's job is (i) to formalize the bias and its decomposition, and (ii) to demonstrate that correcting it changes downstream answers in operationally important ways.

**Empirical status (preregistered N=200, M=200, R=1000, two engines):** the total bias prediction holds within MCSE; bias correction yields modest but consistent size-adjusted power gain in MI LRT and recovers ~11pp of true-model selection accuracy in MI-AIC. **Most striking finding:** 100% of uncorrected MI-AIC misclassifications land on the highest-RIV candidate model — perfect directional confirmation of the v4.5 derivation's predicted mechanism (the strongest possible empirical signature, hard for a skeptic to dismiss as noise). See "Verification suite" below for the full witness landings.

---

## Positioning in the literature

This work sits in a tradition of refining MI-based likelihood inference. After the reframe, the lineage is best read as **upstream of test-calibration work**:

- **Rubin (1987)** — establishes MI, RIV, and the variance-pooling framework
- **Cavanaugh & Shumway (1998)** — AICcd: deviance bias under EM-based observed-data MLE, penalty $+2\text{tr}(\text{RIV})$. Parallel universe: different target estimator, same RIV machinery.
- **Meng (1994)** — defines congeniality
- **Meng & Rubin (1992)** — first combining rule for MI LRT, scalar $r_L$
- **Claeskens & Consentino (2008)** — variable selection / AIC under missing covariates, block-diagonal information
- **Chan & Meng (2022, Stat Sinica)** — stacked-data LRT, dropped non-negativity / invariance / power problems of $D_L$; retained EFMI
- **Chan (2022, AoS)** — general SMI framework, drops EFMI, full eigenvalue spectrum, exact MC reference distribution. Universal (Wald, LR, score). **Now the canonical reference for MI test calibration.**
- **This work** — deviance-bias decomposition. Applies to anything that consumes $\bar Q_\infty$.

Chan & Meng (2022) and Chan (2022) handle the calibration of the LRT statistic *given* its numerator. We handle the bias of that numerator. Together, the two literatures close the gap between MI inference and complete-data inference: Chan ensures the reference distribution is right; we ensure the statistic being referred to it is centered.

---

## Applications

The bias correction is necessary wherever the complete-data deviance is consumed. The paper focuses on **two** applications.

### Application 1: Likelihood-ratio tests and model comparison

The MI LRT numerator is $\hat d_L = 2[\bar Q_\infty(\hat\psi^*) - \bar Q_\infty(\hat\psi_0^*)]$. Under our bias decomposition, this has expected value

$$\mathbb{E}[\hat d_L] - [2\ell_{\text{com}}(\hat\psi^*) - 2\ell_{\text{com}}(\hat\psi_0^*)] \;=\; \text{tr}(\text{RIV}(\hat\psi^*)) - \text{tr}(\text{RIV}(\hat\psi_0^*))$$

Key observations:

- **Under $H_0$**, $\hat\psi^* \approx \hat\psi_0^*$ asymptotically, the two RIVs converge, the differential bias vanishes. So Chan's null calibration is unaffected by ignoring our bias.
- **Under local alternatives and away from $H_0$**, the bias is non-zero and distorts the LRT statistic's distribution. This affects power, non-centrality structure, and confidence regions inverted from MI LRTs.
- **In non-nested model comparison** (Vuong-style tests), there is no canonical null, the bias is non-vanishing across the comparison, and it distorts model ranking.

**Empirical landing (W2, preregistered M=200, R=1000):** at the preregistered Amelia + Chan-AoS-MC configuration, the bias correction yields a *consistent* size-adjusted power gain over uncorrected at every $\delta$ in the local-alternative grid (margins 0.5–3 pp). Type I calibration at $M = 200$ is reasonable for *all three* MI tests (within ~1 pp of nominal); the bias correction's value at preregistered M is in size-adjusted power, not raw calibration. At smaller M (M=50 pilot), the bias correction is more essential for Type I — uncorrected over-rejects at 0.07 while corrected lands at 0.04.

**Three-way practitioner menu (§4 framing):** at M=200, the three MI tests offer different tradeoffs and we present them as a menu rather than ranking one strictly best:

| Test | Type I at α=0.05 | Size-adjusted power | What it offers |
|---|---|---|---|
| Bias-corrected + Chan MC (C2) | 0.034 (conservative) | best (highest at every δ) | best inference quality with size adjustment |
| Uncorrected + Chan MC (C3) | 0.042 (near-nominal) | middle | default Chan procedure; small Type I inflation |
| Satorra-Bentler on differential (C5) | 0.045 (nominal) | lowest (~3-5 pp behind C2) | closed-form, no MC needed, immediately nominal |

### Application 2: Information criteria

AIC and BIC under MI take the form $-2\bar Q_\infty + \text{penalty}$. Each candidate model has its own RIV matrix (because RIV depends on which parameters are in the model), so the bias $-\text{tr}(\text{RIV})$ in $-2\bar Q_\infty$ is **model-specific**. Ignoring it systematically distorts model rankings — uncorrected MI-AIC/MI-BIC preferentially favor models with **larger** RIV: the downward bias of $-2\bar Q_\infty$ scales with $\text{tr}(\text{RIV})$, making high-RIV candidates look artificially better than they would under complete data. This is the same direction as Cavanaugh-Shumway's AICcd correction (penalty $2q + 2\text{tr}(\text{RIV})$, additionally penalizing high-RIV models); bias correction here restores complete-data-equivalent model selection.

This is the application with the highest empirical stakes. Cavanaugh-Shumway's AICcd penalty addresses a different point in the pipeline (observed-data target); our correction is for MI-AIC's complete-data target. Both can coexist.

**Empirical landing (W3, preregistered N=200, M=200, R=1000) — the headline result of the paper:** bias correction recovers **+11 pp** of true-model selection accuracy lost to MI (oracle 0.912 → uncorrected 0.716 → corrected 0.829). The directional prediction holds in the strongest possible form: **100% of the uncorrected rule's 284 misclassifications land on $M_D$**, the largest-RIV candidate. Zero land on the lowest-RIV candidate. Both FIML and Amelia engines confirm to within MCSE. **Satorra-Bentler on differential deviance vs the saturated model adds another ~0.6 pp** for free.

The 100% directional concordance across 1000 replicates is the photogenic finding — the kind of empirical signature a skeptic cannot dismiss as noise.

---

## Running example

Same as before: $X \sim \mathcal{N}_p(\mu, \Sigma)$, both unknown, structured missingness, joint MVN imputation (Schafer 1997 / NORM). Same MVN setting threads through W1, W2, W3 so the reader builds intuition across applications.

**Why this and not MVN-mean with known $\Sigma$**: same reasons as before (joint MVN is the imputation engine people actually use; anisotropic RIV arises naturally; tested-vs-nuisance structure; recognizable textbook setting). The "anisotropy" of RIV is no longer the load-bearing claim, but it's still the setting that makes the bias correction's model-dependent magnitude evident in W3.

---

## Verification suite (witnesses) — three witnesses, all empirically complete

**Principle.** Every load-bearing equation gets a numerical witness — a pre-registered prediction, simulation result, and prose alongside the math. Because the derivation is AI-assisted, the reader is afforded additional evidence of validity of each load-bearing claim, independent of the proof.

**Outcomes at preregistered config (N=200, M=200, R=1000, both engines).** All three witnesses passed their headline criterion; W1 and W3 had partial pass/miss on auxiliary criteria with honest documentation of what passed and what didn't.

| # | Claim | Empirical outcome | §  |
|---|---|---|---|
| W1 | Q-function bias decomposes as $+\tfrac{1}{2}\text{tr}(\text{RIV})$ | **Total bias passes** within MCSE under both engines. Individual terms (Term 1 = +tr, Term 2 = −½tr) have correlated finite-N residuals (~10–20%) that cancel in the sum. Reported honestly. | §3 |
| W2 | Bias-corrected MI LRT has higher power than uncorrected at local alternatives | **PASS at preregistered M=200**: C2 > C3 in size-adjusted power at every δ, margins 0.5–3 pp consistent across the 8-δ grid. M=50 pilot showed the gap as MCSE-bounded (noise dominated signal); preregistered M was needed. SB closed-form alternative competitive at small M. | §4 |
| W3 | Uncorrected MI-AIC has lower true-model selection rate, with misclassifications going to high-RIV candidates | **W3-A (≥10pp gap):** PASS (corrected − uncorrected = +11.3 pp FIML, +10.6 pp Amelia). **W3-B (≤5pp from oracle):** miss (corrected ~8 pp behind oracle). **W3-C (≥60% misclass → high-RIV):** PASS PERFECTLY (1.000 — every single uncorrected misclassification lands on $M_D$). | §5 |

**Layout (built and complete):**

```
verification/
├── 00-setup.R                  # shared simulation primitives (MVN data gen, MI, fits, Chan SMI, custom Cholesky)
├── 00-test-primitives.R        # smoke tests
├── W1-bias-decomposition.R     # theorem validation
├── W2-lrt-power.R              # LRT power under local alternatives
├── W2-size-adjusted-power.R    # post-hoc size-adjusted power analysis
├── W3-model-selection.R        # MI-AIC/BIC selection (oracle / corrected / uncorrected / SB)
└── cache/                      # RDS outputs read by manuscript
```

**Verification-theater mitigation worked as designed.** Two notable preregistration-discipline saves:

1. **W2 reversal-of-reversal.** Pilot at M=50 R=200 looked like "powers tied at equal Type I" — initial reframe to "calibration not power." Preregistration kept us honest enough to run M=200 production; at preregistered M the original prediction (C2 > C3) was validated. The pilot's null finding was an MCSE artifact of low M, not the truth. Without the preregistration commitment we might have settled on the wrong framing.
2. **W1 finite-N residual.** Production at R=1000 exposed correlated finite-N residuals in the Term 1 / Term 2 decomposition individually (each ~10-20% off) that cancel in the total. Honest reporting of this in §3 strengthens rather than weakens the paper — readers see we know what we're claiming and what we aren't.

---

## Comprehensive sweep results (2026-05-23)

Pre-registered at `todo/005-comprehensive-sweep-hypotheses.md` (signed off 2026-05-23) and executed via the centralized `verification/run_all.R` entrypoint. Full grid:
- **Phase 0** — smoke tests (`apply_missingness_ampute` vs `apply_mar`) + analytic pre-flight `tr(RIV)` table (12 cells × 50 seeds).
- **Phase 1** — W1 theorem-validation sweep, FIML analytic, 18 cells (2 patterns × 3 mechanisms × 3 N), R=2000 each.
- **Phase 2** — W3 main sweep, 60 cells (2 patterns × 2 mechanisms × 3 N × 5 engine/M/cong combos), R=2000 each.
- **Phase 3** — H3b rate side experiment, 3 cells (low-rate arm only; rate=60% deferred for Amelia stability reasons documented in todo/005), R=2000 each.
- **Phase 4** — MNAR parameter-bias measurement, 18 cells (2 patterns × 3 mechanisms × 3 N), R=2000 each. *New phase added 2026-05-23 to directly quantify `E[theta_obs - theta_truth]` and answer the "did MNAR introduce material parameter bias?" question.*
- **Phase 5** — aggregation + hypothesis verdicts → `verdicts.md` + `combined.csv`.

~3 hours of compute on a 20-core PSOCK cluster, zero per-replicate errors across the entire run. Single-command reproducibility: `Rscript verification/run_all.R 2000 prod all 20`.

**The strongest finding (and it is genuinely strong):** W3-C — the directional concordance of uncorrected MI-AIC's misclassifications onto the highest-RIV candidate — was **1.000 across every single cell of the 60-cell main sweep, the 3-cell rate experiment, and every congeniality and engine variant**. Every misclassification under uncorrected MI-AIC landed on M_D, the maximum-RIV candidate. Across 63 cells × ~few-hundred-per-cell misclassifications averaging out to ~10,000+ misclassified replicates total: not one landed elsewhere. This is the kind of empirical signature that does not arise from noise.

**Headline verdicts (4 pass, 1 fail by reversed direction, 3 observational):**

| H | Claim | Verdict | Notes |
|---|---|---|---|
| H1 | Monotone shows ≥5pp larger W3-A than non_monotone | **FAIL, direction reversed** | Pre-flight tr(RIV) table predicted this before the sweep ran. Median monotone W3-A = 0.098; non_monotone = 0.147 (diff −0.049). The RIV-heterogeneity-is-driver intuition was wrong for this design; non_monotone has *more* candidate-level RIV spread, not less. Documented as the §H1 fallback. |
| H2-MAR | At MAR + congenial: W3-C ≥ 0.80 and W3-A ≥ 0.05 at every cell | **PASS** | min W3-C = 1.000; min W3-A = 0.088. Universal. |
| H2-MNAR | Observational only — expected possible breakdown | **observational, framework SURVIVES (refined claim — see Parameter Bias Anchor below)** | W3-A range under MNAR + congenial = [0.093, 0.156] (median 0.127), comparable to MAR; W3-C = 1.000 at every MNAR cell. The framework's empirical guarantees extend further than the derivation's MAR-only requirement. Phase 4 measurement reveals our MNAR mechanism produces mean parameter `‖bias‖ = 0.262` (~13% relative) and biases σ_24 by -13.2% of truth under monotone — so the survival is NOT because the mechanism was weak; the framework is robust to MNAR-induced bias of *this magnitude on these particular parameters*. |
| H3 | W3-B shrinks with N; W3-A approximately N-invariant; W3-C ≥ 0.80 at all N | **PASS** | W3-B median by N: 0.101 → 0.077 → 0.089 (shrinks). W3-A max−min across N = 0.014 (well below 0.05 threshold). W3-C = 1.000 at every N. The asymptotic prediction "leading-order W3-A is N-invariant, finite-N corrections in W3-B shrink as 1/N" is empirically validated. |
| H3b | Partial only — rate=60% deferred due to Amelia bootstrap chol() failure | **observational, super-linear** | At available rates {20%, 40%}: W3-A monotone in rate (PASS). Ratio W3-A(40%) / W3-A(20%) = 3.11 — *exceeds* linear scaling, which would predict ratio 2.0. W3-A is N-invariant at each rate within 0.4–1.7pp. The recovery's dependence on missingness rate is super-linear; rate matters even more than the leading-order theory predicts. |
| H4 | W3-A(M=200) ≥ W3-A(M=20) − 0.02 at every MAR+cong cell | **PASS** | M=20 and M=200 give nearly identical recovery (sweep means 0.121 vs 0.123). Practitioner-default M=20 is fine for the framework. |
| H5 | Congeniality — expected uncongenial breakdown | **observational, partial halving** | Median W3-A: congenial 0.117, uncongenial 0.057 — uncongeniality halves the bias-correction gap (because uncorrected MI-AIC ends up near the oracle: empri-based shrinkage toward diagonal happens to align with selecting the correlation-restricted true model). But **W3-C = 1.000 even under uncongeniality** — direction survives when magnitude shrinks. Less dramatic breakdown than predicted. |
| H6 | FIML vs Amelia cong M=200 agree within 3pp at every cell | **PASS** | Engine-independence validated across the sweep. |

**W1 sweep (18 FIML cells, R=2000).** Total bias `T_hat` is within MCSE of the predicted `+½ tr(RIV)` at every MAR cell (passT = TRUE for all 6 MAR cells). Under MNAR the theorem breaks cleanly, as expected: non_monotone+MNAR drifts toward negative T_hat with growing N (-2.0 at N=1000); monotone+MNAR grows unboundedly with N (+45 at N=1000). This is the strongest possible MNAR-stress evidence — visibly diverges in the way the proper-MI assumption violation predicts. The W1 sweep also includes 6 MNAR_targeted cells (see Parameter Bias Anchor below for the mechanism design rationale); they behave qualitatively like standard MNAR — theorem violated, magnitudes comparable.

**Parameter Bias Anchor (Phase 4 — new in this run).** A direct measurement of `E[theta_obs - theta_truth]` at the W3 DGP across 18 cells (2 patterns × 3 mechanisms × 3 N), R=2000 each. This phase answers a question that W3's "selection survives MNAR" finding could not on its own: *did our MNAR actually bias the parameters substantially, or did W3 just happen to be insensitive to a weak MNAR?* The answer:

- **MAR**: `‖bias‖` decays as `1/√N` (0.012 → 0.005 → 0.003 across N=200/500/1000). Consistent estimator, as expected.
- **MNAR (standard, mice::ampute weights = X_j-itself for pattern j)**: `‖bias‖` is N-invariant at ~0.23 non_monotone / ~0.29 monotone (relative ~11–14%). Bias is **concentrated in μ and diagonal variances**: μ_1, μ_2 biased by 0.16 each under non_monotone MNAR at N=1000 (|z|=187); μ_4 biased by -0.23 (|z|=264) under monotone MNAR at N=1000.
- **σ_24 specifically** (load-bearing for the M_C true model): biased -13% of truth under monotone MNAR (|z|=56 at N=1000). σ_13 biased only -2%.
- **MNAR_targeted (weights designed to disrupt σ_13 / σ_24 joint distributions)**: pilot + R=2000 confirmation showed the targeted weights *reduce* total `‖bias‖` (~0.14 / 0.21) and produce essentially the same σ_13 / σ_24 bias as standard MNAR (~1.5% / ~13%). Conclusion: within ampute's linear weight regime, ~13% σ_24 bias is the engineering ceiling for MNAR strength on the load-bearing parameter; broader weight matrices spread selection across more parameters but don't concentrate it on the off-block correlations.

**Why W3 selection survives despite material MNAR-induced bias.** The W3 candidate-model comparison's sensitivity is asymmetric in the parameters:
- M_A, M_B, M_C, M_D all freely fit μ and diagonal variances — the bulk of MNAR bias is invisible to model ranking.
- The comparison depends on which *off-block correlations* (σ_12, σ_13, σ_24, σ_34) you let be nonzero.
- Even with σ_24 biased to 0.348 (13% off truth 0.4), M_C still beats M_A and M_B (which force σ_24 = 0 — misspecified by the full 0.4) and out-performs M_D (which over-fits MNAR-induced spurious cross-correlations like σ_41 = -0.016 and σ_43 = -0.046 that only appear under MNAR).

**Refined H2-MNAR claim for §6:** The framework is empirically robust to MNAR mechanisms of the magnitude ampute can engineer (~13% bias on the load-bearing σ_24, larger bias on parameters M_C and friends fit nuisance-freely). A mechanism designed to specifically and aggressively bias the off-block correlations could plausibly break selection; engineering such a mechanism would require leaving ampute's linear-weight regime (e.g., multiplicative or interactive selection probabilities). This is a clean piece of follow-up work, not a hole in the current claim.

**H1 reversal — re-framing for the manuscript.** The pre-flight tr(RIV) calculation (analytic, 12 cells × 50 seeds at the truth) showed before the sweep ran that monotone has *less* candidate-level RIV heterogeneity (M_D − M_C spread 1.86 vs non_monotone 2.85). The empirical sweep confirmed exactly that mapping into W3-A magnitudes. The manuscript §5 will reframe: instead of "monotone is the harder case," it's "the bias correction's value tracks the *spread* in candidate-level tr(RIV), and our particular pattern × candidate-model interaction makes non_monotone the higher-spread setting." The pre-flight table itself becomes a Figure or appendix item — empirical evidence that the framework's value is predictable from the analytic differential-bias quantity.

**Implication for §5 (IC application).** The headline empirical story strengthens: W3-A = +11 pp at the preregistered cell, and the comprehensive sweep extends that to "between 0.04 and 0.16 pp recovery across every MAR + congenial cell of a 60-cell grid, with W3-C = 1.000 universally." The directional finding is universal; the magnitude is consistently meaningful. The framework's safety margins are also tighter than predicted: MNAR doesn't break it, M=20 works fine, and uncongeniality halves but doesn't destroy the recovery.

**What the sweep did NOT change.** The basic v4.5 derivation is unchanged; the bias decomposition is empirically supported under every condition tested. The reframing is about *where the value lands*, not the theorem's correctness.

**Artifacts (committed; single-command reproducibility):**
- `verification/run_all.R` — **single entrypoint**. `Rscript verification/run_all.R 2000 prod all 20` reproduces the entire sweep from scratch in ~3 hours on a 20-core cluster.
- `verification/_modules/` — modular phase functions: `smoke-tests.R`, `w1-sweep.R`, `w3-sweep.R`, `w3-rate.R`, `mnar-bias.R`, `aggregate.R`.
- `verification/_legacy/` — retired standalone scripts (8 files) preserved for traceability; superseded by run_all.R. See `_legacy/README.md` for the mapping.
- `verification/00-setup.R` — shared primitives, extended for the sweep with `apply_missingness_ampute()` (mice::ampute wrapper supporting MAR / MNAR / MNAR_targeted × non_monotone / monotone), `empri` arg on `impute_mvn_amelia()`, `par_init` warm-start protocol on `mle_chol_sigma12()` / `chan_smi_test_k1()`.
- `verification/cache/run_all-prod/` — per-phase cache directories:
  - `phase0/preflight-trRIV.csv` — analytic RIV anchor across (pattern, mech, N).
  - `phase1-w1/summary.csv` + per-cell `.rds` — W1 theorem-validation outcomes.
  - `phase2-w3/summary.csv` + per-cell `.rds` — W3 main sweep selection rates.
  - `phase3-rate/summary.csv` + per-cell `.rds` — H3b rate experiment.
  - `phase4-mnar-bias/summary.csv` + per-cell `.rds` — parameter-bias measurements.
  - `phase5/verdicts.md` — auto-generated hypothesis verdict table.
  - `phase5/combined.csv` — tidy combined frame across phases.

**Three-layer reproducibility:** IDEAS.md (this file) is the *what we found and what it means*; `verification/run_all.R` is *how to reproduce it*; the per-phase `.rds` caches and summary CSVs are *the raw evidence*. Each layer points at the next.

---

## Citation discipline

Encoded in `CLAUDE.md` and operationalized in `todo/001-literature-and-hooks.md`. PreToolUse hook at `.claude/hooks/check_citations.py` enforces.

Summary: every `@<citekey>` in `manuscript/` must be backed by `literature/<citekey>.md`, read in the current session. Defense against AI-hallucinated citations.

Reference acquisition backlog at `todo/003-references-to-acquire.md`.

---

## Companion paper relationship

- `~/git-repositories/MI-IC` holds the SEM methodology paper, the v4.5 derivation source, the `miicsem` R package, the empirical SEM simulation pipeline, and the congeniality/PMM empirics.
- **MI-IC Study 1** (mediation model, MCAR/MAR/MNAR, M=20, N=100) empirically validates the $\tfrac{1}{2}\text{tr}(\text{RIV})$ bias formula in a general-likelihood setting — this is direct empirical support for W1 in *this* paper.
- **This paper does the standalone theoretical derivation** of the bias decomposition; MI-IC consumes it for SEM-specific machinery (CFI/TLI/RMSEA, MI-AIC/MI-BIC in SEM).
- **The SEM paper cites this paper for the derivation** and stands on its independent empirical work. That separation is what makes the SEM paper sole-authorable under traditional norms while this paper is honestly AI-co-authored under JAIGP norms.

**Discipline:** if you find yourself wanting to add SEM-specific content here, push it to MI-IC.

---

## Methodological notes (worth small mentions in the paper)

These are second-tier contributions worth a paragraph each:

1. **Custom Cholesky + analytic gradient for constrained MVN MLE under one-zero off-diagonal constraint.** 25× faster per fit than lavaan; made the M=200 preregistered W2 production feasible in 84 min instead of an estimated 35 hours with all-lavaan. The construction generalizes to any single-zero-off-diagonal constraint and is implementable in ~50 lines of R. Worth a methods footnote with the gradient derivation in an appendix.

2. **First end-to-end implementation of Chan (2022, AoS) SMI Algorithm 2.1 outside Chan's own paper.** Stacked-imputation construction + jackknife OMI estimator + MC reference distribution. Verifies Chan's machinery works as described in a non-trivial setting (k=1, anisotropic MAR) and provides clean R code for re-use.

3. **Satorra-Bentler scaled-shifted as parsimonious alternative.** Applied to the differential deviance (vs the saturated reference for IC, or vs the unconstrained for LRT). At M=50 it's competitive with Chan's MC; at M=200 it's slightly inferior in size-adjusted power but achieves dead-nominal Type I in closed form. The MI-IC step5 SEM validation shows SB matches oracle exactly at N=500. For practitioners who don't want Chan's MC machinery, SB is a defensible default — and the present paper provides the formula for the differential-deviance variant.

---

## Open work

### Theoretical

- Formal proof of the bias decomposition Theorem (clean version of MI-IC v4.5 §3 derivation, stripped of SEM language and generalized for arbitrary regular likelihood models).
- Le Cam-style power-dominance Conjecture for the LRT application — moved to Discussion as a conjecture pending V7-style witness (now W2-extended).

### Numerical verification — COMPLETE at preregistered config

- W1, W2, W3 all executed per `todo/004-simulation-hypotheses.md` at preregistered N=200, M=200, R=1000 with both engines (FIML and Amelia).
- Preregistered sensitivity sweeps still to run if needed for §5 robustness: W3 at N ∈ {100, 500, 1000} and missingness rate ∈ {20%, 60%}. Each cell is ~50s of compute with the optimized pipeline. Run if reviewer asks.
- Each witness needs its companion `::: {.callout-tip}` block in the manuscript at the right section.

### Literature acquisition

- Phase 1 of `todo/001-literature-and-hooks.md` is closed (26 references in `literature/`, all verified or acquired).
- `todo/003-references-to-acquire.md` is the active acquisition backlog for any new references that arise.

### Writing

- Title candidates: *"Deviance Bias under Multiple Imputation, with Applications to Likelihood-Ratio Tests and Information Criteria"* or *"An Unbiased Estimator of the Complete-Data Q-Function under Congenial Multiple Imputation"*.
- Target length: 12–15 pages (JAIGP standard) rather than the originally-planned 20–25.
- Structure (revised): intro (LRT and IC framing) → setup → bias decomposition (§3, W1) → LRT application with three-way practitioner menu (§4, W2 + SB) → IC application with directional concordance headline (§5, W3 + SB) → discussion (one-DGP limitation + cross-paper coordination with MI-IC + next-study scope) → brief appendix with proof + Cholesky gradient.

### Real-data demonstration — deferred

- Considered NHANES lipid panel (item-level missingness only ~6-7%, too modest for the W3 RIV-anisotropy story to land cleanly) and HRS wealth components (longitudinal, 25-40% refusal, much better fit for the demonstration). Decision deferred until manuscript prose is further along — the empirical case from W3 alone is strong without it.

---

## Boundary discipline

If you find yourself writing about:

- "SEM chi-square test"
- lavaan, MLR, Bollen et al.
- "Type I error in CFA"
- `miicsem`, CFI, TLI, RMSEA
- PMM, Amelia, congeniality empirics

...you've drifted. Push it to MI-IC. This paper is about general MI deviance inference.

If you find yourself proposing a "scaled-shifted chi-square correction" or "spectral test based on RIV_⊥ eigenvalues" — that's archived. Chan (2022, AoS) already did it better. The paper is now bias-decomposition-focused.

If you find yourself writing a citation without `literature/<citekey>.md` open in this session, stop and run the literature acquisition workflow (`todo/001-literature-and-hooks.md`).

---

## Archive: original spectral-correction conception (pre-reframe)

*Material below was the load-bearing content before the 2026-05-22 reading of Chan (2022, AoS). Preserved for traceability. **Do not draft from this material.***

### Three original claims (pre-reframe)

1. **+½tr(RIV) bias of the Q-function** — **retained** as the headline. Foundational MI deviance bias result, decomposed as +tr(RIV) imputation bias minus ½tr(RIV) estimation mismatch. General for any likelihood-based model fit on congenially imputed data.
2. **Obs/mis decomposition + generalized eigendecomposition → scaled-shifted correction** — **dropped**. Chan (2022, AoS) provides a more accurate non-EFMI test via exact Monte Carlo of the limiting distribution $\mathbb{D}$ on the full OMI eigenvalue spectrum. Our scaled-shifted form is the kind of two-moment approximation he explicitly tests and dismisses (§A.3, §B.1) as inferior.
3. **PMM sign-flips Term 1 (congeniality empirics)** — out of scope (lives in MI-IC).

### Original Le Cam power-dominance theorem (pre-reframe)

Claim (a)/(b)/(c) about asymptotic non-centrality dominance over Chan-Meng under anisotropic RIV. Reframed as a conjecture in Discussion (Application 1, §4); empirical support to come from W2 rather than a separate witness.

### Original lineage paragraph (pre-reframe)

Rubin (1987) → Meng-Rubin (1992) → Chan-Meng (2022) → "this work (full eigenspectrum, anisotropic FMI)". **Replaced.** Chan-Meng (2022) and Chan (2022) are now adjacent test-calibration work; we sit upstream as the deviance-bias-correction layer.

### Original seven witnesses (pre-reframe)

| # | Original claim | Status |
|---|---|---|
| V1 | $+\text{tr}(\text{RIV})$ imputation bias | Becomes part of W1 |
| V2 | $-\tfrac{1}{2}\text{tr}(\text{RIV})$ estimation mismatch | Becomes part of W1 |
| V3 | $\chi^2 = A + B$ obs/mis split | Dropped (no longer headline) |
| V4 | Eigenvalues $\{\lambda_j\}$ of $\text{RIV}_\perp$ | Dropped |
| V5 | $\text{Var}[\chi^2_{\text{MI}}]$ formula | Dropped |
| V6 | Rank-1 collapse to Chan-Meng | Dropped |
| V7 | Power dominance under anisotropy | Generalized to W2 (LRT power loss under local alternatives) |

V1+V2 become W1. V7 generalizes to W2 (broader claim than CM-specific dominance). W3 is new.
