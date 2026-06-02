# Independent adversarial audit — todo/018 "(A)+(C) information-convention" resolution

**Target:** commit `d37183b` (main), `manuscript/derivation.qmd` @sec-termA + @sec-combine, the
todo/018+019 apparatus, and `verification/term-ac-realized-info.R`.
**Auditor stance:** adversarial — find errors, do not confirm. Every claim re-verified against the
literature, the code, and a fresh reproduction (not the cached logs). Date: 2026-06-02.

---

## VERDICT: **PASS** (headline holds; **0 BLOCKER**) — with **2 material WARNs** to fix before submission

- A citation: ok · B evidence↔source: ok (K&M re-verified in-session, all 4 quotes faithful) ·
  C reproducibility: ok (WAY-1 reproduced from scratch; render exit-0) · D consistency: **1 WARN**
  (a self-contradiction at line 906) · E honesty: **1 WARN** (overstated cross-model independence) +
  minor INFO · F lifecycle: ok.
- Engine (mechanical): 0 BLOCKER / 3 WARN / 13 INFO — the 3 WARN are confirmed brace-glob false
  positives (all 5 `cas-wolfram/verify_term_ac*.py` files exist). Reconciles with the prior
  `derivation-audit-2026-06-02-acinfo.md`.

**The headline claim under test is substantially TRUE:** the convention is correctly settled to the
observed/realized information (K&M 1998, impeccably sourced); the reported realized value −0.34→−0.46
is the committed empirical; Δ_KM is genuinely O(1) under MAR and 0 under MCAR; the code mapping is NOT
inverted; WAY-1 reproduces to machine precision. The two WARNs do not break the headline but are real
defects in the committed text — one is *exactly the GOTCHA todo/018 claimed to have avoided*.

---

## Per-claim verification (independent)

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1a | §5 quote verbatim in @sec-termA | **PASS** | derivation.qmd:952-954 / :1423 quote = K&M:544 *exactly*. |
| 1b | K&M recommends OBSERVED under MAR; naive expected biased; 0-iff-MCAR | **PASS** | K&M abstract:38, §2:105-112, §3.2:374 ("orthogonality...lost", "n&s condition...α₀=α₁=0...MCAR"). All present and read in-session. |
| 1c | `fisher_info_obs_mvn`=naive `i_N`; `observed_info_obs_mvn`=realized `i_O` (NOT inverted) | **PASS** | 00-setup.R:483 = block-diagonal, population Σ_OO, zero cross block. 00-setup.R:1064 = data-dependent via `M=Σe_Oe_Oᵀ`, `r=Σe_O`, non-zero μ×Σ cross. Mapping correct; story does NOT invert. The manuscript itself labels `fisher_info_obs_mvn` "the naive, block-diagonal information...omits the MAR cross term" (derivation.qmd:1139-1141) — consistent. |
| 2a | `|I_U − I_mc| ~ 1e-11` | **PASS** | Fresh run: 3.5e-11 / 1.3e-10 / 1.5e-10 (machine precision; abs grows ∝N, rel ~1e-13). |
| 2b | Δ_KM ≈ −0.55 non-mono / −0.44 mono, FLAT in N (O(1), not 2-pt illusion) | **PASS** | Fresh run R=2000: non-mono **−0.557 / −0.525 / −0.551** (3 N, no trend); mono **−0.440 / −0.438**. Genuinely flat. |
| 2c | MCAR control → 0 | **PASS** | Fresh run: MCAR non-mono **−0.026 / +0.009 / +0.001**. |
| 2d | `build_info`: I_N population+zero-cross; I_U selected M2_P/m1_P; mirrors fisher/observed; complete-case INCLUDED | **PASS** | term-ac-realized-info.R:94-118. At `M2=Σ_OO, m1=0` the realized block reduces EXACTLY to the naive `0.5·Dᵀ(Σ⁻¹⊗Σ⁻¹)D` and cross→0 (= K&M n&s condition). Complete cases included (:75-76, the bug-fix). `sane` check ties I_U to E[observed_info] at 1e-11. Tried to break it — faithful. |
| 3a | Blind packet leakage-free (numbers/names) | **PASS** | `extract_modes` SENT text: −0.22,−0.46,0.55,−0.34,−0.44,kenward,molenberghs,m2_p,delta_km all **ABSENT**. |
| 3b | GPT-5.5 independently got block structure (μ×Σ ∝ selected mean, Σ ∝ selected−pop 2nd moment), O(1) not O(1/n), 0-iff-MCAR | **PASS (structure/order)** | modeB ΣΣ block `½DᵀRᵀ[{S(B−A)S⊗S}+{S⊗S(B−A)S}]RD` expands to *exactly* the code's `build_info` realized−naive block; cross `(mᵀS⊗S)RD` = code `cross`. Mode B explicitly REFUTES O(1/n) → O(1) (the todo/016 blind spot, not repeated). 0-iff-MCAR derived both modes. |
| 3c | "derived two independent ways that agree" / "spontaneously the K&M recommendation" | **OVERSTATED (WARN)** | The trace functional `D=tr(J_N⁻¹J_com)−tr(J_O⁻¹J_com)` was **handed to the model in the prompt** (Mode A Q3, Mode B Q3), not independently derived. The K&M recommendation was **directly solicited** by Mode A Q4 ("which references…recommend"). GPT produced **no number** — agreement is structural/order, not "−0.55". |
| 4 | Lavaan paired gap −0.627→−0.582→−0.569 → −0.55; rem_real/rem_exp high-variance | **PASS** | n3000 log: gap −0.6275/−0.5824/−0.5686 (se 0.003–0.006, paired, low-var); rem_real/rem_exp se 0.42–0.78 (high-var). Converges toward analytic −0.55. |
| 5 | Step 3: `tr(C·I_obs⁻¹)=RIV` exact under REALIZED convention | **PASS (sound)** | By Louis, `C = I_com − I_obs^O` (selected missing info under MAR), so `tr(C·I_obs^{O,-1}) = tr(I_obs^{O,-1}I_com) − k = tr(RIV^O)` by construction. Exact under realized; would NOT hold under naive (population) info. Sign/logic correct (somewhat tautological, but right). |
| 6 | Discipline: citation / render / engine | **PASS** | @kenwardLikelihoodBasedFrequentist1998 backed by `literature/…md`, read in-session. `quarto render` **exit 0**. Engine 0 BLOCKER. |

