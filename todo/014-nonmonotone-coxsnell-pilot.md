# Todo 014 — Non-monotone `(A)+(C)` via Cox–Snell: scoped pilot

**Status:** Draft (2026-06-01). Plan; to be executed in a fresh session.

**Goal.** Replace the manuscript's *empirical* non-monotone `(A)+(C)` asymptote (phase-8 2-point
extrapolation, `≲−0.46`) with a **derived closed (or semi-closed) form**, by computing the general
covariance-MLE second-order bias `b_Σ` under non-monotone missingness via the Cox–Snell machinery in
Wolfram — then assembling `(A)+(C)_∞` and checking it against the phase-8 sign/magnitude.

This is Layer-2 **TODO-B** of `todo/013`. (TODO-A — the *bivariate-monotone* `(A)+(C)` — is done:
independently re-derived in `verification/cas-wolfram/verify_term_ac.py`, commit `d2ba31c`.)

---

## 1. The one missing ingredient

The general-MVN design-imbalance asymptote is (`derivation.qmd` @sec-termA, lines ~801, 828):
`(A)+(C)_∞ = αᵀ b_Σ + ½ tr(𝓗_φ I_obs⁻¹)`, where
- `α` = conditional-entropy gradient (**covariance-only**), closed form
  `α_a = −½ Σ_{i:mis} tr(S₀ᵢ⁻¹ ∂_a Sᵢ)`;
- `𝓗_φ` = cross-entropy curvature (per-unit Gauss–Newton form, lines 812–816);
- `b_Σ = lim_{n→∞} n·E[Σ̂_obs − Σ]` = the **covariance-block FIML MLE bias coefficient**.

`α` and `𝓗_φ` are **mechanical** (Magnus confirms no gap; same machinery already exercised
symbolically for the bivariate in `verify_term_ac.py`). The **only** open piece is `b_Σ` for the
non-monotone case — where the observed-data likelihood does **not** factor into a clean conditional-
regression sequence, so the monotone closed forms (Anderson–Olkin / Kanda–Fujikoshi / Hyodo) do not
apply and **no published formula exists** (todo/003, 2026-06-01 `b_Σ` pass). Hence: derive it.

## 2. The tool — Cox–Snell second-order bias

Cox & Snell (1968) eq. (20) [`coxGeneralDefinitionResiduals1968`, verified]:
```
b_s = ½ Σ_{r,t,u} I^{rs} I^{tu} ( K_{rtu} + 2 J_{t,ru} ) + O(n⁻²)
```
with score `U_r = ∂ℓ/∂θ_r`, `V_{rs} = ∂²ℓ/∂θ_r∂θ_s`, `W_{rst} = ∂³ℓ`,
`I_{rs} = E[−V_{rs}]` (Fisher info, `I^{rs}` its inverse), `J_{r,st} = E[U_r V_{st}]`,
`K_{rst} = E[W_{rst}]`. Valid for **non-iid / pattern-mixed** observations (Cordeiro–Klein 1994
matrix form, `cordeiroBiasCorrectionARMA1994`, verified) — exactly the non-monotone case, where the
observed-data contributions are heterogeneous across missingness patterns.

**Execution template:** Patriota & Lemonte (2008) `patriotaBiasCorrectionMultivariate2009` (acquired,
`literature/`, **not yet read in-session**) executes Cox–Snell for a general-parameterization MVN via
weighted least-squares regressions. **Read this first** — it is the "how to run Cox–Snell for the
MVN" recipe; adapt it from complete-data to the FIML observed-data score/info.

## 3. Pilot scope — start at the minimal non-factoring case

Do **not** start at the 4-variate ampute design. Start at the smallest pattern where the observed-
data likelihood genuinely does not factor:

- **Minimal:** bivariate `(X₁,X₂) ~ N(μ,Σ)` with **three** unit groups — complete, `X₁`-missing
  (observe `X₂`), and `X₂`-missing (observe `X₁`). The two incomplete patterns `{X₂}` and `{X₁}` do
  not nest ⇒ non-monotone; the joint `(μ,Σ)` MLE has no closed form (needs EM), so the bias needs
  Cox–Snell. This is the cleanest proof-of-method.
- If clean, step up to the **3-variate "file-matching"** pattern (observe `{X₁,X₂}` vs `{X₂,X₃}`),
  then the 4-variate to meet the phase-8 design.

The observed-data log-likelihood is a sum over patterns `P` of the marginal Gaussian on the observed
block: `ℓ_obs(θ) = Σ_P Σ_{i∈P} log φ(y_{obs,i}; μ_P, Σ_{PP})`. Parametrize `θ = (μ, vech Σ)`.

## 4. Recipe (Wolfram)

