# Todo 009 — Next-session resume (handoff 2026-06-01)

Session 2026-05-31/06-01 did a deep rigor pass on the deviance-bias result. Two big outcomes:
(1) the **one-RIV resolution** (fully implemented + committed), and (2) a **new finding** that
**Term A does not cancel under MAR**, which turns out to be **largely precedented by Shimodaira &
Maeda (2017)**. The contribution claim for *both* mi-spectral and MI-IC is now under review,
gated on a careful read of that paper. Full record in `todo/008`; references in `todo/003`.

---

## UPDATE 2026-06-01 (this session) — positioning settled, plan approved, Phase 1 done

Read Shimodaira–Maeda (2017) + Shimodaira (2000) in full. **Verdict:** the net `tr(RIV)` IC penalty is
**precedented** (= their `AIC_{x;y}`; cite, don't claim). **Novel slices:** (1) the Term-A MAR `(A)+(C)`
design-imbalance correction; (2) the congenial **proper-MI** generalization (posterior draws / finite M /
impute-once-select-many — beyond their EM Q-function); (3) the LRT/Chan application. Approved 5-phase plan
(`~/.claude/plans/jaunty-squishing-breeze.md`): de-risk → truth-repair derivation → derive new content →
reproducible verification → manuscript + MI-IC coordination.

**Phase 1 novelty gate — DONE → Branch A.** Re-read Cavanaugh–Shumway (1998) + Claeskens–Consentino (2008):
**neither carries `(A)+(C)`** (C-S: assumes it away + MCAR sims, penalty `2tr(RIV)`; C-C: targets the
adjusted-likelihood KL, penalty `tr(JI⁻¹)`→`p`, clean O(1/n)). Full verdict table in `todo/003`
(Phase-1 verdict section). **Gate CLOSED 2026-06-01:** Hens–Aerts–Molenberghs (2006) acquired
(migrate→index→lit-sync→read in full; `hensModelSelectionIncomplete2006a`) → **does NOT carry `(A)+(C)`**
(complete-case IPW route, penalty `2K`; its imputation-based variant uses the naive `2K` = the uncorrected
MI-AIC). **Branch A confirmed; `(A)+(C)` novel** vs all five predecessors. MI-IC already uses 1×`tr(RIV)`
(no penalty bug; citation/coordination only).

**Phase 2 DONE** (derivation.qmd truth-repair: theorem now `½tr(RIV)+[(A)+(C)]`, MCAR-exact/MAR-O(1); S-M
2017 cited; rendered clean, Appendix-B asserts pass). Wang–Robins(1998)+Nielsen(2003) synced/citeable
(`wangLargesampleTheoryParametric1998`, `nielsenProperImproperMultiple2003`) — read when starting Phase 3b.
**Next: Phase 4 (reproducible phase-8 module) and/or Phase 3 (general-MVN `(A)+(C)` + proper-MI term).**

---

## STATE — what is DONE and committed

**One-RIV resolution (settled, implemented, committed).**
- The W1 "two-RIV" split (A→expected, B→sample) was an **artifact** of grading against
  `fisher_info_obs_mvn`, which is **block-diagonal = as-if-MCAR = incomplete under MAR**. Under MAR
  the observed-data information carries a mean–covariance **cross term** (selection-induced; closed
  form `E[Xₖ|R1] = (b·Σₖ₃/√(1+b²))·λ(a/√(1+b²))`). This is **Kenward & Molenberghs (1998) §3.2**
  (acquired, verified, cited; `literature/kenwardLikelihoodBasedFrequentist1998.md`).
- There is **ONE RIV** — the observed-data RIV `tr(I_obs⁻¹ I_mis)` with `I_obs = observed_info_obs_mvn`
  (= `tr_riv_observed_general`). Both A and B calibrate to it (lemma revalidation: L1/L2/L3 hold vs
  the observed info; `verification/lemma-revalidation.R`).
- Brought in line everywhere: `manuscript/derivation.qmd` rewritten (D6, `#sec-riv`, theorem,
  `@eq-combine`, App. C; inline App. B checks `@lst-mc-obsinfo`/`@lst-mc-crossterm`; renders clean);
  phase-6 `w1-information-diagnostic.R` + `aggregate.R` reframed and **re-run** (prod cache);
  phase-2 W3 `w3-sweep.R` IC correction **re-pointed** `AIC_corrected = -2 barL + 2q + trRIV_obs`
  (was naive `trRIV`), `termspec` arm removed, **re-run** (verdicts unchanged: H1 FAIL, H2_MAR PASS,
  H3 PASS; per-cell `pi_corrected` shift mean +0.005, max 0.013 — "wash for selection" confirmed).
- Item 1 (audit): B-remainder `E[B]+½tr(RIV_obs)` decays at `b≈−1.34` (O(1/n) or better);
  `verification/remainder-rate.R`. B-part of the theorem is clean.

**NEW FINDING — Term A does NOT cancel under MAR (the live issue).**
- `E[A] = tr(RIV_obs) + (A)+(C)`, and **`(A)+(C) = (n_mis/n_obs)[1 − ½·tr(Q_mis Q_obs⁻¹)]`**,
  where `Q_mis`, `Q_obs` are the conditioning-variable second-moment matrices of the missing vs
  observed units. **`= 0` iff MCAR** (`Q_mis = Q_obs`); a **nonzero O(1)** under MAR.
- Confirmed: S1 (bivariate monotone, formula matched to sim across selection strength b), S2
  (4-variate ampute MAR: `E[A]−tr_obs ≈ −0.31` non_monotone, `−0.21` monotone at N=800; masked by a
  positive finite-n transient at small N → why W1/W3 sweeps read as fine). `verification/term-a-mar-diagnostic.R`.
- So **`E[T] = ½tr(RIV) + (A)+(C)`** — exact under MCAR, **O(1) Term-A correction under MAR**
  (~8% of ½tr(RIV) at N≥800). **Affects mi-spectral AND MI-IC.**
- ⚠️ **`derivation.qmd` Term-A lemma is now WRONG under MAR** (it asserts `(A)+(C)=O(1/n)` for any
  regular family — true only under MCAR). Needs correcting once positioning settles.

**Novelty / prior art.**
- Consensus search found no predecessor (saved verbatim:
  `literature/consensus-searches/AIC_bias_correction_multiple_imputation_MAR_2026-05-31.md`).
- BUT the **MI-IC litrev database has the predecessor**: **Shimodaira & Maeda (2017)**, "An
  information criterion for model selection with missing data via complete-data divergence."
  Key quote (their §6): *"the difference is `E{Q(θ₀;θ̂_y)} − E{Q(θ₀;θ₀)} = O(1)` in general without
  assuming (22), leading to the bias of AIC_cd."* `Q` = the EM/MI Q-function = **our `barQ`**. So
  they explicitly identified that the **Q-function deviance is O(1)-biased** — our Term-A finding.
  Their `AIC_{x;y}` penalty = `tr(RIV)` (half of PDIO/AICcd's `2tr(RIV)`); their strong assumption
  (22) `q̂_x = p_{z|y}(θ̂_y)q̂_y` **is FIML imputation**.
- Added **Shimodaira–Maeda 2017** (`8WVVPSBG`) and **Shimodaira 2000** covariate-shift (`3AA54IRU`)
  to the **MI-SPECTRAL Zotero collection** (merged out the `_needs-pdf` duplicates). NOT yet synced
  to `literature/`.

---

## NEXT SESSION — ordered todo

> **UPDATE 2026-06-01:** Acquisition (item 2 below) is **DONE** — both PDFs copied MI-IC→MI-SPECTRAL
> and lit-synced (no Mathpix re-pay): `literature/shimodairaInformationCriterionModel2017.md` and
> `literature/shimodairahidetoshiImprovingPredictiveInference2000.md`, both citeable. **Item 1 (the
> positioning read) is fully unblocked — start there, fresh.**

1. **[GATE — do first] Full in-session read of Shimodaira & Maeda (2017)** (+ Shimodaira 2000
   covariate-shift). Settle the three positioning questions:
   - (a) Is our net `tr(RIV)` correction *identical* to their `AIC_{x;y}`? (If so, our novelty is
     the decomposition + K&M observed-info-under-MAR + MI/posterior-draw generality, not the penalty.)
   - (b) Is the **Term-A MAR `(A)+(C)` term** *within* their framework (their setup is `x=(y,z)` iid
     — possibly fixed-pattern/MCAR-implicit) or **genuinely beyond** it (the MAR cross-unit
     `Q_mis≠Q_obs` imbalance; Shimodaira 2000 covariate-shift is where it might already live)?
   - (c) Reconcile the **MCAR puzzle**: we find `(A)+(C)=0` under MCAR; they say "O(1) in general."
     Is their `E{Q(θ₀;θ̂_y)}−E{Q(θ₀;θ₀)}` the same object as our `(A)+(C)`?
   - **This decides the contribution claim for both papers.** Hold derivation/writing until done.

2. **[Prereq for #1 — USER drives the litrev pipeline]** Before Claude can read/cite:
   - Remove the spurious `_needs-pdf` tag the merge left on `8WVVPSBG` and `3AA54IRU`.
   - Ensure the PDFs are in `~/Google Drive/Literature/MI-SPECTRAL/` (migrate), then **re-export the
     BBT** (`literature/mi-spectral-better-bibTeX.bib`).
   - Then **Claude runs `py scripts/lit_sync.py`** → writes `literature/<key>.md` (PDFs already
     Mathpix-converted/indexed, so no re-pay). Citekeys: likely `shimodairaInformation...2017`
     (note CrossRef shifted its date to 2018-04 → key may render `…2018`), `shimodaira…2000`.

3. **[USER decision] Reframe the contribution** given Shimodaira–Maeda precedence — coordinate
   across mi-spectral AND MI-IC. Likely-novel slice to defend: the **MCAR-vs-MAR characterization +
   closed-form `(A)+(C)`**, the **K&M observed-info RIV under MAR**, the **MI/posterior-draw**
   generality. Update MI-IC too (it cites only `@shimodaira1994` PDIO `2tr(RIV)`, not the 2017
   halved result).

4. **[Conditional on #1/#3] Derive a MAR correction** if the `(A)+(C)` term is worth claiming:
   general-MVN `(A)+(C)` (start with the **bivariate-monotone closed form** — tractable; owned
   literature: Little–Rubin §7.3 + Anderson 2003; Cox–Snell only if generalizing). Then add a
   "corrected" arm to `term-a-mar-diagnostic.R` showing `E[T] − [½tr(RIV)+(A)+(C)] → 0` under MAR.

5. **[Cleanup]** Correct the `derivation.qmd` Term-A lemma (it's wrong under MAR) per whatever #1
   settles. Also re-read the OWNED `cavanaughAkaikeInformationCriterion1998a` + `claeskensconsentino…2008`
   for whether they carry the design term / are MCAR-implicit (todo/003 logs this). Optionally queue
   Shimodaira 1994 PDIO (`W5A626VT`/`EDJGHKXF`) and Imori–Shimodaira 2019 (`3QVGA2JH`, in db).

6. **[Deferred] Manuscript rebuild** — `manuscript/mi-spectral.qmd` was deleted this session
   (recover snapshot: `git show 4da1e0c:manuscript/mi-spectral.qmd`). User will supply an outline;
   the rebuild must now account for the Shimodaira positioning. Also the open W3 SB-arm bug
   (`todo/000`, issue #1) is auxiliary and unaffected.

---

## Key files / pointers (don't re-derive)
- Record of the whole investigation: **`todo/008-information-diagnostic.md`** (read this first).
- References + novelty log: **`todo/003-references-to-acquire.md`** (K&M verified; Shimodaira–Maeda
  2017 / Shimodaira 2000 / Hens–Aerts 2006 proposed; Cox–Snell conditional).
- Reproducible diagnostics: `verification/{lemma-revalidation.R, remainder-rate.R, term-a-mar-diagnostic.R}`
  (standalone, `Rscript … [R] [n_cores]`). Run on the 20-core PSOCK default.
- `manuscript/derivation.qmd` renders clean; App. B executes the cross-term checks inline.
- litrev RAG reads are allowed inline (`mcp__litrev__search_papers`/`ask_papers`); convert/index +
  migrate + BBT export are USER-driven.
