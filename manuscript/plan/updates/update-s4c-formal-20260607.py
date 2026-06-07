# S4 part (c) - formalize P19/P20, 2026-06-07
#
# Same treatment as parts (a)/(b): the constructions displayed, audited against
# the companion @sec-ic-ladder (derivation.qmd :1624-:1699):
#   P19: T_k display + the three anchoring properties with the closed form
#        T_k = N[log|Sigma_k| - log|S*|] (:1624-:1634); null weights defined as
#        the eigenvalues of the projected operator (:1636-:1639).
#   P20: the three maps DISPLAYED - mean shift; unique affine (a_k, b_k) with the
#        moment-identity corollary (:1645-:1650); equipercentile equating with the
#        PIT exactness (:1658-:1663); Imhof/Davies evaluation; preregistered
#        fallback. SEM-tradition framing kept with its sources.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = {p["id"]: p for p in l3["paragraphs"]}

paras["S4-P19"]["draft_prose"] = (
    "Selection depends on more than a mean. At the null the limiting law of each "
    "anchored deviance is $\\sum_j \\lambda_j \\chi^2_1$ with every weight at least "
    "one (@eq-spectrum-sum), so the variance is inflated by "
    "$\\sum_j \\lambda_j^2 / q_{\\mathrm{d}}$ even after the mean is fixed, and "
    "inflated spread flips rankings. This motivates a graded contrast, "
    "pre-registered in full before any code was written: match the first moment, "
    "the first two moments, or the entire null distribution, and measure what each "
    "step achieves. The working statistic anchors every candidate at the saturated "
    "model fit to the same imputations,\n"
    "$$ T_k \\;=\\; 2\\big[\\bar Q_\\infty(\\hat\\psi^{*}_{\\text{sat}}) - "
    "\\bar Q_\\infty(\\hat\\psi^{*}_k)\\big] \\;\\ge\\; 0. $$\n"
    "Anchoring costs nothing, because AIC ranking is invariant to the common shift, "
    "and it buys three things. The anchor is the congenial imputation model itself, "
    "so the heavy-tailed realized $(A)+(C)$ component and the $O_p(\\sqrt n)$ noise "
    "cancel dataset by dataset, which is the @prp-pairing mechanism applied to "
    "every candidate. Every $T_k$ is a proper likelihood-ratio statistic with a "
    "constructible per-model null law: the analytic weights "
    "$\\lambda_{k,1}, \\dots, \\lambda_{k,q_{d,k}}$ are the nonzero eigenvalues of\n"
    "$$ \\big[I_{\\text{com}}^{-1} - G_k(G_k^\\top I_{\\text{com}} "
    "G_k)^{-1}G_k^\\top\\big]\\, I_{\\text{com}}\\, I_{\\text{obs}}^{-1}\\, "
    "I_{\\text{com}}, \\qquad \\sum_j \\lambda_{k,j} = q_{d,k} + "
    "\\operatorname{tr}(\\mathrm{RIV}_{\\perp,k}), \\quad \\lambda_{k,j} \\ge 1, $$\n"
    "available from the law of @prp-lrt without knowing the global truth. And each "
    "candidate here is a block-diagonal zero pattern, so the constrained maximizer "
    "is closed-form and\n"
    "$$ T_k \\;=\\; N\\big[\\log|\\hat\\Sigma_k| - \\log|S^{*}|\\big] $$\n"
    "exactly, with $S^{*}$ the saturated E-step second-moment matrix."
)

