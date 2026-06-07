# Level-2 review cycle 1 - 2026-06-06 (in-chat annotation, Marcus on phone + Claude)
#
# Minutes, one block per unit:
#
# U1 (S1 INTRODUCTION): SP1 rewritten - "settled" is ATTRIBUTED to the field's own
#   state-of-the-art accounts, not endorsed by us; the introduction's question becomes
#   what "settled" should even mean. SP3 sharpened - the replication principle supplies
#   the missing criterion of settledness (classical results pass at the estimate level,
#   LRT/IC were never graded against any stated criterion).
#
# U2 (S2 BACKGROUND), U3 (S3 METHODS), U5 (S5 SIMULATIONS): approved as drafted.
#
# U4 (S4 DERIVATIONS): DAG-conformance check against todo/030 surfaced three
#   under-carried nodes; Marcus approved all three repairs:
#   - SP1 gains the entropy-plug-in consistency-check tail (DAG S7).
#   - NEW SP5b = DAG L5, the absorption argument (calibrated reference absorbs
#     tr(RIV_perp) at the null; numerator correction on a calibrated test
#     double-counts, W2 0.042 vs 0.034; bias matters where no reference exists).
#     Inserted between SP5 and SP6 as the (b)->(c) bridge.
#   - SP7 extended with DAG I7's two structural limits (W3/ladder family = the
#     naive-trace equality case, agreement 3.6e-15; marginal transforms cannot
#     calibrate a difference distribution, equated 6.10 vs complete-data 10.00).
#
# U6 (S6 DISCUSSION): SP6 (provenance declaration) REMOVED from the Discussion -
#   Marcus: it belongs in a title-page declaration, not section content. S6 now ends
#   on the workflow reflection (SP5). Title-page declaration recorded as a new
#   front-matter element (decision D-11 in decisions.md); old-S8 mapping updated.
#
# Follow-up queued (not this cycle): sync todo/030 + litrev argument-map DB with the
#   post-D-09/D-10 structure (replication-principle and Methods-as-workflow nodes).

import json

PATH = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level2-sections.json"

with open(PATH, encoding="utf-8") as f:
    plan = json.load(f)

sections = {s["id"]: s for s in plan["sections"]}

# ---------------------------------------------------------------- metadata
plan["metadata"]["status"] = "annotated_cycle1"
plan["metadata"]["amended"] = (
    "2026-06-06 (cycle 1, in-chat): S1-SP1 attributed / S1-SP3 sharpened (settledness "
    "criterion); S4 repaired against the todo/030 DAG (S7 tail on SP1, new SP5b = L5 "
    "absorption, SP7 + I7 structural limits); S6-SP6 moved to a title-page declaration "
    "(D-11); U2/U3/U5 approved as drafted. Minutes: updates/update-level2-20260606.py."
)

# ---------------------------------------------------------------- U1: S1 SP1 + SP3
s1 = sections["S1"]
for sp in s1["super_propositions"]:
    if sp["id"] == "S1-SP1":
        sp["claim"] = (
            "The field's own state-of-the-art accounts treat MI's core inferential "
            "machinery - mechanisms, point estimation, Wald-type inference - as settled; "
            "this maturity claim is reported as theirs, not endorsed, and the "
            "introduction's question is what 'settled' should even mean."
        )
    if sp["id"] == "S1-SP3":
        sp["claim"] = (
            "The complete-data replication principle supplies the missing criterion of "
            "settledness - the classical results pass it at the estimate level, which is "
            "why they feel settled, while LRT and IC have never been assessed against any "
            "stated criterion - posed at three levels (estimates / criterion-in-expectation "
            "/ decision rates) in the authors' voice, asserted-here: empirical full-data "
            "benchmarking is precedented (Wood 2008, C-C 2010), the named principle with an "
            "achievability characterization is not."
        )

s1["goal_statement"] = s1["goal_statement"].replace(
    "(i) MI's major inferential results are settled but LRT and IC are not - on the field's own testimony;",
    "(i) the field's own accounts treat MI's major inferential results as settled while LRT and IC are not - and the right question is what 'settled' should mean;"
)

