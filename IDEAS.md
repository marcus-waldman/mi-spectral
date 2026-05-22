# IDEAS.md

Curated load-bearing pieces from the conversation that birthed this repo (2026-05-22). Directional anchor for drafting; not a manuscript draft.

---

## The three claims and what made the cut

1. **+½tr(RIV) bias of the Q-function** — foundational MI deviance bias result, decomposed as +tr(RIV) imputation bias minus ½tr(RIV) estimation mismatch. **IN SCOPE.**

2. **Obs/mis decomposition + generalized eigendecomposition → scaled-shifted correction.** Variance correction; builds on #1. **IN SCOPE.**

3. **PMM sign-flips Term 1 (congeniality empirics).** Empirical finding, not a theorem. **OUT OF SCOPE** for JAIGP — files into the MI-IC methodology paper as robustness/limitations, or as a standalone applied-stats note.

---

## Positioning relative to Chan–Meng (2022)

CM and this work generalize Meng–Rubin (1992) along **orthogonal axes**:

| Axis | M–R (1992) | CM (2022) | This work |
|---|---|---|---|
| Numerator construction | average-then-max | **max-stacked-data** (fixes non-negativity, invariance, monotonic power) | **inherits CM's stacked-data construction** |
| Null calibration | scalar r_L | scalar r_m (EFMI) | **full eigenvalue spectrum of RIV_⊥** |
| Finite-M variance | none | asymptotic in m only | **finite-m, exact under anisotropic FMI** |

**Synthesis.** Use Chan–Meng's stacked-data LRT as the numerator; replace their scalar EFMI calibration with the spectral scaled-shifted correction. Reduces to CM under EFMI as a special case (when all RIV_⊥ eigenvalues are equal).

CM is explicit about EFMI being a strong assumption (their p.6). This work drops it.

---

## Le Cam-style power dominance theorem (to prove formally)

**Claim.** Under congenial MI and standard regularity conditions, the scaled-shifted MI test (with CM-stacked d̂_L as numerator + spectral calibration):

- (a) Achieves nominal level α exactly in the asymptotic-N, fixed-M regime.
- (b) Is asymptotically equivalent to the complete-data LR test in non-centrality structure — i.e., achieves the asymptotic power envelope at level α.
- (c) At matched (size-corrected) level α, has asymptotic power ≥ Chan–Meng's D̂_L, with strict inequality whenever the RIV_⊥ eigenvalue spectrum is anisotropic.

**Proof sketch for (c).** Both tests share the same numerator (CM-stacked LRT). They differ only in null calibration. By Cauchy–Schwarz, Σ λ_j² ≥ (Σ λ_j)² / df, with equality iff all λ_j are equal. So under anisotropic spectra, CM's effective null variance is *smaller* than the true MI variance → CM is under-dispersed → size-correction shrinks the rejection region → strict power loss. Le Cam third lemma + contiguous alternatives delivers the asymptotic non-centrality structure.

**Caveats.** "Uniformly more powerful" in strict Neyman–Pearson sense is too strong for composite hypotheses with chi-square LR tests. The defensible claim is **asymptotic Pitman efficiency at matched level**. Proof needs careful working — no obvious obstructions, but contiguity setup under MI deserves care.

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
- Verify the rank-1 (isotropic-spectrum) reduction to CM. Algebraic check: when all λ_j are equal, does the scaled-shifted correction collapse to CM's F-distribution form?

### Numerical verification (minimal — JAIGP doesn't need a sprawling simulation study)

- A **generic, non-SEM** anisotropic-FMI example: e.g., multivariate normal mean problem with structured missingness producing anisotropic RIV_⊥. Demonstrate v4.5 controls level at α while CM (EFMI) inflates.
- Empirical confirmation that the Cauchy–Schwarz gap is what drives the power difference.

### Writing

- Working title candidates: *"A finite-M spectral correction for likelihood-based inference under multiple imputation"* or *"Spectral completion of multiple-imputation likelihood-ratio tests."*
- Target length: 20–30 pages.
- Structure: intro → setup (congenial MI, Q-function) → bias decomposition → obs/mis split → eigendecomposition → scaled-shifted correction → CM positioning → power theorem → minimal worked example → discussion.

---

## Boundary discipline

If you find yourself writing about:

- "SEM chi-square test"
- lavaan, MLR, Bollen et al.
- "Type I error in CFA"
- `miicsem`, CFI, TLI, RMSEA
- PMM, Amelia, congeniality empirics

...you've drifted. Push it to MI-IC. This paper is about general MI hypothesis testing.
