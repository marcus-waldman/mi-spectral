# S5 Simulation studies - from-scratch draft (D-12), 2026-06-07
#
# Fifth Level-3 drafting cycle, under the approved S5 blueprint + D-03-A1 (S5 is
# now the paper's COMPLETE empirical account: everything moved out of S4 lands
# here). Subheads per D-09-A1: "Simulation studies: setup" / "Simulation studies:
# results". T-07: repetitions, never replications. D-05: failures in main text.
# Quarried from 180e2b5 sec-numerics (:824-:919) with all numbers verbatim;
# anchored statistic uses S4's renamed hat d_k family. 14 paragraphs (blueprint
# estimated 10-13; the D-03-A1 expansion accounts for the overshoot - flagged).
#   Setup:   P1 roadmap, P2 apparatus, P3 preregistration map, P4 grading protocol
#   Results: P5 theorem validation (incl. misses), P6 targeted experiments,
#            P7 LRT absorption, P8 discrimination, P9 pairing, P10 selection sweep,
#            P11 ladder (table + findings + internal checks), P12 structural-limit
#            exhibits, P13 non-nested (incl. the failed headline), P14 engine
#            sensitivity.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

P1 = (
    "## Simulation studies: setup\n\n"
    "This section is the paper's complete empirical account. Every quantitative claim "
    "in @sec-derivations points here, and every number here traces to a study whose "
    "predictions and pass criteria were committed before the study's code was written "
    "(@sec-methods). The setup is stated once. The results follow, study by study, "
    "including the predictions that were not met. Everything in this section carries "
    "the *measured* tier of @sec-methods unless stated otherwise."
)

P2 = (
    "**Apparatus.** All designs are multivariate normal, bivariate and four-variate, "
    "with monotone and non-monotone missingness patterns and MCAR, MAR, and MNAR "
    "mechanisms, the last for robustness arms only. Missingness rates are near 40% in "
    "the main cells. Two imputation arms are used. The deterministic arm evaluates "
    "$\\bar Q_\\infty$ analytically at the FIML estimate $\\hat\\theta_{\\text{obs}}$, "
    "which is the EM Q-function itself with no simulation error. The proper-MI arm "
    "draws imputations by expectation-maximization with bootstrapping, as implemented "
    "in Amelia [@honakerAmeliaIIProgram2011]: EM is run on bootstrap resamples of the "
    "incomplete data to obtain approximate posterior draws of $(\\mu, \\Sigma)$, and "
    "completions are drawn at those values. The exact alternative, data augmentation, "
    "was not run. The resulting scope limit is stated with the engine-sensitivity "
    "result below and in @sec-discussion."
)

P3 = (
    "**The studies and their registrations.** Six study groups appear below. The "
    "bias-decomposition, likelihood-ratio, and selection studies were preregistered "
    "together and frozen before any engine code existed. The distribution-matching "
    "contrast and the non-nested measurement each carry their own preregistration, "
    "committed before their scripts, with dated amendments in the documents' version "
    "histories. The targeted experiments, the sign-regime and known-scale runs, are "
    "dedicated single-question designs. All runs use fixed seeds and single "
    "entry-point scripts, outputs are cached as committed artifacts, and the software "
    "environment is recorded, as @sec-methods states."
)

P4 = (
    "**Grading.** Each study is graded against its frozen pass criteria, and two "
    "reporting rules apply throughout. Failed predictions are reported here, in the "
    "main text, beside the successes. And every quantitative claim is stated for "
    "totals and paired differentials, never for components, for a reason the first "
    "study makes concrete."
)

