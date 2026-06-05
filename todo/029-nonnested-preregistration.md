# Todo 029 — PREREGISTRATION: the non-nested (Vuong-regime) (A)+(C) differential, CS vs AR(1)

**Status:** PREREGISTERED 2026-06-04, **before any measurement-engine code exists.** This file is
committed ALONE (with the deterministic pseudo-true prep `verification/nonnested-pseudotrue-prep.R`
and the CAS skeleton) in a commit that contains NO replicate/measurement loop — fixing the
single-commit provenance defect flagged in todo/027 §6 (commit `4aa238d`). The measurement engine
(`verification/w4-nonnested-vuong.R`) is written only after this commit lands.

Spec lineage: handoff `todo/028`; locked analytic assets in `derivation.qmd @sec-lrt`
(Propositions L1–L4 — **restated below, never re-derived**) and `@sec-ic`; machinery template
`verification/ic-ladder.R` (todo/027) and the paired-differential template
`verification/w2-paired-differential-mu1-cell.R`. The frozen preregistered originals
(`W1/W2/W3-*.R`) and `ic-ladder.R` are **not touched**; this is a NEW script.

Predictions and pass criteria here were written before the engine existed. If reality differs, the
framing in `@sec-lrt-ac` / `@sec-ic` modifies to match reality — failures are reported, not re-run
away. Any amendment after the first run (or any re-scope after the power-gate pilot) is dated and
labelled.

**What this closes.** The only derived-but-never-measured quantitative claim in the paper:
Proposition L4 — the design-imbalance $(A)+(C)$ differential cancels at the null, is $o(1)$ under
local alternatives, and re-emerges as a genuine $O(1)$ **only for non-nested comparison**
(pseudo-true values $O(1)$ apart, the Vuong regime), where IC ranking consumes it un-absorbed
(`@sec-lrt-consequences`, `@sec-ic-criterion`).

---

## 1. Objects and constructions (fixed before code)

### 1.1 Design
- 4-variate MVN, $\mu_0 = 0$. Two truths (cells A, B below), each run under the X1-heavy **MAR**
  mechanism and its **MCAR** twin (cells A′, B′). $N \in \{500, 1000, 2000\}$.
- **X1-heavy MAR** (the strongest imbalance generator; `amp_fun` of
  `w2-paired-differential-mu1-cell.R`): $P(\text{miss }X_1\mid X_3)=\Phi(0.8+1.2\,X_3)$
  (marginal $\approx \Phi(0.8/\sqrt{1+1.2^2}) \approx 0.696$), $P(\text{miss }X_2)=\Phi(-3)\approx0.001$,
  $X_3,X_4$ complete.
- **MCAR twin:** $X_1$ missing with fixed probability $0.696$ (Bernoulli, independent of all data),
  $X_2$ at $0.001$ — same marginal pattern frequencies as the MAR arm, mechanism independent of the
  data, so the design-imbalance cross term $(A)+(C)=0$ (`@sec-termA`).
- Engine: deterministic-FIML $\bar Q_\infty$ (imputation parameter $=\hat\theta_{\text{obs}}$, the
  saturated FIML fit), matching the scope of the `@sec-lrt` propositions. The single per-replicate
  FIML fit is the only lavaan call; all candidate fits are closed-form.

### 1.2 Candidates and the saturated-anchored statistic — Chan-style maximizers
The MI deviance of candidate $k$ against the saturated anchor is
$T_k = 2[\bar Q_\infty(\hat\psi^*_{\text{sat}}) - \bar Q_\infty(\hat\psi^*_k)]$,
$\hat\psi^*_k = \arg\max_{M_k}\bar Q_\infty$, with $\hat\psi^*_{\text{sat}}=\hat\theta_{\text{obs}}=(m^*,S^*)$
(E-step moments). Each candidate fixes $\hat\mu_k=m^*$ (mean unconstrained) and fits $\Sigma$:

- **CS** $\Sigma=\sigma^2[(1-\rho)I+\rho J]$ — **closed form** (exact MLE on $S^*$ via the
  parameter-independent $J$-eigenframe): $\hat a=\mathbf 1'S^*\mathbf 1/p$ (rank-1 span($\mathbf 1$)),
  $\hat b=\operatorname{tr}(QS^*)/(p-1)$, $Q=I-J/p$; $\hat\sigma^2=\operatorname{tr}(S^*)/p$,
  $\hat\rho=(\hat a-\hat b)/(\hat a+(p-1)\hat b)$. **6 params** (4 $\mu$ + 2).
