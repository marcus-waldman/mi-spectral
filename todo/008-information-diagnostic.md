# Todo 008 — Finite-sample information diagnostic (expected vs sample RIV)

**Status:** Exploratory / post-hoc (NOT pre-registered). Folded into the comprehensive
battery as **Phase 6** of `verification/run_all.R`
(`_modules/w1-information-diagnostic.R`, output `cache/run_all-<suffix>/phase6-info/`).
Surfaced 2026-05-30/31 while interrogating the W1 finite-sample remainder.

> **⚠ SUPERSEDED (2026-05-31).** The "two finite-sample RIVs (A→expected, B→sample)" framing
> in **"What it establishes"** below (and its "headline numbers") is **retired**. The rate
> study + MCAR control + analytic `E[r_P]` + the decisive A-vs-RIV check established that there
> is **ONE correct RIV** — the observed-data RIV with the MAR cross term — and both A and B
> track it. The apparent split was an artifact of grading against `fisher_info_obs_mvn`, which
> is **block-diagonal (as-if-MCAR) and incomplete under MAR**. Read the **"UNEXPECTED finding"**
> section onward as the current understanding; the top sections are kept only as the trail.

## What it establishes

The W1 theorem's per-term identities (`E[A]=+tr(RIV)`, `E[B]=-½tr(RIV)`) hold to leading
order against the **expected-information** RIV, but the two terms calibrate to **different
finite-sample RIVs**:

1. **A (imputation bias) → expected-information RIV** `tr(I_obs⁻¹ I_mis)`. A consumes
   `Var(θ̂_obs)`, which equals `I_obs⁻¹` even at finite n (well-behaved).
2. **B (estimation mismatch) → sample / observed RIV** (Rubin between/within ≈ observed-
   information). B consumes `Var(θ̂_obs − θ̂_com)`, whose asymptotic identity
   `I_obs⁻¹ − I_com⁻¹` (derivation Lemma L2) is finite-sample **inflated** by ~10% at n≤2000.
3. **Information equality holds** — `tr(𝒥̂ 𝓘⁻¹) ≈ k` (correct specification). So the split is
   the **finite-sample (Efron–Hinkley)** face of the J-vs-I distinction, **not** the
   misspecification (TIC/Pawitan §13.6) face.
4. **T = A + B** therefore sits below `½tr(RIV)` at finite n by ≈ `½(tr_samp − tr_exp)`,
   closing only as the Efron–Hinkley gap closes (slowly — empirically slower than O(n⁻¹)).
5. **Engine-independent**: proper MI (Amelia) gives the same picture as deterministic FIML;
   proper MI even *lowers* A slightly vs FIML (Jensen — dispersed imputations averaged
   through the concave complete-data loglik), so posterior draws do not push A onto the
   sample RIV.

This refutes the earlier "individual terms ~10–20% off but residuals cancel so T holds"
story (derivation.qmd note after `@eq-combine`) — T does **not** exactly hold at finite n;
the deviation is the expected-vs-sample information gap. Drives the derivation edits
(define both informations, state which variance each term consumes, correct that note).

## Headline numbers (high-R reference; apply_mar, RB-A)

Proper-MI (Amelia M=80), N=2000, R=40000:

| | A_proper | A_FIML | B | T_proper | tr_exp | tr_samp |
|---|---|---|---|---|---|---|
| mean | 5.36 | 5.62 | −3.03 | 2.33 | 5.51 | 6.09 |

- `A_proper − tr_exp ≈ −0.15` (≈0); `A_proper − tr_samp ≈ −0.73` (and not closing) → A tracks **expected**.
- `B + ½tr_samp ≈ +0.01` (B tracks **sample**); `B + ½tr_exp ≈ −0.27` (off).
- `T_proper − ½tr_exp ≈ −0.43`, not closing over n≤2000.
- proper − FIML A ≈ −0.26 (robustly negative, ~10σ; Jensen).

