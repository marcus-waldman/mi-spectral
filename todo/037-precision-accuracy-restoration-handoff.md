# todo/037 — Precision & accuracy restoration pass (HANDOFF, next session)

**Status:** OPEN, not started. Authored 2026-06-28 during the apaquarto-preview /
front-matter session (Marcus flagged four recurring prose patterns to address in a
fresh session). Branch `contributions-delphi-todo035`, head `db2a0ac`,
**unmerged/unpushed**.

**Intent (Marcus):** a reviewer-grade pass that **re-injects the precision and
accuracy the plainification arc traded away**. This is the *complement* of the
shelved tightening pass (todo/036): tightening cut words; this one will sometimes
**add** words for specificity and accuracy. The submission audience is **expert
reviewers who want verifiable facts**, not a learner who needs scaffolding.

---

## The root cause (one frame)

The readability / cadence / vocab-softening arc optimized for **plainness and flow**.
Its token guards (`apply_cadence_batch.py`) protected numbers, citations, and math —
but nothing protected **meaning**. So a phrasing that is vaguer, more
pronoun-dependent, names the wrong cause, or editorializes all passed every check.
This pass restores precision against that erosion. Four patterns, all one theme:
**trade pedagogical scaffolding for verifiable facts.**

A guard that must not be over-read: *stating a logical step plainly is substance and
stays; the "a little redundancy is OK" license covers restating CONTENT for clarity.*
It never licenses vagueness (1), orphaned pronouns (2), a wrong cause (3), or
evaluating that-something-matters (4).

---

## The four patterns

### 1. Specificity — name the direction, not "one / the other"
- **What:** placeholders that hide a load-bearing asymmetry.
- **Example (Marcus):** "...what happens when values built around one estimator are
  read as if built around the other." The result is **not** symmetric: the deviance
  is built around the **observed-data maximizer $\theta_{\text{obs}}$** and read as if
  built around the **complete-data maximizer $\theta_{\text{com}}$**. "One / the other"
  deletes exactly the fact that makes the claim specific.
- **Fix:** when there is a direction or an asymmetry, name **both** roles; never
  abstract them into interchangeable tokens.
- **Detect:** mostly **semantic** (not cleanly lexical). A light scout can flag
  "one ... the other", "these two", "each ... the other", and bare "it/this" near a
  headline claim, but the real catch is the mechanism-fidelity lens + human read.

### 2. Orphaned "it" / "itself" — join the clauses
- **What:** a pronoun whose antecedent sits a clause-or-more back, especially at
  clause/sentence ends and (worst) in headers and list labels.
- **The fix is to JOIN, not merely "name the noun":**
  - **Compound predicate.** "$\theta_{\text{com}}$ is computable only when nothing is
    missing. **It** is the target..." -> "$\theta_{\text{com}}$ is computable only when
    no data are missing **and is** the target the analyst would have reached with full
    data." One subject, two predicates joined by "and"; the orphaned "It" is gone and
    $\theta_{\text{com}}$ reads as one idea. ("no data are missing" also beats the
    colloquial "nothing is missing".)
  - **Relative clause.** "The E-step computes $Q(\cdot\mid\phi^{(p)})$ **and** the
    M-step maximizes **it**." -> "...computes $Q(\cdot\mid\phi^{(p)})$, **which** the
    M-step **then** maximizes." "which" sits right after $Q$ (unambiguous referent);
    "which...then" subordinates the M-step as acting **on the E-step's output**, which
    is the actual algorithm — "and" flattened it to parallel actions.
  - **Self-contained entry points.** "The deviance bias behind **it**." (a list
    header) is unreadable to a reader who jumps in. Headers, list labels, and topic
    sentences must carry no back-referencing pronoun -> "The deviance bias behind the
    correction."
- **Principle:** an orphaned "it" usually signals two clauses that want to be one
  (joined by "and / which / so / then") — which kills the pronoun, anchors the
  referent locally, and exposes the logic the two-sentence version hid. This is also
  where independent-plus-dependent-clause variety comes from.
- **Detect:** `cadence_flag.py` already counts pronoun-OPENERS; extend to all
  it/its/itself/this/that with a distant/ambiguous antecedent, and **separately**
  flag any header / list-label / topic-sentence containing a back-referencing pronoun
  (zero tolerance at entry points). Reinforces the punctuation-budget-v2
  no-orphaned-pronoun rule.

