# C2 — analytic reconciliation: `E[T] = Δ_n` and `Δ_n = ½tr(RIV) + (A)+(C)`

**Date:** 2026-06-02. Executes `todo/017-c2-deltan-entropy-reconciliation.md`.
**Outcome:** CONFIRMED (two CAS + MC). The manuscript's `(A)/(B-main)/(C)` split and the
conditional-entropy `Δ_n` story are the *same total*, regrouped. `+½tr(RIV)` kept as the headline
(author intent); a one-paragraph reconciliation remark added to `derivation.qmd`.

## Objects

For the unknown-`(μ,Σ)` MVN, the per-unit conditional of the missing block given the observed block
is Gaussian, `Y_M | Y_O = y ~ N(m_θ, S_θ)` with `m_θ = μ_M + Σ_MO Σ_OO⁻¹(y−μ_O)`,
`S_θ = Σ_MM − Σ_MO Σ_OO⁻¹ Σ_OM`. Define the one bivariate seed function

> `F(φ, ψ) = E_{Y_M ~ p(·|y; φ)} [ log p(Y_M | y; ψ) ]`
> `        = −½ log|2π S_ψ| − ½ tr(S_ψ⁻¹ S_φ) − ½ (m_φ − m_ψ)ᵀ S_ψ⁻¹ (m_φ − m_ψ)`,

the expected log conditional density when the completion is **drawn** at `φ` and the density is
**evaluated** at `ψ`. Three slices of the one surface:

| object | definition | role |
|---|---|---|
| cross-entropy | `f₀(φ) = F(φ, θ₀)` | draw varies, eval pinned at truth → Term-A imputation slot |
| (neg.) expected loglik | `g₀(ψ) = F(θ₀, ψ)` | draw pinned at truth, eval varies → standard MLE slot |
| (neg.) conditional entropy | `C_n(θ) = F(θ, θ)` | both move together → the entropy plug-in object |

For the Gaussian, `C_n(θ) = −½ Σ_i [ |M_i| log 2πe + log|S_{θ,i}| ]` — depends on θ **only through Σ**
(via the conditional/Schur covariance `S_{θ,i}`), not through μ. The conditional-entropy plug-in bias is

> `Δ_n = E[ C_n(θ̂_obs) − C_n(θ₀) ]`.

