# Sweep batch 2: S2 Background to the D-26 register (todo/048 Phase D(ii)).
#
# Gate: Marcus approved manuscript/reviews/style/batch-S2-proposal-2026-07-05.md
# ("I approve", 2026-07-05). Register changes and R11 precision changes labeled
# below; propositions untouched (style pass, ground rule 2).
#
# Units: S2-P1 opener fix; S2-P4 one verb; S2-P5 three repairs (R10 formula fold,
# metaphor family, de-metaphorized "drives" with merge); S2-P6 one verb phrase;
# S2-P7 FULL rewrite = ratified Demo 3 + authorized R11 rescopes #3/#4 (em-dash ->
# semicolon per the kept ban); S2-P10 one join; S2-P12 one verb; S2-P13 one noun.
# S2-P2/P3/P8/P9/P11: NO CHANGE per the approved proposal.
#
# Guards: full-string equality for the S2-P7 rewrite; unique-substring asserts for
# every partial repair. Any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

# ------------------------------------------------------------- S2-P7 (full; Demo 3 + R11)
OLD_P7 = (
    "**Proper imputation.** The imputations this paper studies are proper in Rubin's "
    "sense, and whether imputation is proper or improper changes the bias the theorem "
    "derives. Proper imputation propagates parameter uncertainty. A parameter value is "
    "first drawn from its posterior given the observed data, and the missing values are "
    "then drawn from the predictive distribution at that drawn value. Chapter 4 of "
    "@rubinMultipleImputationNonresponse1987 states the validity conditions and gives "
    "the fully normal Bayesian scheme as the canonical example. Improper imputation "
    "skips the first draw and imputes at a fixed parameter value. The Monte Carlo "
    "E-step of the previous paragraph is improper by construction, and so is the entire "
    "deterministic-EM line of work in which the earlier missing-data criteria were "
    "derived [@cavanaughAkaikeInformationCriterion1998a; "
    "@shimodairaInformationCriterionModel2017]. The distinction is not bookkeeping, "
    "because the extra posterior draw contributes its own variation to the averaged "
    "log-likelihood, and the main theorem prices it exactly. Consider the known-scale "
    "case. The bias is zero under improper imputation at the observed-data estimate, "
    "while under proper imputation it is $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$, "
    "so the two forms differ by precisely the posterior-draw contribution. Properness "
    "is also not absolute. @nielsenProperImproperMultiple2003 shows that Bayesian "
    "imputations are proper when the analyst's complete-data estimator is the maximum "
    "likelihood estimator, but the same imputations can fail to be proper for a "
    "different estimator. This paper's analyst always uses the complete-data MLE, which "
    "is the case where congeniality implies properness "
    "[@nielsenProperImproperMultiple2003]. The extension of the bias accounting from "
    "the improper, deterministic Q-function to proper multiple imputation is one of the "
    "things this paper adds."
)
NEW_P7 = (
    "**Proper imputation.** The imputations this paper studies are proper in Rubin's "
    "sense, and whether imputation is proper or improper changes the bias the theorem "
    "derives. Proper imputation propagates parameter uncertainty: a parameter value is "
    "first drawn from its posterior given the observed data, and the missing values are "
    "then drawn from the predictive distribution at that drawn value; Chapter 4 of "
    "@rubinMultipleImputationNonresponse1987 states the validity conditions and gives "
    "the fully normal Bayesian scheme as the canonical example. Improper imputation, by "
    "contrast, skips the first draw and imputes at a fixed parameter value; the Monte "
    "Carlo E-step of the previous paragraph is improper by construction, as is the "
    "entire deterministic-EM line of work in which the earlier missing-data criteria "
    "were derived [@cavanaughAkaikeInformationCriterion1998a; "
    "@shimodairaInformationCriterionModel2017]. The distinction is more than a matter "
    "of bookkeeping, because the extra posterior draw contributes its own variation to "
    "the averaged log-likelihood, and the main theorem quantifies that contribution to "
    "leading order: in the known-scale case the bias is zero under improper imputation "
    "at the observed-data estimate but $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ "
    "under proper imputation, so the two forms differ, to leading order, by the "
    "posterior-draw contribution. Nor is properness absolute. "
    "@nielsenProperImproperMultiple2003 shows that Bayesian imputations are proper when "
    "the analyst's complete-data estimator is the maximum likelihood estimator, yet the "
    "same imputations can fail to be proper for a different estimator; this paper's "
    "analyst always uses the complete-data MLE, which is the case where congeniality "
    "implies properness [@nielsenProperImproperMultiple2003]. The extension of the bias "
    "accounting from the improper, deterministic Q-function to proper multiple "
    "imputation is one of the things this paper adds."
)

# ------------------------------------------------------------- partial repairs
SUBS = [
    ("S2-P1",
     "This section fixes the paper's notation and assembles the results the "
     "derivations use. The reader needs five things.",
     "This section fixes the paper's notation and assembles, in five items, the "
     "results the derivations use."),
    ("S2-P4",
     "Conflating them corrupts every trace formula in this paper.",
     "Conflating them invalidates every trace formula in this paper."),
    ("S2-P5",
     "The object whose bias this paper derives is a Q-function. So its definition and "
     "one geometric fact about it are needed.",
     "The object whose bias this paper derives is a Q-function, so its definition and "
     "one geometric fact about it are needed."),
    ("S2-P5",
     "The reasoning is direct. We do not know",
     "The reasoning is direct: we do not know"),
    ("S2-P5",
     "Two facts from their analysis carry the weight later.",
     "Two facts from their analysis recur throughout what follows."),
    ("S2-P5",
     "This single geometric fact drives the likelihood-ratio result. Constrained fits "
     "of the averaged log-likelihood project in the $I_{\\text{com}}$ metric.",
     "This single geometric fact underlies the likelihood-ratio result, because "
     "constrained fits of the averaged log-likelihood project in the "
     "$I_{\\text{com}}$ metric."),
    ("S2-P6",
     "One feature of this construction must be marked at once.",
     "One feature of this construction should be noted at once."),
    ("S2-P10",
     "That estimate is too optimistic. It needs a correction for the downward bias "
     "from replacing $\\theta$ with its estimate $\\hat\\theta$, and that correction "
     "is simply to add the parameter count $k$.",
     "That estimate is too optimistic, and the needed correction for the downward "
     "bias from replacing $\\theta$ with its estimate $\\hat\\theta$ is simply to add "
     "the parameter count $k$."),
    ("S2-P12",
     "shows where the difference lodges, because",
     "shows where the difference lies, because"),
    ("S2-P13",
     "each is restated here as the launch point it provides",
     "each is restated here as the starting point it provides"),
]

p7 = para["S2-P7"]
if p7["draft_prose"] != OLD_P7:
    raise SystemExit("S2-P7: current draft_prose does not match the gated Current "
                     "text -- aborting (no writes made).")
p7["draft_prose"] = NEW_P7
print("S2-P7: replaced (full).")

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if old not in cur:
        raise SystemExit(f"{pid}: expected substring not found -- aborting.")
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring not unique -- aborting.")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: replaced (sub).")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("batch 2 applied: 8 units touched; S2-P2/P3/P8/P9/P11 untouched.")
