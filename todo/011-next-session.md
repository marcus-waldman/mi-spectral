# Todo 011 — Closed-form general-MVN `(A)+(C)`: monotone branch DERIVED + in manuscript (2026-06-01)

**Resume entrypoint.** Supersedes `todo/010`. Phase-3a closed-form general-MVN `(A)+(C)` asymptote:
the **monotone branch is now fully derived (path b done) and integrated into `derivation.qmd`**.
Approved plan: `~/.claude/plans/toasty-launching-hummingbird.md`. Nothing committed yet (commit when asked).

## UPDATE (path b complete + manuscript integration)
- **Exact `(C)` via the pure cross-entropy curvature `H_φφ = ∇²_φ barQ(θ₀,φ)|_{θ₀}`** (imputation
  slot only; excludes the eval-obs cross block that gives `(B)main=tr(RIV)`), so `(C)=½tr(H_φφ I_obs⁻¹)`
  with NO `−tr(RIV)`. Cross-checks: `∇_φ f₀ = α` (max diff 5e-4); decoupling error `C_coupled` vs
  `C_decVar` tiny (~0.01–0.04, shrinking in N). `verification/scratch-AC-pathb.R`.
- **Headline value: `(A)+(C)_∞ ≈ −0.22`** for the 4-var monotone-MAR design — `(A)=α⊤b_Σ=+0.54`,
  `(C)=½tr(H_φφ I_obs⁻¹)=−0.76`; **N-stable** (−0.220/−0.223/−0.221 at N=300/800/1500), consistent
  with the high-R measured RB-A curve (scatters −0.12 to −0.27 at large N as MCSE grows).
- **Reproducible artifact committed-worthy:** `verification/term-a-mar-closedform.R` — computes the
  closed form for MAR (≈−0.22) and the **MCAR control (→0)**; MAR N=800 cell confirmed (−0.223).
- **Manuscript integrated:** `derivation.qmd §sec-termA` "General-MVN closed form (monotone)" block
  replaces the old "deferred/empirical" text (the recursion, analytic `α`, the value −0.22, MCAR→0,
  scope = monotone-derived / non-monotone-empirical). Margin note + combine line updated. **Renders
  clean** (exit 0, all 20 cells, `derivation.html`). Hyodo/Kanda–Fujikoshi/Cox–Snell/Cordeiro–Klein
  written as prose "pending acquisition" (render-clean; promote to `@cite` after lit-sync).

## REMAINING
- **Acquire + lit-sync** Hyodo (2016) + Kanda–Fujikoshi (1998) → swap the prose refs in `§sec-termA`
  to `@cite`. (Also Wang–Robins/Nielsen for Phase 3b.) See `todo/003`.
- **Promote** `term-a-mar-closedform.R` into `run_all.R` (e.g. extend phase 8) if a committed sweep
  cell is wanted; add a Sympy/NumPy Appendix-B inline check mirroring `@lst-mc-crossterm`.
- **Commit** the session (scratch scripts, `term-a-mar-closedform.R`, `todo/003`/`011`, derivation.qmd).
- **Non-monotone closed form (optional Phase D):** Cox–Snell/Cordeiro–Klein on the FIML observed-data
  likelihood; currently empirical (≈−0.46).
- Downstream: Phase 3b proper-MI, Phase 4.2, Phase 5 manuscript rebuild + MI-IC coordination.

---

## (Original session record below)

## DONE this session

### Literature pass (the "don't reinvent the wheel" ask) — logged in `todo/003` (2026-06-01 section)
9-agent litrev/consensus/web/owned pass. **Verdict: monotone = REUSE; general non-monotone = DERIVE.**
- **Monotone reuse:** Hyodo, Shutoh, Seo & Pavlenko (2016) — *read in-session* (open Hiroshima TR13-05
  PDF, cached at `…/131f54f1-…/tool-results/webfetch-1780337704981-idje1s.pdf`) gives the explicit
  2-step monotone MLE + exactly-unbiased estimator (Lemma 2.1) ⇒ `b_Σ = lim N·(MLE − unbiased)`;
  Kanda & Fujikoshi (1998) exact k=2,3; owned L&R §7.4.2 / Schafer §6.5 / Anderson 2003 / Magnus suffice.
