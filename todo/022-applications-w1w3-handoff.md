# Todo 022 — Handoff: shore up the W1–W3 application witnesses

**Status:** Handoff (2026-06-02). Execute in a **fresh session**. Continues todo/020 (the bias
derivation + correction, now settled and audited). This todo is the **application-evidence** layer that
todo/020 §6 explicitly deferred, scoped by the adversarial confidence audit run at the end of the
todo/020 session.

## 0. What is LOCKED — do NOT re-open

The deviance-bias derivation is settled and adversarially audited (5-pillar confidence audit,
independent agents on committed artifacts). Carry these as given:

- **Headline `E[T]=+½tr(RIV)`** + the `+tr(RIV)` / `−½tr(RIV)` split, and the `+tr(RIV)` deviance/IC
  correction (= Shimodaira `AIC_{x;y}`). SOLID; honestly scope-fenced to **estimated-scale/covariance**
  models (known-scale collapses to 0 / `−½tr`); `Q̄_∞` is the fitted predictive (not oracle).
- **`(A)+(C)` structure + convention (K&M realized info) + closed-form `Δ_KM≈−0.55`.** SOLID.
- **`(A)+(C)` absolute value:** sign, `O(1)` order, MCAR-vanishing, and the `O(1/n)` correction order
  are FIRM; the value itself is **not independently pinned** (the −0.22 is a leading-order analytic
  anchor the control variate is conditional on; manuscript wording matches this — `@sec-termA`). Do not
  re-tighten this to a pinned number without a NEW estimator that does not take −0.22 as an input.

Commits this session: `f1dda46`, `17ba403`, `46013b0`, `77a99c9`, `f35e048`. Audit output:
`tasks/.../wpmfmc3pt.output` (5-pillar verdicts).

## 1. The W1–W3 / applications work-list (from the audit's flagged items)

**A. Reconcile the preregistered W1 verdict (Pillar 1 + Pillar 5 finding).**
`verification/cache/run_all-prod/phase5/verdicts.md` records **H1 (the +½tr(RIV) headline) = FAIL** on
the monotone-vs-non-monotone **diff** criterion, even though MAR per-cell `passT=TRUE` and MNAR is
out-of-scope by design. The clean `+½` in the manuscript leans on the *controlled* run
(`rederivation-L0-fitted-vs-oracle.R`, N=200 R=4000, ratio 0.985); the *preregistered* W1 sweep is
noisier/non-monotone (`That/½tr ≈ 0.55/0.32/0.16/0.37` across N, `passT=FALSE` at N=1000;
`phase1-w1/summary.csv`). **Task:** decide whether to (i) re-run W1 at higher R / more N to pin the
`+½tr(RIV)` trend cleanly in the estimated-Σ MAR regime, (ii) amend the preregistration diff-criterion
with a documented rationale, and/or (iii) surface the controlled-vs-sweep tension at `@sec-thm`. Do NOT
silently rely on the controlled run alone.

**B. Component-level finite-n behavior (Pillar 1).** Individual terms `E[A]`, `E[B]` miss their MC
targets by 9–20% at finite n (only the **total** `T` and the **paired `Δ_n`** are tight). Characterize
the finite-n convergence of the individual terms, or state in the W1 write-up that only the total +
paired contrast are MC-tight.

**C. W2 (LRT) — back the differential claim empirically (Pillar 5).** The manuscript now says the LRT
`(A)+(C)` differential is "structurally better-conditioned" (a variance-structure claim, NOT a committed
measurement). **Task:** build a *paired* estimator that directly measures the between-model `(A)+(C)`
differential `2[(A+C)_ψ* − (A+C)_ψ0*]` on the same data and shows the heavy-tailed noise cancels (mirror
`term-ac-controlvariate-pin.R`'s pairing, but across nested models). Then the "better-conditioned"
clause can be upgraded from theory to evidence. Existing W2 witness: `W2-prod-fiml.rds` (rejection
table, null calibration `C3_uncorrected≈0.044`, `trRIV_un≈4.98` vs `cn≈3.96`).

**D. W3 (IC) — calibrate the "restores" wording (Pillar 5).** Committed `phase2-w3/summary.csv`:
corrected selection `π≈0.81` vs oracle `π≈0.90` (uncorrected `≈0.65`), `W3C_high_RIV_frac=1.0`. So the
correction **substantially recovers** but does not fully reach the oracle (`~0.09` residual = finite-n
MI-AIC noise, per Appendix C). Reword the intro IC bullet's "restores complete-data-equivalent
selection" to match Appendix C's candor, or pin the residual.

**E. Open W3 SB-arm bug (CLAUDE.md issue #1).** The W3 (IC) SB arm applies the scaled-shift to the
*uncorrected* deviance; auxiliary arm only, headline unaffected. Fix or formally retire.

**F. Proper-MI engine-independence (gap, honestly disclosed).** Data augmentation (`da.norm`) not run;
robustness shown only for EMB/Amelia (W3-A gap `0.011`, within 2–3%). Either run DA or keep the
empirical-only scoping explicit for the proper-MI novelty.

## 2. Also-deferred (todo/020 §6) — revisit alongside W1–W3

- **Satorra–Bentler scaled-correction / Chan-2022 test-calibration** re-evaluation
  (`asparouhovRobustChiSquare2006`, `satorraEnsuringPositivenessScaled2010`) — downstream of the
  numerator bias; pair with W2.

## 3. Guardrails (carried)

- Few-core R (segfault under contention); lavaan FIML / `da.norm` for non-monotone (em_mvn unreliable);
  heavy-tailed `(A)+(C)` statistics ⇒ prefer paired/control-variate estimators, not brute-force means.
- Citation discipline: any new `@cite` needs `literature/<key>.md` read in-session.
- Any analytic derivation ⇒ blind GPT-5.5 xhigh/24h cross-check, backgrounded (the standing directive;
  template todo/019/021).
- Touch the manuscript ⇒ `quarto render` exit-0 + `/derivation-audit` 0 BLOCKER (3 cas-wolfram WARN are
  known brace-glob false positives).

*Handoff 2026-06-02. The bias theory is done + audited; this is its empirical-application layer.*