---

## BLOCKER (0)
- none. The headline (settled value, observed-info convention, Δ_KM O(1)/MCAR, K&M sourcing, code
  mapping, WAY-1 reproduction) holds under independent re-verification.

## WARN (2 material + 3 minor)

- **derivation.qmd:906 — [D/E] internal contradiction: −0.22 mislabeled as "naive", implying
  −0.22 + Δ_KM = −0.46 (the exact GOTCHA todo/018 claims to have avoided).** The sentence reads
  "*that convention difference is the whole content of the −0.22 (naive) vs −0.46 (realized)
  separation*." But (i) the clean naive value is **+0.1→+0.3** (line 987), not −0.22; (ii) with the
  measured Δ_KM ≈ −0.58, "naive −0.22 + Δ_KM" = **−0.80 ≠ −0.46**; (iii) the −0.22→−0.46 *separation*
  is −0.24, **not** Δ_KM (−0.55/−0.58). Everywhere else (lines 880-882, 944, 1018-1024, 1058-1062)
  −0.22 is correctly framed as a *leading-order approximation to the realized value*. Line 906 is the
  lone residual that the todo/018 cleanup missed, and it directly contradicts the project's own
  recorded GOTCHA ("−0.22 + Δ ≈ −0.46 does NOT hold"). — evidence: derivation.qmd:906 vs :987-989 vs
  lavaan rem_exp; WAY-1 Δ_KM=−0.55. — fix: drop the "(naive)" label on −0.22 and the
  "−0.22 vs −0.46 separation" phrasing; state the convention gap as separating the **measured naive
  +0.1→+0.3** from the realized −0.34→−0.46 (consistent with line 987).

- **derivation.qmd:959-967, :1082-1083 — [E] overstated cross-model independence.** The margin note
  claims GPT-5.5 "independently returns the same Δ_KM…closed form…and **spontaneously** the same
  Kenward–Molenberghs observed-information recommendation." Against the actual blind packet
  (`extract_modes`): the trace functional `D` was **given in the prompt** (Mode A/B Q3) and the K&M
  recommendation was **directly asked for** (Mode A Q4). What GPT *did* independently produce — and
  it genuinely matches the code — is the ΔI **block structure** and the **O(1)-not-O(1/n)** order
  (the real todo/016 blind-spot test). — evidence: extracted-modes-AUDIT.txt Mode A Q3/Q4, Mode B Q3;
  modeA.md §4, modeB.md verdict. — fix: soften to "independently reproduced the block structure and
  the O(1)/MCAR order (the prior blind spot); the trace functional and the reference were supplied in
  the prompt." Drop "spontaneously."

