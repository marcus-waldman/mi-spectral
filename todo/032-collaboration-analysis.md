# todo/032 — Qualitative analysis of the collaboration record (for S3-P2)

**Status:** open (handoff). Created 2026-06-07.
**Blocks:** the final form of S3-P2 (Methods, "Roles and decision records").
**Decided in-chat 2026-06-07:** S3-P2 must characterize the collaboration by a
heuristic derived from the actual working record, then illustrate with examples —
not lead with whatever examples the drafting session happens to remember. The
evidence exists: the full session-transcript archive.

## Objective

Produce a committed analysis document that answers, with evidence:

1. What did "direction" by the human author actually consist of, across the whole
   project? (A taxonomy of intervention types with frequencies, not a vibe.)
2. What did the challenge dynamic look like in both directions? (Human challenges
   AI output; AI surfaces options/decisions for human ratification; what each
   party caught that the other missed.)
3. Which substantive content of the paper traces to a human intervention, and
   which to AI proposal? (The provenance question a skeptical referee will ask.)

The deliverable feeds S3-P2: a heuristic statement of the collaboration pattern
(3-6 named patterns), each backed by counted occurrences and 1-2 dated episodes.

## Data

- `C:\Users\marcu\.claude\projects\C--Users-marcu-git-repositories-mi-spectral\*.jsonl`
  — 35 session transcripts, ~85 MB, 2026-05-22 through 2026-06-07 (project
  inception to present). JSONL message streams; user turns are Marcus verbatim.
- Cross-validation sources: `manuscript/plan/decisions.md` (D-01..D-12, T-01..T-07,
  each with rejected options), `todo/0xx` files (preregistrations + amendments),
  `IDEAS.md`, git log (dated commits tie episodes to artifacts).

## Method (qualitative coding, lightweight but disciplined)

- **Phase A — inventory.** Parse the JSONLs. Extract every user turn with session
  id + timestamp. Drop trivial turns (bare "yes", "ok", "continue"). Expect a few
  hundred substantive interventions.
- **Phase B — open coding.** Code each intervention. Seed codes (revise freely):
  `pose-question` (organizing questions, e.g. what should "settled" mean),
  `challenge-derivation`, `challenge-framing`, `catch-gap` (e.g. proper imputation
  absent), `reject-prose/style`, `set-standard` (verification gates, typing rule,
  preregistration), `scope-decision`, `ratify`, `redirect-priority`,
  `supply-domain-judgment` (venue, literature, what is publishable). Note
  AI-initiated counterparts: `surface-decision`, `flag-risk`, `propose-options`.
- **Phase C — consolidate.** Frequencies per code; 1-2 representative episodes per
  major code, each with date, session id, a short verbatim quote, and the artifact
  it produced (commit / decision id / manuscript content). Each episode must be
  cross-validated against decisions.md or git before use.
- **Phase D — synthesize.** Write the heuristic (3-6 named collaboration patterns)
  and the revised S3-P2 from it. The analysis doc is committed (suggested:
  `verification/collaboration-analysis.md`) and S3-P2 cites it with a `verif:`
  pointer, like any other quantitative claim in the paper.

Practical notes for the executing session: the parser is ~30 lines of Python
(read JSONL, keep `type == "user"` text turns); code in batches by session, oldest
first, since the early sessions carry the reframing-era decisions; sessions on
2026-06-01 (8 files) and 2026-06-04..06 are the densest. Parallel per-session
coding by subagents is sensible IF Marcus opts into a workflow; otherwise
sequential is fine across 2-3 sittings, recording progress in this file.

## Open questions for Marcus (answer before or during execution)

1. Do the raw transcripts enter the public record (JAIGP provenance maximalism),
   or does only the committed analysis? (Candidate decision D-13. Transcripts may
   contain material not intended for publication; the analysis quotes selectively
   either way.)
2. Does the analysis cover only mi-spectral, or also the MI-IC sessions where the
   replication-principle terminology originated?

## Current state of S3-P2

Drafted at `00f666d` with an expanded collaboration account, but its two examples
(replication principle, proper-imputation catch) are both from the 2026-06-06/07
sessions — recency-sampled, the exact defect this analysis fixes. P2 is flagged
`awaiting_collaboration_analysis` in level3-paragraphs.json and keeps its current
text as placeholder until Phase D rewrites it.
