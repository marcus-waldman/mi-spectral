# Todo 015 — General-`p` non-monotone `b_Σ` via Cox–Snell; reach the 4-variate phase-8 `−0.46`

**Status:** **EXECUTED 2026-06-02.** Sibling of todo/014.

## Outcome (2026-06-02)

**General-`p` Cox–Snell `b_Σ` derived and validated** (`verification/cas-wolfram/verify_term_ac_nonmonotone_genp.py`):
arbitrary `p`, arbitrary non-monotone pattern set, per-dimension Gauss–Hermite. Gates all pass —
**p=2 reduction reproduces the committed bivariate `b_Σ` to `1.5e-13`**; zero-score/Bartlett `~1e-15`
at p=3,4; exact structural checks (always-observed block → complete-data `−σ`; monotone reduction →
`−σ_pp`; `σ_ij=0` → `b=0`); GH-converged (per-dim `[10,10,26,26]` ≡ uniform 20). 4-variate phase-8
`b_Σ` (fractions 0.4/0.2/0.2/0.2): `s11=s22=−1.391, s21=−0.722, s33=s44=−1.0, s43=−0.5, s31=s42=−0.3`.
`b_Σ` is **nearly selection-invariant** at fixed fractions (additive sweep: `s11` `−1.391→−1.362` over
`b=0→1.2`).

