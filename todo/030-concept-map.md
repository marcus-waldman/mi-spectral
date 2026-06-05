# todo/030 — Argument map of the derivation guide

**Status:** open (drafting tool). Created 2026-06-05.
**Purpose:** a node-and-edge representation of `manuscript/derivation.qmd`, built to restructure
`manuscript/mi-spectral.qmd`. The manuscript is effective when each section states its central
proposition first, presents the evidence that establishes it, and derives consequences from
evidence already presented — never the reverse order.

**Ontology** (the litrev argument-map model, `litrev_mcp/tools/argument_map.py`):

- **Proposition** — an arguable assertion, stated as a checkable sentence.
- **Evidence** — citable support: a derivation.qmd section, a verification script/cache, a
  preregistration grade, or a literature source (`[citekey]` = `literature/<citekey>.md`).
- **Topic** — a theme grouping propositions; here, the manuscript sections.
- **Edge** — a typed directed relation: `depends_on`, `supports`, `extends`, `qualifies`,
  `leads_to`, `enables`, `contradicts`.
- **Standing** — the strength class of each proposition, stated explicitly:
  **T** = proved theorem/proposition with symbolic (CAS) verification;
  **M** = Monte-Carlo-confirmed quantitative claim (preregistered where noted);
  **E** = empirical finding scoped to the designs studied, not a theorem.

---

## Topics (= mi-spectral.qmd sections)

| Topic | Manuscript section | Central proposition |
|---|---|---|
| T1 Problem and positioning | §1 Introduction | C5 |
| T2 Main theorem | §2 Setup and main theorem | C1, C2 |
| T3 Likelihood-ratio comparison | §3 Application I | C3 |
| T4 Information-criterion selection | §4 Application II | C4 |
| T5 Numerical studies | §5 | evidence layer for C1–C4 |
| T6 Discussion | §6 | gaps G1–G6 |

---

## Central propositions

**C1 — Q-function deviance bias decomposition.** *(Standing: T + M)*
Under congenial proper MI with the complete-data MLE as target, for any regular likelihood whose
conditional missing-data entropy depends on the estimated parameters (an estimated scale or
covariance; MVN with estimated Σ throughout),
E[Q̄_∞(θ̂_obs) − ℓ_com(θ̂_com)] = +tr(RIV) − ½tr(RIV) = +½tr(RIV) + O(n⁻¹),
the first term imputation bias (averaging ℓ_com over imputation-model completions), the second
estimation mismatch (MI targets θ̂_com; Q̄_∞ is centered at θ̂_obs).
Evidence: `derivation.qmd @sec-thm` (@eq-theorem), proof `@sec-termB`/`@sec-termA`/`@sec-combine`;
CAS `@sec-verify-terms` + `@lst-mc-combine`; MC `verification/rederivation-L0-fitted-vs-oracle.R`;
pooled preregistered W1: T̂ = 2.43 ± 0.26 vs augmented target 2.42–2.55
(`verification/w1-h1-pooled-reconciliation.R`). Component-level caveat: only totals and paired
contrasts are MC-tight; E[A], E[B] individually miss by 9–20% at finite n.

**C2 — MAR design-imbalance term (A)+(C).** *(Standing: T for structure/sign/order; G1 for magnitude)*
Under MAR, Term A carries an additional O(1) term
(A)+(C) = αᵀE[δ] + ½tr(𝓗 I_obs⁻¹) − tr(RIV), zero exactly when missing and observed units share a
conditioning-variable distribution (MCAR); bivariate monotone closed form
(n_mis/n_obs)[1 − ½tr(Q_mis Q_obs⁻¹)]. The information convention is the realized (observed)
information [kenwardLikelihoodBasedFrequentist1998], whose gap from the naive expected information
is the closed-form Δ_KM ≈ −0.55. Firm: sign, O(1) order, MCAR vanishing, O(1/n) higher-order
correction. Not firm: the absolute magnitude (see G1).
Evidence: `@sec-termA` lemma; `verification/term-a-mar-closedform.R` (leading order ≈ −0.22, MCAR
control ≈ 0); Cox–Snell b_Σ at general p
(`verification/cas-wolfram/verify_term_ac_nonmonotone{,_genp}.py`);
`verification/term-ac-controlvariate-pin.R`, `verification/term-ac-higherorder-paired.R`.

