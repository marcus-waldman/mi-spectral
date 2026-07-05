# Sweep batch 5 proposal: S5 Simulation studies (D-26 register, for Marcus's gate)

**Date: 2026-07-05. GATE DOCUMENT — nothing applied until Marcus approves.** Same
protocol as batches 1–4. S5 is the vocabulary-dense section: this batch clears all 16
remaining S5 vocabulary warnings, converts the "Perfect is ..." caption convention to
register syntax per D-26 (the convention itself — every exhibit names its reference —
stays; the uniform replacement is "The reference is ..."), lands the ratified Demo 5 at
S5-P18, the authorized E3 thin at S5-P16, borderline #8 at S5-P20, and the
@fig-w4-nonnested escaping normalization (incidental catch #2). Every number in every
design, result, caption, and table is untouched.

## Caption convention (uniform, 10 instances)

| unit | old | new |
|---|---|---|
| S5-P1 | "because each one names the perfect reference and the value the study achieved" | "because each one names its reference value and the value the study achieved" |
| S5-P12 | "Perfect is the analytic target, the dotted line at the preregistered half-trace $2.77$ and the shaded band at the order-one-augmented prediction $2.42$ to $2.55$." | "The analytic target is the reference: the dotted line marks the preregistered half-trace $2.77$, and the shaded band marks the order-one-augmented prediction $2.42$ to $2.55$." |
| S5-P13 | "Perfect is the pair of analytic targets." | "The reference is the pair of analytic targets." |
| S5-P14 | "Perfect is the nominal $0.05$ line." | "The reference is the nominal $0.05$ line." |
| S5-P15 | "Perfect is the projected-trace prediction" | "The reference is the projected-trace prediction" |
| S5-P16 | "Perfect is a flat line at order one." | "The reference is a flat line at order one." |
| S5-P17 | "Perfect is the complete-data benchmark, the dashed line and the black bar." | "The reference is the complete-data benchmark, the dashed line and the black bar." |
| S5-P18 | "Perfect is the complete-data benchmark, the dashed line above each cell." | "The reference is the complete-data benchmark, the dashed line above each cell." |
| S5-P19 | "Perfect is zero, approached by" | "The reference is zero, approached by" |
| S5-P21 | "Perfect for the twin is zero, and" / "Perfect is no effect, the line at zero." | "The twin's reference is zero, and" / "The reference is no effect, the line at zero." |

The S5-P20 table header "| Structural limit | perfect | achieved |" becomes
"| Structural limit | reference | achieved |", and its caption's "an exact structural
prediction" becomes "a structural prediction" (borderline #8, authorized).

## Vocabulary and formula repairs

| unit | old | new |
|---|---|---|
| S5-P4 | "sits between" (3×) | "lies between" (3×) |
| S5-P7 | "the run passes if the data land on the projected-trace value" | "the run passes if the data agree with the projected-trace value" |
| S5-P9 | "The headline cell is non-monotone missing-at-random" | "The primary cell is non-monotone missing-at-random" |
| S5-P10 | "the third is a junk design at $0$ where the truth is diagonal" | "the third is a no-signal design at $0$ where the truth is diagonal" |
| S5-P11 | "for genuinely separated candidates" | "for candidates separated at $O(1)$" (the literal content) |
| S5-P11 | "The pre-registered similar-pair headline is assessed honestly" | "The pre-registered similar-pair prediction is assessed honestly" |
| S5-P12 | "One cell is a genuine miss, because" | "One cell departs from the prediction, because" |
| S5-P16 | "This is exactly the failure mode the result specifies." | "This is the failure mode the result specifies." — **E3 thin, authorized (qmd :446)** |
| S5-P19 | "Two internal measurements show why the ladder works" | "Two internal measurements show why the ladder succeeds" |
| S5-P21 | "and the pre-registered headline for the similar pair stays below resolution" | "and the pre-registered prediction for the similar pair stays below resolution" |
| S5-P21 | "A pilot's apparent value of $-2$ dissolved in the full run. We report that failure as the discipline requires." | "A pilot's apparent value of $-2$ did not persist in the full run, a failure we report as the pre-registration requires." |
| S5-P21 | the caption's `width=\"100%\"` (escaped backslashes, unlike every other figure) | `width="100%"` — **incidental catch #2, authorized** |
| S5-P22 | "This robustness is empirical and scoped to the designs studied." | "This robustness is empirical and restricted to the designs studied." |

## S5-P18 — ratified Demo 5 (three substring replacements)

1. The opening two sentences become Demo 5's proposed single sentence ("...wherever the
   errors come from choosing too rich a model, while a residual shortfall remains where
   selection is hard even with complete data (@fig-ladder)").
2. The @tbl-ladder row label "$\rho = 0$ (junk)" becomes "$\rho = 0$ (no signal)" —
   every number in the row untouched.
3. The interpretation paragraph becomes Demo 5's proposed text verbatim ("The
   zero-correlation cell removes $90$ percent of the difference...", "We read that
   shortfall as a limit of the information in the data rather than as a calibration
   error, an interpretation the calibration checks below support...").

Invariance: as certified in Demo 5 (all ten numbers, all hedges, the
measurement-not-theorem close).

## NO CHANGE (5 units)

S5-P2 (apparatus), S5-P3 (assessment and registration), S5-P5, S5-P6, S5-P8 (the
known-scale/sign-regime, likelihood-ratio, and pairing designs — no flags; the singular
"sign-regime" design name stays per D-26).

## Gate

Approve / amend per unit. On approval: atomic script → check_plan → rebuild → render →
scouts. Expected vocabulary-gate movement: all 16 S5 warnings clear (26 → 10, leaving
only S6 for the final batch).
