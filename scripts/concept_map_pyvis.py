"""Render todo/030-concept-map.md as an interactive PyVis network.

Nodes are propositions (hover for the full statement, standing, and evidence).
Edge labels are the argument-map relation types. Output is a self-contained
HTML file at todo/030-concept-map.html.

Run:  py scripts/concept_map_pyvis.py
"""

from pathlib import Path
from pyvis.network import Network

# Standing classes -> color
COLORS = {
    "T":   "#1d4ed8",  # proved + CAS-verified
    "T+M": "#0f766e",  # proved + Monte-Carlo-confirmed
    "E":   "#b45309",  # empirical, scoped to designs studied
    "G":   "#6b7280",  # gap: qualified or absent evidence
}

# (id, label, standing, central?, tooltip)
NODES = [
    ("C1", "C1  +1/2 tr(RIV)\ndecomposition", "T+M", True,
     "THEOREM. Under congenial proper MI targeting the complete-data MLE, "
     "E[Qbar_inf(th_obs) - l_com(th_com)] = +tr(RIV) (imputation bias) "
     "- 1/2 tr(RIV) (estimation mismatch) = +1/2 tr(RIV) + O(1/n), "
     "for models with an estimated scale/covariance.\n"
     "Standing: T+M.\n"
     "Evidence: derivation @sec-thm (eq-theorem); CAS @sec-verify-terms + lst-mc-combine; "
     "MC rederivation-L0-fitted-vs-oracle.R; pooled preregistered W1: 2.43 +/- 0.26 "
     "vs augmented target 2.42-2.55 (w1-h1-pooled-reconciliation.R)."),

    ("C2", "C2  MAR (A)+(C)\ndesign imbalance", "T", True,
     "Under MAR, Term A carries an additional O(1) term "
     "(A)+(C) = a'E[d] + 1/2 tr(H I_obs^-1) - tr(RIV); zero iff missing and observed "
     "units share a conditioning-variable distribution (MCAR). Bivariate monotone closed form "
     "(n_mis/n_obs)[1 - 1/2 tr(Q_mis Q_obs^-1)]. Convention: realized (observed) information "
     "(Kenward-Molenberghs 1998); Delta_KM ~ -0.55 closed form.\n"
     "Firm: sign, O(1) order, MCAR vanishing, O(1/n) correction order. Open: absolute magnitude (G1).\n"
     "Standing: T (structure).\n"
     "Evidence: @sec-termA lemma; term-a-mar-closedform.R (-0.22, MCAR control ~0); "
     "verify_term_ac_nonmonotone{,_genp}.py."),

    ("C3", "C3  LRT differential\ntr(RIV_perp), I_com metric", "T+M", True,
     "PROPOSITION L1. At the null, E[d_L - d_com] = tr(RIV_perp) + O(1/n): the tested "
     "directions' missing information projected onto the null tangent space in the I_com "
     "metric (the Q-function curvature is I_com, the EM identity) - not in I_obs.\n"
     "Standing: T+M.\n"
     "Evidence: @sec-lrt-bias; three independent routes (w2diff-stage1-routes.json); "
     "CAS verify_w2_differential.py A1-A4; MC 52-se discrimination from the naive formula "
     "(2.64 predicted vs 8.47 naive; w2-paired-differential-mu1-cell.R); "
     "blind cross-model re-derivation + adversarial pass sustained (layer3-gpt-5.5-w2diff)."),

    ("C4", "C4  IC correction\nAIC + tr(RIV_k)", "T+M", True,
     "The bias is model-specific (RIV_k on candidate k's own parameter space), so uncorrected "
     "MI-AIC/BIC favor high-RIV candidates by the differential bias. Corrected criterion: "
     "AIC^c(k) = -2 Qbar_inf + 2 q_k + tr(RIV_k) (eq-ic-corrected) = Shimodaira's AIC_{x;y} "
     "as a penalty.\n"
     "Standing: T (criterion as consequence of C1) + M (recovery).\n"
     "Evidence: @sec-ic-criterion; preregistered W3 (phase2-w3/summary.csv): uncorrected 0.674, "
     "corrected 0.816, oracle 0.898 at N=500; 100% of uncorrected misclassifications on the "
     "largest-RIV (saturated) candidate."),

    ("C5", "C5  Positioning\nupstream of calibration", "T", True,
     "This work corrects the NUMERATOR of MI test statistics; Meng-Rubin (1992), Chan-Meng "
     "(2022), Chan (2022 AoS) calibrate the REFERENCE DISTRIBUTION - complementary. "
     "The IC penalty is not new (= AIC_{x;y}, Shimodaira 2017, which halved AICcd/PDIO's "
     "2tr(RIV)). New: (i) imputation/estimation decomposition; (ii) MAR (A)+(C) term "
     "(beyond Shimodaira's fixed-pattern setting; his sec. 8 future work); "
     "(iii) extension to proper MI. Hens-Aerts 2006 reaches the target by IPW reweighting; "
     "leaves the imputation-based criterion open.\n"
     "Standing: T (by comparison of stated results).\n"
     "Evidence: @sec-intro-lineage; verbatim passages in @sec-sources."),

    # --- Premises of C1 ---
    ("S1", "S1  RIV = Rubin's r_inf", "T", False,
     "RIV = I_obs^-1 I_mis|obs in matrix form; its trace is Rubin's r_inf. Disambiguated from "
     "the EM rate / fraction of missing information.\nStanding: T.\n"
     "Evidence: @sec-riv; 'Identification: RIV equals Rubin's r_inf'."),
    ("S2", "S2  one observed-data RIV", "T+M", False,
     "Both terms calibrate to a single RIV built on the unconditional observed-data information, "
     "which under MAR carries a mean-covariance cross term (Kenward-Molenberghs 1998). The "
     "earlier two-RIV reading was an artifact of the naive block-diagonal information.\n"
     "Standing: T+M.\nEvidence: @sec-two-rivs; Appendix C; lemma-revalidation.R; run_all phase 6."),
    ("S3", "S3  fitted, not oracle", "T+M", False,
     "Qbar_inf is the FITTED predictive (imputation model at the estimated/drawn parameter). "
     "Defining the target as the oracle E[l_com | Y_obs] at the truth reverses the sign to "
     "-1/2 tr(RIV).\nStanding: T+M.\nEvidence: @sec-qfun; rederivation-L0-fitted-vs-oracle.R."),
    ("S4", "S4  estimated-scale scope", "T+M", False,
     "Known scale (location-only fit): conditional entropy is parameter-free and the bias "
     "collapses to 0 (deterministic FIML) or -1/2 tr(RIV) (proper MI); arms differ by "
     "C_n = 1/2 tr(RIV).\nStanding: T+M.\n"
     "Evidence: scope callout after @sec-thm; rederivation-knownvar.R (R=2e5)."),
    ("S5", "S5  Term B = -1/2 tr(RIV)", "T", False,
     "Second-order Taylor about th_com + variance-of-the-gap lemma "
     "Var(th_obs - th_com) = I_obs^-1 - I_com^-1.\nStanding: T.\nEvidence: @sec-termB."),
    ("S6", "S6  Term A = +tr(RIV) + (A)+(C)", "T", False,
     "Entropy gradient a != 0, supported on the covariance parameters only (do not invoke "
     "Gibbs).\nStanding: T.\nEvidence: @sec-termA."),
    ("S7", "S7  plug-in-entropy reading", "T", False,
     "E[T] = Delta_n, the conditional-entropy plug-in bias, via Hess(C_n) = H_phiphi + I_mis|obs; "
     "the (A)/(C)/half-trace split is the same bias regrouped; T is convention-free.\n"
     "Standing: T (consistency check).\nEvidence: remark after @sec-combine; two CAS."),

    # --- Consequences/refinements of C3 ---
    ("L2", "L2  naive difference\nalways overstates", "T", False,
     "tr(RIV_perp) <= tr(RIV) - tr(RIV_0), equality iff col(I_obs^1/2 G) is invariant under the "
     "standardized missing information; exact gap tr[(I+H11)^-1 H12 H12'] = the "
     "missing-information coupling between tested and retained directions.\n"
     "Standing: T.\nEvidence: @sec-lrt-naive (Gram/Schur); CAS B1-B4; factor >3 in the mu1 design, "
     "~5% in the W2 design."),
    ("L3", "L3  paired noise\nO(sqrt n) -> O(1)", "T+M", False,
     "The per-dataset paired differential has sd O(1) at the null and under local alternatives "
     "(the shared-imputation O_p(sqrt n) terms are identical realizations in both levels and "
     "cancel dataset by dataset); reverts to O(sqrt n) at fixed alternatives.\n"
     "Standing: T+M.\nEvidence: @sec-lrt-pairing; sd(D)=1.58/1.47/1.57 flat vs "
     "sd(T)=18.4/26.6/36.5 across N=500/1000/2000."),
    ("L4", "L4  (A)+(C) differential\n0 at null; O(1) if separated", "T+M", False,
     "(A)+(C) contributions are properties of the imputation, not the fitted model: exact "
     "cancellation at the null; O(n^-1/2) under local alternatives; O(1) differential only for "
     "pseudo-true-separated candidates (separation, not nesting; Vuong regime). Measured: level "
     "~ +2.5/candidate under MAR (collapses MCAR); similar pair below resolution; dissimilar "
     "pair resolved -1.2 (-3.5 se).\nStanding: T+M.\n"
     "Evidence: @sec-lrt-ac; preregistered todo/029 + Amendment 2; w4-nonnested-vuong.R; "
     "w4-dissimilar-vuong.R; CAS verify_w4_nonnested.py."),
    ("L5", "L5  which procedures\ninherit the bias", "T+M", False,
     "At the null, tr(RIV_perp) equals the mean inflation of a correctly calibrated reference "
     "(sum lambda_j = q_d + tr(RIV_perp); Chan 2022 eq. 1.10), so a calibrated test absorbs it "
     "and extra numerator correction double-counts (W2: 0.042 vs 0.034). The bias affects "
     "exactly the procedures with no reference distribution: IC ranking, explicit numerator "
     "corrections, non-nested comparison.\nStanding: T+M.\n"
     "Evidence: @sec-lrt-consequences; W2-prod-amelia.rds."),

    # --- Consequences/refinements of C4 ---
    ("I4", "I4  calibration ladder\nmean/2-moment/equating", "T+M", False,
     "Saturated-anchored T_k has an analytic null law sum lambda chi2_1 (the C3 spectrum). "
     "Three derived maps: mean shift tr(RIV_perp,k); unique affine two-moment map (a_k, b_k); "
     "equipercentile equating via Imhof/Davies. Null side calibrates completely "
     "(KS 0.281 -> 0.019; variance ratio 3.18 -> 0.97); rho=.40 selection 0.678 -> 0.904/0.903 "
     "vs oracle 0.899; junk cell closes 90%.\nStanding: T+M (preregistered todo/027, all pass).\n"
     "Evidence: @sec-ic-ladder{,-results}; ic-ladder.R; CAS verify_ic_ladder.py L-A1-L-A4."),
    ("I5", "I5  noncentral shrinkage\nexact and unavoidable", "T+M", False,
     "Two-moment and equating maps shrink noncentral statistics by exactly a_k and ~1/lambda_max "
     "(measured 0.586 vs predicted 0.570; 0.362 vs 0.398): no observed-data transform restores "
     "destroyed Fisher information; conservatism is the price of null-side calibration.\n"
     "Standing: T+M.\nEvidence: @sec-ic-ladder-results."),
    ("I6", "I6  information-loss floor", "E", False,
     "Weak-signal cell (rho=0.10): oracle 0.820; no correction passes 0.650; the 0.17 residual "
     "is information loss, not calibration error. A measured floor, not an impossibility proof "
     "(G4).\nStanding: E.\nEvidence: @sec-ic-ladder-results."),
    ("I7", "I7  structural limits\nequality case; copulas", "T+M", False,
     "(a) The W3/ladder family is block-diagonal = L2's exact equality case (naive = exact to "
     "3.6e-15): the overstatement is invisible there, material only for constraints that do not "
     "block-decompose. (b) Per-model marginal transforms cannot calibrate a DIFFERENCE "
     "distribution (score copula invariant under marginal maps; measured 6.10 vs 10.00).\n"
     "Standing: T+M.\nEvidence: @sec-ic-ladder-results closing remark."),

    # --- Gaps ---
    ("G1", "G1  (A)+(C) magnitude\nnot independently pinned", "G", False,
     "The O(1/n) higher-order result is conditional on the -0.22 analytic anchor; direct MC is "
     "heavy-tailed and untrended (-0.34/-0.46/-0.29/+0.17). Firm: sign, order, MCAR vanishing; "
     "comparisons use only the paired differential."),
    ("G2", "G2  proper-MI carry-over\nnot separately measured", "G", False,
     "L1-L4 are proved and MC-confirmed for deterministic-FIML Qbar_inf; the proper-MI "
     "carry-over is argued structurally (shared posterior, shared draws), not measured."),
    ("G3", "G3  engine robustness\nempirical only", "G", False,
     "EMB vs exact data augmentation: sample RIV within 2-3% of observed-data RIV, W3 selection "
     "within 0.011 - empirical, scoped to designs studied; DA not run."),
    ("G4", "G4  floor is measured,\nnot proved", "G", False,
     "The 0.17 weak-signal residual is a measured floor, not a proof that no estimator built "
     "from the same observed data could do better."),
    ("G5", "G5  misspecification O(1)\ncan offset (A)+(C)", "G", False,
     "For dissimilar pairs a mechanism-independent misspecification O(1) coexists with the "
     "design-imbalance O(1) and can partially offset the net ranking bias; the MCAR contrast "
     "separates them in measurement only."),
    ("G6", "G6  MVN instantiation", "G", False,
     "The theorem is stated for general regular likelihoods with an estimated scale but verified "
     "only in the MVN family."),
]

