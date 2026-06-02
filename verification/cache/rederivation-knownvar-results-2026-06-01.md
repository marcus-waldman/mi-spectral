# Known-variance adjudicating experiment — results (2026-06-01)

Execution of the "Adjudicating experiment" in `todo/015-chat-conjectures-reconciliation.md`.
Script: `verification/rederivation-knownvar.R`. Tests **Conjecture C1** (non-universality of the
`+½tr(RIV)` headline) and **C3** (deterministic FIML ≠ proper MI); corroborates **C2**'s
conditional-entropy mechanism.

## Design

Known-variance MVN: `Σ = Σ0` fixed/known (`default_Sigma`), estimate the mean only.
Repo DGP (`gen_data`, `default_mu`) + repo MAR (`apply_mar`: `X1|X3`, `X2|X4` missing; `X3,X4`
always observed). Per replicate, on the same data:

- `θ̂_com` = `colMeans(X)` (complete-data mean MLE, known Σ).
- `θ̂_obs` = closed-form GLS observed-data mean MLE, known Σ
  (`(Σ_i S_i' Σ_OO⁻¹ S_i) μ = Σ_i S_i' Σ_OO⁻¹ y_O`).
- `barQ_fiml(μ_eval)` = `E_{X_mis|Y_obs,θ̂_obs}[ℓ_com(μ_eval;X)]` (deterministic E-step; reuses
  `barQ_fiml_analytic` with Σ0 in both slots).
- `barQ_proper(μ_eval)` = `barQ_fiml − C_n`, `C_n = ½ Σ_i tr(Σ0⁻¹ H_i Φ H_i')`, `Φ = I_obs(μ)⁻¹`
  (analytic `m→∞` proper Q-function; the posterior-draw `μ̃ ~ N(θ̂_obs, Φ)` contribution to the
  imputation covariance). **Validated** by (i) the univariate fully-missing hand-calc `C_n → ½tr(RIV)`,
  and (ii) a built-in MC spot-check averaging `barQ_fiml_analytic` over drawn `μ̃` (R=40, 150 draws:
  `max|analytic − MC| = 0.135`, `mean = 0.046` — pure MC noise).
- `A_* = barQ_*(θ̂_obs) − ℓ_com(θ̂_obs)`, `B = ℓ_com(θ̂_obs) − ℓ_com(θ̂_com)`, `T_* = A_* + B`.
- `tr(RIV)` = μ-block only: `tr(I_com(μ) I_obs(μ)⁻¹) − p`, `I_com(μ)=NΣ0⁻¹`, `I_obs(μ)=Σ_i S_i'Σ_OO⁻¹S_i`.

## Results

`E[·]/target` ratios; SE in parentheses. trRIV is N-stable (≈1.12) — RIV is set by the missingness
fractions, not N. Note **SD(A,T) ∝ √N** (mean-zero cross-terms summed over ~N missing units), so the
N=200 read is the sharpest per fixed R; B and C_n are exact at all N.

| run | trRIV | E[B]/(−½tr) | E[A_fiml]/(½tr) | **E[T_fiml]/(½tr)** | E[A_proper]/(½tr) | **E[T_proper]/(−½tr)** | E[C_n]/(½tr) |
|---|---|---|---|---|---|---|---|
| N=200, R=20000 | 1.123 | 0.997 | 1.083 | **+0.086** | 0.083 | **0.914** | 1.000 |
| N=800, R=20000 | 1.115 | 0.985 | 1.126 | +0.142 | 0.126 | 0.858 | 1.000 |
| **N=200, R=200000** | 1.122 | 0.997 | 1.042 | **+0.045** | 0.042 | **0.955** | 1.000 |

Tightest run (N=200, R=200000, SE≈0.018 on A/T, SE≈0.0015 on B, SE≈0.0002 on C_n):

```
mean tr(RIV_mu) = 1.1222   (½ trRIV = 0.5611)
E[B]        = -0.5597 (SE 0.0015)   ratio B/(-½ trRIV) = 0.997
FIML  : E[A] = +0.5848 (SE 0.0181)  ratio A/(½ trRIV) = 1.042
        E[T] = +0.0251 (SE 0.0179)  T/(½ trRIV) = +0.045   <-- ~0, NOT +1
proper: E[A] = +0.0237 (SE 0.0181)  ratio A/(½ trRIV) = 0.042  <-- ~0
        E[T] = -0.5360 (SE 0.0179)  T/(-½ trRIV) = 0.955    <-- -½ trRIV, NOT +½
E[C_n] (FIML-proper gap) = +0.5611 (SE 0.0002)  ratio = 1.000  <-- exactly ½ trRIV
DISCRIMINATING: FIML T/(+½trRIV)=+0.045, proper T/(+½trRIV)=-0.955  (universal would be ~+1.0)
```

Caches: `verification/cache/rederivation-knownvar-N{200,800}-R{20000,200000}.rds`.

## Verdict against the decision gates

- **C1 (non-universality) — CONFIRMED.** Known-variance `E[T]` is `≈0` (FIML) / `−½tr(RIV)` (proper);
  **neither is `+½tr(RIV)`**. The contrast with the unknown-Σ baseline (`E[T]≈+½tr(RIV)`,
  `rederivation-L0-fitted-vs-oracle.R`) is decisive. The manuscript's "`+½tr(RIV)` for *any* regular
  likelihood fit" is an overreach: it requires the conditional (missing-data) entropy to depend on the
  estimated parameters — i.e. (co)variance/scale estimation. **Action: restate theorem scope.**

- **C3 (FIML ≠ proper) — CONFIRMED.** FIML and proper differ by **exactly** `C_n = ½tr(RIV)`
  (ratio 1.000, SE 2e-4): `E[T_fiml]=0` vs `E[T_proper]=−½tr(RIV)`. The "deterministic FIML = proper MI"
  equivalence is false off the estimated-(co)variance regime. **Action: scope the FIML/proper equivalence
  to the regime where it holds; soften the `00-setup.R`/D9 "[mc] equal" comments.**

- **C2 (Δ_n conditional-entropy reframing) — mechanism CORROBORATED.** With Σ known, the conditional
  entropy `H_θ(Y_mis|Y_obs)=½log|2πe Σ_MM·O|` is θ-free ⇒ `Δ_n=0` ⇒ `E[T_fiml]=0`, exactly as observed.
  The full analytic identity `Δ_n = ½tr(RIV)+(A)+(C)` for unknown-Σ MVN remains a separate symbolic task.

- **Finite-n note.** A tiny positive residual `E[T_fiml]≈+0.025` at N=200 (≈4.5% of ½trRIV; ~1.4 SE)
  shrinks with R toward 0 and is plausibly a small `O(1/n)` partial-MAR `(A)+(C)`-type term. It is
  negligible against the `+0.56` that universality would require and does not affect the verdict.

## Bottom line for the paper

The `+½tr(RIV)` headline **survives for the paper's actual regime** — estimated-covariance MVN, which
is where the **IC application (§5 / W3)** lives (MI-AIC/BIC over MVN models with estimated Σ). What
fails is the *universality* phrasing ("any regular likelihood"). Restate the theorem to require
parameter-dependent conditional (missing-data) entropy — concretely, (co)variance/scale estimation —
and note the known-scale/mean-only collapse (`E[T]=0` FIML / `−½tr(RIV)` proper).
