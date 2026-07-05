# Evidence-map table (todo/048 follow-on; Marcus's claims-to-evidence organization).
#
# Gate: Marcus approved manuscript/reviews/style/evidence-map-proposal-2026-07-05.md
# ("Agree. trim the Design column--you can just refer to the section in the paper.
# Approved", 2026-07-05). Amendment applied: the Study column carries the design's
# run-in name only (the designs are stated under the same names in the setup
# subsection), no one-line design summaries. Includes the RECOMMENDED S4-P1 pointer
# clause. New unit S5-P1b inserted directly after S5-P1; a pure index, no new claims;
# all numbers restate the manuscript's own values (verified 27/27 pre-proposal).

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

paras = l3["paragraphs"]
ids = [p["id"] for p in paras]
if "S5-P1b" in ids:
    raise SystemExit("S5-P1b already exists -- aborting.")
i_p1 = ids.index("S5-P1")

TABLE = (
    "The correspondence between the derivations and the studies is collected in "
    "@tbl-evidence-map before the designs are stated: each row names a claim, the "
    "analytic result behind it, the study that tests it, and the outcome with the "
    "exhibit that reports it. The designs are stated under the same study names in "
    "the paragraphs that follow, and a reader can treat the table as the section's "
    "map, returning to it from any single design or result.\n\n"
    "| Claim tested | Analytic basis | Study | Result |\n"
    "|---|---|---|---|\n"
    "| The averaged log-likelihood overstates its complete-data counterpart by "
    "$\\tfrac12\\operatorname{tr}(\\mathrm{RIV}) + (A){+}(C)$ | @thm-bias | Theorem "
    "validation | pooled $2.43 \\pm 0.26$, centered on the augmented band $2.42$ to "
    "$2.55$; the $N=1000$ cell is the one reported miss (@fig-w1-theorem) |\n"
    "| Known-scale collapse: bias $0$ under deterministic FIML, "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under proper MI | @eq-knownscale | "
    "Known scale and sign regime | $0.025 \\pm 0.018$ and $-0.536 \\pm 0.018$ against "
    "targets $0$ and $-0.561$ (@fig-knownscale) |\n"
    "| Imputing from the true model reverses the sign of the total | the conditioning "
    "fork at @eq-qbar | Known scale and sign regime | the total reverses sign, as the "
    "fitted-versus-true-model distinction requires (reported with @fig-knownscale) |\n"
    "| A calibrated reference absorbs the null bias, so correcting the numerator on "
    "top double-counts | @eq-spectrum-sum | Likelihood ratio | Type I error $0.042$ "
    "uncorrected and $0.034$ corrected, near the nominal $0.05$ (@fig-lrt-absorption) "
    "|\n"
    "| The differential bias at the null is $\\operatorname{tr}(\\mathrm{RIV}_\\perp)$, "
    "not the naive trace difference | @prp-lrt, @prp-naive | Formula discrimination | "
    "$2.64 \\pm 0.11$ and $2.70 \\pm 0.11$ against the predicted $2.64$; the naive "
    "$8.5$ excluded at $52$ standard errors (@fig-discrimination) |\n"
    "| Pairing holds the differential's noise at $O(1)$ | @prp-pairing | Pairing | "
    "null sd near $1.5$ and flat, against $18.4$ to $36.5$ for a single model; the "
    "fixed alternative reverts (@fig-pairing) |\n"
    "| Uncorrected MI-AIC favors the largest-RIV candidate, and the trace correction "
    "restores selection | @thm-bias, @eq-ic-corrected | Selection sweep | $0.67$ "
    "uncorrected, $0.82$ corrected, benchmark $0.90$ at $N=500$; 100% of "
    "misclassifications on the largest-RIV candidate (@fig-w3-selection) |\n"
    "| The null side calibrates map by map, and noncentral statistics shrink by "
    "predictable factors | the three maps of @sec-derivations | Distribution-matching "
    "ladder | two-moment and equating arms reach $0.904$ and $0.903$ against the "
    "benchmark $0.899$; shrinkage $0.59$ and $0.36$ against predicted $0.56$ and "
    "$0.40$ (@tbl-ladder, @fig-ladder-internals) |\n"
    "| Block-diagonal families fall at the equality case, and per-model maps cannot "
    "calibrate a difference | @prp-naive; the structural limits of @sec-derivations | "
    "Distribution-matching ladder | equality to $3.6 \\times 10^{-15}$; naive-input "
    "cost $0.824$ against $0.904$; difference law $6.10$ and $5.99$ against $10.00$ "
    "and $7.10$ (@tbl-structural-limits) |\n"
    "| The design-imbalance differential decouples only for separated candidates and "
    "grows with dissimilarity | @prp-ac-diff | Non-nested measurement | the dissimilar "
    "pair resolves at $-1.2$ ($3.5$ standard errors); the similar pair stays below "
    "resolution, the reported failure (@fig-w4-nonnested) |\n"
    "| The bootstrap engine tracks the analytic arm, bounding the cost of not running "
    "data augmentation | the G3 scope statement of @sec-discussion | Engine "
    "sensitivity | $\\operatorname{tr}(\\mathrm{RIV})$ within $2$ to $3$ percent; "
    "selection within $0.011$ |\n\n"
    ": **The studies of this section mapped to the claims they test.** Each row names "
    "a claim from @sec-derivations, the analytic result behind it, the study that "
    "tests it, and the outcome with its exhibit. {#tbl-evidence-map}"
)

