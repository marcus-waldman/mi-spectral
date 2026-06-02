# Todo 018 — Reconcile the (A)+(C) value: realized vs expected observed information

**Status: ✅ DONE (2026-06-02).** Continues todo/015–016; sibling of todo/017 (different axis — see §7).

## ✅ OUTCOME — the (A)+(C) value is SETTLED

- **Step 0 (convention, from the literature):** Kenward & Molenberghs (1998),
  `literature/kenwardLikelihoodBasedFrequentist1998.md`, §3.2 + §5 + abstract — under MAR the
  **observed (realized)** information is the principled choice; the naive expected (population Σ_OO,
  pattern-fixed) info is **biased**, with cross-terms **0 iff MCAR**. ⇒ the reported `(A)+(C)` is the
  **realized** `−0.34→−0.46`; `−0.22` is a leading-order approximation (right sign/order, undershoots).
- **Step 1 / WAY 1 (Claude analytic, `verification/term-ac-realized-info.R`):** realized-information
  term `Δ_KM = tr(I_N⁻¹ I_com) − tr(E[I_O]⁻¹ I_com)`, closed form from the per-pattern selected moments
  (μ×Σ cross block ∝ selection shift `m1_P`, Σ block ∝ `M2_P−Σ_OO`); analytic `E[I_O]` vs MC realized
  Hessian to `1e-11`; `Δ_KM ≈ −0.55` (non-mono) / `−0.44` (mono), **n-stable** (O(1)); MCAR control →0.
- **Step 1b / WAY 2 (blind GPT-5.5, `todo/019`, `cache/layer3-gpt-5.5-acinfo-mode{A,B}.md`):** off the
  Claude lineage, independently returns the **same** ΔI block structure, the same closed form `D =
  tr(J_N⁻¹ J_com) − tr(J_O⁻¹ J_com)`, **O(1)** under MAR (Mode B explicitly rejects the O(1/n)
  off-ramp — the todo/016 blind spot, not repeated), 0-iff-MCAR, and spontaneously the K&M
  observed-info recommendation. **The two ways AGREE.**
- **Step 2 (lavaan, n=800/1500/3000, `cache/rem-realized-expected-lavaan-n3000-log.txt`):** paired gap
  `−0.627→−0.582→−0.569` converges onto the analytic asymptote `−0.55` ⇒ O(1), **not finite-n** (Q3
  resolved). Self-consistent: `(A)+(C)_realized = (A)+(C)_naive[+0.1→+0.3] + Δ_KM[−0.6]` reproduces
  `−0.34→−0.46`.
- **Step 3 (Louis cross-term):** `tr(C I_obs⁻¹) = RIV` is **exact under the realized convention** (C =
  selected missing info; committed RIV uses realized I_obs) — the lemma caveat was sign-fixed (it had
  said "holds under expected"; it holds under realized).
- **Step 4 (manuscript):** `@sec-termA` + `@sec-combine` upgraded from "not yet settled" to the
  confirmed realized-convention statement; `quarto render` exit-0; `/derivation-audit` PASS (0
  blockers); `todo/016` open flag closed. Committed on main.

**GOTCHA recorded:** the plan's `−0.22 + Δ ≈ −0.46` arithmetic does NOT hold — `−0.22` is a
mixed-convention leading-order approx to the *realized* value, not the clean naive value; the
self-consistent decomposition uses the measured naive `+0.1→+0.3`, not `−0.22`. See
[[project-nonmonotone-coxsnell]].

---

*Original plan below (executed).*

**One-line goal.** Pin down the **numerical value** of the MAR design-imbalance term `(A)+(C)`, which
this session found to be **information-convention-dependent and currently unresolved**. Decide which
observed-information convention the reported `(A)+(C)` should use, derive the missing **realized-
information term** in closed form — **derived two independent ways: (i) here with Claude (analytic,
from the selected moments), and (ii) blind via GPT-5.5 through the API (Layer-3 cross-model, as in
todo/016)** — confirm it reproduces the empirical, and then **upgrade `@sec-termA`** from its current
honest "value not yet settled" status to a settled statement. Cross-model agreement is the bar (the
b_Σ work and todo/016 showed a single lineage can share a blind spot).

