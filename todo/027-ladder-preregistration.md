# Todo 027 — PREREGISTRATION: the IC calibration ladder (saturated-anchored, rungs 0–3)

**Status:** PREREGISTERED 2026-06-04, **before any ladder code was written**. Spec lineage:
todo/026 REVISION 2 (the in-paper ladder decision); design record todo/023 (the 2026-06-03
discussion, extract at `verification/cache/_equating_extract.txt`); analytic assets locked in
`derivation.qmd @sec-lrt` (Propositions L1–L4 — restated below, never re-derived). The frozen
preregistered originals (`W1-bias-decomposition.R`, `W2-lrt-power.R`, `W3-model-selection.R`,
`_modules/w3-sweep.R`) are **not touched and not re-run**; the ladder is a NEW script,
`verification/ic-ladder.R`.

Predictions and pass criteria in this file were written before the script existed. If reality
differs, the framing in `@sec-ic` modifies to match reality — failures are reported, not
re-run away. Any amendment to this file after the first run is dated and labelled.

---

## 1. Objects and constructions (fixed before code)

### 1.1 Design (carried from the W3 sweep, `00-setup.R`)

- 4-variate MVN, $\mu_0 = 0$, truth $\Sigma_0 = $ `w3_sigma(rho)`: $\sigma_{13} = \sigma_{24} =
  \rho$, all other off-diagonals 0.
- Candidates (zero-pattern covariance submodels of the saturated MVN; `W3_FREE_IDX`):
  - **MA** diagonal (8 params, $q_d = 6$ tested directions vs saturated)
  - **MB** $\sigma_{12}, \sigma_{34}$ free (10 params, $q_d = 4$) — junk directions under truth
  - **MC** $\sigma_{13}, \sigma_{24}$ free (10 params, $q_d = 4$) — TRUE model when $\rho > 0$
  - **MD** = saturated (14 params, $q_d = 0$) — **the anchor and the congenial imputation model**
- Missingness: `apply_missingness_ampute(X, prop = 0.40, mech = "MAR", pattern_type =
  "non_monotone")` — the headline W3 fiml cell's configuration.
- Engine: deterministic-FIML $\bar Q_\infty$ (imputation parameter = the saturated FIML
  estimate $\hat\theta_{\text{obs}}$), matching the scope of the @sec-lrt propositions.
  Engine-sensitivity is settled (todo/017: NOT SENSITIVE); no Amelia arm here.

### 1.2 The working statistic — Chan-style maximizers, not plug-in

Per `@sec-lrt-setup`, the MI deviance for candidate $k$ vs the saturated anchor is
$$T_k = 2[\bar Q_\infty(\hat\psi^*_{\text{sat}}) - \bar Q_\infty(\hat\psi^*_k)], \qquad
\hat\psi^*_k = \arg\max_{\theta \in M_k} \bar Q_\infty(\theta),$$
with $\hat\psi^*_{\text{sat}} = \hat\theta_{\text{obs}}$ by EM self-consistency. Concretely:
compute the E-step moments $(m^*, S^*)$ at the saturated FIML fit; then $\hat\psi^*_{\text{sat}}
= (m^*, S^*)$ and, because every candidate is a block-diagonal zero pattern (MA: blocks
$\{1\},\{2\},\{3\},\{4\}$; MB: $\{1,2\},\{3,4\}$; MC: $\{1,3\},\{2,4\}$), each constrained
$\bar Q_\infty$-maximizer is **closed-form**: $\hat\mu_k = m^*$, $\hat\Sigma_k =$ the
block-diagonal restriction of $S^*$, giving
$$T_k = N\,[\log|\hat\Sigma_k| - \log|S^*|] \;\ge\; 0.$$
The complete-data counterpart $T_{\text{com},k}$ is the same construction on the complete-data
moments. **Design note (recorded before running):** the frozen W3 arm evaluated $\bar Q$ at each
candidate's own observed-data FIML estimate (a plug-in that differs from $\hat\psi^*_k$ by an
$O_p(1)$ deviance term and can go negative); the ladder uses the $\hat\psi^*$ construction the
derived theory prices. This is a definitional improvement in a NEW script, not an edit to the
frozen arm.