`α = ∇f₀(θ₀) = −E'(θ₀)` is the entropy gradient (A3); `H_φ = ∇²f₀(θ₀)` the cross-entropy curvature
(the lemma's imputation-slot Hessian); `I_mis|obs = E_{θ₀}[S_mis|obs S_mis|obsᵀ]` the conditional
Fisher information; `RIV = tr(I_obs⁻¹ I_mis|obs)`.

## The two operator identities (the whole substance)

A second-order Taylor expansion of `Δ_n = E[C_n(θ̂_obs) − C_n(θ₀)]` in `δ = θ̂_obs − θ₀` reduces the
target scalar to two derivative identities of `C_n` at the truth:

**(I1) Gradient.** `∇C_n(θ₀) = α`.
Chain rule on `C_n(θ)=F(θ,θ)`: `∇C_n = ∇_φF + ∇_ψF`. The eval-slot gradient `∇_ψF(θ₀,θ₀)=∇g₀(θ₀)=0`
(Gibbs: `E_{θ₀}[S_mis|obs]=0`), leaving `∇C_n(θ₀)=∇_φF(θ₀,θ₀)=α`. Since `S_{θ,i}` is μ-free,
`α_μ=0` (covariance-only), matching the A3 warning callout.

**(I2) Hessian split.** `∇²C_n(θ₀) = H_φ + I_mis|obs`.
Chain rule: `∇²C_n = ∇²_φφF + 2∇²_φψF + ∇²_ψψF`, all at `(θ₀,θ₀)`. The three blocks are
- `∇²_φφF = H_φ` (cross-entropy curvature — the lemma's `H_φ`, the `ℓ(SSᵀ−J)` form of @sec-termA),
- `∇²_ψψF = −I_mis|obs` (eval slot = expected-loglik Hessian = −Fisher),
- `∇²_φψF = +I_mis|obs` (Bartlett: `∫ ∂_φ p · ∂_ψ log p = E_{θ₀}[S Sᵀ]`).

So `∇²C_n = H_φ + 2 I_mis|obs − I_mis|obs = H_φ + I_mis|obs`. ∎

Both are verified symbolically (generic conditioning value `x`, full 5-parameter
`(μ₁,μ₂,σ₁₁,σ₁₂,σ₂₂)` natural parametrization) by **two** computer-algebra systems —
`verification/cas-wolfram/verify_term_ac.py` (Wolfram) and `..._sympy.py` (SymPy).

## The reconciliation

Plug (I1)–(I2) into the Taylor expansion, with `E[δ]` the MLE bias and
`Var(θ̂_obs)=I_obs⁻¹` (A5 / BvM alignment so the same `I_obs⁻¹` enters all three pieces):

> `Δ_n = E[δ]ᵀ ∇C_n(θ₀) + ½ tr(∇²C_n(θ₀) · I_obs⁻¹) + O(n^{−3/2})`
> `    = αᵀE[δ]  +  ½ tr( (H_φ + I_mis|obs) I_obs⁻¹ )`
> `    = ⟨αᵀE[δ]⟩_(A)  +  ⟨½ tr(H_φ I_obs⁻¹)⟩_(C)  +  ⟨½ tr(I_mis|obs I_obs⁻¹)⟩_{½tr(RIV)}`.

Hence

> **`Δ_n = ½tr(RIV) + (A) + (C)`**,   and since `E[T] = ½tr(RIV) + (A)+(C)` (@eq-combine),  **`E[T] = Δ_n`.**

The two decompositions are one total, regrouped:

- **Manuscript:** `E[A] = tr(RIV) + (A)+(C)` (the `(B)-main` cross-term supplies `tr(RIV)`),
  `E[B] = −½tr(RIV)`. Net `E[T] = ½tr(RIV) + (A)+(C)`.
- **Entropy:** `E[T] = Δ_n`, whose **first-order** part is `(A)` and whose **second-order** part is
  `½tr(RIV) + (C)`. Equivalently `E[A] = ½tr(RIV)[KL cross-term] + Δ_n`, so the two `½tr(RIV)`
  halves visibly cancel against `E[B]`.

The regrouping is exactly the Hessian split: `tr(RIV)` (manuscript, from the `(B)-main` cross-term)
splits as `½tr(RIV)` from `∇²_φψF` (entropy's mixed block) `+ ½tr(RIV)` left to cancel `E[B]`.

## Boundary anchors (all consistent)

- **Known scale (Σ fixed).** `C_n` is μ-free ⇒ `Δ_n = 0`. The split forces `(H_φ)_μμ = −I_mis|obs`
  (because `(∇²C_n)_μμ = 0`) — this **is** the Scope-callout Isserlis identity, now a corollary of
  (I2) rather than a separate fourth-moment computation. With `α=0`: `(A)=0`, `(C)=−½tr(RIV)`, so
  `E[A]=½tr(RIV)`, `E[T]=0` (FIML). Matches `rederivation-knownvar.R` (`Δ_n→0`, the boundary).
- **Estimated-Σ MCAR.** `(A)+(C)=0` ⇒ `Δ_n = ½tr(RIV)` — the clean headline; the `½tr(RIV)` the
  result gains over the known-scale case is exactly the entropy term `Δ_n`.
- **Estimated-Σ MAR.** `Δ_n = ½tr(RIV) + (A)+(C)`, the design-imbalance `(A)+(C)` nonzero.

## C2b — `T` is convention-free for the normalized unknown-Σ MVN

Term A (and hence `T`) is **not** invariant to a θ-free, `Y_mis`-dependent additive constant `c(Y)` in
`ℓ_com`: adding `c` shifts `E[T]` by `E[(E_φ̃ − E_{θ₀})[c(Y)|Y_obs]]`, an entropy-type `O(1)` term that
is nonzero whenever `c` depends on `Y_mis`. For the **full normalized** MVN log-density
`ℓ_com = −n/2 log|2πΣ| − ½ Σ_i (Y_i−μ)ᵀΣ⁻¹(Y_i−μ)`, every `Y`-dependent term carries `Σ⁻¹` and is
therefore θ-dependent; the only θ-free terms (`−np/2·log2π`) are also `Y`-free. **No θ-free,
`Y_mis`-dependent floating constant exists, so `T` is well-defined and convention-free.**

Contrast (the known-variance subtlety): with σ² *known*, the kernel piece `−½σ⁻²Σy²` is θ-free and
`Y`-dependent, so whether it is carried changes the `E[A]` bookkeeping by exactly the entropy term —
this is the same `Δ_n` boundary value (`Δ_n=0` known-scale). The full normalized density removes the
ambiguity by construction.

## Verification ledger (all PASS)

1. **Wolfram** `verify_term_ac.py` — (I1), (I2), Bartlett, Isserlis mean-block, and the scalar
   `Δ_n − [½tr(RIV)+(A)+(C)] = 0` with generic `I_obs⁻¹`, `E[δ]`. Symbolic, exact, generic in `x`,
   full 5-parameter natural `(μ,Σ)`. All six checks `→ 0`.
2. **SymPy** `verify_term_ac_sympy.py` — independent second-CAS mirror; identical six checks `→ 0`.
   (`α_σ22 = −σ₁₂²/(2σ₂₂(σ₁₁σ₂₂−σ₁₂²)) ≠ 0`, both engines — entropy gradient is real and covariance-only.)
3. **Monte-Carlo** `rederivation-L0-fitted-vs-oracle.R` (R=4000, 20 cores; the per-replicate `Δ_n` and a
   paired `T_fitted − Δ_n` check):

   | N | `mean tr(RIV)` | `E[Δ_n]` | `E[T_fitted]` | paired `E[T−Δ_n]` | `E[Δ_n]/(½trRIV)` |
   |---|---|---|---|---|---|
   | 200 | 5.552 | +2.722 (SE .117) | +2.735 (SE .172) | **+0.013 (SE .126)** | 0.980 |
   | 800 | 5.517 | +2.728 (SE .224) | +2.999 (SE .340) | +0.271 (SE .255) | 0.989 |

   `E[Δ_n]` tracks `½tr(RIV)` precisely at both N (the small residual `≈ −0.05/−0.03` is the
   design-imbalance `(A)+(C)`); `E[Δ_n]` is a lower-variance functional than `E[T_fitted]`, so the
   paired difference is the sharpest read and is consistent with zero. `cache/c2-deltan-mc-N{200,800}.txt`.
4. **Boundary anchor** `rederivation-knownvar.R` — `E[Δ_n] = 0` exactly (max|·| = 0 per replicate);
   `C_n` is Σ-free when Σ is known, so `Δ_n ≡ 0`, and `E[T_fiml] ≈ 0`, `E[C_n] = ½tr(RIV)` (ratio 1.000).

## Decision

CONFIRMED ⇒ per `todo/017` gate and author intent: **keep `+½tr(RIV)` as the headline**; add only a
one-paragraph reconciliation **remark** to `manuscript/derivation.qmd` (near the Scope callout /
`@sec-combine`). `E[T]=Δ_n` is *not* promoted to the primary statement.