J-vs-I check (R=4000): `tr(𝒥̂ 𝓘_obs⁻¹) ≈ 13.9 ≈ k=14` (info equality); `tr(I_obs·Var̂(θ̂_obs)) ≈ 14.3`
(θ̂_obs variance clean); `tr(I_com·Var̂(gap)) ≈ 6.0` vs expected `5.5` — the inflation lives in
the **gap** variance (Lemma L2 / the `Cov(θ̂_obs,θ̂_com)=I_com⁻¹` step), not in `Var(θ̂_obs)`.

## Rejected — do NOT re-attempt

**Control variate (b): regress A on the score at θ_true.** Reduces variance (residual sd flat
~3.4 across N) but is **biased ~+0.25 (≈9σ at R=15k)** because A is *quadratic* in θ̂_obs and a
linear regression on the score cannot preserve the quadratic's mean when the score→θ̂ map is
random. Use plain brute force (unbiased) for E[A]/E[T] precision. Confirmed 2026-05-31.

## Reproduce

```
Rscript verification/run_all.R 2000 prod "6,5" 20   # phase 6 + aggregate fold-in
```

Phase 6 is MAR cells only (congenial regime), 2 patterns × N∈{200,500,1000,2000}, Amelia M=50,
info-equality on a capped subset (score_cap=600). Self-contained verdicts; aggregate (phase 5)
folds the `INFO` row into `phase5/verdicts.md` when both run.

## Rate-of-decay study (phase 7, design — settled 2026-05-31)

Turns the "the expected-vs-sample (Efron–Hinkley) gap closes *slowly*, not as a clean
O(n⁻¹)" claim (derivation.qmd `@eq-combine` note + Appendix C) from **eyeballed** into
**fitted**.

**Estimand.** The decay exponent `b` in `gap(N) = tr_samp(N) − tr_exp(N) ≈ c·N^b`
(`b = −1` ⇒ O(1/n); `b = −1/2` ⇒ O(1/√n)).

**Design.**
- **Fixed log-spaced N grid** (~10 points, 200 → 10⁴): `round(exp(seq(log(200), log(1e4), length=10)))`.
  Log- not linear-spacing: the regressor is `log N`, so even spacing in `log N` balances
  leverage; uniform-in-N starves the small-N end. **Fixed grid, not per-rep random N**, so we
  can **average per N before logging** — this avoids (i) the Jensen bias `E[log|ρ|] ≠ log E[ρ]`
  (which is N-dependent and would tilt the slope) and (ii) the `log` of near-zero/negative
  single-rep remainders. Per-rep random log-uniform is statistically ≈ an equi-spaced grid for
  the slope anyway (same `Var(log N)` per total reps), with no offsetting benefit here.
- **R reps per N** → precise per-N mean + MCSE.
- **WLS log-log:** `log(mean_gap_N) ~ log(N)`, weights `(mean_gap / MCSE)²` (delta-method
  precision of the log mean; per-N MCSE is heteroskedastic in N). Slope = `b`, with 95% CI.
- **Target the gap** (positive, low-variance, analytic ⇒ `log` well-defined). A/B/T remainders
  are reported per N descriptively but **not** rate-fit (A/T are MCSE-limited, sd ∝ √N, and
  cross zero ⇒ `log|·|` unstable).
- **Engine: FIML / analytic** — the gap needs only the FIML fit `θ̂_obs` +
  `tr_riv_analytic` (expected) + `tr_riv_observed_general` (observed); no imputations, no
  numerical derivatives, so a long grid + large R is cheap. Both patterns, MAR.

**Output.** Per-(pattern, N) means + MCSE for `tr_exp, tr_samp, gap, A, B, T`; per-pattern
fitted gap exponent `b` + CI. Module `_modules/w1-rate-decay.R`, run_all **phase 7**.

### Result + UNEXPECTED finding (run 2026-05-31, R=2000, N=200..10⁴, extended to 3×10⁵)

