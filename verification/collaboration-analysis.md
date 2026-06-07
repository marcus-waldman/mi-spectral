# Collaboration analysis: the mi-spectral session record

**Status:** committed record (todo/032 executed 2026-06-07). Cited by manuscript
paragraph S3-P2 via `verif:verification/collaboration-analysis.md`.
**Publication decision:** D-13 (2026-06-07, `manuscript/plan/decisions.md`) — the
raw session transcripts enter the public record; this document is the citable
summary resting on them.

## 1. Purpose

The Methods section of the manuscript states that direction, scope, and the
acceptance or rejection of every result were decided by the human author of
record. That sentence invites a question a skeptical reader should ask. What did
direction actually consist of? This document answers with a qualitative coding
of the complete session record rather than with episodes recalled by the
drafting session. It reports a taxonomy of human intervention types with
frequencies, a parallel set of AI-initiated move types, a verified episode table
tying interventions to dated artifacts, and a five-pattern characterization of
the collaboration. Manuscript paragraph S3-P2 is written from the
characterization, with the examples drawn from the episode table.

## 2. Data

The corpus is the complete set of Claude Code session transcripts for the
mi-spectral project, 2026-05-22 (inception) through 2026-06-07, recorded at
`~/.claude/projects/C--Users-marcu-git-repositories-mi-spectral/*.jsonl`.

A count reconciliation against D-13 is needed once. D-13 says "35 files". At
ratification the project directory held 35 `.jsonl` files. One of them
(`682aca99-*`, 149 bytes) is a bridge-session stub containing no conversation
turns. The analyzed corpus is therefore **34 substantive transcripts** (~88 MB
with the stub). The session that executed this analysis (`1088cf6b-*`) began
after D-13 was ratified and is outside the frozen corpus. The session that
created todo/032 and ratified D-13 (`35b5e1cf-*`) is inside it and was coded
like any other. MI-IC sessions are out of scope per D-13.

Per-file SHA-256 hashes for the deposit are prepared in
`verification/cache/collab-analysis/deposit-manifest.md`, with a
sensitive-content scan in `deposit-sensitive-scan.md` (same directory). Neither
constitutes the deposit itself, which awaits the author's review.

## 3. Method

Four phases, executed 2026-06-07. The analysis itself was performed by AI
agents. Its checkable parts (verbatim quotes, artifact existence, dates, the
frequency arithmetic) were verified mechanically. Its judgment parts (code
assignments) were not human-validated, which Section 9 records as the principal
limitation.

**Phase A — inventory** (`scripts/collab_extract_turns.py`). Every user-channel
turn was extracted with session id and timestamp. Harness traffic was dropped
and counted by reason. Of 976 non-tool-result user-channel turns: 106 metadata
turns, 65 slash-command invocations, 65 background-task notifications (see
below), 34 command-output dumps, 39 bare interruption markers, 67 trivial
approvals (bare "yes" / "ok" / "continue"), and 1 harness continuation summary
were dropped. **599 substantive human-authored turns remained (29,394 words)
across the 34 sessions.** Each turn carries the tail of the assistant message it
responds to, so coders could interpret the move in context.

