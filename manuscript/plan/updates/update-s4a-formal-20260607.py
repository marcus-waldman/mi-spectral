# S4 part (a) - formalization pass, 2026-06-07
#
# Marcus: a Derivations section must read as a derivation, not a narrative summary
# pointing at the companion ("take my word for it" fails D-08's own rejection of the
# pure-pointer posture). Fix: the proof sketches now carry the actual displayed
# steps, quarried from the companion's B1-B4 / A1-A4 / lemma chain
# (derivation.qmd :804-:918):
#   P6 (T_est): expansion display -> E[T_est] = -1/2 tr(I_com Var(gap)) -> the
#      score-identity chain displayed -> Var(gap) -> trace reduction displayed.
#   P7 (T_imp): factorization display -> iterated-expectation display (oracle tie-in)
#      -> the three-piece expansion DISPLAYED with alpha defined formally and the
#      Gibbs warning -> main piece reduced to tr(RIV) in a display.
#   NEW P7b ((A)+(C)): order counting displayed ((A) = E[delta]'alpha = O(1),
#      (C) = 1/2 tr(H_phiphi I_obs^-1) = O(1)) -> MCAR cancellation -> closed form
#      -> standing narrative (kept from the previous revision).
#   P8: the curvature identity nabla^2 C_n = H_phiphi + I_mis|obs promoted to a display.
# Labeling: companion's three pieces are (A)/(B)/(C); the manuscript uses
# "(A) / the main cross term / (C)" because the letter B collides with the old
# Term B (and the letters with T_imp/T_est bridge are already explained in P5).
# Inserted id S4-P7b to avoid renumbering the whole section.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras = {p["id"]: p for p in l3["paragraphs"]}

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
    "The theorem is firm in the sense of @sec-methods, and the two terms are derived "
    "in turn. The estimation-mismatch term comes first. Expanding "
    "$\\ell_{\\text{com}}$ to second order about its own maximizer, where the score "
    "vanishes,\n"
    "$$ T_{\\text{est}} \\;=\\; -\\tfrac12\\,(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}})^\\top \\mathcal{J}_{\\text{com}}"
    "(\\hat\\theta_{\\text{com}})\\,(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}}) + O_p(n^{-3/2}). $$\n"
    "Taking expectations, replacing the realized curvature by $I_{\\text{com}}$, and "
    "writing the quadratic form as a trace gives\n"
    "$$ \\mathbb{E}[T_{\\text{est}}] \\;=\\; -\\tfrac12\\operatorname{tr}\\!"
    "\\big(I_{\\text{com}}\\operatorname{Var}(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}})\\big) + O(n^{-3/2}). $$\n"
    "The variance of the gap is the substantive step, and it runs through the score "
    "identity. Differentiating the factorization of @eq-split's first term and taking "
    "conditional expectations gives "
    "$U_{\\text{obs}} = \\mathbb{E}[U_{\\text{com}} \\mid Y_{\\text{obs}}]$, hence\n"
    "$$ \\operatorname{Cov}(U_{\\text{obs}}, U_{\\text{com}}) = "
    "\\operatorname{Var}(U_{\\text{obs}}) = I_{\\text{obs}}, \\qquad "
    "\\operatorname{Cov}(\\hat\\theta_{\\text{obs}}, \\hat\\theta_{\\text{com}}) = "
    "I_{\\text{obs}}^{-1}\\, I_{\\text{obs}}\\, I_{\\text{com}}^{-1} = "
    "I_{\\text{com}}^{-1}, $$\n"
    "the second equality by the asymptotic linearity of both estimators. An "
    "equivalent statement is that the complete-data estimator is asymptotically "
    "uncorrelated with the gap. Assembling the three pieces of the variance,\n"
    "$$ \\operatorname{Var}\\big(\\hat\\theta_{\\text{obs}} - "
    "\\hat\\theta_{\\text{com}}\\big) \\;=\\; I_{\\text{obs}}^{-1} + "
    "I_{\\text{com}}^{-1} - 2I_{\\text{com}}^{-1} \\;=\\; I_{\\text{obs}}^{-1} - "
    "I_{\\text{com}}^{-1}, $$ {#eq-vargap}\n"
    "and substituting back,\n"
    "$$ \\mathbb{E}[T_{\\text{est}}] \\;=\\; -\\tfrac12\\operatorname{tr}\\!\\big("
    "I_{\\text{com}} I_{\\text{obs}}^{-1} - I_k\\big) \\;=\\; "
    "-\\tfrac12\\big(\\operatorname{tr}(I_{\\text{obs}}^{-1} I_{\\text{com}}) - "
    "k\\big) \\;=\\; -\\tfrac12\\operatorname{tr}(\\mathrm{RIV}). $$\n"
    "One trap is worth naming. Substituting "
    "$\\operatorname{Var}(\\hat\\theta_{\\text{obs}})$ for the variance of the gap in "
    "the second display produces a spurious $-\\tfrac12 k$, and @eq-vargap is "
    "displayed to forestall it."
)

