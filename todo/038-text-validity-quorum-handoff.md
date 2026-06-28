# todo/038 — Text-validity defense via tkal-in-ket (two delphis → quorum) (HANDOFF, next session)

**Status:** OPEN, not started. Designed 2026-06-28 (the session that executed todo/037).
Branch `contributions-delphi-todo035`, head `eb6c155`, **unmerged/unpushed**. The
manuscript prose is post-todo/037 (precision pass done; check_plan green; APA preview
clean at 85 ¶ / 7 sections).

**Intent (Marcus):** put the manuscript **text as written** through a rigorous,
repo-grounded defense. The panel reads the actual prose, points at a specific
sentence, and challenges it as *speculation / overclaim / unsupported-as-written* or as
*citing a source that does not support the claim*. The in-session Claude (me) defends —
a committed honest advocate, reluctant to concede, never asserting an inaccuracy —
grounding each defense in what the paper itself shows (for claim support) or in
**verbatim** text from the cited source (for citation support). Concede only a
**wording amendment** where the prose genuinely outruns its support; never the science.

**Off the table:** the correctness of the theorem and the simulation results. Those
already went through the S5 cross-family tribunal (verdict AMEND, no result retracted;
`tkal-reviews/tribunal-20260627T014721Z/`, memory `project_s5_tribunal_review`). This
exercise tests the **writing's fidelity to** the results, not the results.

---

## The canonical example (Marcus's, defines the mode)

> **Panel:** "You wrote in the abstract that it favors more complex models, but you
> show no evidence of that — that claim comes across as speculation."
>
> **Defender (me):** Not speculation; derived then measured, and the abstract names the
> cause itself: *"biased toward more complex models, **because their larger relative
> increase in variance** makes the fit look better than it is."* The mechanism is proved
> in §4 (each candidate's criterion inflated by its own ½ tr(RIV), so higher-RIV is
> favored). The evidence is preregistered in §5: across all 60 cells, *"every
> misclassification by uncorrected MI-AIC chose the candidate with the largest RIV"*
> (W3-C = 1.000), against the prediction registered at S4-P18. In the nested families
> studied, the more complex candidate is the higher-RIV one, so the two descriptions
> coincide there. **Concession boundary:** if the panel holds that "more complex models"
> overreaches its nested-family evidence (complexity ⇒ high-RIV is not universal), amend
> to keep the headline on the proven driver — *"biased toward the candidates with more
> missing information, which in nested families are the more complex ones"* — the same
> accuracy invariant the body already uses (S1-P4, S1-P6b, and CLAUDE.md). A **wording**
> fix, not a retraction.

That texture — defend by pointing to where the paper earns it; concede only wording
where it doesn't — is the whole job.

---

## Structure: two delphis (parallel) → one quorum

### Stage 1a — claim-support delphi (pool mode)
Does the prose earn each claim from the paper's **own** derivation / figure /
preregistration? Panel converges (iterate-to-stability) on the consensus set of the
sentences that read as speculation, overclaim, or unsupported-as-written.
**Constraint in the prompt:** the theorem and the sims are correct and OFF-LIMITS —
challenge the *writing*, not the math. A claim that *lacks* a needed citation folds in
here (an internal-support gap), not in 1b.

### Stage 1b — citation-support delphi (pool mode)
Does each **existing** citation actually support the claim it is attached to? The panel
may challenge from **training knowledge** of the cited works. **Guard (keep 1b
signal-rich):** flag a citation only with a *specific* recollection of what the source
covers, and state confidence — not vague unfamiliarity. The defender rebuts with
**verbatim** text from `literature/<citekey>.md`.

**Why 1b is well-posed:** the panel challenges from *fallible training memory*; I rebut
from *ground truth* — the local markdown is the actual PDF we converted and read
in-session. Memory loses to source. It directly stress-tests the #1 AI-paper failure
mode (hallucinated / misattributed citation). And pool convergence is the noise filter:
a single model's shaky recollection that the other two don't independently share drops
out before the ratified set — so 1b only escalates citations multiple families doubt
for concrete reasons.

1a and 1b are independent lenses → **run them in parallel**.

### Stage 2 — quorum
I defend the **union** of both ratified issue sets, repo-grounded:
- claim-support issues → defended by pointing to the paper's own § / figure /
  preregistration;
- citation issues → defended by **verbatim** source text.

Per-issue determination: **upheld-as-written / amend-wording / refute**. The looping
deliberation is free to escalate a *new* issue if one of my defenses opens a hole (the
delphi set is the floor, not a hard freeze).

**Output / deliverable:** a defended, adjudicated edit list — the amend/refute items
become concrete wording / citation fixes for the next annotation pass and feed
compile-enablement; the upheld items are certified earned. tkal artifacts land under
`tkal-reviews/` (as prior tribunal/delphi runs did).

---

## Locked design decisions (ratified this session)

- **Two delphis, parallel:** 1a claim-support + 1b citation-support (distinct failure
  modes, distinct defenses).
