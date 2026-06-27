# Display-equation line-breaks (todo/034 items 1+2), 2026-06-27
#
# Long display equations overflowed the right text margin in the assembled preview
# (xelatex Overfull \hbox: eq-lrt-bias 112pt over, the T_imp tr-chain 79pt, the score Z
# block 30pt, eq-timp-pieces 3.6pt). Where an equation overflows it is clipped at the
# page edge, which is the "renders as $$ / not given" symptom Marcus saw -- there is no
# malformed markup (no literal $$ or unparsed {#eq-} in the .tex; all 21 labelled
# displays parse). The fix is to break the wide multi-part displays at their relation
# symbols / comma+\qquad separators onto aligned lines.
#
# Method: each block is wrapped in \begin{aligned}...\end{aligned} (or \begin{gathered}
# for the one heterogeneous list) and broken with \\. Edits are expressed only as
# (anchor -> replacement) substring swaps on the ORIGINAL inner, so no mathematical token
# is ever retyped. A token-preservation verifier confirms that, after removing only the
# scaffold tokens we add (\begin{aligned},\end{aligned},\begin{gathered},\end{gathered},
# &, \\) and the pure spacing macros \qquad/\quad (some converted to breaks) and all
# whitespace, the new inner is character-for-character identical to the old inner.

import json, re

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"
DEC = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\decisions.md"

BLK = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
NL = "\n"
BR = r" \\"          # LaTeX line break (space + backslash-backslash)