AIC on the anchored scale: $s_k = T^{(\text{rung})}_k + 2\,p_k$ with $p_k$ the candidate's
parameter count ($T_{\text{MD}} = 0$); select $\arg\min_k s_k$ over {MA, MB, MC, MD}. This
ranking is identical to MI-AIC ranking (the saturated terms are a common shift).

### 1.3 The analytic null law and the three rungs

From `@sec-lrt` (locked): at candidate $k$'s own null, $T_k \rightsquigarrow \sum_{j=1}^{q_{d,k}}
\lambda_{k,j}\,\chi^2_1$ with $\lambda_{k,j} = 1 + r_{\perp,k,j} \ge 1$ and $\sum_j \lambda_{k,j}
= q_{d,k} + \operatorname{tr}(\mathrm{RIV}_{\perp,k})$ (@eq-lrt-bias; Chan 2022 AoS eq. 1.10).
Operationally, $\lambda_{k,j}$ = the $q_{d,k}$ nonzero eigenvalues of
$$P_k = \big[I_{\text{com}}^{-1} - G_k (G_k^\top I_{\text{com}} G_k)^{-1} G_k^\top\big]\,
I_{\text{com}}\, I_{\text{obs}}^{-1}\, I_{\text{com}},$$
with all matrices the full 14-dim analytic informations evaluated at $\hat\psi^*_k$ and $G_k$
the selection matrix of the candidate's free indices. (That the nonzero spectrum of $P_k$ is the
null-law weight set is immediate from the quadratic-form representation of $\hat d_L$ in
@sec-lrt-bias: $T_k = Z^\top A Z + o_p(1)$, $Z \sim N(0, V)$, $A = I_{\text{com}}^{-1} -
G(G^\top I_{\text{com}}G)^{-1}G^\top$, $V = I_{\text{com}} I_{\text{obs}}^{-1} I_{\text{com}}$,
and the law of a Gaussian quadratic form is the weighted $\chi^2$ with weights
$\operatorname{eig}(AV)$.)

The rungs, each applied per candidate (MD passes through as 0):

- **Rung 0 (uncorrected):** $T^{(0)}_k = T_k$.
- **Rung 1 (mean / first moment):** $T^{(1)}_k = T_k - \operatorname{tr}(\mathrm{RIV}_{\perp,k})$
  — the I_com-metric complement trace of @eq-lrt-bias, **not** the naive
  $\operatorname{tr}(\mathrm{RIV}) - \operatorname{tr}(\mathrm{RIV}_0)$ (Proposition L2). Linear
  per-model shift ⇒ coherent across all pairs, telescopes.
- **Rung 2 (SB two-moment, coefficients DERIVED):** match mean and variance of the analytic null
  law to $\chi^2_{q_{d,k}}$. Since $E[\sum\lambda\chi^2_1] = \sum\lambda_j$ and
  $\operatorname{Var} = 2\sum\lambda_j^2$, the unique affine map is
  $$T^{(2)}_k = a_k T_k + b_k, \qquad a_k = \sqrt{q_{d,k} / \textstyle\sum_j \lambda_{k,j}^2},
  \qquad b_k = q_{d,k} - a_k \textstyle\sum_j \lambda_{k,j},$$
  equivalently $a_k\,(T_k - \operatorname{tr}(\mathrm{RIV}_{\perp,k})) + q_{d,k}(1 - a_k)$ — the
  issue-#1 "wrap the bias correction" form with derived coefficients. Provenance of the
  scaled-and-shifted form: Satorra–Bentler / Asparouhov–Muthén (both held); the coefficients here
  are derived from the @sec-lrt law, not borrowed.
