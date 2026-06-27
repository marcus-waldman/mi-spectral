# S5 tribunal amendments (cross-family adversarial review, 2026-06-26)
#
# Source: tkal-reviews/tribunal-20260627T014721Z/ (challenges -> repo-grounded
# defense -> cross-family press round). Verdict AMEND. No result retracted, no
# headline number changed. The two unanimous "blockers" (W1 goalpost,
# block-diagonal luck) were rebutted on the evidence and survive only as wording;
# the "hidden failure" charge was rebutted by todo/005 (uncongenial/MNAR
# registered observational). Seven local edits remain. See VERDICT-SYNTHESIS.md.
#
# PLUS an outside-reader terminology pass (Marcus, 2026-06-26): the insider word
# "oracle" (complete-data sense) -> "complete-data benchmark" across all of S5 and
# the new G6, glossed once at first use; the two "fitted-versus-oracle" usages
# (S5-P5, S5-P13) reworded to "fitted-model-versus-true-model". NOTE: "oracle"
# still appears in S3 (x2) and S4 (x4); a consistent manuscript-wide sweep + a
# decisions.md terminology entry is a recommended follow-up, not done here.
#
# Edits (all draft_prose / pointer; the figures and numbers are unchanged):
#   1. S5-P22  tighten the engine-sensitivity pointer to the exact CSVs
#              (phase6-info tr_samp-vs-tr_obs = the 2-3%; phase2-w3 = the 0.011).
#   2. S5-P12  bridge: declare the 2.77 leading-order anchor first, then the
#              independently-derived dated O(1) MAR term (~-0.22) and the band;
#              "consistent with" both, not "confirms the completed theorem".
#   3. S5-P20  decouple the 0.824/0.904 naive-INPUT moment-map gap from
#              trace-formula superiority; point the latter to @prp-naive + Study 8.
#   4. S5-P17  W3C direction-not-mechanism rescope; note the registered prediction
#              held across all sixty cells; nested ordering makes saturated the sink.
#   5. S6-P4b  NEW G6 congeniality limit (fulfills the todo/005 H5 section-6
#              disclosure commitment; names the uncongenial overshoot).
#   6. S5-P15  localize the 52-sigma to the engineered cell; correctness rests on
#              the 2.64 match; "always overstates" attributed to @prp-naive.
#   7. S5-P18/P19  two-sided MCSE interval for "indistinguishable" + conjecture-
#              label the weak-cell attribution (P18); resolve the ncratio label
#              mapping a_k / 1-over-lambda-max with predicted-vs-measured (P19).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
L4 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level4-evidence.json"

W1 = "verif:verification/cache/W1-prod-fiml.rds"
PRE = "verif:todo/004-simulation-hypotheses.md"
MU1 = "verif:verification/cache/w2-paired-differential-mu1-cell.rds"
W3 = "verif:verification/cache/run_all-prod/phase2-w3/summary.csv"
LADDER = "verif:verification/cache/ic-ladder-summary.csv"
W4 = "verif:verification/cache/w4-nonnested-summary.csv"
W4D = "verif:verification/cache/w4-dissimilar-summary.csv"
P6INFO = "verif:verification/cache/run_all-prod/phase6-info/summary.csv"


def FIG(caption, fname, label, width):
    return "\n\n![" + caption + "](figures/" + fname + "){#" + label + " width=\"" + width + "\"}"


# ===================== amended result-paragraph prose =====================

P12 = (
    "## Simulation studies: results\n\n"
    "**Theorem validation.** The net deviance bias tracks the analytic half-trace "
    "across every sample size (@fig-w1-theorem). The preregistered target was the "
    "leading-order half-trace, near $2.77$. The completed theory of "
    "@sec-derivations adds an independently derived order-one missing-at-random "
    "term of about $-0.22$, obtained from the missingness mechanism after the run "
    "and recorded as a dated amendment, which shifts the prediction to the band "
    "$2.42$ to $2.55$. The inverse-variance pooled estimate is $2.43 \\pm 0.26$. "
    "Its interval contains the leading-order target $2.77$ at $1.3$ standard "
    "errors and centers on the augmented band, so the data are consistent with "
    "both. One cell is a genuine miss. At $N = 1000$ the estimate falls $2.6$ "
    "standard errors below the leading-order target, a consequence of the "
    "heavy-tailed per-repetition statistic, whose standard deviation grows with "
    "the sample size and leaves the larger cells unable to resolve an order-one "
    "offset at fixed repetition count. The component terms separately miss their "
    "targets by roughly $9$ to $20$ percent, which is why the grading reports only "
    "totals and paired differentials." +
    FIG(
        "**Theorem validation.** Each point is the net deviance bias "
        "$\\mathbb{E}[T]$ at one sample size with a $95$ percent interval, "
        "estimated on the analytic arm with $1000$ repetitions. Perfect is the "
        "analytic target, the dotted line at the preregistered half-trace $2.77$ "
        "and the shaded band at the order-one-augmented prediction $2.42$ to "
        "$2.55$. The solid line is the inverse-variance pooled estimate "
        "$2.43 \\pm 0.26$, whose interval contains the leading-order target and "
        "centers on the band. The $N = 1000$ cell falls $2.6$ standard errors "
        "below the leading-order target, the study's one reported miss.",
        "fig-w1-theorem.png", "fig-w1-theorem", "82%")
)