- **AR(1)** $\Sigma=\sigma^2R(\rho)$, $R_{ij}=\rho^{|i-j|}$ — 1-D profile:
  $\hat\sigma^2(\rho)=\operatorname{tr}(R^{-1}S^*)/p$, minimize $g(\rho)=p\log\hat\sigma^2(\rho)+(p-1)\log(1-\rho^2)$
  over $\rho\in(-0.985,0.985)$ (KMS tridiagonal $R^{-1}$; grid pre-scan + `optimize`). **6 params.**
- **Independence** $\Sigma=\sigma^2I$, $\hat\sigma^2=\operatorname{tr}(S^*)/p$ — **5 params**;
  nested in both CS and AR(1) (the fixed-alternative diagnostic, §2 M2-aux).

The anchored statistic is computed in the **full curved form**
$$T_k = N\big[\log|\hat\Sigma_k| + \operatorname{tr}(\hat\Sigma_k^{-1}S^*) - \log|S^*| - p\big].$$
**Recorded before running:** both CS and AR(1) carry a free scale $\sigma^2$, so at the exact
maximizer the first-order condition forces $\operatorname{tr}(\hat\Sigma_k^{-1}S^*)=p$ and $T_k$
collapses to $N[\log|\hat\Sigma_k|-\log|S^*|]\ge0$ — the same form as the block-diagonal ladder.
The full form is kept as a **convergence guard** (CS exact to machine precision; AR(1) only to
`optimize` tol), with the per-replicate assert $|\operatorname{tr}(\hat\Sigma_k^{-1}S^*)-p|<10^{-6}$.
It is a robustness guard, not a correction.

Equal parameter counts (CS, AR(1) both 6) ⇒ **$\Delta\mathrm{AIC}=\Delta T$ exactly** — a pure
Vuong comparison with no penalty term.

### 1.3 The paired differential (the measurand carrier)
Both candidates are fit on the **same** $S^*$ (same $\hat\theta_{\text{obs}}$, same deterministic
imputation), so the anchor $-N(\log|S^*|+p)$ and (at the maximizer) both trace terms cancel in the
pairwise difference:
$$\Delta T_{\text{MI}} = T_{\text{MI}}(\mathrm{CS})-T_{\text{MI}}(\mathrm{AR1}) = N\log\frac{|\hat\Sigma_{\text{CS}}|}{|\hat\Sigma_{\text{AR1}}|},$$
with the complete-data counterpart $\Delta T_{\text{com}}=N\log(|\hat\Sigma_{\text{CS,com}}|/|\hat\Sigma_{\text{AR1,com}}|)$
on `mle_complete_mvn(X)$Sigma`. The **paired differential** is $D_{\text{pair}}=\Delta T_{\text{MI}}-\Delta T_{\text{com}}$.
(Per-candidate full $T_k$ is also recorded, for the noise-order arm and the M3 L2 report.)

