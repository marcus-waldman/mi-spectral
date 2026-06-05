# Todo 028 — Handoff: the non-nested (Vuong-regime) measurement cell — CS vs AR(1)

**Status: EXECUTED 2026-06-04** (next-session focus, done same day). Preregistered (`todo/029`,
committed alone `7677777` before any engine code), CAS-blessed (`verify_w4_nonnested.py` ALL PASS),
engine built (`w4-nonnested-vuong.R`, smoke-validated), pilots → power gate (dated Amendment 1,
recalibrated 0.25→O(1) MDE, R=20,000, commit `99c7fd4`), graded run (240k replicates, 0 errors, all
asserts pass), landed in `@sec-lrt-ac`/`@sec-ic` + mi-spectral §5/§6. **Result (todo/029 §6):** the
$(A)+(C)$ *level* is a large O(1) (~+2.5 per curved candidate, up to 37 se) that collapses under MCAR
and *decouples* between CS/AR1; the paired noise returns to O($\sqrt n$) (for any pseudo-true-separated
pair, nested-but-false included — separation, not nesting, governs); the naive trace overstates the
exact $\operatorname{tr}(\mathrm{RIV}_\perp)$ by ~9% per curved candidate (first in-vivo off L2's
equality). **The headline (a *resolved* nonzero $(A)+(C)$ *differential*) was NOT met** — for the
similar CS-vs-AR1 pair the two large levels nearly cancel, differential consistent with 0 (≤1.5 se,
below ~0.5 resolution at N=2000; the pilot's −2 was MC noise). Framing modified per discipline: the
differential is real per candidate but mild for similar candidates, scaling with dissimilarity (the
dissimilar-pair magnitude → pairwise-matrix sequel, todo/023). Original handoff text preserved below.

**Original handoff.** Closes the only derived-but-never-measured quantitative claim in the paper
(M3: the $(A)+(C)$ differential returns as a genuine $O(1)$ for non-nested comparison —
Proposition L4 / `@sec-lrt-ac`; consumed un-absorbed by IC ranking per `@sec-lrt-consequences`
and `@sec-ic-criterion`).

**Sequencing discipline (lesson from todo/027's provenance note):** the preregistration
(new `todo/029`, predictions + pass criteria + power gate) is written AND **committed before
the first line of script code**. Then build, pilot, set R by the power gate, run, grade.

## The design (user-selected pair: compound symmetry vs AR(1))

- $p = 4$ MVN; candidates fit by constrained $\bar Q$-maximization on the E-step moments at
  the saturated FIML fit (the ic-ladder.R construction):
  - **CS**: $\Sigma = \sigma^2[(1-\rho)I + \rho J]$ — CLOSED FORM given $(m^*, S^*)$
    (project onto the $J$-eigenframe: $\hat a = \mathbf{1}'S^*\mathbf{1}/p$ on the rank-1
    eigenspace, $\hat b = \operatorname{tr}(QS^*)/(p-1)$ on the complement).
  - **AR(1)**: $\Sigma = \sigma^2 R(\rho)$, $R_{ij} = \rho^{|i-j|}$ — 1-D profile over
    $\rho \in (-1,1)$ ($\hat\sigma^2(\rho) = \operatorname{tr}(R^{-1}S^*)/p$;
    $|R| = (1-\rho^2)^{p-1}$; tridiagonal inverse). `optimize()`.
  - Both 6 params (4 $\mu$ + 2) ⇒ **ΔAIC = ΔT exactly** (penalty cancels; pure Vuong setting).
  - **Independence** ($\rho = 0$, 5 params) is nested in BOTH — the internal nested control
    pair on the same data/imputations.
- No lavaan in the candidate loop ⇒ per-replicate cost ~ms ⇒ brute R feasible (10–20k),
  which is REQUIRED: in the non-nested regime the paired noise is $O(\sqrt n)$ *by the claim
  under test* — pairing cannot remove it; precision is bought with R.
- Saturated anchoring as in ic-ladder.R: $T_k = N[\log|\hat\Sigma_k| + \operatorname{tr}(\hat\Sigma_k^{-1}S^*) - \log|S^*| - p]$
  (the trace term no longer cancels for curved candidates — keep the full form, $T_k \ge 0$).
- $\operatorname{tr}(\mathrm{RIV}_{\perp,k})$ and the null-law spectrum need the
  **general-Jacobian** version of the ladder machinery ($G_k$ = analytic
  $\partial(\mu, \operatorname{vech}\Sigma)/\partial(\mu, \sigma^2, \rho)$ — closed form for
  both candidates; the CAS file's L-A3 already covers generic full-rank $G$).

## Cells

| Cell | Truth | Mechanism probe |
|---|---|---|
| A | AR(1), $\rho = 0.5$ | true vs $O(1)$-misspecified (clean Vuong regime) |
| B | Toeplitz tuned so $KL(\text{truth}\|\text{CS}^*) = KL(\text{truth}\|\text{AR1}^*)$ | **money cell**: complete-data selection ≈ coin flip; the MI $O(1)$ differential shifts it — the M3 decision-level punchline |
| A′, B′ | same truths, **MCAR** | $(A)+(C) = 0$ ⇒ residual should collapse — isolates the design-imbalance mechanism from generic non-nested $O(1)$s |

- Missingness for A/B: the **X1-heavy MAR** design (`w2-paired-differential-mu1-cell.R`
  amputation — strongest imbalance generator; $(A)+(C)$ levels are small, the differential
  needs it). N ∈ {500, 1000, 2000}.
- **Vuong caveat (load-bearing):** CS and AR(1) OVERLAP at $\rho = 0$; near the intersection
  the LR limit degenerates. Truth must keep both pseudo-true $\rho$'s well away from 0; the
  prereg states the pseudo-true values and the separation explicitly (compute them
  numerically from the population moments before freezing).

## Measurands and pass-criteria shape (to be frozen in todo/029)

1. **The O(1) residual:** paired mean of $(\Delta T_{\text{MI}} - \Delta T_{\text{com}})$
   minus $[\operatorname{tr}(\mathrm{RIV}_{\perp,\text{CS}}) - \operatorname{tr}(\mathrm{RIV}_{\perp,\text{AR1}})]$.
   Pass shape: nonzero at ≥ 3 se; **un-trending across N** (O(1) not o(1)); ≈ 0 for the
   nested control pair in the same run; collapses under MCAR (A′/B′ vs A/B).
2. **Noise order:** sd of the paired differential $\propto \sqrt n$ for the non-nested pair,
   flat for the nested control (the L3 boundary, measured from both sides in one run).
3. **Decision distortion (cell B):** P(select CS) under corrected MI-AIC vs complete-data
   AIC — the trace correction does NOT remove the gap (prereg the direction once the sign of
   the differential is derived/piloted; if the sign is not derivable cheaply, prereg
   two-sided ≥ 3 se).
4. **L2 in-vivo bonus (report):** naive vs $I_{\text{com}}$-metric trace per candidate —
   these CURVED candidates should sit OFF the equality case (unlike the W3 zero-patterns);
   report the gap and, if material, the selection consequence of using the naive trace.

## Risks / gates

- **Power:** the $(A)+(C)$ differential magnitude is unknown (levels ≈ −0.3; the
  differential could be smaller or larger — the O(1) pseudo-true separation enters the
  entropy-gradient contractions). Prereg includes a PILOT-based power gate: estimate
  sd(paired diff) at N=500 small-R, choose R for ≥ 3-se resolution of a 0.25-sized effect,
  THEN freeze and run. If the gate says infeasible at sane R, record that and re-scope
  (e.g., strengthen imbalance) as a dated amendment BEFORE unblinding means.
- Pseudo-true computation: population $S_\infty$ per cell → constrained fits on it →
  KL values; cell B's Toeplitz tuned by 1-D search on the equal-KL condition. All analytic /
  deterministic; goes in the prereg.
- Scope: ONE focused measurement for the paper's M3 (lands as a short addition to
  `@sec-lrt-ac` / `@sec-ic` + a paragraph in mi-spectral.qmd §5). The full pairwise-matrix
  testbed stays sequel (todo/023).
- Optional cell 0 (cheap pilot): MB-vs-MC from the W3 family under X1-heavy MAR (zero new
  fit code; but both are zero-patterns at the L2-equality case and symmetry may suppress the
  differential — treat as exploratory only, not the headline).

## Also queued for that session (carried from 2026-06-04)

- Mode-B exact-gap remark in `@sec-lrt-naive` + CAS A5 extension (cheap, sharpens L2).
- One sentence grading the impossibility statement's evidence level in `@sec-ic`.
- Then: mi-spectral.qmd §3–§6 drafting + the three `@TODO` resolutions (in-session reads).

*Handoff captured 2026-06-04 at the end of the IC-landing session (user decision: non-nested
measurement is the next session's focus; CS-vs-AR(1) is the user-selected pair).*
