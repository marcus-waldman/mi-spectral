# IDEAS.md

Directional anchor for drafting the JAIGP paper. Captures the load-bearing reasoning from the 2026-05-22 session that birthed this repo.

---

## Motivation and venue choice

**Why JAIGP, not a traditional methodology journal.** The technical derivation was developed in collaboration with Claude (Anthropic, Opus 4.7). The human prompter declined to submit derivation-heavy theory to *Psychological Methods* or *Structural Equation Modeling* under standard sole-authorship norms, on the grounds that the math came from AI dialogue rather than independent human work. JAIGP — peer-reviewed, ORCID-verified human prompters, transparent AI co-authorship as the explicit norm (founded by César A. Hidalgo at Toulouse School of Economics, in collaboration with Anthropic) — fits the ethical posture.

**Tradeoff accepted.** JAIGP is new (peer review pipeline launched March 2026), not yet indexed (no DOI, Scopus, or Web of Science as of mid-2026). The trade is real: a more prestigious venue would carry more weight with traditional methodology reviewers. The trade is accepted because:

- The derivation is empirically validated already — the companion SEM paper (MI-IC repo) shows the spectral correction restores Type I from 21% to ~5% (oracle level). The math works regardless of venue.
- The companion SEM methodology paper at MI-IC will cite this one for the derivation and stand on its independent empirical contributions (`miicsem` package, simulation results, congeniality empirics) — those *are* the human prompter's independent work.
- Mitigation: deposit on Zenodo in parallel for a stable DOI; cite the Zenodo DOI from the SEM paper to handle JAIGP's indexing-status concern at the receiving venue.

---

## The three claims and what made the cut

Earlier conversation identified three candidate "broader contributions" beyond SEM. Two are in scope for this paper; one is not.

1. **+½tr(RIV) bias of the Q-function** — foundational MI deviance bias result, decomposed as +tr(RIV) imputation bias minus ½tr(RIV) estimation mismatch. **IN SCOPE.** General for any likelihood-based model fit on congenially imputed data.

2. **Obs/mis decomposition + generalized eigendecomposition → scaled-shifted correction.** Variance correction; builds on #1. **IN SCOPE.** This is where the headline theorem lives.

3. **PMM sign-flips Term 1 (congeniality empirics).** Empirical finding, not a theorem. **OUT OF SCOPE** for JAIGP — too applied, no theoretical characterization of what PMM is doing yet. Files into the MI-IC methodology paper as a robustness/limitations section, or eventually a standalone applied-stats note targeting *Stat in Med* or *Stat Sci*.

---

## Positioning in the Meng–Rubin / Chan–Meng lineage

This work is the **third entry** in a 30-year program of refining likelihood-ratio testing under multiple imputation. Each step relaxes a stronger assumption.

### Lineage at a glance

| Step | Year | What it fixed | What it left open |
|---|---|---|---|
| Meng–Rubin (D_L) | 1992 | First combining rule for LR tests under MI. Scalar correction r_L (essentially average eigenvalue). | Non-negativity, invariance, monotonic power, EFMI, finite-M variance. |
| Chan–Meng | 2022 | Non-negativity, invariance, monotonic power, computational feasibility (via stacked-data LRT). | EFMI assumption retained. Finite-M variance still uncorrected. |
| **This work** | 2026 | **Drops EFMI** by using the full eigenvalue spectrum of $\text{RIV}_\perp$. Scaled-shifted correction calibrates **both moments** at **finite M**. | Uncongenial MI (e.g., PMM) — open. |

### The orthogonal-axes insight (critical for framing)

Chan–Meng (CM) and this work generalize Meng–Rubin along **orthogonal axes**:

| Axis | M–R (1992) | CM (2022) | This work |
|---|---|---|---|
| Numerator construction | average-then-max | **max-stacked-data** (fixes non-negativity, invariance, monotonic power) | **inherits CM's stacked-data construction** |
| Null calibration | scalar $r_L$ | scalar $r_m$ (EFMI) | **full eigenvalue spectrum of $\text{RIV}_\perp$** |
| Finite-M variance | none | asymptotic in $m$ only | **finite-$m$, exact under anisotropy** |

