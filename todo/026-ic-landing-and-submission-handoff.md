# Todo 026 — Handoff: land the IC application + calibration ladder, then open submission drafting

**Status:** Handoff, **REVISION 2** (2026-06-04, same day — user scope decision). Execute in a
fresh session. Continues todo/024–025 (the W2 differential session — EXECUTED, cross-model gate
cleared, commits `6217ae9`/`c08a18a`/`80d2d7e`).

---

## REVISION 2 (2026-06-04) — the calibration ladder moves IN-PAPER. Supersedes items below.

**User decision** (recovering the 2026-06-03 design discussion, session `ea505749…`, extract at
`verification/cache/_equating_extract.txt`): the paper's IC application must **contrast first-,
second-, and all-moment matching** — mean `tr(RIV)` correction vs SB two-moment vs equipercentile
equating — so that the distribution of pairwise ΔAIC/ΔBIC matches the complete-data law as far as
is achievable. This un-parks ladder rungs 1–3 from todo/023 (which now keeps only the
de-shrinkage map, the full pairwise-matrix-with-Z testbed, and copula/triangle-closure at scale).

**Supersessions of the items below:**
- **Work Item 1 (the IC section)** becomes *IC application + calibration ladder*: the planned
  @sec-ic content PLUS the three-rung contrast with the preregistered null/noncentral split.
- **The SB arm FLIPS from "retire" to "fix as rung 2"** — you cannot contrast two-moment
  matching without a working two-moment arm. Issue #1 stays OPEN until the ladder arm lands,
  then closes as "superseded by the ladder rung 2 (new script); original preregistered arm
  documented as buggy, frozen, not re-run."
- **The §5 SB wording caution** (rev. 1, below) is superseded in part: the two-moment rung IS
  now derived/used in-paper — @sec-lrt makes the coefficients derivable (two-moment matching of
  the weighted-χ² `Σ(1+r_⊥,j)χ²₁` to `χ²_q`), and the rung must use the CORRECT I_com-metric
  complement trace (Proposition L2), reporting the naive trace for comparison. What survives of
  the caution: never present the ladder as fully restoring complete-data selection — the
  noncentral side is impossible in principle.

**The ladder, precisely (from the recovered discussion + todo/023, now with the @sec-lrt asset):**
- Working statistic: saturated-anchored `T_k = D(M_k) − D(M_sat)` (the anchor is the congenial
  imputation model ⇒ the heavy realized (A)+(C) cancels — Proposition L3's mechanism for free;
  rankings invariant; every T_k is a null-referenceable LRT statistic; W3's candidates form a
  nested chain so pairs telescope).
- Rung 1 (mean): `−tr(RIV_⊥,k)` — the I_com-metric complement trace per candidate (@eq-lrt-bias),
  NOT the naive difference; linear ⇒ coherent across all pairs.
- Rung 2 (SB two-moment): `a·(T_k − tr(RIV_⊥,k)) + b` with a, b derived by matching mean AND
  variance of the analytic weighted-χ² null law to `χ²_{q_k}` — coefficients now DERIVED, not
  borrowed (cite Satorra–Bentler/Asparouhov–Muthén as provenance of the form; both held).
- Rung 3 (equipercentile): `T_eq = F_com⁻¹(F_MI(T_k))` per model under ITS OWN null —
  **closed-form for nested pairs** via the analytic weighted-χ² CDF (Davies/Imhof — both held),
  falling back to Chan-style MC where needed.
- **Preregistered predictions (write BEFORE running):** each rung closes more of the
  null-side/overfit calibration gap (equating exact there, all moments); on the noncentral/
  underfit side equating is first-moment-only and CONSERVATIVE (shrunken gaps — the toy: equated
  mean 11 vs complete-data 21); the corrected-vs-oracle residual decomposes into fixable
  calibration error vs the irreducible information-loss floor; stress cell = weak true
  coefficient (near-tied pairs) shows the underfit-retention cost; junk-heavy cell shows the
  calibration win. LIGHT indirect-pair diagnostic only (one near-tied B-vs-C cell measuring
  s_B − s_C against complete-data ΔAIC(B,C)); the instrumented testbed stays sequel.
- **Honest-claim fence:** all-moment matching is claimed ONLY per pair under that pair's null;
  noncentral pairs are first-moment-corrected, full matching impossible in principle
  (information loss is not equatable — no monotone transform restores destroyed Fisher
  information); per-model marginal equating cannot calibrate difference distributions in
  general (copula invariance) — state, don't hide.
- **New analytic claims trigger the protocol:** the derived SB a/b and the analytic equating map
  are new claims ⇒ CAS check + (if formalized beyond two lines) the GPT-5.5 gate, per the
  standing directive. Empirically running the ladder does not.
- **Sequencing within the session:** (1) preregister the ladder arm (new todo/027 or todo/004
  Amendment 3 — predictions + pass criteria BEFORE code); (2) build the NEW ladder script
  (frozen originals untouched); (3) run at moderate scale (few cores); (4) land the combined
  @sec-ic; (5) mi-spectral.qmd opening becomes the stretch goal / next session.
