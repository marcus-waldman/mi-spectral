# Todo 017 — Imputation-engine sensitivity screener: Bayes-proper DA vs EMB (Amelia)

**Status:** Plan (2026-06-02). Execute in a **fresh session**. Sibling of todo/015, todo/016.

**One-line goal.** Decide — as cheaply as possible — whether the paper's proper-MI conclusions are
**sensitive** to the imputation engine: **EMB / Amelia** (bootstrap; fast; independent draws; only an
*approximate* posterior) vs **Bayesianly-proper data augmentation** (`norm::da.norm`; conjugate
Normal-Inverse-Wishart posterior; *exact* stationary law but **MCMC / slow**). Run DA **only if the
cheap screener says it's necessary.** If sensitive → update `manuscript/derivation.qmd` with the
limitation.

---

## 0. Why this came up (context for a cold session)

This is fallout from the todo/015–016 thread on the non-monotone `(A)+(C)` design-imbalance term:
- The leading-order analytic `(A)+(C)_∞ ≈ −0.22`; the committed empirical phase-8 remainder is
  `−0.34 (n=800) → −0.46 (n=1500)`, still increasing. A GPT-5.5 Layer-3 adversarial check (todo/016,
  commit `ffff008`) found the named candidate terms are tiny (`B_cov=−0.02`) or cancel (Δ by Louis);
  the live lead is a **realized-vs-expected observed-information** effect under MAR.
- Chasing that surfaced a separate, broader worry: **the proper-MI evidence in the paper rests almost
  entirely on Amelia (EMB)**, and Amelia's bootstrap is only an *asymptotic* approximation to the
  posterior — shakiest exactly on this **non-monotone** design with few complete cases, and it
  re-uses the realized sample (so it couples to the realized-information fluctuations). `da.norm`
  (the conjugate-posterior alternative) is implemented but **barely used** in the actual results.

So before trusting (or amending) anything, we want to know: **does Bayes-proper imputation change the
conclusions vs EMB?** If not, document that Amelia is adequate and move on. If yes, the derivation
guide needs a limitations section and the key witnesses need a DA re-run.

## 1. What is and isn't at risk

**AT RISK (uses Amelia draws):** W1 headline (`E[A]=+tr(RIV)`, `E[T]=+½tr(RIV)`), the proper-MI
`(A)+(C)` value, W3 MI-AIC model selection, the proper-MI extension claims (R4–R7), W2 power.

**NOT at risk (no draws — analytic / FIML):** the Cox–Snell `b_Σ` (todo/015), the FIML `(A)+(C)`
(`barQ_fiml_analytic`; W1 "fiml" engine, phase-8 `_modules/term-a-mar-correction.R`), `tr_riv_analytic`.
These are engine-free and stay valid regardless of this investigation's outcome.

## 2. Engine facts (so the comparison is fair) — established this session

| | distribution | draws | speed |
|---|---|---|---|
| **`da.norm`** (Schafer DA) | **exact** observed-data posterior (stationary) | **autocorrelated** MCMC (must thin) | **slow** |
| **Amelia** (EMB) | **approximate** (bootstrap proxy) | **independent** (fresh bootstrap+EM each m) | fast |

- The observed-data posterior is closed-form **only for monotone** patterns; non-monotone breaks
  observed-level conjugacy (same reason the observed *likelihood* doesn't factor → why `b_Σ` needed
  Cox–Snell). So there is **no exact-and-independent** option for the phase-8 non-monotone design.
- `da.norm` current settings (`impute_mvn`, `00-setup.R`): init at the **EM/MLE** (`em_mvn`),
  `burnin=200`, `thin=100`, `M=200` — but these are **UNVALIDATED heuristics** (no ESS/autocorr check
  anywhere) and `da.norm` is in fact only exercised by the **primitive smoke test** (`burnin=50,
  thin=20, M=5`). `norm::rngseed` is set **only** in the smoke test.
- Starting values: you set the starting **θ** (via `norm::makeparam.norm(s, list(mu,sigma))`), not the
  missing cells directly; the first I-step regenerates `Y_mis` from θ. The MLE-start is
  *under-dispersed* (it can **hide** non-convergence) — for diagnostics use **over-dispersed** starts.

## 3. Screener — cheap, decisive, DA-minimizing (DO THIS FIRST)

Strategy: reference everything to the **engine-free analytic** `tr(RIV)` so we can often conclude
**without running DA at all**.

**Step 0 — mine existing evidence (zero new compute).** Two committed diagnostics may already answer
it:
- `_modules/w1-information-diagnostic.R` computes `tr_samp` (Amelia Rubin between/within sample RIV)
  vs `tr_obs` (analytic K&M RIV). **If `tr_samp ≈ tr_obs` across N on the non-monotone cells, Amelia's
  between-imputation variance is already calibrated → likely NOT sensitive.** Read its cache/summary
  (run it if no cache).
- Aggregate verdict **H6** (`_modules/aggregate.R`): "FIML vs Amelia congenial M=200 agree within
  3pp" on the W3-A metric. If H6 passed in `cache/run_all-prod/phase5/`, that's direct evidence the
  W3 conclusion is engine-robust. Read `cache/run_all-*/` summaries.