paras["S4-P7"]["draft_prose"] = (
    "The imputation-bias term is the delicate half, and its derivation has three "
    "steps. First, factor the complete-data log-likelihood as "
    "$\\ell_{\\text{com}}(\\theta) = \\ell_{\\text{obs}}(\\theta) + "
    "\\ell_{\\text{mis}\\mid\\text{obs}}(\\theta)$ with "
    "$\\ell_{\\text{mis}\\mid\\text{obs}}(\\theta) := \\log P(Y_{\\text{mis}} \\mid "
    "Y_{\\text{obs}}, \\theta)$. The observed parts cancel inside $T_{\\text{imp}}$, "
    "leaving\n"
    "$$ T_{\\text{imp}} \\;=\\; \\mathbb{E}_{Y_{\\text{mis}}\\mid Y_{\\text{obs}},"
    "\\tilde\\phi}\\big[\\ell_{\\text{mis}\\mid\\text{obs}}"
    "(\\hat\\theta_{\\text{obs}})\\big] - \\ell_{\\text{mis}\\mid\\text{obs}}"
    "(\\hat\\theta_{\\text{obs}}). $$\n"
    "Second, take expectations over the true completion. What remains is the "
    "discrepancy between averaging the missing-data log-density under the fitted "
    "$\\tilde\\phi$ and averaging it under the truth,\n"
    "$$ \\mathbb{E}[T_{\\text{imp}}] \\;=\\; \\mathbb{E}_{Y_{\\text{obs}}}\\big[\\,"
    "\\mathbb{E}_{\\tilde\\phi}[\\ell_{\\text{mis}\\mid\\text{obs}}"
    "(\\hat\\theta_{\\text{obs}})] - \\mathbb{E}_{\\theta_0}"
    "[\\ell_{\\text{mis}\\mid\\text{obs}}(\\hat\\theta_{\\text{obs}})]\\,\\big]. $$\n"
    "These two inner expectations would cancel were $\\tilde\\phi = \\theta_0$, which "
    "is the oracle case of @eq-qbar and the tower-property branch stated there. The "
    "term is nonzero precisely because the imputations use "
    "$\\tilde\\phi \\approx \\hat\\theta_{\\text{obs}} \\neq \\theta_0$. Third, "
    "expand to second order in $\\tilde\\phi$ about $\\theta_0$, differentiating "
    "under the integral and using the Bartlett identity "
    "$\\mathbb{E}_{\\theta_0}[S_{\\text{mis}\\mid\\text{obs}}"
    "S_{\\text{mis}\\mid\\text{obs}}^\\top] = I_{\\text{mis}\\mid\\text{obs}}$. Three "
    "pieces result:\n"
    "$$ \\mathbb{E}[T_{\\text{imp}}] \\;=\\; \\underbrace{\\mathbb{E}\\big[("
    "\\tilde\\phi-\\theta_0)^\\top\\alpha\\big]}_{(A)} \\;+\\; "
    "\\underbrace{\\mathbb{E}\\big[(\\tilde\\phi-\\theta_0)^\\top "
    "I_{\\text{mis}\\mid\\text{obs}}(\\hat\\theta_{\\text{obs}}-\\theta_0)\\big]}_"
    "{\\text{main cross term}} \\;+\\; \\underbrace{\\tfrac12\\mathbb{E}\\big[("
    "\\tilde\\phi-\\theta_0)^\\top H_{\\phi\\phi}(\\tilde\\phi-\\theta_0)\\big]}_"
    "{(C)}. $$ {#eq-timp-pieces}\n"
    "Here $\\alpha = \\operatorname{Cov}_{\\theta_0}\\big("
    "\\ell_{\\text{mis}\\mid\\text{obs}}, S_{\\text{mis}\\mid\\text{obs}}\\big) = "
    "-\\mathcal{E}'(\\theta_0)$ is the gradient of the conditional missing-data "
    "entropy, and $H_{\\phi\\phi}$ is the curvature of the conditional cross-entropy. "
    "The labels $(A)$ and $(C)$ follow the companion derivation's bookkeeping; the "
    "companion letters its main piece $(B)$, which this paper avoids for obvious "
    "reasons. The entropy gradient is not zero. Gibbs' inequality concerns varying "
    "the evaluation point of $\\mathbb{E}_{\\theta_0}[\\log p_\\theta]$, while "
    "$\\alpha$ varies the sampling distribution of the completions, and the two are "
    "different functions. For the normal family the gradient is supported entirely "
    "on the covariance parameters: $\\alpha_\\mu = 0$ and "
    "$\\alpha_{\\sigma^2} = -n_{\\text{mis}}/2\\sigma^2 \\neq 0$ in the univariate "
    "case. The main cross term reduces directly. Proper MI centers $\\tilde\\phi$ at "
    "$\\hat\\theta_{\\text{obs}}$, so\n"
    "$$ \\mathbb{E}\\big[(\\tilde\\phi-\\theta_0)^\\top I_{\\text{mis}\\mid"
    "\\text{obs}}(\\hat\\theta_{\\text{obs}}-\\theta_0)\\big] \\;=\\; "
    "\\operatorname{tr}\\!\\big(I_{\\text{mis}\\mid\\text{obs}}\\, "
    "\\operatorname{Cov}(\\tilde\\phi, \\hat\\theta_{\\text{obs}})\\big) \\;=\\; "
    "\\operatorname{tr}\\!\\big(I_{\\text{mis}\\mid\\text{obs}}\\, "
    "I_{\\text{obs}}^{-1}\\big) + O(n^{-1}) \\;=\\; "
    "\\operatorname{tr}(\\mathrm{RIV}) + O(n^{-1}), $$\n"
    "the leading constant of the theorem."
)

