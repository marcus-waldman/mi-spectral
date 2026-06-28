# todo/039 — Citation audit: is every citation valid and appropriate as used? (HANDOFF, next session)

**Status:** OPEN, not started. Designed 2026-06-28 (the session that executed todo/038
stage 1a). Branch `contributions-delphi-todo035`, **pushed** to
`origin/contributions-delphi-todo035`. The manuscript prose is post-1a: the 20
text-validity wording/citation amendments are committed at `57df922` (determination
AMENDED, no result retracted). check_plan green; APA preview renders clean (85 ¶ / 7
sections).

**Intent (Marcus):** audit **every citation in the manuscript text** and confirm each is
(a) **valid** — the citekey resolves to the correct real work — and (b) **appropriate for
how it is used** — the cited source actually supports the specific claim it is attached to,
at the strength and scope claimed, with the right work for that point. Flag
misattribution, overstatement (the source is weaker/narrower than the claim), wrong-work
(a different reference is the correct one), or unsupported-as-cited. This is the
**citation-support (1b)** lens that was deferred from todo/038.

**This is the repo-grounded "other way" — NOT a delphi.** In todo/038 we started 1b as a
cross-family delphi and **killed it**: it leaned on the panel's *fallible training memory*
to FIND citation problems, and that is exactly what hung GPT-5.5 (reasoning over ~27
citations from memory). We hold **local verbatim copies of every cited PDF**
(`literature/<citekey>.md`, the Mathpix conversions we read in-session). So the audit runs
**ground-truth-first**: the check IS the verbatim comparison of source against claim. Do
NOT run the staged 1b-cite delphi under `tkal-reviews/textvalidity-20260628T193253Z/1b-cite/`
— that approach is abandoned; the staged config is obsolete.

**Off the table:** the theorem and the simulation results (correct; S5-tribunal-defended)
and the 1a claim-support pass (done, committed `57df922`). This exercise is purely
citation↔claim fit.

---

## Scope — ALL bibliographic citations, ALL sections (including §4)

Citation-appropriateness is section-agnostic, so unlike the 1a overclaim review (which
excluded §4 Derivations), the citation audit covers the **whole manuscript**: abstract +
§1 + §1B + §2 + §3 + §4 + §5 + §6. A misattributed citation in §4 is still a defect.

~35 distinct bibliographic citekeys (the 27 in-scope from todo/038 plus the §4-only set:
`daviesAlgorithm155Distribution1980`, `imhofComputingDistributionQuadratic1961`,
`vuongLikelihoodRatioTests1989`, `satorraEnsuringPositivenessScaled2010`,
`asparouhovRobustChiSquare2006`, `kolenTestEquatingScaling2014`,
`vaartAsymptoticStatistics1998a`, `schaferAnalysisIncompleteMultivariate1997`). Each is
used at one or more attachment points; audit each *attachment*, not just each key. Audit
the CURRENT post-`57df922` text (1a added `@satorraEnsuringPositivenessScaled2010;
@asparouhovRobustChiSquare2006` to S5-P6 and rescoped the "only one IC" claim in S1-P2).

