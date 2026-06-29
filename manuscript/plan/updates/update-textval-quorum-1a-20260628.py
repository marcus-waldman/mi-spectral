#!/usr/bin/env python3
"""Apply the text-validity quorum (1a) adjudicated edits to level3-paragraphs.json.

Determination: AMENDED (no result retracted). 20 bounded wording/citation edits.
Deviations from the verbatim EDIT-LIST.md (to avoid redundancy/duplication with
surrounding text, and to reflect the due-diligence finding that W3-C = 1.000 held in
ALL 60 cells, not only congenial) are tagged DEVIATION in the notes and reported.

Two-pass: validate every `old` matches exactly once, THEN apply + write. Aborts on any
mismatch so no partial edit is written.
"""
import json
from pathlib import Path

L3 = Path(r"C:/Users/marcu/git-repositories/mi-spectral/manuscript/plan/level3-paragraphs.json")

# (loc, tv, old, new, note)   loc = "abstract" or a paragraph id
EDITS = [
 ("abstract", "TV-02",
  "Model selection on multiply imputed data is biased toward more complex models, because their larger relative increase in variance makes the fit look better than it is.",
  "Model selection on multiply imputed data is biased toward the candidates with more missing information, which in the nested families studied are the more complex models, because their larger relative increase in variance makes the fit look better than it is.",
  "headline on missing information, not complexity; complexity scoped to studied families (R2 lead-specified)"),
 ("abstract", "TV-01",
  "Adding one trace term per candidate removes the bias and restores complete-data-equivalent selection.",
  "Adding one trace term per candidate removes the deviance bias in expectation and substantially restores complete-data model selection.",
  "in expectation + substantially restores (matches body)"),
 ("S1-P2", "TV-18",
  "Only one information criterion has been proposed for multiply imputed data.",
  "Only one information criterion has been proposed specifically for averaging over multiply imputed data.",
  "scope to the averaged-criterion-for-MI class"),
 ("S1-P3", "TV-17",
  "The open questions above are open because the second and third levels had not been posed.",
  "Posing the second and third levels reframes these open questions, which had been posed only at the first level.",
  "recast causal-history claim as the paper's reframing"),
 ("S1-P4", "TV-03",
  "every deviance and every information criterion computed from multiply imputed data is too optimistic.",
  "every deviance and information criterion built on the averaged log-likelihood across imputations is, in expectation, too optimistic.",
  "name the criterion class (averaged log-likelihood) + in expectation (R2 lead-specified)"),
 ("S1-P4", "TV-11",
  "A model-comparison table built on imputed data therefore favors the candidates with the most missing information.",
  "A model-comparison table built on imputed data therefore tends, all else equal, to favor the candidates with the most missing information.",
  "tendency, not deterministic"),
 ("S1-P4", "TV-14",
  "In our pre-registered study, every misclassification by uncorrected MI-AIC chose the candidate with the largest RIV.",
  "In our pre-registered simulations, 100% of uncorrected MI-AIC's misclassifications fell on the candidate with the largest RIV.",
  "DEVIATION: plain empirical 100% (Marcus); NO 'congenial' qualifier -- due diligence: W3-C=1.000 in all 60 cells, not only congenial"),
 ("S1-P5", "TV-05",
  "The missing data have then destroyed part of the evidence in its favor, and we show that no transformation of the observed data can recover it.",
  "The missing data have then destroyed part of the evidence in its favor, and the corrected criteria and calibrated tests studied here cannot recover it.",
  "align with G4: scope to the procedures studied, drop absolute impossibility"),
 ("S1-P5", "TV-06",
  "Correction then restores complete-data behavior entirely.",
  "Correction then restores complete-data behavior in this case.",
  "drop 'entirely' (Marcus: reads as bragging); scope to the equal-fit case"),
 ("S1-P6b", "TV-04",
  "removes the bias and substantially restores the ranking that complete data would have given.",
  "removes the trace component of the bias and substantially restores the ranking that complete data would have given.",
  "name the trace component (design-imbalance term remains)"),
 ("S3-P6", "TV-16",
  "A derivation produced and checked within a single model family would likely have shipped one sign without noticing that there was a choice.",
  "A less diverse, single-family check could have missed that the sign turned on a conditioning choice.",
  "recast counterfactual as interpretation (8-of-9 already stated above)"),
 ("S5-P6", "TV-19",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic referred to $\chi^2_1$.",
  r"By contrast, the Satorra-Bentler arm applies a scaled-and-shifted statistic [@satorraEnsuringPositivenessScaled2010; @asparouhovRobustChiSquare2006] referred to $\chi^2_1$.",
  "add the Satorra-Bentler / scaled-shifted citation at point of use"),
 ("S5-P17", "TV-15",
  "In every congenial cell, all of the uncorrected criterion's errors land on the saturated, largest-missing-information candidate. This is a registered directional prediction, and it held across all sixty cells.",
  "In our simulations, every misclassification by the uncorrected criterion fell on the saturated, largest-missing-information candidate, 100% in all sixty cells. This directional pattern was registered for the congenial cells and held in the uncongenial ones as well.",
  "DEVIATION: due diligence -- W3-C=1.000 held in ALL 60 cells; state plainly (was conservatively scoped to congenial)"),
 ("S5-P22", "TV-13",
  "which bounds the cost of not running data augmentation.",
  "which indicates the cost of not running data augmentation is small on these designs.",
  "'bounds' -> 'indicates' (empirical check, not a derived bound)"),
 ("S6-P1", "TV-08",
  "The bias exists only when the fit estimates a scale or covariance.",
  "The deviance optimism that inflates the criteria exists only when the fit estimates a scale or covariance.",
  "name the object (distinguishes it from the known-scale -1/2 tr(RIV) term named next)"),
 ("S6-P6", "TV-20",
  "joint calibration of score vectors across candidates are developed separately.",
  "joint calibration of score vectors across candidates are left to future work.",
  "due diligence: de-shrinkage/joint-calibration is a follow-up plan (todo/023), no published companion -> future work"),
 ("S6-P7", "TV-07",
  "No transformation of the observed data manufactures the lost evidence back.",
  "No correction studied here manufactures the lost evidence back.",
  "align with G4 (conclusion restatement)"),
 ("S6-P7", "TV-09",
  "Corrected selection and calibrated tests behave as they would have with complete data.",
  "There, corrected selection and calibrated tests behave as they would have with complete data.",
  "DEVIATION: minimal scope anchor 'There,' (the full clause would duplicate the preceding sentence)"),
 ("S6-P7", "TV-12",
  "Then trust the result the way complete-data results are trusted.",
  "Then trust the result the way complete-data results are trusted, subject to the stated conditions.",
  "DEVIATION: dropped redundant 'and the close-comparison exception below' (it is the very next sentence)"),
 ("S6-P7b", "TV-10a",
  "When the aim is to rank models or to compare nested models on imputed data, and no calibrated reference distribution already absorbs the bias, add the per-candidate trace correction before reading off the result.",
  "When the aim is to rank models on imputed data, and no calibrated reference distribution already absorbs the bias, add the per-candidate trace correction before reading off the result.",
  "remove 'or to compare nested models' (it conflated IC ranking with the nested-LRT result)"),
 ("S6-P7b", "TV-10b",
  "so a numerator correction applied on top would double-count and should be left out.",
  "so a numerator correction applied on top would double-count and should be left out. For a nested comparison without a calibrated reference, the relevant bias is the missing information in the tested directions alone, not the difference of the candidates' separate trace corrections.",
  "DEVIATION: surgical add of the nested-comparison rule (avoids duplicating the existing IC/LRT sentences that the wholesale split-rule would have)"),
]