**Synthesis.** Use Chan–Meng's stacked-data LRT as the numerator (inherit their bookkeeping fixes); replace their scalar EFMI calibration with the spectral scaled-shifted correction. The resulting test reduces to CM under EFMI as a **rank-one special case** (when all eigenvalues of $\text{RIV}_\perp$ are equal). Anisotropic spectra are where this work strictly improves CM.

CM is explicit (Chan & Meng 2022, p. 6) about EFMI being a strong assumption that collapses $k$ nuisance FMIs into one scalar — exactly the dimensionality reduction this paper avoids.

---

## The Le Cam-style power dominance theorem (the headline)

**Claim.** Under congenial MI and standard regularity conditions, the scaled-shifted MI test (CM-stacked $\hat d_L$ numerator + spectral calibration):

- **(a)** Achieves nominal level $\alpha$ exactly in the asymptotic-$N$, fixed-$M$ regime.
- **(b)** Is asymptotically equivalent to the complete-data LR test in non-centrality structure — i.e., achieves the asymptotic power envelope at level $\alpha$.
- **(c)** At matched (size-corrected) level $\alpha$, has asymptotic power $\geq$ Chan–Meng's $\hat D_L$, with strict inequality whenever the $\text{RIV}_\perp$ eigenvalue spectrum is anisotropic.

**Proof sketch for (c).** Both tests share the same numerator (CM-stacked LRT). They differ only in null calibration. By Cauchy–Schwarz, $\sum \lambda_j^2 \geq (\sum \lambda_j)^2 / \text{df}$, with equality iff all $\lambda_j$ are equal. So under anisotropic spectra:

- CM's effective null variance is **smaller** than the true MI variance → CM is under-dispersed under $H_0$ → CM has inflated Type I error.
- Size-correcting CM (using a larger critical value to control level) **shrinks the rejection region** → strict power loss under any alternative.
- v4.5 has correctly calibrated variance → no shrinkage needed → preserves the complete-data power profile.

Le Cam's third lemma + contiguous alternatives delivers the asymptotic non-centrality structure.

**Caveats.**

- "Uniformly more powerful" in strict Neyman–Pearson sense is too strong for composite hypotheses with chi-square LR tests.
- The defensible claim is **asymptotic Pitman efficiency at matched level** — not finite-sample uniform domination across all alternatives.
- Proof needs careful working: no obvious obstructions, but contiguity setup under MI deserves care. The empirical signal from MI-IC simulations (chi2_D3 = 14.8% Type I vs chi2_MI_corr ≈ 5%) is the diagnostic.

This theorem is the contribution's intellectual payoff. Everything else in the paper supports it.

---

## Running example: full multivariate normal

The entire verification suite and the worked example use one setting:

> $X \sim \mathcal{N}_p(\mu, \Sigma)$, both $\mu$ and $\Sigma$ unknown. Test $H_0: \mu = \mu_0$. Per-variable structured missingness (rates vary across coordinates). Joint MVN imputation (congenial with the analysis model).

**Why this and not MVN-mean with known $\Sigma$:**

1. **It's the imputation engine itself.** Joint MVN ≡ Schafer's NORM ≡ Amelia. Verifying the spectral correction *inside the imputation model people actually use* lands much harder than in a stripped-down toy.
2. **Anisotropic $\text{RIV}_\perp$ arises naturally.** With both $\mu$ and $\Sigma$ unknown, mean and covariance components carry different missing-information loads; anisotropy doesn't need to be engineered.
3. **Tested-vs-nuisance structure.** $\mu$ is tested; $\Sigma$ is nuisance. This is exactly the setup where EFMI (one scalar FMI summarizing both blocks) fails most naturally — and EFMI's failure is the paper's headline.
4. **Recognizable textbook setting.** Hotelling's $T^2$ and the LR test for the MVN mean are canonical. Reviewers anchor on what the complete-data test would have been; no ambiguity about the comparison.

**Rejected (and why):** MVN-mean with known $\Sigma$. Smaller, simpler, fewer bugs in verification code — but no nuisance structure, no natural anisotropy, fails to exercise the EFMI-violation story. Pedagogical simplicity wasn't worth the lost credibility.