**C3 — LRT differential bias at the null.** *(Standing: T + M)*
At the null, E[d̂_L − d̂_com] = tr(RIV_⊥) + O(n⁻¹), where tr(RIV_⊥) is the missing information of
the q_d tested directions projected onto the null tangent space **in the I_com metric** — because
the Q-function curvature is I_com (the EM identity), not I_obs (`@eq-lrt-bias`, Proposition L1).
Evidence: three independent derivation routes with referee recomputation
(`verification/cache/w2diff-stage1-routes.json`); CAS
`verification/cas-wolfram/verify_w2_differential.py` (A1–A4); MC discrimination from the naive
formula at 52 standard errors (2.64 predicted, 8.47 naive;
`verification/w2-paired-differential-mu1-cell.R`); blind cross-model re-derivation and adversarial
pass both sustained (`verification/cache/layer3-gpt-5.5-w2diff-mode{A,B}.md`, `todo/024`).

**C4 — Model-specific IC bias and its correction.** *(Standing: T for the criterion; M for recovery)*
The bias is model-specific — RIV_k is computed on candidate k's own parameter space — so
uncorrected MI-AIC/BIC favor candidates with larger tr(RIV_k) by exactly the differential bias
−[tr(RIV_j) − tr(RIV_k)]. The corrected criterion is
AIC_MI^c(k) = −2Q̄_∞(ψ̂*_k) + 2q_k + tr(RIV_k) (`@eq-ic-corrected`), identical as a penalty to
AIC_{x;y} [shimodairaInformationCriterionModel2017].
Evidence: consequence of C1 applied per candidate (`@sec-ic-criterion`); preregistered W3 sweep
(`verification/cache/run_all-prod/phase2-w3/summary.csv`): uncorrected 0.674, corrected 0.816,
oracle 0.898 at N=500, with 100% of uncorrected misclassifications on the largest-RIV (saturated)
candidate; calibration ladder (I4) for the distribution-level extension.

**C5 — Position relative to existing work.** *(Standing: T, by comparison of stated results)*
The result corrects the *numerator* of MI test statistics; Meng–Rubin
[mengPerformingLikelihoodRatio1992b], Chan–Meng [chanMultipleImprovementsMultiple2022], and Chan
[chanGeneralFeasibleTests2022] calibrate the *reference distribution* the numerator is referred to.
The two are complementary. As a penalty the IC correction is not new — it equals AIC_{x;y}
[shimodairaInformationCriterionModel2017], which halved the 2tr(RIV) of AICcd/PDIO
[cavanaughAkaikeInformationCriterion1998a]. New here: (i) the imputation/estimation decomposition
of C1; (ii) the MAR design-imbalance term C2 (beyond Shimodaira's fixed-pattern i.i.d. setting;
named as future work in his §8); (iii) the extension from the deterministic EM Q-function to
proper MI. Hens–Aerts–Molenberghs [hensModelSelectionIncomplete2006a] reach the complete-data
target by inverse-probability reweighting and leave the imputation-based criterion open.
Evidence: `@sec-intro-lineage`; verbatim source passages in `@sec-sources`.

---

## Satellite propositions

### Premises of C1 (T2; each is a `depends_on` edge from C1)

- **S1 — RIV identification.** *(T)* RIV = I_obs⁻¹ I_mis|obs in matrix form; its trace is Rubin's
  r_∞ [rubinMultipleImputationNonresponse1987]. Evidence: `derivation.qmd` "Identification: RIV
  equals Rubin's r_∞" and the disambiguation from the EM rate / fraction of missing information.