P7b = (
    "The two remaining pieces of @eq-timp-pieces form the design-imbalance term, and "
    "their orders are counted directly. Under proper MI centered at "
    "$\\hat\\theta_{\\text{obs}}$, the displacement $\\delta := \\tilde\\phi - "
    "\\theta_0$ has $\\mathbb{E}[\\delta] = O(n^{-1})$, the MLE bias, and "
    "$\\operatorname{Var}(\\delta) = I_{\\text{obs}}^{-1} = O(n^{-1})$, while "
    "$\\alpha$ and $H_{\\phi\\phi}$ are both $O(n)$, extensive in "
    "$n_{\\text{mis}}$. Hence\n"
    "$$ (A) = \\mathbb{E}[\\delta]^\\top\\alpha = O(1), \\qquad "
    "(C) = \\tfrac12\\operatorname{tr}\\!\\big(H_{\\phi\\phi}\\, "
    "I_{\\text{obs}}^{-1}\\big) + O(n^{-1}) = O(1), $$\n"
    "two order-one pieces of opposite sign. Their leading parts cancel exactly when "
    "the missing and observed units share a conditioning-variable distribution, "
    "which is MCAR. Under MAR the sum survives, with bivariate monotone closed form\n"
    "$$ (A)+(C) \\;=\\; \\frac{n_{\\text{mis}}}{n_{\\text{obs}}} \\Big[\\, 1 - "
    "\\tfrac12 \\operatorname{tr}\\big(Q_{\\text{mis}} Q_{\\text{obs}}^{-1}\\big) "
    "\\Big] + O(n^{-1}), $$ {#eq-ac}\n"
    "where $Q_{\\text{mis}}$ and $Q_{\\text{obs}}$ are the conditioning-variable "
    "second-moment matrices of the missing and observed units. The term is zero "
    "exactly when the two distributions agree. For non-monotone patterns the "
    "covariance-MLE bias entering $(A)$ comes from the general second-order "
    "Cox-Snell bias of the MLE, carried to general dimension and verified in two "
    "computer-algebra systems. Summing the pieces of @eq-timp-pieces with "
    "$\\mathbb{E}[T_{\\text{est}}]$ gives @eq-thm. These statements do not all rest "
    "on the same footing, and the distinction matters for how the term is used. "
    "What is firm, in the sense of @sec-methods, is everything structural about "
    "$(A)+(C)$: its sign, its $O(1)$ order under MAR, its exact vanishing under "
    "MCAR, the closed form @eq-ac, and the information convention it is computed "
    "in. Its absolute magnitude is another matter. The per-replicate statistic is "
    "heavy-tailed, so direct Monte Carlo estimates scatter without trend around the "
    "analytic leading-order value, and the magnitude is measured only imprecisely. "
    "The saving fact is that comparisons never depend on the magnitude alone. "
    "Candidates fit to the same imputations touch $(A)+(C)$ only through their "
    "difference, the heavy-tailed component cancels in that difference, and the "
    "comparison-relevant differential is derived and measured precisely in the next "
    "part."
)