### 3. Mechanism inaccuracies — name the correct cause
- **What:** a plain-but-WRONG cause substituted for the precise one.
- **The recurring instance:** "...favor the models that **lost the most data**."
  Models do **not** lose data — every candidate is fit to the **same** imputed data;
  the per-candidate driver is its own **$\operatorname{tr}(\mathrm{RIV})$** (its
  missing information about the parameters). This is the exact misconception fixed in
  the **abstract** (`53b96bc`) that **still sits in the S1-P6b Contributions list**
  (item 1) — the abstract fix was a point-fix, not a sweep.
- **Why it happens:** plainification swaps the precise driver ("larger relative
  increase in variance") for a wrong plain one ("lost the most data") — plainer, flows
  better, changes no protected token, and is wrong. The overclaim pass can't catch it
  (it hunts claim STRENGTH, not mechanism). The root: there is **no
  mechanism-fidelity guard**.
- **Fix:** state the correct driver — model-specific
  $\operatorname{tr}(\mathrm{RIV})$ / missing information about the parameters.
- **Detect:** (a) **data-quantity scout** — flag "lose / lost / less / more data",
  "models that ... data": since all candidates share the imputed data, any such phrase
  is wrong by construction (cheap, catches this recurring error directly); (b)
  **claim-level mechanism-fidelity lens** (semantic, the real fix).

### 4. Color commentary — cut evaluative narration
- **What:** sentences that **evaluate** an object's importance or narrate the "work"
  it does, instead of stating the object and its consequence.
- **Examples (Marcus):** "This assumption is what **gives the main theorem its
  force**." / "**does real work** in the theorem." Also: "the **key/crucial/essential**
  assumption", "**crucially**", "the **heart/crux** of", "**carries/drives**", "the
  **workhorse**", "does the **heavy lifting**", "what **makes** X **work**".
- **Why bad for reviewers:** padding, and it tells an expert what to find important —
  which invites "don't tell me, show me".
- **Fix:** state the fact **and its consequence**; demonstrate that something is
  load-bearing by showing what changes without it, never by asserting it.
  - "This assumption is what gives the main theorem its force." -> name the assumption
    and the consequence riding on it: *"The
    $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ term arises only because the model
    estimates a scale or covariance; a known-scale fit does not produce it."* The
    "force" is now shown, and a reviewer can check it.
- **Distinction (keep-rule guard):** "We use Result 3.2 here" stays; "Result 3.2 does
  the real work here" goes. The human gate keeps the rare instance where the gloss
  genuinely aids comprehension.
- **Detect:** **lexical scout** for the evaluative-phrase list; generalizes the
  `force_metaphor` category already in `fluff_flag.py` (which caught "gives it its
  force") to the whole evaluative-narration class.

---

## Standing accuracy invariant (prevent recurrence)

Record and enforce: **"Models never lose or gain data — every candidate is fit to the
SAME imputed data; the per-candidate driver of the bias is its own
$\operatorname{tr}(\mathrm{RIV})$ (its missing information about the parameters)."**
- Add to CLAUDE.md prose-style standards (alongside T-03 banned vocabulary).
- Add a banned-phrase entry to `scripts/check_plan.py`: flag data-quantity
  attributions ("lose/lost/less/more data" near selection claims) and the
  color-commentary phrase list, so future plainification has a guardrail.

---

## Audit tooling to build (scouts + lenses)

- `scripts/color_commentary_flag.py` (or extend `fluff_flag.py`) — evaluative-phrase
  scout (pattern 4). Cleanly lexical.
- `scripts/mechanism_flag.py` (or a `check_plan` rule) — data-quantity attribution
  scout (pattern 3). Cleanly lexical.
- extend `scripts/cadence_flag.py` — distant/ambiguous-pronoun + header/label
  self-containment check (pattern 2). Mostly lexical.
- **mechanism-fidelity LENS** (pattern 3) and **specificity LENS** (pattern 1) — these
  are SEMANTIC; they are an adversarial-agent charge, not a scout. The agent compares
  each claim's stated cause/direction against the proof (`derivation.qmd`, the
  CLAUDE.md core-contribution statement). Do not expect a clean worst-first list for 1
  and 3 — they need the read, with the scouts only as a lexical assist.

---

## The mechanism (how to run it) — same as todo/036, Marcus-ratified

Per-paragraph, **human-in-the-loop, single independent adversary via the Agent tool
(NOT a Workflow)** — the WORKFLOW-PALATABILITY decision (2026-06-27) stands. For each
flagged paragraph: propose a precision-restoring rewrite, spawn one adversary, present
**original -> rewrite -> adversary's objections + verdict**, Marcus rules
keep/apply/edit.

**Adversary's charge (this pass):** (1) every number, @citation, $math$, hedge, and
scope condition preserved or correctly added; (2) the stated cause/direction matches
the proof (no mechanism error reintroduced; "lost data" etc. banned); (3) orphaned
pronouns removed by JOINING, not just renaming; entry points self-contained; (4) color
commentary cut WITHOUT cutting substance; (5) not over-tightened, reading level not
raised, plain-expository arc intact; (6) newlines + protected tokens preserved (the
todo/036 newline guard).

**Applier caveat — important difference from todo/036:** precision rewrites may
legitimately **add** a math symbol (naming $\theta_{\text{obs}}$/$\theta_{\text{com}}$)
or a citation, which the `apply_cadence_batch.py` token guard would REJECT as a
math/ref multiset mismatch. So either (a) extend the applier to allow reviewed
additions, or (b) apply through a normal level3 update script under
`manuscript/plan/updates/` with per-change review. The newline guard still applies.

**Method:** calibrate on ~4-6 paragraphs against Marcus's eye before scaling (the same
proven method as the readability and cadence passes), since patterns 1 and 3 are
judgment-heavy.

