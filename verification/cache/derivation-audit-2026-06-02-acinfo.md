## Derivation audit — manuscript/derivation.qmd  (post todo/018 @sec-termA upgrade)

**PASS** — 0 BLOCKER / 3 WARN / 13 INFO
A citation ok · B evidence↔source ok (K&M attributions verified in-session) · C reproducibility ok (3 WARN are pre-existing brace-glob false positives) · D consistency ok · E honesty ok · F lifecycle ok

All WARN/INFO are **pre-existing** and unrelated to this session's edits (the @sec-termA /
@sec-combine (A)+(C) information-convention upgrade). The edits introduced **no** new blockers,
broken pointers, or unsupported attributions.

### BLOCKER (0)
- none

### WARN (3) — all pre-existing, all false positives
- derivation.qmd:657 — [C] pointer `verification/cas-wolfram/verify_term_ac_nonmonotone{,_genp}.py` "missing" — evidence: brace-expansion the engine does not expand; both `verify_term_ac_nonmonotone.py` and `..._genp.py` EXIST — fix: none (engine limitation; pre-existing).
- derivation.qmd:1003 — [C] pointer `..._nonmonotone{,_sympy}.py` "missing" — evidence: `..._nonmonotone.py` and `..._nonmonotone_sympy.py` EXIST — fix: none (pre-existing).
- derivation.qmd:1118 — [C] pointer `verify_term_ac{,_sympy}.py` "missing" — evidence: `verify_term_ac.py` and `verify_term_ac_sympy.py` EXIST — fix: none (pre-existing).

### INFO (13) — all pre-existing
- 8× Appendix-A snippet fingerprint misses (schafer, vaart, rubin1987, little ×2, kenward:1419, pawitan ×2) — evidence: Mathpix math-markup artifacts; the kenward §3.2 quote at :1419 was re-read this session and is faithful (orthogonality lost under MAR; necessary-and-sufficient = MCAR) — fix: none.
- 5× foundational corpus not in todo/003 lifecycle (rubin1987, meng1994, chan2022, meng1992, vaart1998) — evidence: tracked in todo/001 (Phase-1 corpus) — fix: none.

### Semantic verdict on this session's edits (dimensions B / C / E)
- **B (K&M attributions, verified against `literature/kenwardLikelihoodBasedFrequentist1998.md` read in-session):**
  - §5 verbatim quote "provided the observed information matrix is used, conventional likelihood based frequentist inference is applicable in the MAR setting" — **supported** (exact, source :544).
  - "observed (realized) information is the principled MAR convention; naive expected info biased; cross-terms 0 iff MCAR" — **supported** (abstract; §3.2 eqs 9–11 with selection shift α₁; n&s = MCAR, source :374).
- **C (new numbers → reproducible artifacts that exist):** Δ_KM ≈ −0.55 (non-mono) / −0.44 (mono), MCAR→0, build-vs-MC 1e-11 → `verification/term-ac-realized-info.R` (ran; `cache/term-ac-realized-info-log.txt`). Paired gap −0.627/−0.582/−0.569 at n=800/1500/3000 → `verification/scratch-rem-realized-expected-lavaan.R` (ran; `cache/rem-realized-expected-lavaan-n3000-log.txt`). Two-ways/blind GPT-5.5 → `todo/019` + `cache/layer3-gpt-5.5-acinfo-mode{A,B}.md`. All exist.
- **C (evidence-type vs claim-type):** "Δ_KM is O(1), n-stable" backed by analytic flat-in-N (−0.557/−0.525/−0.551) AND three lavaan N-points converging to the asymptote — not a single finite-n point. No WARN.
- **E (honesty):** "settled", "derived two ways", "approximation" (for −0.22) all match the evidence the document admits; no "proved"/"exact"/"general" overreach; no banned reader-facing house jargon. The −0.22 is framed as a leading-order *approximation* (not the headline), and the headline realized value −0.34→−0.46 carries the K&M convention citation. No overclaim.