- **derivation.qmd:987-989 — [C/E, minor] the "+0.13+(−0.58)=−0.45 reproduced" check is a near-identity.**
  `rem_real`, `rem_exp`, `gap` share the same `A_rb`, so `rem_real ≡ rem_exp + gap` by construction;
  "reproduced" slightly overstates it as an independent confirmation. The genuine independent check
  (analytic WAY-1 Δ_KM=−0.55 ≈ measured gap −0.58) IS present and foregrounded (lines 977-982), so the
  severity is low. — fix: phrase as "the analytic Δ_KM matches the measured paired gap; the naive and
  realized values are tied by it" rather than "reproduced." 

- **derivation.qmd:987 — [C, minor] "naive…≈+0.1→+0.3…measured at the fit" understates its softness.**
  Directly-measured `rem_exp` is +0.82/+0.01/−0.32 (se 0.42–0.78, strongly N-trending) at R=2000; the
  "+0.1→+0.3" is the R=40k anchored value (committed_realized − gap ≈ +0.29/+0.13, se~0.09). Defensible
  at R=40k but it is the softest, anchored number — not on the same footing as the low-variance paired
  gap. — fix: note the naive value is the anchored/high-variance leg; the gap and analytic Δ_KM are the
  carriers.

- **derivation.qmd:980-982 — [C, minor] "converges onto −0.55" not yet landed.** Lavaan gap at n=3000
  is −0.569 (still 0.02 above the analytic −0.55); WAY-1 analytic-at-θ₀ is −0.54/−0.55. The 0.02 is the
  θ₀-vs-θ̂ effect. Honest as a trend; phrasing "→ −0.55" is mildly optimistic. — fix: "approaching ≈−0.55
  (−0.569 at n=3000), the residual being the θ̂-vs-θ₀ offset."

## INFO (engine, all pre-existing — confirmed)
- 3× [C] `cas-wolfram/verify_term_ac{,_…}.py` "missing" — **false positives**: all 5 files exist
  (`verify_term_ac.py`, `…_nonmonotone.py`, `…_nonmonotone_genp.py`, `…_nonmonotone_sympy.py`,
  `…_sympy.py`). Engine doesn't brace-expand. No action.
- 8× [B] Appendix-A snippet fingerprint misses (incl. kenward:1419) — Mathpix-markup artifacts. The
  kenward :1419 quote was re-read this session and is **verbatim-faithful** to K&M:374. No action.
- 5× [F] foundational corpus (rubin1987, meng1994, chan2022, meng1992, vaart1998) not in todo/003 —
  tracked in todo/001 (Phase-1 corpus). No action.

---

## Reconciliation with `derivation-audit-2026-06-02-acinfo.md`
- Engine counts match exactly (0/3/13). The prior cache's claim "3 WARN are brace-glob false
  positives, files exist" — **confirmed** (all 5 exist).
- The prior cache graded E (honesty) as "ok" and B (K&M) as "supported." I **confirm B** (all four
  K&M quotes faithful). I **partially dissent on E**: the prior cache did not flag the line-906
  self-contradiction nor the overstated GPT-5.5 independence; both are real and added here as WARNs.

## What is firm vs soft (for the record)
- **FIRM (independently verified):** observed-info convention (K&M, four faithful quotes); code
  mapping (fisher=naive, observed=realized); WAY-1 analytic Δ_KM=−0.55/−0.44, flat in N, MCAR→0,
  build-vs-MC 1e-11; the low-variance paired gap; the Louis cross-term logic; render exit-0.
- **SOFT (correct but over-narrated):** the "two independent ways that agree" (true for block
  structure + O(1) order; the functional and the reference were prompt-supplied); the
  naive=+0.1→+0.3 value (anchored, high-variance); the +0.13+(−0.58)=−0.45 "reproduction"
  (near-identity).
- **WRONG (1 sentence):** line 906's "−0.22 (naive) vs −0.46 (realized)" framing.

*Independent re-verification: literature read in-session; `term-ac-realized-info.R 2000 800,1500,3000`
re-run solo (fresh printout, not cached log); blind packet re-extracted and token-scanned; both GPT-5.5
responses read critically; `quarto render` re-run (exit 0); mechanical engine re-run.*
