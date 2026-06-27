#!/usr/bin/env python3
"""
todo/035 review (Marcus, 2026-06-27): no direct quotation of other work --
paraphrase or summarize instead, keeping the citation to the stating passage.
This reverses the verbatim-quote half of style rule T-06 for documented-open
claims (the claim and its citation are preserved; only the verbatim quoting is
removed). Targeted substring replacements preserve all surrounding math,
citations, and prose.

Idempotent: each replacement is a no-op if the quote is already gone.

Run:  py manuscript/plan/updates/update-no-direct-quotes-todo035-20260627.py
Then: py scripts/check_plan.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

# (paragraph id, verbatim-quoting original, paraphrase) ---------------------- #
REPLACEMENTS = [
    ("S1-P2",
     'It closes by saying the method "seems worthwhile to be further '
     'investigated, both theoretically as well as in practical situations". '
     "That investigation lay beyond the paper's scope "
     "[@consentinoclaeskensOrderSelectionTests2010].",
     "Its authors call for further theoretical and practical study of the "
     "method and place that work beyond their own scope "
     "[@consentinoclaeskensOrderSelectionTests2010]."),

    ("S1-P2",
     'The first comprehensive study of model selection after multiple '
     'imputation calls the literature "surprisingly sparse" '
     "[@schomakerModelSelectionModel2014a]. The same study cautions that "
     'selecting by averaged criteria "is not supported by MI literature." '
     'For variable selection, "there are currently no guidelines" '
     "[@woodHowShouldVariable2008a].",
     "The first comprehensive study of model selection after multiple "
     "imputation describes the available literature as unexpectedly thin "
     "[@schomakerModelSelectionModel2014a]. That study also cautions that "
     "selecting models by averaged criteria has no support in the "
     "multiple-imputation literature. A dedicated study of variable selection "
     "with multiply imputed data reports that no guidelines yet exist "
     "[@woodHowShouldVariable2008a]."),

    ("S2-P8",
     'It is "the usual approximation of the posterior distribution as normal", '
     "a Laplace-type approximation [@Tierney01031986].",
     "It is the usual treatment of the posterior distribution as approximately "
     "normal, a Laplace-type approximation [@Tierney01031986]."),

    ("S2-P10",
     'It "needs a correction for the downward bias introduced by replacing '
     '$\\theta$ by $\\hat\\theta$. This correction is simply realized by adding '
     '$k$," the parameter count.',
     "It needs a correction for the downward bias from replacing $\\theta$ with "
     "its estimate $\\hat\\theta$, and that correction is simply to add the "
     "parameter count $k$."),
]

NOTE = ("Direct quotes of other work paraphrased per Marcus 2026-06-27 "
        "(no verbatim quoting; citation to the stating passage retained).")


def main():
    d = json.loads(L3.read_text(encoding="utf-8"))
    by_id = {p["id"]: p for p in d["paragraphs"]}

    applied = 0
    for pid, old, new in REPLACEMENTS:
        p = by_id[pid]
        prose = p["draft_prose"]
        if old in prose:
            p["draft_prose"] = prose.replace(old, new, 1)
            applied += 1
            print(f"{pid}: paraphrased a direct quote")
        elif new in prose:
            print(f"{pid}: already paraphrased (skip)")
        else:
            raise SystemExit(f"ERROR: neither quote nor paraphrase found in {pid}")

    # honest audit note on the three touched paragraphs
    for pid in {r[0] for r in REPLACEMENTS}:
        a = by_id[pid].setdefault("audit", {})
        notes = a.get("notes", "")
        if "paraphrased per Marcus 2026-06-27" not in notes:
            a["notes"] = (notes + " " + NOTE).strip()

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"done: {applied} replacement(s) applied.")


if __name__ == "__main__":
    main()