- **Rung 3 (equipercentile equating, per-model, under its own null):**
  $$T^{(3)}_k = F^{-1}_{\chi^2_{q_{d,k}}}\big(F_{W_k}(T_k)\big), \qquad
  W_k = \textstyle\sum_j \lambda_{k,j}\chi^2_1,$$
  with $F_{W_k}$ evaluated **closed-form** by Imhof/Davies numerical inversion
  (`CompQuadForm::imhof`, confirmed installed; Chan-style MC reference only as fallback if the
  inversion fails — failures counted and reported, preregistered tolerance < 1% of replicates).

**Protocol note (cross-model gate).** Rungs 2–3 are stated as two-line corollaries of the
already-gate-cleared Proposition L1 + Chan's weighted-$\chi^2$ law (moment matching and the
probability integral transform are textbook). Per todo/026 rev. 2 the GPT-5.5 gate fires only if
these are formalized beyond that; **decision: not triggered**. The CAS check (§4) is mandatory
and runs before the simulation is graded.

### 1.4 Cells (all N = 500, R = 2000 per cell, seeds `20260604 + r`, few-core PSOCK ≤ 8)

| Cell | Truth | True model | Purpose |
|---|---|---|---|
| MAIN | `w3_sigma(0.40)` | MC | the headline regime (comparable to `fiml_non_monotone_MAR_N500`: oracle 0.898 / corrected 0.816 / uncorrected 0.674) |
| WEAK | `w3_sigma(0.10)` | MC | near-tied / weak-coefficient stress cell — where equating's underfit-retention cost should appear |
| JUNK | `w3_sigma(0.00)` | MA | junk-heavy: every candidate ⊇ truth, ALL anchored statistics are null-type — the pure calibration-win regime |

R = 2000 gives MC se on selection rates ≈ 0.010 and two-sample-KS noise floor ≈ 0.043 (5%
critical). If runtime forces a reduction, the floor is R = 1000 with criteria C1–C6 evaluated at
correspondingly inflated se — recorded as an amendment, not silently.

### 1.5 Per-replicate internal asserts (gates on the run itself)

- Spectrum identity: $|\sum_j \lambda_{k,j} - (q_{d,k} + \operatorname{tr}(\mathrm{RIV}_{\perp,k}))|
  \le 10^{-6}\max(1, \sum_j\lambda_{k,j})$ for every candidate, every replicate.
- Weight bound: $\min_j \lambda_{k,j} \ge 1 - 10^{-6}$ (each null-law weight exceeds 1; the
  multiplicative-monotonicity argument from $V \succeq I_{\text{com}}$).
- $T_k \ge 0$ exactly (nested maximization of the same $\bar Q_\infty$).
- Imhof fallback count < 1% of replicates per cell.

A violated assert stops the run and is reported as an implementation failure (not graded
against the predictions).

---

## 2. Preregistered predictions and pass criteria

Notation: $\pi^{(j)}$ = fraction of replicates whose rung-$j$ AIC selects the cell's true model;
$\pi^{\text{orc}}$ = the complete-data (oracle) AIC rate; $D_{KS}(\cdot)$ = two-sample
Kolmogorov–Smirnov distance against the paired complete-data sample of the same statistic.
"se" = the relevant Monte-Carlo standard error; paired quantities use paired se (Proposition L3:
the paired differential is $O(1)$, so paired contrasts are the only estimators used — the
heavy-tail guardrail).

### P1 — Null-side ladder: each rung closes more of the calibration gap (MAIN cell, T_MC)

The true model's anchored statistic $T_{\text{MC}}$ is a null LRT statistic ($q_d = 4$).
Mechanism: rung 1 fixes the mean only; rung 2 the mean and variance; rung 3 the whole
distribution (PIT exact up to the asymptotic approximation at N = 500 and plug-in spectrum
noise).

**Pass criteria:**
- C1a (monotone KS): $D_{KS}(T^{(3)}) \le D_{KS}(T^{(2)}) \le D_{KS}(T^{(1)}) \le D_{KS}(T^{(0)})$,
  no inversion exceeding 0.02 (the KS MC noise scale at R = 2000).