# (source, relation, target, dashed?)
EDGES = [
    ("C1", "depends_on", "S1", False),
    ("C1", "depends_on", "S2", False),
    ("C1", "depends_on", "S3", False),
    ("C1", "depends_on", "S4", False),
    ("C1", "depends_on", "S5", False),
    ("C1", "depends_on", "S6", False),
    ("C1", "depends_on", "S7", False),
    ("C2", "extends", "C1", False),
    ("C1", "leads_to", "C3", False),
    ("C1", "leads_to", "C4", False),
    ("L2", "supports", "C3", False),
    ("L3", "enables", "C3", False),
    ("C3", "leads_to", "L5", False),
    ("C2", "necessitates", "L4", False),
    ("L4", "qualifies", "C4", True),
    ("L5", "leads_to", "C4", False),
    ("C3", "enables", "I4", False),
    ("I5", "qualifies", "I4", True),
    ("I6", "qualifies", "C4", True),
    ("I7", "qualifies", "L2", True),
    ("I7", "qualifies", "I4", True),
    ("C5", "qualifies", "C1", True),
    ("C5", "qualifies", "C4", True),
    ("S3", "qualifies", "C1", True),
    ("S4", "qualifies", "C1", True),
    # gap attachments
    ("G1", "qualifies", "C2", True),
    ("G2", "qualifies", "C3", True),
    ("G3", "qualifies", "C4", True),
    ("G4", "qualifies", "I6", True),
    ("G5", "qualifies", "L4", True),
    ("G6", "qualifies", "C1", True),
]