**KEY FINDING — `b_Σ` is NOT the missing piece for `−0.46`.** Feeding the derived `b_Σ` through the
pattern-general assembly (`verification/verify_term_ac_nonmonotone_4v.R`, reusing
`term-a-mar-closedform.R`'s `alpha_expected`/`hphi_expected`) gives the **leading-order
`(A)+(C)_∞ ≈ −0.22`** (A=+0.78, C=−1.00) — the *same* constant as the monotone design — confirmed two
independent ways (analytic α/H_φ **and** finite-differencing the analytic `barQ`), with MCAR control
→ 0. The committed phase-8 empirical remainder (`−0.34@800 → −0.46@1500`, still increasing) lies
**beyond** this leading-order constant. The offset is a **higher-order (finite-n / realized-information)
gap**, the same kind already present in the monotone (`−0.22` vs `−0.27`) and bivariate (`−0.10` vs
`−0.07`) cases — *not* a `b_Σ` shortfall. A cross eval-impute-curvature "bracket" candidate for the
gap was investigated but is dominated by single-dataset sampling noise (±0.3) and did not cleanly
reproduce the empirical; pinning the gap is **open higher-order theory**, not a mechanical scale-up.

**Disposition (user decision, honest reframe):** manuscript `@sec-termA` updated — `b_Σ` now stated as
derived at general `p` incl. the 4-variate phase-8 design, leading-order `(A)+(C)_∞≈−0.22` (parallel to
monotone), empirical `−0.46` reframed as the realized-information gap (not a target for `b_Σ`).
`todo/013` TODO-B updated. `quarto render manuscript/derivation.qmd` exit-0.

---
*Original plan below (2026-06-01).*

**Goal.** Generalize the (verified) **bivariate** non-monotone Cox–Snell `b_Σ` to **general `p`**
(arbitrary non-monotone pattern set), validate it reduces to the committed `p=2` result, then point it
at the **4-variate phase-8 ampute design** to reproduce the empirical non-monotone `(A)+(C)`
(`−0.34` at `n=800 → −0.46` at `n=1500`). This converts the manuscript's non-monotone branch from
"derived (bivariate); 4-variate the remaining target" to fully closed.

## 1. What is already done (the template — commit `08ee37b`, todo/014)

The bivariate non-monotone `b_Σ = lim n·E[Σ̂_obs − Σ]` is **derived and verified five ways** (two CAS
to ~1e-9, score/Bartlett identities, exact monotone reduction, direct MC, MCAR control). Reuse these
**verbatim as the structure to generalize**:
- `verification/cas-wolfram/verify_term_ac_nonmonotone.py` — Wolfram: symbolic U/V/W, Cox–Snell
  eq.(20) `b_s = ½ Iʳˢ Iᵗᵘ (K_rtu + 2 J_{t,ru})`, expectations via a NIntegrate moment table.
- `verification/cas-wolfram/verify_term_ac_nonmonotone_sympy.py` — SymPy: exact derivs + tensor
  Gauss–Hermite; selection-strength sweep.
- `verification/cas-wolfram/_wolfram.py` — kernel discovery/retry.
- `verification/verify_term_ac_nonmonotone.R` — monotone-reduction gate, direct-MC gate, `(A)+(C)`
  assembly. **The R assembly (`est_moments`, `alpha_expected`, `hphi_expected`) is already
  pattern-general** — it loops over arbitrary observed-blocks; only `compute_bSigma` is monotone-only,
  and Cox–Snell `b_Σ` replaces exactly that. So the assembly side needs almost no change for general `p`.

## 2. Recipe for general `p` (Cox–Snell)

Parameter `θ = (μ, vech Σ)`, `k = p + p(p+1)/2` (vech = column-major lower-tri, matching
`vech_index_table`/`duplication_matrix` in `00-setup.R`: for the Σ-block, index `s` ↔ `Epert(s)`).

1. Build `Σ` as a general symmetric `p×p` of symbols, `μ` as `p` symbols. For each missing pattern
   `P` with observed block `O_P`, the per-unit log-density is the **marginal Gaussian on `O_P`**:
   `ℓ_P = −½ log|Σ_{O_P,O_P}| − ½ (y_{O_P}−μ_{O_P})ᵀ Σ_{O_P,O_P}⁻¹ (y_{O_P}−μ_{O_P})`.
2. `U_r = ∂_r ℓ_P`, `V_{rs}`, `W_{rst}` symbolic; evaluate at `θ0` → polynomials in the data.
3. Per-unit cumulants as **joint expectations over (X, pattern)** at `θ0`:
   `i_rs = −E[Σ_P w_P V_{rs}^P]`, `j_{t,ru} = E[Σ_P w_P U_t^P V_{ru}^P]`, `k_rtu = E[Σ_P w_P W_{rtu}^P]`,
   with `w_P(x) = P(pattern P | x)` the MAR weights (§3). Expectation over `X ~ N(μ0,Σ0)`.
4. `b_s = ½ Σ_{r,t,u} (i⁻¹)_{rs} (i⁻¹)_{tu} (k_{rtu} + 2 j_{t,ru})`; extract the Σ-block → `b_Σ`.
   (Per-unit cumulants give the `lim n·E[·]` directly — no extra `n` factor.)
5. Assemble `(A)+(C) = αᵀ b_Σ + ½ tr(𝓗_φ I_obs⁻¹)` with the existing R machinery.

**Expectations (the only real scaling cost).** Tensor Gauss–Hermite over `X = μ0 + L z`, `z~N(0,I)`,
`L = chol(Σ0)`: nodes `√2·t_i`, weights `Π w_i / π^{p/2}`. The derivative products are degree ≤ 4
polynomials (GH-exact with ≥3 nodes/dim); the smooth MAR weights need ~15–20 nodes/dim. So `20^p`
points: `p=3 → 8k`, `p=4 → 160k` (fine), `p=5 → 3.2M` (heavy but OK), `p≥6 → switch to Monte-Carlo`
(Rao-Blackwellized: weight each draw by `w_P`, average). Keep both engines (Wolfram NIntegrate,
SymPy GH) for the two-CAS check at small `p`; for `p=4` GH is the workhorse, NIntegrate the check.

## 3. The MAR mechanism — CRITICAL (this is where the bivariate pilot first went wrong)

Each pattern's probability must depend **only on that pattern's observed block** (genuine MAR); a
shared multinomial-logit denominator makes `P(P|x)` depend on the *missing* coordinates ⇒ **MNAR**,
which the **zero-score gate `E[U]=0` catches** (it was ~9e-3 under the MNAR bug, ~1e-13 when fixed).
The bivariate fix was the **additive half-sigmoid**; generalize it so the pattern probabilities
partition (`Σ_P w_P = 1` pointwise, all in [0,1]) — e.g. cap each pattern's probability so the sum
≤ 1, each as a sigmoid of a linear form in *its own observed block*. **Keep the zero-score and
Bartlett (`E[UUᵀ]=I`) gates as the first checks on any candidate mechanism.**

For the **phase-8 match specifically**: replicate the exact mechanism of
`apply_missingness_ampute(X, prop=0.40, mech="MAR", pattern_type="non_monotone")` (00-setup.R:133) —
its patterns and weighted-sum logistic scores — so the Cox–Snell `b_Σ` and the empirical phase-8
rem use the *same* design. Truth: `default_mu = (0,0,0,0)`, `default_Sigma` (00-setup.R:1194). If the
ampute mechanism is awkward to mirror analytically, fall back to estimating the selected moments /
pattern frequencies by MC (the assembly already does this) and feed Cox–Snell `b_Σ` computed under a
matched analytic MAR mechanism — sign/magnitude/scaling is the success bar, not bit-exactness.

## 4. Validation gates (pass before trusting the 4-variate number)

- **Reduce to `p=2`:** general-`p` code at `p=2`, same mechanism/`θ0`, must reproduce the committed
  `b_Σ = (s11=−1.19122, s12=−0.48203, s22=−1.19122)` (commit `08ee37b`).
- **Two-CAS** at `p=3` (and `p=4` if feasible): Wolfram ≡ SymPy on `b_Σ`.
- **Zero-score / Bartlett** to ~1e-9 (MAR sanity).
- **MCAR control:** `(A)+(C) → 0`.
- **Monotone reduction:** drop patterns until monotone ⇒ matches `compute_bSigma`
  (`term-a-mar-closedform.R`) and `b_{σ_pp}=−σ_pp` for the always-observed-last variable.
- **Direct MC:** `n·E[Σ̂−Σ]` matches `b_Σ` within MCSE.
- **Phase-8:** assembled `(A)+(C)_∞` consistent with `−0.34 (n=800) → −0.46 (n=1500)`.

## 5. Gotchas (carried from todo/014 execution)

- `b_Σ` is **nearly selection-invariant** (≈ its MCAR value); the `(A)+(C)` imbalance enters almost
  entirely through the **selected moments** in `α/𝓗_φ/I_obs`, not `b_Σ`. So even a roughly-right `b_Σ`
  plus accurate selected moments gives the right `(A)+(C)`.
- There is a **genuine small `O(1/n)` mean bias `b_μ`** under non-monotone MAR (mean couples to the
  biased Σ̂; both CAS agree). It's **covariance-irrelevant** (α is covariance-only) — do **not** gate on
  `b_μ ≈ 0` except under MCAR.
- vech ordering must match R's column-major lower-tri throughout (`b_Σ` extraction at Σ-block indices).
- Wolfram NIntegrate at strong selection: use `Quiet[…, NIntegrate::slwcon]`, `AccuracyGoal`, finite
  `MaxRecursion` (near-zero odd moments otherwise trigger slow-convergence warnings).

## 6. First-session steps

1. Re-read this file + `verification/cas-wolfram/verify_term_ac_nonmonotone_sympy.py` (cleanest engine).
2. Generalize the SymPy script to arbitrary `p` + arbitrary pattern set + p-D GH; pass the `p=2`
   reduction gate, then `p=3` two-CAS.
3. Replicate (or MC-match) the phase-8 `apply_missingness_ampute` non_monotone design at `p=4`.
4. Run the gates (§4); assemble `(A)+(C)_∞`; compare to `−0.46`.
5. If it lands: update `@sec-termA` ("4-variate phase-8 value the remaining target" → "derived"),
   `todo/013` TODO-B (drop the 4-variate caveat); commit on `main` with the Co-Authored-By trailer.

## Definition of done

A general-`p` Cox–Snell `b_Σ` that reproduces the committed `p=2` result and passes the §4 gates, with
the 4-variate assembled `(A)+(C)_∞` consistent with the phase-8 `≈−0.46`. Semi-symbolic / MC-at-`θ0`
is acceptable; sign/magnitude/scaling is the bar (phase-8 is a 2-point extrapolation), not bit-exactness.

*Draft 2026-06-01. Continues todo/014 (bivariate, done, `08ee37b`). Memory:
[[project-nonmonotone-coxsnell]].*