1. Build `ℓ_obs(θ)` as the pattern-sum above (symbolic in `μ, vech Σ`; pattern frequencies `n_P`).
2. `D[]` to get `U_r, V_{rs}, W_{rst}` symbolically.
3. Take expectations under the true `θ₀` to form `I_{rs}, J_{r,st}, K_{rst}` (Gaussian moments;
   selection enters through the per-pattern frequencies / conditioning — keep the MAR design explicit).
4. Apply Cox–Snell ⇒ full bias vector `b`; extract the **Σ-block** `b_Σ`.
5. Assemble `(A)+(C)_∞ = αᵀ b_Σ + ½ tr(𝓗_φ I_obs⁻¹)` using the mechanical `α, 𝓗_φ` (reuse the
   `verify_term_ac.py` derivation of `α, 𝓗_φ`, generalized to the pattern set).
6. Compare to phase-8 (`_modules/term-a-mar-correction.R`: non-monotone `−0.34 (n=800) → −0.46
   (n=1500)`): sign, magnitude, `n`-scaling.

## 5. Cross-checks (these are the verification, not the number-matching)

- **MCAR control:** make the pattern frequencies independent of the values ⇒ `(A)+(C)_∞` must → 0.
  (Same control as the committed scripts.)
- **Monotone reduction:** specialize the pattern set to monotone (drop the `X₂`-missing group) ⇒
  `b_Σ` and `(A)+(C)` must reduce to the **already-verified** bivariate-monotone closed form
  (`verify_term_ac.py`) and the Kanda–Fujikoshi / Hyodo `Σ̂` bias. A failure here means the Cox–Snell
  setup is wrong.
- **Numeric MC:** direct Monte-Carlo `E[Σ̂_obs − Σ]·n` for the same small pattern (or `mle.tools`
  `coxsnell.bc()`, todo/003) must match the symbolic `b_Σ` within MCSE.

## 6. Risks & fallbacks

- **Algebraic blow-up.** The MVN `W_{rst}` cumulants are many; even bivariate may be heavy. Fallback:
  keep `b_Σ` **semi-symbolic** — symbolic in `Σ` entries at a fixed `μ`, or evaluate `I, J, K`
  numerically at a fixed `θ₀` and keep only the pattern-frequency dependence symbolic. A semi-closed
  `b_Σ` that reproduces the phase-8 curve still converts "empirical" → "derived (numeric-exact)".
- **No clean `I_obs⁻¹`.** The non-monotone observed-data Fisher info may not invert cleanly in closed
  form; carry it numerically at `θ₀` if needed.
- **The target is itself soft.** Phase-8 `≲−0.46` is a 2-point extrapolation, so success = consistent
  sign/magnitude/scaling, not exact equality. A third `n` in phase-8 would firm the target (optional).

## 7. First-session steps

1. Read `literature/patriotaBiasCorrectionMultivariate2009.md` (the Cox–Snell-for-MVN template) and
   re-skim `coxGeneralDefinitionResiduals1968.md` §3 / `cordeiroBiasCorrectionARMA1994.md` §2.
2. New script `verification/cas-wolfram/verify_term_ac_nonmonotone.py` (reuse the kernel-discovery +
   retry helpers from `verify_term_ac.py`; consider factoring them into `_wolfram.py`).
3. Implement the recipe (§4) for the **minimal bivariate non-monotone** case; pass the three
   cross-checks (§5) before trusting any number.
4. Decide go/no-go on scaling to 3- and 4-variate.
5. If it lands: update `@sec-termA`'s non-monotone branch from "reported empirically" to "derived",
   and the `todo/013` Layer-2 table (TODO-B done).

## 8. Definition of done

A `b_Σ` for the minimal non-monotone pattern that (a) passes the MCAR and monotone-reduction
cross-checks symbolically and (b) matches a direct MC within MCSE — plus an assembled `(A)+(C)_∞`
consistent with the phase-8 sign/magnitude. Closed-form if tractable; semi-symbolic/numeric-at-`θ₀`
is an acceptable first win. Scaling to the 4-variate is a stretch goal, not a gate.

---

## Repo state at hand-off (2026-06-01)

- On `main`. Derivation audit WARN-clean (`8824f21`). Wolfram CAS companions committed:
  `verification/cas-wolfram/verify_traces.py` (`3977bdd`), `verify_term_ac.py` (`d2ba31c`).
- Wolfram 14.3 kernel auto-discovers (deep binary under `SystemFiles\Kernel\Binaries`); the helper
  retries flaky fresh-install WSTP startups. `wolframclient` installed.
- The mechanical `α, 𝓗_φ` derivation to reuse is in `verify_term_ac.py`; the monotone closed form it
  reproduces is the reduction target for the cross-check.

*Draft 2026-06-01. Sibling of `todo/013` (independent re-derivation). Execute in a fresh session.*