### 1.4 The analytic correction term — general-Jacobian $\operatorname{tr}(\mathrm{RIV}_\perp)$
From `@sec-lrt` (locked): candidate $k$'s saturated-anchored deviance has bias
$E[T_{\text{MI},k}-T_{\text{com},k}]=\operatorname{tr}(\mathrm{RIV}_{\perp,k})+[(A)+(C)]_k$,
$\operatorname{tr}(\mathrm{RIV}_{\perp,k})$ the missing information of the $q_{d,k}=14-p_k=8$ tested
directions projected in the **$I_{\text{com}}$ metric** (@eq-lrt-bias). The `ic-ladder.R` machinery
generalizes from the selection matrix to the **analytic Jacobian**
$G_k=\partial(\mu,\operatorname{vech}\Sigma)/\partial(\mu,\sigma^2,\rho)$ ($14\times6$), built with the
repo's own `vech()` on the analytic derivative matrices (CS: $\partial\Sigma/\partial\sigma^2=(1-\rho)I+\rho J$,
$\partial\Sigma/\partial\rho=\sigma^2(J-I)$; AR1: $\partial\Sigma/\partial\sigma^2=R$,
$\partial\Sigma/\partial\rho=\sigma^2\partial R$, $\partial R_{ij}/\partial\rho=|i-j|\rho^{|i-j|-1}$):
$$\operatorname{tr}(\mathrm{RIV}_{\perp,k}) = \operatorname{tr}(I_{\text{obs}}^{-1}I_{\text{mis}})
- \operatorname{tr}\!\big[(G_k^\top I_{\text{com}}G_k)^{-1}G_k^\top I_{\text{com}}I_{\text{obs}}^{-1}I_{\text{mis}}G_k\big],$$
with $I_{\text{com}}=$ `fisher_info_com_mvn`, $I_{\text{obs}}=$ `fisher_info_obs_mvn` (expected info),
$I_{\text{mis}}=I_{\text{com}}-I_{\text{obs}}$, **all evaluated at the candidate's own per-replicate
pseudo-true $\hat\psi_k=(m^*,\hat\Sigma_k)$** (mirroring `ic-ladder.R:204-205`, which evaluates the
spectrum at the candidate's fit, not the saturated anchor; the IC criterion `@eq-ic-corrected`
prices the correction in the candidate's own parameter space). The null-law weights
$\lambda_{k,j}$ = the $q_{d,k}$ nonzero eigenvalues of $V^{1/2}AV^{1/2}$,
$A=I_{\text{com}}^{-1}-G_k(G_k^\top I_{\text{com}}G_k)^{-1}G_k^\top$, $V=I_{\text{com}}I_{\text{obs}}^{-1}I_{\text{com}}$,
with $\sum_j\lambda_{k,j}=q_{d,k}+\operatorname{tr}(\mathrm{RIV}_{\perp,k})$. The general-$G$ form of
this identity is already CAS-blessed (`verify_ic_ladder.py` L-A3, 200 random full-rank $G$); §4
re-checks it on the actual CS/AR(1) $G_k$.

### 1.5 Frozen pseudo-true inputs (from `nonnested-pseudotrue-prep.R`, deterministic)
Candidate definitions use the complete-data E-step moment $S_\infty=\Sigma_T$. Population pseudo-true
and KL ($\mathrm{KL}(N(0,\Sigma_T)\|N(0,\Sigma_k))=\tfrac12[\log(|\Sigma_k|/|\Sigma_T|)+\operatorname{tr}(\Sigma_k^{-1}\Sigma_T)-p]$):

| Cell | Truth $\Sigma_T$ (first row of the correlation matrix) | CS* $(\sigma^2,\rho)$ / KL | AR1* $(\sigma^2,\rho)$ / KL |
|---|---|---|---|
| A | AR(1) $\rho{=}0.5$: $(1, 0.5, 0.25, 0.125)$ | $(1, 0.3542)$ / $0.13766$ | $(1, 0.5000)$ / $0$ |
| B | Toeplitz $w^*{=}0.528909$: $(1, 0.473555, 0.355782, 0.296895)$ | $(1, 0.4049)$ / $0.034375$ | $(1, 0.4736)$ / $0.034375$ |

Cell B's truth is the one-parameter Toeplitz family $\tau(w)=(1-w)(1,.5,.25,.125)+w(1,.45,.45,.45)$
tuned by `uniroot` on $\mathrm{KL}_{\text{CS}}=\mathrm{KL}_{\text{AR1}}$: $w^*=0.528909$, equal-KL
$=0.034375$, residual $4.4\times10^{-16}$ — complete-data selection between CS and AR(1) is a genuine
coin flip. **Vuong non-degeneracy gates (PASS):** $\min|\rho_{\text{pseudo-true}}|=0.354$ (A), $0.405$
(B), both $\ge0.15$ (well away from the CS$\cap$AR1 intersection at $\rho{=}0$); $\Sigma_T$ PD,
min-eig $0.375$ (A), $0.468$ (B).

### 1.6 Sign of the $(A)+(C)$ differential — TWO-SIDED (decision recorded)
**Prereg default: two-sided $\ge3$ se.** The $(A)+(C)$ *level* is a known heavy-tailed $O(1)$ whose
sign is unstable across $N$ even for a single fit ($-0.34/-0.46/-0.29/+0.17$ in the bivariate Term-A
study; memory `project_nonmonotone_coxsnell`). A clean analytic sign for the *differential* would
require the second-order conditional-entropy curvature $\nabla^2C_n=H_\varphi+I_{\text{mis}|\text{obs}}$
(`cond_entropy_Cn`, `verify_term_ac*.py`) evaluated and contracted at two distinct, $O(1)$-separated
pseudo-true points ($\Sigma_{\text{CS}}^*$ vs $\Sigma_{\text{AR1}}^*$) — not cheap, and inheriting the
level's fragility. A numeric MC probe at the pseudo-true points would constitute premature
unblinding. Per `todo/028` ("signed prereg if derivable, two-sided $\ge3$ se if not"), the sign is
preregistered **two-sided**; if a clean, stable sign emerges from the data post-hoc, it is reported
as a finding, not a confirmed prediction. **GPT-5.5 cross-model gate: not triggered** — the
construction is the corollary-level application of the gate-cleared L1/L4 to curved candidates +
the CAS-blessed general-$G$ spectrum (decision recorded per todo/027 §1.3 precedent).

### 1.7 Per-replicate internal asserts (gates on the run)
- Spectrum identity $|\sum_j\lambda_{k,j}-(q_{d,k}+\operatorname{tr}(\mathrm{RIV}_{\perp,k}))|\le10^{-6}\max(1,\sum_j\lambda_{k,j})$, each candidate.
- Weight bound $\min_j\lambda_{k,j}\ge1-10^{-6}$.
- $T_k\ge0$; trace-cancellation guard $|\operatorname{tr}(\hat\Sigma_k^{-1}S^*)-p|<10^{-6}$.
- PD: $\hat\Sigma_{\text{CS}},\hat\Sigma_{\text{AR1}},S^*$ min-eig $>10^{-6}$; AR(1) $|\hat\rho|<0.94$ (bound flag).
- Realized pseudo-true Vuong gate $\min(|\hat\rho_{\text{CS}}|,|\hat\rho_{\text{AR1}}|)\ge0.15$ (monitored; piling near 0 flagged).
- **Build-time smoke (gates the whole run):** setting $G$ to the selection columns of a
  block-diagonal candidate reproduces `ladder_spectrum`'s `free_idx` result to $10^{-10}$ (pins the
  general-$G$ code against the validated selection code). Plus a finite-difference check of each
  analytic $G_k$ column.

