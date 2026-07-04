# Derivation audit — `manuscript/derivation.qmd`

**Run:** 2026-06-01 17:44 · **Skill:** `/derivation-audit` (read-only; flag-only) · **Target:** `manuscript/derivation.qmd` (1806 lines)

**PASS (with warnings)** — 0 BLOCKER / 10 WARN / 14 INFO

A citation `0/0/0` · B evidence↔source `2 WARN / 5 INFO` (25/25 attributions graded supported or partially-supported; 0 mismatch, 0 unverifiable) · C reproducibility `2 WARN / 1 INFO` · D consistency `2 WARN` · E honesty `1 WARN / 2 INFO` · F lifecycle `3 WARN / 6 INFO`

**Method.** Mechanical engine (`audit_derivation.py`: 0 BLOCKER / 5 WARN / 13 INFO) + 5 parallel source-readers that read the actual `literature/<key>.md` text for all 25 cited keys + direct verification of every prose R-pointer, phase cache, and the closed-form/`todo/008` artifacts. **No citation is hallucinated or unbacked** — every `@key` resolves to a real, substantial source whose text supports its attribution. The flags below are about *precision* (4 load-bearing "partially-supported" attributions), *internal consistency*, and *reproducibility hygiene* — not fabricated evidence.

---

## BLOCKER (0)

None. Every `literature/<citekey>.md` exists and is substantive; every load-bearing attribution (missing-information identity → Schafer eq 3.19 *conditional-on-Y_obs*; RIV scalar → Rubin 1987; observed-info-under-MAR cross term, orthogonality-lost-iff-MCAR, observed-info recommendation → Kenward §3.2/§5; AIC_{x;y} penalty = tr(RIV), PDIO/AICcd double → Shimodaira-Maeda 2017; ψ̂* maximizes the averaged log-lik → Chan & Meng 2022 eq 2.1–2.2; MVN info → Magnus; monotone Σ̂ bias → Kanda & Fujikoshi) is verbatim-grounded in the local text. All 64 linerefs resolve; all 11 `lst-mc` listings exist; all 7 engine fingerprint-misses confirmed FAITHFUL (Mathpix markup, not drift).

## WARN (10)

- `derivation.qmd:565` (margin `:570`) [B, **load-bearing**] — L4 states the variance-recovery **equality** `T_∞ = Var(θ̂_obs) = I_obs⁻¹` and attributes it to Meng (1994) Lemma 3 + Main result, but Meng's local text states an efficiency **inequality** ("at least as efficient … at most the same width"; Lemma 3 = MI variance ≤ Var(θ̂_obs)), with equality requiring an extra condition — evidence: Meng `:503–:511` give "≤", not "=" — fix: derive the equality from congeniality (R4) explicitly, or lead the citation with Rubin 1987 §4 for the equality and cite Meng for dominance (Rubin §4's backing of the exact equality was *not* independently re-verified this pass — confirm it).
- `derivation.qmd:603` [D, headline-adjacent] — the Theorem statement calls the general-MVN **monotone** `(A)+(C)` asymptote "measured, not yet closed-form" and quotes phase-8 empirical (monotone `−0.18→−0.27`, "asymptote ≈−0.3"), but `@sec-termA` (`:828–:831`) *derives a general-MVN monotone closed form* `(A)+(C)_∞ ≈ −0.22` (stable in n) — evidence: same object, two framings + numbers (`≈−0.3` vs `−0.22`) — fix: update the Theorem to cite the `−0.22` monotone closed form and restrict "empirical only" to the non-monotone case (consistent with `:837–:842`).
- `derivation.qmd:59` [E/D, headline] — "this ½ tr(RIV) is **exact under MCAR**" overstates a leading-order result: the theorem carries `+O(n⁻¹)` (`:589`), the body states "`(A)+(C)=O(n⁻¹)` under MCAR" (`:717`), and L2 is "exact only to leading order" (`:556`) — evidence: "exact" contradicts the doc's own `O(n⁻¹)` remainder — fix: "to leading order under MCAR" / "the design-imbalance term vanishes (`O(n⁻¹)`) under MCAR".
- `derivation.qmd:541` [D] — proof invokes `A8` (also `:562`) and `A7` (`:1547`) as if labeled identities, but no `A1–A8` labels are defined anywhere; `@sec-alg` lists the matrix/expectation identities as **unlabeled bullets** — evidence: grep finds only *uses* of `A7`/`A8`, no definitions — fix: number the `@sec-alg` identities `A1–A8` (so `A7`=Gaussian-conditional/Schur, `A8`=quadratic-form/score-covariance), or replace `A7/A8` with the named identity.
- `derivation.qmd:1198` [C] — Appendix-B intro cites `verification/W1-sweep.R` as "the Monte Carlo study", but that path exists **only under `_legacy/`** (retired; CLAUDE.md forbids citing legacy as live) — evidence: `verification/W1-sweep.R` absent; present at `verification/_legacy/W1-sweep.R` — fix: point to `verification/W1-bias-decomposition.R` (preregistered) or `verification/_modules/w1-sweep.R` (the run_all module), or the `phase1-w1` cache.
- `derivation.qmd:1302` [C] — listing `lst-mc-trriv` has no `assert`, yet the Verification-summary table (`:1717`) lists it as a checked "symbolic" identity — evidence: cell only `print`s `trRIV` (the identity is asserted *transitively* in `lst-mc-terma/termb/combine`) — fix: add a one-line `assert` (normal form == `Trace(I_obs.inv()*I_com) − n`), or mark the summary row "helper".
- `derivation.qmd:110` [B] — "[Shimodaira 2017] itself named there (§8) as the **open** 'missingness × covariate-shift' direction" overstates the source: its concluding remarks frame this as the authors' forward *plan* ("we plan to work on … combine a missing mechanism with … covariate-shift"), and "design-imbalance" is the manuscript's gloss — evidence: source `:486` is future-work phrasing, not a flagged open limitation — fix: soften to "named as future work in its concluding remarks". (This props up novelty claim (ii), so worth tightening.)
- `derivation.qmd:173` [F] — `@littleStatisticalAnalysisMissing2019` cited but untracked in any lifecycle log (neither `todo/003` nor `todo/001`) — evidence: author/year absent from both — fix: add a lifecycle row marking it verified/cited (foundational; verified in-session this audit).
- `derivation.qmd:187` [F] — `@rubinInferenceMissingData1976b` cited but untracked in any lifecycle log — evidence: absent from `todo/003` and `todo/001` — fix: add a verified/cited row (foundational; verified in-session).
- `derivation.qmd:523` [F] — `@andersonIntroductionMultivariateStatistical2003` cited but untracked in any lifecycle log — evidence: absent from `todo/003` and `todo/001` — fix: add a verified/cited row (foundational; verified in-session).

