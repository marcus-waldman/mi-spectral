# Sweep batch 6 proposal: S6 Discussion (D-26 register, for Marcus's gate — final section batch)

**Date: 2026-07-05. GATE DOCUMENT — nothing applied until Marcus approves.** Same
protocol as batches 1–5. This batch clears the last 10 vocabulary warnings, lands the
ratified Demo 6 at S6-P1 **with the authorized incidental content fix (the stale "six
specific limits" becomes "nine": the Discussion runs G1–G9)**, retires the three
remaining "The practical recommendation/summary" formulas in the register's advice voice,
and keeps both D-26 signature sentences ("Corrected criteria are honest, not
clairvoyant." already landed in S1; "the data no longer say" stays here).

## S6-P1 — ratified Demo 6, with the count fix

Demo 6's proposed text verbatim, except "six specific limits remain" → "nine specific
limits remain" (incidental catch #1, authorized in D-26; Demo 6 had preserved "six"
under style-pass invariance and flagged it). Every other fact, number, hedge, and the
@mengMultipleImputationInferencesUncongenial1994a citation as certified in the demo.

## Surgical repairs (old → new)

| unit | old | new |
|---|---|---|
| S6-P3 (G3) | "Imputation-engine robustness is empirical and scoped, which qualifies" | "Imputation-engine robustness is empirical and restricted in scope, which qualifies" |
| S6-P3 (G4) | "The weak-signal floor is a measurement, not an impossibility proof" | "The weak-signal shortfall is a measurement, not an impossibility proof" (consistent with the S5 rename) |
| S6-P4b (G7) | "The practical recommendation is to diagnose congeniality before trusting bias-corrected selection." | "In practice it is wise to diagnose congeniality before trusting bias-corrected selection." |
| S6-P4c (G8) | "BIC already sits close to the complete-data benchmark" | "BIC is already close to the complete-data benchmark" |
| S6-P4c (G8) | "The practical recommendation is to expect the correction to matter most for BIC where its own penalty has not yet reached that regime, and to read any BIC-based comparison at a small sample with that limit in mind." | "In practice the correction should be expected to matter most for BIC where its own penalty has not yet reached that regime, and any BIC-based comparison at a small sample should be read with that limit in mind." |
| S6-P4d (G9) | "so the plug-in lands on the general $+\tfrac12$ trace value plus a base-measure term" | "so the plug-in bias is the general $+\tfrac12$ trace value plus a base-measure term" |
| S6-P4d (G9) | "lands at $+0.11\pm0.03$ against its derived $+0.10$" | "measures $+0.11\pm0.03$ against its derived $+0.10$" (matching the Student-t sentence's verb) |
| S6-P4d (G9) | "Membership in the two regimes is decided by" | "Membership in the two cases is decided by" |
| S6-P5 | "One question is left as a conjecture. We label it as one. We conjecture that the bias-corrected likelihood-ratio comparison dominates its uncorrected counterpart in power uniformly. The preregistered likelihood-ratio study's power arms provide partial support (@sec-simulations). We state no theorem." | "One question is left as a conjecture, and we label it as one. We conjecture that the bias-corrected likelihood-ratio comparison dominates its uncorrected counterpart in power uniformly; the preregistered likelihood-ratio study's power arms provide partial support (@sec-simulations), but we state no theorem." |
| S6-P6 | "Running the headline studies under data augmentation" | "Running the main studies under data augmentation" |
| S6-P7 | "one model genuinely fits better" | "one model truly fits better" (matching S1-P5's landed wording) |
| S6-P7 | "The practical summary for an applied reader is short. Correct the criterion, or match its null distribution. Then trust the result the way complete-data results are trusted, subject to the stated conditions." | "In practical terms the advice is short: correct the criterion, or match its null distribution, and then trust the result the way complete-data results are trusted, subject to the stated conditions." |
| S6-P8 | "two preregistered headlines were given up rather than rescued" | "two preregistered predictions were given up rather than salvaged" |

Notes: "There, the honest answer is that the data no longer say." (S6-P7) is KEPT
verbatim — the second D-26 signature sentence. G9's "the estimated-scale regime"-style
singulars stay. The S6-P8 "headlines" plural escaped the WARN gate (the pattern is
singular-only) — the closing commit extends the pattern to `\bheadlines?\b` when
flipping the gate fatal.

## NO CHANGE (3 units)

S6-P2 (G1 — its "exact MCAR vanishing" is the addendum's best-guarded E1 instance),
S6-P4 (G5/G6), S6-P7b (applied-practice implications — conformant).

## Gate

Approve / amend per unit. On approval: atomic script → check_plan → rebuild → render →
scouts. Expected: all 10 remaining warnings clear (10 → 0). Then the closing step —
whole-document consistency read, flip `VOCAB_GATE_FATAL = True` (with the plural fix),
rerun `corpus_vocab_check.py` + `style_register_stats.py` as the exit measurement, one
final commit.