- C1b (equating ≈ exact): $D_{KS}(T^{(3)}) \le 0.08$.
- C1c (variance): $\operatorname{Var}(T^{(1)})/\operatorname{Var}(T_{\text{com}}) \ge 1.5$
  (mean correction leaves the variance inflation), while
  $\operatorname{Var}(T^{(2)})/\operatorname{Var}(T_{\text{com}})$ and
  $\operatorname{Var}(T^{(3)})/\operatorname{Var}(T_{\text{com}})$ both fall in $[0.8, 1.2]$.
- C1d (means): paired mean gap $|\overline{T^{(j)} - T_{\text{com}}}| \le \max(3\,\text{se}_{\text{paired}},\ 0.15)$
  for $j = 1, 2, 3$ (all three rungs are first-moment-correct at the null).

### P2 — Equating is exact on null pairs generally (JUNK cell, all three statistics)

In the JUNK cell every candidate contains the truth, so $T_{\text{MA}}$ ($q_d{=}6$),
$T_{\text{MB}}$, $T_{\text{MC}}$ ($q_d{=}4$) are all null-type.

**Pass criterion C2:** $D_{KS}(T^{(3)}_k) \le 0.08$ for each of the three candidates.

### P3 — The noncentral side: rungs 2–3 are CONSERVATIVE; only rung 1 preserves the evidence level

Mechanism (the 11-vs-21 toy, sharpened): under misspecification $T_k$ is noncentral; the null
equating map divides the far tail by $\approx \lambda_{\max}$ and the SB map scales by
$a_k \approx (\text{RMS of } \lambda)^{-1} < 1$, while the rung-1 shift is $O(1)$ against an
$O(n)$ level. No observable transform restores the information the missing data destroyed; the
upper rungs *actively shrink* the evidence against misspecified models — that is the price of
null-side calibration.

**Pass criteria (MAIN cell, underfit MA):**
- C3a: $\overline{T^{(3)}_{\text{MA}}} / \overline{T_{\text{com,MA}}} \le 0.85$ and
  $\overline{T^{(2)}_{\text{MA}}} / \overline{T_{\text{com,MA}}} \le 0.85$ (predicted
  $\approx 1/\lambda_{\max}$ and $\approx a_k$ respectively).
- C3b: $\overline{T^{(1)}_{\text{MA}}} / \overline{T_{\text{com,MA}}} \in [0.90, 1.10]$ (the
  first moment of the *level* is preserved at leading order — imputation under the consistent
  saturated fit recovers the complete-data population mean of the deviance, and the rung-1
  shift corrects the $O(1)$ bias).

### P4 — Selection ladder in the pure-null regime (JUNK cell)

Mechanism: with all pairs null-type, selection error is purely overfit seduction, which is
exactly what the variance/distribution rungs calibrate. The uncorrected arm's known failure mode
(100% of misclassifications land on the largest-RIV candidate, W3-C = 1.0) is maximal here.

**Pass criteria:**
- C4a (monotone): $\pi^{(3)} \ge \pi^{(2)} \ge \pi^{(1)} \ge \pi^{(0)}$, inversions ≤ 0.02.
- C4b (magnitude): $\pi^{(3)} - \pi^{(0)} \ge 0.6\,(\pi^{\text{orc}} - \pi^{(0)})$, applicable
  if $\pi^{\text{orc}} - \pi^{(0)} \ge 0.05$ (else the cell is uninformative and C4b is void).

### P5 — Where the residual lives: variance-fixable in MAIN, information-loss floor in WEAK

Mechanism: in MAIN, the corrected arm's residual against oracle is predicted to be mostly
overfit-flip (variance) error, which rungs 2–3 remove; the irreducible information-loss floor
binds where discrimination is hard (WEAK), not where margins are huge (MAIN).

**Pass criteria:**
- C5a (MAIN): $\pi^{(3)} - \pi^{(1)} \ge 0.5\,(\pi^{\text{orc}} - \pi^{(1)}) - 2\,\text{se}$ —
  the distribution rung closes at least half the remaining gap.
