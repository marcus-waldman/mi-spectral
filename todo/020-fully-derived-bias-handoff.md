# Todo 020 — Handoff: get the bias derivation to "fully derived / fully pinned"

**Status:** ✅ EXECUTED (2026-06-02). Continues todo/018. **W1–W3 applications and the
Satorra–Bentler re-evaluation remained DEFERRED** (see §6).

## ✅ OUTCOME (2026-06-02)

**Decision gate revised mid-session (user correction): the exact `(A)+(C)` value IS load-bearing** —
directly for the LRT bias level/calibration (it is also one of the paper's three named contributions),
so scoping it out was wrong. Pivoted to pinning/deriving it.

**Headline finding — the value is heavy-tailed, not precisely pinnable; the prior "−0.34→−0.46
increasing" was MC noise.** The per-replicate remainder `A_rb − tr(RIV)` is heavy-tailed/right-skewed
with sd ∝ √n (median ≈ −1.2 vs mean ≈ −0.3, range ±90). The realized `(A)+(C)` mean **bounces**
`−0.34, −0.46, −0.29, +0.17` across n=800/1500/3000/6000 (se 0.09–0.35; pooled ≈ −0.35±0.07) — untrended,
**broadly consistent with the 2nd-order analytic −0.22** within ~1–2 se. The 2nd-order −0.22 was
re-derived cleanly (total-derivative `∇²A_RB = 2 I_mis|obs + H_φ`; eval-point accounted; higher orders
O(1/n)). So **route (c) closed-form is moot** — no precise target to derive toward.

**Cross-model check (added on reflection — standing directive).** The "higher orders are O(1/n) ⇒
−0.22 is the asymptote, −0.46 is heavy-tailed noise" conclusion is a *fresh, load-bearing analytic
claim* (it contradicts the prior "open higher-order theory" stance), so per the cross-model protocol it
needs an off-lineage check — which I initially skipped (wrongly). Blind packet built (`todo/021`,
distinct from todo/019's convention-gap check): Mode A derives the order of the second-order Taylor
remainder `R_n` of the imputation-bias functional; Mode B red-teams "R_n=O(n⁻¹), so the empirical
departure is finite-sample noise" against the sign-bouncing MC mean. Blind-check PASS (key hard-stripped,
no leak terms). Launched gpt-5.5 `--effort xhigh --timeout 86400` backgrounded.

**Cross-model RESULT (todo/021 GRADING OUTCOME): full agreement — `R_n=O(n⁻¹)`, second-order `−0.22`
is the asymptote, empirical departure is heavy-tailed MC noise; escalation NOT hit (Mode A explicitly
rejected the `O(n⁻¹/²)` off-ramp; Mode B independently proposed the paired Taylor-control estimator).**

**EMPIRICAL CAPSTONE — control-variate pin (`term-ac-controlvariate-pin.R`, the decisive test):**
pairing each replicate's `A_rb` against its decoupled 2nd-order Taylor (population coeffs) cancels the
`√n` noise; decoupled sanity ✓ (−0.222/−0.220/−0.220); the residual coupling = `+0.157/+0.074/+0.045`
at n=800/1500/3000 (`n·coupling ≈ 125/111/135` ⇒ **O(1/n), POSITIVE**), so `(A)+(C) = −0.22 + 124/n →
−0.22`. An **O(1)** coupling (which would make the value `−0.46`) is **RULED OUT**. ⇒ **asymptote is
−0.22**; the empirical `−0.34→−0.46` is a finite-n + right-tail-skew artifact (direct mean sits below
the true value, per Mode B). The paired diagnostic (`term-ac-higherorder-paired.R`) independently
gives 3rd-order remainder `O(1/n)` (n·rbar ≈ 75). **Net: −0.22 confirmed three ways (CV + cross-check +
paired-sim); my mid-session "reversal" toward −0.46 was an over-reaction to a noisy `mean(taylor2)` and
was never committed.** The committed manuscript (−0.22-leaning, heavy-tailed-empirical) is correct.

**What stays robust (closed-form / precise):** Δ_KM (realized−naive RIV gap) = −0.55 flat
(−0.5685/−0.5593 at n=3000/6000, se ~8e-4; analytic vs MC realized info to 1e-10; MCAR→0; monotone
−0.44). Convention settled (K&M observed info). `(A)+(C)` is O(1) under MAR, →0 under MCAR.

**LRT (the load-bearing point):** the intro bullet OMITTED the differential `2[(A+C)1−(A+C)0]`; now
carried (`@sec-thm`/`@sec-combine`/intro). Key: the LRT uses a **paired differential** across candidate
models, which cancels the heavy tail ⇒ **precisely estimable even though the standalone value isn't**.
(Empirical LRT-differential experiment deferred — W2 territory, §6.)

**fitted-vs-oracle (secondary):** verified, RESOLVED — `rederivation-L0-fitted-vs-oracle.R` confirms
FITTED `E[T]=+½tr(RIV)` (ratio 0.985), ORACLE `−½` (the tower misreading), C2 `Δ_n≈T_fitted`. The
`@sec-qfun` callout neutralizes it; memory note marked resolved.

**Artifacts:** `verification/term-ac-rem-distribution.R` (NEW, heavy-tail diagnostic);
`term-ac-rivgap-lavaan.R` (n3000/6000 pin); `term-ac-realized-info.R` (Δ_KM n→6000).
Manuscript render exit-0. **Supersedes todo/018's "realized −0.34→−0.46 settled" value claim** (the
convention settlement + Δ_KM stand). See [[project-nonmonotone-coxsnell]] (REFINED), [[project_fitted_vs_oracle_sign]] (RESOLVED).

