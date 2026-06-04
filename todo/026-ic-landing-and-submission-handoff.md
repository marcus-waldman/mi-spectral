# Todo 026 — Handoff: land the IC application, retire the SB arm, then open submission drafting

**Status:** Handoff (2026-06-04). Execute in a fresh session. Continues todo/024–025 (the W2
differential session — EXECUTED, cross-model gate cleared, commits `6217ae9`/`c08a18a`/`80d2d7e`)
under the scope split of todo/023. The W2/LRT arc is DONE; this session closes the remaining
application-layer items and opens the JAIGP submission document.

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