---

## 0. Why this is open (context for a cold session)

Original task (todo/015): derive general-`p` `b_Σ` and reproduce the empirical non-monotone
`(A)+(C) ≈ −0.46`. The `b_Σ` was derived and validated (solid). But assembling `(A)+(C)` exposed a
deeper problem:

- The analytic assembly `(A)+(C) = αᵀE[δ] + ½ tr(H_φ I_obs⁻¹)` gives **≈ −0.22** (two ways: analytic
  α/H_φ AND finite-differencing `barQ`), for BOTH monotone and non-monotone designs.
- The committed empirical (`_modules/term-a-mar-correction.R`, R=40k) is **−0.18→−0.27 (monotone),
  −0.34→−0.46 (non-monotone)** over n=800,1500, **both increasing**.
- A GPT-5.5 Layer-3 check (todo/016, `ffff008`) flagged the two-term decomposition as incomplete; the
  named extra terms turned out tiny (`B_cov=−0.02`) or cancel by Louis (`Δ`).
- A clean **lavaan-FIML** decomposition (`9193769`) localized it: the empirical subtracts the
  **realized** (K&M) observed-information Hessian; the paired `tr(RIV; realized) − tr(RIV; expected
  Fisher) ≈ −0.6`, roughly **n-stable** — a genuine **O(1) MAR effect** (the *selected* second moments
  in the realized Hessian), NOT finite-n.

So `(A)+(C)` swings ~0.6 with the information convention; `−0.22` is the *expected/population* value,
`−0.46` the *realized/selected (K&M)* value, and the analytic matches neither cleanly. `@sec-termA` was
**de-speculated** (`85ad410`) to say so honestly. This todo settles it.

## 1. The precise open questions

1. **Which convention is principled?** Does the K&M (1998) / Rubin RIV the paper calibrates to use the
   **observed** (realized Hessian) or **expected** (Fisher) information? The empirical uses realized
   (cross-inclusive observed info, K&M). Pin this from the literature — it decides which value is "the"
   `(A)+(C)`. (Check `literature/` for K&M 1998 / Kim & co.; the manuscript already cites it.)
2. **Closed-form realized-information term.** The gap is the **selected-vs-population second moments**
   entering `observed_info_obs_mvn` (the `Si·crossprod(e_O)·Si` term) under MAR. Derive it in closed
   form from the **selected moments** `M2_P = E[e_O e_Oᵀ | P]` the assembly already computes
   (`est_moments`) — it should be `tr((I_mis^sel − I_mis^pop) I_obs⁻¹)`-shaped. Add it to −0.22 and
   check → −0.46.
3. **n-dependence.** The empirical is still *increasing* at n=1500. Is the realized-info `(A)+(C)` a
   single O(1) constant (and the empirical converging to it), or genuinely n-growing? Resolve whether
   −0.46 is the asymptote or it keeps climbing (the lavaan gap shrinks slightly, −0.63→−0.58, so the
   limit is uncertain).
4. **θ₀ vs θ̂.** The assembly evaluates at θ₀; the empirical at the biased fit θ̂. Quantify whether
   this contributes to the gap (likely small vs the −0.6 info effect, but check).
5. **Cross-term (Louis) bookkeeping.** Re-derive `tr(C I_obs⁻¹)` (C = eval–impute cross-Hessian)
   under the **realized** convention: does it cancel `tr(RIV; realized)` exactly (→ clean derivation of
   −0.46), and where does the lemma's "no −tr(RIV) correction enters" (now caveated) actually stand?

## 2. Confirmed numerical facts (carry into the cold session)

