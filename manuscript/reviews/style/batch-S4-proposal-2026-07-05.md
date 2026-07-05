# Sweep batch 4 proposal: S4 Derivations (D-26 register, for Marcus's gate)

**Date: 2026-07-05. GATE DOCUMENT — nothing applied until Marcus approves.** Same
protocol as batches 1–3. S4's proof prose graded well in Phase B (the theorem rhythm,
the "delicate half", the warning paragraphs all conform), so outside the one ratified
demo this batch is surgical: the retired-formula family ("prices" 3×, bare "This result
is firm." 3×, "The practical reading is direct.", "worth naming"), the Bucket-2 narration
verbs ("close/closes this part/theorem"), the two "regimes" plurals, the authorized R11
rescope #5 and E3 thin, and the "buys three things" commerce verb. Every display,
proposition statement, and proof step is untouched.

## Surgical repairs (old → new, each a unique-substring replacement)

| unit | old | new |
|---|---|---|
| S4-P1 | "This section delivers the paper's analytic results" | "This section presents the paper's analytic results" |
| S4-P1 | "It prices the bias of the averaged log-likelihood to leading order" | "It quantifies the bias of the averaged log-likelihood to leading order" |
| S4-P4 | "The two regimes are distinguished experimentally" | "The two cases are distinguished experimentally" |
| S4-P5 | "Seven regularity conditions are in force, and none is exotic." | "Seven regularity conditions are in force, and all are standard." |
| S4-P6 | "One trap is worth naming. Substituting ... produces a spurious $-\tfrac12 q$. We display @eq-vargap to forestall it." | "One trap deserves note: substituting ... produces a spurious $-\tfrac12 q$, and we display @eq-vargap to forestall it." |
| S4-P8 | "Two checks close the theorem" | "Two checks complete the theorem" |
| S4-P8 | "The two arms differ by exactly the posterior-draw imputation variance" | "The two arms differ, to leading order, by the posterior-draw imputation variance" — **R11 rescope #5, authorized** |
| S4-P9 | "The theorem prices one model's bias." | "The theorem quantifies one model's bias." |
| S4-P10 | "This result is firm. The metric is its substance." | "This result is firm, and the metric is its substance." |
| S4-P11 | "This result is firm. The proof is one matrix inequality." | "This result is firm, and the proof is one matrix inequality." |
| S4-P11 | "The practical reading is direct. Correcting an MI deviance comparison by the difference of the two models' own traces over-corrects at the null. This happens whenever the tested directions mix unequally-missing information." | "In practical terms, correcting an MI deviance comparison by the difference of the two models' own traces over-corrects at the null whenever the tested directions mix unequally-missing information." |
| S4-P11 | "Both regimes are exhibited in @sec-simulations." | "Both cases are exhibited in @sec-simulations." |
| S4-P12 | "This result is firm. The mechanism is exact cancellation" | "This result is firm, and the mechanism is exact cancellation" |
| S4-P14 | "matters instead exactly where no reference distribution stands" | "matters instead where no reference distribution stands" — **E3 thin, authorized (qmd :352)** |
| S4-P15 | "A scope statement closes this part." | "A scope statement concludes this part." |
| S4-P18 | "The residual matters. A correctly centered criterion can still select worse than complete-data AIC. The reason is the subject of the rest of this part." | "The residual matters, because a correctly centered criterion can still select worse than complete-data AIC, and the reason is the subject of the rest of this part." |
| S4-P19 | "and yet it buys three things" | "and yet it yields three things" |
| S4-P22 | "Two structural limits close this part." | "Two structural limits conclude this part." |

Notes: S4-P8's "the estimated-scale regime" (singular) stays — the gate and D-26 ban only
the plural; the singular also survives in S5's sign-regime design name. The E1 "exact"
instances throughout S4 (the closed form @eq-gap, "zero exactly when $H_{12}=0$",
"reproduces exactly the naive difference", "exact cancellation of realizations",
"$\hat d_k = N[\ldots]$ exactly") all KEEP per the adopted addendum.

## S4-P16 — ratified Demo 4, verbatim (full replacement)

As certified in `demonstrations-2026-07-05.md`, Demo 4: the part-opener moves to "where
no reference distribution stands between the statistic and its use" (the manuscript's own
S4-P14 phrase, an intentional pickup across the two adjacent parts), "lands directly in
the ranking" → "enters the ranking directly" (this clears the S4-P16 vocabulary warning),
"the anatomy" → "the decomposition of the bias", the display lead-in becomes "The
corrected criterion is", and the Shimodaira/Cavanaugh sentences join by semicolon.
Borderline #7 ("by exactly that surplus") is KEPT per D-26 — the antecedent is the
already-scoped leading term.

## NO CHANGE (8 units)

S4-P2, S4-P3 (setup and RIV instantiation — register-shaped; "changes every constant
below" is the model warning form), S4-P7, S4-P7b (the imputation-bias derivation — "the
delicate half" is R4-attested), S4-P13 (@prp-ac-diff), S4-P17, S4-P20, S4-P21 (the maps
and pre-registration paragraphs — conformant).

## Gate

Approve / amend per unit. On approval: atomic script → check_plan → rebuild → render →
scouts. Expected vocabulary-gate movement: the S4-P4, S4-P11, and S4-P16 warnings clear
(29 → 26).