P15 = (
    "**Discrimination of the two formulas.** This run uses an adversarial design "
    "that makes one coordinate $70$ to $79$ percent missing, separating the two "
    "candidate formulas as widely as the design allows (@fig-discrimination). The "
    "observed differential is $2.64 \\pm 0.11$ at $N = 500$ and $2.70 \\pm 0.11$ "
    "at $N = 1000$, matching the projected-trace prediction of $2.64$. Correctness "
    "rests on that match. The same statistic sits $52$ standard errors from the "
    "naive trace difference, which excludes the naive formula in this engineered "
    "cell. That the naive difference always overstates the projected trace is the "
    "proved general statement of @prp-naive, and the size of the gap here reflects "
    "the maximal-separation design rather than typical balanced missingness." +
    FIG(
        "**Discrimination.** The observed paired differential at two sample sizes "
        "with $95$ percent intervals, from $2000$ repetitions on the "
        "heavy-missingness $\\mu_1$ design. Perfect is the projected-trace "
        "prediction $\\operatorname{tr}(\\mathrm{RIV}_\\perp) = 2.64$, the solid "
        "line. The naive trace difference, the dashed line near $8.5$, is excluded "
        "at $52$ standard errors in this maximal-separation cell.",
        "fig-discrimination.png", "fig-discrimination", "72%")
)

P17 = (
    "**Selection.** The uncorrected criterion favors high-missing-information "
    "models, and the correction moves selection back toward the complete-data "
    "benchmark (@fig-w3-selection). At $N = 500$ on the deterministic arm the "
    "complete-data benchmark selects the true model at $0.90$, the uncorrected "
    "criterion at $0.67$, and the corrected criterion at $0.82$. In every "
    "congenial cell all of the uncorrected criterion's errors land on the "
    "saturated, largest-missing-information candidate, a registered directional "
    "prediction that held across all sixty cells. Because the candidates are "
    "nested and ordered by missing information, the saturated model is the natural "
    "destination for any downward-biased deviance, so this pattern confirms the "
    "predicted direction of the bias rather than discriminating the specific "
    "decomposition. The recovery is substantial and visibly short of the "
    "complete-data benchmark, which is what the distribution-matching ladder was "
    "registered to explain." +
    FIG(
        "**Selection.** True-model selection rate by the Akaike criterion at "
        "three sample sizes on the non-monotone missing-at-random cell, $2000$ "
        "repetitions. Perfect is the complete-data benchmark, the dashed line and "
        "the black bar. The uncorrected criterion sits well below it and the "
        "correction recovers most of the gap. All uncorrected errors fall on the "
        "largest-missing-information candidate.",
        "fig-w3-selection.png", "fig-w3-selection", "82%")
)

P18 = (
    "**The distribution-matching ladder.** Across three levels of signal strength "
    "the stronger constructions recover the complete-data benchmark where the "
    "errors come from choosing too rich a model, and a floor remains where "
    "selection is genuinely hard (@fig-ladder). The true-model selection rates "
    "are reported below, with Monte Carlo standard error near $0.010$:\n\n"
    "| Cell | complete-data | uncorrected | mean | two-moment | equating |\n"
    "|---|---|---|---|---|---|\n"
    "| $\\rho = 0.40$ | 0.899 | 0.678 | 0.814 | 0.904 | 0.903 |\n"
    "| $\\rho = 0.10$ | 0.820 | 0.582 | 0.650 | 0.648 | 0.650 |\n"
    "| $\\rho = 0$ (junk) | 0.727 | 0.422 | 0.585 | 0.702 | 0.696 |\n\n"
    "At correlation $0.40$ the two-moment and equating arms reach $0.904$ and "
    "$0.903$ against the complete-data benchmark's $0.899$. The differences are "
    "within twice the Monte Carlo standard error of about $0.010$, so the arms are "
    "statistically indistinguishable from the benchmark, with a small overshoot "
    "the same interval does not resolve. The junk cell closes $90$ percent of the "
    "gap from uncorrected to benchmark. In the weak-signal cell the benchmark "
    "itself drops to $0.820$ and no arm passes $0.650$. We read that floor as a "
    "limit of the information in the data rather than a calibration error, an "
    "interpretation the calibration checks below support but do not separately "
    "decompose in the weak-signal cell. The residual is a measurement on these "
    "designs rather than a theorem." +
    FIG(
        "**Distribution-matching ladder.** True-model selection rate for four "
        "constructions in three cells at $N = 500$ with $2000$ repetitions. "
        "Perfect is the complete-data benchmark, the dashed line above each cell. "
        "At $\\rho = 0.40$ the two-moment and equating arms reach the benchmark. "
        "At $\\rho = 0.10$ no arm reaches it, the weak-signal floor.",
        "fig-ladder.png", "fig-ladder", "92%")
)