paras["S4-P20"]["draft_prose"] = (
    "Three maps are compared, each built from the analytic null weights. The mean "
    "map is the @eq-lrt-bias complement shift,\n"
    "$$ T^{(1)}_k \\;=\\; T_k - \\operatorname{tr}(\\mathrm{RIV}_{\\perp,k}), $$\n"
    "a linear per-model shift that telescopes, so every pairwise comparison is "
    "simultaneously mean-corrected. The two-moment map is the affine "
    "transformation\n"
    "$$ T^{(2)}_k \\;=\\; a_k T_k + b_k, \\qquad a_k = "
    "\\sqrt{\\,q_{d,k}\\big/\\textstyle\\sum_j \\lambda_{k,j}^2\\,}, \\qquad "
    "b_k = q_{d,k} - a_k \\textstyle\\sum_j \\lambda_{k,j}, $$\n"
    "the unique affine map carrying the null law's mean and variance onto those of "
    "$\\chi^2_{q_{d,k}}$. Uniqueness is an immediate corollary of the moment "
    "identities $\\mathbb{E}[\\sum_j \\lambda_j \\chi^2_1] = \\sum_j \\lambda_j$ "
    "and $\\operatorname{Var} = 2\\sum_j \\lambda_j^2$. Matching a misbehaving "
    "statistic's first two moments is the standard repair in the "
    "structural-equation tradition: the Satorra-Bentler scaled difference statistic "
    "matches the mean [@satorraEnsuringPositivenessScaled2010], and the "
    "mean-and-variance-adjusted statistics match both from the same moment inputs "
    "$\\operatorname{tr}(M)$ and $\\operatorname{tr}(M^2)$ "
    "[@asparouhovRobustChiSquare2006]. Here the coefficients are derived from the "
    "analytic null law rather than estimated from sandwich matrices. The third map "
    "matches all moments by equipercentile equating,\n"
    "$$ T^{(3)}_k \\;=\\; F^{-1}_{\\chi^2_{q_{d,k}}}\\big(F_{W_k}(T_k)\\big), "
    "\\qquad W_k = \\textstyle\\sum_j \\lambda_{k,j} \\chi^2_1, $$\n"
    "the equating function $e_Y(x) = G^{-1}[F(x)]$ of observed-score test equating "
    "[@kolenTestEquatingScaling2014], applied with the analytic null law as $F$ and "
    "the complete-data $\\chi^2$ as $G$. By the probability integral transform the "
    "equated statistic matches the entire null distribution. The "
    "weighted-$\\chi^2$ distribution function is evaluated by numerical inversion "
    "of the characteristic function [@imhofComputingDistributionQuadratic1961; "
    "@daviesAlgorithm155Distribution1980], and a simulated reference in the style "
    "of Chan's Monte Carlo null was the pre-registered fallback. The "
    "pre-registration predicted the split the data then delivered. Each step "
    "should close more of the null-side gap, while the two stronger maps shrink "
    "evidence against misspecified candidates, the affine map by $a_k < 1$ and the "
    "equating map by approximately $1/\\lambda_{\\max}$ in the far tail, because "
    "no transform built from the observed data can restore destroyed Fisher "
    "information."
)

for pid in ("S4-P19", "S4-P20"):
    paras[pid]["audit"]["notes"] = (paras[pid]["audit"]["notes"] +
        " Formalized 2026-06-07 and audited against derivation.qmd @sec-ic-ladder "
        "(:1624-:1699): T_k display + closed form, eigenvalue definition of the null "
        "weights, the three maps displayed with the moment-identity corollary and "
        "PIT exactness.").strip()
paras["S4-P19"]["audit"]["numbers"] = {"T_k construction + null-weight spectrum": "deriv:sec-ic"}
paras["S4-P20"]["audit"]["numbers"] = {"the three maps + (a_k, b_k) uniqueness + PIT exactness": "deriv:sec-ic"}

l3["metadata"]["status"] = "drafting_s4_part_c_formalized"
l3["metrics_gate"]["notes"] = (
    "S4 fully formalized 2026-06-07: parts (a)/(b)/(c) all carry displayed "
    "derivation chains audited against the companion; no simulation numbers "
    "(D-03-A1); 51 paragraphs. Remaining: S5 (absorbing all empirics), S6."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S4 P19/P20 formalized")