---

*Original handoff plan below (executed).*

**One-line goal.** Close the three *soft legs* of the MAR design-imbalance term `(A)+(C)` so the
reported bias is either a closed-form number or a tightly-pinned one — without re-opening the parts
that are already solid (the headline `½tr(RIV)`, the convention, and the `Δ_KM` mechanism).

---

## 0. Where we are (read this first)

The deviance bias decomposes as `E[T] = +½tr(RIV) + [(A)+(C)]`. Two very different confidence tiers:

**TIER 1 — `½tr(RIV)` — DONE (derived + strongly multi-sourced). Do not re-open.**
- Term B `−½tr(RIV)`: elementary Taylor; θ̂_com-target bulletproof.
- Term A `tr(RIV)`: machine-checked vs FIML code (`A − tr(RIV) == 0`); leading order.
- Combine: re-derived via the entropy–Hessian split `∇²C_n = H_φ + I_mis|obs`, **2 CAS + MC**
  (C2/Δ_n reconciliation, closed; [[project_c2_deltan_reconciliation]]).
- `tr(RIV)` is **computable in closed form** (Appendix C, observed info with cross block).

**TIER 2 — `(A)+(C)` MAR term — structure + convention + mechanism DONE; VALUE still soft.**
- Structure derived (α, H_φ, general-`p` Cox–Snell `b_Σ` — `b_Σ` is 2-CAS + MC verified).
- Convention **settled** (todo/018): observed/realized information (K&M 1998); `0` iff MCAR.
- `Δ_KM` (realized−naive RIV gap) **derived analytically** (`verification/term-ac-realized-info.R`):
  `−0.55` non-mono / `−0.44` mono, **flat in N** (O(1)), MCAR→0, analytic `E[I_O]` vs realized Hessian
  to `1e-11`; **block structure + O(1) order cross-checked blind off-lineage** (GPT-5.5, todo/019).

**The THREE SOFT LEGS this todo closes:**
1. The reported `(A)+(C)_realized = −0.34→−0.46` is **empirical** (R=40k, `_modules/term-a-mar-correction.R`),
   not a from-first-principles number. The leading-order analytic assembly `−0.22` undershoots it ~2×.
2. The naive leg `(A)+(C)_naive ≈ +0.1→+0.3` is **anchored** (= committed_realized − gap) and
   high-variance to measure directly (rem_exp se ≈ 0.4–0.8 at R=2000).
3. The realized **asymptote is not pinned** to one number (lavaan gap `−0.627→−0.582→−0.569` still
   approaching the analytic `−0.55`; the realized value itself is "still increasing" at n=1500).

## 1. DECISION FIRST (do not skip — may make most of §2 unnecessary)

**Is the exact `(A)+(C)` value load-bearing for the paper's claims?** Appendix C already records that
for model *selection* the naive-vs-observed information gap "nearly cancels in the arg-min" (roughly
proportional across candidate models), and the headline is `½tr(RIV)` (solid, computable). So the
exact `(A)+(C)` magnitude matters for the **bias level** and **LRT calibration**, **not** for the IC
model-selection headline.