Fitted gap-decay exponents: non_monotone `b = −0.066` (95% CI [−0.098, −0.033]), monotone
`b = −0.027` ([−0.043, −0.010]). But the gap does **not** decay to zero — it **plateaus** at a
nonzero constant (~0.557 non_monotone, ~0.443 monotone), flat across N = 10⁴ → 3×10⁵
(0.554 → 0.549; O(1/√n) would have driven it to ~0.18). The tiny exponents are a small-N
transient + a nonzero asymptote, **not** a power-law decay to zero.

**Not expected.** The observed-data MVN likelihood is correctly specified, so its observed
information should → its expected information and the gap → 0. It doesn't.

**Localization** (observed vs expected info, block-wise, mean over 20 reps):

| N | mean_rel | cov_rel | cross_rel |
|---|---|---|---|
| 1000 | 0.000 | 0.023 | 0.068 |
| 10000 | 0.000 | 0.012 | 0.065 |
| 100000 | 0.000 | 0.009 | 0.065 |

mean block identical; cov block → 0; the **mean × vech-Σ cross block is persistent (~6.5%, flat,
O(n))** — it is the entire gap.

**Mechanism (hypothesis — needs analytic confirmation).** `fisher_info_obs_mvn` is
**block-diagonal**: it sets the mean–covariance cross block to 0. Under **MAR**, missingness
depends on observed values, so within each pattern the observed-variable means are
systematically shifted from the marginal means ⇒ the per-pattern residual sum
`r_P = Σ(yᵢ^O − μ_O)` has **nonzero expectation** (O(n), not an O(√n) fluctuation — hence the
flat `cross_rel`). That `E[r_P] ≠ 0` puts a genuine cross term in `E[−∂²ℓ_obs]` that the
block-diagonal form omits; it should vanish under **MCAR** (`E[r_P]=0`). `observed_info_obs_mvn`
(validated vs numerical Hessian to 5e-7) includes it.

**MCAR control CONFIRMS the mechanism (2026-05-31).** Same non-monotone pattern + same ~31%
marginal missing rate, toggling only the selection (`apply_mar` b=0 ⇒ MCAR vs b=0.4 ⇒ MAR):

| mech | N | gap | cross_rel |
|---|---|---|---|
| MCAR | 1000 / 10000 / 100000 | 0.035 / 0.005 / −0.002 | 0.014 / 0.004 / 0.001 |
| MAR  | 1000 / 10000 / 100000 | 0.540 / 0.483 / 0.494 | 0.059 / 0.059 / 0.057 |

Under MCAR the gap and cross block → 0 (observed → expected, standard theory holds); under MAR
both persist, flat. So `fisher_info_obs_mvn` is the correct expected info under MCAR but
**incomplete under MAR** (omits the selection-induced cross term).

**Analytic confirmation (2026-05-31).** `apply_mar` sets R1=1 (X1 missing) iff `S1 := V1 − b·X3 < a`
(`V1~N(0,1)` indep), so selection is on a Gaussian correlated with the data through `−b·X3`. The
selected-Gaussian moment gives the per-pattern mean shift in closed form:
`E[Xₖ | R1=1] = (b·Σₖ₃ / √(1+b²)) · λ(a/√(1+b²))`, `λ(z)=φ(z)/Φ(z)` (inverse Mills). Validated vs
empirical (N=4×10⁶) to 3 decimals: MAR (a=−0.5, b=0.4) → [X1,X2,X3,X4] = [0.124, 0, 0.414, 0.207]
(empirical [0.124, 0.000, 0.415, 0.208]); MCAR (b=0) → 0. The shift is `∝ b·(Σ-coupling)·λ` —
nonzero under MAR, exactly 0 under MCAR — confirming `E[r_P] ≠ 0` under MAR and hence the genuine
cross term in `E[−∂²ℓ_obs]`. (Two-selection patterns P1/P2/P3 use the bivariate-selection analog;
not yet written out, but the single-selection result establishes the mechanism + closed form.)