**Phase B — open coding.** Each session was coded in full by one of 34 parallel
coding agents (Claude Opus 4.8, the same model lineage that produced the
project's derivations). Codes were constrained to a fixed list (Section 4);
phenomena outside the list had to be proposed explicitly rather than coded
freely. Every turn received one to three codes, dominant first. The agents also
recorded AI-initiated moves visible in the assistant-context tails and nominated
episode candidates. The per-session coded outputs are committed at
`verification/cache/collab-analysis/coded/` and are the primary data of this
analysis. AI coding is not deterministic, so these files, not the procedure, are
the record.

A data-cleaning step came out of the coding itself. Three coding agents
independently proposed a "system-notification" code for turns that occupy the
user channel but are machine-emitted (background-task completion notices). 65
such turns had survived the Phase A filter. They were excluded, the extractor
was fixed, and every count in this document is computed net of them
(`scripts/collab_consolidate.py`).

**Phase C — consolidation and cross-validation.** Frequencies were tallied from
the committed coded outputs. 61 episode candidates were then each cross-validated
by an independent verification agent, which checked the quote verbatim against
the extracted turn and traced the claimed artifact in
`manuscript/plan/decisions.md`, the git history, or the repository files. 58
survived: one quote needed correction (a dropped clause, corrected and
re-verified), two candidates were machine-emitted turns, and one artifact could
not be traced. Five further episodes needed for coverage of the patterns were
verified the same way by the consolidating session (quote check against the
extracted turns, artifact check against git). The verified table is
`verification/cache/collab-analysis/final-episodes.json`; Section 6 prints the
subset used in the manuscript.

**Phase D — synthesis.** This document and the S3-P2 rewrite.

## 4. Taxonomy

Ten codes were seeded by todo/032. Three were added before coding began, after
inspection of the first sessions: `assign-task` (plain operational instruction),
`provide-resource` (pasting external material in), and `audit-artifact`
(checking that records and outputs actually exist as claimed). The coding agents
proposed nine further codes. Three of those (`system-notification`,
`system-artifact`, `monitor-background-job`) describe machine turns and became
the data-cleaning rule above. The remaining six (`report-progress`,
`drive-tooling-pipeline`, `import-external-pattern`, `withhold-go-ahead`,
`request-handoff`) were judged real but subsumable: they are recorded here as
facets of existing codes (operating the literature pipeline by hand under
`assign-task`/`provide-resource`; importing the plan-system pattern from another
repository under `supply-domain-judgment`; information-only probes under
`audit-artifact`; session handoffs under `assign-task`) and the frequencies were
not recoded. The handoff facet recurs often enough to appear in pattern 5.

Human-side codes and frequencies (599 turns; a turn carries up to three codes,
so assignments exceed turns):

| code | definition (abbreviated) | assignments | dominant |
|---|---|---|---|
| assign-task | operational instruction to do work | 224 | 146 |
| set-standard | imposes or tightens a process rule (preregistration, citation discipline, verification gates, decision logging) | 136 | 64 |
| scope-decision | rules work in or out of the paper; splits scope | 103 | 39 |
| pose-question | organizing or reframing question that sets the agenda | 81 | 47 |
| redirect-priority | reorders the plan; moves the session to a different target | 80 | 43 |
| supply-domain-judgment | contributes field knowledge: literature leads, methods, venue, referee expectations | 80 | 26 |
| ratify | substantive approval of a proposed option or result | 71 | 60 |
| audit-artifact | checks the records or outputs (saved? committed? actually run?) | 67 | 47 |
| catch-gap | spots something missing or wrong the AI did not flag | 61 | 34 |
| provide-resource | pastes external material into the session | 51 | 35 |
| challenge-derivation | disputes or stress-tests a mathematical claim or result | 45 | 25 |
| challenge-framing | disputes positioning, novelty, or narrative framing | 41 | 18 |
| reject-prose-style | rejects prose, voice, punctuation, or structure | 25 | 15 |

AI-initiated moves, observed in the assistant-context tails only (a deliberate
undercount; the tails are 600 characters):

| code | definition | observed |
|---|---|---|
| flag-risk | flagged a risk, limitation, or potential error unprompted | 68 |
| surface-decision | put a decision to the human instead of deciding silently | 63 |
| propose-options | laid out alternatives with trade-offs for the human to choose | 44 |

## 5. The heuristic: five patterns

The patterns below are the summary S3-P2 states. Each is named, counted, and
anchored to verified episodes (Section 6, cited by id).

**Pattern 1 — standards before steps.** The single most frequent move is a plain
work assignment (224 assignments), but the densest block of non-tasking activity
is rule-setting: 136 set-standard assignments plus 67 audit-artifact checks that
the rules were actually followed. The standards came early and got tighter:
preregistration must be committed and pushed before code (E01), simulation may
not run before explicit sign-off (E02), every invoked source needs its equation
or line number (E03), analytic claims need an independent model lineage at high
reasoning effort with a 24-hour timeout (E04). Organizing questions were the
usual vehicle for new standards (81 pose-question assignments): "What would a
skeptical reviewer want?" produced the self-contained lemma rule (E05), and "How
much of a pain ... to formalize the proof ... using software?" produced the
executable symbolic appendix (E06).

**Pattern 2 — proposal, ratification, record.** The assistant surfaced choices
(63 surface-decision, 44 propose-options observed); the human ratified
explicitly (71 ratify assignments) and the ratification was written down with
date, rejected options, and rationale (decisions D-01..D-13 and style rules
T-01..T-07 in `manuscript/plan/decisions.md`). Ratifications were specific, not
rubber stamps: D-09 was ratified with an instruction to amend the level-1 plan
in the same breath (E07), and the AI-proposed dissimilar-pair check was ratified
and preregistered before its code existed (E08).

**Pattern 3 — challenge in both directions.** Human challenge-class moves
(challenge-derivation 45, challenge-framing 41, catch-gap 61,
reject-prose-style 25; 172 assignments in all) are the part of the record the
manuscript's one-line role statement compresses most. The human author caught a
circular definition in the derivation's information matrices (E09), stress-tested
a Type I claim against its own numbers (E10), caught that the cited EM-based
results concern improper imputation while the paper's subject is proper
imputation (E11), and rejected the AI's prose register repeatedly, from house
jargon (E12) to punctuation (E13). In the other direction the assistant flagged
risks unprompted 68 times, and the protocol the human imposed did the largest
reverse catch mechanically: eight of nine blind re-derivations by an independent
model returned the opposite sign of the main theorem, exposing a silent
conditioning substitution, and the fix was ratified by the human in one line
(E14). Accountability also ran from human to protocol: "So did we never actually
call Chat gpt-5.5?" exposed an under-application of the cross-model rule and
launched the missing check within minutes (E15).

**Pattern 4 — domain knowledge entered from the human side.** 80
supply-domain-judgment and 51 provide-resource assignments. The Shimodaira
precedent that re-anchored the novelty claim came from the human author's memory
of another project's database (E16). The equipercentile-equating idea that
became calibration-ladder rung 3 came from the human author's psychometrics
background (E17). The Wolfram-client library that enabled the second
computer-algebra system was a pasted link (E18). The FIML marginalization
cross-check in the first witness study was the human author's proposal (E19).

**Pattern 5 — scope and continuity managed deliberately.** 103 scope-decision
and 80 redirect-priority assignments. Scope was cut in writing: the MVN running
example kept "in control" pending referee pushback, the information-criterion
calibration ladder split to a sequel and partially recalled later (E20), an
entire candidate expansion demoted to conjecture pending a fresh-session
reconciliation (E21). Work was deliberately partitioned across sessions with
written handoffs, the todo/0xx files, so that no single context window carried a
load-bearing thread alone (E22).

## 6. Verified episodes

Each episode below passed two checks: the quote is verbatim from the extracted
turn (typos preserved; ellipses mark omissions; line breaks normalized to
spaces), and the named artifact exists with consistent content and timing in
`decisions.md`, the git history, or the repository. Verification was by
independent agents for all episodes except E04, E11, E13, E20, and E23, which
were verified the same way by the consolidating session (marked †). Artifacts
give local commit times where minutes matter. The full 58-episode table with
per-episode assessments is
`verification/cache/collab-analysis/final-episodes.json`.

| id | date | session | code | quote (verbatim) | artifact |
|---|---|---|---|---|---|
| E01 | 2026-05-23 | c691d23e | set-standard | "You need to write these in a markdown and commit and push for them to be preregistered" | commit `ddc9037` (todo/004 preregistration, ~4 min later) |
| E02 | 2026-05-23 | cc106375 | set-standard | "CRITICAL FIRST STEP: confirm with me that I have signed off on todo/005. ... Do not run the sweep until I explicitly conf[irm]" | todo/005 §4 dated sign-off, commit `5592d52` |
| E03 | 2026-05-24 | 9436d7e4 | set-standard | "NOw it isn't enough to just cite the reference. You need to provide equations from the reference that you are invoking." | commit `33c418b` (verbatim-source appendix + equation numbers, same day) |
| E04† | 2026-06-02 | 29059e85 | set-standard | "If we are going to do any analytic derivations, I really want chat GPT 5.5 as an indepdnent and I want xhigh reasoning, with a very long time out (24 hours)" | commit `07b021c` (cross-model protocol baked into todo/020, 3 min later) |
| E05 | 2026-05-25 | dc9724ea | pose-question | "What would a skeptical reviewer want?" | commit `40ed6dc` (A4 pointer replaced by self-contained lemma, ~28 min later) |
| E06 | 2026-05-23 | cc106375 | pose-question | "How much of a pain in the ass would it be to formalize the proof the central theorem we have here using software in mathematics ?" | commit `fe31a8a` (Sympy verification + todo/007, 38 min later) |
| E07 | 2026-06-06 | 1877b2af | ratify | "Yes that matches my intent, record D-09 and amend level 1" | commit `fb863ad` (D-09 row + level-1 amendment, 3 min later) |
| E08 | 2026-06-05 | 972eb380 | ratify | "Agree a dissimilar pair makes sense" | commit `39cfc38` (todo/029 Amendment 2 preregistered before code, ~5 min later) |
| E09 | 2026-05-24 | 9436d7e4 | challenge-derivation | "Why in D5 are you invoking Q^bar when defining the complete data likelihood? Y not just \scriptl(\theta\|Y)?" | commit `1de7f40` (D5/D6 redefined as plain Fisher informations) |
| E10 | 2026-05-23 | c691d23e | challenge-derivation | "If C2 was .03 and C4 was .04 for the type 1 error, help me make sense of this statement the bias-corrected MI LRT controls Type I more precisely" | commit `40e7dac` (claim reframed as M-dependent calibration + size-adjusted power) |
| E11† | 2026-06-07 | 35b5e1cf | catch-gap | "Why do you never invoke proper imputation. Sure Monte Carlo em is multiple imputation but it isn’t proper. ... they don’t touch proper imputations like we do" | commit `f1126db` (S2 proper-imputation paragraph, 5 min later) |
| E12 | 2026-05-25 | dc9724ea | reject-prose-style | "still is not outside reader friendly. First there are some words that a theoretical statistician would never use like \"ledge\" or \"numerical witness\"" | commit `1b4ba7e` (de-jargon + roadmap restructure; later codified as T-03) |
| E13† | 2026-06-07 | 35b5e1cf | reject-prose-style | "Why so many semicolons dashes and colons? Again. Write like a high shooler" | commit `00f666d` (S3 punctuation rewrite + CLAUDE.md budget rule, 1 min later) |
| E14 | 2026-06-02 | b27ba43d | ratify | "Yes, please fix D9" | commit `6bc7206` (fitted-vs-oracle ambiguity fixed; body cites 8/9 blind re-derivations on −½, 9 min later) |
| E15 | 2026-06-02 | 5ee18e70 | audit-artifact | "So did we never actually call Chat gpt-5.5?" | commit `17ba403` (concedes "under-application of the protocol", launches blind GPT-5.5 check, 7 min later) |
| E16 | 2026-06-01 | 424fd178 | supply-domain-judgment | "I think Shimodaira is in MI-IC project, you can see in our database" | commit `a2dc3f6` (Shimodaira–Maeda 2017 + Shimodaira 2000 acquired, ~3 h later) |
| E17 | 2026-06-04 | c7fe11b9 | supply-domain-judgment | "we want o do equipercentile equating here contrast first and second moment with \"all moment matching\" with the reference distribution" | commit `1614169` (todo/026 rev 2: ladder rungs 1–3 in-paper, ~13 min later) |
| E18 | 2026-06-02 | 336e846b | provide-resource | "I believe there is a wolfram client library for python: https://reference.wolfram.com/language/WolframClientForPython/" | commit `3977bdd` (verification/cas-wolfram/ via wolframclient, ~32 min later) |
| E19 | 2026-05-23 | c691d23e | supply-domain-judgment | "get the fiml estimates and marginalize across Ymiss from the FIML estimate? I believe the derivation accommodates that" | commit `d9404ba` (FIML-marginalized analytic cross-check in W1, ~11 min later) |
| E20† | 2026-06-04 | ea505749 | scope-decision | "This seems like a follow up paper. Maybe we just focus on the bias correction and LRT for this paper?" | D-06 (decisions.md, 2026-06-04) + commit `0777aa3` (scope split) |
| E21 | 2026-06-02 | b27ba43d | scope-decision | "Let’s consider chat’s findings conjectures that need reconciling and evidence, which we’ll do in a new session" | commit `2ee1f23` (GPT findings logged as conjectures + handoff, ~3 min later) |
| E22 | 2026-06-01 | 131f54f1 | assign-task | "Go ahead an make a markdown that I can bring to a new session." | todo/012-next-session.md (commit `874f7e8`, ~14 min later) |
| E23† | 2026-05-23 | 1659f932 | challenge-framing | "It may mean we need to perhaps look away \"we are doing this as a chi-squared test\" and towards the deviance is used in lots of thing: model fit statitics, information critieria, and so we better have an unbiased estiamte of the complete data log deviance. Thoughts?" | D-01 (decisions.md, dated 2026-05-22; turn is 2026-05-22 19:48 local) — the reframing pivot |
| E24 | 2026-05-25 | 63b28d6e | challenge-framing | "The format still has a subtle posture of “I’m entitled to your trust because I have earned my membership to this community.” I’m thinking we need to rewrite in a IMRAD format" | D-09 (IMRaD with Methods-as-workflow; ratified 2026-06-05) |
| E25 | 2026-06-01 | 8e25a96f | audit-artifact | "Where is this report saved? or is it?" | verification/cache/derivation-audit-2026-06-01.md (header records the requested 17:44 timestamp) |

## 7. The provenance question

Objective 3 of todo/032 asks which substantive content traces to a human
intervention and which to AI proposal. The episode table supports the following
attributions; anything not listed should be presumed AI-produced and
human-gated, which is the default division of labor.

Traceable to a human intervention: the deviance-bias reframing direction after
the Chan (2022) discovery (E23 → D-01); the IMRaD structure with Methods as
workflow (E24 → D-09); the Shimodaira positioning that re-scoped the novelty
claim (E16); the equipercentile-equating mechanism of calibration-ladder rung 3
(E17); the FIML cross-check engine in W1 (E19); the Satorra–Bentler arm and the
bug report that became repository issue #1; the proper-versus-improper
imputation distinction in the Background (E11); the second computer-algebra
system (E18); and the verification regime itself, preregistration-before-code,
sign-off gates, source-equation provenance, cross-model adversarial review
(E01–E04), which is a contribution of method rather than mathematics.

Traceable to AI proposal with human ratification: the dissimilar-pair
preregistration amendment (E08); the D9 fitted-vs-oracle repair, where the
apparatus the human mandated produced the catch and the human ratified the fix
(E14); and the derivations, drafts, and computations throughout, which were
AI-produced and entered the record only through the gates above.

## 8. Reproduction

```
py scripts/collab_extract_turns.py     # Phase A inventory from the transcript archive
py scripts/collab_consolidate.py       # frequency tables from the committed coded outputs
py scripts/collab_deposit_prep.py      # deposit manifest + sensitive-content scan
```

Committed primary data: `verification/cache/collab-analysis/coded/` (34 files,
per-turn codes), `clean-tally.json` (frequencies), `final-episodes.json`
(verified episode table), `inventory-summary.json` (Phase A accounting),
`workflow-result.json` (orchestration record: 95 agents, 34 coders + episode
verifiers). The `turns/` directory regenerates deterministically from the
transcript archive via the extractor. Phase B coding is AI judgment and does not
regenerate deterministically; the committed coded outputs are the data of
record.

## 9. Limitations

The coding was performed by the same model lineage being analyzed, with no human
second coder and no inter-rater reliability measurement. The frequencies are
therefore model judgments. What is verified is narrower: the corpus accounting,
the verbatim quotes, the artifact existence and timing for every episode used,
and the arithmetic. The AI-side counts are undercounts by construction, since
coders saw only message tails. The trivial-turn filter removed 67 bare
approvals, so `ratify` understates total human assent. Episode selection
favored turns with nameable artifacts, which biases the table toward decisive
moments and away from routine supervision. A reader who wants the unselected
record has it: the transcripts themselves enter the public archive under D-13.