- **Pre-session user action:** acquire **Kolen & Brennan (2014)** via the litrev pipeline
  (todo/003, promoted High) — the equating rung needs its canonical citation; Holland–Thayer /
  von Davier et al. optional.

---

*(Revision 1 below — items superseded as noted above; everything else stands.)*

## 0. Scope frame (carried, do not re-litigate)

- **This paper = bias correction + LRT (W1/W2) + IC-as-application with honest wording.** The W3
  distributional-calibration ladder is the sequel (`todo/023`) — at most a future-work pointer.
- Target documents: `manuscript/derivation.qmd` (canonical theory+applications doc, audited) and —
  NEW this session — `manuscript/mi-spectral.qmd` (the JAIGP submission), which may now be
  CREATED: the gate ("submission drafting comes after derivation.qmd is done") is satisfied once
  item 1 below lands.
- Audit baseline is now **0 BLOCKER / 0 WARN** (engine brace-glob fix, `80d2d7e`): any new WARN in
  /derivation-audit is a REAL signal — the old "3 known false positives" disclaimer is retired.

## 1. LOCKED — do NOT re-open

- Everything in todo/025 §1 (headline, split, +tr(RIV) correction = AIC_{x;y}, fitted-predictive,
  estimated-scale fence, (A)+(C) structure/convention/Δ_KM/value-not-pinned).
- NEW since: the entire `@sec-lrt` result set (Propositions L1–L4) — derived 3 ways + refereed,
  CAS (`cas-wolfram/verify_w2_differential.py`), MC-discriminated at 52 se
  (`w2-paired-differential-mu1-cell.R`), cross-model audited both modes
  (`cache/layer3-gpt-5.5-w2diff-mode{A,B}.md`, grading record in todo/024), independently
  re-audited end-to-end (clean PASS). Cite/restate, don't re-derive.
- H1 disposition: todo/004 **Amendment 2** (pooled 2.434±0.258 on the (A+C)-augmented mean;
  per-cell FAIL = criterion artifact). Don't re-run W1 brute-force.

## 2. WORK ITEM 1 — land the IC application section in derivation.qmd

The paper's two applications are LRT (now @sec-lrt) and IC (currently only the intro bullet +
lineage). Mirror @sec-lrt with a compact `@sec-ic` AFTER it (recommended; if on reflection the IC
content reads better deferred wholly to mi-spectral.qmd, record the decision in this file and
skip — but the default is to land it):

- **Content:** (i) the corrected criterion `-2Q̄_∞ + 2q + 2tr(RIV)` coincides with Shimodaira's
  AIC_{x;y} — the decomposition (+tr / −½tr), the MAR (A)+(C) term, and the proper-MI extension
  are what's new (this is already stated in @sec-intro-lineage; the section makes it formal);
  (ii) why uncorrected MI-AIC favors larger-RIV candidates (the model-specific −tr(RIV) bias);
  (iii) the W3 evidence with HONEST wording: corrected selection **substantially recovers**
  (π≈0.81 vs oracle ≈0.90, uncorrected ≈0.65; `cache/run_all-prod/phase2-w3/summary.csv`),
  100% of uncorrected misclassifications land on the largest-RIV candidate (W3-C = 1.0);
  do NOT write "restores complete-data-equivalent selection" unqualified (todo/022 item D);
  (iv) the cross-model-comparison caveat from the NEW L4 result: across non-nested candidates the
  (A)+(C) differential is a genuine O(1) and the paired noise is O(√n) — the IC ranking regime is
  exactly where the differential bias bites un-absorbed (ties @sec-lrt-consequences to the IC
  story); (v) one future-work sentence → sequel (todo/023), no more.
- **Citations (all held; in-session read + claim check before @cite):**
  `shimodairaInformationCriterionModel2017` (AIC_{x;y}; §8 future-work passage already quoted in
  intro), `shimodairahidetoshiImprovingPredictiveInference2000`,
  `cavanaughAkaikeInformationCriterion1998a` (AICcd 2tr penalty),
  `claeskensconsentinoVariableSelectionIncomplete2008`, `hensModelSelectionIncomplete2006a`,
  optionally `konishiGeneralisedInformationCriteria1996`, `burnhamModelSelectionMultimodel2010`.
  Several already have Appendix-A entries — extend only where a NEW claim needs a new passage.
- **Numbers:** every number from a committed cache with a pointer (phase2-w3 summary, todo/004
  W3 tables). No new simulation needed.
- Gate: render exit-0 + /derivation-audit **0 BLOCKER / 0 WARN** (new baseline).

## 3. WORK ITEM 2 — small closures (no gates, ~minutes each)