**Implications — OPEN, do NOT write into manuscript/derivation until resolved:**
- The "expected RIV" benchmark used throughout W1 (`fisher_info_obs_mvn`) may be an
  **incomplete** observed-data information under MAR (missing the cross term). The
  observed-information RIV is the cross-inclusive one, and **B tracks it** (B = −4.08 ≈ −½·8.18
  at N=10⁴, not −½·7.63).
- This may reframe the two-RIV story (derivation.qmd two-RIV callout + Appendix C) from
  "Efron–Hinkley observed-vs-expected, vanishing as n→∞" to "`fisher_info_obs_mvn` omits a real
  MAR cross term." **The committed derivation edits (09291e0) are under review.**
- Resolution path: (1) derive `E[r_P]` under the MAR mechanism analytically (confirm ≠0 under
  MAR, =0 under MCAR); (2) decide which information the theorem's RIV should use; (3) re-examine
  the earlier "A→expected, B→sample" split (A may have tracked the incomplete benchmark).

### DECISIVE A-vs-RIV check — it is ONE RIV (2026-05-31)

Does `E[A]` track the correct/observed RIV (`tr_samp`) or the incomplete block-diagonal one
(`tr_exp` = `fisher_info_obs_mvn`)? High-R Rao-Blackwellized A, ampute non_monotone MAR 40%,
R=12000:

| N | E[A_rb] (MCSE) | E[A_noisy] | tr_exp | tr_samp | A_rb − tr_exp | A_rb − tr_samp |
|---|---|---|---|---|---|---|
| 200 | 8.734 (0.101) | 8.726 | 7.707 | 8.561 | **+1.027 (≈10σ)** | +0.173 (1.7σ) |
| 1000 | 7.968 (0.190) | 8.316 | 7.646 | 8.253 | +0.322 | −0.285 |

At N=200 (tight MCSE, gap 0.85) A is **~10σ from `tr_exp`** and consistent with **`tr_samp`**;
at N=1000 (looser MCSE) A straddles `tr_samp` (A_noisy 8.316 ≈ tr_samp 8.253). So **A tracks the
correct observed-information RIV, not the block-diagonal one** — and B already tracked `tr_samp`.

**Resolution — there is ONE RIV.** Both `A = +tr(RIV)` and `B = −½tr(RIV)` calibrate to the same
**correct observed-data RIV** `I_obs⁻¹ I_mis`, with the **cross-inclusive** `I_obs =
observed_info_obs_mvn` (= `tr_samp`). The earlier "A→expected / B→sample" two-RIV split was an
**artifact** of grading against `fisher_info_obs_mvn` (block-diagonal = as-if-MCAR = incomplete
under MAR). The theorem holds cleanly: `E[T] = +½ tr(RIV)` against the correct RIV.

**Consequences for the paper (pending lit check on novelty):**
- The RIV in the theorem and the IC correction must use the **observed-data information**
  (`tr_riv_observed_general`), not the block-diagonal `tr_riv_analytic` / `fisher_info_obs_mvn`.
- The two-RIV callout (`#sec-two-rivs`) + Appendix C "Efron–Hinkley observed-vs-expected"
  framing in `derivation.qmd` (commit 09291e0) is **retired** — no two RIVs, no finite-sample
  E–H gap; one correct RIV, and the block-diagonal form is just the wrong (MCAR-only) information.
- W1's "expected RIV" benchmark (block-diagonal) should be re-pointed to the observed-data RIV.
- **Open (→ lit check):** is "the observed-data information under MAR ≠ the per-pattern
  block-diagonal form; it carries a selection-induced mean–covariance cross term" a known result
  (Kenward–Molenberghs / FIML-information literature) or novel? Determines footnote vs contribution.

## References (acquired this session — see todo/003)

- `efronAssessingAccuracyMaximum1978` — observed vs expected Fisher information
- `pawitanAllLikelihoodStatistical2013` — 𝒥/𝓘, sandwich, 𝒥=𝓘 under correct spec, `tr(𝒥𝓘⁻¹)`
- `konishiGeneralisedInformationCriteria1996` — GIC/TIC under misspecification