- Analytic `(A)+(C)` (expected info): **−0.22** — mono (`+0.54 − 0.76`), non-mono (`+0.78 − 1.00`).
- Empirical `(A)+(C)` (realized/K&M): mono `−0.18→−0.27`, non-mono `−0.34→−0.46` (n=800,1500), increasing.
- Paired info gap `tr_exp − tr_real ≈ −0.6` (non-mono; `−0.63@800 → −0.58@1500`), em- and lavaan-robust.
- `B_cov = tr(I_obs⁻¹ Cov(S_obs,g)) = −0.02` (tiny, →0 MCAR); `Δ` cross-Hessian cancels by Louis.
- 4-variate `b_Σ` (vech): `s11=s22=−1.391, s21=−0.722, s31=s42=−0.30, s33=s44=−1.0, s43=−0.5, s41=s32=0`.
- MCAR controls `≈0` throughout (the whole effect is MAR-driven).

## 3. Plan (cheapest-first)

**Step 0 — literature/definitional (decides everything).** Settle Q1: read the K&M 1998 RIV
definition (observed vs expected info) in `literature/`. If K&M/Rubin RIV is the **observed**
(realized) information, then **−0.46 is the correct `(A)+(C)`** and the task's original target was
right — proceed to derive it (Step 1). If expected, then −0.22 is correct and the empirical −0.46 is a
realized-info finite-sample diagnostic to report separately.

**Step 1 — derive the realized-information term (analytic, no MC) — WAY 1 (Claude).** Extend the
`term-a-mar-closedform.R` assembly to compute the realized-info correction from the per-pattern
selected `M2_P` (already in `est_moments`). Target: `(A)+(C)_realized = −0.22 + Δ_realized ≈ −0.46`.
This is pure matrix algebra on quantities the assembly has — fast, deterministic, no segfault risk.

