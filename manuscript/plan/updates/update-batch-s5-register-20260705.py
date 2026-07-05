# Sweep batch 5: S5 Simulation studies to the D-26 register (todo/048 Phase D(ii)).
#
# Gate: Marcus approved manuscript/reviews/style/batch-S5-proposal-2026-07-05.md
# ("Approved", 2026-07-05). Clears all 16 S5 vocabulary warnings; converts the
# "Perfect is ..." caption convention to "The reference is ..." (convention kept,
# syntax registered, per D-26); ratified Demo 5 at S5-P18 (three substrings incl.
# the (junk) table label); authorized E3 thin at S5-P16; borderline #8 at S5-P20;
# fig-w4-nonnested escaping normalization (incidental catch #2). Every number in
# every design, result, caption, and table untouched.
# Guards: unique-substring asserts; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

SUBS = [
    # ---- caption convention: "Perfect is" -> "The reference is" (10 instances) ----
    ("S5-P1",
     "names the perfect reference and the value the study achieved",
     "names its reference value and the value the study achieved"),
    ("S5-P12",
     "Perfect is the analytic target, the dotted line at the preregistered half-trace "
     "$2.77$ and the shaded band at the order-one-augmented prediction $2.42$ to "
     "$2.55$.",
     "The analytic target is the reference: the dotted line marks the preregistered "
     "half-trace $2.77$, and the shaded band marks the order-one-augmented prediction "
     "$2.42$ to $2.55$."),
    ("S5-P13",
     "Perfect is the pair of analytic targets.",
     "The reference is the pair of analytic targets."),
    ("S5-P14",
     "Perfect is the nominal $0.05$ line.",
     "The reference is the nominal $0.05$ line."),
    ("S5-P15",
     "Perfect is the projected-trace prediction",
     "The reference is the projected-trace prediction"),
    ("S5-P16",
     "Perfect is a flat line at order one.",
     "The reference is a flat line at order one."),
    ("S5-P17",
     "Perfect is the complete-data benchmark, the dashed line and the black bar.",
     "The reference is the complete-data benchmark, the dashed line and the black bar."),
    ("S5-P18",
     "Perfect is the complete-data benchmark, the dashed line above each cell.",
     "The reference is the complete-data benchmark, the dashed line above each cell."),
    ("S5-P19",
     "Perfect is zero, approached by",
     "The reference is zero, approached by"),
    ("S5-P21",
     "Perfect for the twin is zero, and",
     "The twin's reference is zero, and"),
    ("S5-P21",
     "Perfect is no effect, the line at zero.",
     "The reference is no effect, the line at zero."),
    # ---- S5-P20 table header + caption (borderline #8, authorized) ----
    ("S5-P20",
     "| Structural limit | perfect | achieved |",
     "| Structural limit | reference | achieved |"),
    ("S5-P20",
     "an exact structural prediction",
     "a structural prediction"),
    # ---- vocabulary and formula repairs ----
    ("S5-P7",
     "the run passes if the data land on the projected-trace value",
     "the run passes if the data agree with the projected-trace value"),
    ("S5-P9",
     "The headline cell is non-monotone",
     "The primary cell is non-monotone"),
    ("S5-P10",
     "a junk design at $0$ where the truth is diagonal",
     "a no-signal design at $0$ where the truth is diagonal"),
    ("S5-P11",
     "for genuinely separated candidates",
     "for candidates separated at $O(1)$"),
    ("S5-P11",
     "The pre-registered similar-pair headline is assessed honestly",
     "The pre-registered similar-pair prediction is assessed honestly"),
    ("S5-P12",
     "One cell is a genuine miss, because",
     "One cell departs from the prediction, because"),
    ("S5-P16",
     # E3 thin (authorized, precision addendum qmd :446)
     "This is exactly the failure mode the result specifies.",
     "This is the failure mode the result specifies."),
    ("S5-P19",
     "Two internal measurements show why the ladder works",
     "Two internal measurements show why the ladder succeeds"),
    ("S5-P21",
     "and the pre-registered headline for the similar pair stays below resolution",
     "and the pre-registered prediction for the similar pair stays below resolution"),
    ("S5-P21",
     "A pilot's apparent value of $-2$ dissolved in the full run. We report that "
     "failure as the discipline requires.",
     "A pilot's apparent value of $-2$ did not persist in the full run, a failure we "
     "report as the pre-registration requires."),
    ("S5-P21",
     # incidental catch #2 (authorized): literal backslash-escaped quotes
     "width=\\\"100%\\\"",
     "width=\"100%\""),
    ("S5-P22",
     "This robustness is empirical and scoped to the designs studied.",
     "This robustness is empirical and restricted to the designs studied."),
    # ---- ratified Demo 5 at S5-P18 (three substrings) ----
    ("S5-P18",
     "Across three levels of signal strength the stronger constructions recover the "
     "complete-data benchmark where the errors come from choosing too rich a model. A "
     "floor remains where selection is genuinely hard (@fig-ladder).",
     "Across three levels of signal strength, the stronger constructions recover the "
     "complete-data benchmark wherever the errors come from choosing too rich a model, "
     "while a residual shortfall remains where selection is hard even with complete "
     "data (@fig-ladder)."),
    ("S5-P18",
     "$\\rho = 0$ (junk)",
     "$\\rho = 0$ (no signal)"),
    ("S5-P18",
     "At correlation $0.40$ the two-moment and equating arms reach $0.904$ and $0.903$ "
     "against a complete-data benchmark of $0.899$, and the differences are within "
     "twice the Monte Carlo standard error of about $0.010$. Both arms are therefore "
     "statistically indistinguishable from the benchmark, with a small overshoot the "
     "same interval does not resolve. The junk cell closes $90$ percent of the gap "
     "from uncorrected to benchmark. In the weak-signal cell the benchmark itself "
     "drops to $0.820$, and no arm passes $0.650$. We read that floor as a limit of "
     "the information in the data rather than a calibration error, and the calibration "
     "checks below support that interpretation, though they do not separately "
     "decompose it in the weak-signal cell. The residual is a measurement on these "
     "designs rather than a theorem.",
     "At correlation $0.40$ the two-moment and equating arms reach $0.904$ and $0.903$ "
     "against a complete-data benchmark of $0.899$; because the differences are within "
     "twice the Monte Carlo standard error of about $0.010$, both arms are "
     "statistically indistinguishable from the benchmark, with a small overshoot the "
     "same interval does not resolve. The zero-correlation cell removes $90$ percent "
     "of the difference between the uncorrected criterion and the benchmark. In the "
     "weak-signal cell, by contrast, the benchmark itself drops to $0.820$ and no arm "
     "passes $0.650$. We read that shortfall as a limit of the information in the data "
     "rather than as a calibration error, an interpretation the calibration checks "
     "below support, although they do not separately decompose it in the weak-signal "
     "cell; the residual is a measurement on these designs rather than a theorem."),
]

# S5-P4: "sits between" -> "lies between", exactly three occurrences
p4 = para["S5-P4"]
if p4["draft_prose"].count("sits between") != 3:
    raise SystemExit("S5-P4: expected exactly 3 'sits between' -- aborting.")
p4["draft_prose"] = p4["draft_prose"].replace("sits between", "lies between")
print("S5-P4: replaced (3x).")

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if old not in cur:
        raise SystemExit(f"{pid}: expected substring not found -- aborting:\n  {old[:80]}")
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring not unique -- aborting:\n  {old[:80]}")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: replaced (sub).")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("batch 5 applied: 13 units touched; S5-P2/P3/P5/P6/P8 untouched.")
