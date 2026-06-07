# D-03 Amendment 1 applied to S4 + phi-tilde definition, 2026-06-07
#
# Ratified in-chat: the Derivations section carries NO Monte Carlo numbers and no
# simulation findings; preregistered claims get one-line forward pointers to
# @sec-simulations; all empirical content consolidates in S5. Inline headline
# numbers remain permitted in S1 and the S6 verdict (summary, not substantiation).
# Also: phi-tilde formally defined in P4 (posterior draw, FIML degenerate case,
# centering + variance property used by the order counting in P7b).
#
# Moves OUT of S4 (to be drafted INTO S5): the sign-regime experiment, the
# known-scale experiment (R=2e5, 4%), the pooled theorem confirmation (2.43+/-0.26
# vs 2.42-2.55), the 2.64-vs-8.47 / 52-se discrimination, the pairing sd table
# (18.4/26.6/36.5 vs 1.58/1.47/1.57), the W4 measurements (+2.5 level, similar
# below resolution, dissimilar -1.2 at 3.5 se), the 0.042/0.034 null rates, the
# W3 rates (0.674/0.816/0.898) + 100% largest-RIV signature, the ladder table +
# four findings (KS 0.281->0.019, var 3.18->0.97, shrinkage 0.586/0.570 +
# 0.362/0.398, floor 0.17), the 3.6e-15 / 6.10-vs-10.00 exhibits, the 0.011
# proper-MI tracking. P22's structural limits restated as PROVED facts.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = {p["id"]: p for p in l3["paragraphs"]}

def rep(pid, old, new):
    p = paras[pid]
    if new in p["draft_prose"]:
        return  # already applied (idempotent re-run)
    assert old in p["draft_prose"], f"pattern not found in {pid}: {old[:60]}"
    p["draft_prose"] = p["draft_prose"].replace(old, new)

# ---- P1 roadmap: numbers-inline sentence replaced
rep("S4-P1",
    "Headline numbers are quoted where the claims are made, and the studies behind "
    "them are reported in @sec-simulations.",
    "Where a claim was tested by a pre-registered study, the test is flagged where "
    "the claim is made, and all empirical evidence is reported in @sec-simulations.")

# ---- P4: phi-tilde definition + simulation sentence -> forward pointer
rep("S4-P4",
    "Under congenial proper MI the imputation parameter $\\tilde\\phi$ is a draw from "
    "the imputation posterior fit to $Y_{\\text{obs}}$. Under deterministic FIML "
    "imputation it collapses to the point value $\\hat\\theta_{\\text{obs}}$.",
    "Under congenial proper MI the imputation parameter is a posterior draw, "
    "$\\tilde\\phi \\sim \\pi(\\phi \\mid Y_{\\text{obs}})$, where $\\pi$ is the "
    "posterior of the imputation model, which under congeniality (R4) is the model "
    "whose predictive distribution the analyst's procedure agrees with. Under "
    "deterministic FIML imputation the draw degenerates to the point mass "
    "$\\tilde\\phi = \\hat\\theta_{\\text{obs}}$. In either case $\\tilde\\phi$ is "
    "centered at $\\hat\\theta_{\\text{obs}}$ with "
    "$\\operatorname{Var}(\\tilde\\phi) = I_{\\text{obs}}^{-1} + O(n^{-2})$, the "
    "property the order counting below draws on.")
rep("S4-P4",
    "Both regimes were confirmed by direct simulation: imputing from the truth "
    "drives the imputation bias to zero, and imputing from the fitted model produces "
    "the constants of the theorem (@sec-simulations).",
    "The two regimes are distinguished experimentally by a dedicated study in "
    "@sec-simulations.")

# ---- P8: experiments + pooled number -> forward pointers
rep("S4-P8",
    "A dedicated experiment with $R = 2\\times10^5$ repetitions confirms all four "
    "values within 4%. Every model compared below estimates a covariance",
    "The four-way collapse is a pre-registered prediction, tested in "
    "@sec-simulations. Every model compared below estimates a covariance")