- **S2 — One observed-data RIV.** *(T + M)* Both terms calibrate to a single RIV built on the
  unconditional observed-data information, which under MAR carries a mean–covariance cross term
  [kenwardLikelihoodBasedFrequentist1998]; the earlier two-RIV reading was an artifact of the
  naive block-diagonal information. Evidence: `@sec-two-rivs`, post-`@sec-combine` callout,
  Appendix C; `verification/lemma-revalidation.R`; `run_all.R` phase 6.
- **S3 — Fitted, not oracle.** *(T + M)* Q̄_∞ is the fitted predictive (imputation model at the
  estimated/drawn parameter). Defining the target instead as the oracle conditional expectation
  E[ℓ_com | Y_obs] at the truth reverses the sign to −½tr(RIV). Evidence: `@sec-qfun` and the
  following section; `verification/rederivation-L0-fitted-vs-oracle.R`.
- **S4 — Estimated-scale scope.** *(T + M)* With a known scale (location-only fit) the conditional
  entropy is parameter-free and the net bias collapses: E[T] = 0 under deterministic FIML,
  −½tr(RIV) under proper MI — the two arms differing by the posterior-draw imputation variance
  C_n = ½tr(RIV). Evidence: scope callout after `@sec-thm`; `verification/rederivation-knownvar.R`
  (R = 2×10⁵, all four ratios within 4% of 1).
- **S5 — Term B.** *(T)* E[B] = −½tr(RIV) by a second-order expansion about θ̂_com and the
  variance-of-the-gap lemma Var(θ̂_obs − θ̂_com) = I_obs⁻¹ − I_com⁻¹. Evidence: `@sec-termB`.
- **S6 — Term A.** *(T)* E[A] = +tr(RIV) + (A)+(C); the entropy gradient α is nonzero and
  supported on the covariance parameters only (the do-not-invoke-Gibbs warning). Evidence:
  `@sec-termA`.
- **S7 — Plug-in-entropy reading.** *(T, consistency check)* E[T] equals the conditional-entropy
  plug-in bias Δ_n via ∇²C_n(θ₀) = H_φφ + I_mis|obs; the (A)/(C)/½tr split is the same bias
  regrouped, and T is convention-free. Evidence: remark after `@sec-combine`;
  `verification/cas-wolfram/verify_term_ac{,_sympy}.py`.

### Consequences and refinements of C3 (T3)

- **L2 — The naive difference always overstates.** *(T)*
  tr(RIV_⊥) ≤ tr(RIV) − tr(RIV_0), with equality iff col(I_obs^{1/2}G) is invariant under the
  standardized missing information (includes EFMI and block-diagonal cases); the exact gap is
  tr[(I + H₁₁)⁻¹ H₁₂H₁₂ᵀ] — the missing-information coupling between tested and retained
  directions. Evidence: `@sec-lrt-naive`; Gram/Schur proof; CAS B1–B4 in
  `verify_w2_differential.py`; factor >3 in the μ₁ design, ≈5% in the W2 design.
- **L3 — Paired noise collapse.** *(T + M)* The per-dataset paired differential has sd O(1) at the
  null and under local alternatives — the O_p(√n) terms are identical realizations in both levels
  (same imputations, same realized constants) and cancel dataset by dataset — reverting to O(√n)
  at fixed alternatives. Evidence: `@sec-lrt-pairing`; sd(D) = 1.58/1.47/1.57 flat vs
  sd(T) = 18.4/26.6/36.5 across N = 500/1000/2000
  (`verification/w2-paired-differential-spotcheck.R`).
