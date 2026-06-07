# S4 part (c): rename the anchored statistic T_k -> hat d_k, 2026-06-07
#
# Marcus: T collides with the theorem's total bias T (eq-split). The anchored
# statistic is a deviance, so it joins part (b)'s family: hat d_L there,
# hat d_k here, maps hat d_k^(1..3). Bridge sentence notes the companion's T_k.
# P21/P22 checked: no T_k occurrences. eq-split's T unchanged.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
paras = {p["id"]: p for p in l3["paragraphs"]}

for pid in ("S4-P19", "S4-P20"):
    t = paras[pid]["draft_prose"]
    t = t.replace("T^{(1)}_k", "\\hat d^{(1)}_k")
    t = t.replace("T^{(2)}_k", "\\hat d^{(2)}_k")
    t = t.replace("T^{(3)}_k", "\\hat d^{(3)}_k")
    t = t.replace("$T_k$", "$\\hat d_k$")
    t = t.replace("Every $T_k$", "Every $\\hat d_k$")
    t = t.replace("T_k \\;=\\;", "\\hat d_k \\;=\\;")
    t = t.replace("F_{W_k}(T_k)", "F_{W_k}(\\hat d_k)")
    t = t.replace("a_k T_k + b_k", "a_k \\hat d_k + b_k")
    t = t.replace("T_k - \\operatorname{tr}", "\\hat d_k - \\operatorname{tr}")
    paras[pid]["draft_prose"] = t

# bridge sentence in P19, after the anchored-statistic display sentence
old = ("Anchoring costs nothing, because AIC ranking is invariant to the common shift, "
       "and it buys three things.")
new = ("The companion derivation writes $T_k$ for this statistic; the deviance notation "
       "is used here because the paper's $T$ is the total bias of @eq-split. Anchoring "
       "costs nothing, because AIC ranking is invariant to the common shift, and it "
       "buys three things.")
assert old in paras["S4-P19"]["draft_prose"]
paras["S4-P19"]["draft_prose"] = paras["S4-P19"]["draft_prose"].replace(old, new)

assert "T_k" not in paras["S4-P19"]["draft_prose"].replace("$T_k$", "")  # only the bridge mention remains
for pid in ("S4-P19", "S4-P20"):
    paras[pid]["audit"]["notes"] = (paras[pid]["audit"]["notes"] +
        " Renamed T_k -> hat d_k 2026-06-07 (collision with the bias total T; bridge sentence to the companion's T_k).").strip()

l3["metadata"]["status"] = "drafting_s4_dk_renamed"

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

# sanity: no bare T_k outside the bridge
import re
for pid in ("S4-P19", "S4-P20", "S4-P21", "S4-P22"):
    body = paras[pid]["draft_prose"]
    hits = [m.start() for m in re.finditer(r"T_k", body)]
    bridge_ok = pid == "S4-P19" and len(hits) == 1
    assert not hits or bridge_ok, f"unexpected T_k in {pid}: {hits}"

print("anchored statistic renamed to hat d_k; bridge added; sanity passed")