**Step 1 — Amelia-vs-analytic on the stress cell (no DA).** Pick the most bootstrap-stressed cells:
non-monotone MAR, `default_Sigma`, **N ∈ {200, 500}** (bootstrap miscalibration is worst at small N /
high RIV; p3 observes only X3,X4 → ~N/3 complete-ish cases carrying σ₁₂). Paired seeds, congenial
Amelia (`empri=0`), `M=200`, `R≈1000`. Compute per replicate and average:
- **PRIMARY:** Amelia **sample RIV** (`riv_sample` via `mi_fit_mvn`) vs **`tr_riv_analytic`** — the
  cleanest calibration check (this is where bootstrap-vs-posterior differ).
- **SECONDARY:** W1 `T_hat` vs `½·tr_riv_analytic`, and `E[A]/tr(RIV)` (reuse `W1-bias-decomposition.R`
  amelia branch).
- **Decision A:** if Amelia sample-RIV ≈ analytic (within MCSE) **and** W1 ratios ≈ 1 → **NOT
  sensitive. Amelia adequate. DA unnecessary. STOP** (document in this file + a one-line note in the
  derivation if desired). Do **not** run DA.

**Step 2 — DA confirmation (ONLY if Step 0/1 flags Amelia).** A cheap-DA disagreement could be DA's
*own* poor mixing, so DA is only worth running once Amelia is implicated. Run `da.norm` on the **same
paired cells**, congenial (Jeffreys ≈ congenial), `M=200`, **rngseed per worker**, init EM,
provisional `burnin=100, thin=50`. Compare DA sample-RIV / W1 ratios to analytic and to Amelia.
- **Decision B:** if DA ≈ analytic but Amelia ≠ analytic (materially: >~5% on the RIV ratio, or a
  flipped W3 selection) → **SENSITIVE → escalate (§4).** If DA also ≠ analytic, suspect DA mixing
  first → validate convergence (§4) before concluding.

**Budget:** Step 0 ~ minutes (read caches). Step 1 ~ 1–2 h (Amelia only, 2 cells). Step 2 (if needed)
~ a few hours (DA). Full escalation (§4) is the expensive part we're trying to avoid.

## 4. Escalation — ONLY if the screener says "sensitive"