**Closed-form availability.** Under monotone missingness, $W$, $B$, $\mathcal{I}_\text{com}$, $\text{RIV}_\perp$ are all analytically computable (textbook material from Little & Rubin). Under general MAR patterns, simulation-based estimation is standard; verifications use both modes — monotone for an analytical sanity check, general patterns for the headline witnesses.

**Implementation note.** The covariance-block of the information matrix needs duplication-matrix machinery (Magnus & Neudecker). Numerical conditioning handled via Cholesky symmetrization — same trick as MI-IC v4.5 §13.

---

## Verification suite architecture

**Principle.** Every load-bearing equation in the derivation gets a **numerical witness** — an empirical quantity computed in a small simulation under the running example, shown alongside the math in the manuscript. Witnesses are *not* results; they're calibration checks demonstrating that the AI-derived equations operationally do what they claim. Without witnesses, a human reviewer faced with 30 pages of AI-assisted derivation has no rational basis to invest the time to verify line-by-line. With witnesses, the reviewer can spot-check the empirical evidence first and decide whether the proof structure is worth scrutinizing.

**The seven witnesses.**

| # | Equation verified | Empirical quantity | Manuscript section |
|---|---|---|---|
| V1 | $+\text{tr}(\text{RIV})$ imputation bias | $E[\bar Q(\hat\theta_\text{obs})] - E[\ell_\text{com}(\hat\theta_\text{obs})]$ vs. $\text{tr}(\text{RIV})$ | §3 |
| V2 | $-\tfrac{1}{2}\text{tr}(\text{RIV})$ estimation mismatch | $E[\ell_\text{com}(\hat\theta_\text{obs})] - E[\ell_\text{com}(\hat\theta_\text{com})]$ vs. $-\tfrac{1}{2}\text{tr}(\text{RIV})$ | §3 |
| V3 | $\chi^2 = A + B$ obs/mis split | Empirical $(A_m, B_m)$; $A_\infty$ vs FIML $\chi^2$; $B_\infty$ vs $2 \cdot \text{KL}(p_\text{imp} \| p_{M_1})$ | §4 |
| V4 | Eigenvalues $\{\lambda_j\}$ of $\text{RIV}_\perp$ | Empirical generalized eigendecomposition of $W^{-1}B$ vs. theoretical $\text{RIV}_\perp$ spectrum | §5 |
| V5 | $\text{Var}[\chi^2_\text{MI}] = \text{Var}[\chi^2_\text{com}] + 2\sum \lambda_j^2$ | Empirical variance across reps vs. theoretical prediction | §6 |
| V6 | Rank-1 collapse to Chan–Meng | Under isotropic spectrum (all $\lambda_j$ equal), scaled-shifted form ≡ CM's $F$-distribution form (numerical match) | §7 |
| V7 | Power dominance under anisotropy | At matched (size-corrected) level $\alpha$, power(this) > power(CM) when spectrum is anisotropic | §8 |

**Layout (planned):**

```
verification/
├── 00-setup.R                  # shared simulation primitives (full MVN data gen, MI, fits)
├── V1-imputation-bias.R
├── V2-estimation-mismatch.R
├── V3-obs-mis-split.R
├── V4-eigenvalue-spectrum.R
├── V5-variance-formula.R
├── V6-rank1-collapse.R
├── V7-power-dominance.R
└── cache/                      # serialized outputs (RDS) — read by manuscript
```

Manuscript-side, each witness is a Quarto chunk reading from `cache/` and emitting a small table or figure inside a `::: {.callout-tip}` block titled "Numerical witness." Pre-computed cache keeps render time low; verification scripts are run once when simulation parameters change.

**Verification-theater mitigation.** Two disciplines:

1. **Known-wrong baseline.** Each witness reports the un-corrected quantity alongside the corrected one (e.g., V5 shows Var[χ²_MI] *without* the spectral correction so the correction is visibly doing real work).
2. **Non-trivial anisotropic regime.** Per-variable missingness rates with deliberate variation; not just symmetric or uniform setups.

**Phasing.**

- **Phase A:** `00-setup.R` (MVN primitives). Validates the pipeline mechanically before any claims tested.
- **Phase B:** V1 + V2 (bias decomposition checks). Cheapest; validates Claim 1.
- **Phase C:** V3 + V4 + V5 (spectral-correction core). Most important to get right.
- **Phase D:** V6 + V7 (lineage and power). Headline witnesses.

