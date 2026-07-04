# G9 non-normal illustration (v1 AI-review response, todo/040 Phase 3, r3#2, 2026-07-03)
#
# New Discussion paragraph S6-P4d (G9), inserted after G8 (S6-P4c) and before S6-P5,
# reporting the Phase-3 non-normal illustration: Gamma (estimated-scale) confirms the
# pattern; Bernoulli (nominal "scale-free" exemplar) misses both registered targets,
# traced to a genuine mechanism (Bernoulli/Poisson are one-parameter families with no
# independent dispersion parameter, so they don't satisfy the known-scale condition
# the way a known-variance Gaussian mean does). See
# todo/040-v1-review-response-registration.md Sec.10 for the full numbers and
# manuscript/reviews/v1/response/response-letter.md r3#2 for the response-letter text.
#
# Also updates the G1-G8 -> G1-G9 range references in level1-thesis.json and
# level2-sections.json, matching the precedent set when G8 was added (G1-G7 -> G1-G8).

import json

L1 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level1-thesis.json"
L2 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level2-sections.json"
L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

G9 = {
    "id": "S6-P4d",
    "section": "S6",
    "goal": "scope_limit",
    "proposition": "G9: a first non-normal check (Gamma estimated-scale, Bernoulli scale-free) confirms the pattern for Gamma but misses both registered targets for Bernoulli; the miss traces to Bernoulli/Poisson lacking an independent dispersion parameter, so they do not satisfy the known-scale flat-entropy condition the way a known-variance Gaussian mean does.",
    "depends_on": ["S6-P4"],
    "dep_types": ["qualifies"],
    "review": {
        "serves_L2": "S6-SP1",
        "serves_L1": "M5 DISCUSSION (inverse gradient; D-11 no provenance section; no Conclusion)",
        "sets_up": "-",
        "topic_sentence": "A first check outside the normal family sharpens, rather than removes, the scope of G6.",
        "closing_sentence": "...not which named family is in use.",
        "status": "drafted",
        "flags": "added 2026-07-03 (todo/040 Phase 3 non-normal illustration, r3#2, Marcus-directed via AskUserQuestion). G-number continues G6 (S6-P4) through G8 (S6-P4c); range G1-G8 -> G1-G9 in level1/level2.",
    },
    "draft_prose": (
        "**G9.** A first check outside the normal family sharpens, rather than removes, "
        "the scope of G6. We ran the theorem on two non-normal likelihoods, a Gamma "
        "model that estimates its own dispersion and a Bernoulli model that does not. "
        "The Gamma check confirms the pattern already established for the normal "
        "family. A deterministic plug-in measures $+0.32$ times the trace, inside a "
        "wide interval around the predicted one half, and a genuine posterior draw "
        "measures $-0.52$, more negative than the plug-in in the same direction the "
        "multivariate-normal posterior-draw check already found. The Bernoulli check "
        "misses both of its targets, and the reason traces to the family itself "
        "rather than to the run. The known-scale collapse needs the conditional "
        "missing-data entropy to stay flat as the estimated parameter moves, which "
        "holds for a Gaussian mean under a fixed variance because that entropy "
        "depends on the variance alone. That flatness does not hold for a Bernoulli "
        "probability, whose own entropy changes with the probability and is flat only "
        "at the single point one half. Bernoulli and Poisson estimate one parameter "
        "that sets both the mean and the entire shape of the distribution, so neither "
        "family carries a separate dispersion parameter to hold fixed in the first "
        "place. The registered prediction had treated the absence of a named "
        "dispersion parameter as the same condition as a flat entropy. They are not "
        "the same condition, and the measured Bernoulli numbers confirm the "
        "difference. The generalization the check leaves in place asks whether a "
        "family's own missing-data entropy depends on the parameter being estimated, "
        "not which named family is in use."
    ),
    "audit": {
        "status": "complete",
        "citations": {},
        "numbers": {
            "Gamma FITTED +0.32 (predicted +0.5), brms draw -0.52": "verif:verification/cache/phase3-nonnormal-prod.rds",
            "Bernoulli FITTED +0.85 (predicted ~0), mice draw +0.63 (predicted ~-0.5)": "verif:verification/cache/phase3-nonnormal-prod.rds",
        },
        "notes": "Phase-3 non-normal illustration (G9); Gamma is a scored confirmation, Bernoulli is a disclosed, mechanism-traced miss, not a pre-registered pass target beyond the theorem's own scope condition.",
    },
}

ids = [p["id"] for p in l3["paragraphs"]]
if "S6-P4d" in ids:
    raise SystemExit("S6-P4d already exists -- aborting to avoid duplication.")
insert_at = ids.index("S6-P4c") + 1
if ids[insert_at] != "S6-P5":
    raise SystemExit(f"Expected S6-P5 immediately after S6-P4c, found {ids[insert_at]!r} -- aborting.")
l3["paragraphs"].insert(insert_at, G9)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
print(f"Inserted S6-P4d (G9) at index {insert_at}.")


def bump_g8_to_g9(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    n = text.count("G1-G8")
    if n == 0:
        raise SystemExit(f"{path}: no 'G1-G8' occurrences found -- aborting.")
    text = text.replace("G1-G8", "G1-G9")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{path}: replaced {n} occurrence(s) of G1-G8 -> G1-G9.")


bump_g8_to_g9(L1)
bump_g8_to_g9(L2)