Internal cross-references (`@sec-`/`@eq-`/`@fig-`/`@prp-`/`@thm-`) are NOT citations — skip
them. The literature corpus is complete: check_plan already enforces that every `@key` has
a `literature/<key>.md`. This audit goes *beyond existence* (check_plan's job) to
**appropriateness** (does the source support the claim) — the substantive part.

Scrutinize hardest the load-bearing attributions, where a specific result is pinned to a
specific source: `chanGeneralFeasibleTests2022` (AoS) and `chanMultipleImprovementsMultiple2022`
(Stat Sinica) — keep the two Chan works' results straight; `mengMultipleImputationInferencesUncongenial1994a`
(congeniality), `mengPerformingLikelihoodRatio1992b` (LRT combining rule),
`rubinMultipleImputationNonresponse1987` / `rubinInferenceMissingData1976b`,
`cavanaughAkaikeInformationCriterion1998a` (AICcd, EM observed-data MLE — a *parallel*
universe, not this paper's target), `shimodairaInformationCriterionModel2017` (AIC_{x;y};
the penalty precedent), `weiMonteCarloImplementation1990` (MCEM), `nielsenProperImproperMultiple2003`,
`woodburyMissingInformationPrinciple1972`, `kenwardLikelihoodBasedFrequentist1998` (observed
vs expected information convention), `claeskensconsentinoVariableSelectionIncomplete2008`
(missing-covariate, Takeuchi-type — a *different* discrepancy) vs
`consentinoclaeskensOrderSelectionTests2010` (the MI averaged-criterion proposal),
`hensModelSelectionIncomplete2006a` (reweighting). §4: `vuongLikelihoodRatioTests1989`
(non-nested), `daviesAlgorithm155Distribution1980` / `imhofComputingDistributionQuadratic1961`
(quadratic-form distribution), `kolenTestEquatingScaling2014` (equating),
`satorraEnsuringPositivenessScaled2010` / `asparouhovRobustChiSquare2006` (scaled-shifted).

---

## Method (per attachment)

1. **Enumerate** every `@citekey` occurrence in level3 (`draft_prose` of all sections +
   `abstract`) with its **attachment context** — the exact claim sentence/clause it backs.
   Adapt `scratchpad/discover_level3.py` from todo/038 (it already strips cross-refs and
   maps keys→sections). Emit a citation→claim map.
2. For each distinct key, **read `literature/<key>.md`** (the verbatim source).
3. For each attachment, **judge support**: does the source, as written, establish the claim
   AS USED here? Verdict ∈ {supports / overstates / misattributed / wrong-work / partial},
   with the **exact supporting (or contradicting) passage** quoted from the source as
   evidence.
4. **Compile flagged** attachments → an edit list: fix the attribution, soften the claim to
   what the source supports, swap to the correct work, add a better source, or move/remove
   the cite.

**Guard against self-rubber-stamping** (the in-session Claude reading its own draft risks
confirmation bias): lead with the repo-grounded read, but escalate every FLAGGED or
borderline attachment to an **independent check** before finalizing — either a separate
Agent that reads source+claim cold and rules support/no, or (for a contested batch) a
`tkal-in-ket:quorum` where I defend the attribution from the verbatim source and the
cross-family peers probe. The verbatim passage is the arbiter, so most calls are near
mechanical.

---

## Gates (human-in-the-loop, mirror todo/038)

- show Marcus the **assembled citation→claim map** before auditing;
- show the **flagged set** (with the source passage per flag) before building edits;
- show the **edit list** before applying. Do NOT edit level3 during the audit — collect
  verdicts, then edit.

**Output / deliverable:** a per-citation audit result + an adjudicated edit list, fed to the
annotation pass and compile-enablement. Apply via an atomic update script under
`manuscript/plan/updates/` run through **Bash** (the check_citations hook misfires on
Edit/Write under `manuscript/`); keep check_plan green; render + commit + push.

---

## Lessons to carry from todo/038 (1a)

- **Due diligence against the DATA, not the prose or a panel's assumption.** In 1a the
  quorum recommended adding a "congenial" qualifier to the W3 100% claim; the actual results
  (`verification/cache/run_all-regen/phase2-w3/summary.csv`, `W3C_high_RIV_frac = 1.000` in
  all 60 cells; verdicts H2/H5) showed it held everywhere, so the qualifier was *dropped*.
  Verify each claim's wording against the source/results directly.
- **tkal "REFUTED" aggregation bug** (if any quorum is used): `collect_sustained_objections`
  OR's the *probe-time* `is_inaccuracy` flag, so a determination that merely re-lists an
  inaccuracy-tagged objection as an edit item trips the refuted gate even when every peer
  ruled `determination: "amended"` with `is_inaccuracy: false`. Read the per-peer
  `determination.json` (`determination` + per-objection `is_inaccuracy`), not the printed
  headline class. One-line fix worth making in `~/git-repositories/tkal-in-ket`: use the
  determination-stage flag, or skip `withdrawn` objections.
- **tkal gotchas** (reusable): `tkal preflight --config <cfg>` is definitive; route a
  rate-limited family through DeepInfra (`routes`+gateway `models` id; Gemini =
  `google/gemini-3.1-pro`); do not set `thinking_budget` for the claude provider (opus-4-8
  rejects it). The quorum tier presets are DeepInfra-forward (even `standard` = 2 cheap
  open-weights + a frontier lead); for a frontier-only panel, override `peers`/`lead`
  explicitly rather than trusting a preset name.

## Binding standards (inherit)

- Citation discipline: every `@key` in `manuscript/` backed by a `literature/<key>.md` read
  in-session — that local source is exactly what makes this audit possible.
- D-17 (no verbatim quotation of other work in the *manuscript prose*) is about the
  manuscript; quoting `literature/` sources *into the audit artifact and to any review
  panel* (not into the manuscript) is the mechanism and is fine.
- level3 is the prose source of truth; edits via the update-script path above.
- tkal runs are billed and user-triggered; if a quorum/tribunal is used for the flagged set,
  confirm scope with Marcus first. Save artifacts under `tkal-reviews/`.

---

## State at handoff

- Branch `contributions-delphi-todo035`, pushed to `origin` (set up to track). `main` is
  unchanged (not merged). The 1a edits are at `57df922`.
- todo/038 stage 1a COMPLETE: cross-family delphi (pool, unanimous 20-issue set) → quorum
  (frontier-core: GPT-5.5 lead + Gemini-via-DeepInfra; I defended repo-grounded) →
  determination AMENDED → 20 edits applied + committed. Run record:
  `tkal-reviews/textvalidity-20260628T193253Z/` (delphi `1a-claim/REPORT.md`; quorum
  `quorum/DETERMINATION.md` + `EDIT-LIST.md`).
- Obsolete: the `1b-cite/` delphi staging in that run dir (the delphi approach for 1b was
  abandoned — use the repo-grounded audit here).
- Optional consistency item (out of scope for 1a, fold in here or at annotation): **S4-P22**
  also says "…refinements are developed separately", the same phrasing the quorum fixed in
  S6-P6 → consider "left to future work".
- Nothing in this audit started. This handoff is the design of record.
