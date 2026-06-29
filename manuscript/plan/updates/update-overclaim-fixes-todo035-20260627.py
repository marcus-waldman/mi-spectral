#!/usr/bin/env python3
"""
todo/035 accuracy pass: apply the 15 overclaim fixes confirmed by the adversarial
audit (overclaim-accuracy-audit workflow; 16 suspects -> 15 confirmed 3/3, 1
cleared, 0 split). Each rewrite scopes a claim to exactly what the proofs and the
measured results support; every number, citation, cross-reference, and math token
is preserved. Per-paragraph targeted replacement with assertions. Idempotent.

Run:  py manuscript/plan/updates/update-overclaim-fixes-todo035-20260627.py
Then: py scripts/check_plan.py ; py scripts/overclaim_flag.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

R = {
    "S1-P4": [
        ("The practical consequence is that every deviance and every information criterion computed from multiply imputed data is too optimistic.",
         "The practical consequence is that, for such a model, every deviance and every information criterion computed from multiply imputed data is too optimistic."),
    ],
    "S1-P5": [
        ("The relevant statistics shrink by factors we predict exactly, and the remaining shortfall is information loss rather than a fixable calibration error.",
         "The relevant statistics shrink by factors we predict, and the remaining shortfall is information loss rather than a fixable calibration error."),
    ],
    "S1-P6": [
        ("Fourth, the exact differential bias of the likelihood-ratio numerator in the complete-data metric.",
         "Fourth, the exact differential bias of the likelihood-ratio numerator at the null in the complete-data metric."),
    ],
    "S1-P6b": [
        ("Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and restores the ranking that complete data would have given.",
         "Adding one term per candidate, the trace of its relative-increase-in-variance matrix, removes the bias and substantially restores the ranking that complete data would have given."),
        ("We show that the averaged log-likelihood across imputations overstates its complete-data counterpart by half the trace of the relative-increase-in-variance matrix, plus a design-imbalance term that appears only under data missing at random and disappears when data are missing completely at random.",
         "For a model that estimates a scale or covariance, we show that the averaged log-likelihood across imputations overstates its complete-data counterpart by half the trace of the relative-increase-in-variance matrix, plus a design-imbalance term that appears only under data missing at random and disappears when data are missing completely at random."),
    ],
    "S1B-P1": [
        ("This section describes the collaboration and shows that it was productive.",
         "This section describes the collaboration and shows that it was active and human-directed."),
        ("The human prompter of record is ORCID-verified, and the full record of the work is public.",
         "The human prompter of record is ORCID-verified, and the full record of the work enters the public record."),
    ],
    "S1B-P2": [
        ("The transcripts, the decision log, and the coded analysis are all part of the public record, so this description is auditable rather than self-reported.",
         "The transcripts, the decision log, and the coded analysis are all part of the public record, so this description is auditable, though the coding itself was produced by the same kind of system it describes."),
    ],
    "S2-P12": [
        ("The design-imbalance term $(A)+(C)$ is nonzero exactly when MCAR fails, and it is computed against the observed information.",
         "The design-imbalance term $(A)+(C)$ vanishes under MCAR and is a nonzero $O(1)$ under MAR, and it is computed against the observed information."),
    ],
    "S3-P4": [
        ("Every analytic claim passed through a fixed sequence.",
         "Every analytic claim entered a fixed sequence."),
    ],
    "S4-P1": [
        ("It prices the bias of the averaged log-likelihood exactly, so the criterion can be restored to its complete-data expectation.",
         "It prices the bias of the averaged log-likelihood to leading order, so the criterion can be restored to its complete-data expectation."),
    ],
    "S4-P16": [
        ("For two candidates the uncorrected difference carries a differential bias of exactly the surplus of missing information.",
         "For two candidates the uncorrected difference carries a differential bias whose leading term is the surplus of missing information."),
    ],
    "S5-P12": [
        ("The net deviance bias tracks the analytic half-trace across every sample size (@fig-w1-theorem).",
         "The net deviance bias tracks the analytic half-trace once the sample sizes are pooled (@fig-w1-theorem)."),
    ],
    "S5-P21": [
        ("The mechanism behind the design-imbalance term is confirmed exactly.",
         "The mechanism behind the design-imbalance term is confirmed."),
    ],
    "S6-P1": [
        ("A known-scale, location-only fit has no such bias.",
         "A known-scale, location-only fit has no such bias under deterministic FIML and only $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under proper MI."),
    ],
}


def main():
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}
    applied = skipped = 0
    for pid, subs in R.items():
        prose = by_id[pid]["draft_prose"]
        for old, new in subs:
            if old in prose:
                prose = prose.replace(old, new, 1)
                applied += 1
            elif new in prose:
                skipped += 1
            else:
                raise SystemExit(f"ERROR: {pid}: neither old nor new found:\n  OLD: {old!r}")
        by_id[pid]["draft_prose"] = prose

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"overclaim fixes applied: {applied}, already-applied: {skipped} (of 15)")


if __name__ == "__main__":
    main()
