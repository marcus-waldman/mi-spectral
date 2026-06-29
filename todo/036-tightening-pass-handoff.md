# todo/036 — Prose tightening pass (HANDOFF, next session)

**Status:** OPEN, not started. Authored 2026-06-27 at the end of the todo/035
session (contributions + accuracy pass + cadence/style pass). Branch
`contributions-delphi-todo035`, head `af2f22c`, **unmerged/unpushed**.

**Intent (Marcus, verbatim sense):** a pass that **tightens the prose without
losing meaning**, cutting the fluff/filler words and empty force-phrases ("give it
its force", etc.), while **abiding by the prose standards already set**. Marcus does
**NOT** want this run as a Workflow ("that is problematic"). He **does** want an
**adversarial check on the proposed tightening of each paragraph**, but interactive
and human-gated, not a fire-and-forget batch.

---

## The design principle (the central tension)

Tightening pulls against three standing house rules: *state every logical step
plainly*, *a little redundancy is acceptable*, *keep the reading level low*. A naive
"make it shorter" pass breaks all three. So the goal is **not** "shorter":

> **Remove words that carry no information; keep every load-bearing step.**

- **Fluff** (cut it): empty intensifiers and filler — "very / quite / rather /
  somewhat / fairly / relatively", "simply / clearly / obviously / of course /
  basically / essentially / actually / really / just / indeed / notably /
  importantly", and empty phrases — "it is important to note that", "it should be
  noted", "it is worth noting", "as we have seen", "in order to", "due to the fact
  that", "the fact that", "for the purpose of", "with respect to", "in terms of",
  "a number of", "there is/are ... that", "it turns out that", and vague
  force-metaphors like "gives it its force".
- **NOT fluff** (keep it): the restatement that saves the reader an inference, the
  explicit logical step, the hedge / qualifier / scope condition. Cutting these is
  the failure mode the adversary exists to catch.

The distinction between fluff and clarifying-redundancy is the whole job. Tightening
is precision, not compression.

## Why not a Workflow, and the mechanism instead

The todo/035 cadence Workflow *auto-rejected* (36 paragraphs flagged invisibly,
all-or-nothing; the human never saw the argument), auto-applied in big batches, and
hid a literal-`\n` corruption. For tightening, "did this cut meaning" is a judgment
**Marcus** should make, not a lens. So flip it: **the adversary surfaces objections
to the human; the human is the gate.**

**Per-paragraph, human-in-the-loop, no Workflow tool:**
1. **Fluff flagger** (build `scripts/fluff_flag.py`, same scout pattern as
   `cadence_flag.py` / `overclaim_flag.py`): score each level3 paragraph by
   filler-word / empty-phrase density, rank worst-first, write the work-list to
   `verification/cache/`. Deterministic and auditable.
2. **Per paragraph, worst-first:** the main agent proposes a tightened version, then
   spawns **ONE independent adversary** via the **Agent tool** (a single subagent,
   NOT the Workflow machinery) charged to attack the proposal. Present to Marcus:
   **original → tightened → adversary's objections + verdict**. Marcus rules
   keep / apply / edit on each. One at a time, fully visible.
3. **Apply** through the token guard in `scripts/apply_cadence_batch.py` — but FIRST
   add a **newline-structure guard** (count real newlines and reject any rewrite that
   introduces a literal backslash-n; this is the gap that let the todo/035
   corruption through — the token guard checks math/numbers/citations, not newline
   structure).

The single-adversary-per-paragraph gives the same rigor as the Workflow's verify
lenses, but synchronous, visible, small blast radius, human-adjudicated.

## The adversary's charge (its checklist for each proposal)

1. **Meaning / hedge / scope preserved?** Did the cut drop a qualifier, a hedge, or
   a scope condition? No softened word ("exactly / every / always / restores",
   known-scale qualifier, "at the null", "to leading order", "substantially")
   reintroduced — this must not undo the todo/035 accuracy pass.
2. **Genuinely tighter, or just shorter?** Shorter-but-vaguer fails.
3. **Over-tightened?** Did it re-introduce an inference the reader now has to make,
   or raise the reading level? (Guards the "state steps plainly / redundancy OK /
   low reading level" rules.)
4. **Standards:** punctuation budget v2 (connectives fine, <=1 semicolon, no
   em-dash, no rhetorical colon), T-03 jargon ban, trust-ordering intact.
5. **Cadence not regressed:** tightening loves to delete the connectives the cadence
   pass just added; check the result did not revert to a monotone short-declarative
   column (`scripts/cadence_flag.py` can spot-check).
6. **Tokens / newlines preserved:** every number, @citation, @cross-ref, $math$,
   image/caption verbatim; no literal `\n`.

## State at handoff

- **Branch** `contributions-delphi-todo035` (4+ todo/035 commits + the style pass;
  unmerged/unpushed). Last render clean: arxiv-pdf, 26 pp, 0 Overfull.
- **Done this session:** contributions list + implications + abstract (Delphi-vetted,
  D-15); author block (D-16); no-direct-quotes (D-17); punctuation budget **v2**
  (CLAUDE.md + `check_plan.py` gate — connectives encouraged, <=1 semicolon allowed,
  em-dash banned, no-orphan-pronoun rule); **accuracy pass** (15 overclaim fixes,
  3d0d844); **cadence/style pass** (45 paragraphs rewritten, connective rate
  0.07 -> 0.16/sentence).
- **Reusable scouts already committed:** `scripts/corpus_vocab_check.py` (manuscript
  vs literature vocab), `scripts/overclaim_flag.py` (sweeping/precision claims),
  `scripts/cadence_flag.py` (monotony), `scripts/apply_cadence_batch.py` (token-guarded
  applier — ADD the newline guard before reuse).
- **Optional leftover (separate from tightening):** the cadence pass flagged 36
  paragraphs the strict cadence lens rejected (not applied). A softer cadence
  "pass-3" could reclaim ~15-20. Ids: S5-P2, S5-P15, S3-P8, S2-P9, S5-P19, S2-P6,
  S4-P18, S6-P7, S4-P10, S6-P6, S5-P16, S6-P4b, S2-P2, S4-P11, S4-P8, S6-P1, S6-P2,
  S4-P1, S3-P7, S4-P7, S2-P10, S4-P9, S1-P4, S4-P14, S3-P6, S5-P14, S1-P2, S1-P5,
  S3-P4, S6-P8, S6-P5, S1-P3, S4-P22, S6-P4, S4-P15, S2-P5. Decide whether to fold
  this into the tightening pass or skip it.

## Binding standards to obey (do not relitigate)

- level3 paragraphs are the prose source of truth; edit via an atomic update script
  under `manuscript/plan/updates/` run through Bash (the check_citations hook
  misfires on Edit/Write under `manuscript/`); keep `check_plan` green.
- CLAUDE.md "Manuscript prose style": plain expository, punctuation budget v2,
  no orphaned pronouns, T-06 (no verbatim quotation of other work, D-17),
  trust-ordered claims, banned vocabulary T-03.
- Render with `manuscript/preview-jasa/build_preview.py` then quarto
  (`C:\Program Files\RStudio\resources\app\bin\quarto\bin\quarto.exe`). If the render
  is slow, it is a one-time tinytex tlmgr package update — LET IT FINISH, do not kill
  it or hand-roll xelatex (see memory `feedback_render_use_standard_quarto`).