P19 = (
    "**Ladder internals.** Two internal measurements show why the ladder works "
    "(@fig-ladder-internals). On the true model's anchored statistic the "
    "distance to the paired complete-data statistic falls from $0.281$ under the "
    "uncorrected deviance to $0.019$ under equating, and the variance ratio "
    "falls from $3.18$ to near one. The mean correction's paired gap of "
    "$0.076 \\pm 0.100$ is a direct confirmation of @eq-lrt-bias at four tested "
    "directions. On the underfit candidate the noncentral statistic shrinks by "
    "its two predicted factors. The two-moment match shrinks it by the factor "
    "$a_k$, predicted near $0.56$ and measured at $0.59$, and equating shrinks it "
    "by $1/\\lambda_{\\max}$, predicted near $0.40$ and measured at $0.36$. The "
    "internal validity checks held on every repetition, with the spectrum-trace "
    "identity to $3 \\times 10^{-15}$ and no failure of the reference inversion in "
    "$18{,}000$ evaluations." +
    FIG(
        "**Ladder internals.** Left, the null-side Kolmogorov-Smirnov distance to "
        "the complete-data statistic across the four arms in the main cell. "
        "Perfect is zero, approached by the two-moment and equating arms, with "
        "the variance ratio falling from $3.18$ toward one. Right, the "
        "noncentral shrinkage factor measured against predicted on the line "
        "$y = x$. The two-moment and equating points sit on the diagonal.",
        "fig-ladder-internals.png", "fig-ladder-internals", "100%")
)

P20 = (
    "**The structural limits.** Three structural checks of @sec-derivations appear "
    "directly in the data, the equality case where the naive and projected traces "
    "coincide, the cost of the naive moment-map input, and the limit of a "
    "per-model map. The table reports them on the selection rates, with Monte "
    "Carlo standard error near $0.010$:\n\n"
    "| Structural limit | perfect | achieved |\n"
    "|---|---|---|\n"
    "| block-diagonal family, naive vs projected trace | exact equality | agree to $3.6 \\times 10^{-15}$ |\n"
    "| off-equality moment map, main-cell rate | complete-data $0.899$ | naive input $0.824$, correct input $0.904$ |\n"
    "| per-model map, equated difference mean and sd | complete-data $10.00$ and $7.10$ | $6.10$ and $5.99$ |\n\n"
    "Two points follow. In this block-diagonal candidate family the naive and "
    "projected traces coincide, to $3.6 \\times 10^{-15}$, so the family cannot by "
    "itself separate the two trace formulas. The $0.824$ against $0.904$ gap in "
    "the second row is therefore a cost of the naive moment-map input, not "
    "evidence about the trace formulas. The proof of @prp-naive establishes that "
    "the naive trace difference overstates the projected trace whenever the two "
    "differ, and the non-nested measurement of @fig-w4-nonnested supplies the "
    "measured off-equality case, about $9$ percent. The third row is separate "
    "again, showing that a per-model marginal map cannot calibrate the joint "
    "difference distribution."
)

# new G6 limitation paragraph (congeniality)
P4B = (
    "**G6.** The correction's guarantees assume congenial imputation, and "
    "uncongeniality is the practical boundary. When the imputation model shrinks "
    "the cross-block correlations the analysis estimates, as a strong ridge prior "
    "does, the deviance bias no longer points the way the theory assumes. In the "
    "sweep's uncongenial cells the uncorrected criterion already selects the true "
    "model more often than the complete-data benchmark, near $0.93$ against the "
    "benchmark's $0.91$, and the correction pushes past it to about $0.98$, an "
    "overshoot rather than a recovery. This behavior was registered as an "
    "observational stress test rather than a pass target, and it marks where the "
    "framework's safety margin ends. The practical recommendation is to diagnose "
    "congeniality before trusting bias-corrected selection."
)

