# Sweep batch 4: S4 Derivations to the D-26 register (todo/048 Phase D(ii)).
#
# Gate: Marcus approved manuscript/reviews/style/batch-S4-proposal-2026-07-05.md
# ("I approve", 2026-07-05). S4-P16 = ratified Demo 4 (full replacement, keeps the
# section header and the display anchor). 18 surgical repairs incl. R11 rescope #5
# (S4-P8) and the authorized E3 thin (S4-P14). Displays, propositions, and proof
# steps untouched. Guards: full-string equality for S4-P16; unique-substring
# asserts elsewhere; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

# --------------------------------------------------------- S4-P16 (full; Demo 4)
OLD_P16 = (
    "## Information-criterion selection\n\n"
    "This part takes up the replication principle's third level for selection, where "
    "the bias has no reference distribution to hide behind. Model selection by "
    "information criterion compares penalized deviances as numbers and takes the "
    "smallest, so whatever bias each candidate's $-2\\bar Q_\\infty$ carries lands "
    "directly in the ranking. By @thm-bias that bias is model-specific, because "
    "$\\mathrm{RIV}_k$ is computed on candidate $k$'s own parameter space. The "
    "corrected criterion takes this form.\n"
    "$$ \\mathrm{AIC}_{\\mathrm{MI}}^{c}(k) \\;=\\; -2\\bar Q_\\infty(\\hat\\psi^{*}_k) "
    "+ 2q_k + \\operatorname{tr}(\\mathrm{RIV}_k). $$ {#eq-ic-corrected}\n"
    "This penalty reproduces $\\mathrm{AIC}_{x;y}$ of "
    "@shimodairaInformationCriterionModel2017, and its missing-data surcharge is "
    "exactly half that of the earlier complete-data-discrepancy criteria "
    "[@cavanaughAkaikeInformationCriterion1998a]. What @thm-bias adds is the anatomy, "
    "the MAR term, and the proper-MI scope. The ranking consequence is immediate. For "
    "two candidates the uncorrected difference carries a differential bias whose "
    "leading term is the surplus of missing information, so the candidate with more "
    "missing information about its own parameters looks artificially better by exactly "
    "that surplus."
)
NEW_P16 = (
    "## Information-criterion selection\n\n"
    "This part takes up the replication principle's third level for selection, where "
    "no reference distribution stands between the statistic and its use. Because model "
    "selection by information criterion compares penalized deviances as numbers and "
    "takes the smallest, whatever bias each candidate's $-2\\bar Q_\\infty$ carries "
    "enters the ranking directly, and by @thm-bias that bias is model-specific, since "
    "$\\mathrm{RIV}_k$ is computed on candidate $k$'s own parameter space. The "
    "corrected criterion is\n"
    "$$ \\mathrm{AIC}_{\\mathrm{MI}}^{c}(k) \\;=\\; -2\\bar Q_\\infty(\\hat\\psi^{*}_k) "
    "+ 2q_k + \\operatorname{tr}(\\mathrm{RIV}_k). $$ {#eq-ic-corrected}\n"
    "This penalty reproduces $\\mathrm{AIC}_{x;y}$ of "
    "@shimodairaInformationCriterionModel2017, with a missing-data surcharge exactly "
    "half that of the earlier complete-data-discrepancy criteria "
    "[@cavanaughAkaikeInformationCriterion1998a]; what @thm-bias adds is the "
    "decomposition of the bias, the MAR term, and the proper-MI scope. The consequence "
    "for ranking is immediate: for two candidates, the uncorrected difference carries "
    "a differential bias whose leading term is the surplus of missing information, so "
    "the candidate with more missing information about its own parameters looks "
    "artificially better by exactly that surplus."
)

SUBS = [
    ("S4-P1",
     "This section delivers the paper's analytic results",
     "This section presents the paper's analytic results"),
    ("S4-P1",
     "It prices the bias of the averaged log-likelihood to leading order",
     "It quantifies the bias of the averaged log-likelihood to leading order"),
    ("S4-P4",
     "The two regimes are distinguished experimentally",
     "The two cases are distinguished experimentally"),
    ("S4-P5",
     "Seven regularity conditions are in force, and none is exotic.",
     "Seven regularity conditions are in force, and all are standard."),
    ("S4-P6",
     "One trap is worth naming. Substituting $\\operatorname{Var}(\\hat\\theta_"
     "{\\text{obs}})$ for the variance of the gap in the second display produces a "
     "spurious $-\\tfrac12 q$. We display @eq-vargap to forestall it.",
     "One trap deserves note: substituting $\\operatorname{Var}(\\hat\\theta_"
     "{\\text{obs}})$ for the variance of the gap in the second display produces a "
     "spurious $-\\tfrac12 q$, and we display @eq-vargap to forestall it."),
    ("S4-P8",
     "Two checks close the theorem",
     "Two checks complete the theorem"),
    ("S4-P8",
     # R11 rescope #5 (authorized, precision addendum item 5)
     "The two arms differ by exactly the posterior-draw imputation variance of "
     "@sec-background's proper-imputation paragraph.",
     "The two arms differ, to leading order, by the posterior-draw imputation "
     "variance of @sec-background's proper-imputation paragraph."),
    ("S4-P9",
     "The theorem prices one model's bias.",
     "The theorem quantifies one model's bias."),
    ("S4-P10",
     "This result is firm. The metric is its substance.",
     "This result is firm, and the metric is its substance."),
    ("S4-P11",
     "This result is firm. The proof is one matrix inequality.",
     "This result is firm, and the proof is one matrix inequality."),
    ("S4-P11",
     "The practical reading is direct. Correcting an MI deviance comparison by the "
     "difference of the two models' own traces over-corrects at the null. This "
     "happens whenever the tested directions mix unequally-missing information.",
     "In practical terms, correcting an MI deviance comparison by the difference of "
     "the two models' own traces over-corrects at the null whenever the tested "
     "directions mix unequally-missing information."),
    ("S4-P11",
     "Both regimes are exhibited in @sec-simulations.",
     "Both cases are exhibited in @sec-simulations."),
    ("S4-P12",
     "This result is firm. The mechanism is exact cancellation",
     "This result is firm, and the mechanism is exact cancellation"),
    ("S4-P14",
     # E3 thin (authorized, precision addendum qmd :352)
     "matters instead exactly where no reference distribution stands",
     "matters instead where no reference distribution stands"),
    ("S4-P15",
     "A scope statement closes this part.",
     "A scope statement concludes this part."),
    ("S4-P18",
     "The residual matters. A correctly centered criterion can still select worse "
     "than complete-data AIC. The reason is the subject of the rest of this part.",
     "The residual matters, because a correctly centered criterion can still select "
     "worse than complete-data AIC, and the reason is the subject of the rest of "
     "this part."),
    ("S4-P19",
     "and yet it buys three things",
     "and yet it yields three things"),
    ("S4-P22",
     "Two structural limits close this part.",
     "Two structural limits conclude this part."),
]

p16 = para["S4-P16"]
if p16["draft_prose"] != OLD_P16:
    raise SystemExit("S4-P16: current draft_prose does not match the gated Current "
                     "text -- aborting (no writes made).")
p16["draft_prose"] = NEW_P16
print("S4-P16: replaced (full).")

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

print("batch 4 applied: 15 units touched; 8 untouched.")
