# Tier C fixes (v1 AI-review response, todo/040 Phase 4, 2026-07-03)
#
# Nine easy level3 prose/notation fixes triaged as Tier C in
# todo/040-v1-review-response-registration.md Sec.1 / response-letter.md:
#   proof#10  abstract: add the estimated-scale/covariance qualifier
#   proof#11  abstract: scope "removes the deviance bias" to the trace component only
#   contra#12 S4-P7: alpha = -E'(theta_0) is the NEGATIVE gradient, not the gradient
#   contra#13 S5-P19: KS text says 0.019, figure (sprintf("%.3f", 0.0185)) shows 0.018 --
#             fix text to match the figure's mechanically-produced rounding
#   contra#14 S4-P2/S4-P3/S4-P6: k double-duty (parameter-count dimension AND model
#             index in S4-P16/19/20) -- rename the parameter-count usage to q, leave
#             the model-index usage as k
#   contra#15 S2-P6/S4-P3/S4-P5/S4-P9: standardize the asymptotic imputation-count
#             limit on M (matching the simulation's M in {20,200}), not lowercase m
#   r2#4      S5-P12: define +/- at first use (one MC standard error; figures plot
#             95 percent intervals, a different, larger multiplier -- confirmed by
#             reading w1-h1-pooled-reconciliation.R's pooled_se = 1/sqrt(sum(w)) vs
#             figures.R's est +/- 1.96*se)
#   r2#5      S5-P9: name all four W3 candidate models explicitly (currently only
#             the two extremes, diagonal and saturated, are named); also fixes a
#             separate factual error found while researching this fix -- the truth
#             was misdescribed as "compound-symmetry" (a W4 non-nested candidate,
#             not the W3 truth), when W3's actual truth is sigma_13=sigma_24=0.4
#             (verification/00-setup.R:956,1249; w3-sweep.R:164)
#   r2#6      S5-P4: state which of the six coordinate pairs get 0.6/0.3/0.5
#             (verification/00-setup.R:1242-1247, default_Sigma)
#
# See manuscript/reviews/v1/ai-review-paper-88.md for the reviewer comments and
# manuscript/reviews/v1/response/response-letter.md for the response-letter text.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras_by_id = {p["id"]: p for p in l3["paragraphs"]}


def replace_one(container, key, old, new, label):
    text = container[key]
    if old not in text:
        raise SystemExit(f"{label}: expected OLD text not found -- aborting.\nOLD={old!r}")
    if text.count(old) != 1:
        raise SystemExit(f"{label}: OLD text is not unique ({text.count(old)} occurrences) -- aborting.")
    container[key] = text.replace(old, new)


# ---- proof#10 + proof#11: abstract ----------------------------------------

replace_one(
    l3, "abstract",
    "Under congenial proper multiple imputation with the complete-data maximum "
    "likelihood estimate as target, the averaged log-likelihood overstates its "
    "complete-data counterpart",
    "Under congenial proper multiple imputation with the complete-data maximum "
    "likelihood estimate as target and an estimated scale or covariance, the "
    "averaged log-likelihood overstates its complete-data counterpart",
    "proof#10 (abstract estimated-scale qualifier)",
)
replace_one(
    l3, "abstract",
    "Adding one trace term per candidate removes the deviance bias in expectation "
    "and substantially restores complete-data model selection.",
    "Adding one trace term per candidate removes that trace component of the "
    "deviance bias in expectation and substantially restores complete-data model "
    "selection.",
    "proof#11 (trace-component scoping)",
)

# ---- contra#12: alpha sign (S4-P7) ----------------------------------------

replace_one(
    paras_by_id["S4-P7"], "draft_prose",
    "is the gradient of the conditional missing-data entropy.",
    "is the negative gradient of the conditional missing-data entropy.",
    "contra#12 (alpha sign, S4-P7)",
)

# ---- contra#13: KS 0.019 -> 0.018 (S5-P19) --------------------------------

replace_one(
    paras_by_id["S5-P19"], "draft_prose",
    "falls from $0.281$ under the uncorrected deviance to $0.019$ under equating.",
    "falls from $0.281$ under the uncorrected deviance to $0.018$ under equating.",
    "contra#13 (KS text-figure mismatch, S5-P19)",
)

# ---- contra#14: k (parameter-count) -> q, leaving k as the model index ----

replace_one(
    paras_by_id["S4-P2"], "draft_prose",
    "of dimension $k = p + \\tfrac12 p(p+1)$",
    "of dimension $q = p + \\tfrac12 p(p+1)$",
    "contra#14 (S4-P2 dimension definition)",
)
replace_one(
    paras_by_id["S4-P3"], "draft_prose",
    "&\\;=\\; I_{\\text{obs}}^{-1} I_{\\text{com}} - I_k, \\\\\n"
    "\\operatorname{tr}(\\mathrm{RIV}) &= \\operatorname{tr}(I_{\\text{obs}}^{-1} I_{\\text{com}}) - k.",
    "&\\;=\\; I_{\\text{obs}}^{-1} I_{\\text{com}} - I_q, \\\\\n"
    "\\operatorname{tr}(\\mathrm{RIV}) &= \\operatorname{tr}(I_{\\text{obs}}^{-1} I_{\\text{com}}) - q.",
    "contra#14 (S4-P3 RIV display)",
)
replace_one(
    paras_by_id["S4-P3"], "draft_prose",
    "$D = (I_k + \\mathrm{RIV})^{-1}\\mathrm{RIV}$",
    "$D = (I_q + \\mathrm{RIV})^{-1}\\mathrm{RIV}$",
    "contra#14 (S4-P3 fraction-of-missing-information D)",
)
replace_one(
    paras_by_id["S4-P6"], "draft_prose",
    "\\mathbb{E}[T_{\\text{est}}] &\\;=\\; -\\tfrac12\\operatorname{tr}\\!\\big(I_{\\text{com}} I_{\\text{obs}}^{-1} - I_k\\big) \\\\\n"
    "&\\;=\\; -\\tfrac12\\big(\\operatorname{tr}(I_{\\text{obs}}^{-1} I_{\\text{com}}) - k\\big) \\\\",
    "\\mathbb{E}[T_{\\text{est}}] &\\;=\\; -\\tfrac12\\operatorname{tr}\\!\\big(I_{\\text{com}} I_{\\text{obs}}^{-1} - I_q\\big) \\\\\n"
    "&\\;=\\; -\\tfrac12\\big(\\operatorname{tr}(I_{\\text{obs}}^{-1} I_{\\text{com}}) - q\\big) \\\\",
    "contra#14 (S4-P6 T_est derivation display)",
)
replace_one(
    paras_by_id["S4-P6"], "draft_prose",
    "produces a spurious $-\\tfrac12 k$.",
    "produces a spurious $-\\tfrac12 q$.",
    "contra#14 (S4-P6 spurious-term warning)",
)