PROSE = {"S5-P12": P12, "S5-P15": P15, "S5-P17": P17,
         "S5-P18": P18, "S5-P19": P19, "S5-P20": P20}

# audit.numbers replacements (pointer / description), applied after prose swap
NUMBERS = {
    "S5-P12": {"pooled 2.43 +/- 0.26; leading-order 2.77; dated O(1) MAR term ~-0.22; N=1000 2.6 se miss; components 9-20%": [W1, PRE],
               "fig-w1-theorem.png": "verif:manuscript/figures/fig-w1-theorem.png"},
    "S5-P19": {"KS 0.281->0.019; var 3.18->0.97; gap 0.076+/-0.100; two-moment a_k pred 0.56/meas 0.59; equating 1/lam_max pred 0.40/meas 0.36; 3e-15; 0/18000": LADDER,
               "fig-ladder-internals.png": "verif:manuscript/figures/fig-ladder-internals.png"},
    "S5-P22": {"sample-vs-observed RIV within 2-3% (tr_samp vs tr_obs)": P6INFO,
               "selection agreement within 0.011 (FIML vs EMB-congenial)": W3},
}

FLAG = "tribunal-amended 2026-06-26 (S5 cross-family adversarial review; verdict AMEND; tkal-reviews/tribunal-20260627T014721Z)"
TERMFLAG = "oracle -> complete-data benchmark (outside-reader terminology, 2026-06-26)"


# outside-reader pass: the complete-data sense of "oracle" -> "complete-data
# benchmark"; the fitted-versus-oracle contrast -> fitted-model-versus-true-model.
# Applied to the S5 paragraphs NOT rewritten above (P5,P6,P9,P10,P13). The gloss
# is added at the first design-stage use (P9).
def deoracle(t):
    t = t.replace("fitted-versus-oracle distinction", "fitted-model-versus-true-model distinction")
    t = t.replace("computed for the complete-data oracle,",
                  "computed for the complete-data benchmark, the result an analyst would reach with no missing data,")
    t = t.replace("complete-data oracle", "complete-data benchmark")
    t = t.replace("the oracle", "the complete-data benchmark")
    return t


with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = l3["paragraphs"]
by_id = {p["id"]: p for p in paras}

# --- apply prose + numbers + flag to the six result paragraphs ---
for pid, prose in PROSE.items():
    p = by_id[pid]
    p["draft_prose"] = prose
    p["review"]["flags"] = FLAG + " | " + TERMFLAG
    if pid in NUMBERS:
        p["audit"]["numbers"] = NUMBERS[pid]

# --- S5-P22 pointer-only fix (prose unchanged) ---
by_id["S5-P22"]["audit"]["numbers"] = NUMBERS["S5-P22"]
by_id["S5-P22"]["review"]["flags"] = FLAG

# --- outside-reader oracle pass: the complete-data sense only ---
# S5-P5/P13 carry the fitted-versus-oracle sense (handled inside deoracle); the
# rest are the complete-data-benchmark sense. S4-P21 is the same benchmark sense
# and is folded in for cross-section consistency. The oracle-CONDITIONING sense in
# S3-P6, S4-P4, S4-P7 is a distinct load-bearing term left for a separate decision.
for pid in ("S5-P5", "S5-P6", "S5-P9", "S5-P10", "S5-P13", "S4-P21"):
    p = by_id[pid]
    new = deoracle(p["draft_prose"])
    if new != p["draft_prose"]:
        p["draft_prose"] = new
        fl = p["review"].get("flags")
        p["review"]["flags"] = (fl + " | " if fl else "") + TERMFLAG

# guard: no stray complete-data-sense "oracle" left in S5 (the only remaining
# 'oracle' tokens, if any, would be inside math and are not expected here)
left = [p["id"] for p in paras if p.get("section") == "S5" and "oracle" in (p.get("draft_prose") or "")]
assert not left, f"oracle still present in S5: {left}"