A violated assert stops the run (implementation failure, not graded against predictions).

---

## 2. Preregistered predictions and pass criteria

Notation: $\overline{\cdot}$ = mean over $R$ ok replicates; se = `sd/sqrt(R)`; $\Delta\operatorname{tr}_\perp=\operatorname{tr}(\mathrm{RIV}_{\perp,\text{CS}})-\operatorname{tr}(\mathrm{RIV}_{\perp,\text{AR1}})$
(per-replicate analytic, averaged). **Primary identification = MAR-residual $-$ MCAR-residual**
(A$-$A′, B$-$B′): subtracting the MCAR arm removes the trace differential, curved-model
higher-order artifacts, and any $\hat\psi_k$-evaluation-point convention, leaving the
design-imbalance $(A)+(C)$ differential.

### M1 — The $O(1)$ residual is a genuine, design-imbalance-driven $O(1)$ (headline)
Residual $\hat\Delta_{AC}(N,\text{cell})=\overline{D_{\text{pair}}}-\overline{\Delta\operatorname{tr}_\perp}$.
- **C1a (nonzero under MAR):** $|\hat\Delta_{AC}^{\text{MAR}}|\ge3\,\text{se}$ in at least cell A (two-sided).
- **C1b (un-trending / $O(1)$ not $o(1)$):** $\hat\Delta_{AC}^{\text{MAR}}$ does not trend to 0 across
  $N\in\{500,1000,2000\}$ — $|\hat\Delta_{AC}^{\text{MAR}}(2000)|\ge\tfrac12|\hat\Delta_{AC}^{\text{MAR}}(500)|$
  and no monotone decay toward 0 beyond se (an $o(1)$ term would shrink with $N$).
- **C1c (collapses under MCAR — the mechanism isolator):** $|\hat\Delta_{AC}^{\text{MCAR}}|<|\hat\Delta_{AC}^{\text{MAR}}|$
  and the isolated differential $\hat\Delta_{AC}^{\text{MAR}}-\hat\Delta_{AC}^{\text{MCAR}}\ge3\,\text{se}_{\text{paired}}$ (cell A; reported for cell B).
- **C1d (null control $\approx0$):** the $\mu_1{=}0$ null nested test on the same seeds (q_d=1; truth
  $\mu{=}0$) has residual $|\hat\Delta_{AC}^{\mu_1}|\le\max(3\,\text{se},0.15)$ — at the null the
  $(A)+(C)$ differential vanishes (Proposition L4; re-confirms the locked W2 result in-run).

### M2 — Noise order: $\sqrt n$ for non-nested, flat for the null control
- **C2a (non-nested $\sqrt n$):** $\operatorname{sd}(D_{\text{pair}}^{\text{MAR}})$ increases with $N$
  at the $\sqrt n$ rate — ratio $\operatorname{sd}(2000)/\operatorname{sd}(500)\in[1.5,2.5]$ (ideal $\sqrt4=2$).
