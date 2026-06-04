# Todo 024 — W2 LRT differential: analytic derivation FIRST, then audit, then simulation

**Status:** OPEN (2026-06-03). Supersedes the "just build the paired estimator" reading of
todo/022 item C. User directive: multimodal evidence — analytic derivation + blind GPT-5.5
adversarial audit BEFORE any full-scale simulation. The simulation confirms a pre-stated analytic
claim; it does not explore.

**Scope decision context:** the paper is now bias correction + LRT (W1/W2); the W3
distributional-calibration ladder is the sequel (`todo/023`). W2 is therefore the application
centerpiece and its differential claim must be derived, not just measured.

## The claims to derive (in-house first, Claude lineage)

Setting: nested models `ψ0 ⊂ ψ` (df difference `q_d`), both fit to the SAME congenially imputed
MVN data under ignorable MAR; `d̂_L = 2[Q̄_∞(ψ̂*) − Q̄_∞(ψ̂0*)]`. From the locked theory, each
model's deviance carries `+tr(RIV_model) + 2(A+C)_model + O(1/n)`.

- **D1 (differential structure — mostly assembled, make rigorous).**
  `Bias[d̂_L] = [tr RIV_ψ − tr RIV_ψ0] + 2[(A+C)_ψ − (A+C)_ψ0] + O(1/n)`, with both differentials
  `O(1)`. Establish precisely what "the same imputed data" buys: which realized quantities are
  common to the two fits.

- **D2 (conditioning — the load-bearing NEW claim).** The per-dataset statistic for the LEVEL,
  `ac_i = A_rb,i − tr_obs,i`, has sd `≍ c√n` (heavy right tail) — established in todo/020/021. The
  per-dataset PAIRED DIFFERENTIAL `ac_i(ψ) − ac_i(ψ0)` (same dataset, same imputations, nested
  fits) has sd of strictly lower order. Derive the order. Mechanism to formalize: the `O(√n)`
  linear noise term `α^⊤δ` is driven by the common realized data through the shared sufficient
  statistics; for nested fits the two linear terms agree on the shared parameter subspace, so the
  difference retains only the `q_d`-dimensional complement — kill the `O(√n)` component, leaving
  `O(1)` sd (conjectured; DERIVE, do not assume). This is the analytic content behind the
  manuscript's "structurally better-conditioned" clause and the design basis for the paired
  estimator (mirror of `term-ac-controlvariate-pin.R` / `term-ac-higherorder-paired.R`).

- **D3 (value at H0 and under local alternatives).** Show the `(A)+(C)` differential is 0 at H0 to
  leading order (both differentials vanish when the extra parameters are null and carry no
  missing-information differential), and derive its leading-order magnitude under local
  alternatives `ψ = ψ0 + n^{-1/2}·h` — in particular whether it is `O(1)` (matters for power) or
  `o(1)` (the tr(RIV) differential dominates). This determines what §4 may claim about WHERE the
  differential bias bites.

**Verification per claim (multimodal):** (i) derivation written two independent ways where
feasible (the WAY-1/WAY-2 discipline of todo/020); (ii) CAS check of the expansion coefficients
(sympy, mirroring the bivariate/4-variate machinery); (iii) SMALL-scale paired MC spot check
(few cores, R ≤ 2000, the existing 4-variate non-monotone MAR design) — NOT the full sweep.

## Stage 2 — blind GPT-5.5 adversarial audit (the gate)

After the in-house derivation is written and CAS-checked, author the layer-3 packet in this file
(below the Mode-A section header, exactly the todo/019/021 template):

- **Mode A (blind):** self-contained problem — derive the order of the per-dataset paired
  differential's sd and the H0/local-alternative behavior of the differential, from scratch. No
  hint of our answer.