**Gate:** If Phase B fails empirically, revisit the derivation before going on. Same for Phase C.

---

## Citation discipline

Encoded in `CLAUDE.md` and operationalized in `todo/001-literature-and-hooks.md`.

Summary: every `@<citekey>` in `manuscript/` must be backed by `literature/<citekey>.md`, read in the current session. A PreToolUse hook (spec written, not yet implemented) blocks edits that violate this. Defense against AI-hallucinated citations, which is one of the most common failure modes for AI-assisted papers in peer review.

**Status:** spec done; hook script not yet implemented. Initial citation corpus listed in the todo with proposed citekeys (Rubin 1987, Meng-Rubin 1992, Meng 1994, Chan-Meng 2022, Xie-Meng 2017, Cavanaugh-Shumway, Asparouhov-Muthén, van der Vaart 1998, Schafer 1997, Magnus-Neudecker). Open questions for the next session at the bottom of the todo.

---

## Companion paper relationship

- `~/git-repositories/MI-IC` holds the SEM methodology paper, the v4.5 derivation source, the `miicsem` R package, the empirical SEM simulation pipeline, and the congeniality/PMM empirics.
- **This paper cites no SEM content.** It draws on the MI-IC v4.5 §12–§13 derivation as source material (acknowledged in the Provenance block of the manuscript) but reframes the same machinery for general likelihood inference.
- **The SEM paper cites this paper for the derivation** and stands on its independent empirical work. That separation is what makes the SEM paper sole-authorable under traditional norms while this paper is honestly AI-co-authored under JAIGP norms.

**Discipline:** if you find yourself wanting to add SEM-specific content here, push it to MI-IC.

---

## What to lift from MI-IC's v4.5 derivation

The current SEM-framed derivation lives at `~/git-repositories/MI-IC/claude/derivations/mi_deviance_bias_derivation_v4.qmd`. For this repo:

- **§10 (CFI/TLI/RMSEA derivation):** DROP. SEM-specific.
- **§12 (Theta-subset-Phi closure):** KEEP, REFRAME. Generalize from SEM-imputed Phi to general congenial imputation parameter space.
- **§13 (finite-M variance via generalized eigendecomposition):** KEEP — this is the core. Strip SEM language; frame for general likelihood models.
- **"Practical Application" appendix:** DROP. The corrections decision table is SEM-specific; lives in MI-IC.
- **v4.4 §12 closing the Theta-subset-Phi gap:** KEEP.

---

## Open work

### Theoretical

- Formal proof of Theorem (a)–(c) above. v4.5 derivation has (a) and (b) implicit; (c) needs an explicit Le Cam contiguity argument.
- Tighter derivation of the obs/mis decomposition. Currently introduced as "split along obs/mis"; should be derived more carefully from the imputation model's likelihood factorization.
- Verify the rank-1 (isotropic-spectrum) reduction to CM algebraically: when all $\lambda_j$ are equal, does the scaled-shifted correction collapse exactly to CM's $F$-distribution form?

### Numerical verification

- Execute the seven-witness suite in `verification/` (see architecture section).
- Each witness needs its companion `::: {.callout-tip}` block in the manuscript at the right section.

### Literature acquisition

- Execute `todo/001-literature-and-hooks.md` Phases 1–3 before any citations are written.

### Writing

- Working title candidates: *"A finite-M spectral correction for likelihood-based inference under multiple imputation"* or *"Spectral completion of multiple-imputation likelihood-ratio tests."*
- Target length: 20–30 pages.
- Structure (already stubbed in `manuscript/mi-spectral.qmd`): provenance → intro → setup → bias decomposition → obs/mis split → eigendecomposition → scaled-shifted correction → CM positioning → power theorem → worked example → discussion.

---

## Boundary discipline

If you find yourself writing about:

- "SEM chi-square test"
- lavaan, MLR, Bollen et al.
- "Type I error in CFA"
- `miicsem`, CFI, TLI, RMSEA
- PMM, Amelia, congeniality empirics

...you've drifted. Push it to MI-IC. This paper is about general MI hypothesis testing.

If you find yourself writing a citation without `literature/<citekey>.md` open in this session, stop and run the literature acquisition workflow (`todo/001-literature-and-hooks.md`).
