# r3#3 (v1 AI-review response, todo/040 Phase 4 tail, 2026-07-04)
#
# The reviewer: the manuscript recommends diagnosing congeniality but "does not
# provide, nor does it cite, any practical methods or established literature for
# how an applied researcher should actually perform this diagnosis."
#
# Fix: three sentences appended to the G7 congeniality-limit paragraph (S6-P4b),
# citing three verified references (all acquired via Zotero -> lit-sync
# 2026-07-04, read in-session the same day; claim checks recorded in
# todo/003-references-to-acquire.md):
#   @heDiagnosingImputationModels2012 -- posterior predictive checks that apply
#     the analyst's own target analysis to completed data and to replicates
#     drawn under the imputation model; re-imputation implementation on standard
#     MI software (Abstract; Sec.3.2-3.3); explicitly motivated by
#     uncongeniality (keyword; Sec.1).
#   @bondarenkoGraphicalNumericalDiagnostic2016 -- graphical/numerical checks of
#     observed vs imputed values conditional on the response propensity, with
#     the stated objective that "the analyst can diagnose uncongeniality"
#     without knowing the imputation model (Abstract, objective (1); keyword
#     "congeniality").
#   @nguyenModelCheckingMultiple2017 -- applied overview of imputation-model
#     checking (graphical, propensity-conditional, regression diagnostics,
#     cross-validation, posterior predictive checking), with a case study in
#     which the posterior predictive check catches an imputation/analysis
#     incompatibility (Abstract; "Checking the imputation model"; Table 5).
#
# Response-letter entry: manuscript/reviews/v1/response/response-letter.md r3#3.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras_by_id = {p["id"]: p for p in l3["paragraphs"]}
p = paras_by_id["S6-P4b"]


def replace_one(container, key, old, new, label):
    text = container[key]
    if old not in text:
        raise SystemExit(f"{label}: expected OLD text not found -- aborting.\nOLD={old!r}")
    if text.count(old) != 1:
        raise SystemExit(f"{label}: OLD text is not unique ({text.count(old)} occurrences) -- aborting.")
    container[key] = text.replace(old, new)


replace_one(
    p, "draft_prose",
    "The practical recommendation is to diagnose congeniality before trusting "
    "bias-corrected selection.",
    "The practical recommendation is to diagnose congeniality before trusting "
    "bias-corrected selection. Practical tools for that diagnosis exist. "
    "@heDiagnosingImputationModels2012 give a posterior predictive check that "
    "applies the analyst's own target analysis to the completed data and to "
    "replicates drawn under the imputation model, and their re-imputation scheme "
    "runs on standard imputation software. "
    "@bondarenkoGraphicalNumericalDiagnostic2016 compare observed and imputed "
    "values conditional on the response propensity, so an analyst can judge "
    "congeniality without knowing the imputation model. "
    "@nguyenModelCheckingMultiple2017 review these and related checks for "
    "applied use.",
    "r3#3 (G7 congeniality diagnostics)",
)

replace_one(
    p["review"], "closing_sentence",
    "The practical recommendation is to diagnose congeniality before trusting "
    "bias-corrected selection.",
    "...review these and related checks for applied use.",
    "r3#3 (closing sentence)",
)

p["proposition"] = (
    p["proposition"]
    + " Practical diagnostics cited: He-Zaslavsky 2012 (target-analysis posterior "
      "predictive checks), Bondarenko-Raghunathan 2016 (propensity-conditional "
      "checks; analyst-side congeniality diagnosis), Nguyen et al. 2017 (applied "
      "overview)."
)

p["review"]["flags"] = (
    p["review"]["flags"]
    + " | r3#3 2026-07-04: three congeniality-diagnostic citations appended (v1 "
      "review response; refs acquired + read in-session same day; todo/003)."
)

p["audit"]["citations"].update({
    "heDiagnosingImputationModels2012":
        "verified (read in-session 2026-07-04; target-analysis PPC on completed "
        "data vs posterior replicates, re-imputation on standard software, per "
        "Abstract + Sec.3.2-3.3; uncongeniality framing Sec.1)",
    "bondarenkoGraphicalNumericalDiagnostic2016":
        "verified (read in-session 2026-07-04; propensity-conditional "
        "observed-vs-imputed checks; stated objective (1): 'the analyst can "
        "diagnose uncongeniality' without knowing the imputation model, Abstract)",
    "nguyenModelCheckingMultiple2017":
        "verified (read in-session 2026-07-04; applied overview of imputation "
        "model checking incl. PPC; case study catches imputation/analysis "
        "incompatibility, Abstract + Table 5)",
})

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)

print("r3#3 congeniality-diagnostics citations applied to S6-P4b.")