Decide (with the user) one of:
- **(a) Scope it out:** declare "`(A)+(C)` structure derived, convention settled (K&M), magnitude an
  empirically-characterized `O(1)`; exact value not load-bearing for the IC headline." Then §2 is a
  *nice-to-have*, not a blocker, and "fully" is essentially already met for the headline. **Cheapest.**
- **(b) Pin it (Route 1):** tighten the empirical realized asymptote so the reported number has a tight
  CI. "Fully pinned," not "fully derived." Moderate compute.
- **(c) Derive it (Route 2):** derive the higher-order term the `−0.22` Taylor misses → a closed-form
  realized `(A)+(C)`. "Fully derived." Hard analytic; cross-model-check it.

Recommend asking the user (a) vs (b)/(c) before spending analytic effort. Default lean: (a) for the
paper + (b) as a one-off pin for the record.

## 2. Routes to close the value (cheapest-first, if (b)/(c) chosen)

**Route 1 — pin the realized asymptote empirically (cheap, "fully pinned").**
Re-run the phase-8 non-monotone `(A)+(C)_realized = E[A_rb] − tr(RIV^O)` at higher R and more N
(n=3000, 6000) to nail the asymptote with a tight CI. The RB statistic `A_rb` is low-variance; the
remainder `rem` is high-variance (MCSE ≈ 0.65·√(n/R)), so use **large R** and the **paired** structure
where possible. Use **few cores** (segfault gotcha). Files: `_modules/term-a-mar-correction.R` (the
committed empirical), `term-ac-rivgap-lavaan.R` (the paired diagnostic).

**Route 2 — derive the higher-order term (the real "fully derived").**
The `−0.22` assembly is the second-order Taylor of `E[A_rb] − tr(RIV)` at θ₀; it undershoots the
realized `−0.46` by ≈ 0.24. The missing piece is the **higher-order `E[A_rb]` curvature** (third-order
Taylor / the θ̂-vs-θ₀ offset / the realized-information curvature the population-moment assembly omits).
Derive it (Cox–Snell-style next order on `barQ_fiml_analytic`, or the realized-information correction
applied to `E[A_rb]` itself, not just to the RIV). Then `(A)+(C)_realized = E[A_rb]_analytic −
tr(RIV^O)_analytic` (the latter already in hand from `term-ac-realized-info.R`/Appendix C). **Cross-check
blind off-lineage — REQUIRED (user directive): GPT-5.5, `--effort xhigh`, `--timeout 86400` (24h; now
the runner default), launched BACKGROUNDED** (mirror todo/019; protocol in §5). This is the only route
that yields a closed-form number.

**Route 3 — derive the naive leg, use `realized = naive + Δ_KM`.**
If `(A)+(C)_naive = E[A_rb] − tr(RIV^N)` has a cleaner closed form (naive info is block-diagonal,
population moments), derive it; then add the already-analytic `Δ_KM`. **Caveat:** `E[A_rb]` is the same
hard object regardless of which RIV is subtracted, so Route 3 does *not* obviously dodge the
higher-order `E[A_rb]` problem of Route 2 — confirm before banking on it.

## 3. Secondary item — verify (do NOT rebuild) the fitted-vs-oracle exposition

The 2026-06-01 concern ([[project_fitted_vs_oracle_sign]]: 8/9 blind re-derivations read D9's literal
`E[ℓ_com|Y_obs]` as `−½` via the tower property; the fitted `Q̄_∞` gives `+½`) **appears already
addressed**: there is a dedicated callout "`Q̄_∞` is the *fitted* predictive, not the oracle conditional
expectation" (`manuscript/derivation.qmd` `@sec-qfun`, ~lines 368–389) + the D9 notation-clash note +
`verification/rederivation-L0-fitted-vs-oracle.R`. **Task:** read that callout and the script, confirm
they fully neutralize the `−½`-via-tower misreading, and either downgrade the memory note to "resolved"
or list the precise residual wording gap. Likely a 20-minute verification, not a derivation.

## 4. Confirmed facts to carry in (verified; do not re-litigate)

- Convention: observed/realized info (K&M 1998); `0` iff MCAR. Reported `(A)+(C)` = realized `−0.34→−0.46`.
- `Δ_KM` analytic: `−0.55` non-mono / `−0.44` mono, flat in N; MCAR→0; build vs MC `1e-11`. Closed form
  `tr(I_N⁻¹ I_com) − tr(E[I_O]⁻¹ I_com)`; blocks: μμ=0, cross ∝ `E[e_O|P]`, Σ ∝ `M2_P−Σ_OO`.