# (pid, block_index, env, [(anchor, replacement), ...])
# replacements insert & for alignment and BR+NL for line breaks; nothing else changes.
EDITS = [
    ("S2-P13", 0, "aligned", [
        (r"\hat d_{\mathrm{L}} \;=\;", r"\hat d_{\mathrm{L}} &\;=\;"),
        (r", \qquad \hat\psi^{*} = \arg\max", r"," + BR + NL + r"\hat\psi^{*} &= \arg\max"),
    ]),
    ("S4-P3", 0, "aligned", [
        (r"\mathrm{RIV} \;=\;", r"\mathrm{RIV} &\;=\;"),
        (r"I_{\text{mis}\mid\text{obs}} \;=\; I_{\text{obs}}^{-1} I_{\text{com}}",
         r"I_{\text{mis}\mid\text{obs}}" + BR + NL + r"&\;=\; I_{\text{obs}}^{-1} I_{\text{com}}"),
        (r"- I_k, \qquad \operatorname{tr}(\mathrm{RIV}) = ",
         r"- I_k," + BR + NL + r"\operatorname{tr}(\mathrm{RIV}) &= "),
    ]),
    ("S4-P4", 0, "aligned", [
        (r"\bar Q_\infty(\theta) \;:=\;", r"\bar Q_\infty(\theta) &\;:=\;"),
        (r"\big) \;=\; \mathbb{E}_{\tilde\phi}",
         r"\big)" + BR + NL + r"&\;=\; \mathbb{E}_{\tilde\phi}"),
    ]),
    ("S4-P5", 0, "aligned", [
        (r"T \;=\;", r"T &\;=\;"),
        (r"\text{imputation-bias term}} \;+\; \underbrace",
         r"\text{imputation-bias term}}" + BR + NL + r"&\;+\; \underbrace"),
    ]),
    ("S4-P6", 1, "aligned", [
        (r"T_{\text{est}} \;=\;", r"T_{\text{est}} &\;=\;"),
        (r"(\hat\theta_{\text{obs}} - \hat\theta_{\text{com}}) + O_p(n^{-3/2}).",
         r"(\hat\theta_{\text{obs}} - \hat\theta_{\text{com}})" + BR + NL + r"&\quad + O_p(n^{-3/2})."),
    ]),
    ("S4-P6", 3, "aligned", [
        (r"\operatorname{Cov}(U_{\text{obs}}, U_{\text{com}}) =",
         r"\operatorname{Cov}(U_{\text{obs}}, U_{\text{com}}) &="),
        (r"I_{\text{obs}}, \qquad \operatorname{Cov}(\hat\theta_{\text{obs}}, \hat\theta_{\text{com}}) =",
         r"I_{\text{obs}}," + BR + NL + r"\operatorname{Cov}(\hat\theta_{\text{obs}}, \hat\theta_{\text{com}}) &="),
    ]),
    ("S4-P6", 4, "aligned", [
        (r"\big) \;=\; I_{\text{obs}}^{-1} + I_{\text{com}}^{-1}",
         r"\big) &\;=\; I_{\text{obs}}^{-1} + I_{\text{com}}^{-1}"),
        (r"- 2I_{\text{com}}^{-1} \;=\; I_{\text{obs}}^{-1} - I_{\text{com}}^{-1},",
         r"- 2I_{\text{com}}^{-1}" + BR + NL + r"&\;=\; I_{\text{obs}}^{-1} - I_{\text{com}}^{-1},"),
    ]),
    ("S4-P6", 5, "aligned", [
        (r"\mathbb{E}[T_{\text{est}}] \;=\;", r"\mathbb{E}[T_{\text{est}}] &\;=\;"),
        (r"\big) \;=\; -\tfrac12\big(\operatorname{tr}",
         r"\big)" + BR + NL + r"&\;=\; -\tfrac12\big(\operatorname{tr}"),
        (r"- k\big) \;=\; -\tfrac12\operatorname{tr}(\mathrm{RIV}).",
         r"- k\big)" + BR + NL + r"&\;=\; -\tfrac12\operatorname{tr}(\mathrm{RIV})."),
    ]),
    ("S4-P7", 0, "aligned", [
        (r"T_{\text{imp}} \;=\;", r"T_{\text{imp}} &\;=\;"),
        (r"\big] - \ell_{\text{mis}\mid\text{obs}}(\hat\theta_{\text{obs}}).",
         r"\big]" + BR + NL + r"&\quad - \ell_{\text{mis}\mid\text{obs}}(\hat\theta_{\text{obs}})."),
    ]),
    ("S4-P7", 1, "aligned", [
        (r"\mathbb{E}[T_{\text{imp}}] \;=\;", r"\mathbb{E}[T_{\text{imp}}] &\;=\;"),
        (r"(\hat\theta_{\text{obs}})] - \mathbb{E}_{\theta_0}",
         r"(\hat\theta_{\text{obs}})]" + BR + NL + r"&\quad - \mathbb{E}_{\theta_0}"),
    ]),
    ("S4-P7", 2, "aligned", [
        (r"\mathbb{E}[T_{\text{imp}}] \;=\;", r"\mathbb{E}[T_{\text{imp}}] &\;=\;"),
        (r"}_{(A)} \;+\; \underbrace", r"}_{(A)}" + BR + NL + r"&\;+\; \underbrace"),
        (r"}_{\text{main cross term}} \;+\; \underbrace",
         r"}_{\text{main cross term}}" + BR + NL + r"&\;+\; \underbrace"),
    ]),
    ("S4-P7", 3, "aligned", [
        (r"\big] \;=\; \operatorname{tr}\!\big(I_{\text{mis}\mid\text{obs}}\, \operatorname{Cov}",
         r"\big]" + BR + NL + r"&\;=\; \operatorname{tr}\!\big(I_{\text{mis}\mid\text{obs}}\, \operatorname{Cov}"),
        (r"\hat\theta_{\text{obs}})\big) \;=\; \operatorname{tr}\!\big(I_{\text{mis}\mid\text{obs}}\, I_{\text{obs}}^{-1}\big)",
         r"\hat\theta_{\text{obs}})\big)" + BR + NL + r"&\;=\; \operatorname{tr}\!\big(I_{\text{mis}\mid\text{obs}}\, I_{\text{obs}}^{-1}\big)"),
        (r"+ O(n^{-1}) \;=\; \operatorname{tr}(\mathrm{RIV})",
         r"+ O(n^{-1})" + BR + NL + r"&\;=\; \operatorname{tr}(\mathrm{RIV})"),
    ]),
    ("S4-P7b", 0, "aligned", [
        (r"(A) = ", r"(A) &= "),
        (r"O(1), \qquad (C) = ", r"O(1)," + BR + NL + r"(C) &= "),
    ]),
    ("S4-P7b", 1, "aligned", [
        (r"(A)+(C) \;=\;", r"(A)+(C) &\;=\;"),
        (r"\Big] + O(n^{-1}),", r"\Big]" + BR + NL + r"&\quad + O(n^{-1}),"),
    ]),
    ("S4-P10", 0, "aligned", [
        (r"\big] \;=\; \operatorname{tr}(\mathrm{RIV}_\perp) + O(n^{-1}),",
         r"\big] &\;=\; \operatorname{tr}(\mathrm{RIV}_\perp) + O(n^{-1}),"),
        (r"O(n^{-1}), \qquad \operatorname{tr}(\mathrm{RIV}_\perp) \;:=\;",
         r"O(n^{-1})," + BR + NL + r"\operatorname{tr}(\mathrm{RIV}_\perp) &\;:=\;"),
        (r"\big) - \operatorname{tr}\big[(G^\top I_{\text{com}} G)^{-1}",
         r"\big)" + BR + NL + r"&\quad - \operatorname{tr}\big[(G^\top I_{\text{com}} G)^{-1}"),
    ]),
    ("S4-P10", 1, "aligned", [
        (r"Z \;=\; S +", r"Z &\;=\; S +"),
        (r"+ O_p(1) \;=\; I_{\text{com}}\, I_{\text{obs}}^{-1}\, S",
         r"+ O_p(1)" + BR + NL + r"&\;=\; I_{\text{com}}\, I_{\text{obs}}^{-1}\, S"),
        (r"+ O_p(1), \qquad \operatorname{Var}(Z) \;=\;",
         r"+ O_p(1)," + BR + NL + r"\operatorname{Var}(Z) &\;=\;"),
    ]),
    ("S4-P11", 1, "aligned", [
        (r"\, G \;\succeq\;", r"\, G" + BR + NL + r"&\;\succeq\;"),
    ]),
    ("S4-P11", 2, "aligned", [
        (r"\operatorname{tr}(\mathrm{RIV}_\perp) \;=\;",
         r"\operatorname{tr}(\mathrm{RIV}_\perp)" + BR + NL + r"&\;=\;"),
        (r"H_{12}^\top\big] \;\ge\; 0,",
         r"H_{12}^\top\big]" + BR + NL + r"&\;\ge\; 0,"),
    ]),
    ("S4-P19", 1, "gathered", [
        (r"I_{\text{com}}, \qquad \sum_j \lambda_{k,j}",
         r"I_{\text{com}}," + BR + NL + r"\sum_j \lambda_{k,j}"),
    ]),
    ("S4-P20", 1, "aligned", [
        (r"\hat d^{(2)}_k \;=\;", r"\hat d^{(2)}_k &\;=\;"),
        (r"+ b_k, \qquad a_k = \sqrt", r"+ b_k," + BR + NL + r"a_k &= \sqrt"),
        (r"\,}, \qquad b_k = q_{d,k}", r"\,}," + BR + NL + r"b_k &= q_{d,k}"),
    ]),
    ("S4-P20", 2, "aligned", [
        (r"\hat d^{(3)}_k \;=\;", r"\hat d^{(3)}_k &\;=\;"),
        (r"\big), \qquad W_k = ", r"\big)," + BR + NL + r"W_k &= "),
    ]),
]