new_unit = {
    "id": "S5-P1b",
    "section": "S5",
    "goal": "roadmap",
    "proposition": (
        "Every study in this section tests a named claim from @sec-derivations; "
        "@tbl-evidence-map indexes claim -> analytic basis -> study -> result in one "
        "place, introducing no new claims (a pure index of results stated elsewhere)."
    ),
    "depends_on": ["S5-P1"],
    "dep_types": ["builds_on"],
    "review": {
        "serves_L2": "S5-SP1 (framing)",
        "serves_L1": (
            "M4b SIMULATION STUDIES (D-03-A1 full empirical account); Marcus "
            "2026-07-05: readers cannot hold the S4-claim / S5-design / S5-result "
            "join in working memory -- give them the map"
        ),
        "sets_up": "all S5",
        "topic_sentence": (
            "The correspondence between the derivations and the studies is collected "
            "in @tbl-evidence-map before the designs are stated."
        ),
        "closing_sentence": (
            "...a reader can treat the table as the section's map, returning to it "
            "from any single design or result."
        ),
        "status": "drafted",
        "flags": (
            "Added 2026-07-05 per Marcus's claims-to-evidence directive (gate record "
            "manuscript/reviews/style/evidence-map-proposal-2026-07-05.md, approved "
            "with the Study-column trim). Pure index: every cell restates numbers "
            "verified verbatim against the manuscript (27/27); both failed "
            "predictions included as the text reports them."
        ),
    },
    "draft_prose": TABLE,
    "audit": {
        "status": "complete",
        "citations": {},
        "numbers": {},
        "notes": (
            "All values restate S5 results paragraphs; mirrors the "
            "level4-evidence.json join table in human-readable form."
        ),
    },
}

paras.insert(i_p1 + 1, new_unit)
print("S5-P1b inserted after S5-P1.")

# ---- approved S4-P1 pointer clause ----
p41 = {q["id"]: q for q in paras}["S4-P1"]
old = "and all empirical evidence is reported in @sec-simulations."
new = ("and all empirical evidence is reported in @sec-simulations, where "
       "@tbl-evidence-map maps each claim to its study.")
if p41["draft_prose"].count(old) != 1:
    raise SystemExit("S4-P1: pointer anchor not found uniquely -- aborting.")
p41["draft_prose"] = p41["draft_prose"].replace(old, new)
print("S4-P1: pointer clause added.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("evidence map applied: 88 paragraphs now expected.")
