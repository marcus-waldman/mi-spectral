# S4 part (a) fixes from Marcus's read, 2026-06-07
#
# 1. Notation collision: Term A vs piece (A). Manuscript drops the A/B letters from
#    the split; subscripts T_imp (imputation-bias term) and T_est (estimation-mismatch
#    term), matching S1-P4's mechanism names and the companion's own underbrace text.
#    Bridge sentence added (the companion says Term A / Term B). Companion checked:
#    collision exists there too but renaming the audited companion is out of scope;
#    the bridge sentence carries the mapping.
# 2. Covariance restored to the Term-B sketch, in the companion's logical order
#    (L3 -> L2 at derivation.qmd :616-:632): score identity -> Cov(U_obs,U_com)=I_obs
#    -> Cov(theta_obs,theta_com)=I_com^-1 -> subtract. The uncorrelated-gap reading
#    stated as the equivalent, not the reason.
# 3. The Firm:/Measured:/Structural: segmented list in P7 -> narrative.
#    "consume" (banned, T-03) avoided.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras = {p["id"]: p for p in l3["paragraphs"]}

paras["S4-P5"]["draft_prose"] = (
    "The bias is split at the pivot $\\hat\\theta_{\\text{obs}}$ into two terms with "
    "distinct mechanisms,\n"
    "$$ T \\;=\\; \\underbrace{\\big[\\bar Q_\\infty(\\hat\\theta_{\\text{obs}}) - "
    "\\ell_{\\text{com}}(\\hat\\theta_{\\text{obs}})\\big]}_{T_{\\text{imp}}:\\ "
    "\\text{imputation-bias term}} \\;+\\; "
    "\\underbrace{\\big[\\ell_{\\text{com}}(\\hat\\theta_{\\text{obs}}) "
    "- \\ell_{\\text{com}}(\\hat\\theta_{\\text{com}})\\big]}_{T_{\\text{est}}:\\ "
    "\\text{estimation-mismatch term}}, $$ {#eq-split}\n"
    "on the log-likelihood scale. Deviance-scale statements double everything. The "
    "companion derivation calls these Term A and Term B. The descriptive subscripts "
    "are used here instead, because the companion's bookkeeping also uses the labels "
    "$(A)$ and $(C)$ for pieces inside the first term, and the letters must not "
    "collide. Seven regularity conditions are in force and none is exotic. R1 and R2 "
    "are smoothness and positive-definite information "
    "[@vaartAsymptoticStatistics1998a]. R3 is ignorability "
    "[@rubinInferenceMissingData1976b]. R4 through R6 are congeniality, properness, "
    "and self-efficiency [@mengMultipleImputationInferencesUncongenial1994a; "
    "@rubinMultipleImputationNonresponse1987]. R7 is the infinite-imputation "
    "idealization, with Rubin's finite-$m$ corrections applying otherwise. Together "
    "they deliver the variance-recovery property "
    "$T_\\infty = I_{\\text{obs}}^{-1}$ that identifies @eq-riv with $r_\\infty$."
)

paras["S4-P6"]["draft_prose"] = (
    "::: {#thm-bias}\n"
    "## Q-function deviance bias\n\n"
    "Under R1-R7, for a model that estimates a scale or covariance, to leading order\n"
    "$$ \\mathbb{E}[T] \\;=\\; +\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) \\;+\\; "
    "\\big[(A)+(C)\\big] \\;+\\; O(n^{-1}), $$ {#eq-thm}\n"
    "decomposing as $\\mathbb{E}[T_{\\text{imp}}] = +\\operatorname{tr}(\\mathrm{RIV}) "
    "+ [(A)+(C)] + O(n^{-1})$ and $\\mathbb{E}[T_{\\text{est}}] = "
    "-\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) + O(n^{-1})$. The design-imbalance "
    "term $(A)+(C)$ vanishes under MCAR and is a nonzero $O(1)$ under MAR.\n"
    ":::\n\n"
    "The theorem is firm in the sense of @sec-methods. The estimation-mismatch term "
    "is an elementary Taylor argument. Expanding $\\ell_{\\text{com}}$ about its own "
    "maximizer kills the first-order term, and the second-order term runs through the "
    "variance of the estimator gap. That variance has three pieces, "
    "$\\operatorname{Var}(\\hat\\theta_{\\text{obs}}) + "
    "\\operatorname{Var}(\\hat\\theta_{\\text{com}}) - "
    "2\\operatorname{Cov}(\\hat\\theta_{\\text{obs}}, \\hat\\theta_{\\text{com}})$, "
    "and the covariance is the substantive step. The observed-data score is the "
    "conditional expectation of the complete-data score, so the two scores have "
    "covariance $\\operatorname{Cov}(U_{\\text{obs}}, U_{\\text{com}}) = "
    "\\operatorname{Var}(U_{\\text{obs}}) = I_{\\text{obs}}$, and the asymptotic "
    "linearity of both estimators turns this into "
    "$\\operatorname{Cov}(\\hat\\theta_{\\text{obs}}, \\hat\\theta_{\\text{com}}) = "
    "I_{\\text{com}}^{-1}$. An equivalent statement is that the complete-data "
    "estimator is asymptotically uncorrelated with the gap. Substituting the three "
    "pieces gives\n"
    "$$ \\operatorname{Var}\\big(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}}\\big) \\;=\\; I_{\\text{obs}}^{-1} - "
    "I_{\\text{com}}^{-1}, $$ {#eq-vargap}\n"
    "and contracting against the curvature $I_{\\text{com}}$ reduces the trace to "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$. One trap is worth naming. "
    "Substituting $\\operatorname{Var}(\\hat\\theta_{\\text{obs}})$ for the variance "
    "of the gap produces a spurious $-\\tfrac12 k$, and @eq-vargap is displayed to "
    "forestall it."
)