**Step 1b — independent derivation via GPT-5.5 — WAY 2 (cross-model).** Build a focused Layer-3
packet (mirror `todo/016`: blind Mode A + red-team Mode B, grading key hard-stripped) asking GPT-5.5
to derive *from scratch* the `O(1)` realized-vs-expected (selected-vs-population) observed-information
contribution to `E[A_rb] − tr(RIV)` for the pattern-mixture MVN under MAR. **Blind it:** do NOT leak
−0.22 / −0.46 / Claude's closed form / the `M2_P` route. Run via
`py verification/run_layer3_openai.py gpt-5.5 --package todo/0XX-... --tag -acinfo` (the runner
hard-truncates at the GRADING KEY banner). **Cross-check:** Claude's Δ (Step 1) ≡ GPT-5.5's, to
agreement; a disagreement is the signal to investigate (as todo/016's B_cov catch showed). Verify the
packet is blind + key-stripped before sending (the `extract_modes` dry-run check in todo/016).

**Step 2 — confirm vs empirical (lavaan, paired, low-variance).** Reuse
`scratch-rem-realized-expected-lavaan.R` (the working diagnostic). Confirm the analytic realized-info
`(A)+(C)` matches the empirical −0.34→−0.46 across n, and resolve Q3 (asymptote vs growing) by adding
n=3000 (gap is precise; anchor rem_real to committed). **Run with FEW cores** (see §5).

**Step 3 — clean cross-term derivation (Q5).** Reconcile the Louis cross-term bookkeeping under the
realized convention so the result is *derived*, not just numerically matched.

**Step 4 — decide & rewrite `@sec-termA`.** Upgrade from "value not yet settled" to the confirmed
value/convention. If −0.46 is confirmed correct: state `(A)+(C)` with the realized-information term
derived (this *delivers* the original −0.46 target). Update the monotone passage consistently. Keep
`quarto render` exit-0; run `/derivation-audit` afterward to catch any residual over-claiming.

## 4. What's confirmed vs what must NOT be re-asserted until settled

- **Confirmed (keep):** `(A)+(C)` is O(1) under MAR, 0 under MCAR; `b_Σ` derived (general-p); the
  decomposition *form*; the empirical values as measured facts.
- **Do NOT re-assert** until Step 0–3 settle it: that −0.22 is "the" `(A)+(C)`, or that −0.46 is a
  finite-n artifact. (Both were the speculation removed in `85ad410`.)

## 5. Gotchas (carried from this session)

- **`em_mvn` is unreliable for the non-monotone design** (opposite-sign `rem` vs lavaan). Use **lavaan
  FIML** (or da.norm) for fits. `scratch-realized-vs-expected.R` uses em_mvn — treat as untrustworthy;
  `scratch-rem-realized-expected-lavaan.R` is the good one.
- **Heavy parallel R segfaults under contention** (a 20-core job crashed while todo/017 ran
  concurrently). Use **few cores** and prefer **analytic/deterministic** computation (Step 1) over big
  parallel MC.
- **`rem` is high-variance** (MCSE ≈ 0.65·√(n/R)); use the **paired** info-gap (low variance) and
  anchor `rem_real` to the committed −0.34/−0.46. The FD cross-Hessian "bracket" is noisy per-dataset
  (±0.3) — derive it analytically (Step 1), don't rely on FD MC.
- **FIML vs proper-MI:** the FIML `(A)+(C)` uses `Var(φ̃)=I_obs⁻¹`; proper MI ≈ doubles `(C)`. This
  axis is **todo/017** (engine); keep it separate, but be aware the "which info / which Var(φ̃)"
  questions interact.

## 6. Files / pointers

- Analytic assembly (extend here for Step 1): `verification/term-a-mar-closedform.R` (monotone, −0.22),
  `verification/verify_term_ac_nonmonotone_4v.R` (non-monotone assembly + FD).
- `b_Σ`: `verification/cas-wolfram/verify_term_ac_nonmonotone_genp.py` (+ genp4.json cache).
- Empirical (authoritative): `_modules/term-a-mar-correction.R` (committed −0.34/−0.46);
  caches `cache/run_all-*/phase8-terma-mar/summary.csv`.
- Realized-vs-expected diagnostic: `verification/scratch-rem-realized-expected-lavaan.R`
  (+ `cache/rem-realized-expected-lavaan.rds`); `scratch-bcov-check.R` (B_cov).
- Info objects: `observed_info_obs_mvn` (realized Hessian, selected M2) vs `fisher_info_obs_mvn`
  (expected, Σ_OO) in `verification/00-setup.R`.
- Commits: `446d1a4` (b_Σ + first reframe), `ffff008` (GPT-5.5 Layer-3), `9193769` (lavaan diagnostic),
  `85ad410` (de-speculation). Memory: `[[project-nonmonotone-coxsnell]]`. Status note: todo/016
  "GRADING OUTCOME".

## 7. Relationship to todo/017 (do not conflate)

- **todo/018 (this):** *information-convention* axis — realized vs expected observed information in the
  `(A)+(C)`/RIV. Draw-free (FIML/analytic).
- **todo/017:** *imputation-engine* axis — Amelia EMB vs da.norm for the proper-MI witnesses.
  Both bear on "what is the right `(A)+(C)`," but they are independent questions; settle 018 analytically
  first (it's cheaper and may resolve the headline value).

## 8. First steps (fresh session)

1. Read this + todo/016 "GRADING OUTCOME" + `[[project-nonmonotone-coxsnell]]`.
2. **Step 0**: read the K&M 1998 RIV definition in `literature/` — observed or expected info? (decides
   which value is correct).
3. **Step 1 (Way 1)**: derive the realized-information term analytically from the selected moments;
   check `−0.22 + Δ ≈ −0.46`.
4. **Step 1b (Way 2)**: build the blind GPT-5.5 packet, verify it's key-stripped, run it, cross-check
   GPT-5.5's Δ against Claude's.
5. Confirm (Step 2, lavaan, few cores), reconcile the cross-term (Step 3), then rewrite `@sec-termA`.

## Definition of done

A settled, *derived* `(A)+(C)` value with its information convention justified from the literature; the
realized-information term in closed form **derived two independent ways (Claude analytic + GPT-5.5
blind) that agree**, reproducing the empirical −0.34→−0.46 (and its monotone counterpart);
`@sec-termA` upgraded from "not yet settled" to the confirmed statement (render exit-0,
derivation-audit clean); and `todo/016`'s open flag closed.

*Plan 2026-06-02. Continues the todo/015–016 (A)+(C) thread.*