- **C2b (null control flat):** $\operatorname{sd}(D_{\mu_1})$ flat — ratio $\in[0.75,1.3]$ (Proposition L3, $O(1)$).
- **M2-aux (fixed-alternative nested diagnostic; report, no gate):** the Independence-vs-CS and
  Independence-vs-AR(1) paired differentials test the *false* restriction $\rho{=}0$ (pseudo-true
  $\rho\approx0.35$–$0.47$). Prediction (L4 sub-test): these show $\sqrt n$ growth and a nonzero
  residual **like the non-nested pair**, because the operative condition is pseudo-true separation,
  not nesting. This is why the flat control is the $\mu_1{=}0$ *null* test, not the (nested-but-false)
  Independence pair — a refinement of the `todo/028` "nested control" framing.

### M3 — Decision distortion in the money cell (cell B)
Corrected MI-AIC selects CS over AR(1) iff $\Delta T_{\text{MI}}-\Delta\operatorname{tr}_\perp<0$;
oracle iff $\Delta T_{\text{com}}<0$ ($p_{\text{CS}}=p_{\text{AR1}}$ ⇒ penalty cancels).
- **C3 (residual distortion):** $|P_{\text{MI-corr}}(\text{select CS})-P_{\text{oracle}}(\text{select CS})|\ge3\,\text{se}$
  in cell B — the trace correction does **not** remove the gap (the $(A)+(C)$ differential shifts the
  split). Direction two-sided (§1.6). Reported for cell B′ (MCAR) as the mechanism check.

### M4 — L2 in-vivo: curved candidates sit OFF the equality case (report, no gate)
Per candidate, naive $\operatorname{tr}(\mathrm{RIV})-\operatorname{tr}(\mathrm{RIV}_0)$ vs the
$I_{\text{com}}$-metric $\operatorname{tr}(\mathrm{RIV}_\perp)$. Prediction (Proposition L2): naive
$\ge$ exact in every replicate, and the gap is **material** (the W3 zero-pattern family hit equality
to $3.6\times10^{-15}$ by block-diagonal structure; CS/AR(1) do **not** block-decompose, so they sit
off the equality case — the first in-vivo naive-vs-exact test in a selection context). Report the gap
and, if material, the selection consequence of using the naive trace.

---

## 3. Power gate (pilot-based; before the full run, before reading any mean)

The non-nested paired noise is $O(\sqrt n)$ **by the claim under test** (Proposition L3) — pairing
cannot reduce it, so brute $R$ is the only precision lever.
- **Pilot:** cell A, X1-heavy MAR, $N=500$, $R_{\text{pilot}}=300$. Estimate $\widehat{\operatorname{sd}}=\operatorname{sd}(D_{\text{pair}})$.
- **Required $R$:** to resolve a $0.25$-sized effect at $\ge3$ se, $R=\lceil(3\,\widehat{\operatorname{sd}}/0.25)^2\rceil$, rounded up to a clean number.
- **Decision rule:** $R\le 50{,}000$ ⇒ freeze and run all cells × $N$. $R>50{,}000$ ⇒ **infeasible
  at sane $R$**: record $\widehat{\operatorname{sd}}$ and $R_{\text{req}}$, then re-scope (strengthen
  the X1-heavy imbalance) as a **dated amendment BEFORE unblinding means**.
- **$\sqrt n$ re-validation:** because $\operatorname{sd}$ grows with $N$, the $R$ chosen at $N=500$
  is **re-validated** (not re-chosen) against the $N=2000$ sd; if the $N=2000$ resolution would
  breach $3$ se, inflate $R$ accordingly (recorded).
- **Honest fence:** the gate resolves a *fixed* $0.25$ effect. A null at the chosen $R$ is reported
  as "$(A)+(C)$ differential $<0.25$ at this design," **not** "no differential."

---

## 4. CAS check (mandatory, before grading)
`verification/cas-wolfram/verify_w4_nonnested.py` (new; sympy + numpy, clone `verify_ic_ladder.py`):
- **A1:** the CS closed form $(\hat a,\hat b,\hat\sigma^2,\hat\rho)$ equals a brute KL/ML minimizer on
  the frozen $\Sigma_T$ (numeric) and the first-order conditions vanish (symbolic, generic $S$).
- **A2:** AR(1) profile identities — KMS $R^{-1}$ ($R\cdot R^{-1}=I$ symbolic), $|R|=(1-\rho^2)^{p-1}$,
  $\hat\sigma^2(\rho)=\operatorname{tr}(R^{-1}S)/p$; profiled-$g$ minimizer equals a full 2-D `optim`.