- **Retire the W3 SB arm (issue #1).** Per the scope split: retire, don't fix. Close
  github.com/marcus-waldman/mi-spectral/issues/1 with the rationale (a fixed SB arm is the
  sequel's rung 2; headline unaffected; arm documented as retired), add a retirement comment at
  the SB block in `verification/_modules/w3-sweep.R` + `verification/W3-model-selection.R`
  (comment only — do NOT touch the preregistered logic), and fix the STALE todo/000 Open-issues
  line (it references `manuscript/mi-spectral.qmd §6`, which doesn't exist yet).
- **todo/022 item B (component-level finite-n).** One honest remark where the roadmap caveat
  already lives (or @sec-thm empirics): individual components E[A], E[B] miss MC targets by
  ~9–20% at finite n (B overshoots by −0.3..−0.55 with tight MCSE — see
  `w1-h1-pooled-reconciliation.R` part (4) and todo/004's 2026-05-22 W1 note); only the total T
  and paired contrasts are MC-tight. No new runs.
- **Stage 3 disposition (todo/024).** Default: record SKIP — the spot check + 52-se
  discriminating cell already measure the differential; more scale adds nothing the manuscript
  needs. (If the user wants an n-range plot for the submission, that's a small few-core run —
  ask only if it comes up.)
- **OPTIONAL polish:** add Mode B's exact-gap closed form as a remark in @sec-lrt-naive —
  `naive − exact = tr((I+H₁₁)⁻¹H₁₂H₁₂ᵀ)`, H = I_obs^{-1/2}I_mis I_obs^{-1/2} blocked on
  col(I_obs^{1/2}G) — and extend `verify_w2_differential.py` with that identity (A5). Cheap,
  sharpens Proposition L2; skip if time is tight.

## 4. WORK ITEM 3 — open `manuscript/mi-spectral.qmd` (the JAIGP submission)

Create the stub + first full skeleton (drafting continues over subsequent sessions):

- **Structure sketch:** §1 intro (problem, result, why it matters — adapt derivation.qmd intro,
  outside-reader prose per the standing memory: no "ledger/witness/tagged/machine-checked/
  Stage N/consume"); §2 setup + main theorem (STATE, cite derivation.qmd as the companion
  sourced derivation — JAIGP provenance norms); §3 the LRT application (from @sec-lrt);
  §4 the IC application (from @sec-ic); §5 numerical studies (W1 with the Amendment-2-honest
  framing, W2, W3-with-honest-wording); §6 discussion (scope fence, proper-MI/engine scoping,
  Le Cam-style power-dominance as a CONJECTURE only, sequel pointer to the calibration program).
- **§5 Satorra–Bentler wording caution (decided 2026-06-04):** the SB-type scaled-shift (W2 arm
  C5; the retired W3 SB arm) and equipercentile equating were NEVER analytically justified
  anywhere in this paper — both are sequel rungs (todo/023). Present C5 strictly as an
  *empirical two-moment-matching comparison arm* (cite Asparouhov–Muthén / Satorra–Bentler from
  the held corpus if named), never as a derived correction. If a sentence of theory is wanted,
  the most that may be said is what @sec-lrt already implies: at H0 the limit law is
  $\sum\lambda_j\chi^2_1$ with the I_com-metric complement spectrum, so a two-moment correction
  is *derivable* — and note honestly that the committed C5 coefficients used the naive
  $\mathrm{tr}$ difference as their $tr_\perp$ input, which Proposition L2 shows overstates
  $\mathrm{tr(RIV_\perp)}$ (immaterial in the near-aligned W2 design, real in general). Do NOT
  derive the SB coefficients in this paper — that is deliberate sequel scope.
- **Authorship/provenance:** AI-assisted derivation, ORCID-verified human prompter
  marcus.waldman, transparent per JAIGP norms; the derivation.qmd + verification/ +
  literature/ stack IS the provenance appendix.
- Citation discipline applies in full (the hook guards manuscript/*; every @cite needs an
  in-session-read literature/<key>.md).
- /derivation-audit accepts any manuscript/*.qmd target — run it on mi-spectral.qmd too before
  committing (expect INFO-level findings while it's a skeleton; 0 BLOCKER still required).

## 5. Guardrails (carried)

- Few-core R (segfaults under contention); lavaan FIML / da.norm for non-monotone.
- Preregistered originals (W1/W2/W3 .R) frozen — comments only, amendments via todo/004.
- Citation hook + @TODO:<slug> drafting bypass; reference proposals → todo/003 same-response.
- R style per ~/.claude/CLAUDE.md if computation is added.
- Touch manuscript ⇒ render exit-0 + /derivation-audit 0 BLOCKER / 0 WARN (new baseline).

## 6. FINISH line

- @sec-ic landed (or the skip-decision recorded here with rationale); render + audit clean.
- Issue #1 closed as retired; todo/000 Open-issues line fixed; item-B remark landed; Stage-3
  disposition recorded in todo/024.
- mi-spectral.qmd exists with the full skeleton and at least §1–§2 in submission-quality prose.
- Commit(s) on main with the Co-Authored-By trailer; todo/000 + memory updated
  (IC landing; submission opened; SB retired).

*Handoff 2026-06-04. The theory and both application derivations are done and audited; this
session converts them into the submission.*
