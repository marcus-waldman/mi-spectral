#!/usr/bin/env python3
r"""
todo/037 precision pass -- BATCH 1 (orphan clusters + one pattern-4 jargon cut).
Per-paragraph, human-gated, each verified by an independent adversary; Marcus ruled
the batch. Targeted replacement, idempotent. Some rewrites add no math/citation; none
drop any token.

  S2-P6 -- 3 orphan joins (participial "drawing"/"noting"; "It is" -> compound)  APPLY AS-IS
  S3-P4 -- triple "It was ... It was ... It was ..." -> one compound predicate     APPLY AS-IS
  S3-P8 -- "It asks ... It states ..." join; closing_sentence metadata synced       APPLY AS-IS
  S6-P8 -- "The protocol caught X. It caught Y. And it forced Z." -> one tricolon    APPLY AS-IS
  S3-P6 -- pattern 4: "Load-bearing claims" -> "The claims the paper's results       APPLY w/ REV
           depend on" (T-03 jargon cut); topic_sentence metadata synced

Run:  py manuscript/plan/updates/update-batch1-todo037-20260628.py
Then: py scripts/check_plan.py ; py scripts/cadence_flag.py ; py scripts/color_commentary_flag.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"

R = {
    "S2-P6": [
        ("@weiMonteCarloImplementation1990 implement the E-step by simulation. They draw $z^{(1)},\\dots,z^{(m)}$ from the conditional predictive distribution of the missing data.",
         "@weiMonteCarloImplementation1990 implement the E-step by simulation, drawing $z^{(1)},\\dots,z^{(m)}$ from the conditional predictive distribution of the missing data."),
        ("Their Remark 2 makes the connection to multiple imputation explicit. They note that Rubin (1987) referred to the quantities $z^{(1)}, \\ldots, z^{(m)}$ as multiple imputations.",
         "Their Remark 2 makes the connection to multiple imputation explicit, noting that Rubin (1987) referred to the quantities $z^{(1)}, \\ldots, z^{(m)}$ as multiple imputations."),
        ("The $m \\to \\infty$ limit of the averaged log-likelihood is written $\\bar Q_\\infty(\\theta)$. It is the central object of this paper.",
         "The $m \\to \\infty$ limit of the averaged log-likelihood is written $\\bar Q_\\infty(\\theta)$ and is the central object of this paper."),
    ],
    "S3-P4": [
        ("Every analytic claim entered a fixed sequence. It was derived first. It was then verified symbolically in two independent computer-algebra systems. It was then confirmed by Monte Carlo simulation against criteria fixed in advance.",
         "Every analytic claim entered a fixed sequence. It was derived first, then verified symbolically in two independent computer-algebra systems, and finally confirmed by Monte Carlo simulation against criteria fixed in advance."),
    ],
    "S3-P8": [
        ("The protocol does not ask the reader to trust an AI derivation. It asks the reader to check one. It states where the checking has already been done and where it cannot be.",
         "The protocol does not ask the reader to trust an AI derivation. It asks the reader to check one, and states where the checking has already been done and where it cannot be."),
    ],
    "S6-P8": [
        ("The protocol caught a sign error that eight of nine blind re-derivations shipped. It caught a wrong shortcut in an early entropy-gradient argument. And it forced every failed prediction into @sec-simulations.",
         "The protocol caught a sign error that eight of nine blind re-derivations shipped, caught a wrong shortcut in an early entropy-gradient argument, and forced every failed prediction into @sec-simulations."),
    ],
    "S3-P6": [
        ("Load-bearing claims were re-derived blind by a model from an independent family.",
         "The claims the paper's results depend on were re-derived blind by a model from an independent family."),
    ],
}

META = {
    "S3-P8": [
        ("closing_sentence",
         "It states where the checking has already been done and where it cannot be.",
         "It asks the reader to check one, and states where the checking has already been done and where it cannot be."),
    ],
    "S3-P6": [
        ("topic_sentence",
         "Load-bearing claims were re-derived blind by a model of an independent lineage.",
         "The claims the paper's results depend on were re-derived blind by a model from an independent family."),
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

    meta_applied = meta_skipped = 0
    for pid, fields in META.items():
        review = by_id[pid]["review"]
        for field, old, new in fields:
            if review.get(field) == old:
                review[field] = new
                meta_applied += 1
            elif review.get(field) == new:
                meta_skipped += 1
            else:
                raise SystemExit(f"ERROR: {pid}.review.{field}: neither old nor new found:\n  OLD: {old!r}\n  GOT: {review.get(field)!r}")

    with L3.open("w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    n = sum(len(v) for v in R.values())
    nm = sum(len(v) for v in META.values())
    print(f"batch1 prose fixes applied: {applied}, already-applied: {skipped} (of {n})")
    print(f"metadata syncs applied: {meta_applied}, already-applied: {meta_skipped} (of {nm})")


if __name__ == "__main__":
    main()
