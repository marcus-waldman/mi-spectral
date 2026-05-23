# Todo 002 — Verification implementation (read Chan–Meng *very* carefully)

**Status:** Open. Blocks any quoted Type I number in the manuscript.

## Why this matters

The paper's headline empirical claim is that the spectral correction restores nominal Type I where Chan–Meng (2022) does not, under anisotropic $\text{RIV}_\perp$. That claim is only meaningful if our simulation compares to **Chan–Meng's actual test**, including their reference distribution and degrees-of-freedom adjustments — not a sloppy approximation.

Two failure modes if we get this wrong:

1. **Conflating reference-distribution miscalibration with EFMI-violation miscalibration.** If we compare $D_3$ or stacked-LRT to a plain $\chi^2(\text{df})$ when the source paper specifies a particular $F$ distribution with specific df adjustments, our reported Type I inflation lumps together "wrong reference" and "wrong assumption." Reviewers will catch this and demand re-runs. Worse — the paper's contribution shrinks if a fraction of the inflation we attribute to anisotropy is actually a coding error.

2. **The MI-IC v4.x simulations may have this exact problem.** The earlier exploratory Type I numbers (saturated 16.6%, PMM 16.3%, congenial mvn_M1 4.8% — see MI-IC's flexibility-gap brief) were collected before the Chan–Meng paper was on the radar in this project. Whether those tests used Chan–Meng's reference distribution or an older Meng–Rubin / Schafer–Reiter F-approximation is **unverified**. Those numbers cannot be borrowed into this paper without re-checking — and that's a separate, MI-IC-scoped task.

## What we need to do before writing any simulation

Read each source paper for the comparison statistics we'll run, and implement to spec:

| Statistic | Source | What to verify | Reference distribution |
|---|---|---|---|
| $D_3$ | Meng & Rubin (1992) §3 | The combining rule for $\bar d_L$ and $r_L$ exactly as in their eqs (3.7)–(3.8) | Their $F_{k, w(r_L)}$ with $w(r)$ defined in eq (2.7) |
| $\hat{D}_L^\diamond$ (Chan-Meng) | Chan & Meng (2022) | Stacked-data LRT $\hat{d}_L = 2\{\bar{L}(\hat{\psi}^*) - \bar{L}(\hat{\psi}_0^*)\}$ where $\bar L = m^{-1}\sum_\ell L^{(\ell)}$. Statistic $\hat{D}_L^\diamond = \hat{d}_L / [k(1+\hat{r}_L^\diamond)]$ with $\hat{r}_L^\diamond = \frac{m+1}{h(m-1)}(\bar\delta_L - \hat\delta_L)$. **Requires EFMI on full $\psi$** (Assumption 4: $\mathcal{I}_\psi = (1+r)\mathcal{U}_\psi$). | **$F_{k, \widehat{df}(\hat{r}_L^\diamond, h)}$** where $\widehat{df}(r_m, h) = h(m-1)/f_m^2$ and $f_m = r_m/(1+r_m)$ — confirmed from §2.3, equation (2.15). The exact limit (Theorem 4) is $(1+r_m)M_1/(1+r_m M_3)$ with $M_1 \sim \chi^2_k/k$ and $M_3 \sim \chi^2_{h(m-1)}/\{h(m-1)\}$. F-approximation matches first two moments of the denominator. |
| $\hat{D}_L^+$ (Chan-Meng alternative) | Chan & Meng (2022) | Uses $\hat{r}_L^+ = \max(0, \hat{r}_L)$ instead of $\hat{r}_L^\diamond$. $\hat{r}_L$ depends only on $\theta$ (the tested parameter), not full $\psi$ — does not require EFMI but loses consistency under $H_1$. | $F_{k, \widetilde{df}(\hat{r}_L^+, k)}$ — Li-Meng-Raghunathan-Rubin (1991) df formula. |
| Spectral correction | This work | $\chi^2_{\text{MI,corr}} = a\chi^2 + b$ with $a, b$ matching first two moments via $\{\lambda_j\}$ | Approximated $\chi^2(\text{df}^*)$ via scaled-shifted theory |
| Complete-data oracle | Standard | LRT under no missingness | $\chi^2(\text{df})$ |

For each: a small unit-test that reproduces a published-value or known-distribution result before we trust it for our headline simulation. E.g., reproduce Meng & Rubin's contingency table example (eq 4.4, Table 2) for $D_3$; reproduce a worked example from Chan & Meng (2022) for stacked LRT.

## Specific reading queue (in order)

1. **`literature/chanMultipleImprovementsMultiple2022.md` — DONE (cold read 2026-05-22).** Reference distribution confirmed as $F_{k, \widehat{df}(\hat{r}_L^\diamond, h)}$ with $\widehat{df} = h(m-1)/f_m^2$ where $f_m = r_m/(1+r_m)$ is the finite-$m$ corrected FMI. Test statistic is $\hat{D}_L^\diamond = \hat{d}_L / [k(1+\hat{r}_L^\diamond)]$ with the stacked-data LRT $\hat{d}_L$. **EFMI on full $\psi$ is assumed (Theorem 2/4); they acknowledge violation degrades performance — see Chan (2021) below.**
2. **Chan, K. W. (2021) "General and feasible tests with multiply-imputed datasets" *Ann. Statist.* — NOT YET ACQUIRED. URGENT.** Chan-Meng (2022) explicitly cite this as the "possible remedy" for the EFMI violation regime, which is precisely mi-spectral's target. Must read before finalizing §1 contribution claims; could be the closest known predecessor and may reshape what we're claiming as novel.
3. `literature/mengPerformingLikelihoodRatio1992b.md` — refresh on $D_L$ / $\tilde{r}_L$ formulas (which Chan-Meng built on). Reproduce their Table 2 (contingency-table example) as a smoke test.
4. `literature/li1991significance.md` — Li-Meng-Raghunathan-Rubin (1991, Stat Sinica). Original $\widetilde{df}$ formula in (1.6), which Chan-Meng's $\widehat{df}$ improves on. Reference for $F_{k, \widetilde{df}(\hat{r}_L^+, k)}$.
5. `literature/li1991large.md` — Li-Raghunathan-Rubin (1991, JASA). The $D_m$ moment-based Wald test. Useful as another comparator and for understanding the F-reference history.

## Implementation guardrails

- One R function per comparator, in `verification/00-comparators.R`. Each function takes the per-imputation log-likelihood values (and any auxiliary quantities the test needs) and returns `list(statistic = ..., df_num = ..., df_den = ..., p_value = ...)`. Forces explicit specification of which reference distribution is being used.
- A test harness `verification/00-test-comparators.R` that runs each comparator on a synthetic complete-data scenario (no missingness) and verifies the test reduces correctly to its no-missing limit.
- Smoke test: reproduce Meng-Rubin Table 2 numbers exactly. If we can't, the implementation is wrong.

## Adjacent concern — out of scope for this paper

The MI-IC SEM simulations may also have this issue. Whether to re-run them with proper Chan-Meng reference distribution is **MI-IC's call**, not ours. Flag in MI-IC's todo but do not block on it here.
