# Workflow-vocabulary softening proposal (todo/035 follow-up, for Marcus's review)

From `scripts/corpus_vocab_check.py`. The T-03 banned scan is **clean (0 hits)**.
What remains is the engineering-metaphor family — words in the same spirit as the
T-03 bans, heavily over-represented vs the 61 source papers and mostly **absent
from them entirely**. Nothing here is wrong; the question is whether it reads like
a statistics paper to an AI-skeptical referee. Grouped by priority. **None applied
— this is a menu.**

## Priority 1 — leaks into the technical sections (S4-S6) + the positioning verb

These are where un-stats-like vocabulary appears *outside* the workflow sections.

| where | current | suggested |
|---|---|---|
| S4-P11 | "the design **sits** near the invariance case" | "the design **lies** near" / "is near" |
| S4-P8 | "the applications therefore **sit** in the estimated-scale regime" | "therefore **fall** in" / "are in" |
| S4-P17 | "happens to **sit** at the exact equality case" | "happens to **fall** at" / "to be" |
| S1-P6 | "These results **sit** upstream ... routes **sit** nearby" | "**stand** upstream" / "**lie** nearby" |
| S5 (×8: P12/P14/P15/P17/P21/P6) | "**sits** 1.3 standard errors away", "**sits** at 0.042", "**sits** near nominal" | "**lies** N se away" / "**is** at 0.042" / "**is** near nominal" |
| S4-P15 | "The cross-model **gate** of @sec-methods" | "The cross-model **check**" |
| S4-P1 / S5-P1 | "the four **tier** labels", "the *measured* **tier**" | "the four **grades**", "the *measured* **grade**" |
| S4-P10/19/21, S5-P3/11/12 | "**graded** in @sec-simulations", "**graded** against pass criteria" | "**assessed** in", "**checked** against pass criteria" |

## Priority 2 — the Methods/AI-collab sections (S3, S1B): defensible but dense

Here the words describe the actual verification process, so they are closest to
literal. Softening is optional; if kept, the density is the main tell.

| where | current | suggested (if softening) |
|---|---|---|
| S3-P1, S3-P4 | "a verification **pipeline**", "The claim **pipeline**" | "a verification **sequence**", "The chain of checks" |
| S3-P1, S3-P4, S3-P8 | "trust **tiers**", "a **tier** label" | "trust **grades**", "a **grade** label" |
| S3-P4, S3-P6, S1-P6b | "the **gates** they cleared", "what this **gate** catches", "**gates** the reader can check" | "the **checks** they passed", "what this **check** catches", "**checks** the reader can run" |
| S3-P3, S3-P4 | "**pinned** to a source document", "not **pinned** in closed form" | "**traced** to a source document", "not **established** in closed form" |
| S3-P6 | "a single model **lineage**", "an independent **lineage**", "Independent **lineages**" | "a single model **family**", "an independent **model**", "Independent **models**" |
| S3-P1, S3-P6 | "**grading** sheets", "**grading** records" | "**scoring** records" / "assessment records" |
| S1-P6b, S3-P1 | "**sourced** citations" | "**source-checked** citations" / "documented citations" |

## Leave as-is (false positives / fine)

- **scope / scoped** — standard academic usage ("beyond their scope", "scoped to
  the designs studied"). Not jargon. No change.
- **transcripts** (S1B-P2) — literal and factual (session transcripts). Fine.
- The technical over-represented words (trace, differential, bias, deviance,
  naive, numerator, criterion, ...) — these ARE the contribution. Expected.

## Note

`grading`/`tier`/`graded` are the trust-grade scheme (firm / measured / structural
/ conjecture). If you rename "tier" → "grade", do it consistently across S3 (where
it is defined) and the S4/S5 labels that reference it, or leave all of them.