# ---- contra#15: standardize the imputation-count limit on M --------------

replace_one(
    paras_by_id["S2-P6"], "draft_prose",
    "drawing $z^{(1)},\\dots,z^{(m)}$ from the conditional predictive distribution",
    "drawing $z^{(1)},\\dots,z^{(M)}$ from the conditional predictive distribution",
    "contra#15 (S2-P6 Wei-Tanner draws)",
)
replace_one(
    paras_by_id["S2-P6"], "draft_prose",
    "noting that Rubin (1987) referred to the quantities $z^{(1)}, \\ldots, z^{(m)}$ as multiple imputations.",
    "noting that Rubin (1987) referred to the quantities $z^{(1)}, \\ldots, z^{(M)}$ as multiple imputations.",
    "contra#15 (S2-P6 Rubin attribution)",
)
replace_one(
    paras_by_id["S2-P6"], "draft_prose",
    "The $m \\to \\infty$ limit of the averaged log-likelihood",
    "The $M \\to \\infty$ limit of the averaged log-likelihood",
    "contra#15 (S2-P6 limit statement)",
)
replace_one(
    paras_by_id["S4-P3"], "draft_prose",
    "Under congenial proper MI with $m \\to \\infty$, Rubin's rules give",
    "Under congenial proper MI with $M \\to \\infty$, Rubin's rules give",
    "contra#15 (S4-P3)",
)
replace_one(
    paras_by_id["S4-P5"], "draft_prose",
    "R7 is the infinite-imputation idealization, and Rubin's finite-$m$ corrections apply otherwise.",
    "R7 is the infinite-imputation idealization, and Rubin's finite-$M$ corrections apply otherwise.",
    "contra#15 (S4-P5)",
)
replace_one(
    paras_by_id["S4-P9"], "draft_prose",
    "the infinite-$m$ limit of the maximize-then-average statistic",
    "the infinite-$M$ limit of the maximize-then-average statistic",
    "contra#15 (S4-P9)",
)

# ---- r2#4: define +/- at first use (S5-P12) -------------------------------

replace_one(
    paras_by_id["S5-P12"], "draft_prose",
    "The inverse-variance pooled estimate is $2.43 \\pm 0.26$, which centers on the augmented band.",
    "The inverse-variance pooled estimate is $2.43 \\pm 0.26$ (one Monte Carlo "
    "standard error; the figure's whiskers instead show $95$ percent intervals), "
    "which centers on the augmented band.",
    "r2#4 (+/- definition, S5-P12)",
)

# ---- r2#5: name all four W3 candidate models + fix the truth description --

replace_one(
    paras_by_id["S5-P9"], "draft_prose",
    "The candidate set is four nested multivariate-normal covariance models, "
    "ranging from a diagonal model up to the saturated model, while the truth "
    "has a compound-symmetry structure.",
    "The candidate set is four nested multivariate-normal covariance models: a "
    "diagonal model with every off-diagonal entry fixed at zero (eight free "
    "parameters); a model that frees the wrong off-diagonal pair, "
    "$\\sigma_{12}$ and $\\sigma_{34}$ (ten free parameters); a model that "
    "frees the correct off-diagonal pair, $\\sigma_{13}$ and $\\sigma_{24}$ "
    "(ten free parameters, the true model); and the saturated model, which "
    "frees every entry (fourteen free parameters). The truth sets "
    "$\\sigma_{13} = \\sigma_{24} = 0.4$ and every other off-diagonal entry to zero.",
    "r2#5 (name all four W3 models, S5-P9)",
)

# ---- r2#6: exact coordinate-pair placement in the theorem-validation Sigma --

replace_one(
    paras_by_id["S5-P4"], "draft_prose",
    "Three coordinate pairs have correlations $0.6$, $0.3$, and $0.5$, and the "
    "rest are zero, which gives a relative-increase-in-variance trace near $5.55$.",
    "Three coordinate pairs are correlated and two are zero: $\\sigma_{12}=0.6$ "
    "between the two coordinates that carry missingness, $\\sigma_{13}=\\sigma_{24}=0.3$ "
    "between each missing coordinate and the fully observed coordinate that drives "
    "its own missingness, and $\\sigma_{34}=0.5$ between the two fully observed "
    "driving coordinates, with $\\sigma_{14}=\\sigma_{23}=0$; this gives a "
    "relative-increase-in-variance trace near $5.55$.",
    "r2#6 (Sigma coordinate-pair placement, S5-P4)",
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)

print("All nine Tier C fixes applied.")