## INFO (14)

- `derivation.qmd:1151, :1166, :1170, :1080, :1084, :1028` [B] — the 6 Appendix-A snippet fingerprint-misses (Kenward, Pawitan ×2, Little ×2, van der Vaart) are **confirmed FAITHFUL** by source-readers — evidence: each quote matches its source verbatim modulo Mathpix math/subscript markup — fix: none (mechanical artifact; quotes are good).
- `derivation.qmd:943` [B] — Schafer eq (3.2) Appendix-A quote is faithful (elides the observed-data-loglik RHS via "…"), **but** `literature/schaferAnalysisIncompleteMultivariate1997.md` itself carries a source-side OCR garble there ("`=log P(Y|θ)`" repeated where it should read "`=log P(Y_obs|θ)`") — evidence: file line ~947 — fix: re-sync/clean that line in the corpus copy (manuscript needs no change).
- `derivation.qmd:813` [B] — the monotone sequential-regression factorization is a joint cite `[anderson; little; schafer]`; Anderson's own backing is exercise-level (Problem 4.48 / Anderson 1957), not a general main-text development — evidence: a1/a2 (conditional dist) are main-text; the general j-block monotone sequence is carried by Little&Rubin/Schafer (and Kanda&Fujikoshi prints the full factorization) — fix: none (joint cite is fair).
- `derivation.qmd:96` [B] — Chan (2022) calibrates the **OMI/FMI** spectrum (eigenvalues of `I_mis I_com⁻¹`), which is RIV-*adjacent*, not literally `RIV = I_mis I_obs⁻¹`; the manuscript's "reference distribution" / "-type" phrasing stays accurate — evidence: source defines `r_j` via `F=I_mis I_com⁻¹` — fix: none unless ever tightened to "RIV spectrum" (then say OMI/FMI).
- `derivation.qmd:120` [B] — "Hens et al. … explicitly leaves a **bias-corrected** *imputation*-based criterion … as open": the source leaves an imputation-based AIC as "topic of current research" but not specifically a *bias-corrected* one ("bias-corrected" is the manuscript's qualifier) — evidence: hens `:516` — fix: drop "bias-corrected" or soften.
- `derivation.qmd:671, :867` [E] — house-jargon "consume(s)" in reader-facing proof prose ("Term B/A consumes …") — evidence: ban list (intro/proof-sketch prose) — fix: "Term B uses / is governed by the variance of the gap".
- `derivation.qmd:427` [E] — section anchor `#sec-ledger` uses banned house-jargon "ledger" (anchor id only; the rendered heading is "Assumptions and lemmas", so not reader-visible) — evidence: cosmetic — fix: optional rename to `#sec-assumptions`.
- `derivation.qmd:606` [C] — the **non-monotone** `(A)+(C)` asymptote ("≲−0.46") is extrapolated from two still-increasing finite-n points (`−0.34` at n=800 → `−0.46` at n=1500); the doc honestly flags it "measured, not yet closed-form / reported empirically" — evidence: 2-point trend, not converged — fix: none required (already hedged); a third n would firm it up.
- `derivation.qmd:29, :33, :73, :77, :94, :220` [F] — 6 foundational keys (Rubin 1987, Meng 1994, Chan & Meng 2022, Chan 2022, Meng & Rubin 1992, van der Vaart 1998) are in `todo/001` not the `todo/003` proposal lifecycle — evidence: author/year present in `001-literature-and-hooks.md` — fix: expected for the Phase-1 corpus; no action.

---

## Source-check coverage (positive verdicts, for the record)

All 25 cited keys read in-session; files confirmed real (line counts): schafer 8628, little 11763, vaart 14120, pawitan 21674, anderson 10895, kanda 1340, chanMeng 1241, cox 1092, meng1994 790, hyodo 620, konishi 613, cavanaugh 599, shimodaira2017 583, kenward 579, shimodaira2000 572, hens 562, chan2022 528, cordeiro 444, claeskens 407, rubin1976 394, meng1992 362, efron 960, rubin1987 7240, magnus 1840, petersen 3927.

- **IC headline (Shimodaira-Maeda 2017):** AIC_{x;y} penalty = `d + tr(I_{z|y} I_y⁻¹)` (the tr(RIV)/FMI trace) — supported; "only half the value of that in PDIO" + empirical over-penalization (Table 1) — supported; §8 covariate-shift "open" — *partially* (future-work framing → WARN above).
- **Cavanaugh-Shumway 1998 / Claeskens-Consentino 2008 / Hens 2006:** AICcd `2·tr(I_oc I_o⁻¹)` penalty — supported; Claeskens Takeuchi-type penalty on a different (EM-adjusted) discrepancy — supported; Hens IPW/HT, penalty stays `2K`, `Cov(y,π)/E[π]` MAR shift — supported (only "bias-corrected" qualifier soft → INFO).
- **Chan / LRT calibration:** Chan 2022 SMI drops EFMI + MC/full-spectrum reference — supported; Chan & Meng 2022 ψ̂*=argmax of the averaged log-lik (eq 2.1–2.2) — supported; Meng-Rubin 1992 pooled D_L→F — supported; complementarity (they calibrate the reference, take the numerator as given; no deviance-bias correction in either Chan file) — supported.
- **MAR observed-info (Kenward, Efron, Pawitan, Konishi):** all 13 sub-claims supported, all 3 fingerprints FAITHFUL.
- **Core MI foundations (Schafer, Meng 1994, Rubin 1987/1976, Little, vaart):** all supported except Meng L4 equality (→ WARN above); Schafer's conditional-on-Y_obs framing of eq 3.19 explicitly confirmed (`:1504` "each quantity … is a function of Y_obs although this fact has been suppressed").
- **Matrix/MVN/monotone bias (Magnus, Petersen, Anderson, Hyodo, Kanda, Cox-Snell, Cordeiro-Klein):** all supported (Anderson monotone-factorization joint-cite nuance → INFO; Kanda "exact bias of Σ̂" verbatim; Cox-Snell O(n⁻¹) bias formula and Cordeiro-Klein matrix correction both present).

## Artifact verification (dimension C)

- Prose R-pointers all resolve **except** `verification/W1-sweep.R` (legacy → WARN). Present & on-topic: `00-setup.R`, `W1-bias-decomposition.R`, `term-a-mar-diagnostic.R`, `term-a-mar-closedform.R`, `lemma-revalidation.R`, `_modules/term-a-mar-correction.R`, `_modules/w1-sweep.R`, `manuscript/proof-verification-fixture.json`.
- Phase caches exist: `phase0..7` under `run_all-prod`; `phase8-terma-mar` under `run_all-terma` (**git-tracked** → "committed phase-8 sweep" is accurate), also under untracked `run_all-cal`/`run_all-smoke`.
- `term-a-mar-closedform.R` computes `(A)+(C)_∞ = α'b_Σ + ½tr(H_φ I_obs⁻¹)` with an MCAR control; header confirms `MAR ≈ −0.22 (design imbalance); MCAR ≈ 0 (control). Fully analytic, no finite diff.` — matches the manuscript's `+0.54 / −0.76 / ≈−0.22` claims.
- `todo/008-information-diagnostic.md`: the earlier "two RIVs" framing is **SUPERSEDED (2026-05-31)** to a single observed-data RIV; the derivation's "both terms calibrate to the single observed-data RIV" callout (`:887–:912`) reflects the current understanding, and the phase-6 numbers (`tr(I_com·Var(gap))≈6.0` vs `5.5`; `tr(𝒥̂ I_obs⁻¹)≈13.9≈k=14`) reproduce.

---

## Bottom line

The derivation is citation-clean at the BLOCKER level: nothing is hallucinated, every source backs its claim, and the headline `½ tr(RIV)` and its IC/LRT positioning are verbatim-grounded. The substantive items to address before submission are the four reader-facing precision issues — **(W1)** the Meng-vs-equality attribution for L4, **(W2)** the stale "not-yet-closed-form" Theorem text vs the `−0.22` monotone closed form, **(W3)** "exact under MCAR", and **(W4)** the undefined `A7/A8` labels — plus the legacy `W1-sweep.R` pointer (W5). Everything else is hygiene (lifecycle rows, jargon, one missing assert).

*Engine JSON dump (mechanical half only) at `C:\Users\marcu\AppData\Local\Temp\derivation-audit.json` (transient).*