- **Mode B (red-team):** our claim + lemma sheet + the heavy-tail empirical facts; attack the
  cancellation argument (e.g. "the linear terms do NOT agree on the shared subspace because the
  two MLEs differ at O(n^{-1/2})").
- **grading key at bottom** — hard-strip before sending; runner truncates at the `##` header.
- Pre-send: dry-run `extract_modes` + token-scan for leakage (no `-0.22`, no verdict words, no
  order answers in the modes).
- Launch BACKGROUNDED:
  `py verification/run_layer3_openai.py gpt-5.5 --effort xhigh --timeout 86400 --package todo/024-w2-differential-analytic-first.md --tag -w2diff`

**While the audit runs (~hours, 24h timeout):** proceed with todo/022 item A (W1/H1
reconciliation — empirical, governed by the LOCKED theory, no new analytic claim, no gate).

## Stage 3 — paired simulation (only after the audit returns)

- Escalation NOT hit ⇒ build the paired between-model estimator (template:
  `term-ac-controlvariate-pin.R` pairing logic, across nested models on shared imputations),
  prereg the predicted orders from D2/D3, run at moderate scale, then upgrade §4's
  "structurally better-conditioned" to a derived + audited + measured claim.
- Escalation HIT ⇒ stop, reconcile, re-derive; do NOT run the sweep against a disputed claim.

## Guardrails (carried)

- Few-core targeted runs; heavy-tailed statistics ⇒ paired/control-variate only.
- Do NOT re-open the locked level results (headline, (A)+(C) value not-pinned, −0.22 anchor).
- Touch manuscript ⇒ render exit-0 + /derivation-audit 0 BLOCKER.

*Opened 2026-06-03; the analytic-first sequencing is a user directive for this session.*

---

## Stage-1 status (2026-06-04 — derivation DONE, CAS-checked; packet below)

In-house derivation complete via three independent routes (difference-of-levels, direct
quadratic expansion, realized pairing), each independently refereed
(`verification/cache/w2diff-stage1-routes.json`). Consensus (2 routes + 2 referees + the
session's own derivation agree; the third route made the I_obs-metric error its referee caught
and corrected to the consensus formula — instructively, the wrong formula IS the naive one):

- **D1.** `E[d_L − d_com] = tr(RIV_f) − tr((G'I_com G)^{-1} G'I_com I_obs^{-1} I_mis G) + O(n^{-1})`
  at H0. The curvature of Qbar is `I_com` (EM identity; forced by the FIML self-consistency
  `psi-hat = theta-hat_obs`), so the constrained MI maximizer projects in the **I_com metric** —
  NOT I_obs. Equivalently `B_direct = tr(M_com I_com I_obs^{-1} I_com) − q_d`,
  `M_com = I_com^{-1} − G(G'I_com G)^{-1}G'`.
- **D1 vs naive.** `B_direct ≤ tr(RIV_f) − tr(RIV_0)` ALWAYS (two independent PSD proofs:
  Gram/Schur and operator-variance), equality iff `col(I_obs^{1/2}G)` is invariant under
  `I_obs^{-1/2} I_mis I_obs^{-1/2}` (includes EFMI, where both = c·q_d). The committed W2
  `bias_correction = trRIV_un − trRIV_cn` (naive) therefore OVERSTATES the H0 differential
  bias off the invariant case. CAS: `verification/cas-wolfram/verify_w2_differential.py`
  (route-form equivalences exact; inequality strict generically, median gap 0.07).
- **D2.** `sd(D) = O(1)` at H0 and under `h/√n` local alternatives; reverts to `O(√n)` at fixed
  alternatives / non-nested. Mechanism: the heavy `O_p(√n)` level noise lives in a
  fit-independent realized constant (the shared-imputation `F(θ0, θ̂_imp)` pieces + realized
  `ℓ_com − ℓ_obs` at θ0) that cancels EXACTLY, realization by realization; the survivors are
  `O_p(1)` quadratic forms. This REFINES the todo/024 conjectured mechanism: the cancellation is
  the shared-imputation common constant (φ-slot commonality), not a subspace projection of the
  linear noise.
- **D3.** The `(A)+(C)` differential is exactly 0 at H0 at leading order (it sits in the
  fit-independent common constant; first nonvanishing contribution `O(n^{-1})`); `O(n^{-1/2}) = o(1)`
  under local alternatives (the trace differential dominates local power distortion); genuine
  `O(1)` at fixed alternatives / non-nested, where the heavy tail also returns.

**MC spot check COMPLETE (2026-06-04), P1–P5 all confirmed**
(`verification/w2-paired-differential-spotcheck.R`, R=2000/cell):
sd(T_f) = 18.4/26.6/36.5 (~√n) vs sd(D) = 1.58/1.47/1.57 (flat) at H0; local arm flat at ~2.8;
fixed arm reverts 12.4/16.8/24.9 (~√n); mean(D) consistent with B_direct/2 with no O(1) offset;
EM fixed point to 4e-6. The σ12 design cannot separate B_direct from D_naive (gap 5%), so a
DISCRIMINATING cell was added (`w2-paired-differential-mu1-cell.R`: H0 μ₁=0, X1 ~75% missing MAR
on X3 — exercises the MAR μ×Σ cross term): targets D_naive = 8.47 vs B_direct = 2.64;
**mean(dL−dcom) = 2.639 ± 0.113 (N=500) and 2.701 ± 0.112 (N=1000) — ON B_direct (0.0/0.5 se),
52 se from the naive value.** Caches: `cache/w2-paired-differential-{spotcheck,mu1-cell}.rds`.

**Stage 2 LAUNCHED 2026-06-04:** packet below authored, `extract_modes` dry-run clean (ModeA 5543 /
ModeB 5819 chars), token-scan CLEAN (`cache/_dryrun_scan_w2diff.py`; one F1-given-fact exemption
asserted), runner launched backgrounded
(`py verification/run_layer3_openai.py gpt-5.5 --effort xhigh --timeout 86400 --package
todo/024-w2-differential-analytic-first.md --tag -w2diff`).

**GRADING OUTCOME — MODE A (returned + graded 2026-06-04, same session): FULL AGREEMENT on every
load-bearing point; no escalation trigger hit.** `cache/layer3-gpt-5.5-w2diff-modeA.md`, blind,
off-lineage:
- `J = −∇²Qbar(θ0) = I_com` (boxed), derived via the differentiated conditional-score identity
  `∇²_ψψF(θ0,θ0) = −M_R` — a cleaner route than ours; `Z = I_com I_obs^{-1} S + O_p(1)`.
- `ψ̂ = θ̂_obs` EXACTLY (global argument: conditional-KL + ℓ_obs maximality, not merely local).
- Constrained maximizer = **I_com-metric projection, "not the I_obs metric"** (boxed verbatim).
- The H0 formula boxed term-for-term `= tr(I_obs^{-1}I_mis) − tr[(G'I_com G)^{-1}G'I_com I_obs^{-1}I_mis G] + O(n^{-1})`.
- **Definite-sign comparison** (the strong-signal item): `E[d_L−d_com] ≤ tr(RIV_f) − tr(RIV_0)`
  ALWAYS, via a THIRD independent proof (`W'C^{-1}W ⪰ (W'CW)^{-1}` Schur, C = whitened I_obs);
  "the self-contained RIV-trace difference generally overstates the actual MI deviance differential
  bias"; equality iff `I_com^{-1}I_obs col(G) ⊆ col(G)` — equivalent to our invariance condition
  (both inclusions are equalities of k0-dim subspaces).
- `sd(D) = O(1)` at H0 and local (same mechanism: the common base `B_R(θ0)` carries BOTH
  `O_p(√n)` pieces — the conditional log-lik residual and `α_R'δ` — and cancels exactly);
  `O(√n)` at fixed alternatives.
- `(A)+(C)` differential "zero through O(1)" at H0 (residual `O(n^{-1})`), `O(n^{-1/2})` local,
  `O(1)`-in-expectation at fixed alternatives with `O_p(√n)` realized noise. Bonus: cleanly
  separates the `t'M_Rδ` cross term (the RIV channel) from the pure `(A)+(C)` pieces — matching
  our quadratic-route referee's distinction.

**MODE B: pending** (runner still in flight; grade on return against the key below — its planted
objection is already answered by Mode A's §4.2, but grade it independently).

**Manuscript LANDED 2026-06-04:** `derivation.qmd @sec-lrt` (Propositions L1–L4, sources, Appendix-A
entries for Wilks / Chan–Meng / Chan-AoS / Meng–Rubin-92 / Vuong, vdV §16.4 passage); intro LRT
bullet + @sec-thm better-conditioned clause updated; render exit-0; /derivation-audit 0 BLOCKER
(3 cas-wolfram WARN = known brace-glob false positives).

---

## MODE A — blind re-derivation (paste from here to the Mode-A end marker)

> You are a mathematical statistician. Solve the following self-contained problem from scratch,
> using only your own knowledge of likelihood theory, M-estimation/MLE asymptotics, EM/multiple
> imputation, and matrix algebra. Show every step, name the standard results you use, and DERIVE
> every order and every formula — do not assume them.
>
> **Setup.** `X ~ N_p(mu, Sigma)`, `theta = (mu, vech Sigma)` in `R^k`; `n` i.i.d. units; some
> coordinates of each unit are missing under an ignorable MAR mechanism (propensity depends only
> on always-observed coordinates; mechanism parameter distinct from `theta`; patterns may be
> non-monotone). `theta_0` = truth. Objects (all `O(n)` unless noted):
>
> - `l_obs(theta)`: observed-data (FIML) log-likelihood; `theta-hat_obs` its maximizer;
>   `S = grad l_obs(theta_0)`; `delta_obs = theta-hat_obs − theta_0`. Standard MLE asymptotics:
>   `E[delta_obs] = O(n^-1)`, `Var(delta_obs) = I_obs^-1 = O(n^-1)`, signed third/fourth central
>   moments `O(n^-2)`; `I_obs = Var(S)`; `I_com` = expected complete-data information;
>   `I_mis = I_com − I_obs` (Orchard–Woodbury); `RIV = I_obs^-1 I_mis`, `tr(RIV) = O(1)`.
> - `F(psi, phi) := sum_i E_{Y_mis,i ~ p_phi(.|Y_obs,i)}[ log p_psi(Y_mis,i | Y_obs,i) ]` — a
>   realized function of `Y_obs` and the realized patterns. Facts you may take as given
>   (previously derived and audited): **(F1)** `grad_psi F(psi,phi)` at `psi = phi = theta_0` is
>   EXACTLY zero for every realization (conditional-score identity, unit by unit). **(F2)**
>   `grad_psi grad_phi F(theta_0,theta_0)` = realized missing information, expectation `I_mis`
>   (Bartlett-type identity). **(F3)** `grad_phi F(theta_0,theta_0) =: alpha_R` (realized,
>   `E[alpha_R] =: alpha = O(n)`, supported on covariance coordinates for the Gaussian);
>   `grad_phi grad_phi F(theta_0,theta_0) =: H_R`, `E[H_R] =: H_phi = O(n)`. Realized-minus-
>   expected versions of `alpha_R`, `H_R`, and the information matrices fluctuate at `O_p(n^{1/2})`.
> - MI Q-function with deterministic (FIML, `M = infinity`) imputation at a fitted imputation
>   parameter: `Qbar(theta) := l_obs(theta) + F(theta, theta-hat_imp)`, with
>   `theta-hat_imp = theta-hat_obs` (the FULL model's observed-data MLE). THE SAME imputations
>   (same `theta-hat_imp`, same realized `F`) serve both model fits below.
> - **Level theorem (take as given; previously derived and audited).** For the full model,
>   `E[Qbar(theta-hat_obs) − l_com(theta-hat_com)] = +(1/2) tr(RIV) + [(A)+(C)] + O(n^-1)`, where
>   `l_com` is the complete-data log-likelihood, `theta-hat_com` its maximizer, and
>   `(A)+(C) = alpha' E[delta_obs] + (1/2) tr(H_phi I_obs^-1) + O(n^-1)` is `O(1)` under MAR, `0`
>   under MCAR. The per-dataset statistic `T := Qbar(theta-hat_obs) − l_com(theta-hat_com)` is
>   heavy-tailed with sd `~ c sqrt(n)`.
>
> **Nested pair and the MI likelihood-ratio construction.** Null submodel `theta = g(gamma)`,
> `gamma in R^{k0}`, `k0 = k − q_d`, `g` smooth, `G := dg/dgamma'` (k × k0, full column rank, at
> `gamma_0`); H0: `theta_0 = g(gamma_0)`. Both models are fit to the SAME imputed data:
> `psi-hat := argmax_theta Qbar(theta)`; `gamma-hat* := argmax_gamma Qbar(g(gamma))` — note this
> is the constrained maximizer of the SAME `Qbar`, NOT the null model's own observed-data MLE.
> `d_L := 2[Qbar(psi-hat) − Qbar(g(gamma-hat*))]` (the MI deviance numerator);
> `d_com := 2[l_com(theta-hat_com) − l_com(g(gamma-hat_com))]` (complete-data counterpart;
> `E[d_com] = q_d + O(n^-1)` at H0 by Wilks). Define the levels
> `T_f := Qbar(psi-hat) − l_com(theta-hat_com)`, `T_0 := Qbar(g(gamma-hat*)) − l_com(g(gamma-hat_com))`,
> and the per-dataset paired differential `D := T_f − T_0 = (d_L − d_com)/2`.
>
> Also define, for reference, each model's "self-contained" RIV trace:
> `tr(RIV_f) := tr(I_obs^-1 I_mis)` and `tr(RIV_0) := tr((G'I_obs G)^{-1} (G'I_mis G))`.
>
> **Tasks. Work at H0 first; complete order bookkeeping throughout.**
>
> 1. **The MI objective's local geometry.** Derive `Z := grad Qbar(theta_0)` and
>    `J := −grad^2 Qbar(theta_0)` in terms of `S`, `delta_obs`, and the realized F-derivatives
>    (use (F1)–(F3)). Derive where `psi-hat` and `g(gamma-hat*)` sit to `O_p(n^-1)`: in
>    particular, determine in WHICH metric the constrained maximizer projects the score, and
>    verify whether `psi-hat` coincides with `theta-hat_obs`. Do not assume the answers.
> 2. **Differential bias.** Derive `E[d_L − d_com]` at H0 to `O(1)`, with the order of the
>    remainder, as an explicit matrix formula in `I_com`, `I_obs`, `G`, `q_d`.
> 3. **Comparison.** Does your formula equal `tr(RIV_f) − tr(RIV_0)` in general? If not: give the
>    exact condition for equality, and determine whether the discrepancy has a definite sign
>    (prove it, or give a counterexample).
> 4. **The paired differential's noise.** The level `T_f` has sd `~ c sqrt(n)` (given). Derive
>    the ORDER in `n` of `sd(D)` at H0. Identify exactly which `O_p(sqrt n)` realized pieces of
>    `T_f` and `T_0` cancel, and why. Then derive `sd(D)` under (i) local alternatives
>    `theta_n = g(gamma_0) + h/sqrt(n)` with `h` outside `col(G)`, and (ii) a fixed alternative
>    (both models' pseudo-truths `O(1)` apart, as in non-nested comparison).
> 5. **The `(A)+(C)` differential.** Isolate the `(A)+(C)`-type contributions of each model's
>    level within your expansion and derive their difference: at H0 (derive its order in `n`,
>    and state which parts, if any, cancel and at what order), under the local alternatives of
>    Task 4(i), and at a fixed alternative.

<!-- MODE-A END -->

---

## MODE B — adversarial red-team (paste the brief + the lemma sheet + this prompt)

> You are an adversarial referee. Below are four claims about the multiple-imputation
> likelihood-ratio statistic, with a lemma sheet. Your job is to BREAK them: construct the
> strongest technical attack on each, then adjudicate whether the attack succeeds. Do not skip
> any task; show explicit computations.
>
> **The setting** (lemma sheet below): nested Gaussian models under ignorable MAR, both fit to
> the SAME deterministically imputed data (imputation parameter = the full model's FIML MLE
> `theta-hat_obs`); `d_L` = MI deviance numerator, `d_com` = complete-data deviance,
> `D = (d_L − d_com)/2` the per-dataset paired differential; each model's LEVEL statistic is
> heavy-tailed with sd `~ c sqrt(n)`.
>
> **The claims.**
> - **C1 (metric).** `−grad^2 Qbar(theta_0) → I_com`, so the constrained MI maximizer
>   `gamma-hat*` projects the MI score in the `I_com` metric, and at H0
>   `E[d_L − d_com] = tr(RIV_f) − tr((G'I_com G)^{-1} G'I_com I_obs^{-1} I_mis G) + O(n^{-1})`.
> - **C2 (naive overstatement).** The self-contained difference `tr(RIV_f) − tr(RIV_0)`, with
>   `tr(RIV_0) = tr((G'I_obs G)^{-1} G'I_mis G)`, is ALWAYS `>=` the C1 formula, with equality
>   iff `col(I_obs^{1/2} G)` is an invariant subspace of `I_obs^{-1/2} I_mis I_obs^{-1/2}`
>   (e.g. equal-fraction-of-missing-information, where both equal `(missing fraction)·q_d`).
> - **C3 (paired-noise collapse).** `sd(D) = O(1)` at H0 and under `h/sqrt(n)` local
>   alternatives — strictly lower order than the level's `O(sqrt n)` — because the heavy
>   `O_p(sqrt n)` noise lives in a fit-independent realized constant (the shared-imputation
>   `F(theta_0, theta-hat_imp)` pieces plus the realized `l_com − l_obs` at `theta_0`) that is
>   IDENTICAL in `T_f` and `T_0` and cancels realization-by-realization. `sd(D)` reverts to
>   `O(sqrt n)` at a fixed alternative.
> - **C4 ((A)+(C) differential).** The `(A)+(C)` design-imbalance term cancels EXACTLY (to
>   leading order; residual `O(n^{-1})`) in the differential at H0, is `O(n^{-1/2}) = o(1)` under
>   local alternatives, and is a genuine `O(1)` only at fixed alternatives / non-nested
>   comparison.
>
> **Attacks to mount (then adjudicate each).**
> 1. **Against C3 (the planted objection).** Argue: "the linear terms do NOT cancel, because the
>    two MLEs differ at `O(n^{-1/2})`: the gradient of the level statistic at `theta_0` is
>    `O_p(sqrt n)` (it contains `alpha_R`-type terms of size `O(n)` times nothing — i.e. a raw
>    `O_p(sqrt n)` realized fluctuation), and contracting an `O_p(sqrt n)` gradient against the
>    `O_p(n^{-1/2})` between-fit displacement gives `O_p(1)` only if the gradient is the SAME
>    realization for both fits — but each fit has its own evaluation point, so the
>    `alpha_R' (fit displacement)` pieces differ by `O(n) × O(n^{-1/2}) = O(sqrt n)`." Make this
>    case as strongly as possible, with explicit decompositions; then determine rigorously
>    whether `sd(D)` at H0 is `O(sqrt n)` or `O(1)`.
> 2. **Against C1.** Argue: "all estimation noise is observed-data noise, `Var(Z)` is built from
>    `I_obs`, and the null fit is consistent for the same `theta_0` — so the constrained fit
>    projects in the `I_obs` metric and the H0 differential bias is exactly
>    `tr(RIV_f) − tr(RIV_0)`." Compute `−grad^2 Qbar(theta_0)` from the lemma sheet identities
>    and settle the metric. Check your answer against the requirement that the UNCONSTRAINED
>    maximizer of `Qbar` must reproduce `theta-hat_obs` (why must it?).
> 3. **Against C2.** Try to construct a counterexample where the self-contained difference
>    UNDERSTATES the C1 formula (PD `I_obs`, PSD `I_mis`, any full-rank `G`). If you cannot,
>    prove the inequality and its equality condition.
> 4. **Against C4.** Argue: "the two models' conditional-entropy gradients are evaluated at
>    different fitted points, so the `alpha`-pieces differ at `O(n) × O(n^{-1/2})` and the
>    `(A)+(C)` differential is `O(n^{1/2})`, or at least `O(1)`, even at H0." Adjudicate, paying
>    attention to which pieces are evaluated at `theta_0` versus at the fitted points, and to
>    what is common between the two fits.
> 5. **Verdict.** For each of C1–C4: SUSTAINED (claim survives) or REFUTED (give the corrected
>    statement). If your Task-2 conclusion contradicts C1, state which formula is correct and
>    why.
>
> ### Lemma sheet
>
> - Model/missingness: `X ~ N_p(mu, Sigma)`, `theta = (mu, vech Sigma) in R^k`, `n` i.i.d. units,
>   ignorable MAR (propensity on always-observed coordinates), patterns possibly non-monotone;
>   truth `theta_0 = g(gamma_0)` (H0). Null submodel `theta = g(gamma)`, `G = dg/dgamma'`
>   (k × k0, full rank), `q_d = k − k0`.
> - `F(psi, phi) = sum_i E_{Y_mis,i ~ p_phi(.|Y_obs,i)}[log p_psi(Y_mis,i|Y_obs,i)]` (realized,
>   `O(n)`). **(F1)** `grad_psi F(theta_0, theta_0) = 0` exactly, every realization.
>   **(F2)** `grad_psi grad_phi F(theta_0,theta_0)` = realized missing information, mean `I_mis`.
>   **(F3)** `grad_phi F(theta_0,theta_0) = alpha_R` (mean `alpha = O(n)`, covariance-supported);
>   `grad_phi grad_phi F(theta_0,theta_0) = H_R` (mean `H_phi = O(n)`). Realized-minus-expected
>   fluctuations of all these are `O_p(n^{1/2})`.
> - `Qbar(theta) = l_obs(theta) + F(theta, theta-hat_obs)`; both fits maximize this one realized
>   function (full: over `theta`; null: over `g(gamma)`).
> - MLE asymptotics: `S = grad l_obs(theta_0)`, `Var(S) = I_obs`; `delta_obs = I_obs^{-1} S + O_p(n^{-1})`;
>   `E[delta_obs] = O(n^{-1})`; central moments of `delta_obs` of order 3/4 are `O(n^{-2})`.
> - Level theorem (audited, take as given): `E[T] = (1/2)tr(RIV) + (A)+(C) + O(n^{-1})` per model,
>   `(A)+(C) = alpha' E[delta_obs] + (1/2) tr(H_phi I_obs^{-1}) + O(n^{-1})`; per-dataset level sd
>   `~ c sqrt(n)`, heavy right tail.
> - Wilks: `E[d_com] = q_d + O(n^{-1})` at H0.

---

## ★ GRADING KEY — REMOVE BEFORE SENDING TO ANY MODEL ★

*(Never paste below this line into the API call. The runner `verification/run_layer3_openai.py`
hard-truncates at this `##` header.)*

**Our position (Stage 1, 2026-06-04; 3 in-house routes + referees + CAS).**

- **Metric/D1.** `J = −grad^2 Qbar(theta_0) = I_obs + I_mis = I_com` (Fisher's EM identity via
  (F2); independently forced by FIML self-consistency: the unconstrained `Qbar`-maximizer must
  equal `theta-hat_obs`, and `Z = I_com I_obs^{-1} S + O_p(1)`, so only `J = I_com` gives
  `J^{-1}Z = delta_obs`). Constrained maximizer: `g(gamma-hat*) − theta_0 = G(G'I_com G)^{-1}G'Z`
  — the I_com-metric projection. `E[d_L] = tr(M_com Var(Z)) + o(1)`, `Var(Z) = I_com I_obs^{-1} I_com`,
  giving `E[d_L − d_com] = tr(RIV_f) − tr((G'I_com G)^{-1}G'I_com I_obs^{-1}I_mis G) + O(n^{-1})`
  (= `B_direct = tr(M_com I_com I_obs^{-1} I_com) − q_d`). An I_obs-metric answer
  (`= tr(RIV_f) − tr(RIV_0)`) is the EXACT trap one in-house route fell into (its referee caught
  it; numerically a fixed-sign O(1) overstatement). Remainder `O(n^{-1})`.
- **Naive comparison/C2.** `B_direct <= tr(RIV_f) − tr(RIV_0)` ALWAYS; two PSD proofs
  (Gram/Schur: `G'B A^{-1}B G >= (G'BG)(G'AG)^{-1}(G'BG)`; operator-variance form
  `tr(A^{-1} Q'N(I−QQ')NQ) >= 0`); equality iff `col(I_obs^{1/2}G)` invariant under
  `I_obs^{-1/2}I_mis I_obs^{-1/2}` (includes EFMI/proportional, both `= c q_d`). CAS-verified
  symbolically + 400 random instances (strict generically, median gap 0.07); a sign-indefinite
  claim is WRONG (one in-house referee's "−0.39" seed traced to an alt-rep arithmetic slip of
  exactly `q_d`).
- **D2/C3.** `sd(D) = O(1)` at H0 and local; `O(sqrt n)` at fixed alternatives. The planted
  objection fails because the heavy noise is NOT a model-specific gradient contraction: by (F1)
  the `psi`-gradient of `F` at `(theta_0, theta_0)` vanishes exactly, so the `alpha_R`-type
  `O_p(sqrt n)` noise sits in the fit-INDEPENDENT additive constant
  `F(theta_0, theta-hat_imp) ≈ alpha_R' delta_obs + ...` (same realization in both levels) plus
  the common realized `l_com − l_obs` at `theta_0`; it cancels exactly in `D`. What survives:
  differences of `O_p(1)` quadratic forms. MC spot check (running): sd(T_f) ≈ 21 vs sd(D) ≈ 0.9
  at H0 (N=1000), fixed-arm sd(D) ≈ 15.
- **D3/C4.** `(A)+(C)` differential: exactly 0 at H0 at leading order (it sits in the common
  fit-independent constant; first nonvanishing `O(n^{-1})`); `O(n^{-1/2}) = o(1)` under local
  alternatives (the trace differential dominates local power); genuine `O(1)` at fixed/non-nested.

**Agreement bar.**
- (Agreement.) Mode A derives `J → I_com`, the I_com-metric projection, the `B_direct` formula
  (any algebraically equivalent form), `sd(D)` orders O(1)/O(1)/O(sqrt n), and the
  exactly-zero-at-H0 `(A)+(C)` differential. Mode B SUSTAINS C1–C4 (Task-3 ideally reproducing
  the PSD proof).
- (Strong independent signal.) Mode A spontaneously notes the naive difference overstates with
  fixed sign, or that the wrong metric reproduces the naive formula; or connects `E[d_L]` at H0
  to the mean of the weighted-chi-square reference (sum of complement eigenvalues of
  `I_com I_obs^{-1}` in the I_com metric — the quantity reference-distribution calibration
  absorbs).
- **(ESCALATE / divergence.)** (i) A DEFENDED I_obs-metric projection (i.e. the claim
  `E[d_L − d_com] = tr(RIV_f) − tr(RIV_0)` exactly, generally); (ii) a derived
  `sd(D) = O(sqrt n)` at H0 under shared imputations; (iii) a genuine `O(1)` `(A)+(C)`
  differential at H0 or under local alternatives; (iv) a verified counterexample where the naive
  difference UNDERSTATES `B_direct` (PD `I_obs`, PSD `I_mis`). Any of these contradicts the
  Stage-1 consensus — STOP, reconcile, do not simulate against a disputed claim.