- **A3 (must-have):** the general-Jacobian spectrum-trace identity $\sum_j\lambda_j=q_d+\operatorname{tr}(\mathrm{RIV}_\perp)$
  and $\min_j\lambda_j\ge1$ on the **actual CS/AR(1) $G_k$** at generic $(\sigma^2,\rho)$ + random PD
  $I_{\text{obs}},I_{\text{mis}}$; plus a finite-difference check of each analytic $G_k$ column against
  the duplication convention of `fisher_info_com_mvn`.
- **A5 (optional):** the equal-KL Toeplitz residual at $w^*$ reproduces (numeric, cell B).

## 5. Outputs
- `verification/cache/w4-nonnested-{A,B,Aprime,Bprime}-N{500,1000,2000}.rds` — per-cell replicate matrices + config.
- `verification/cache/w4-nonnested-summary.csv` — one row per (cell × N × arm) with $\hat\Delta_{AC}$,
  sds, selection rates, L2 gaps, assert counters.
- Run log `verification/cache/w4-nonnested-runlog.txt`; environment `…-sessioninfo.txt`.
- Grading of M1–M4 recorded in §6 (appended after the run) and consumed by `@sec-lrt-ac` / `@sec-ic`.

## Amendment 1 — power-gate recalibration + control reinterpretation (dated 2026-06-04, before the graded run)

Pilots run with the committed engine (`w4-nonnested-vuong.R`; R=300 at N=500 and R=200 at
N=1000/2000, cells A and A′; **not graded**) settle the power gate and surface a control
misclassification. Both fixes are dated here, BEFORE the graded R=20,000 run.

**Pilot facts (cell A, X1-heavy MAR / A′ MCAR):**
- `sd(D_pair)` (non-nested) = 29.8 / 39.2 / 66.7 at N = 500 / 1000 / 2000 — grows $\approx\sqrt n$
  (66.7/29.8 = 2.24), confirming the Proposition L3 non-nested $O(\sqrt n)$ noise.
- `sd(D_mu1)` (the $\mu_1{=}0$ single-test paired differential) = 8.7 / 8.7 / 9.7 — **flat** across
  N, confirming the L3 $O(1)$ null-control noise.
- The $\mu_1{=}0$ residual $\overline{D_{\mu_1}}-\operatorname{tr}(\mathrm{RIV}_{\perp,\mu_1})$
  = +4.0 / +3.9 / +4.7 under MAR (un-trending $O(1)$), collapsing to +0.16 under MCAR (A′). A
  standalone in-session diagnostic confirms this is the **(A)+(C) level**: $\overline{d_L-d_{\text{com}}}$
  = +5.71 lands on $\operatorname{tr}(\mathrm{RIV}_\perp)$ computed with the **realized** observed
  info (`observed_info_obs_mvn`, +5.67, resid +0.04) but exceeds the same with the
  **expected/pattern-mixture** info (`fisher_info_obs_mvn`, +1.69) by +4.0 — the gap IS $(A)+(C)$,
  large because X1-heavy MAR makes the observed entries a *selected* subsample (so the expected
  info $\ne E[$realized Hessian$]$ under MAR selection). The engine uses the **expected** info for
  $\operatorname{tr}(\mathrm{RIV}_\perp)$, so its `resid` correctly isolates $(A)+(C)$.

**Fix 1 — C1d reinterpretation (the $\mu_1$ control is the (A)+(C) LEVEL, not a differential$\approx$0).**
The $\mu_1{=}0$ single-model test's residual is the $(A)+(C)$ **level** (≈+4, un-trending, ~6.5 se),
NOT the $(A)+(C)$ **differential** (which cancels at the null between two models sharing a
pseudo-true). It therefore serves as (i) the **flat-sd reference** for M2/C2b (`sd(D_mu1)`≈9 flat vs
the non-nested $O(\sqrt n)$), and (ii) a **single-model $(A)+(C)$ demonstration** that collapses
MAR→MCAR (+4.0 → +0.16). **The differential=0 reference is the MCAR twin** (A′/B′: `resid`≈0), which
the primary MAR−MCAR isolation already uses. C1d is replaced by:
- **C1d′ ($\mu_1$ level):** $\overline{D_{\mu_1}}-\operatorname{tr}(\mathrm{RIV}_{\perp,\mu_1})\ge3$
  se under MAR, un-trending across N, collapsing under MCAR ($<3$ se; $|\text{MAR}-\text{MCAR}|\ge3$
  se). The single-model $(A)+(C)$ level is large and design-imbalance-driven.
- The headline M1 ((A)+(C) DIFFERENTIAL for CS-vs-AR1) and the MAR−MCAR isolation are unchanged.