rep("S4-P8",
    "The total is convention-free, and both readings are verified symbolically and "
    "by simulation. The pre-registered Monte Carlo confirmation of @eq-thm pools to "
    "$\\hat T = 2.43 \\pm 0.26$ against the augmented target range $2.42$ to $2.55$ "
    "in the four-variate MAR design (@sec-simulations).",
    "The total is convention-free, and both readings are verified symbolically. The "
    "theorem's pre-registered Monte Carlo confirmation is reported in "
    "@sec-simulations.")

# ---- P10: discrimination numbers -> forward pointer
rep("S4-P10",
    "The derivation was carried through three independent routes. On a four-variate "
    "design built to separate the two formulas, @eq-lrt-bias gives "
    "$2.64$ where the naive difference gives $8.47$, and the Monte Carlo mean lands on "
    "@eq-lrt-bias within sampling error, which is $52$ standard errors from the naive "
    "value (@sec-simulations).",
    "The derivation was carried through three independent routes. In designs where "
    "the tested directions mix unequally-missing information the two formulas are far "
    "apart, and a pre-registered design built to separate them is graded in "
    "@sec-simulations.")

# ---- P12: sd numbers -> forward pointer
rep("S4-P12",
    "The measurement matches. At the null, the "
    "single-model standard deviation grows $18.4$, $26.6$, $36.5$ across "
    "$N = 500$, $1000$, $2000$, while the paired differential stays flat at $1.58$, "
    "$1.47$, $1.57$. At the fixed alternative the growth returns. This is why",
    "Both the growth of the single-model noise and the flatness of the paired "
    "differential are exhibited across sample sizes in @sec-simulations. This is why")

# ---- P13: W4 measurement passage -> analytic caveat + forward pointer
rep("S4-P13",
    "Separation, not nesting, is the criterion. A nested but false restriction "
    "triggers the decoupling just as a non-nested pair does. A direct measurement "
    "confirms the mechanism and adds one refinement, and its findings are measured in "
    "the sense of @sec-methods. Fitting compound-symmetry and AR(1) candidates to the "
    "same imputations under a strong MAR design, with $20{,}000$ repetitions per cell "
    "and an MCAR twin to isolate the design-imbalance contribution: the per-candidate "
    "level is a large $O(1)$ of about $+2.5$ deviance units that collapses under MCAR, "
    "and the two candidates' levels decouple. The differential between these two "
    "similar candidates is below Monte Carlo resolution, because they respond to the "
    "imbalance almost identically. A maximally dissimilar pair, a structure-blind "
    "diagonal model against AR(1), carries a resolved differential of $-1.2$ at "
    "$3.5$ standard errors. The differential's size scales with how differently the "
    "competitors handle the missing data. One caveat travels with the dissimilar case "
    "and is restated in @sec-discussion. A badly misspecified candidate also carries a "
    "mechanism-independent misspecification $O(1)$, separable by the MCAR contrast but "
    "able to offset part of the design-imbalance term in the net ranking bias.",
    "Separation, not nesting, is the criterion. A nested but false restriction "
    "triggers the decoupling just as a non-nested pair does. The expectation from the "
    "expansion is that the differential's size scales with how differently the "
    "competitors handle the missing data, because similar candidates respond to the "
    "same imbalance almost identically and their contributions nearly cancel. One "
    "caveat is analytic and travels with dissimilar pairs. A badly misspecified "
    "candidate also carries a mechanism-independent misspecification $O(1)$, "
    "separable from the design-imbalance term in measurement by an MCAR contrast but "
    "able to offset part of it in the net ranking bias. The decoupling, the "
    "dissimilarity scaling, and the caveat were all the subject of a pre-registered "
    "measurement reported in @sec-simulations.")