- **General non-monotone:** NO published formula; Cox–Snell (1968) / Cordeiro–Klein (1994) machinery +
  Patriota–Lemonte (2008) template. (All acquisitions logged with DOIs in `todo/003`.)

### `b_Σ` (the hard ingredient) — DERIVED (per-step recursion)
Monotone MVN MLE factors into per-step regressions (block `j` on `1..j−1`, fit on the `r_j` units
observed through step `j`). **All cross-step covariances vanish** (each step's OLS slope is
conditionally unbiased given the conditioning vars; `Σ̂_{<j}` is a function of those vars only ⇒
`Cov(β̂_j, Σ̂_{<j})=0`). Recursion (`b_Σ = lim N·E[Σ̂_obs − Σ_0]`, blockwise):
```
b[1,1] = -σ_11
for j>=2, P = 1:(j-1):
  b[j,P] = b_j · b[P,P]                                   # slope-propagated cov-block bias
  b[j,j] = -(j/f_j)·σ_{jj.<j}                             # residual-variance MLE bias (j params)
         + b_j · b[P,P] · b_jᵀ                            # recursive predictor-block bias
         + (σ_{jj.<j}/f_j)·tr(Σ_PP (Σ_PP^{(j)})⁻¹)        # slope-variance back-transform
```
`f_j = E[r_j]/N`; `Σ_PP^{(j)} = Cov(X_P | observed through j)` = the **selected (design-imbalanced)**
predictor covariance (= `Σ_PP` under MCAR ⇒ trace = `j−1`). Values (default_Sigma, monotone MAR 40%):
`s11=-1.0, s21=-0.6, s31=-0.3, s41=0, s22=-1.085, s32=+0.024, s42=-0.34, s33=-1.254, s43=-0.657,
s44=-1.352`; `f=(1.0, 0.867, 0.733, 0.601)`. `σ_{jj.<j}=(—, 0.640, 0.859, 0.462)`.
**Validation status:** structurally sound; `s11=-1.0` exact by construction. Direct MC measurement is
**noise-limited** (`scratch-bsigma-measure.R`, R=40000 ⇒ MCSE≈0.20 on `N·bias`; the σ11 sanity check
`scratch-sanity-var.R/-seed.R` confirms the ~0.20 floor and that the consecutive-seed convention is
fine). So `b_Σ` is consistent with the measurement but not tightly confirmed by it.

### `α` (entropy gradient) — DERIVED + VALIDATED
At `θ_0` the quadratic `(m_0−m_θ)` factor vanishes, leaving the **cov-only** per-unit form
`α_a = -½ Σ_{i:mis} tr(S_{0,i}⁻¹ dS_i[E_a])`, `dS[dΣ]=dMM − dMO Bᵀ − B dOM + B dOO Bᵀ`, `B=Σ_MO Σ_OO⁻¹`.
`α` per unit is deterministic (no y) ⇒ `α = Σ_patterns n_P α_P`. **Matches finite-diff `g_bar` to 3e-5;
`α_μ=0` exactly** (`scratch-alpha-analytic.R`).

### `(A)+(C)_∞` semi-analytic value
`(A)+(C)_∞ = α_u⊤ b_Σ + [½tr(𝓗_u I_{obs,u}⁻¹) − tr(RIV)]`. With analytic `α`, analytic `b_Σ`, and
**numeric** `𝓗`/`I_obs` (`scratch-AC-asymptote.R`): `(A)≈+0.54` (N-stable), `(C)≈-0.78`, **`(A)+(C)_∞ ≈ -0.24`**.
Measured RB-A curve (`scratch-AC-highR.R`, R=40000): `-0.180(800), -0.275(1500), -0.140(3000),
-0.121(6000)` (MCSE 0.06→0.17). The curve does **not** grow monotonically past −0.27 (the prior
concern); it scatters ≈−0.15 to −0.27 at large N ⇒ **consistent with the closed-form −0.24 within noise**.