P5 = (
    "## Simulation studies: results\n\n"
    "**Theorem validation.** The preregistered bias-decomposition study estimates "
    "$\\mathbb{E}[T_{\\text{imp}}]$, $\\mathbb{E}[T_{\\text{est}}]$, and "
    "$\\mathbb{E}[T]$ across patterns, mechanisms, and sample sizes against the "
    "analytic $\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$. One caveat is part of the "
    "record. The study was preregistered against the half-trace alone, before the "
    "$O(1)$ MAR term had been derived, and the per-replicate statistic is heavy-tailed "
    "with standard deviation growing as $\\sqrt n$, so at fixed repetition count the "
    "larger-$n$ cells cannot resolve an $O(1)$ offset. One cell, $N = 1000$, misses "
    "the original target at $2.6$ standard errors. Pooling the four sample sizes by "
    "inverse variance gives $\\hat T = 2.43 \\pm 0.26$ against the preregistered "
    "target $2.77$ and the $(A)+(C)$-augmented range $2.42$ to $2.55$. The pooled "
    "preregistered data corroborate the completed theorem, under a criterion "
    "amendment documented in the preregistration's version history. At the component "
    "level the individual terms miss their targets by roughly 9% to 20% at the sample "
    "sizes studied, with $\\mathbb{E}[T_{\\text{est}}]$ overshooting its "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ target by $-0.3$ to $-0.55$ at "
    "tight Monte Carlo error. This is why the totals-and-differentials rule of the "
    "grading protocol exists."
)

P6 = (
    "**Targeted experiments.** Two dedicated runs complete the theorem's picture. "
    "Imputing from the truth instead of the fitted model reverses the sign of the "
    "total exactly as the fitted-versus-oracle distinction of @sec-derivations "
    "requires. The known-scale experiment, at $R = 2 \\times 10^5$ repetitions, "
    "reproduces all four values of @eq-knownscale within 4%: zero and "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ across the deterministic and "
    "proper arms, the pair differing by exactly the posterior-draw contribution."
)

P7 = (
    "**Likelihood-ratio absorption.** The preregistered rejection study confirms the "
    "absorption property. The uncorrected numerator referred to Chan's simulated "
    "reference rejects at $0.042$ at the null, and additionally correcting the "
    "numerator gives $0.034$, slightly conservative, as double-counting predicts. One "
    "scope note travels with this study: its committed correction arm used the naive "
    "trace difference as input, and in its near-invariance design the difference from "
    "@eq-lrt-bias is about 5% and immaterial, but @eq-lrt-bias is the correct general "
    "form. The study's power arms, with a post-hoc size-adjusted analysis, are the "
    "partial empirical support cited for the power conjecture of @sec-discussion."
)

P8 = (
    "**Discrimination of the two formulas.** The dedicated experiment for @prp-lrt "
    "ran $R = 2000$ repetitions on the $\\mu_1$ design, where the tested direction "
    "mixes unequally-missing information and the two candidate formulas separate "
    "widely: @eq-lrt-bias gives $2.64$ and the naive difference gives $8.47$. The "
    "observed differentials are $2.639 \\pm 0.113$ at $N = 500$ and "
    "$2.701 \\pm 0.112$ at $N = 1000$, on the predicted value to within sampling "
    "error and $52$ standard errors from the naive value."
)

P9 = (
    "**Pairing.** The noise-collapse study behind @prp-pairing measured the "
    "single-model standard deviation growing $18.4$, $26.6$, $36.5$ across "
    "$N = 500$, $1000$, $2000$ at the null, while the paired differential stayed "
    "flat at $1.58$, $1.47$, $1.57$. At the fixed alternative the $\\sqrt n$ growth "
    "returns, at $12.4$, $16.8$, $24.9$, exactly as the proposition's failure mode "
    "specifies."
)

P10 = (
    "**Selection.** The committed 60-cell selection sweep produced the directional "
    "signature @sec-derivations predicts. At $N = 500$ under deterministic FIML, "
    "complete-data AIC selects the true model at $0.898$, uncorrected MI-AIC at "
    "$0.674$, and the corrected criterion at $0.816$. In every congenial cell, 100% "
    "of the uncorrected criterion's misclassifications land on the saturated, "
    "largest-RIV candidate. The recovery is substantial and visibly short of the "
    "oracle, which is what the distribution-matching contrast was preregistered to "
    "explain."
)