- C5b (WEAK): $\pi^{\text{orc}} - \pi^{(3)} \ge \max(0.02,\ 2\,\text{se})$ — the floor persists;
  no rung reaches oracle in the hard regime.
- C5c (no harm where evidence is strong, MAIN): $\pi^{(3)} \ge \pi^{(1)} - 0.02$.

### P6 — Underfit-retention cost of the upper rungs (WEAK cell)

Mechanism: P3's conservatism costs exactly in the near-tied regime — the shrunken noncentral
gaps keep underfit candidates alive.

**Pass criterion C6:** underfit-selection rate (MA or MB chosen) under rung 3 exceeds the
oracle's underfit rate by $\ge 2\,\text{se}$. **Directional watch (no gate):** $\pi^{(3)} \le
\pi^{(1)} + 2\,\text{se}$ in WEAK — equating is not predicted to beat the mean rung where
selection is hard; if it does, that finding is reported as a surprise.

### P7 — Rung 2 (derived) vs the committed SB arm (report, no gate)

Report, side by side, in MAIN: the derived rung-2 statistic vs the frozen W3 SB arm's functional
form (scaled-shift applied to the uncorrected statistic, naive trace difference and naive
$\sum\lambda^2$ difference as inputs — the issue-#1 construction). Also report the naive trace
$\operatorname{tr}(\mathrm{RIV}) - \operatorname{tr}(\mathrm{RIV}_0)$ alongside
$\operatorname{tr}(\mathrm{RIV}_\perp)$ per candidate (Proposition L2 predicts naive ≥ exact in
every replicate; in the W3 design the gap is expected small — the design sits near the
invariance case — and that magnitude is the issue-#1 closure evidence).

### P8 — Indirect-pair diagnostic (LIGHT; WEAK cell; report, no gate)

One measurement, per todo/026: the near-tied MB-vs-MC pair. Report mean and sd of
$(s^{(3)}_{\text{MB}} - s^{(3)}_{\text{MC}})$ against the complete-data
$\Delta\text{AIC}(\text{MB}, \text{MC})$ distribution, plus
$\operatorname{corr}(s^{(3)}_{\text{MB}}, s^{(3)}_{\text{MC}})$ under MI vs the complete-data
analog. Per-model marginal equating cannot calibrate difference distributions in general (the
copula is invariant under marginal transforms); this measures how much that costs here. The
instrumented pairwise-matrix-with-Z testbed stays sequel (todo/023).

---

## 3. Honest-claim fences (carried into @sec-ic verbatim in spirit)

1. All-moment matching is claimed ONLY per pair under that pair's own null.
2. Noncentral matching is impossible in principle — information loss is not equatable; no
   monotone transform built from observed data restores destroyed Fisher information. The upper
   rungs trade noncentral evidence for null calibration (P3).
3. Per-model marginal equating cannot calibrate difference distributions in general (copula
   invariance); indirect pairs inherit unquantified distortion (P8 measures one instance).
4. The ladder is presented as common-reference (saturated-anchored) calibration; rungs 2–3 are
   nonlinear/affine-per-model and do NOT telescope — only rung 1 is coherent across all pairs
   simultaneously.
5. Never claim the ladder "restores complete-data selection" — the preregistered prediction is
   that it does NOT (P5b, P6).

## 4. CAS check (mandatory, before grading)

`verification/cas-wolfram/verify_ic_ladder.py` (new file; sympy + numpy):

- L-A1: $E[\sum\lambda_j\chi^2_1] = \sum\lambda_j$, $\operatorname{Var} = 2\sum\lambda_j^2$
  (symbolic).
- L-A2: the rung-2 $(a, b)$ is the unique affine two-moment match, and the two stated forms
  ($a T + b$ vs $a(T - \operatorname{tr}\mathrm{RIV}_\perp) + q_d(1-a)$) are identical (symbolic).
- L-A3: spectrum-trace identity $\sum_j \lambda_j(P) = q_d + \operatorname{tr}(\mathrm{RIV}_\perp)$
  on random PD instances (numeric, ≥ 200 instances, tol 1e-8), plus $\min_j \lambda_j \ge 1$.
- L-A4: PIT exactness of rung 3 through the Imhof CDF: samples of $\sum\lambda\chi^2$ mapped by
  $F^{-1}_{\chi^2_q}(F_W(\cdot))$ pass a KS test against $\chi^2_q$ at the MC tolerance
  (numeric).

## 5. Outputs

- `verification/cache/ic-ladder-{MAIN,WEAK,JUNK}.rds` — per-cell replicate matrices + cell config.
- `verification/cache/ic-ladder-summary.csv` — one row per cell × arm with $\pi$, the P1–P3
  distributional measures, assert counters.
- Run log `verification/cache/ic-ladder-runlog.txt`.
- Grading of P1–P8 recorded in this file (§6, to be appended) and consumed by `@sec-ic`.

## 6. Results vs predictions

**Run executed 2026-06-04**, same session, after §§1–5 were frozen and the CAS check passed
(`verify_ic_ladder.py`: ALL PASS, L-A1–L-A4). `Rscript verification/ic-ladder.R 2000 6
MAIN,WEAK,JUNK`; ok = 2000/2000 in every cell, 0 errors; log
`verification/cache/ic-ladder-runlog.txt`; caches `ic-ladder-{MAIN,WEAK,JUNK}.rds` +
`ic-ladder-summary.csv`.

**Internal asserts (§1.5): all pass.** max spectrum-identity gap $3.1\times10^{-15}$; min
null-law weight $= 1.000000$; Imhof fallbacks 0.000% (closed-form equating used on every
replicate); $T_k \ge 0$ everywhere.

**Selection rates** ($\pi$(true), MC se $\approx 0.010$):

| Cell | oracle | rung 0 | rung 1 | rung 2 | rung 3 | frozen-SB form |
|---|---|---|---|---|---|---|
| MAIN | 0.899 | 0.678 | 0.814 | **0.904** | **0.903** | 0.824 |
| WEAK | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 | 0.658 |
| JUNK | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 | 0.596 |

**Grading (all preregistered criteria PASS):**

- **C1a PASS** (MAIN, $T_{\text{MC}}$): $D_{KS}$ ladder $0.281 \ge 0.228 \ge 0.026 \ge 0.019$,
  strictly monotone, no inversion.
- **C1b PASS**: $D_{KS}(T^{(3)}) = 0.019 \le 0.08$ — at the two-sample-KS noise floor
  ($0.043$ at 5%, $n{=}m{=}2000$): the equated null statistic is *statistically
  indistinguishable* from the complete-data statistic.
- **C1c PASS**: $\operatorname{Var}$ ratios $3.18\,/\,3.17\,/\,0.98\,/\,0.97$ — rung 1 leaves the
  variance inflation (3.17 ≥ 1.5); rungs 2–3 land within $[0.8, 1.2]$.
- **C1d PASS**: paired mean gaps $+2.93$ (rung 0) $\to$ $0.076 \pm 0.100$ / $0.015$ / $0.015$
  (rungs 1–3) — and rung 1's gap sits within 1 paired se of zero, a direct confirmation of
  @eq-lrt-bias at $q_d = 4$.
- **C2 PASS** (JUNK, all three null statistics): $D_{KS}(T^{(3)}) = 0.035 / 0.023 / 0.023$ for
  MA/MB/MC, all $\le 0.08$.
- **C3a PASS** (MAIN, underfit MA): noncentral mean ratios $0.586$ (rung 2, predicted
  $\approx a_k = 0.570$) and $0.362$ (rung 3, predicted $\approx 1/\lambda_{\max} = 1/2.511 =
  0.398$) — both $\le 0.85$; the upper rungs shrink the evidence as predicted, by almost
  exactly the predicted factors.
- **C3b PASS**: rung-1 ratio $1.002 \in [0.90, 1.10]$ — the mean rung preserves the evidence
  level.
- **C4a PASS** (JUNK): $0.422 \le 0.585 \le 0.702$, then $0.696$ (single adjacent inversion
  $0.006 \le 0.02$).
- **C4b PASS**: $\pi^{(3)} - \pi^{(0)} = 0.274 \ge 0.6\,(\pi^{\text{orc}} - \pi^{(0)}) = 0.183$
  (the ladder closes 90% of the junk-cell gap).
- **C5a PASS** (MAIN): $\pi^{(3)} - \pi^{(1)} = 0.089 \ge 0.5\,(\pi^{\text{orc}} - \pi^{(1)})
  = 0.043$ — rungs 2–3 close the *entire* remaining gap; $0.904/0.903$ vs oracle $0.899$ is
  within MC noise (the conservative tilt happens to trade invisibly-cheap underfit retention
  for the binding overfit-flip error mode at $\rho = 0.40$).
- **C5b PASS** (WEAK): $\pi^{\text{orc}} - \pi^{(3)} = 0.170$ — the information-loss floor is
  large and real exactly where discrimination is hard.
- **C5c PASS** (MAIN): $\pi^{(3)} = 0.903 \ge \pi^{(1)} - 0.02$.
- **C6 PASS** (WEAK): underfit-selection rate $0.270$ (rung 3) vs $0.091$ (oracle), excess
  $0.179 \approx 13$ se. Directional watch confirmed: $\pi^{(3)} = 0.650 = \pi^{(1)}$ — the
  upper rungs add nothing to selection accuracy in the hard regime; their null-side
  calibration win ($D_{KS} = 0.019$, var ratio $1.01$) is fully offset by underfit retention.

**P7 (report).** The frozen W3 SB functional form (issue #1: scaled-shift on the uncorrected
statistic, naive-difference inputs) scores $0.824 / 0.658 / 0.596$ vs the derived rung 2's
$0.904 / 0.648 / 0.702$ — the derived coefficients are worth $+0.08$–$0.11$ where calibration
binds (MAIN, JUNK) and $-0.01$ in WEAK (milder shrinkage retains slightly less underfit).
**Unpredicted finding (derived post hoc, simple):** in this candidate family the naive trace
difference equals $\operatorname{tr}(\mathrm{RIV}_\perp)$ **to machine precision**
($3.6\times10^{-15}$) — the zero-pattern candidates are *block-diagonal* covariance models, and
at a block-diagonal evaluation point both $I_{\text{com}}$ and (expected) $I_{\text{obs}}$
decompose over {within-block, cross-block} vech coordinates, which is exactly the invariance /
equality condition of Proposition L2. The naive-vs-exact distinction is therefore invisible in
the W3 family by structure (not by luck), and bites for constraints that do not
block-decompose (the $\mu_1$ cell of @sec-lrt-bias, factor 3+).

**P8 (report, WEAK indirect pair).** $s^{(3)}_{\text{MB}} - s^{(3)}_{\text{MC}}$: mean $6.10$,
sd $5.99$ vs complete-data $\Delta$AIC(MB, MC) mean $10.00$, sd $7.10$ —
the indirect gap is shrunken (conservative), consistent with per-model marginal equating not
calibrating difference distributions; $\operatorname{corr}(s_{\text{MB}}, s_{\text{MC}})$:
$0.279$ (MI) vs $0.226$ (complete) — MI's shared-imputation noise mildly *increases* the
score correlation (direction that helps difference conditioning).

**Net.** Every preregistered pass criterion held; the null/noncentral achievability split
landed quantitatively where the analytic law put it ($a_k$ and $1/\lambda_{\max}$). The
@sec-ic narrative uses these numbers as graded.

*Preregistered 2026-06-04 before `verification/ic-ladder.R` existed. Author of record:
marcus.waldman (ORCID-verified human prompter); AI-assisted per JAIGP norms.*
