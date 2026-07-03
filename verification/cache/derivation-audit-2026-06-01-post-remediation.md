# Derivation audit — `manuscript/derivation.qmd` (post-remediation re-run)

**Run:** 2026-06-01 (post-remediation) · **Skill:** `/derivation-audit` (read-only; flag-only) · **Target:** `manuscript/derivation.qmd`

**PASS** — 0 BLOCKER / 0 WARN / 15 INFO

A citation `0/0/0` · B evidence↔source `0 WARN / 9 INFO` · C reproducibility `0 WARN / 1 INFO` · D consistency `0 WARN` · E honesty `0 WARN / 1 INFO` · F lifecycle `0 WARN / 5 INFO`

**Diff vs prior report (`derivation-audit-2026-06-01.md`, 17:44 — 0 BLOCKER / 10 WARN / 14 INFO):** **all 10 WARN cleared.** Mechanical engine went 5 WARN → 0; the 5 semantic WARN (W1, W2, W3, W4, Shimodaira) all resolved and re-verified against in-session source reads. Render is clean (exit 0; all 20 Appendix-B cells `Done`, incl. the new `lst-mc-trriv` assert).

**Method.** Mechanical engine (`audit_derivation.py`: 0 BLOCKER / 0 WARN / 13 INFO) + targeted semantic re-check of the *changed* attributions (W1 Meng/Rubin, Shimodaira §8) against `literature/*.md` text read in-session; the 21 unchanged attributions retain the prior audit's **supported** verdicts.

---

## BLOCKER (0)

None.

## WARN (0)

None. Each prior WARN is resolved:

- **W1** L4 Source line [B, load-bearing] — **CLEARED.** The variance-recovery *equality* `T_∞ = Var(θ̂_obs) = I_obs⁻¹` is now grounded on R4 (congeniality) + Rubin §4.2 proper-imputation randomization-validity (conditions (4.2.1)-(4.2.2) and Result 4.1, `:3489`/`:3563`) + regularity (L1); Meng (Lemma 3 `:486`; Main result `:503`/`:511`) is cited for the efficiency *dominance* (inequality) only — "at least as efficient … at most the same width." Verified against Meng `:480`-`:524` and Rubin `:3475`-`:3568`. The Rubin §4.2 variance-validity quote was added to `@sec-src-rubin1987`.
- **W2** Theorem `(A)+(C)` text [D, headline-adjacent] — **CLEARED.** The general-MVN **monotone** asymptote is now the derived closed form `(A)+(C)_∞ ≈ −0.22` (+0.54 entropy-gradient, −0.76 Hessian; n-stable −0.220/−0.223/−0.221; MCAR control ≈0; `verification/term-a-mar-closedform.R`); "reported empirically" is restricted to the **non-monotone** case (≲−0.46). Consistent with the `@sec-termA` "Scope (honest)" block.
- **W3** "exact under MCAR" [E/D, headline] — **CLEARED.** Now "holds **to leading order under MCAR** (the design-imbalance term is `O(n⁻¹)`)", consistent with the theorem's `+O(n⁻¹)` remainder, L2 "exact only to leading order", and the body's "`(A)+(C)=O(n⁻¹)` under MCAR".
- **W4** undefined `A7`/`A8` labels [D] — **CLEARED.** The three inline uses now resolve to **named, cross-referenced** identities in `@sec-alg`: the score-covariance identity (split into its own named bullet) at the two `A8` sites, the Schur-complement bullet at the `A7` site. (A1–A8 numbering was *not* used — it would collide with the existing Term-A proof-step labels A1–A5; the plan's sanctioned named-cross-ref alternative was taken.)
- **W5** legacy `W1-sweep.R` pointer [C] — **CLEARED.** Appendix-B intro now cites `verification/W1-bias-decomposition.R` (preregistered original).
- **lst-mc-trriv** no assert [C] — **CLEARED.** Added `assert sp.expand(trace_normal(Trace(I_obs.inv()*I_com), n) - n - trRIV) == 0`; the render executes and passes it (Cell 4/20 `Done`).
- **Shimodaira §8** "open" [B] — **CLEARED.** Now "named there (§8) as **future work in its concluding remarks**" with the faithful quote "combine a missing mechanism with other sampling mechanisms, such as the covariate-shift … problem" (source `:486`).
- **Little 2019 / Rubin 1976 / Anderson 2003** lifecycle [F×3] — **CLEARED.** Added a "Foundational references verified during the 2026-06-01 derivation audit" subsection to `todo/003`. (Also updated the stale Chan-2022-AoS row from "proposed — URGENT" to "cited".)

## INFO (15)

- `derivation.qmd` Appendix-A snippet fingerprint misses (8) [B] — all confirmed **faithful** (Mathpix math/hyphen markup, not drift): schafer (`:954`, the known OCR-garbled `P(Y|θ)` line — manuscript quote elides the RHS, faithful; Tier-5 corpus fix optional/deferred), vaart (`:1039`), **rubin1987 (`:1082`, the new §4.2 quote — verified verbatim vs `:3480`/`:3486`/`:3489`)**, little (`:1100`,`:1104`), kenward (`:1171`), pawitan (`:1186`,`:1190`).
- `derivation.qmd` non-monotone `(A)+(C)` asymptote ≲−0.46 [C] — extrapolated from two finite-n points; the doc honestly hedges ("hedged from two still-increasing points"). No action required.
- `derivation.qmd:427` `#sec-ledger` anchor id uses "ledger" [E] — anchor only, not reader-visible (heading renders "Assumptions and lemmas"); intentionally **skipped** (cosmetic; renaming risks dangling `@sec-ledger` cross-refs for zero reader benefit).
- 5 foundational keys (Rubin 1987, Meng 1994, Chan & Meng 2022, Meng & Rubin 1992, van der Vaart 1998) in `todo/001` not `todo/003` [F] — expected for the Phase-1 corpus; no action.

---

## Bottom line

The derivation is now WARN-clean. The four reader-facing precision items (W1 Meng-vs-equality, W2 stale closed-form text, W3 "exact under MCAR", W4 undefined A7/A8) plus the legacy pointer (W5), the missing `lst-mc-trriv` assert, the Shimodaira softening, the Hens "bias-corrected" qualifier, the two "consume" jargon sites, and the three untracked lifecycle rows are all resolved. Render exits 0. Residual INFO is mechanical fingerprint markup (all faithful), the honestly-hedged non-monotone extrapolation, the intentionally-skipped `#sec-ledger` anchor, and the expected Phase-1 corpus lifecycle items.
