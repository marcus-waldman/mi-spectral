# G9 rewrite (todo/045c Sec.2, ratified by Marcus 2026-07-04)
#
# Replaces the STALE pre-quorum G9 (S6-P4d) with the corrected,
# chronology-first account per the quorum's binding amendments
# (tkal-reviews/quorum-phase3-bernoulli-20260703/) and the todo/045 Q2
# findings (Lemma P derivation + CAS + pre-registered blind scans + GPT-5.5
# gate CLEARED + Gemini repo-grounded compliance validation, 9/10 HONORED,
# the one finding fixed pre-ratification).
#
# ONE wording deviation from the ratified staged text, recorded here and in
# todo/045c: the staged final sentence used an em-dash pair ("-- not by the
# family's name -- and non-canonical links remain underived"), which the
# check_plan prose gate bans; landed as two plain sentences with identical
# content. closing_sentence updated to match.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

p = {q["id"]: q for q in l3["paragraphs"]}["S6-P4d"]

# guard against drift: we must be replacing the stale pre-quorum text
if not p["draft_prose"].startswith(
    "**G9.** A first check outside the normal family sharpens, rather than removes,"
):
    raise SystemExit("S6-P4d does not hold the expected STALE G9 text -- aborting.")

p["proposition"] = (
    "G9: a first check outside the normal family exposed a registration error "
    "(Bernoulli misclassified as known-scale by a category-error analogy), whose "
    "correction was then derived (canonical-link GLMs hit the general $+\\tfrac12$ "
    "trace value; a base-measure term moves Poisson to $+0.104$), CAS-verified, and "
    "confirmed by pre-registered blind scans -- including a Student-t fixed-scale "
    "exemplar that verifies the known-scale collapse outside the normal family for "
    "the first time."
)

p["draft_prose"] = (
    "**G9.** A first check outside the normal family exposed an error in our own "
    "registration before it sharpened the theory, and we report it in that order. "
    "We registered a Gamma model as the estimated-scale exemplar and a Bernoulli "
    "model as the known-scale exemplar. The registered Bernoulli prediction for the "
    "genuine posterior draw was approximately $-0.5$ times the trace; the measured "
    "value was $+0.63$ (se $0.16$), about seven standard errors away and of the "
    "opposite sign, and the plug-in arm missed its registered target of "
    "approximately $0$ by about five standard errors. The registration had treated "
    "the absence of a named dispersion parameter as the known-scale condition, but "
    "the collapse actually requires the family's conditional missing-data entropy "
    "to stay flat in the estimated parameter, and the binary entropy is not flat, "
    "because its derivative is the negative logit. After the miss we derived what a "
    "canonical-link model should show, rather than re-scoring against an assumed "
    "value. Under response-only MCAR missingness the two order-one design terms in "
    "the theorem's proof cancel exactly for any canonical link, so the plug-in "
    "lands on the general $+\\tfrac12$ trace value plus a base-measure term. That "
    "term is zero for Bernoulli and moves Poisson to a derived $+0.10$. Because "
    "this derivation was produced after the miss, its predictions were "
    "pre-registered and then run blind. The Bernoulli plug-in reaches an asymptote "
    "of $+0.51\\pm0.04$ across an $N$-scan against the derived $+0.5$, and the "
    "earlier $+0.85$ at $N{=}200$ proves to have been Monte-Carlo noise around a "
    "true $+0.52$. A Poisson model, simulated here for the first time only after "
    "its target was fixed, lands at $+0.11\\pm0.03$ against its derived $+0.10$. A "
    "Student-t location model with fixed scale, a genuine known-scale family, "
    "measures $+0.02\\pm0.05$ for the plug-in and $-0.48\\pm0.05$ for the posterior "
    "draw against the derived $0$ and $-0.5$, so the known-scale collapse now has a "
    "check outside the normal family. The superseded Bernoulli draw value also "
    "carried a fixed imputation seed across repetitions, which its quoted standard "
    "error did not reflect. The Gamma result stays directional ($+0.32\\pm0.20$ "
    "against the predicted one half), because its log link is not canonical and the "
    "new argument does not cover it. What G6 keeps is therefore sharper but real. "
    "Membership in the two regimes is decided by the entropy-gradient condition "
    "and, for canonical links, by the base measure, not by the family's name. "
    "Non-canonical links remain underived."
)

p["review"]["topic_sentence"] = (
    "A first check outside the normal family exposed an error in our own "
    "registration before it sharpened the theory, and we report it in that order."
)
p["review"]["closing_sentence"] = "Non-canonical links remain underived."
p["review"]["flags"] = (
    p["review"]["flags"]
    + " | rewritten 2026-07-04 per the quorum amendments (todo/045 Sec.4 -> "
      "todo/045c, Marcus-ratified after the GPT-5.5 gate + Gemini compliance "
      "validation); chronology-first disclosure; numbers from "
      "phase3-family-scan-*-prod.rds; one em-dash-removal wording deviation "
      "recorded in the update script."
)

p["audit"]["numbers"] = {
    "Bernoulli draw registered -0.5, measured +0.63 (se 0.16); plug-in registered "
    "~0, measured +0.85 (se 0.16) (superseded originals, quoted as history)":
        "verif:verification/cache/phase3-nonnormal-prod.rds",
    "Bernoulli plug-in asymptote +0.51+/-0.04; N=200 truth +0.52":
        "verif:verification/cache/phase3-family-scan-bern_fitted-prod.rds",
    "Poisson +0.11+/-0.03 vs derived +0.10":
        "verif:verification/cache/phase3-family-scan-pois_fitted-prod.rds",
    "t exemplar +0.02+/-0.05 and -0.48+/-0.05 vs 0 / -0.5":
        "verif:verification/cache/phase3-family-scan-t_exemplar-prod.rds",
    "draw discount -0.31+/-0.07 at N=2000 vs derived -0.261":
        "verif:verification/cache/phase3-family-scan-bern_draw-prod.rds",
    "Gamma FITTED +0.32 (se 0.20), brms draw -0.52":
        "verif:verification/cache/phase3-nonnormal-prod.rds",
}

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)

print("G9 (S6-P4d) rewritten per todo/045c Sec.2.")