# ---- P14: null rates -> forward pointer
rep("S4-P14",
    "Correcting the numerator on top of it "
    "double-counts. The pre-registered null rates agree: $0.042$ uncorrected against "
    "the simulated reference, $0.034$ and slightly conservative with the additional "
    "correction. The differential bias matters",
    "Correcting the numerator on top of it double-counts, a prediction checked "
    "against pre-registered null rates in @sec-simulations. The differential bias "
    "matters")

# ---- P18 (C3): full replacement - predictions only
paras["S4-P18"]["draft_prose"] = (
    "Selection is where the theorem's directional content becomes testable. The "
    "corrected criterion makes two pre-registered predictions. Uncorrected MI-AIC "
    "should misclassify toward the candidates with the most missing information "
    "about their own parameters, because that is the direction of the differential "
    "bias. Adding each candidate's own trace should remove the tilt and recover "
    "complete-data selection in expectation. Both predictions, the recovery the "
    "correction achieves, and the residual it leaves are graded in "
    "@sec-simulations. The residual matters. A correctly centered criterion can "
    "still select worse than complete-data AIC, and the reason is the subject of "
    "the rest of this part."
)
paras["S4-P18"]["proposition"] = "The two preregistered directional predictions for selection, stated as predictions with the forward pointer; the residual motivates the ladder."
paras["S4-P18"]["review"]["topic_sentence"] = "Selection is where the theorem's directional content becomes testable."
paras["S4-P18"]["review"]["closing_sentence"] = "A correctly centered criterion can still select worse than complete-data AIC, and the reason is the subject of the rest of this part."
paras["S4-P18"]["audit"]["numbers"] = {"directional prediction + recovery": "verif:todo/004-simulation-hypotheses.md (predictions; results in S5)"}

# ---- P20: fallback sentence trimmed of the count
rep("S4-P20",
    "A simulated reference in the style of Chan's Monte Carlo null was the "
    "pre-registered fallback and was never needed.",
    "A simulated reference in the style of Chan's Monte Carlo null was the "
    "pre-registered fallback.")

# ---- P21 (C6): full replacement - the three predictions
paras["S4-P21"]["draft_prose"] = (
    "The pre-registration states what each map should achieve, and the predictions "
    "split along the null/noncentral axis. On the null side, each map should close "
    "more of the calibration gap than the one before it, and matching the full null "
    "distribution should make selection indistinguishable from complete-data AIC "
    "wherever overfit flips drive the errors. On the noncentral side, the two "
    "stronger maps should shrink the evidence against misspecified candidates by "
    "factors computable in advance from the null weights, the affine map by $a_k$ "
    "and the equating map by approximately $1/\\lambda_{\\max}$ in the far tail. "
    "And where the complete-data oracle itself struggles, no observed-data "
    "correction should close the remaining gap, because the shortfall there is "
    "information loss rather than miscalibration. All three predictions, with the "
    "frozen pass criteria they were graded against, are reported in "
    "@sec-simulations."
)
paras["S4-P21"]["proposition"] = "The ladder's preregistered predictions (null-side completeness; exact noncentral shrinkage factors; the information-loss floor), stated as predictions with the forward pointer."
paras["S4-P21"]["review"]["topic_sentence"] = "The pre-registration states what each map should achieve, and the predictions split along the null/noncentral axis."
paras["S4-P21"]["review"]["closing_sentence"] = "All three predictions, with the frozen pass criteria they were graded against, are reported in @sec-simulations."
paras["S4-P21"]["audit"]["numbers"] = {"predicted shrinkage factors a_k, 1/lambda_max": "deriv:sec-ic", "predictions + pass criteria": "verif:todo/027-ladder-preregistration.md"}