P11 = (
    "**The distribution-matching contrast.** Three cells at $N = 500$ with "
    "$R = 2000$ repetitions each: the preregistered design at $\\rho = 0.40$, a "
    "weak-signal stress cell at $\\rho = 0.10$ with near-tied candidates, and a junk "
    "cell at $\\rho = 0$ where the truth is diagonal and every anchored statistic is "
    "null-type. True-model selection rates, with Monte Carlo standard error near "
    "$0.010$:\n\n"
    "| Cell | oracle | uncorrected | mean | two-moment | equating |\n"
    "|---|---|---|---|---|---|\n"
    "| $\\rho = 0.40$ | 0.899 | 0.678 | 0.814 | 0.904 | 0.903 |\n"
    "| $\\rho = 0.10$ | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 |\n"
    "| $\\rho = 0$ (junk) | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 |\n\n"
    "Every preregistered pass criterion was met, and four findings summarize the "
    "table. First, the null side calibrates completely. On the true model's anchored "
    "statistic the Kolmogorov-Smirnov distance to the paired complete-data statistic "
    "falls $0.281$, $0.228$, $0.026$, $0.019$ across the four arms, and the variance "
    "ratio falls from $3.18$ to $0.97$. The mean correction's paired gap, "
    "$0.076 \\pm 0.100$, is itself a direct confirmation of @eq-lrt-bias at "
    "$q_{\\mathrm{d}} = 4$. Second, where overfit flips drive the errors, "
    "distribution matching reaches the oracle: the two-moment and equating arms "
    "select at $0.904$ and $0.903$ against the oracle's $0.899$, statistically "
    "indistinguishable, and the junk cell closes 90% of the uncorrected-to-oracle "
    "gap. Third, the noncentral side shrinks as the law predicts. The underfit "
    "candidate's mean statistic, relative to its complete-data counterpart, is "
    "$1.002$ under the mean correction, $0.586$ under two moments against the "
    "predicted $a_k = 0.570$, and $0.362$ under equating against the predicted "
    "far-tail factor $1/\\lambda_{\\max} = 0.398$. Fourth, where selection is "
    "genuinely hard, nothing closes the floor. In the weak-signal cell the oracle "
    "itself drops to $0.820$ and no correction passes $0.650$; the stronger arms' "
    "null-side gains are fully offset by underfit retention, at rate $0.270$ against "
    "the oracle's $0.091$. The $0.17$ residual is information loss, not calibration "
    "error, and it is a measurement on these designs rather than a theorem. The "
    "internal validity checks held on every repetition: the spectrum-trace identity "
    "to $3 \\times 10^{-15}$, every null-law weight at least one, and zero failures "
    "of the characteristic-function inversion in 18,000 evaluations, so the "
    "preregistered simulated-reference fallback was never invoked."
)

P12 = (
    "**The structural limits, exhibited.** Both proved limits of @sec-derivations "
    "appear in the data. The candidate family is block-diagonal, and the naive trace "
    "difference agrees with the exact projected trace to $3.6 \\times 10^{-15}$, the "
    "equality case made visible. An earlier sweep arm that applied a moment map "
    "built from naive-difference inputs scores $0.824$ in the $\\rho = 0.40$ cell "
    "against the derived two-moment arm's $0.904$, which is what the overstatement "
    "costs when the inputs are wrong off the equality case. And per-model marginal "
    "maps leave difference distributions uncalibrated: in the weak-signal near-tied "
    "pair the equated score difference has mean $6.10$ and standard deviation "
    "$5.99$ against the complete-data difference's $10.00$ and $7.10$."
)