paras["S4-P7"]["draft_prose"] = (
    "The imputation-bias term is the delicate half. Factoring the complete-data "
    "log-likelihood as $\\ell_{\\text{obs}} + \\log P(Y_{\\text{mis}} \\mid "
    "Y_{\\text{obs}}, \\theta)$ cancels the observed parts, and a second-order "
    "expansion in $\\tilde\\phi$ leaves three pieces. The main cross term pairs the "
    "imputation error with the estimation error through "
    "$I_{\\text{mis}\\mid\\text{obs}}$ and contributes the leading "
    "$+\\operatorname{tr}(\\mathrm{RIV})$. The piece labeled $(A)$ pairs the bias of "
    "$\\tilde\\phi$ with the gradient of the conditional missing-data entropy. The "
    "piece labeled $(C)$ pairs the variance of $\\tilde\\phi$ with the curvature of "
    "the conditional cross-entropy. The labels follow the companion derivation's "
    "bookkeeping, and they name pieces inside the imputation-bias term, not the terms "
    "of @eq-split. The entropy gradient is not zero. A tempting appeal to Gibbs' "
    "inequality fails, because the gradient varies the sampling distribution of the "
    "completions rather than the evaluation point of the log-density, and for the "
    "normal family it is supported entirely on the covariance parameters. The leading "
    "parts of $(A)$ and $(C)$ cancel exactly when the missing and observed units "
    "share a conditioning-variable distribution, which is MCAR. Under MAR their sum "
    "is the design-imbalance term, with bivariate monotone closed form\n"
    "$$ (A)+(C) \\;=\\; \\frac{n_{\\text{mis}}}{n_{\\text{obs}}} \\Big[\\, 1 - "
    "\\tfrac12 \\operatorname{tr}\\big(Q_{\\text{mis}} Q_{\\text{obs}}^{-1}\\big) "
    "\\Big] + O(n^{-1}), $$ {#eq-ac}\n"
    "zero exactly when the two conditioning-variable distributions agree. These "
    "statements do not all rest on the same footing, and the distinction matters for "
    "how the term is used. What is firm, in the sense of @sec-methods, is everything "
    "structural about $(A)+(C)$: its sign, its $O(1)$ order under MAR, its exact "
    "vanishing under MCAR, the closed form above, and the information convention it "
    "is computed in. Its absolute magnitude is another matter. The per-replicate "
    "statistic is heavy-tailed, so direct Monte Carlo estimates scatter without trend "
    "around the analytic leading-order value, and the magnitude is measured only "
    "imprecisely. The saving fact is that comparisons never depend on the magnitude "
    "alone. Candidates fit to the same imputations touch $(A)+(C)$ only through their "
    "difference, the heavy-tailed component cancels in that difference, and the "
    "comparison-relevant differential is derived and measured precisely in the next "
    "part."
)

for pid in ("S4-P5", "S4-P6", "S4-P7"):
    paras[pid]["audit"]["notes"] = (paras[pid]["audit"]["notes"] +
        " Revised 2026-06-07 (Marcus part-a read): T_imp/T_est rename with companion bridge; "
        "covariance step restored per derivation.qmd L2/L3 (:616-:632); standing passage to narrative.").strip()

l3["metadata"]["status"] = "drafting_s4_part_a_revised"

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4 P5-P7 revised")
