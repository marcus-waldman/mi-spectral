#!/usr/bin/env python3
"""
todo/035 step 3 -- atomic level3 update: add the Delphi-vetted Contributions
enumeration to the Introduction and an "Implications for applied research"
paragraph to the Discussion, and give the abstract a tracked home.

Placement (Marcus, AskUserQuestion 2026-06-27): Intro contributions list + a
Discussion applied-implications passage (two units). Content ratified by a
tkal-in-ket Delphi (pool-then-axes): pool converged 8/8 unanimous at round 5;
axes 5 unanimous / 7 majority / 0 split. Run artifacts under
tkal-reviews/delphi-{pool,axes}-*/.

This script is idempotent: re-running it does not duplicate the inserts.

Run:  py manuscript/plan/updates/update-contributions-todo035-20260627.py
Then: py scripts/check_plan.py   (must stay green)
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

# --- new prose (house style: plain expository, no semicolons, no rhetorical
#     colons; bold run-in labels only) -------------------------------------- #

S1P6B_PROSE = (
    "The contributions follow, stated for use rather than for novelty and "
    "ordered as an applied reader is likely to need them.\n\n"
    "1. **A correction for model selection after imputation.** Choosing among "
    "models by AIC or BIC on multiply imputed data is biased, and the bias is "
    "specific to each candidate. It grows with the candidate's missing "
    "information, so the uncorrected criteria favor the models that lost the "
    "most data. Adding one term per candidate, the trace of its "
    "relative-increase-in-variance matrix, removes the bias and restores the "
    "ranking that complete data would have given.\n"
    "2. **The deviance bias behind it.** We show that the averaged "
    "log-likelihood across imputations overstates its complete-data counterpart "
    "by half the trace of the relative-increase-in-variance matrix, plus a "
    "design-imbalance term that appears only under data missing at random and "
    "disappears when data are missing completely at random. The proof for "
    "proper imputation and the design-imbalance term are new, while the trace "
    "itself matches a penalty already known from a related prediction problem.\n"
    "3. **The bias of a likelihood-ratio comparison.** For two nested models "
    "compared at the null, the relevant bias is the missing information carried "
    "by the tested directions alone, measured in the complete-data metric. The "
    "obvious alternative, the difference of the two models' separate "
    "corrections, always overstates it.\n"
    "4. **A sharper way to run that comparison.** Fitting the competing models "
    "to the same imputed data sets rather than to separate ones cancels most of "
    "the shared noise and tightens the comparison.\n"
    "5. **An auditable AI-human workflow.** We treat the way the derivations "
    "were produced as a contribution in its own right, with transparent "
    "provenance and gates the reader can check. These are sourced citations, "
    "independent symbolic verification, preregistered simulations whose failures "
    "are reported, adversarial re-derivation that caught a sign error in this "
    "very work, and full reproducibility. Its checkable records are verified "
    "mechanically, and its one descriptive part, a coding of the project's own "
    "session record, was produced by the same kind of system it describes and "
    "is reported as such."
)

S6P7B_PROSE = (
    "Two implications for applied practice follow. The first is statistical. "
    "When the aim is to rank models or to compare nested models on imputed "
    "data, and no calibrated reference distribution already absorbs the bias, "
    "add the per-candidate trace correction before reading off the result. "
    "Information-criterion selection is the main such case. The exception is a "
    "calibrated likelihood-ratio test, where the reference distribution already "
    "carries the null mean, so a numerator correction applied on top would "
    "double-count and should be left out. The second implication is about "
    "method. An applied team deciding whether to rely on an AI-assisted "
    "derivation can ask for the same evidence required here. That evidence is "
    "sourced citations, independent symbolic checks, preregistered numerical "
    "criteria with their failures reported, adversarial review by a separate "
    "model, and a reproducible record. What makes such a result safe to use is "
    "the standard it meets, not the name of the system that produced it."
)

ABSTRACT = (
    "Model-selection tables built on multiply imputed data are biased toward "
    "the models that lost the most data. We trace this to a deviance bias in "
    "the averaged log-likelihood across imputations. Under congenial proper "
    "multiple imputation with the complete-data maximum likelihood estimate as "
    "target, the averaged log-likelihood overstates its complete-data "
    "counterpart by one half the trace of the relative-increase-in-variance "
    "matrix, plus a design-imbalance term that vanishes when data are missing "
    "completely at random. The bias is specific to each candidate model, which "
    "is why uncorrected information criteria favor the models with more missing "
    "information. Adding one trace term per candidate removes the bias and "
    "restores complete-data-equivalent selection. The same analysis gives the "
    "bias of a likelihood-ratio comparison at the null, the missing information "
    "in the tested directions alone, and identifies where a calibrated test "
    "already supplies the correction so that it must not be applied twice. The "
    "derivation is AI-assisted under a stated, auditable verification protocol."
)

# --- new paragraph objects ------------------------------------------------- #

S1P6B = {
    "id": "S1-P6b",
    "section": "S1",
    "goal": "state_result",
    "proposition": (
        "The paper's contributions as an applied-first enumeration: (1) the "
        "per-candidate tr(RIV_k) correction for information-criterion "
        "selection; (2) the deviance-bias theorem (+1/2 tr(RIV) + the MAR "
        "design-imbalance term; proof for proper MI and the MAR term new, trace "
        "matches Shimodaira's penalty); (3) the LRT differential bias "
        "tr(RIV_perp) in the complete-data metric, which the naive difference "
        "overstates; (4) imputation reuse / pairing; (5) the auditable AI-human "
        "workflow, with the same-lineage self-coding caveat carried in the "
        "claim sentence. Delphi-vetted (todo/035): pool 8/8 unanimous, axes 5 "
        "unanimous / 7 majority / 0 split."
    ),
    "depends_on": ["S1-P6"],
    "dep_types": ["builds_on"],
    "review": {
        "serves_L2": "S1-SP4 (the result, as an explicit contributions enumeration)",
        "serves_L1": "M1 contributions skim hook (todo/035 D-15); applied-first order",
        "sets_up": "S1-P7 (meta layer), S4 (the derivations that prove each item)",
        "topic_sentence": "The contributions follow, stated for use rather than for novelty and ordered as an applied reader is likely to need them.",
        "closing_sentence": "Its checkable records are verified mechanically, and its one descriptive part, a coding of the project's own session record, was produced by the same kind of system it describes and is reported as such.",
        "status": "drafted",
        "flags": "todo/035 Delphi-vetted contributions; applied-first order (lead = IC correction); workflow first-class with self-coding caveat in-sentence; T-03 vocabulary check passed; punctuation budget respected (no semicolons, bold run-in labels only)."
    },
    "draft_prose": S1P6B_PROSE,
    "audit": {
        "status": "complete",
        "citations": {},
        "numbers": {
            "IC correction (item 1) and model-specific bias": "deriv:sec-ic",
            "deviance-bias theorem (item 2)": "deriv:sec-thm",
            "LRT differential bias (item 3)": "deriv:sec-lrt",
            "auditable workflow (item 5)": "verif:verification/collaboration-analysis.md"
        },
        "notes": "Contributions enumeration; summarizes results proved in S4 and the workflow documented in S1B/S3 (no new inline numbers). Delphi-vetted (todo/035); pool+axes artifacts in tkal-reviews/. Punctuation sweep clean."
    }
}

S6P7B = {
    "id": "S6-P7b",
    "section": "S6",
    "goal": "summarize",
    "proposition": (
        "Two Delphi-ratified applied implications: (i) the statistical scope "
        "guard -- use the per-candidate tr(RIV_k) correction for "
        "information-criterion ranking and wherever no calibrated reference "
        "distribution absorbs the mean, and do not add it on top of a "
        "calibrated likelihood-ratio test, whose reference already carries the "
        "null mean; (ii) the methodological evidence standard -- the auditable "
        "evidence an applied team should require of an AI-assisted derivation "
        "before relying on it."
    ),
    "depends_on": ["S6-P7"],
    "dep_types": ["builds_on"],
    "review": {
        "serves_L2": "S6-SP4 (the applied takeaway, as explicit implications)",
        "serves_L1": "M5 applied implications (todo/035 D-15)",
        "sets_up": "S6-P8 (the workflow reflection that closes the paper)",
        "topic_sentence": "Two implications for applied practice follow.",
        "closing_sentence": "What makes such a result safe to use is the standard it meets, not the name of the system that produced it.",
        "status": "drafted",
        "flags": "todo/035 Delphi-vetted implications (scope guard + evidence standard); no double-apply on a calibrated LRT; T-03 vocabulary check passed; punctuation budget respected."
    },
    "draft_prose": S6P7B_PROSE,
    "audit": {
        "status": "complete",
        "citations": {},
        "numbers": {
            "scope guard (IC vs calibrated LRT)": "deriv:sec-lrt",
            "the per-candidate correction": "deriv:sec-ic",
            "auditable evidence standard": "verif:verification/collaboration-analysis.md"
        },
        "notes": "Applied-implications passage between the verdict (S6-P7) and the workflow reflection (S6-P8). Delphi-ratified (todo/035). No new numbers. Punctuation sweep clean."
    }
}


def insert_after(paras, anchor_id, new_para):
    """Insert new_para immediately after the paragraph with id anchor_id.
    Idempotent: if new_para['id'] already present, replace it in place."""
    ids = [p["id"] for p in paras]
    if new_para["id"] in ids:
        paras[ids.index(new_para["id"])] = new_para
        return paras
    idx = ids.index(anchor_id)
    paras.insert(idx + 1, new_para)
    return paras


def main():
    d = json.loads(L3.read_text(encoding="utf-8"))
    paras = d["paragraphs"]

    insert_after(paras, "S1-P6", S1P6B)
    insert_after(paras, "S6-P7", S6P7B)

    # rewire the Intro meta paragraph to follow the new contributions list
    for p in paras:
        if p["id"] == "S1-P7":
            p["depends_on"] = ["S1-P6b"]

    # abstract: tracked home in level3 (Marcus, AskUserQuestion 2026-06-27).
    # build_preview.py sources the preview front matter from here.
    d["abstract"] = ABSTRACT

    amend = ("2026-06-27 (todo/035): added S1-P6b (Delphi-vetted Contributions "
             "enumeration, applied-first) before the Intro meta paragraph, and "
             "S6-P7b (Implications for applied research) between the Discussion "
             "verdict and the workflow reflection; abstract given a tracked home "
             "(top-level 'abstract'). Content ratified by a tkal-in-ket Delphi "
             "(pool 8/8 unanimous; axes 5 unanimous / 7 majority / 0 split).")
    md = d.setdefault("metadata", {})
    prev = md.get("amended")
    md["amended"] = (prev + " || " + amend) if prev else amend

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("level3 updated: +S1-P6b, +S6-P7b, S1-P7.depends_on -> [S1-P6b], "
          "abstract field added.")
    print(f"paragraphs now: {len(paras)}")


if __name__ == "__main__":
    main()