P13 = (
    "**The non-nested measurement.** A preregistered measurement at "
    "$N \\in \\{500, 1000, 2000\\}$ with $20{,}000$ repetitions per cell, and an "
    "MCAR twin isolating the mechanism, targeted the one derived-but-unmeasured "
    "quantity in @sec-derivations: the design-imbalance differential of "
    "@prp-ac-diff for genuinely separated pairs. The mechanism was confirmed "
    "exactly. Each candidate's $(A)+(C)$ level is a large $O(1)$, near $+2.5$ "
    "deviance units and tens of standard errors from zero, and it collapses to zero "
    "under MCAR. The two candidates' levels decouple, at $+2.33$ against $+2.85$. "
    "The paired noise returns to $O(\\sqrt n)$, and a nested-but-false restriction "
    "triggers the same return, confirming that separation rather than nesting is "
    "the criterion. The preregistered headline for the similar pair, compound "
    "symmetry against AR(1), was not met. Its differential sits below Monte Carlo "
    "resolution, and a pilot's apparent $-2$ dissolved in the full run. We report "
    "that failure as the discipline requires. The preregistered dissimilar-pair "
    "follow-up, a structure-blind diagonal model against AR(1) committed before its "
    "code, resolved the predicted scaling: an isolated design-imbalance "
    "differential of $-1.2$, at $3.5$ standard errors from zero, three to four "
    "times the similar pair's bound and stable across $N$. A byproduct supplied the "
    "first measured case off the equality condition of @prp-naive: for these curved "
    "candidates the naive trace difference overstates the exact projected trace by "
    "about 9%."
)

P14 = (
    "**Engine sensitivity.** On the most demanding cells, non-monotone MAR with $N$ "
    "as small as $200$, where the bootstrap approximation to the imputation "
    "posterior is weakest, the sample RIV built from the EMB draws reproduces the "
    "observed-data RIV within 2% to 3%, with no widening as $N$ grows, and model "
    "selection agrees between deterministic FIML and the EMB analysis within "
    "$0.011$ on the recovery gap. This robustness is empirical and scoped to the "
    "designs studied. The EMB sampler is only approximately Bayesian, data "
    "augmentation was not run, and a fully Bayesian sampler remains the "
    "conservative choice when the fraction of missing information is large "
    "(@sec-discussion)."
)

def mk(idx, goal, proposition, dep, deptypes, prose, serves_L2, sets_up, topic, closing, flags, citations, numbers, notes):
    return {
        "id": idx, "section": "S5", "goal": goal, "proposition": proposition,
        "depends_on": dep, "dep_types": deptypes,
        "review": {"serves_L2": serves_L2, "serves_L1": "M4b SIMULATION STUDIES (D-03-A1 full empirical account; D-05 failures in main text; T-07)",
                   "sets_up": sets_up, "topic_sentence": topic, "closing_sentence": closing,
                   "status": "drafted", "flags": flags},
        "draft_prose": prose,
        "audit": {"status": "complete", "citations": citations, "numbers": numbers, "notes": notes}
    }

RUNALL = "verif:verification/cache/run_all-prod"
LADDER = "verif:verification/cache/ic-ladder-summary.csv"
W4 = "verif:verification/cache/w4-nonnested-summary.csv"