1. **Validate DA convergence** (don't trust `burnin=200/thin=100` blind): over-dispersed multi-start
   (`makeparam.norm` at θ₀, the MLE, and an inflated-Σ start), **Gelman–Rubin R̂** + **ESS /
   lag-autocorrelation**; set `thin` from the measured ESS; `rngseed` per worker.
2. **Re-run the load-bearing cells** (W1 E[A]/E[T]; one W3 MI-AIC cell; the proper-MI `(A)+(C)`)
   under validated DA; quantify the Amelia-vs-DA gap and its N-trend.
3. **Update `manuscript/derivation.qmd`** with a limitations note: state that the proper-MI evidence
   currently rests on EMB; report the measured DA-vs-EMB discrepancy; recommend DA (or note the regime
   where EMB suffices). Keep `quarto render` exit-0. Honest-reframe discipline (no over-claiming).

## 5. Gotchas (carried from todo/015–016)

- **`em_mvn` is unreliable for this non-monotone design** (its `rem` came out opposite-sign to lavaan
  FIML). For fits use **lavaan FIML** or **`da.norm`**, NOT `em_mvn`. (This broke my last numerical
  check; don't repeat it.)
- **Match the estimand.** FIML `(A)+(C)` and proper-MI `(A)+(C)` differ: proper MI ≈ **doubles (C)**
  via the posterior-draw variance (`Var(φ̃) ≈ 2 I_obs⁻¹` vs `I_obs⁻¹` for FIML). Compare like with
  like; the engine question is about proper-MI draws, so reference the proper-MI quantity (or just use
  the engine-free `tr(RIV)` calibration, which sidesteps this).
- **Congeniality:** keep both engines congenial (Amelia `empri=0`; `da.norm` Jeffreys). The sweep's
  "uncongenial Amelia" (`empri=0.5N`) is a *different* axis — don't conflate.
- **Pairing:** use the **same simulated data** per replicate for both engines (paired) so the
  comparison isn't swamped by between-dataset variance.
- **`rem` MCSE grows with N** (`≈0.65·√(n/R)`); the sample-RIV metric is much lower variance — prefer
  it as the primary screener statistic.

## 6. Files / pointers

- Engines: `impute_mvn` (da.norm), `impute_mvn_amelia` (`verification/00-setup.R`).
- Calibration refs: `tr_riv_analytic`, `riv_sample`, `mi_fit_mvn`, `fisher_info_obs_mvn` vs
  `observed_info_obs_mvn` (`00-setup.R`).
- Witnesses: `W1-bias-decomposition.R` (amelia/fiml branches), `W3-model-selection.R`,
  `_modules/w1-information-diagnostic.R` (tr_samp vs tr_obs), `_modules/w3-sweep.R`,
  `_modules/aggregate.R` (H4/H6).
- Existing caches: `verification/cache/run_all-prod/phase{1,5}/`, `run_all-*/phase8-terma-mar/`.
- This session: commits `446d1a4` (general-p `b_Σ`), `ffff008` (Layer-3 GPT-5.5 check); todo/016
  (engine discussion + GRADING OUTCOME); memory note `[[project-nonmonotone-coxsnell]]`.

## 7. First steps (fresh session)

1. Read this + todo/016 GRADING OUTCOME + the memory note `[[project-nonmonotone-coxsnell]]`.
2. **Step 0**: read `_modules/w1-information-diagnostic.R` outputs and the H6 verdict — they may
   already settle it (cheapest possible answer).
3. If inconclusive, write the **Step 1** screener (paired Amelia vs analytic, sample-RIV primary, 2
   stress cells) and run it; apply Decision A.
4. Escalate to Step 2 / §4 only if flagged.

## Definition of done

A clear **sensitive / not-sensitive** verdict on the stress cells, with the decision and evidence
recorded here. If **not sensitive**: a one-line note that the EMB-based proper-MI evidence is
engine-robust (optionally in the derivation). If **sensitive**: validated-DA re-run of the
load-bearing cells + a limitations section drafted in `manuscript/derivation.qmd`.

*Plan 2026-06-02. Continues the todo/015–016 imputation/(A)+(C) thread.*

---

## VERDICT (2026-06-02) — NOT SENSITIVE. DA not run.

**Step 0 settled it with zero new compute.** The committed `cache/run_all-prod/phase6-info/`
diagnostic (commit `70923a3`, R=2000) **is** the paired Amelia-vs-analytic stress test Step 1
nominated: same non-monotone MAR `default_Sigma` cells, N∈{200,500,1000,2000}, **congenial** Amelia
(`impute_mvn_amelia` default `empri=0`), paired within replicate (one dataset → both the FIML
observed-data RIV and the Amelia sample RIV), at *higher* R than Step 1 proposed. No new run needed;
**Decision A → STOP; DA (Step 2) and the §4 escalation were not triggered.**

**Primary metric — Amelia sample RIV vs the engine-free observed-data RIV** (`phase6-info/summary.csv`,
non-monotone MAR):

| N | `tr_samp` (Amelia) | `tr_obs` (engine-free, correct) | `tr_exp` (naive) | `tr_samp − tr_obs` | rel |
|----|------|------|------|------|------|
| 200 | 8.816 | 8.596 | 7.725 | +0.220 | 2.6% |
| 500 | 8.524 | 8.346 | 7.673 | +0.178 | 2.1% |
| 1000 | 8.431 | 8.265 | 7.652 | +0.166 | 2.0% |
| 2000 | 8.383 | 8.199 | 7.621 | +0.184 | 2.2% |

Amelia's between-imputation variance tracks the correct observed-data RIV within **≤0.22 (≈2–3%),
non-growing in N** (monotone cells similar/smaller; overall `max|tr_samp − tr_obs| = 0.22`). The slight
sign is an *over*-estimate (known small EMB bootstrap over-dispersion) — conservative for the claims.

**Downstream witness — W3 MI-AIC selection** (`phase5/verdicts.md`): **H6 = PASS**,
`max|FIML − Amelia congenial M=200| W3-A = 0.011` (threshold 0.03). The actual headline IC quantity is
engine-robust, bypassing the RIV-reference subtlety entirely.

**⚠ Reference correction to §3 (important — do not re-apply the literal Step-1 metric).** §3 named the
PRIMARY metric "Amelia sample RIV vs `tr_riv_analytic`". But `tr_riv_analytic` (= `tr_exp`) is the
**naive / as-if-MCAR** RIV that drops the MAR mean×covariance cross term; against it Amelia looks off
by ~1.09 at N=200 (~14%), which would **falsely flag** sensitivity. The correct engine-free reference
is the realized **`tr_obs`** (`observed_info_obs_mvn`, the K&M-1998 cross term included) — also what a
congenial proper imputation's posterior variance should reproduce — and Amelia matches it. The
phase-6 "one-RIV" reframe already adopts `tr_obs`; this is the single most load-bearing point.

**Honest caveat — W1 secondary metric.** The proper-MI `A_prop`/`T_prop` (Amelia) residuals vs `tr_obs`
are non-zero and noisy (`A_minus_obs` ≈ −0.48/−0.76/−0.36/−1.33 across N, within ~2 MCSE). These are the
**same finite-n / realized-information `(A)+(C)` offset already documented** (the −0.22→−0.46 thread,
[[project-nonmonotone-coxsnell]]) — present in FIML too (`A_fiml` similarly offset, draw-free) — i.e.
an analytic/FIML phenomenon, **not** an Amelia artifact. Not evidence of engine sensitivity.

**Definition of done: satisfied (not-sensitive branch).** Recorded here; one-line engine-robustness
note added to `manuscript/derivation.qmd` (§sec-combine, "Both terms calibrate to the single
observed-data RIV"); `quarto render` exit-0; no DA re-run, no limitations section needed.