doc = json.loads(L3.read_text(encoding="utf-8"))
paras = {p["id"]: p for p in doc["paragraphs"]}

def get_text(loc):
    if loc == "abstract":
        return doc["abstract"]
    return paras[loc]["draft_prose"]

def set_text(loc, txt):
    if loc == "abstract":
        doc["abstract"] = txt
    else:
        paras[loc]["draft_prose"] = txt

# ---- PASS 1: validate every old matches exactly once (against the CURRENT, sequentially-edited text) ----
work = {}   # loc -> running text
errors = []
for loc, tv, old, new, note in EDITS:
    if loc not in work:
        work[loc] = get_text(loc)
    n = work[loc].count(old)
    if n != 1:
        errors.append(f"  {tv} [{loc}]: old-string found {n}x (expected 1)")
    else:
        work[loc] = work[loc].replace(old, new)

if errors:
    print("ABORT -- old-string validation failed; NOTHING written:")
    print("\n".join(errors))
    raise SystemExit(1)

# ---- PASS 2: apply (reuse the validated running text) + write ----
for loc, txt in work.items():
    set_text(loc, txt)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"APPLIED {len(EDITS)} edits across {len(work)} locations.")
for loc, tv, old, new, note in EDITS:
    tag = "  *DEVIATION*" if note.startswith("DEVIATION") else ""
    print(f"  {tv:7} [{loc}]{tag}")
print("\nParagraph count:", len(doc["paragraphs"]), "(expect 85)")