## OPEN — the exact constant (path b, ~1–2 hr; NOT ampute-blocked)
The `(C)` above used the **decoupled** `½tr(𝓗̄ I_obs⁻¹)` (`𝓗̄`=full A_of_par Hessian); the exact
`(C) = E[½δ'𝓗δ] − tr(RIV)` keeps `𝓗,δδ'` coupled (finite-N error, the source of the −0.24 vs
measured fuzz). To nail it analytically, with no slow Monte-Carlo:
- Use the **pure cross-entropy curvature** `H_φφ = Σ_{i:mis}[(∇m_i)ᵀ S_{0,i}⁻¹ (∇m_i) + ½∇²tr(S_{θ,i}⁻¹ S_{0,i})]`
  (= `∇²f_0`, the sampling-param curvature — NOT the full `A_of_par` Hessian, which adds the
  `2·∂_eval∂_obs` cross block that produces `(B)main=tr(RIV)`). Then
  `(C)_∞ = ½tr(H_φφ,u I_{obs,u}⁻¹)` with no `−tr(RIV)` needed (the cross block, hence `(B)main`, is
  excluded). `∇m`: μ-part deterministic, Σ-part `= (dMO−B dOO)Σ_OO⁻¹(y_O−μ_O)` ⇒ needs per-pattern
  **selected first+second moments** of `(y_O−μ_O)` (analytic via selected-Gaussian/inverse-Mills, todo/008,
  or cheap MC). Validate analytic `H_φφ` vs finite-diff, and the `tr(C_eo I_obs⁻¹)=tr(RIV)` identity.
- Then **B1** (reduce to bivariate `n_mis/n_obs − ½tr(M_mis M_obs⁻¹)`; MCAR ⇒ 0), **B4** (commit a
  reproducible module / Appendix-B check), **C** (integrate into `derivation.qmd §sec-termA`; citing
  Hyodo 2016 + Kanda–Fujikoshi 1998 needs them acquired + lit-synced first).

## Scratch scripts (EXPLORATORY in `verification/`; promote when backing a claim)
`scratch-bsigma-monotone.R` (fast monotone MLE ≡ lavaan FIML, validated to 4e-6 + nesting check);
`scratch-bsigma-measure.R` (direct `b_Σ`, noise-limited); `scratch-bsigma-analytic.R` (`b_Σ` recursion);
`scratch-alpha-analytic.R` (**α validated**); `scratch-AC-asymptote.R` (semi-analytic `(A)+(C)_∞` evaluator);
`scratch-AC-highR.R` (measured RB-A curve, the data above); `scratch-AC-predict.R` (earlier predictor);
`scratch-sanity-var.R`, `scratch-sanity-seed.R` (MCSE-floor diagnostics).

## Notes / gotchas
- `mice::ampute` dominates runtime (every validation run 5–30 min). Path b removes the MC dependence.
- R not on Bash PATH: `"/c/Program Files/R/R-4.5.1/bin/Rscript.exe"`. Inline `-e` with a PSOCK cluster
  segfaulted — use a script file. parLapply closures must `clusterExport` loop vars (e.g. `N`).
- The 4-var ampute "monotone" pattern = nested obs `{1}⊂{1,2}⊂{1,2,3}⊂{1,2,3,4}`, 60% complete,
  `f=(1,.867,.733,.601)`; MAR selection is on the last-observed var at each step (⇒ conditional model
  preserved, residual-variance bias `−j/r_j` standard; imbalance enters only the back-transform).