# P8: promote the curvature identity to a display
paras["S4-P8"]["draft_prose"] = paras["S4-P8"]["draft_prose"].replace(
    "One curvature identity, "
    "$\\nabla^2 C_n(\\theta_0) = H_{\\phi\\phi} + I_{\\text{mis}\\mid\\text{obs}}$, "
    "regroups the proof's three pieces into one expansion and delivers the "
    "known-scale collapse as the parameter-free special case.",
    "One curvature identity regroups the proof's three pieces into a single "
    "expansion,\n"
    "$$ \\nabla^2 C_n(\\theta_0) \\;=\\; H_{\\phi\\phi} + "
    "I_{\\text{mis}\\mid\\text{obs}}, $$ {#eq-entropy-hessian}\n"
    "and delivers the known-scale collapse as the parameter-free special case."
)

# Update review objects
paras["S4-P6"]["review"]["closing_sentence"] = "...@eq-vargap is displayed to forestall it."
paras["S4-P6"]["audit"]["notes"] = (paras["S4-P6"]["audit"]["notes"] +
    " Formalization pass 2026-06-07: B2-B4 chain displayed (quarried from derivation.qmd :811-:821, :608-:632).").strip()
paras["S4-P7"]["review"]["closing_sentence"] = "...the leading constant of the theorem."
paras["S4-P7"]["proposition"] = (
    "T_imp derivation in three displayed steps: factorization, iterated expectation "
    "(oracle tie-in), three-piece expansion with alpha formal + Gibbs warning; main "
    "cross term reduced to tr(RIV) in a display."
)
paras["S4-P7"]["audit"]["notes"] = (paras["S4-P7"]["audit"]["notes"] +
    " Formalization pass 2026-06-07: A1-A3 chain displayed (derivation.qmd :837-:868); main-piece reduction displayed (:880); companion's (B) label avoided.").strip()
paras["S4-P8"]["audit"]["notes"] = (paras["S4-P8"]["audit"]["notes"] +
    " Curvature identity promoted to display (eq-entropy-hessian).").strip()

new_p7b = {
    "id": "S4-P7b",
    "section": "S4",
    "goal": "prove_sketch",
    "proposition": "(A)+(C) formal: order counting displayed, MCAR cancellation, closed form (@eq-ac), Cox-Snell route for non-monotone; theorem assembled; three-standing narrative.",
    "depends_on": ["S4-P7"],
    "dep_types": ["builds_on"],
    "review": {
        "serves_L2": "S4-SP2",
        "serves_L1": "M4a DERIVATIONS (D-03 inline numbers; D-08 proofs in companion; D-10 principle spine)",
        "sets_up": "S4-P13 (the differential); S6 G1",
        "topic_sentence": "The two remaining pieces of @eq-timp-pieces form the design-imbalance term, and their orders are counted directly.",
        "closing_sentence": "...the comparison-relevant differential is derived and measured precisely in the next part.",
        "status": "drafted",
        "flags": None
    },
    "draft_prose": P7b,
    "audit": {
        "status": "complete",
        "citations": {},
        "numbers": {
            "(A)+(C) order counting + closed form": "deriv:sec-lrt-ac",
            "analytic leading-order value ~ -0.22": "deriv:sec-lrt-ac"
        },
        "notes": "Split out of P7 in the formalization pass; quarried from the companion's A4 + lemma (derivation.qmd :871-:918)."
    }
}

# insert P7b right after S4-P7 in array order
arr = l3["paragraphs"]
idx = next(i for i, p in enumerate(arr) if p["id"] == "S4-P7")
arr.insert(idx + 1, new_p7b)

l3["metadata"]["status"] = "drafting_s4_part_a_formalized"
l3["metrics_gate"]["notes"] = (
    "S4 part (a) formalized 2026-06-07 (Marcus: a Derivations section must derive): "
    "T_est B2-B4 chain and T_imp A1-A3 chain displayed; new S4-P7b carries the "
    "(A)+(C) order counting and closed form; 51 paragraphs total. Lint green."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)
# move the (A)+(C) evidence entry from P7 to P7b
for e in l4["evidence_map"]:
    if e["id"] == "E-S4-P7-1":
        e["proposition_id"] = "S4-P7b"
        e["id"] = "E-S4-P7b-1"
with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4 part (a) formalized: P6/P7 rewritten with displayed chains, P7b inserted, P8 identity displayed")
