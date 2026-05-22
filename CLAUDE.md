# CLAUDE.md

## Scope

**JAIGP theory paper.** A finite-M moment correction for likelihood-based hypothesis tests under congenial multiple imputation. Positioned as the spectral completion of the Meng–Rubin (1992) → Chan–Meng (2022) program.

## Out of scope — redirect to `~/git-repositories/MI-IC`

- SEM specifics: lavaan, CFI/TLI/RMSEA, saturated SEM imputation, `miicsem` package.
- Congeniality / PMM empirics (separate applied note, not this paper).
- Empirical SEM simulations (Bollen et al. design, Type I tables, etc.).

If the work drifts into any of the above, push it back to MI-IC.

## Authorship model

AI-assisted derivation, target venue JAIGP (Journal for AI Generated Papers). Provenance is transparent per JAIGP norms. ORCID-verified human prompter: marcus.waldman.

## Core contribution

1. **Bias.** Q-function bias under congenial MI is +½tr(RIV) = +tr(RIV) (imputation bias) − ½tr(RIV) (estimation mismatch). General for any likelihood-based model fit on congenially imputed data.

2. **Variance.** Generalized eigendecomposition of RIV_⊥ = 𝓘^{imp,mis}_{⊥⊥}(𝓘^{imp,obs}_{⊥⊥})^{-1} yields canonical Karhunen–Loève form B̄_∞ = Σ λ_j Z_j². Scaled-shifted correction:
   $$\chi^2_\text{MI,corr} = a\chi^2_\text{MI} + b, \quad a = \sqrt{\frac{2\,\text{df}}{2\,\text{df} + 2\sum_j\lambda_j^2}}, \quad b = \text{df}(1-a)$$
   Drops the EFMI assumption Chan–Meng (2022) retains.

## Lineage

Rubin (1987) → Meng–Rubin (1992, scalar r) → Cavanaugh–Shumway (2001, predictive AIC, target = θ̂_obs) → Chan–Meng (2022, stacked-data LRT + EFMI) → **this work (full eigenspectrum, anisotropic FMI)**.

## Related repos

- `~/git-repositories/MI-IC` — companion SEM methodology paper; v4.5 derivation, `miicsem` package, and SEM simulations live there. JAIGP paper is cited from there.

## Citation discipline (load-bearing)

**Any citation in `manuscript/` must reference a paper whose markdown copy exists at `literature/<citekey>.md` AND has been read in the current session.** Reliance on training-weight knowledge of cited papers is prohibited. The acquisition workflow and enforcement hook are specified in `todo/001-literature-and-hooks.md`.

Rationale: AI-assisted derivations fail in review when citations are hallucinated. The only defense is acquiring actual PDFs and reading them locally before claiming what they say.

If asked to cite something and `literature/<citekey>.md` does not exist, stop and run the acquisition workflow first.

## R style

Inherit `~/.claude/CLAUDE.md` global instructions if computation is added.