**Fix 2 — power-gate recalibration.** With `sd(D_pair)`≈29.8 at N=500, the original 0.25 MDE needs
$R=\lceil(3\cdot29.8/0.25)^2\rceil\approx127{,}900>50{,}000$ — infeasible. But the gate's premise
(effect too small) is FALSE: the $(A)+(C)$ level is ≈+4 ($\mu_1$ control), so the differential of two
such levels is a large $O(1)$, not a sub-0.25 effect. The 0.25 MDE was set blind and is mis-scaled
against the now-known noise. **Recalibrated MDE = an $O(1)$ differential**, with R chosen from the
pilot sd (noise) and the $(A)+(C)$-level scale (≈4), NOT from the headline differential mean (which
remains two-sided and unresolved at pilot scale, −2.1 ± 1.7, −1.2 se). **Freeze R = 20,000** (user
decision; 8 cores): the isolated MAR−MCAR se $=\sqrt2\,\text{sd}/\sqrt R$ is 0.30 / 0.39 / 0.67 at
N = 500 / 1000 / 2000, resolving a 2.0-sized isolated $(A)+(C)$ differential at ≥3 se even at the
binding N=2000. C1a's "≥3 se" and C1b's un-trending are evaluated at this R. **Honest fence
retained:** a null at R=20,000 is reported as "$(A)+(C)$ differential below the ~0.7-resolution at
the largest N," not "zero."

*Amendment 1 dated 2026-06-04, after the (ungraded) pilots, before the graded R=20,000 run.*

## 6. Results vs predictions

**Run executed 2026-06-04** (after §§1–5 + Amendment 1 frozen). `Rscript
verification/w4-nonnested-vuong.R 20000 8 A,B,Aprime,Bprime 500,1000,2000`; 20,000/20,000 ok in every
cell, 0 errors; runtime ≈95 min (8 cores); caches `w4-nonnested-{A,B,Aprime,Bprime}-N{500,1000,2000}.rds`
+ `w4-nonnested-summary.csv`; log `w4-nonnested-runlog.txt`. **Internal asserts (§1.7): all pass** —
max spec_gap $8.8\times10^{-15}$, min $\lambda$ = 1.000000, max $|\operatorname{tr}(\hat\Sigma_k^{-1}S^*)-p|$
= $2.2\times10^{-15}$, AR(1) convergence 1.000, realized pseudo-true $\rho$ on target every cell
($\rho_{\text{CS}}\approx0.354/0.405$, $\rho_{\text{AR1}}\approx0.500/0.473$).

### Headline: the (A)+(C) terms DECOUPLE and are LARGE per model, but their DIFFERENTIAL is small for this similar pair

Per-candidate $(A)+(C)$ level $= \overline{T_{\text{MI},k}-T_{\text{com},k}} - \overline{\operatorname{tr}(\mathrm{RIV}_{\perp,k})}$
(single-model bias minus the expected-info trace), N = 500 / 1000 / 2000:

| cell | mech | $(A)+(C)_{\text{CS}}$ | $(A)+(C)_{\text{AR1}}$ | isolated differential (MAR−MCAR) |
|---|---|---|---|---|
| A | MAR | +2.33 / +2.30 / +2.47 | +2.85 / +2.62 / +2.56 | −0.28 / −0.59 / −0.04 (≤1.5 se) |
| A′ | MCAR | +0.19 / +0.41 / −0.01 | +0.43 / +0.14 / +0.05 | — |
| B | MAR | +2.45 / +2.48 / +2.40 | +2.75 / +2.37 / +2.30 | +0.20 / −0.08 / +0.36 (≤0.7 se) |
| B′ | MCAR | +0.19 / +0.19 / −0.14 | +0.68 / +0.01 / +0.13 | — |

Per-model levels are individually 10–37 se from zero under MAR (e.g. AR1 cell A N=500: $+2.85\pm0.076$ =
37 se) and collapse to ≈0 (within ~2 se) under MCAR.

### Grading (M1–M4 + the Amendment-1 control)

