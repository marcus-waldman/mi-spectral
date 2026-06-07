# Punctuation-budget sweep across all six sections, 2026-06-07
#
# Marcus (on S6): "So many damn colons. Some incomplete sentences." A mechanical
# detector pass found rhetorical colons and fragments across S1-S6 (S1/S2 predate
# the budget; S5/S6 violated it fresh). This sweep converts every rhetorical colon
# to full sentences and removes the Firm:/Not firm: fragments. KEPT per the
# budget: colons introducing displays, tables, definitions of named objects, and
# verbatim quotations; semicolons inside citation brackets and math spacing.
# Idempotent: each replacement skips if already applied.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = {p["id"]: p for p in l3["paragraphs"]}

EDITS = [
("S1-P3",
 "We call it the *complete-data replication principle*: a procedure",
 "We call it the *complete-data replication principle*. A procedure"),
("S1-P3",
 "decision rates match: the same model is selected",
 "decision rates match. The same model is selected"),
("S1-P4",
 "The fix is direct: add each candidate's own trace back to its criterion.",
 "The fix is direct. Add each candidate's own trace back to its criterion."),
("S1-P5",
 "asks for more: the same decisions at the same rates as the complete data.",
 "asks for more. It asks for the same decisions at the same rates as the complete data."),
("S1-P5",
 "The practical reading is this: corrected criteria are honest, not clairvoyant.",
 "The practical reading is this. Corrected criteria are honest, not clairvoyant."),
("S1-P6",
 "The two are complementary: calibration makes the reference distribution right, and",
 "The two are complementary. Calibration makes the reference distribution right, and"),
("S1-P7",
 "and the title page declares it: the derivations are AI-assisted",
 "and the title page declares it. The derivations are AI-assisted"),
("S2-P1",
 "Second, the standing assumptions: ignorable missingness, and congenial, proper imputation.",
 "Second, the standing assumptions of ignorable missingness and congenial, proper imputation."),
("S2-P1",
 "Fourth, the machinery behind the averaged log-likelihood: the EM Q-function, its Monte Carlo implementation, and Rubin's combining rules.",
 "Fourth, the machinery behind the averaged log-likelihood, from the EM Q-function through its Monte Carlo implementation to Rubin's combining rules."),
("S2-P3",
 "The assumption and its conditions are Rubin's [@rubinInferenceMissingData1976b]: the data must be missing at random --- the conditional probability of the observed missingness pattern is the same for all values of the missing data --- and the mechanism's parameter must be distinct from the data parameter.",
 "The assumption and its conditions are Rubin's [@rubinInferenceMissingData1976b]. The data must be missing at random, meaning the conditional probability of the observed missingness pattern is the same for all values of the missing data. The mechanism's parameter must also be distinct from the data parameter."),
("S2-P4",
 "together with a score identity: the observed-data score is the conditional expectation of the complete-data score.",
 "together with a score identity. The observed-data score is the conditional expectation of the complete-data score."),
("S2-P4",
 "The EM literature works with a different normalization of the same ingredients: the EM rate matrix",
 "The EM literature works with a different normalization of the same ingredients. The EM rate matrix"),
("S2-P5",
 "This single geometric fact drives the likelihood-ratio result: constrained fits",
 "This single geometric fact drives the likelihood-ratio result. Constrained fits"),
("S2-P6",
 "implement the E-step by simulation: draws",
 "implement the E-step by simulation. Draws"),
("S2-P6",
 "One feature of this construction must be marked at once: the draws are taken at a *fixed* parameter value --- the current iterate, or in the limit the observed-data estimate.",
 "One feature of this construction must be marked at once. The draws are taken at a *fixed* parameter value, the current iterate or in the limit the observed-data estimate."),
("S2-P7",
 "Proper imputation propagates parameter uncertainty: a parameter value is first drawn",
 "Proper imputation propagates parameter uncertainty. A parameter value is first drawn"),
("S2-P7",
 "and the main theorem prices it exactly: in the known-scale case",
 "and the main theorem prices it exactly. In the known-scale case"),
("S2-P7",
 "Properness is also not absolute: @nielsenProperImproperMultiple2003 shows",
 "Properness is also not absolute. @nielsenProperImproperMultiple2003 shows"),
("S2-P9",
 "The second standing assumption is congeniality: the imputer and the analyst agree.",
 "The second standing assumption is congeniality. The imputer and the analyst must agree."),
("S2-P9",
 "This assumption is what gives the main theorem its force: the bias derived there",
 "This assumption is what gives the main theorem its force. The bias derived there"),
("S2-P12",
 "One convention must be fixed before any trace in this paper is computed: which information matrix to use under MAR.",
 "One convention must be fixed before any trace in this paper is computed. The question is which information matrix to use under MAR."),
("S2-P12",
 "example shows where the difference lodges: under MAR dropout",
 "example shows where the difference lodges. Under MAR dropout"),
("S2-P13",
 "drops the equal-fractions assumption entirely: stacking the imputed data sets yields",
 "drops the equal-fractions assumption entirely. Stacking the imputed data sets yields"),
("S2-P13",
 "That excess matters later: a reference built this way absorbs",
 "That excess matters later. A reference built this way absorbs"),
("S3-P2",
 "An example of the human direction is on record: the author caught",
 "An example of the human direction is on record. The author caught"),
("S4-P1",
 "which is the answer to the replication principle's second level: it prices the bias",
 "which is the answer to the replication principle's second level. It prices the bias"),
("S4-P3",
 "The convention: under MAR the expectation defining $I_{\\text{obs}}$ is taken unconditionally",
 "The convention is fixed first. Under MAR the expectation defining $I_{\\text{obs}}$ is taken unconditionally"),
("S4-P3",
 "The warning repeats @sec-background in local form: the fraction-of-missing-information matrix",
 "The warning repeats @sec-background in local form. The fraction-of-missing-information matrix"),
("S4-P7",
 "the gradient is supported entirely "
 "on the covariance parameters: $\\alpha_\\mu = 0$ and",
 "the gradient is supported entirely "
 "on the covariance parameters, with $\\alpha_\\mu = 0$ and"),
("S2-P10",
 "and it is too optimistic: it \"needs",
 "and it is too optimistic. It \"needs"),
("S2-P13",
 "repair the procedure's known "
 "defects by switching the order of operations: their statistic",
 "repair the procedure's known "
 "defects by switching the order of operations. Their statistic"),
("S4-P19",
 "pre-registered in full before any code was written: match the first moment, "
 "the first two moments, or the entire null distribution, and measure what each "
 "step achieves.",
 "pre-registered in full before any code was written. Match the first moment, "
 "the first two moments, or the entire null distribution, and measure what each "
 "step achieves."),
("S4-P19",
 "statistic with a "
 "constructible per-model null law: the analytic weights",
 "statistic with a "
 "constructible per-model null law. The analytic weights"),
("S4-P20",
 "standard repair in the "
 "structural-equation tradition: the Satorra-Bentler scaled difference statistic",
 "standard repair in the "
 "structural-equation tradition. The Satorra-Bentler scaled difference statistic"),
("S4-P7b",
 "These statements do not all rest on the same footing, and the distinction matters for "
 "how the term is used. What is firm, in the sense of @sec-methods, is everything "
 "structural about $(A)+(C)$: its sign, its $O(1)$ order under MAR, its exact "
 "vanishing under MCAR, the closed form above, and the information convention it "
 "is computed in.",
 "These statements do not all rest on the same footing, and the distinction matters for "
 "how the term is used. The structural facts are firm in the sense of @sec-methods. Its "
 "sign, its $O(1)$ order under MAR, its exact vanishing under MCAR, the closed form "
 "above, and the information convention it is computed in are all proved."),
("S4-P11",
 "whenever the tested directions mix unequally-missing information: negligibly when the design sits "
 "near the invariance case, and by multiples when it does not.",
 "whenever the tested directions mix unequally-missing information. The over-correction is "
 "negligible when the design sits near the invariance case, and it grows to multiples when "
 "it does not."),
("S5-P2",
 "as implemented in Amelia [@honakerAmeliaIIProgram2011]: EM is run on bootstrap resamples",
 "as implemented in Amelia [@honakerAmeliaIIProgram2011]. EM is run on bootstrap resamples"),
("S5-P6",
 "reproduces all four values of @eq-knownscale within 4%: zero and "
 "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ across the deterministic and "
 "proper arms, the pair differing by exactly the posterior-draw contribution.",
 "reproduces all four values of @eq-knownscale within 4%. The deterministic arm returns "
 "zero, the proper arm returns $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$, and the "
 "pair differs by exactly the posterior-draw contribution."),
("S5-P7",
 "One scope note travels with this study: its committed correction arm used "
 "the naive trace difference as input, and in its near-invariance design the difference from "
 "@eq-lrt-bias is about 5% and immaterial, but @eq-lrt-bias is the correct general "
 "form.",
 "One scope note travels with this study. Its committed correction arm used the naive "
 "trace difference as input. In its near-invariance design the difference from "
 "@eq-lrt-bias is about 5% and immaterial, but @eq-lrt-bias is the correct general "
 "form."),
("S5-P8",
 "separate "
 "widely: @eq-lrt-bias gives $2.64$ and the naive difference gives $8.47$.",
 "separate "
 "widely. There @eq-lrt-bias gives $2.64$ and the naive difference gives $8.47$."),
("S5-P11",
 "Three cells at $N = 500$ with "
 "$R = 2000$ repetitions each: the preregistered design at $\\rho = 0.40$, a "
 "weak-signal stress cell at $\\rho = 0.10$ with near-tied candidates, and a junk "
 "cell at $\\rho = 0$ where the truth is diagonal and every anchored statistic is "
 "null-type.",
 "Three cells at $N = 500$ with "
 "$R = 2000$ repetitions each. They are the preregistered design at $\\rho = 0.40$, a "
 "weak-signal stress cell at $\\rho = 0.10$ with near-tied candidates, and a junk "
 "cell at $\\rho = 0$ where the truth is diagonal and every anchored statistic is "
 "null-type."),
("S5-P11",
 "distribution matching reaches the oracle: the two-moment and equating arms "
 "select at",
 "distribution matching reaches the oracle. The two-moment and equating arms "
 "select at"),
("S5-P11",
 "The "
 "internal validity checks held on every repetition: the spectrum-trace identity "
 "to $3 \\times 10^{-15}$, every null-law weight at least one, and zero failures "
 "of the characteristic-function inversion in 18,000 evaluations, so the "
 "preregistered simulated-reference fallback was never invoked.",
 "The "
 "internal validity checks held on every repetition. The spectrum-trace identity held "
 "to $3 \\times 10^{-15}$, every null-law weight was at least one, and the "
 "characteristic-function inversion never failed in 18,000 evaluations, so the "
 "preregistered simulated-reference fallback was never invoked."),
("S5-P12",
 "per-model marginal maps leave difference distributions uncalibrated: in the "
 "weak-signal near-tied pair the equated score difference has mean $6.10$ and "
 "standard deviation $5.99$ against the complete-data difference's $10.00$ and "
 "$7.10$.",
 "per-model marginal maps leave difference distributions uncalibrated. In the "
 "weak-signal near-tied pair the equated score difference has mean $6.10$ and "
 "standard deviation $5.99$, against $10.00$ and $7.10$ for the complete-data "
 "difference."),
("S5-P13",
 "targeted the one "
 "derived-but-unmeasured quantity in @sec-derivations: the design-imbalance "
 "differential of @prp-ac-diff for genuinely separated pairs.",
 "targeted the one "
 "derived-but-unmeasured quantity in @sec-derivations, the design-imbalance "
 "differential of @prp-ac-diff for genuinely separated pairs."),
("S5-P13",
 "resolved the predicted scaling: an isolated design-imbalance "
 "differential of $-1.2$, at $3.5$ standard errors from zero, three to four "
 "times the similar pair's bound and stable across $N$.",
 "resolved the predicted scaling. The isolated design-imbalance differential is "
 "$-1.2$, at $3.5$ standard errors from zero, three to four times the similar "
 "pair's bound and stable across $N$."),
("S5-P13",
 "the first measured case off the equality condition of @prp-naive: for these curved "
 "candidates the naive trace difference overstates the exact projected trace by "
 "about 9%.",
 "the first measured case off the equality condition of @prp-naive. For these curved "
 "candidates the naive trace difference overstates the exact projected trace by "
 "about 9%."),
("S6-P2",
 "Firm: its structure, sign, $O(1)$ order, exact MCAR "
 "vanishing, the closed form @eq-ac, and the $O(1/n)$ order of the correction "
 "beyond the leading-order analytic value. Not firm: the absolute magnitude "
 "itself.",
 "The structural facts are firm. Its sign, its $O(1)$ order, its exact MCAR "
 "vanishing, the closed form @eq-ac, and the $O(1/n)$ order of the correction "
 "beyond the leading-order analytic value are all proved. The absolute magnitude "
 "is not."),
("S6-P7",
 "For "
 "the criterion itself, yes: after correction, a deviance or information criterion "
 "computed from imputed data means what its "
 "complete-data counterpart means, on average, at any signal strength. For "
 "decisions when the competing models fit alike, yes: corrected selection and "
 "calibrated tests behave as they would have with complete data. For decisions "
 "when one model genuinely fits better, no, and the shortfall is not fixable: "
 "the missing data carried part of the evidence, less information means less "
 "power, and no transformation of the observed data manufactures the lost "
 "evidence back.",
 "The first part concerns the criterion itself, and the answer is yes. After "
 "correction, a deviance or information criterion computed from imputed data means "
 "what its complete-data counterpart means, on average, at any signal strength. The "
 "second part concerns decisions when the competing models fit alike, and the answer "
 "is again yes. Corrected selection and calibrated tests behave as they would have "
 "with complete data. The third part concerns decisions when one model genuinely "
 "fits better, and there the answer is no. The missing data carried part of the "
 "evidence. Less information means less power, and no transformation of the observed "
 "data manufactures the lost evidence back."),
("S6-P8",
 "What it demonstrably caught is on the record: a sign "
 "error that eight of nine blind re-derivations shipped, a wrong shortcut in an "
 "early entropy-gradient argument, and every failed prediction now reported in "
 "@sec-simulations.",
 "Three catches are on the record. The protocol caught a sign error that eight of "
 "nine blind re-derivations shipped. It caught a wrong shortcut in an early "
 "entropy-gradient argument. And it forced every failed prediction into "
 "@sec-simulations."),
("S6-P8",
 "What it cost is also visible: claims arrive slower, hedged "
 "to their tier, and two preregistered headlines were given up rather than "
 "rescued.",
 "The cost is also visible. Claims arrived slower, hedged to their tier, and two "
 "preregistered headlines were given up rather than rescued."),
("S6-P8",
 "What it cannot catch was stated in @sec-methods and bears repeating "
 "once: errors shared across model lineages, misreadings of real sources, and "
 "designs that answer the wrong question reproducibly.",
 "What it cannot catch was stated in @sec-methods and bears repeating once. It "
 "cannot catch errors shared across model lineages, misreadings of real sources, or "
 "designs that answer the wrong question reproducibly."),
("S6-P8",
 "The record it leaves behind, the decision log, the preregistrations with their "
 "amendments, the verification gates, and the session transcripts, is published so "
 "that the assertion can be tested by someone other than its authors.",
 "What it leaves behind is a public record. The decision log, the preregistrations "
 "with their amendments, the verification gates, and the session transcripts are all "
 "published, so the assertion can be tested by someone other than its authors."),
]

applied, skipped, missed = 0, 0, []
for pid, old, new in EDITS:
    p = paras[pid]
    if new in p["draft_prose"]:
        skipped += 1
        continue
    if old not in p["draft_prose"]:
        missed.append((pid, old[:70]))
        continue
    p["draft_prose"] = p["draft_prose"].replace(old, new)
    applied += 1
    note = " Punctuation sweep 2026-06-07."
    if note not in p["audit"]["notes"]:
        p["audit"]["notes"] = (p["audit"]["notes"] + note).strip()

l3["metadata"]["status"] = "all_six_drafted_punctuation_swept"

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"punctuation sweep: {applied} applied, {skipped} already clean, {len(missed)} missed")
for pid, frag in missed:
    print("  MISSED", pid, "|", frag)