s5 = [
    mk("S5-P1", "transition", "Roadmap: the complete empirical account; predictions frozen before code; failures included; measured tier.",
       ["S4-P22", "S3-P5"], ["builds_on", "builds_on"], P1, "S5-SP1 (framing)", "all S5",
       "This section is the paper's complete empirical account.",
       "Everything in this section carries the *measured* tier of @sec-methods unless stated otherwise.",
       "S5 drafted at 14 paragraphs vs blueprint estimate 10-13 (D-03-A1 moved all empirics here; flagged for Marcus).",
       {}, {}, "Setup subhead opens here (D-09-A1)."),
    mk("S5-P2", "define_concept", "Apparatus: MVN designs, patterns, mechanisms, rates; deterministic-FIML analytic arm vs EMB/Amelia proper arm; DA not run.",
       ["S5-P1"], ["builds_on"], P2, "S5-SP1", "P14; S6 G3",
       "All designs are multivariate normal, bivariate and four-variate, with monotone and non-monotone missingness patterns and MCAR, MAR, and MNAR mechanisms, the last for robustness arms only.",
       "The resulting scope limit is stated with the engine-sensitivity result below and in @sec-discussion.",
       None,
       {"honakerAmeliaIIProgram2011": "verified (read in-session 2026-06-07; EMB description verbatim at :37)"},
       {}, "Quarried from 180e2b5 Apparatus."),
    mk("S5-P3", "define_concept", "The six study groups and their preregistration/amendment structure; seeds, entry points, caches, environment records.",
       ["S5-P2"], ["builds_on"], P3, "S5-SP1", "P5-P14",
       "Six study groups appear below.",
       "...as @sec-methods states.",
       None, {},
       {"preregistration docs": "verif:todo/004-simulation-hypotheses.md + verif:todo/005-comprehensive-sweep-hypotheses.md + verif:todo/027-ladder-preregistration.md",
        "entry points": "verif:verification/run_all.R + verif:verification/ic-ladder.R"},
       "Registration map."),
    mk("S5-P4", "define_concept", "Grading protocol: frozen criteria; failures in main text (D-05); totals-and-differentials rule.",
       ["S5-P3"], ["builds_on"], P4, "S5-SP1", "P5 (the rule's reason)",
       "Each study is graded against its frozen pass criteria, and two reporting rules apply throughout.",
       "...for a reason the first study makes concrete.",
       None, {}, {}, "Protocol statement."),
    mk("S5-P5", "evaluate_evidence", "Theorem validation: pooled 2.43+/-0.26 vs 2.77 prereg / 2.42-2.55 augmented; N=1000 miss at 2.6 se; component 9-20% misses; the totals rule's reason.",
       ["S5-P4", "S4-P8"], ["builds_on", "instantiates"], P5, "S5-SP2 + SP3 (the W1 miss reported)", "S6 G1",
       "The preregistered bias-decomposition study estimates [the three expectations] against the analytic half-trace.",
       "This is why the totals-and-differentials rule of the grading protocol exists.",
       None, {},
       {"2.43 +/- 0.26; targets 2.77 / 2.42-2.55; 2.6 se miss; 9-20% component misses; T_est overshoot -0.3 to -0.55": RUNALL},
       "Results subhead opens here. W1 grading incl. the caveat + amendment."),
    mk("S5-P6", "evaluate_evidence", "Targeted experiments: sign-regime reversal; known-scale four values within 4% at R=2e5.",
       ["S5-P5", "S4-P4"], ["builds_on", "instantiates"], P6, "S5-SP2", "S4-P4/P8 backfill",
       "Two dedicated runs complete the theorem's picture.",
       "...the pair differing by exactly the posterior-draw contribution.",
       None, {},
       {"sign reversal; four knownscale values within 4% (R=2e5)": "verif:verification/cache/rederivation-knownvar-N200-R20000.rds"},
       "The fitted-vs-oracle and known-scale receipts."),
    mk("S5-P7", "evaluate_evidence", "Absorption: 0.042 / 0.034; naive-input scope note (~5%, immaterial in the near-invariance design); power arms -> conjecture support.",
       ["S5-P4", "S4-P14"], ["builds_on", "instantiates"], P7, "S5-SP2", "S6 SP2 (conjecture)",
       "The preregistered rejection study confirms the absorption property.",
       "...the partial empirical support cited for the power conjecture of @sec-discussion.",
       None, {},
       {"0.042 / 0.034 null rates; ~5% naive-input note": "verif:verification/cache/W2-prod-amelia.rds"},
       "W2 grading."),
    mk("S5-P8", "evaluate_evidence", "Discrimination: 2.639+/-0.113 and 2.701+/-0.112 vs predicted 2.64, naive 8.47; 52 se.",
       ["S5-P4", "S4-P10"], ["builds_on", "instantiates"], P8, "S5-SP2", "-",
       "The dedicated experiment for @prp-lrt ran $R = 2000$ repetitions on the $\\mu_1$ design.",
       "...$52$ standard errors from the naive value.",
       None, {},
       {"2.639 +/- 0.113 / 2.701 +/- 0.112 vs 2.64 / 8.47; 52 se": RUNALL},
       "The I_com-metric discrimination receipt."),
    mk("S5-P9", "evaluate_evidence", "Pairing: sd 18.4/26.6/36.5 vs 1.58/1.47/1.57; fixed-alternative return 12.4/16.8/24.9.",
       ["S5-P4", "S4-P12"], ["builds_on", "instantiates"], P9, "S5-SP2", "-",
       "The noise-collapse study behind @prp-pairing measured the single-model standard deviation growing $18.4$, $26.6$, $36.5$ across $N = 500$, $1000$, $2000$ at the null, while the paired differential stayed flat at $1.58$, $1.47$, $1.57$.",
       "...exactly as the proposition's failure mode specifies.",
       None, {}, {"sd table + alternative return": RUNALL}, "Pairing receipt."),
    mk("S5-P10", "evaluate_evidence", "Selection sweep: 0.898 / 0.674 / 0.816; 100% saturated-candidate misclassifications in every congenial cell.",
       ["S5-P4", "S4-P18"], ["builds_on", "instantiates"], P10, "S5-SP2", "P11",
       "The committed 60-cell selection sweep produced the directional signature @sec-derivations predicts.",
       "...what the distribution-matching contrast was preregistered to explain.",
       None, {}, {"0.898 / 0.674 / 0.816; 100% signature": RUNALL}, "W3 grading."),
    mk("S5-P11", "evaluate_evidence", "Ladder: the table + four findings (KS fall, oracle reached, exact shrinkage, the floor) + internal validity checks.",
       ["S5-P10", "S4-P21"], ["builds_on", "instantiates"], P11, "S5-SP2 + SP3", "S6 verdict",
       "Three cells at $N = 500$ with $R = 2000$ repetitions each.",
       "...the preregistered simulated-reference fallback was never invoked.",
       None, {},
       {"table; KS 0.281->0.019; var 3.18->0.97; gap 0.076+/-0.100; 0.904/0.903 vs 0.899; junk 90%; 1.002/0.586 vs 0.570/0.362 vs 0.398; floor 0.17 (0.270 vs 0.091); 3e-15; weights>=1; 0/18000": LADDER},
       "Ladder grading; all C1-C6 met."),
    mk("S5-P12", "evaluate_evidence", "Structural-limit exhibits: 3.6e-15 equality; naive-input arm 0.824 vs 0.904; difference distribution 6.10/5.99 vs 10.00/7.10.",
       ["S5-P11", "S4-P22"], ["builds_on", "instantiates"], P12, "S5-SP2", "-",
       "Both proved limits of @sec-derivations appear in the data.",
       "...against the complete-data difference's $10.00$ and $7.10$.",
       None, {},
       {"3.6e-15; 0.824 vs 0.904; 6.10/5.99 vs 10.00/7.10": LADDER},
       "The exhibits forward-pointed from S4-P22."),
    mk("S5-P13", "evaluate_evidence", "Non-nested: mechanism confirmed (+2.5 level, MCAR collapse, 2.33/2.85 decoupling, sqrt-n return, nested-false trigger); similar-pair headline NOT met; dissimilar -1.2 at 3.5 se; 9% naive overstatement byproduct.",
       ["S5-P4", "S4-P13"], ["builds_on", "instantiates"], P13, "S5-SP2 + SP3 (the failed headline)", "S6 G5",
       "A preregistered measurement at $N \\in \\{500, 1000, 2000\\}$ with $20{,}000$ repetitions per cell, and an MCAR twin isolating the mechanism, targeted the one derived-but-unmeasured quantity in @sec-derivations.",
       "...the naive trace difference overstates the exact projected trace by about 9%.",
       None, {},
       {"+2.5 level (tens of se); 2.33/2.85; MCAR collapse; similar-pair below resolution (pilot -2 dissolved); dissimilar -1.2 at 3.5 se; ~9% overstatement": W4},
       "W4 grading incl. the reported failure (D-05)."),
    mk("S5-P14", "scope_limit", "Engine sensitivity: EMB within 2-3% on the RIV and 0.011 on selection; empirical, scoped; DA not run.",
       ["S5-P2", "S5-P10"], ["builds_on", "builds_on"], P14, "S5-SP4", "S6 G3",
       "On the most demanding cells, non-monotone MAR with $N$ as small as $200$, where the bootstrap approximation to the imputation posterior is weakest, the sample RIV built from the EMB draws reproduces the observed-data RIV within 2% to 3%.",
       "...a fully Bayesian sampler remains the conservative choice when the fraction of missing information is large (@sec-discussion).",
       None, {}, {"2-3% RIV; 0.011 selection": RUNALL}, "Engine-sensitivity scoping."),
]

