# todo/035 — Contributions + applied-implications subsection, Delphi-vetted (HANDOFF)

**Status:** OPEN, not started. Authored 2026-06-27 as a next-session handoff after
todo/034 (rendering polish + the new S1B "AI–human collaboration" section, branch
`rendering-restructure-todo034`).

**Marcus's intent (verbatim sense):** add a subsection stating the paper's
**contributions** and its **implications for applied research** — the applied angle
so that an applied researcher who only skims the paper still finds it important. A
large part of the contribution is the **structured AI–human workflow/collaboration
with provenance** (now S1B + Methods). Run the contributions through a **Delphi**
(the `tkal-in-ket:delphi` cross-family consensus skill) before finalizing. Then
**modify the abstract and the Discussion close** to incorporate the result.

---

## Two structural wrinkles (resolve at session start)

1. **No Conclusion section.** D-09 ratified: no separate Conclusion; the Discussion
   (S6) broadens to the applied reader and the verdict paragraph (S6-SP4) is the
   takeaway. "Modify the conclusion" → modify the Discussion close.
2. **The abstract has no tracked home.** It currently lives only in
   `manuscript/preview-jasa/build_preview.py` front matter, which is gitignored. A
   durable abstract edit needs a tracked home (e.g. a small `abstract` field in the
   plan) or to ride along with compile-enablement's front-matter porting. Decide
   which before editing the abstract.

## Method note (from the tkal tribunal experience)

The `tkal-in-ket` panel models have **no repo access** and will otherwise deliberate
blind. The Delphi input must be a **self-contained brief**: each candidate
contribution stated with the evidence behind it (deriv anchor / verif artifact /
the W-study + number). Needs `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`
— confirm they are set first.

---

## Proposed sequence

1. **Draft a candidate contributions set** (seed below) + the applied-research
   implications, as a grounded brief.
2. **Run the Delphi** on the candidate set to converge/sharpen it (mode below).
3. **Write the "Contributions and implications for applied research" subsection**
   from the converged set, in the agreed location.
4. **Update the abstract and the Discussion close** to incorporate.
5. **check_plan** green; rebuild the arXiv preview; show Marcus.

## DECISIONS NEEDED FROM MARCUS (proposed defaults; confirm or adjust)

- **D1 — Placement.** Where does the subsection go?
  - *Default:* a subsection in the **Discussion** (S6), where "implications" live and
    the verdict already targets the applied reader, **plus** an abstract update so the
    skim-layer carries the hook.
  - *Alternatives:* a **Contributions enumeration at the end of the Introduction**
    (classic skim hook), or **both** (intro list + discussion implications).
- **D2 — One subsection or two.** *Default:* one ("Contributions and implications for
  applied research"): contributions first, applied implications second. Split if you
  want them separate.
- **D3 — Delphi mode.** *Default:* **pool** (iterate-to-stability — converge on the
  best set/phrasing of contributions). *Alternative:* **axes** to ratify a fixed list
  per criterion (real contribution? novel? important to applied readers?), or
  **pool-then-axes**.

## Seed candidate contributions (raw material for the Delphi; NOT final prose)

1. **Theory.** The averaged log-likelihood under congenial proper MI overstates its
   complete-data target by +½tr(RIV) + (A)+(C): an imputation-bias +tr(RIV) minus an
   estimation-mismatch ½tr(RIV); requires an estimated scale; the MAR design-imbalance
   term (A)+(C) is new (vanishes under MCAR). [deriv:sec-thm; W1]
2. **LRT application.** At the null the deviance numerator's differential bias is
   tr(RIV_⊥) in the I_com metric — provably NOT the naive difference of per-model trace
   corrections, which always overstates it; sharing imputations collapses paired noise
   to O(1). [deriv:sec-lrt; W2]
3. **IC application.** The bias is model-specific, so uncorrected MI-AIC/BIC favor
   high-missing-information candidates; adding tr(RIV_k) restores complete-data-equivalent
   selection and reproduces Shimodaira's AIC_{x;y}; the calibration ladder locates the
   null/noncentral boundary. [deriv:sec-ic; W3 + ladder]
4. **Methodological / workflow (a large part of the contribution).** A structured
   AI–human collaboration with transparent provenance that is both productive AND yields
   accurate conclusions: roles + decision records, sourced citations enforced
   mechanically, derive→dual-CAS→Monte-Carlo with trust tiers, preregistration with
   reported failures, cross-model adversarial review, full reproducibility. [S1B + S3;
   verif:verification/collaboration-analysis.md]

## Applied-research implications (seed)

- Practitioners who select models or compare nested models on multiply-imputed data are
  using statistics that are biased toward the candidates with the most missing
  information; the correction is a single trace term they can compute.
- A worked, auditable template for trustworthy AI-assisted methodological research — what
  an applied team can demand of an AI-assisted derivation before believing it.

## State at handoff
- Branch `rendering-restructure-todo034` @ `79b1e85` (todo/034 done, check_plan green,
  **unmerged, unpushed**). Merge or branch from it before starting.
- Open infra: the `check_citations` pre-write hook misfires on Edit/Write of files in
  `manuscript/` subdirectories (resolves its script path against cwd) — use Bash for
  `manuscript/` writes until fixed.