SCAFFOLD = [r"\begin{aligned}", r"\end{aligned}",
            r"\begin{gathered}", r"\end{gathered}", "&", r"\\"]

def norm(s):
    for t in SCAFFOLD:
        s = s.replace(t, "")
    s = s.replace(r"\qquad", "").replace(r"\quad", "")
    return "".join(s.split())

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)
by_id = {p["id"]: p for p in l3["paragraphs"]}

touched = set()
nblocks = 0
for pid, bidx, env, edits in EDITS:
    p = by_id[pid]
    prose = p["draft_prose"]
    matches = list(BLK.finditer(prose))
    assert bidx < len(matches), f"{pid}: block index {bidx} out of range ({len(matches)} blocks)"
    m = matches[bidx]
    full_old = m.group(0)            # exact $$...$$
    inner_old = m.group(1)           # inner incl. surrounding spaces
    inner_new = inner_old
    for anchor, repl in edits:
        cnt = inner_new.count(anchor)
        assert cnt == 1, f"{pid} blk{bidx}: anchor not unique ({cnt}): {anchor!r}"
        inner_new = inner_new.replace(anchor, repl)
    # token-preservation check (content identical modulo scaffold + spacing)
    assert norm(inner_new) == norm(inner_old), (
        f"{pid} blk{bidx}: token-preservation FAILED\n"
        f"  old-norm: {norm(inner_old)}\n  new-norm: {norm(inner_new)}")
    body = inner_new.strip()
    full_new = ("$$" + NL + "\\begin{" + env + "}" + NL +
                body + NL + "\\end{" + env + "}" + NL + "$$")
    assert prose.count(full_old) == 1, f"{pid} blk{bidx}: full block not unique in prose"
    p["draft_prose"] = prose.replace(full_old, full_new)
    touched.add(pid)
    nblocks += 1

FLAG = "eqn-linebreaks 2026-06-27 (todo/034 #1+2): wide displays broken at relations/separators into aligned lines; tokens preserved."
for pid in sorted(touched):
    fl = by_id[pid]["review"].get("flags")
    by_id[pid]["review"]["flags"] = (fl + " | " if fl else "") + FLAG

l3["metrics_gate"]["notes"] = (
    f"Equation line-breaks 2026-06-27 (todo/034 #1+2): {nblocks} wide display blocks in "
    f"{len(touched)} paragraphs ({', '.join(sorted(touched))}) wrapped in aligned/gathered "
    "and broken at relation symbols / comma+qquad separators to clear the right-margin "
    "overflow (eq-lrt-bias was 112pt over). Token-preservation verified mechanically. "
    "Prior note: " + (l3["metrics_gate"].get("notes") or "")
)

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

entry = (
    "\n## Display-equation line-breaks (2026-06-27, todo/034 #1+2)\n\n"
    f"Wide display equations that overflowed the right text margin in the assembled "
    f"preview ({nblocks} blocks across {len(touched)} paragraphs: "
    f"{', '.join(sorted(touched))}) were broken at their relation symbols and "
    "comma/\\qquad separators onto aligned lines (\\begin{aligned}/\\end{aligned}, one "
    "gathered list). This clears the xelatex Overfull \\hbox warnings (worst was "
    "eq-lrt-bias at 112pt over) and the associated \"equation renders as $$ / not given\" "
    "symptom, which was clipping at the page edge, not malformed markup. Every "
    "mathematical token is preserved verbatim -- the edits only insert alignment "
    "ampersands and line breaks, verified by a normalize-and-compare check.\n"
)
with open(DEC, "a", encoding="utf-8") as f:
    f.write(entry)

print(f"equation line-breaks applied: {nblocks} blocks across {len(touched)} paragraphs")
print("paragraphs:", sorted(touched))
