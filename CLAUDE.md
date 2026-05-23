# CLAUDE.md

## Scope

**JAIGP theory paper.** A deviance-bias correction for the Q-function under congenial multiple imputation, with applications to likelihood-ratio model comparison and information-criterion-based model selection. **Reframed 2026-05-22** after reading Chan (2022, *Annals of Statistics*): the original "spectral chi-square correction" framing was preempted; the paper now sits upstream of Chan's test calibration as the deviance-numerator bias correction. See `IDEAS.md` (Reframing note + archive section) for the full provenance.

## Out of scope

**Redirect to `~/git-repositories/MI-IC`:**
- SEM specifics: lavaan, CFI/TLI/RMSEA, saturated SEM imputation, `miicsem` package.
- Congeniality / PMM empirics (separate applied note, not this paper).
- Empirical SEM simulations (Bollen et al. design, Type I tables, etc.).
- Model fit indices in SEM.

**Archived — do not draft from these:**
- Spectral chi-square correction / scaled-shifted form / generalized eigendecomposition of RIV_⊥ — preempted by Chan (2022, AoS). Cite Chan as the canonical reference for non-EFMI test calibration.
- Le Cam-style power-dominance theorem — demoted to a Discussion conjecture; W2 provides partial empirical support.

**Other out-of-scope:** FIML / EM-based observed-data MLE inference (Cavanaugh-Shumway universe — adjacent, not competing); semiparametric / Wald-only variants; Bayes-factor analogues; non-regular settings (boundary, label-switching mixtures).

If the work drifts into any of the above, push it back to MI-IC or cite Chan (2022) and move on.

## Authorship model

AI-assisted derivation, target venue JAIGP (Journal for AI Generated Papers). Provenance is transparent per JAIGP norms. ORCID-verified human prompter: marcus.waldman.

## Core contribution

**Theorem.** Under congenial proper MI with the complete-data MLE as the target, the Q-function deviance bias decomposes as
$$\text{Bias}[\bar Q_\infty(\hat\theta_{\text{obs}})] = +\text{tr}(\text{RIV}) - \tfrac{1}{2}\text{tr}(\text{RIV}) = +\tfrac{1}{2}\text{tr}(\text{RIV}),$$
where the $+\text{tr}$ term is imputation bias and the $-\tfrac{1}{2}\text{tr}$ term is estimation mismatch (MI's target is $\hat\theta_{\text{com}}$, not $\hat\theta_{\text{obs}}$). General for any regular likelihood model fit on congenially imputed data.

**Two applications:**

1. **Likelihood-ratio model comparison (§4).** The LRT numerator $\hat d_L = 2[\bar Q_\infty(\hat\psi^*) - \bar Q_\infty(\hat\psi_0^*)]$ inherits a differential bias $\text{tr}(\text{RIV}(\hat\psi^*)) - \text{tr}(\text{RIV}(\hat\psi_0^*))$. Vanishes at $H_0$; non-zero under local alternatives and non-nested model comparison. Distorts power and ranking even when the reference distribution (Chan 2022 AoS) is correctly calibrated.

2. **Information criteria (§5, headline empirical claim).** MI-AIC and MI-BIC consume $-2\bar Q_\infty$; the bias $-\text{tr}(\text{RIV})$ is **model-specific** (different candidate models have different RIVs). Uncorrected MI-AIC/BIC systematically favor models with **larger** RIV — the downward bias of $-2\bar Q_\infty$ scales with $\text{tr}(\text{RIV})$, making high-RIV candidates look artificially better than they would under complete data. Bias correction restores complete-data-equivalent model selection (same direction as Cavanaugh-Shumway's AICcd, which penalizes high-RIV models with $+2\text{tr}(\text{RIV})$ on top of $2q$).

**Witness apparatus (W1/W2/W3).** Each application is paired with a pre-registered numerical witness (`todo/004-simulation-hypotheses.md`). Predictions written before simulations; framing modifies if reality differs.

## Lineage

Rubin (1987) → Cavanaugh–Shumway (1998, AICcd for EM-based observed-data MLE — *parallel universe, different target*) → Meng (1994, congeniality) → Meng–Rubin (1992) → Claeskens-Consentino (2008, missing covariates) → Chan–Meng (2022, *Stat Sinica*; stacked-data LRT + EFMI) → Chan (2022, *Annals of Statistics*; SMI, drops EFMI, full eigenvalue spectrum, MC reference distribution — **canonical reference for MI test calibration**) → **this work (deviance-bias correction, upstream of all test-calibration work)**.

Chan & Meng (2022) and Chan (2022) handle the reference distribution; we handle the bias of the numerator being referred to it. Both are necessary for complete-data inferential recovery under MI.

## Related repos

- `~/git-repositories/MI-IC` — companion SEM methodology paper; v4.5 derivation, `miicsem` package, and SEM simulations live there. JAIGP paper is cited from there.

## Citation discipline (load-bearing)

**Any citation in `manuscript/` must reference a paper whose markdown copy exists at `literature/<citekey>.md` AND has been read in the current session.** Reliance on training-weight knowledge of cited papers is prohibited. The acquisition workflow and enforcement hook are specified in `todo/001-literature-and-hooks.md`.

Rationale: AI-assisted derivations fail in review when citations are hallucinated. The only defense is acquiring actual PDFs and reading them locally before claiming what they say.

If asked to cite something and `literature/<citekey>.md` does not exist, stop and run the acquisition workflow first.

## Proposing references in conversation

Naming papers in conversation that aren't yet in `literature/` is allowed for planning purposes, **but every such proposal must be logged in `todo/003-references-to-acquire.md` in the same response.** Otherwise proposals leak silently and we end up drafting around references that were never actually acquired.

For each proposed paper, record: (a) approximate citation, (b) the claim it would support, (c) where in the manuscript it would land, (d) priority. Promotion from `proposed → queued → acquired → verified → cited` is tracked in that file. Only `verified` references (markdown read in-session, claim checked against text) are eligible for `@cite` in `manuscript/`.

## R style

Inherit `~/.claude/CLAUDE.md` global instructions if computation is added.