- **L4 — (A)+(C) differential.** *(T + M)* The (A)+(C) contributions are properties of the
  imputation, not the fitted model: they cancel exactly at the null, are O(n⁻¹ᐟ²) under local
  alternatives, and decouple into a genuine O(1) differential only when the candidates'
  pseudo-true values are separated at O(1) — separation, not nesting, is the criterion
  [vuongLikelihoodRatioTests1989]. Measured: per-candidate level ≈ +2.5 deviance units under MAR
  (collapses under MCAR); similar-pair (CS vs AR(1)) differential below resolution; dissimilar-pair
  (diagonal vs AR(1)) differential resolved at −1.2 (−3.5 se). Evidence: `@sec-lrt-ac`; depends_on
  C2; preregistered `todo/029` + Amendment 2; `verification/w4-nonnested-vuong.R`,
  `verification/w4-dissimilar-vuong.R`; CAS `verify_w4_nonnested.py`.
- **L5 — Which procedures inherit the bias.** *(T + M)* At the null, tr(RIV_⊥) equals the mean
  inflation of a correctly calibrated reference: the limiting law is Σλ_jχ²₁ with
  Σλ_j = q_d + tr(RIV_⊥) [chanGeneralFeasibleTests2022, eq. 1.10], so a calibrated test absorbs
  the bias and additional numerator correction double-counts (W2: 0.042 uncorrected vs 0.034
  over-corrected). The bias therefore affects exactly the procedures with no reference
  distribution: information-criterion ranking, explicit numerator corrections, and non-nested
  comparison. Evidence: `@sec-lrt-consequences`; `verification/cache/W2-prod-amelia.rds`.

### Consequences and refinements of C4 (T4)

- **I4 — Calibration ladder.** *(T for the maps; M preregistered for the outcomes)* Anchoring all
  candidates at the saturated model makes every T_k a likelihood-ratio statistic with an analytic
  null law Σλ_{k,j}χ²₁ (the C3 spectrum), and three derived maps — mean shift tr(RIV_⊥,k); the
  unique affine two-moment map (a_k, b_k); equipercentile equating via Imhof/Davies — match
  successively more of the null distribution. Results (R = 2000/cell): null-side KS distance
  0.281 → 0.019, variance ratio 3.18 → 0.97; ρ = 0.40 selection 0.678 → 0.904/0.903 vs oracle
  0.899; junk cell closes 90% of the gap. Evidence: `@sec-ic-ladder`,
  `@sec-ic-ladder-results`; preregistration `todo/027` (all criteria passed);
  `verification/ic-ladder.R`; CAS `verify_ic_ladder.py` (L-A1–L-A4).
- **I5 — Noncentral shrinkage is exact and unavoidable.** *(T + M)* The two-moment and equating
  maps shrink noncentral statistics by exactly a_k and ≈ 1/λ_max respectively (measured 0.586 vs
  predicted 0.570; 0.362 vs 0.398): no transform built from observed data restores destroyed
  Fisher information; conservatism against misspecified candidates is the price of null-side
  calibration. Evidence: `@sec-ic-ladder-results`.
- **I6 — Information-loss floor.** *(E)* In the weak-signal cell (ρ = 0.10) the oracle itself is
  0.820 and no correction passes 0.650; the 0.17 residual is information loss, not calibration
  error. This is a measured floor, not a proof of impossibility (see G4). Evidence:
  `@sec-ic-ladder-results`.
- **I7 — Structural facts limiting generalization.** *(T + M)* (a) The W3/ladder candidate family
  is block-diagonal, which is exactly L2's equality condition — naive and exact traces agree to
  3.6×10⁻¹⁵ there, so the overstatement is invisible in that family and material only for
  constraints that do not block-decompose. (b) Per-model marginal transforms cannot calibrate a
  *difference* distribution — the score copula is invariant under marginal maps (measured: equated
  Δ mean 6.10 vs complete-data 10.00 in the near-tied pair). Evidence: `@sec-ic-ladder-results`
  closing remark.

---

## Edges