# ---------------------------------------------------------------- U4: S4 repairs
s4 = sections["S4"]
for sp in s4["super_propositions"]:
    if sp["id"] == "S4-SP1":
        sp["claim"] += (
            " The result is confirmed by the convention-free entropy-plug-in reading "
            "(E[T] equals the conditional-entropy plug-in bias Delta_n via the "
            "entropy-Hessian split - the same bias regrouped)."
        )
    if sp["id"] == "S4-SP7":
        sp["claim"] += (
            " Two structural limits qualify generalization: the W3/ladder candidate "
            "family is exactly the naive-trace equality case (the overstatement is "
            "invisible there, naive vs exact agreement 3.6e-15), and per-model marginal "
            "transforms cannot calibrate a difference distribution (score-copula "
            "invariance; equated Delta mean 6.10 vs complete-data 10.00)."
        )

sp5b = {
    "id": "S4-SP5b",
    "claim": (
        "At the null, tr(RIV_perp) is exactly the mean a correctly calibrated reference "
        "distribution absorbs, so adding a numerator correction to a calibrated test "
        "double-counts (W2: size 0.042 uncorrected vs 0.034 over-corrected) - the bias "
        "therefore matters precisely where no reference stands between the statistic and "
        "its use: information-criterion ranking, explicit numerator corrections, and "
        "non-nested comparison."
    ),
    "goal": "state_result",
    "evidence": ["deriv:sec-lrt", "lit:chanGeneralFeasibleTests2022", "verif:verification/cache/W2-prod-amelia.rds"],
    "evidence_status": "grounded"
}
sps = s4["super_propositions"]
idx = next(i for i, sp in enumerate(sps) if sp["id"] == "S4-SP6")
sps.insert(idx, sp5b)

# ---------------------------------------------------------------- U6: S6 SP6 -> title page
s6 = sections["S6"]
s6["super_propositions"] = [sp for sp in s6["super_propositions"] if sp["id"] != "S6-SP6"]
s6["goal_statement"] = s6["goal_statement"].replace(
    "are fully readable by the S1 reader; end with the formal JAIGP provenance declaration. NO separate Conclusion section; the verdict paragraph is the takeaway block.",
    "are fully readable by the S1 reader, ending on the workflow reflection. NO separate Conclusion section; the verdict paragraph is the takeaway block. The JAIGP provenance declaration is NOT section content - it lives in a title-page declaration block (D-11)."
)
s6["mapping_from_180e2b5"] = (
    "Old S7 (sec-discussion), reordered to the inverse gradient with the plain-language "
    "verdict as item (4) and the workflow reflection as the close. Old S8 (sec-provenance) "
    "is split: substance -> S3 Methods; formal declaration -> title-page declaration block "
    "(D-11); nothing of it remains as section content."
)

# ---------------------------------------------------------------- front matter element
plan["front_matter"] = {
    "title_page_declaration": (
        "Authorship and provenance declaration (D-11), title-page block per scholarly "
        "declaration conventions: AI lineage and role in the derivation, ORCID-verified "
        "human prompter of record (marcus.waldman), pointer to the public repository and "
        "the companion derivation document. The reader knows the paper's nature before "
        "page one; M1's closing meta paragraph elaborates what the title page declares."
    )
}

# ---------------------------------------------------------------- gate
plan["metrics_gate"]["notes"] = (
    "Re-evaluated after cycle 1 (2026-06-06): 38 super-propositions (S4 gained SP5b, S6 "
    "lost SP6 to the title page); all evidence-pointed; DAG unchanged and acyclic; every "
    "section serves a ratified arc move. S4 checked against the todo/030 argument map: "
    "C1-C5, S1-S7, L2-L5, I4-I7 all carried (S7 in SP1's tail, L5 as SP5b, I7 in SP7); "
    "map itself lags D-09/D-10 - sync queued as follow-up."
)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("level2-sections.json updated: U1/U4/U6 revisions applied, front_matter added")