# --- insert the new G6 congeniality paragraph right after S6-P4 ---
s6p4 = by_id["S6-P4"]
new_para = {
    "id": "S6-P4b", "section": "S6", "goal": "scope_limit",
    "proposition": "Congeniality limit (G6): under uncongenial imputation the uncorrected criterion can exceed the complete-data benchmark and the correction overshoots past it; registered observational (todo/005 H5); diagnose congeniality before trusting bias-corrected selection.",
    "depends_on": ["S6-P1", "S5-P17"], "dep_types": ["builds_on", "qualifies"],
    "review": {
        "serves_L2": s6p4["review"].get("serves_L2"),
        "serves_L1": s6p4["review"].get("serves_L1"),
        "sets_up": "-",
        "topic_sentence": "The correction's guarantees assume congenial imputation, and uncongeniality is the practical boundary.",
        "closing_sentence": "The practical recommendation is to diagnose congeniality before trusting bias-corrected selection.",
        "status": "drafted",
        "flags": "tribunal-added 2026-06-26: fulfills the todo/005 H5 section-6 disclosure commitment (uncongenial overshoot named); G-number G6 provisional, Marcus may renumber."
    },
    "draft_prose": P4B,
    "audit": {"status": "complete", "citations": {},
              "numbers": {"uncongenial uncorrected ~0.93 > benchmark ~0.91; corrected ~0.98 overshoot (benchmark-minus-corrected negative)": W3},
              "notes": "Congeniality scope limit; ends with the practical recommendation."}
}
pos = next(i for i, p in enumerate(paras) if p["id"] == "S6-P4")
paras.insert(pos + 1, new_para)

l3["metadata"]["status"] = "s5_tribunal_amended_2026-06-26"
l3["metrics_gate"]["notes"] = (
    "S5 tribunal amendments 2026-06-26 (cross-family adversarial review, verdict "
    "AMEND, no result retracted): S5-P12 W1 leading-order-anchor bridge; S5-P15 "
    "52-sigma localized to the engineered cell; S5-P17 W3C direction-not-mechanism; "
    "S5-P18 two-sided MCSE interval + weak-cell-floor wording; S5-P19 ncratio "
    "factors named (a_k / 1-over-lambda-max, predicted-vs-measured); S5-P20 "
    "moment-map decoupled from trace-formula superiority; S5-P22 engine-sensitivity "
    "pointer tightened to phase6-info + phase2-w3; NEW S6-P4b (G6) congeniality "
    "limit fulfilling the todo/005 H5 section-6 commitment. Outside-reader pass: "
    "'oracle' (complete-data sense) -> 'complete-data benchmark' across S5 + G6; "
    "follow-up needed for S3 (x2) and S4 (x4) + a decisions.md terminology entry. "
    "Section totals: S1 7 + S2 13 + S3 8 + S4 23 + S5 22 + S6 9 = 82 paragraphs."
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# ---- Level 4: split the S5-P22 engine-sensitivity pointer; add the S6-P4b entry ----
with open(L4, encoding="utf-8") as f:
    l4 = json.load(f)
em = l4["evidence_map"]

em[:] = [e for e in em if e.get("id") != "E-S5-P22-1"]
em.append({"id": "E-S5-P22-1", "proposition_id": "S5-P22", "pointer": P6INFO,
           "evidence_status": "verified",
           "passage_or_value": "tr_samp vs tr_obs: |sample RIV - observed-data RIV|/tr_obs ~ 2.1-2.6% (N200 2.6%, N500 2.1%), no widening with N.",
           "note": "Engine sensitivity, RIV agreement (exact file)."})
em.append({"id": "E-S5-P22-2", "proposition_id": "S5-P22", "pointer": W3,
           "evidence_status": "verified",
           "passage_or_value": "FIML vs EMB-congenial selection agreement within 0.011 on the recovery gap.",
           "note": "Engine sensitivity, selection agreement (exact file)."})
em.append({"id": "E-S6-P4b-1", "proposition_id": "S6-P4b", "pointer": W3,
           "evidence_status": "verified",
           "passage_or_value": "uncongenial cells: uncorrected ~0.93 > complete-data benchmark ~0.91; corrected ~0.98 (benchmark-minus-corrected negative).",
           "note": "Congeniality limit (tribunal 2026-06-26; fulfills todo/005 H5 section-6 commitment)."})

l4["metrics_gate"]["notes"] = "S1-S6 populated; S5 tribunal-amended 2026-06-26; S6 gains G6 congeniality limit. All pointers resolve. Full gate at compile."

with open(L4, "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S5 tribunal amendments applied:")
print("  prose swapped:", ", ".join(PROSE.keys()))
print("  oracle -> complete-data benchmark across S5 + G6")
print("  pointer fixed: S5-P22 (-> phase6-info + phase2-w3)")
print("  inserted: S6-P4b (G6 congeniality) after S6-P4")
print("  level4: E-S5-P22-1 split into 2 + E-S6-P4b-1 added")
print("  S6 now", sum(1 for p in paras if p.get("section") == "S6"), "paragraphs")
