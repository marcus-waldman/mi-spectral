# S4 part (b) - formalize P10/P11 + strip remaining numbers, 2026-06-07
#
# Marcus: fill out the P10/P11 proof sketches and audit against the companion;
# no numbers in part (b).
# Audit record (every displayed step checked against derivation.qmd):
#   P10: Z/J definitions + Z = I_com I_obs^-1 S + O_p(1), Var(Z) (:1304-:1307);
#        J ->p I_com EM identity (:1308); self-consistency J^-1 Z = delta_obs only
#        for J = I_com (:1311); quadratic-form display (:1315); expectations minus
#        Wilks (:1316-:1317); naive error = I_obs substitution (:1318-:1320);
#        full tr(RIV_perp) definition added to the prop div (:1294-:1296).
#   P11: Gram pair (I_obs^{1/2}G, I_obs^{-1/2}I_com G) (:1351); Schur complement
#        display (:1353-:1354); trace against (G' I_com G)^-1 (:1355); equality
#        condition + equal-fractions special case r*q_d (:1347-:1349); closed-form
#        gap + coupling reading (:1368-:1374). The 5% / factor-3 numbers removed
#        (analytic contrast now qualitative; exhibits live in S5).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = {p["id"]: p for p in l3["paragraphs"]}

paras["S4-P10"]["draft_prose"] = (
    "::: {#prp-lrt}\n"
    "## Differential bias at the null\n\n"
    "Under R1-R7, at the null,\n"
    "$$ \\mathbb{E}\\big[\\hat d_L - \\hat d_{\\text{com}}\\big] \\;=\\; "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp) + O(n^{-1}), \\qquad "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp) \\;:=\\; "
    "\\operatorname{tr}\\big(I_{\\text{obs}}^{-1} I_{\\text{mis}\\mid\\text{obs}}\\big) "
    "- \\operatorname{tr}\\big[(G^\\top I_{\\text{com}} G)^{-1}\\, G^\\top "
    "I_{\\text{com}} I_{\\text{obs}}^{-1} I_{\\text{mis}\\mid\\text{obs}}\\, "
    "G\\big], $$ {#eq-lrt-bias}\n"
    "the missing information of the tested directions, projected onto the null "
    "tangent space in the $I_{\\text{com}}$ metric.\n"
    ":::\n\n"
    "This result is firm, and the metric is its substance. Write "
    "$Z = \\nabla\\bar Q_\\infty(\\theta_0)$ for the score of the averaged "
    "log-likelihood at the truth and $J = -\\nabla^2\\bar Q_\\infty(\\theta_0)$ for "
    "its curvature. Because the conditional density integrates to one, the "
    "evaluation-slot gradient of the imputed part vanishes at $(\\theta_0, "
    "\\theta_0)$, and the score reduces to\n"
    "$$ Z \\;=\\; S + I_{\\text{mis}\\mid\\text{obs}}\\,(\\hat\\theta_{\\text{obs}} "
    "- \\theta_0) + O_p(1) \\;=\\; I_{\\text{com}}\\, I_{\\text{obs}}^{-1}\\, S + "
    "O_p(1), \\qquad \\operatorname{Var}(Z) \\;=\\; I_{\\text{com}}\\, "
    "I_{\\text{obs}}^{-1}\\, I_{\\text{com}} + O(\\sqrt n), $$\n"
    "with $S$ the observed-data score. The curvature converges to\n"
    "$$ J \\;\\to_p\\; I_{\\text{obs}} + I_{\\text{mis}\\mid\\text{obs}} \\;=\\; "
    "I_{\\text{com}}, $$\n"
    "the EM identity restated in @sec-background. The two limits are consistent "
    "only together. The unconstrained maximizer of $\\bar Q_\\infty$ must reproduce "
    "$\\hat\\theta_{\\text{obs}}$, which is EM self-consistency, and indeed "
    "$J^{-1} Z = I_{\\text{com}}^{-1}\\, I_{\\text{com}}\\, I_{\\text{obs}}^{-1} S "
    "= \\hat\\theta_{\\text{obs}} - \\theta_0$ holds only for $J = I_{\\text{com}}$. "
    "The constrained maximizer therefore projects $Z$ onto $\\operatorname{col}(G)$ "
    "in the $I_{\\text{com}}$ metric, and the deviance is the standard difference "
    "of quadratic forms,\n"
    "$$ \\hat d_L \\;=\\; Z^\\top\\big[I_{\\text{com}}^{-1} - G(G^\\top "
    "I_{\\text{com}} G)^{-1} G^\\top\\big] Z + O_p(n^{-1/2}). $$\n"
    "Taking expectations against $\\operatorname{Var}(Z)$ and subtracting Wilks' "
    "$\\mathbb{E}[\\hat d_{\\text{com}}] = q_{\\mathrm{d}} + O(n^{-1})$ gives "
    "@eq-lrt-bias. The natural error is now visible. Substituting "
    "$I_{\\text{obs}}$ for the curvature, which is the same as conflating "
    "$\\hat\\psi_0^{*}$ with the null model's own observed-data MLE, reproduces "
    "exactly the naive difference that the next proposition shows always "
    "overstates. The derivation was carried through three independent routes, and "
    "a pre-registered design built to separate the two formulas is graded in "
    "@sec-simulations."
)

