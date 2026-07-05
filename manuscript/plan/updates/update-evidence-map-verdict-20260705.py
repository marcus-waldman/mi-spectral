# Evidence-map table, verdict column (Marcus's amendment, 2026-07-05).
#
# Marcus: an impatient reader also wants the quick answer -- did the evidence
# support the claim -- with "supporting"/"miss" DEFINED. The definition is the
# paper's own: every study carries a pass criterion fixed in its pre-registration
# before any code was written (@sec-methods, S5-P3), so the verdict column
# restates the section's own assessments (pass / fail / mixed; the engine row,
# which has no registered criterion, is marked as the empirical bound it is).
# Also fixes one vocabulary straggler found while checking verdicts against the
# pass criteria: S5-P13 "Both arms land within Monte Carlo error" (the gate
# pattern lacked "within"; extended in the same commit).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

p = para["S5-P1b"]

# ---- guard: the lead-in and header must be the version landed at e31fd0c ----
if ("| Claim tested | Analytic basis | Study | Result |" not in p["draft_prose"]
        or "Verdict" in p["draft_prose"]):
    raise SystemExit("S5-P1b is not the pre-verdict version -- aborting.")

NEW = (
    "The correspondence between the derivations and the studies is collected in "
    "@tbl-evidence-map before the designs are stated: each row names a claim, the "
    "analytic result behind it, the study that tests it, the outcome with the exhibit "
    "that reports it, and the assessment. The designs are stated under the same study "
    "names in the paragraphs that follow, and a reader can treat the table as the "
    "section's map, returning to it from any single design or result. In the final "
    "column, *pass* means the study met the pass criterion fixed in its "
    "pre-registration before any code was written (@sec-methods), *fail* marks a "
    "registered prediction that was not met, and mixed rows name both parts; the "
    "column restates the section's own reporting rather than adding a new grading.\n\n"
    "| Claim tested | Analytic basis | Study | Result | Verdict |\n"
    "|---|---|---|---|---|\n"
    "| The averaged log-likelihood overstates its complete-data counterpart by "
    "$\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) + (A){+}(C)$ | @thm-bias | Theorem "
    "validation | pooled $2.43 \\pm 0.26$, centered on the augmented band $2.42$ to "
    "$2.55$ (@fig-w1-theorem) | pass (pooled criterion met); the $N=1000$ cell "
    "missed, reported |\n"
    "| Known-scale collapse: bias $0$ under deterministic FIML, "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under proper MI | @eq-knownscale | "
    "Known scale and sign regime | $0.025 \\pm 0.018$ and $-0.536 \\pm 0.018$ against "
    "targets $0$ and $-0.561$ (@fig-knownscale) | pass |\n"
    "| Imputing from the true model reverses the sign of the total | the conditioning "
    "fork at @eq-qbar | Known scale and sign regime | the total reverses sign, as the "
    "fitted-versus-true-model distinction requires (reported with @fig-knownscale) | "
    "pass |\n"
    "| A calibrated reference absorbs the null bias, so correcting the numerator on "
    "top double-counts | @eq-spectrum-sum | Likelihood ratio | Type I error $0.042$ "
    "uncorrected and $0.034$ corrected, near the nominal $0.05$ (@fig-lrt-absorption) "
    "| pass (corrected arm conservative, as double-counting predicts) |\n"
    "| The differential bias at the null is $\\operatorname{tr}(\\mathrm{RIV}_\\perp)$, "
    "not the naive trace difference | @prp-lrt, @prp-naive | Formula discrimination | "
    "$2.64 \\pm 0.11$ and $2.70 \\pm 0.11$ against the predicted $2.64$; the naive "
    "$8.5$ excluded at $52$ standard errors (@fig-discrimination) | pass |\n"
    "| Pairing holds the differential's noise at $O(1)$ | @prp-pairing | Pairing | "
    "null sd near $1.5$ and flat, against $18.4$ to $36.5$ for a single model; the "
    "fixed alternative reverts (@fig-pairing) | pass |\n"
    "| Uncorrected MI-AIC favors the largest-RIV candidate, and the trace correction "
    "restores selection | @thm-bias, @eq-ic-corrected | Selection sweep | $0.67$ "
    "uncorrected, $0.82$ corrected, benchmark $0.90$ at $N=500$; 100% of "
    "misclassifications on the largest-RIV candidate (@fig-w3-selection) | pass (both "
    "registered conditions) |\n"
    "| The null side calibrates map by map, and noncentral statistics shrink by "
    "predictable factors | the three maps of @sec-derivations | Distribution-matching "
    "ladder | two-moment and equating arms reach $0.904$ and $0.903$ against the "
    "benchmark $0.899$; shrinkage $0.59$ and $0.36$ against predicted $0.56$ and "
    "$0.40$ (@tbl-ladder, @fig-ladder-internals) | pass (all three registered "
    "conditions); the weak-signal shortfall was itself the registered prediction |\n"
    "| Block-diagonal families fall at the equality case, and per-model maps cannot "
    "calibrate a difference | @prp-naive; the structural limits of @sec-derivations | "
    "Distribution-matching ladder | equality to $3.6 \\times 10^{-15}$; naive-input "
    "cost $0.824$ against $0.904$; difference law $6.10$ and $5.99$ against $10.00$ "
    "and $7.10$ (@tbl-structural-limits) | pass (structural predictions matched) |\n"
    "| The design-imbalance differential decouples only for separated candidates and "
    "grows with dissimilarity | @prp-ac-diff | Non-nested measurement | the dissimilar "
    "pair resolves at $-1.2$ ($3.5$ standard errors); the similar pair stays below "
    "resolution (@fig-w4-nonnested) | mixed: mechanism and dissimilar pair pass; the "
    "similar-pair prediction failed |\n"
    "| The bootstrap engine tracks the analytic arm, bounding the cost of not running "
    "data augmentation | the G3 scope statement of @sec-discussion | Engine "
    "sensitivity | $\\operatorname{tr}(\\mathrm{RIV})$ within $2$ to $3$ percent; "
    "selection within $0.011$ | within stated tolerances (empirical bound, no "
    "registered criterion) |\n\n"
    ": **The studies of this section mapped to the claims they test.** Each row names "
    "a claim from @sec-derivations, the analytic result behind it, the study that "
    "tests it, the outcome with its exhibit, and the assessment against the "
    "pre-registered pass criterion. {#tbl-evidence-map}"
)

p["draft_prose"] = NEW
p["review"]["flags"] += (
    " | verdict column added 2026-07-05 (Marcus): pass/fail/mixed defined against the "
    "pre-registered pass criteria; restates the section's own assessments."
)
print("S5-P1b: verdict column added.")

# ---- vocabulary straggler found while checking verdicts (S5-P13) ----
p13 = para["S5-P13"]
old = "Both arms land within Monte Carlo error of their targets"
new = "Both arms are within Monte Carlo error of their targets"
if p13["draft_prose"].count(old) != 1:
    raise SystemExit("S5-P13: 'land within' anchor not found uniquely -- aborting.")
p13["draft_prose"] = p13["draft_prose"].replace(old, new)
print("S5-P13: 'land within' -> 'are within'.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("done.")