# ---- P22 (C7): full replacement - limits as proved facts
paras["S4-P22"]["draft_prose"] = (
    "Two structural limits close this part, and both are proved. First, "
    "block-diagonal zero patterns make the naive trace difference and the exact "
    "projected trace coincide. Such constraints decompose both information matrices "
    "over within-block and cross-block coordinates, which is exactly the equality "
    "condition of @prp-naive. The overstatement of @eq-overstate is therefore "
    "invisible in block-diagonal candidate families, and it is material only for "
    "constraints that do not block-decompose, such as the mean restriction in the "
    "design of @prp-lrt. Second, per-model marginal transforms cannot calibrate a "
    "difference distribution. The dependence between two candidates' scores is "
    "invariant under maps applied to each score separately, so no per-model map "
    "controls the law of their difference, and near-tied comparisons remain "
    "uncalibrated after equating. Selection-aware refinements are developed "
    "separately. Both limits are exhibited numerically in @sec-simulations. As in "
    "the likelihood-ratio part, everything here is stated for the "
    "deterministic-FIML $\\bar Q_\\infty$. The anchoring cancellations are "
    "properties of sharing the imputation model, so the construction carries to "
    "proper MI unchanged, and the proper-MI check is part of the pre-registered "
    "evidence in @sec-simulations."
)
paras["S4-P22"]["proposition"] = "The two structural limits stated as proved facts (block-decomposition equality; marginal-map invariance of difference distributions); numerical exhibits and the proper-MI check forward-pointed."
paras["S4-P22"]["review"]["topic_sentence"] = "Two structural limits close this part, and both are proved."
paras["S4-P22"]["review"]["closing_sentence"] = "...the proper-MI check is part of the pre-registered evidence in @sec-simulations."
paras["S4-P22"]["audit"]["numbers"] = {"equality condition / invariance arguments": "deriv:sec-ic"}
paras["S4-P22"]["review"]["flags"] = None

# ---- audit notes
for pid in ("S4-P1", "S4-P4", "S4-P8", "S4-P10", "S4-P12", "S4-P13", "S4-P14", "S4-P18", "S4-P20", "S4-P21", "S4-P22"):
    paras[pid]["audit"]["notes"] = (paras[pid]["audit"]["notes"] +
        " D-03-A1 applied 2026-06-07: simulation numbers/findings moved to S5; forward pointers only.").strip()

l3["metadata"]["status"] = "drafting_s4_d03a1_applied"
l3["metrics_gate"]["notes"] = (
    "D-03 Amendment 1 applied to S4 (2026-06-07): no MC numbers or simulation "
    "findings in the Derivations section; forward pointers to @sec-simulations; "
    "phi-tilde formally defined in P4. S5 drafting must absorb: sign-regime + "
    "known-scale experiments, pooled theorem confirmation, 52-se discrimination, "
    "pairing sd table, W4 measurements, null-rate double-counting, W3 rates + "
    "signature, ladder table + four findings, the two structural-limit exhibits, "
    "proper-MI tracking. 51 paragraphs; lint green."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---- Level 4: remove the S4-attached MC entries (recreated under S5 at its drafting)
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)
drop = {"E-S4-P8-1", "E-S4-P8-2", "E-S4-P12-1", "E-S4-P13-1", "E-S4-P14-2", "E-S4-P18-1", "E-S4-P21-1"}
kept = []
for e in l4["evidence_map"]:
    if e["id"] in drop:
        continue
    if e["id"] == "E-S4-P10-1":
        e["pointer"] = "deriv:sec-lrt"
        e["passage_or_value"] = "Prop L1, I_com metric, three routes."
        e["note"] = "LRT differential (firm); the MC discrimination evidence re-attaches at S5."
    kept.append(e)
l4["evidence_map"] = kept
l4["metrics_gate"]["notes"] = (
    "S4 MC-evidence entries removed under D-03-A1 (re-created against S5 paragraphs "
    "at S5 drafting; the artifacts are unchanged). All remaining pointers resolve."
)

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("D-03-A1 applied to S4; phi-tilde defined; L4 MC entries deferred to S5")
