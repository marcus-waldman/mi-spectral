# Sweep batch 6 (final section batch): S6 Discussion to the D-26 register.
#
# Gate: Marcus approved manuscript/reviews/style/batch-S6-proposal-2026-07-05.md
# ("Approved", 2026-07-05). S6-P1 = ratified Demo 6 WITH the authorized incidental
# content fix (six -> nine specific limits; the Discussion runs G1-G9). 14 surgical
# repairs clear the last 10 vocabulary warnings; the three remaining "practical
# recommendation/summary" formulas move to the register's advice voice; both D-26
# signature sentences stay. Guards: full-string equality on S6-P1; unique-substring
# asserts elsewhere; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

# ------------------------------------------------ S6-P1 (full; Demo 6 + count fix)
OLD_P1 = (
    "The result is scoped by its own mechanism. The scope comes first. The deviance "
    "optimism that inflates the criteria exists only when the fit estimates a scale or "
    "covariance. In that case the conditional missing-data entropy depends on the "
    "estimated parameters. A known-scale, location-only fit has no such bias under "
    "deterministic FIML and only $-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under "
    "proper MI. That is why the estimated-scale clause sits in the theorem rather than "
    "in a footnote. Congeniality is assumed throughout. What the bias becomes without "
    "it [@mengMultipleImputationInferencesUncongenial1994a] is a separate question. "
    "This paper does not take it up. Beyond these scope conditions, six specific "
    "limits remain. Each is stated next to the claim it qualifies, with its evidential "
    "standing. They are followed by one conjecture, three directions, and the answer "
    "to the question the paper opened with."
)
NEW_P1 = (
    "The scope of the result follows from its own mechanism, and we state that scope "
    "first. The deviance optimism that inflates the criteria exists only when the fit "
    "estimates a scale or covariance, because only then does the conditional "
    "missing-data entropy depend on the estimated parameters; a known-scale, "
    "location-only fit has no such bias under deterministic FIML and only "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$ under proper MI, which is why the "
    "estimated-scale clause belongs in the statement of the theorem rather than in a "
    "footnote. Congeniality is assumed throughout, and what the bias becomes without "
    "it [@mengMultipleImputationInferencesUncongenial1994a] is a separate question "
    "that this paper does not take up. Beyond these scope conditions, nine specific "
    "limits remain, each stated next to the claim it qualifies together with its "
    "evidential standing, and they are followed by one conjecture, three directions, "
    "and the answer to the question the paper opened with."
)

SUBS = [
    ("S6-P3",
     "Imputation-engine robustness is empirical and scoped, which qualifies",
     "Imputation-engine robustness is empirical and restricted in scope, which "
     "qualifies"),
    ("S6-P3",
     "The weak-signal floor is a measurement, not an impossibility proof",
     "The weak-signal shortfall is a measurement, not an impossibility proof"),
    ("S6-P4b",
     "The practical recommendation is to diagnose congeniality before trusting "
     "bias-corrected selection.",
     "In practice it is wise to diagnose congeniality before trusting bias-corrected "
     "selection."),
    ("S6-P4c",
     "BIC already sits close to the complete-data benchmark",
     "BIC is already close to the complete-data benchmark"),
    ("S6-P4c",
     "The practical recommendation is to expect the correction to matter most for BIC "
     "where its own penalty has not yet reached that regime, and to read any "
     "BIC-based comparison at a small sample with that limit in mind.",
     "In practice the correction should be expected to matter most for BIC where its "
     "own penalty has not yet reached that regime, and any BIC-based comparison at a "
     "small sample should be read with that limit in mind."),
    ("S6-P4d",
     "so the plug-in lands on the general",
     "so the plug-in bias is the general"),
    ("S6-P4d",
     "lands at $+0.11\\pm0.03$ against its derived $+0.10$",
     "measures $+0.11\\pm0.03$ against its derived $+0.10$"),
    ("S6-P4d",
     "Membership in the two regimes is decided by",
     "Membership in the two cases is decided by"),
    ("S6-P5",
     "One question is left as a conjecture. We label it as one. We conjecture that "
     "the bias-corrected likelihood-ratio comparison dominates its uncorrected "
     "counterpart in power uniformly. The preregistered likelihood-ratio study's "
     "power arms provide partial support (@sec-simulations). We state no theorem.",
     "One question is left as a conjecture, and we label it as one. We conjecture "
     "that the bias-corrected likelihood-ratio comparison dominates its uncorrected "
     "counterpart in power uniformly; the preregistered likelihood-ratio study's "
     "power arms provide partial support (@sec-simulations), but we state no "
     "theorem."),
    ("S6-P6",
     "Running the headline studies under data augmentation",
     "Running the main studies under data augmentation"),
    ("S6-P7",
     "one model genuinely fits better",
     "one model truly fits better"),
    ("S6-P7",
     "The practical summary for an applied reader is short. Correct the criterion, or "
     "match its null distribution. Then trust the result the way complete-data "
     "results are trusted, subject to the stated conditions.",
     "In practical terms the advice is short: correct the criterion, or match its "
     "null distribution, and then trust the result the way complete-data results are "
     "trusted, subject to the stated conditions."),
    ("S6-P8",
     "two preregistered headlines were given up rather than rescued",
     "two preregistered predictions were given up rather than salvaged"),
]

p1 = para["S6-P1"]
if p1["draft_prose"] != OLD_P1:
    raise SystemExit("S6-P1: current draft_prose does not match the gated Current "
                     "text -- aborting (no writes made).")
p1["draft_prose"] = NEW_P1
print("S6-P1: replaced (full, six -> nine).")

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if old not in cur:
        raise SystemExit(f"{pid}: expected substring not found -- aborting:\n  {old[:80]}")
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring not unique -- aborting:\n  {old[:80]}")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: replaced (sub).")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("batch 6 applied: 9 units touched; S6-P2/P4/P7b untouched.")