- **No hard cap on issues.** Use a *severity threshold* ("would a careful reviewer flag
  this?") and let the pool converge on the set it collectively endorses as serious; size
  emerges from real problem density. Applies to BOTH delphis.
- **1b guard:** specific recollection + stated confidence, not vague unfamiliarity.
- **EFFORT/TIER — NOT max** (decision evolved: Marcus first said max, then questioned it
  because the task is training-weight recall + within-text inference, and we agreed to
  step down). Rationale: what discriminates here is cross-family **diversity** + careful
  **reading** + enough probing **rounds**, NOT per-turn reasoning depth; and the
  ground-truth check (1b) is my verbatim quote, which doesn't depend on panel effort.
  - Both **delphis**: frontier cross-family panel (opus-4-8 / gpt-5.5-pro /
    gemini-3.1-pro) at **normal** effort — diversity is the catch engine.
  - **Quorum**: **standard** tier (NOT max, NOT cheap), with **deliberation rounds
    preserved**. Do NOT drop to cheap open-weights peers — weak models misread dense
    methods prose and have poor recall of the specialized citations (Chan 2022 AoS, Meng
    1994), which makes 1b noisy. Rigor lives in the rounds + the relentless-press
    instruction + my reluctance-to-concede, not in token depth.
  - **Caveat to resolve first:** I'm inferring what each quorum tier trades (panel size
    vs rounds vs per-turn effort). READ the skill to confirm exactly what standard-vs-max
    changes; if "standard" guts the rounds rather than just the effort, keep the rounds
    and lower only per-turn effort.
- **Defender is the in-session Claude, repo-grounded.** The harness/tkal defender has no
  repo access and concedes everything (memory `feedback_tkal_tribunal_repo_grounded`,
  Marcus: "you should be the one defending"). I author every defense from the actual
  proofs, figures, preregistrations, and `literature/` sources.
- **Surface (both stages):** abstract + §1 + §1B + §2 + §3 + §5 + §6. **Excludes §4
  (derivations)** — little overclaim risk and the deep technical claims are not what's
  being tested. §5 prose STAYS (check the writing's fidelity to the sims, not re-test the
  sims).

---

## Setup steps for the next session (in order)

1. **Verify branch** is `contributions-delphi-todo035` (`git branch --show-current`). A
   concurrent session can flip the tree; the tell is the assembled paragraph count —
   should be **85**, not 83 (memory `feedback_verify_branch_before_render`).
2. **Inspect both tkal-in-ket skills' interfaces** (`tkal-in-ket:delphi`,
   `tkal-in-ket:quorum`): how each ingests the document, the pool-mode parameters, and
   the exact **tier/effort definitions** (resolve the caveat above). The delphi has pool
   and axes modes — use **pool** (converge on the best SET of issues), not axes.
3. **`tkal preflight`** — the definitive API-key check. The engine `.env` supplies all
   three keys (ANTHROPIC / OPENAI / GEMINI) even when the process env lacks
   ANTHROPIC_API_KEY. Quorum's peer routing may also want DEEPINFRA_API_KEY — but we are
   NOT using cheap open-weights peers, so confirm the standard tier's peer set.
4. **tkal gotcha:** drop `thinking_budget` for the claude provider — it sends
   `thinking.type.enabled`, which opus-4-8 REJECTS. (Memory: tkal-in-ket GOTCHA
   2026-06-27; axes batches all axes per call; preflight is definitive.)
5. **Verify the literature corpus is complete** so no verbatim defense comes up empty:
   every `@citekey` used in level3 prose has a `literature/<citekey>.md` (check_plan
   already enforces this — ~35 distinct keys; `.bib` = the Better BibTeX export). Spot
   the load-bearing ones for 1b: `chanCalibratedMultipleImputation2022` (AoS),
   `mengMultipleImputationInferencesUncongenial1994a`,
   `rubinMultipleImputationNonresponse1987`,
   `cavanaughAkaikeInformationCriterion1998a`, `shimodairaInformationCriterionModel2017`,
   `weiMonteCarloImplementation1990`, `nielsenProperImproperMultiple2003`.
6. **Assemble the manuscript text** from level3 (the clean source of truth) for the
   in-scope sections, **with citations visible** (author-year or @citekey) so 1b can
   target them. Reuse the preview-builder machinery
   (`manuscript/preview-apa/build_apa_preview.py` or `preview-jasa/build_preview.py`) or
   extract `draft_prose` per section directly; whichever shows the citations to the
   panel cleanly. The panel must quote real sentences.
7. **Pre-stage verbatim passages:** once 1b returns its ratified set, pull the relevant
   passage from each flagged `literature/<citekey>.md` before the quorum so the defense
   is fast and exact.

---

## Binding standards to obey (inherit)

- level3 is the prose source of truth; if the quorum yields amend/refute edits, apply
  them via an atomic update script under `manuscript/plan/updates/` run through **Bash**
  (the check_citations hook misfires on Edit/Write under `manuscript/`); keep check_plan
  green. Do NOT apply edits during the defense — collect the determinations, then edit.
- Citation discipline (load-bearing): every `@citekey` in `manuscript/` is backed by a
  `literature/<citekey>.md` read in-session; that is exactly what makes the 1b verbatim
  defense possible.
- No verbatim quotation of other work in the *manuscript prose* (D-17) — note this is
  about the manuscript; quoting `literature/` sources to the **quorum panel** (not into
  the manuscript) is the defense mechanism and is fine.
- tkal runs are billed and user-triggered; this is a deliberate, Marcus-authorized
  exercise. Save artifacts under `tkal-reviews/`.

---

## State at handoff

- Branch `contributions-delphi-todo035`, head `eb6c155`, unmerged/unpushed (the whole
  stack from `bf98d77` is unpushed; merge/push decision still pending Marcus).
- todo/037 precision pass COMPLETE (5 commits: `15e1b1b` scouts, `2e9b28c` S1-P6b +
  accuracy invariant, `fb5e9eb` calibration set, `8d7eccf` batch 1, `eb6c155` color
  guard). check_plan green; color + mechanism scouts clean corpus-wide; APA preview clean.
- No quorum/delphi work started. This handoff is the design of record; nothing executed.
- Optional residual from todo/037 (do or skip): S4-P1 "It prices the bias" → "The theorem
  prices the bias" (triage held KEEP, zero-risk).