---

## Why this pass IS worth it (unlike todo/036)

todo/036 (cut fluff) was shelved because the corpus was already lexically tight —
low yield, real overclaim risk. todo/037 is **high-yield and submission-critical**:
there are genuine **accuracy** defects (the "lost data" mechanism error twins the
abstract fix and would embarrass at review), the orphaned-"it" and color-commentary
patterns are pervasive and reviewer-facing, and the fixes ADD precision rather than
risk cutting meaning.

---

## Binding standards to obey (inherit)

- level3 is the prose source of truth; edit via an atomic update script under
  `manuscript/plan/updates/` run through **Bash** (the check_citations hook misfires on
  Edit/Write under `manuscript/`); keep `check_plan` green.
- Verify `git branch --show-current` is `contributions-delphi-todo035` before building
  or rendering (a concurrent session can flip the working tree; the tell is the
  builder's paragraph count changing). See memory `feedback_verify_branch_before_render`.
- CLAUDE.md prose style: plain expository, punctuation budget v2, no orphaned
  pronouns, no verbatim quotation (D-17), trust-ordered claims, banned vocabulary T-03;
  plus the new accuracy invariant and the no-color-commentary standard above.
- **Audience note to reconcile:** CLAUDE.md names the target reader as an applied
  researcher; the *submission* audience is expert reviewers. These do not conflict —
  plain structure and applied motivation (the roadmap, the applied-first hook) serve
  the applied reader; cutting color commentary and mechanism errors serves both. Keep
  pedagogical CLARITY (plain steps, motivate by use); cut pedagogical EVALUATION
  (telling the reader what matters).
- Render with `manuscript/preview-jasa/build_preview.py` (arxiv) and/or
  `manuscript/preview-apa/build_apa_preview.py` (apaquarto), then quarto; if a render
  is slow it is a one-time tinytex update — let it finish (memory
  `feedback_render_use_standard_quarto`).

---

## State at handoff

- Branch `contributions-delphi-todo035`, head `db2a0ac`, unmerged/unpushed.
- Reusable scouts committed: `corpus_vocab_check.py`, `overclaim_flag.py`,
  `cadence_flag.py`, `fluff_flag.py`, `apply_cadence_batch.py` (token + newline guard).
- The four patterns above were flagged by Marcus from reading the rendered manuscript;
  S1-P6b item 1 is a confirmed concrete pattern-3 instance. No prose touched this
  session.