paras["S4-P11"]["draft_prose"] = (
    "::: {#prp-naive}\n"
    "## The naive difference always overstates\n\n"
    "With $\\operatorname{tr}(\\mathrm{RIV}_0) = \\operatorname{tr}[(G^\\top "
    "I_{\\text{obs}} G)^{-1} G^\\top I_{\\text{mis}\\mid\\text{obs}} G]$ the null "
    "model's own self-contained trace correction, always\n"
    "$$ \\operatorname{tr}(\\mathrm{RIV}_\\perp) \\;\\le\\; "
    "\\operatorname{tr}(\\mathrm{RIV}) - \\operatorname{tr}(\\mathrm{RIV}_0), "
    "$$ {#eq-overstate}\n"
    "with equality if and only if $\\operatorname{col}(I_{\\text{obs}}^{1/2} G)$ is "
    "an invariant subspace of the standardized missing information "
    "$H = I_{\\text{obs}}^{-1/2} I_{\\text{mis}\\mid\\text{obs}} "
    "I_{\\text{obs}}^{-1/2}$. Equal fractions of missing information is a special "
    "case of equality, with both sides equal to $r\\, q_{\\mathrm{d}}$ for the "
    "common odds $r$.\n"
    ":::\n\n"
    "This result is firm, and the proof is one matrix inequality. The Gram matrix "
    "of the pair $(I_{\\text{obs}}^{1/2} G,\\; I_{\\text{obs}}^{-1/2} "
    "I_{\\text{com}} G)$ is positive semidefinite, so its Schur complement gives\n"
    "$$ G^\\top I_{\\text{com}}\\, I_{\\text{obs}}^{-1}\\, I_{\\text{com}}\\, G "
    "\\;\\succeq\\; (G^\\top I_{\\text{com}} G)\\,(G^\\top I_{\\text{obs}} "
    "G)^{-1}\\,(G^\\top I_{\\text{com}} G), $$\n"
    "and tracing both sides against $(G^\\top I_{\\text{com}} G)^{-1}$ yields "
    "@eq-overstate. The gap also has an exact closed form, which makes the "
    "equality condition transparent. Partitioning $H$ by the retained directions, "
    "block $H_{11}$ on $\\operatorname{col}(I_{\\text{obs}}^{1/2} G)$, against the "
    "tested directions, with coupling block $H_{12}$,\n"
    "$$ \\big[\\operatorname{tr}(\\mathrm{RIV}) - "
    "\\operatorname{tr}(\\mathrm{RIV}_0)\\big] - "
    "\\operatorname{tr}(\\mathrm{RIV}_\\perp) \\;=\\; "
    "\\operatorname{tr}\\big[(I + H_{11})^{-1} H_{12} H_{12}^\\top\\big] "
    "\\;\\ge\\; 0, $$ {#eq-gap}\n"
    "zero exactly when $H_{12} = 0$, which is when the tested and retained "
    "directions carry independent missing information. The overstatement is "
    "therefore precisely the missing-information coupling between the two "
    "subspaces, screened by the retained block's own information. The practical "
    "reading is direct. Correcting an MI deviance comparison by the difference of "
    "the two models' own traces over-corrects at the null whenever the tested "
    "directions mix unequally-missing information: negligibly when the design sits "
    "near the invariance case, and by multiples when it does not. Both regimes are "
    "exhibited in @sec-simulations."
)

for pid in ("S4-P10", "S4-P11"):
    paras[pid]["audit"]["notes"] = (paras[pid]["audit"]["notes"] +
        " Formalized 2026-06-07 and audited line-by-line against derivation.qmd "
        "@sec-lrt-bias (:1301-:1320) / @sec-lrt-naive (:1345-:1374); numbers removed per D-03-A1.").strip()
paras["S4-P10"]["audit"]["numbers"] = {"score/curvature/projection chain": "deriv:sec-lrt"}
paras["S4-P11"]["audit"]["numbers"] = {"Gram/Schur step + closed-form gap": "deriv:sec-lrt"}

l3["metadata"]["status"] = "drafting_s4_part_b_formalized"

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4 P10/P11 formalized")