- Naive leg (anchored, high-variance): `+0.29(n=800)/+0.13(n=1500)`.
- lavaan paired gap: `−0.627/−0.582/−0.569` at n=800/1500/3000 (low-variance; the trustworthy carrier).
- `−0.22` = mixed-convention leading-order approximation to the *realized* value (NOT the naive value;
  **do NOT reassert `−0.22 + Δ_KM = −0.46`** — that is the recorded GOTCHA).
- `b_Σ` general-`p`: derived + 2-CAS + MC.

## 5. Gotchas

- **Heavy parallel R segfaults under contention** — Route 1 uses few cores; prefer analytic/deterministic.
- **`em_mvn` is unreliable for non-monotone** — use lavaan FIML or da.norm.
- **`rem` is high-variance**; use the **paired** info-gap and anchor to the committed `−0.34/−0.46`.
- **The `−0.22 + Δ = −0.46` arithmetic does NOT hold** (the convention-tangle gotcha; see §4).
- **Cross-model protocol (REQUIRED for any analytic derivation — user directive).** Independent model
  = **GPT-5.5**; **`reasoning_effort=xhigh`**; **24h timeout** (`--timeout 86400`, now the runner
  default — the prior `high` run timed out at the old hard-coded 1800s cap, so this is load-bearing);
  launch the runner **BACKGROUNDED** (xhigh reasoning takes hours; backgrounded survives across turns
  and notifies on completion). Build the packet (Mode A blind + Mode B red-team), **hard-strip the
  grading key**, **dry-run `extract_modes`** and token-scan for leakage, verify blind BEFORE sending.
  Runner: `verification/run_layer3_openai.py` (supports `--effort`/`--timeout`/`--package`/`--tag`).
  Caveat: a single 24h HTTPS request may be fragile (idle-connection resets); if it drops, consider the
  OpenAI async/background API rather than one long urllib call.

## 6. DEFERRED (explicitly out of scope for this todo — later session)

- **W1 / W2 / W3 application evidence** (the LRT and IC empirical witnesses, `run_all.R`).
- **Re-evaluating the Satorra–Bentler scaled-correction material** (test calibration; the
  `asparouhovRobustChiSquare2006` / `satorraEnsuringPositivenessScaled2010` thread) — this sits with
  Chan (2022) test-calibration territory, downstream of the numerator bias. Revisit with W1–W3.
- The open W3 (IC) SB-arm bug (CLAUDE.md open issue #1; auxiliary arm, headline unaffected).

## 7. Files / pointers

- Δ_KM (WAY-1): `verification/term-ac-realized-info.R` (+ `cache/term-ac-realized-info-log.txt`).
- `−0.22` assembly: `verification/term-a-mar-closedform.R` (mono), `verify_term_ac_nonmonotone_4v.R` (non-mono + FD).
- Empirical realized (authoritative): `_modules/term-a-mar-correction.R` (R=40k, `−0.34/−0.46`).
- Paired gap / rem: `verification/term-ac-rivgap-lavaan.R` (+ n3000 log).
- `b_Σ` general-`p`: `verification/cas-wolfram/verify_term_ac_nonmonotone_genp.py`.
- Manuscript: `@sec-termA` (the upgraded prose), Appendix C (`#sec-appendix-c`, observed info closed
  form), `@sec-qfun` fitted-vs-oracle callout.
- Convention thread: todo/018 (settled), todo/019 (blind GPT-5.5), todo/016 (closed).
- Commits: `d37183b` (todo/018 resolution), `5803c00` (editorial corrections).
- Memory: [[project-nonmonotone-coxsnell]], [[project_fitted_vs_oracle_sign]], [[project_c2_deltan_reconciliation]].

## 8. Definition of done

Either (a) a user-approved scope decision that the exact `(A)+(C)` value is not load-bearing (with the
manuscript wording matched to that), **or** (b)/(c) a pinned/derived realized `(A)+(C)` value with its
soft legs eliminated (naive leg derived or replaced; asymptote pinned), cross-checked; PLUS a confirmed
verdict on the fitted-vs-oracle exposition. `quarto render` exit-0; `/derivation-audit` 0 BLOCKER.
W1–W3 + Satorra–Bentler remain deferred.

*Handoff 2026-06-02. Continues the todo/015–019 (A)+(C) thread.*