def main():
    repo = Path(__file__).resolve().parents[1]
    out_path = repo / "todo" / "030-concept-map.html"

    net = Network(height="950px", width="100%", directed=True,
                  bgcolor="#ffffff", font_color="#111827",
                  cdn_resources="in_line",
                  heading="mi-spectral argument map (todo/030) - hover a node for "
                          "statement, standing, evidence. Teal = proved + Monte Carlo (T+M), "
                          "blue = proved (T), orange = empirical (E), grey = gap (G). "
                          "Dashed edge = qualifies.")

    for node_id, label, standing, central, tooltip in NODES:
        net.add_node(
            node_id,
            label=label,
            title=tooltip,
            color=COLORS[standing],
            shape="dot",
            size=34 if central else (13 if standing == "G" else 19),
            borderWidth=3 if central else 1,
            font={"size": 22 if central else 14, "face": "Georgia"},
        )

    for src, rel, dst, dashed in EDGES:
        net.add_edge(src, dst, label=rel, dashes=dashed,
                     color="#9ca3af" if dashed else "#4b5563",
                     font={"size": 10, "color": "#6b7280", "align": "middle"},
                     arrows="to", smooth=True)

    net.barnes_hut(gravity=-14000, central_gravity=0.25,
                   spring_length=220, spring_strength=0.015, damping=0.4)

    html = net.generate_html(notebook=False)
    out_path.write_text(html, encoding="utf-8")
    print(f"written: {out_path}")


if __name__ == "__main__":
    main()