| From | Type | To | Content |
|---|---|---|---|
| C1 | depends_on | S1–S7 | premises and proof components |
| C2 | extends | C1 | Term A under MAR carries the additional O(1) term |
| C1 | leads_to | C3 | differential of two Q̄_∞ levels at the null |
| C1 | leads_to | C4 | per-candidate bias applied to penalized deviances |
| L2 | supports | C3 | the naive alternative errs in a known direction with an exact gap |
| L3 | enables | C3 | paired contrasts make the correction precisely estimable |
| C2 | necessitates | L4 | the non-nested O(1) differential exists because (A)+(C) does |
| L4 | qualifies | C4 | for dissimilar candidates an un-corrected O(1) differential remains |
| L5 | leads_to | C4 | the bias matters exactly where no reference distribution exists |
| C3 | enables | I4 | the analytic null spectrum supplies the ladder's three maps |
| I5 | qualifies | I4 | null-side calibration costs noncentral evidence, by a known factor |
| I6 | qualifies | C4 | no correction recovers information the data no longer carry |
| I7 | qualifies | L2, I4 | equality case hides the overstatement; marginal maps cannot fix differences |
| C5 | qualifies | C1, C4 | scopes the novelty claim; penalty itself is Shimodaira's |
| I4 | extends | C4 | the ladder extends the mean correction to the whole null distribution |

The map is a DAG under narrative normalization, and must stay one. Convention: `supports`,
`enables`, `leads_to`, `necessitates`, `precedes` point forward (source precedes target in
argument order); `depends_on`, `extends`, `qualifies` point backward (source is stated after
target). Encode each relation as exactly one edge — S3 and S4 are premises of C1 via the
`depends_on` row; their scoping content lives in their own statements, not in a second
`qualifies` edge (an earlier double encoding created 2-cycles, removed 2026-06-05).
Synchronized with the litrev argument-map DB (project MI-SPECTRAL); render the layered view
with `visualize_argument_map(layout="dag")`.

---

## Gaps (qualified or absent evidence — candidate Discussion content, T6)

- **G1.** The absolute magnitude of (A)+(C) is not independently pinned: the O(1/n)
  higher-order result is conditional on the −0.22 analytic anchor, and direct MC is heavy-tailed
  and untrended (−0.34/−0.46/−0.29/+0.17). Firm: sign, order, MCAR vanishing, and that comparisons
  use only the better-conditioned paired differential.
- **G2.** Propositions L1–L4 are proved and MC-confirmed for the deterministic-FIML Q̄_∞; the
  proper-MI carry-over is argued structurally (shared posterior, shared draws) but not separately
  measured.
- **G3.** Imputation-engine robustness (EMB vs exact data augmentation) is empirical and scoped to
  the designs studied; DA was not run. Sample RIV matches observed-data RIV within 2–3%; W3
  selection within 0.011.
- **G4.** The weak-signal floor (I6) is a measured residual, not a proof that no estimator built
  from the same observed data could do better.
- **G5.** For dissimilar candidate pairs, a mechanism-independent misspecification O(1) coexists
  with the design-imbalance O(1) and can partially offset it in the net ranking bias; the MCAR
  contrast separates them in measurement but the manuscript must not claim the design-imbalance
  term dominates every pair.
- **G6.** All instantiation is MVN; the theorem is stated for general regular likelihoods with
  estimated scale but verified only in the MVN family.

---

## Intended use

1. **Drafting order for mi-spectral.qmd §3–§6:** each section opens by stating its central
   proposition (C3 for §3, C4 for §4) with standing and the single strongest piece of evidence;
   satellites enter only where an edge requires them; gaps go to §6, not to footnotes scattered
   through the applications.
2. **Diff check:** any manuscript sentence asserting a relationship not present as an edge here is
   either (a) a missing edge to add with evidence, or (b) an unsupported claim to delete.
3. **Trust ordering:** within each section, present standing-T material before standing-M, and
   standing-M before standing-E; never let a standing-E finding carry a standing-T tone.
