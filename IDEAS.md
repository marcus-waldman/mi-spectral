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
