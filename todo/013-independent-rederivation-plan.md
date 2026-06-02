# Todo 013 — Independent adversarial re-derivation of the deviance-bias theorem

**Status:** Draft (2026-06-01). Strategy plan; not yet executed.

**Goal.** Move the *novel* part of the theorem — the decomposition
`E[A] = +tr(RIV) + (A)+(C)`, `E[B] = −½tr(RIV)`, net `E[T] = +½tr(RIV) + (A)+(C)` — from
single-source internal verification to **multi-source triangulation**, culminating in a
cross-model conceptual check of the premises that no computer-algebra system can validate.

---

## 1. Why this plan exists (honest evidence audit)

| Claim | Current evidence | Tightness |
|---|---|---|
| Penalty value `tr(RIV)` | CAS-exact algebra (SymPy **and** Wolfram, commit `3977bdd`); MC W1 within MCSE; **external convergence** with Shimodaira–Maeda 2017 `AIC_{x;y}` derived by a different route | **High** (multi-source) |
| **Decomposition** `+tr(RIV)` / `−½tr(RIV)` | our own SymPy + Wolfram + MC only — one methodological lineage | **Single-source** |
| **MAR `(A)+(C)`** design-imbalance | bivariate-monotone closed form independently re-derived in Wolfram (`d2ba31c`); general monotone `≈−0.22` analytic; **non-monotone `b_Σ` derived via Cox–Snell at general `p` incl. 4-variate phase-8 (k=14), 2026-06-02** — assembles to leading-order `(A)+(C)_∞≈−0.22` (= monotone); empirical `−0.46` is a higher-order (realized-information) gap, not a `b_Σ` shortfall | **Medium** (triangulated; finite-n gap open) |
| **Proper-MI** extension (R4–R7) | claimed; witnesses are FIML/EM; posterior-draw layer (Wang–Robins, Nielsen) not yet verified | **Thin** |
| Foundations **L1, L3, L4** | cited classical asymptotics; only validated end-to-end by MC | **Cited, not re-derived** |

The external convergence (Shimodaira–Maeda) corroborates the **penalty value only** — *not* the
novel decomposition, the MAR term, or the proper-MI generality. Those rest on our own internal
verification. The single most framing-dependent, conceptually subtle claim is the **`−½tr(RIV)`
term — "MI's estimand is `θ̂_com`, not `θ̂_obs`."** A CAS cannot validate that premise (it is a
modeling assumption, not an algebra step); it is exactly where shared model priors could hide an
error, and exactly what an independent re-derivation must stress.

## 2. Scope

- **In scope:** the headline theorem `E[T] = E[Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com)] = +½tr(RIV) + (A)+(C) + O(n⁻¹)`
  and its two pieces `E[A]`, `E[B]`.
- **Out of scope (already witnessed):** the applications W2 (LRT power) and W3 (model selection),
  and the comprehensive sweep.

## 3. Independence axes (design principle)

Independence is not one thing. Each correlated-error mode has a different, differently-priced
decorrelator:

| Failure mode | Decorrelator | Cost |
|---|---|---|
| **Anchoring** (checker re-confirms our framing) | information isolation (re-derive from a neutral brief, never see our answer) | free, Claude |
| **Framing-induced** (the A/B split biases the result) | method diversity (derive by a different route) | free, Claude |
| **Algebra/arithmetic slips** | CAS oracle (SymPy + Wolfram — symbolic, model-independent) | free |
| **Shared conceptual priors** about MI theory | different model family (o-series / GPT) | API $$ |

**Principle.** Extract ~80% of the adversarial value in the free layers (0–2) *before* spending on
the cross-model layer, and aim that spend at the **premises** (the `−½` estimand, congeniality),
not the algebra (the CAS already owns that — re-grinding traces on a paid model is wasted money).

## 4. The layers

### Layer 0 — Information-isolated Claude re-derivation  [free]

- **Input:** the Neutral Problem Brief (NPB, §7) — the setup with **no answer leaked**.
- **Run:** N ≥ 3 independent agents, blind to the manuscript and to each other, each derives
  `E[Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com)]` to leading order. Naturally a `Workflow` fan-out (needs opt-in).
- **PASS:** a majority converge on `+½tr(RIV)` with the `+tr / −½tr` structure and a MAR
  design-imbalance term.
- **DIVERGE:** localize the first step where an agent departs — that step is the soft spot →
  investigate (it is a *finding*, not a failure).

### Layer 1 — Method-diverse re-derivation  [free]

Force distinct routes and check they land in the same place:

- **R1** pivot on `θ̂_obs` (the manuscript's A/B split).
- **R2** pivot on `θ̂_com`.
- **R3** direct second-order `E[ℓ]` expansion, *no* A/B split.
- **R4** (optional) cumulant/MGF route, or the Cavanaugh–Shumway complete-data-discrepancy route
  specialized to congenial MI.

- **PASS:** all routes give `+½tr(RIV)` (`+ (A)+(C)`). Cross-route agreement = framing-independence.
- This route-set most directly stress-tests the `−½` term — each route treats the estimand
  differently, so a spurious `−½` would not survive all of them.

### Layer 2 — CAS ground-truth  [partly done]

- **DONE:** SymPy (Appendix B, in-doc) + Wolfram companion (`verification/cas-wolfram/verify_traces.py`,
  commit `3977bdd`) — the trace algebra and the MVN Magnus duplication-matrix inversion, two
  independent CAS implementations.
- **TODO-A [DONE, `d2ba31c`]:** independent Wolfram re-derivation of the **bivariate `(A)+(C)`** —
  `verification/cas-wolfram/verify_term_ac.py`.
- **TODO-B [DONE, general-`p`, 2026-06-02]:** the **non-monotone `b_Σ`** via Cox–Snell — derived and
  verified by two CAS (bivariate, `~1e-9`), exact monotone reduction, direct MC, and the score/Bartlett
  identities (todo/014), then **generalized to arbitrary `p`** (`verify_term_ac_nonmonotone_genp.py`):
  p=2 reduction to the committed bivariate value `1.5e-13`; machine-precision score/info identities and
  exact structural checks (always-observed block → complete-data `−σ`; monotone reduction → `−σ_pp`) at
  p=3,4; GH-converged. At the 4-variate phase-8 ampute design (k=14) it assembles to the **leading-order
  `(A)+(C)_∞≈−0.22`** — the *same* constant as monotone — confirmed two ways (analytic α/H_φ and
  finite-differencing `barQ`; `verify_term_ac_nonmonotone_4v.R`), MCAR control → 0.
  *Finding (todo/015):* `b_Σ` is NOT the missing piece for the empirical `−0.46`. The phase-8 remainder
  (`−0.34→−0.46`, still increasing) lies *beyond* the leading-order constant via a higher-order
  (finite-n / realized-information) gap — also present in the monotone (`−0.22` vs `−0.27`) and bivariate
  (`−0.10` vs `−0.07`) cases. Reconciling it is open higher-order theory, not a mechanical scale-up;
  manuscript reframed accordingly.
- **PASS:** symbolic reduction to 0; any nonzero residual is a real finding.

### Layer 3 — Cross-model adversarial  [API budget; scoped tight]

Run **only after 0–2**, on a different model family (o-series / GPT), in two modes:

- **Mode A (blind):** hand it the NPB; does an independent model land on `½tr(RIV)` by its own route?
- **Mode B (red-team):** hand it our derivation + the lemma excerpts; ask it to *find the error*,
  and **specifically challenge the `−½` "estimand is `θ̂_com`" premise and the congeniality setup**.

- **Deliverable prepared in advance:** a self-contained package — NPB + lemma sheet (assembled from
  `literature/*.md`) + red-team prompt — that pastes straight into an API call. **No agentic repo
  access, no litrev pipeline, no provenance rig needed** — the task is self-contained math plus a
  handful of source excerpts we already have.
- **Surgical target:** the conceptual premises, where a CAS is silent and shared Claude/GPT priors
  are the only residual risk.
- **PASS:** the independent model agrees, or its disagreement is run to ground.

## 5. Decision gates

| Layer | PASS signal | DIVERGE signal | Action on divergence |
|---|---|---|---|
| 0 | majority land on `½tr(RIV)` + split | an agent gets a different total/structure | bisect to the first departing step; check it against the lemma it uses |
| 1 | all routes agree | a route disagrees on `−½` or the `(A)+(C)` sign | the disagreeing route exposes a framing assumption — reconcile or correct |
| 2 | symbolic `0` | nonzero residual | a genuine algebra error — fix the manuscript step |
| 3A/3B | independent model agrees / finds nothing | model derives a different answer or refutes the `−½` premise | highest-value finding — escalate; this is the conceptual check the others can't do |

**A divergence is the point, not a failure.** Each one localizes a soft spot; convergence across
independent axes is what upgrades the novel decomposition from single-source to triangulated.

## 6. Sequencing, cost, deliverables

- **Order:** Layers 0 → 1 → 2 (free, ~80% of the value) → Layer 3 (bounded API spend: two scoped
  prompts, a few dollars — not an agentic rig).
- **Deliverables:**
  1. the NPB + answer key (§7, §8 — answer key kept separate, never handed out);
  2. a per-layer results log;
  3. an updated evidence-status note (IDEAS.md / the verification summary);
  4. the Layer-3 cross-model package, ready for the user's API call.

## 7. Appendix A — Neutral Problem Brief (NPB), draft

> **Hand this out verbatim. Do not append the answer key (§8).**
>
> **Setup.** Let `p(x; θ)`, `θ ∈ Θ ⊆ ℝ^k`, be a regular parametric model (smooth, identifiable,
> differentiation under the integral valid, nonsingular Fisher information). When a concrete family
> is wanted, take the multivariate normal `N(μ, Σ)` with `θ = (μ, vech Σ)`. We observe `n` i.i.d.
> units; on each unit some coordinates are **missing at random** under an ignorable mechanism
> (missingness depends only on observed coordinates; its parameter is distinct from `θ`). Partition
> each unit into observed / missing parts.
>
> **Likelihoods and informations.** `ℓ_com(θ; Y)` is the complete-data log-likelihood (as if nothing
> were missing), with MLE `θ̂_com`; `ℓ_obs(θ; Y_obs)` is the observed-data log-likelihood, with MLE
> `θ̂_obs`. Write `I_com`, `I_obs` for the complete- and observed-data expected information, set the
> missing information `I_{mis|obs} := I_com − I_obs`, and define
> `RIV := tr(I_obs⁻¹ I_{mis|obs})`.
>
> **Multiple imputation.** Completions are drawn from a **congenial, proper** imputation model
> (Rubin properness; the imputer's model and the analyst's complete-data procedure are compatible in
> Meng's sense). In the infinite-imputation limit define the averaged complete-data log-likelihood
> at a point `θ`:
> `Q̄_∞(θ) := lim_{m→∞} (1/m) Σ_l ℓ_com(θ; Y_obs, Ỹ_mis^{(l)}) = E[ ℓ_com(θ; Y) | Y_obs ]`,
> the expectation taken over the imputation posterior.
>
> **Question.** Compute, **to leading order in `n`**, the expected discrepancy
> `E[ T ] = E[ Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com; Y) ]`.
> Express the answer in terms of `RIV` and any **design-dependent** quantities you encounter. Show
> the derivation and name the standard asymptotic results you rely on (MLE expansions, score/
> missing-information identities, MI variance facts). State separately how the answer changes, if at
> all, between MCAR and MAR.

**Withheld from the brief (the leak list — keep OUT):** the value `½tr(RIV)`; the
`+tr(RIV) / −½tr(RIV)` split and the words "imputation bias" / "estimation mismatch"; the claim
that MI's estimand is `θ̂_com`; the `(A)+(C)` design-imbalance term and its closed form. The brief
must let the solver *discover* these, not recognize them.

## 8. Appendix B — Answer key (grading only; never handed out)

A correct independent derivation should land on:

- **Net:** `E[T] = +½tr(RIV) + (A)+(C) + O(n⁻¹)` (deviance scale ×2).
- **Imputation piece:** `E[Q̄_∞(θ̂_obs) − ℓ_com(θ̂_obs)] = +tr(RIV) + (A)+(C) + O(n⁻¹)`.
- **Estimation piece:** `E[ℓ_com(θ̂_obs) − ℓ_com(θ̂_com)] = −½tr(RIV) + O(n⁻¹)`, the `−½` arising
  because MI's target is the complete-data maximizer `θ̂_com` while `Q̄_∞` is centered at `θ̂_obs`.
- **`(A)+(C)`:** `O(n⁻¹)` (vanishing) under MCAR; a nonzero `O(1)` design-imbalance under MAR;
  bivariate-monotone closed form `(n_mis/n_obs)[1 − ½tr(Q_mis Q_obs⁻¹)]`; general monotone `≈ −0.22`.

**Convergent signals (corroboration):** the `½` coefficient; the two opposite-sign pieces; a
MAR-only extra term that vanishes under MCAR. **Divergence triggers (investigate):** a different
coefficient (e.g. `tr(RIV)` or `−½k`); no MAR term; or a principled objection to the `θ̂_com`-target
argument behind the `−½`.

## 9. Risks / honest caveats

- **Shared training priors** can survive information isolation *and* method diversity *and* the CAS —
  only the cross-model layer catches those, and only on the conceptual layer. That is why Layer 3
  exists and is aimed at the premises.
- **TODO-A** (independent `(A)+(C)`) depends on reconstructing **MI-IC v4 Steps 6-7** from the
  companion repo; budget for that.
- **The NPB must not leak.** Any phrase that telegraphs `½tr(RIV)` or the A/B split silently
  invalidates the independence of Layers 0 and 3. Review the brief against the leak list (§7) before
  every hand-out; keep §8 in a separate file when packaging Layer 3.

---

*Draft 2026-06-01. Next step: confirm the layer ordering and the NPB wording, then run Layer 0
(free) as the first data point.*
