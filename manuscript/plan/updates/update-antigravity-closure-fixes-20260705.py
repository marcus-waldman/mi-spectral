# Antigravity response-closure validation fixes (todo/050 report; Marcus approved all
# three, 2026-07-05). Manuscript side: (A) G8 (S6-P4c) gains the explicit corrected
# MI-BIC formulation the original reviewer demanded and the letter already claims,
# mirroring @eq-ic-corrected's notation; (B) the Background AIC paragraph (S2-P10) is the
# one parameter-count k the contra#14 rename missed -- renamed to q, closing the
# validator's second partial. (Fix C, the letter's r1#8 relabel, is a direct letter edit,
# not level3.) Guards: unique-substring asserts; any drift aborts before writes.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

para = {q["id"]: q for q in l3["paragraphs"]}

SUBS = [
    # (A) G8: explicit MI-BIC formulation as the second sentence.
    ("S6-P4c",
     "BIC carries the same directional bias as AIC, but its own penalty grows with the "
     "sample size while AIC's does not, so at the sizes used in the main sweep BIC is "
     "already close to the complete-data benchmark before any correction is applied.",
     "BIC carries the same directional bias as AIC, but its own penalty grows with the "
     "sample size while AIC's does not, so at the sizes used in the main sweep BIC is "
     "already close to the complete-data benchmark before any correction is applied. "
     "The corrected criterion is "
     "$\\mathrm{BIC}_{\\mathrm{MI}}^{c}(k) = -2\\bar Q_\\infty(\\hat\\psi^{*}_k) + "
     "q_k\\log N + \\operatorname{tr}(\\mathrm{RIV}_k)$: the same trace correction as "
     "@eq-ic-corrected applied to the same deviance, with BIC's own "
     "sample-size-dependent penalty and the complete-data $N$ in it."),
    # (B) Background AIC paragraph: the missed parameter-count k -> q (prose + display).
    ("S2-P10",
     "the needed correction for the downward bias from replacing $\\theta$ with its "
     "estimate $\\hat\\theta$ is simply to add the parameter count $k$.",
     "the needed correction for the downward bias from replacing $\\theta$ with its "
     "estimate $\\hat\\theta$ is simply to add the parameter count $q$."),
    ("S2-P10",
     "$$ \\mathrm{AIC} \\;=\\; -2\\log(\\text{maximum likelihood}) + 2k. $$",
     "$$ \\mathrm{AIC} \\;=\\; -2\\log(\\text{maximum likelihood}) + 2q. $$"),
]

for pid, old, new in SUBS:
    p = para[pid]
    cur = p["draft_prose"]
    if cur.count(old) != 1:
        raise SystemExit(f"{pid}: substring count {cur.count(old)} != 1 -- aborting:\n  {old[:70]}")
    p["draft_prose"] = cur.replace(old, new)
    print(f"{pid}: applied.")

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("done: 2 units touched (3 substitutions).")