l3["paragraphs"].extend(s5)
l3["metadata"]["status"] = "drafting_s5_complete"
l3["metrics_gate"]["notes"] = (
    "After S5 drafting (2026-06-07): S1 7 + S2 13 + S3 8 + S4 23 + S5 14 = 65 "
    "paragraphs. S5 is the complete empirical account (D-03-A1); failures reported "
    "in main text (D-05); 'repetitions' throughout (T-07); all numbers pointered to "
    "committed caches. Remaining: S6. Regeneration gate running in background."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)

l4["evidence_map"].extend([
    {"id": "E-S5-P2-1", "proposition_id": "S5-P2", "pointer": "lit:honakerAmeliaIIProgram2011", "evidence_status": "verified",
     "passage_or_value": ":37 EMB algorithm description (EM on bootstrap resamples; draws at bootstrapped parameters).", "note": "Engine citation."},
    {"id": "E-S5-P5-1", "proposition_id": "S5-P5", "pointer": RUNALL, "evidence_status": "verified",
     "passage_or_value": "Pooled 2.43 +/- 0.26; 2.77 prereg / 2.42-2.55 augmented; N=1000 2.6 se; components 9-20%.", "note": "W1 grading."},
    {"id": "E-S5-P6-1", "proposition_id": "S5-P6", "pointer": "verif:verification/cache/rederivation-knownvar-N200-R20000.rds", "evidence_status": "verified",
     "passage_or_value": "Known-scale four arms within 4%; sign-regime reversal companion run.", "note": "Targeted experiments."},
    {"id": "E-S5-P7-1", "proposition_id": "S5-P7", "pointer": "verif:verification/cache/W2-prod-amelia.rds", "evidence_status": "verified",
     "passage_or_value": "0.042 / 0.034 null rates.", "note": "Absorption + double-counting."},
    {"id": "E-S5-P8-1", "proposition_id": "S5-P8", "pointer": RUNALL, "evidence_status": "verified",
     "passage_or_value": "2.639 +/- 0.113, 2.701 +/- 0.112 vs 2.64 / 8.47.", "note": "52-se discrimination."},
    {"id": "E-S5-P9-1", "proposition_id": "S5-P9", "pointer": RUNALL, "evidence_status": "verified",
     "passage_or_value": "sd 18.4/26.6/36.5 vs 1.58/1.47/1.57; alt 12.4/16.8/24.9.", "note": "Pairing receipt."},
    {"id": "E-S5-P10-1", "proposition_id": "S5-P10", "pointer": RUNALL, "evidence_status": "verified",
     "passage_or_value": "0.898 / 0.674 / 0.816; 100% saturated misclassifications.", "note": "W3 headline."},
    {"id": "E-S5-P11-1", "proposition_id": "S5-P11", "pointer": LADDER, "evidence_status": "verified",
     "passage_or_value": "Full table + KS/variance/shrinkage/floor + internal checks.", "note": "Ladder grading."},
    {"id": "E-S5-P12-1", "proposition_id": "S5-P12", "pointer": LADDER, "evidence_status": "verified",
     "passage_or_value": "3.6e-15; 0.824 vs 0.904; 6.10/5.99 vs 10.00/7.10.", "note": "Structural exhibits."},
    {"id": "E-S5-P13-1", "proposition_id": "S5-P13", "pointer": W4, "evidence_status": "verified",
     "passage_or_value": "+2.5 level; 2.33/2.85; similar below resolution; dissimilar -1.2 (3.5 se); ~9%.", "note": "W4 incl. reported failure."},
    {"id": "E-S5-P14-1", "proposition_id": "S5-P14", "pointer": RUNALL, "evidence_status": "verified",
     "passage_or_value": "EMB vs observed-data RIV 2-3%; selection within 0.011.", "note": "Engine sensitivity."},
])
l4["metrics_gate"]["notes"] = "S1-S5 populated; all pointers resolve. Full gate when S6 drafted."

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S5 drafted: 14 paragraphs, 12 evidence entries")