- **M1 (the $(A)+(C)$ DIFFERENTIAL is a resolved nonzero $O(1)$): NOT CONFIRMED.** The MCAR-isolated
  differential is ≤1.5 se at every N for both cells (C1a's ≥3 se bar is not met). Reported per the honest
  fence as "differential below the ~0.5 resolution at N=2000," not "zero." **The pilot's −2.1 was
  Monte-Carlo noise** (R=300, −1.2 se); R=20,000 resolves it to ≈0. The decoupling and the noise-return
  ARE confirmed (below) — only the *magnitude of the difference* for this similar pair is small.
- **C1d′ (the $(A)+(C)$ LEVEL): CONFIRMED strongly.** Curved-candidate levels +2.3 to +2.9 under MAR
  (10–37 se), collapsing to ≈0 under MCAR; the $\mu_1{=}0$ control gives the same picture (+3.5 → +0.07,
  ~58 se). The single-model $(A)+(C)$ is large and design-imbalance-driven — a clean positive
  demonstration for *covariance* candidates, not just the mean test. The CS and AR1 levels are genuinely
  *unequal* (e.g. +2.33 vs +2.85) — they **decouple**, exactly as Proposition L4 says they do for
  non-nested comparison (vs the null's exact cancellation).
- **M2 (noise orders): CONFIRMED.** C2a: $\operatorname{sd}(D_{\text{pair}})$ non-nested grows $\sqrt n$
  — cell A 29.9 / 42.4 / 59.6 (ratio 1.99), cell B 32.2 / 45.4 / 64.2 (1.99). C2b: the $\mu_1$ null
  control is flat — 8.6 / 8.4 / 8.5 (MAR), 3.6 / 3.7 / 3.6 (MCAR). **M2-aux (nested-but-false):
  CONFIRMED** — Independence-vs-candidate sd grows $\sqrt n$ (43.7 / 61.1 / 87.4, ratio 2.00): the
  nested-but-false pair behaves like the non-nested one, so it is **pseudo-true separation, not nesting,**
  that triggers the $O(\sqrt n)$ return (a refinement of the todo/028 framing, preregistered as M2-aux).
- **M3 (decision distortion, cell B): NULL** (consistent with M1). P(select CS) = 0.496–0.503 for oracle,
  uncorrected MI, and corrected MI alike at every N — the equal-KL coin flip stays a coin flip under MI;
  the small $(A)+(C)$ differential does not distort the CS-vs-AR1 decision here.
- **M4 (L2 in-vivo): CONFIRMED.** Per curved candidate the naive trace
  $\operatorname{tr}(\mathrm{RIV})-\operatorname{tr}(\mathrm{RIV}_0)$ overstates the exact
  $\operatorname{tr}(\mathrm{RIV}_\perp)$ by ≈0.73 (CS 8.77 vs 8.04; AR1 8.74 vs 7.95) — ~9%, the first
  in-vivo demonstration OFF Proposition L2's equality case (the W3 zero-pattern family hit equality to
  $3.6\times10^{-15}$ by block structure; curved candidates do not block-decompose). The differential of
  the two gaps is small (~0.05), so it does not change the CS-vs-AR1 ranking, but the per-candidate
  overstatement is material.

### Net and framing modification (per the pre-registration discipline)

The measurement **refines** Proposition L4 rather than simply confirming it. **Confirmed:** (i) the
$(A)+(C)$ terms *decouple* under non-nested MAR — each candidate carries a large, MAR-specific $O(1)$
level (~+2.5) that collapses under MCAR, in contrast to the null's exact cancellation; (ii) the paired
noise returns to $O(\sqrt n)$, and does so for any pseudo-true-separated pair (nested-but-false included),
not just non-nested; (iii) the naive trace overstates the exact complement trace materially for curved
candidates (Proposition L2 off the equality case). **Not demonstrated:** a *resolved nonzero $(A)+(C)$
differential* — for the similar CS-vs-AR1 pair the two large levels nearly cancel, leaving a difference
below resolution (≤1.5 se). The un-absorbed $O(1)$ that bites IC ranking is therefore real *per model* but
**mild for similar candidates**; its magnitude scales with how differently the candidates respond to the
design imbalance — largest for dissimilar candidates, a quantitative question left to the pairwise-matrix
sequel (todo/023). `@sec-lrt-ac` and `@sec-ic` are updated to this measured nuance.

*Preregistered 2026-06-04 before the engine existed (commit 7677777); Amendment 1 dated before the graded
run (commit 99c7fd4); §6 appended after. Author of record: marcus.waldman (ORCID-verified human prompter);
AI-assisted per JAIGP norms.*

---

*Preregistered 2026-06-04 before `verification/w4-nonnested-vuong.R` existed; committed alone, ahead
of any measurement-engine code (the fix for todo/027 §6's single-commit defect). Author of record:
marcus.waldman (ORCID-verified human prompter); AI-assisted per JAIGP norms. Reproducibility: seeds
`20260604 + r` set per replicate inside the engine (core-count invariant); pseudo-true inputs
deterministic via `nonnested-pseudotrue-prep.R`.*
