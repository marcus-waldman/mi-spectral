# Current status — read this when resuming

**Last updated:** 2026-06-04 (session 4 — non-nested CS-vs-AR(1) measurement EXECUTED + landed).

**Latest (2026-06-04, session 4 — the non-nested (Vuong) measurement, todo/028 EXECUTED):**
Closed the only derived-but-never-measured quantitative claim — the $(A)+(C)$ differential of
Proposition L4 for a non-nested pair (compound symmetry vs AR(1)). **Discipline:** preregistered
`todo/029` committed **alone** (`7677777`) before any engine code (the fix for todo/027 §6's
single-commit defect); CAS `verify_w4_nonnested.py` ALL PASS (general-Jacobian spectrum identity to
2e-15 on the curved $G_k$ — the new machinery: `ladder_spectrum`'s `free_idx` generalized to the
analytic Jacobian $G_k=\partial(\mu,\operatorname{vech}\Sigma)/\partial(\mu,\sigma^2,\rho)$,
evaluated at each candidate's own pseudo-true); engine `w4-nonnested-vuong.R` built + smoke-gated
(general-G ≡ selection-index to 0.0e0); pilots → **dated Amendment 1** (commit `99c7fd4`,
recalibrated the mis-scaled 0.25 MDE to an O(1) MDE, R=20,000, user-approved) before the graded run;
graded run 240k replicates, 0 errors, every assert clean. **Result (todo/029 §6):** the $(A)+(C)$
LEVEL is a large O(1) (~+2.5/curved candidate, ≤37 se) that collapses under MCAR and decouples
CS/AR1; the paired noise returns to O($\sqrt n$) for *any* pseudo-true-separated pair (nested-but-false
included → separation, not nesting, governs); naive trace overstates exact $\operatorname{tr}(\mathrm{RIV}_\perp)$
by ~9% per curved candidate (first in-vivo off L2's equality, Mode-B closed form
$\operatorname{tr}[(I+H_{11})^{-1}H_{12}H_{12}']$ also CAS-verified + landed @sec-lrt-naive).
**Similar-pair headline NOT met:** the *resolved nonzero differential* — for the similar CS-vs-AR1
pair the two large levels nearly cancel (≤1.5 se, below ~0.5 resolution; pilot's −2 was MC noise).
**Dissimilar-pair anchor MET (todo/029 Amendment 2, prereg'd commit 39cfc38 before code):** Diagonal
vs AR(1) gives a RESOLVED isolated (A)+(C) differential −1.2 (−3.5 se at N=500, un-trending, ~3–4× the
similar pair) — the positive anchor; the dissimilarity-scaling is now MEASURED, not asserted. Honest
rider: a badly-misspecified candidate (diagonal) also carries a mechanism-independent misspecification
O(1) the MCAR contrast separates, which can partially offset the net ranking bias (here net raw-MAR
−0.23). Full magnitude-mapping → sequel todo/023. Landed @sec-lrt-ac + @sec-ic-criterion caveat +
mi-spectral §5/§6 (both pairs); render exit-0; **/derivation-audit 0 BLOCKER / 0 WARN**. Also closed the two small
items: Mode-B exact-gap remark @sec-lrt-naive + CAS B4, and the impossibility-grading sentence @sec-ic.
**mi-spectral.qmd §3–§6 DRAFTED (same session):** all four application/numerics/discussion sections
written into submission prose; all three @TODOs resolved (regularity conditions summarized inline +
companion pointer; SEM/equating cites = Satorra-Bentler 2010 + Asparouhov-Muthén 2006 + Kolen-Brennan
2014, all in-session-read; references section = Quarto `::: {#refs}` auto-gen). Render exit-0, 0
citeproc warnings; /derivation-audit on mi-spectral.qmd PASS 0 BLOCKER / 0 WARN / 5 INFO (foundational
corpus). **NEXT (remaining submission work):** prose polish + a co-read pass against derivation.qmd for
consistency; the dissimilar-pair design/misspecification interplay → pairwise-matrix sequel (todo/023).

**Latest (2026-06-04, session 3 — the IC-landing session, todo/026 rev. 2 EXECUTED):**
The calibration ladder was **preregistered before any code** (`todo/027-ladder-preregistration.md`:
rungs 0–3 on saturated-anchored $T_k = 2[\bar Q(\hat\psi^*_{sat}) - \bar Q(\hat\psi^*_k)]$, the
null/noncentral split, pass criteria C1–C6), CAS-checked
(`verification/cas-wolfram/verify_ic_ladder.py`, L-A1–L-A4 ALL PASS; rung-2 $a_k = \sqrt{q_d/\Sigma\lambda^2}$,
$b_k = q_d - a_k\Sigma\lambda$ unique affine two-moment match; rung-3 = PIT through the Imhof CDF;
GPT-5.5 gate NOT triggered — both rungs are two-line corollaries of the gate-cleared @sec-lrt law,
decision recorded), built as a NEW script (`verification/ic-ladder.R`; frozen originals untouched;
candidates' constrained $\bar Q$-maximizers are CLOSED-FORM block restrictions of the E-step
moments, so $T_k = N\log(|\hat\Sigma_k|/|S^*|) \ge 0$), and run at R=2000 × {MAIN ρ=.40, WEAK
ρ=.10, JUNK ρ=0}, 6 cores, 0 errors, all asserts pass (spectrum identity 3e-15, all λ ≥ 1, zero
Imhof fallbacks). **Every preregistered criterion PASSED** (todo/027 §6): (i) null side calibrates
COMPLETELY — KS 0.281→0.228→0.026→0.019 across rungs, var ratio 3.18→0.97, rung-1 paired mean gap
0.076±0.100 = a direct MC confirmation of @eq-lrt-bias at q_d=4; (ii) where errors are overfit
flips (MAIN) rungs 2–3 REACH the oracle (0.904/0.903 vs 0.899; uncorrected 0.678, rung-1 0.814);
(iii) noncentral side shrinks by exactly the predicted factors (rung-2 ratio 0.586 ≈ a_k = 0.570;
rung-3 0.362 ≈ 1/λ_max = 0.398; rung-1 preserves 1.002); (iv) WEAK floor: oracle−rung3 = 0.170,
underfit retention 0.270 vs 0.091 — upper rungs buy NOTHING where selection is hard; (v) P8
indirect pair: equated ΔAIC mean 6.10 vs complete 10.00 (copula limitation measured). **Bonus
structural finding:** the W3 candidate family sits at Proposition L2's EXACT equality case
(block-diagonal zero patterns ⇒ I_com, I_obs decompose over within/cross-block coordinates) —
naive ≡ perp trace to 3.6e-15; the frozen SB arm's real defect was the uncorrected-statistic
wrapping (worth 0.824→0.904 at MAIN). **@sec-ic landed** in derivation.qmd (corrected criterion =
AIC_{x;y} surcharge formalized vs AICcd's doubled trace; honest W3 wording 0.65→0.81 vs 0.90;
the full ladder contrast + blunt fences: per-pair-own-null only, noncentral matching impossible
in principle, marginal equating can't calibrate differences, no telescoping for rungs 2–3; 8 new
Appendix-A entries — shimodaira2017, cavanaugh, satorra2010, asparouhov2006, kolen, imhof,
davies, chan-AoS §5.1 MC reference). Render exit-0; **/derivation-audit PASS 0 BLOCKER / 0 WARN**
(3 lifecycle WARNs fixed via todo/003 rows; "consume"/"committed sweep" jargon reworded). Issue
#1 CLOSED as superseded by rung 2 (retirement comments only in frozen scripts). Small closures:
todo/022 item-B component-candor remark at the roadmap caveat; Stage-3 SKIP recorded in todo/024.
**Stretch EXECUTED same session: `manuscript/mi-spectral.qmd` opened** — full skeleton with
§1 (intro) + §2 (setup/theorem) in draft submission prose and §3–§6 as structured stubs;
citations restricted to in-session-read sources + 3 deliberate `@TODO:` placeholders; render
exit-0; audit 0 BLOCKER / 3 WARN (the placeholders) / 4 INFO.

**NEXT SESSION (user decision, end of this session): the non-nested (Vuong-regime)
measurement — CS vs AR(1).** The only derived-but-never-measured quantitative claim in the
paper (the O(1) (A)+(C) differential for non-nested pairs, Proposition L4 → IC ranking).
Full design captured in `todo/028-nonnested-measurement-handoff.md`: equal-parameter-count
candidates (ΔAIC = ΔT exactly), closed-form CS / 1-D-profile AR(1) Q̄-maximizers, X1-heavy
MAR + MCAR mechanism-isolation twins, equal-KL money cell, nested internal control
(independence ⊂ both), pilot-based power gate, and the commit-prereg-BEFORE-code discipline
(todo/029). Bonus: curved candidates sit OFF Proposition L2's equality case — first in-vivo
naive-vs-exact trace test in a selection context. After that: mi-spectral.qmd §3–§6 drafting
+ @TODO resolution.

**Earlier (2026-06-04, session 2 — the W2 differential session, todo/024–025 EXECUTED):**
D1–D3 derived through the full multimodal protocol and landed in `derivation.qmd @sec-lrt`
(Propositions L1–L4 + numerics). Headline findings, all in-house-derived (3 independent routes +
referees, `cache/w2diff-stage1-routes.json`), CAS-verified
(`cas-wolfram/verify_w2_differential.py`) and MC-confirmed:
(i) **D1**: at H0, Bias[d̂_L] = tr(RIV_⊥) in the **I_com metric** (`@eq-lrt-bias`) — the Q̄
curvature is I_com (EM identity + FIML self-consistency), so the constrained MI fit projects
there; the naive tr(RIV)−tr(RIV_0) **always overstates** (Gram/Schur; equality iff invariance/EFMI)
— MC-discriminated at **52 se** on a μ₁=0/X1-heavy design (`w2-paired-differential-mu1-cell.R`:
2.639±0.113 vs B_direct 2.636 vs naive 8.47). The committed W2 `bias_correction` is the naive form
(immaterial there, ~5%); at H0 tr(RIV_⊥) is exactly what Chan's calibrated reference absorbs
(explains C3≈0.042, C2 conservative 0.034).
(ii) **D2**: sd(paired differential) = O(1) at H0/local vs the level's O(√n) — mechanism is the
shared-imputation common realized constant (NOT subspace projection of the linear noise); MC: sd(D)
1.5 flat vs sd(T) 18→37 (`w2-paired-differential-spotcheck.R`, P1–P5 all confirmed); reverts to
O(√n) at fixed alternatives.
(iii) **D3**: the (A)+(C) differential cancels **exactly** at H0, is O(n^{-1/2}) local, genuine
O(1) only non-nested (Vuong — read + cited).
**GPT-5.5 xhigh blind audit: BOTH MODES RETURNED + GRADED same session — CROSS-MODEL GATE
CLEARED, zero escalation triggers** (`cache/layer3-gpt-5.5-w2diff-mode{A,B}.md`; grading record in
todo/024). Mode A (blind): I_com metric boxed, formula term-for-term, definite-sign overstatement
via a third independent Schur proof, sd orders + exact (A)+(C) cancellation. Mode B (red-team):
all four claims SUSTAINED; the planted objection located precisely ("attaches the φ-gradient to a
ψ-displacement"); bonus exact closed form for the overstatement gap
`tr((I+H_11)^{-1}H_12 H_12')`.
**H1 reconciled** (todo/022 item A): pooled preregistered W1 T̂ = 2.434±0.258 sits ON the
(A+C)-augmented mean (vs 2.77 preregistered target, −1.3 se); the N=1000 FAIL = criterion artifact
(then-underived O(1) MAR term) + √n heavy tail at fixed R — **Amendment 2 documented in todo/004**
(`w1-h1-pooled-reconciliation.R`); no brute-force re-run (deliberate: direct heavy-tailed means
don't tighten). Render exit-0; audit 0 BLOCKER (3 cas-wolfram WARN = known false positives).
Intro LRT bullet + CLAUDE.md core contribution updated to the derived form ("vanishes at H0" was
wrong — it equals tr(RIV_⊥), which calibration absorbs).

**Earlier (2026-06-04, session 1):** SCOPE SPLIT — this paper = bias correction + LRT (W1/W2); the W3
distributional-calibration ladder (SB/equating/pairwise-ΔAIC) is a SEQUEL, captured in `todo/023`;
W3 SB arm (issue #1) to be retired, not fixed. Current target document is `derivation.qmd` only
(`mi-spectral.qmd` does not exist yet — submission drafting comes after). Literature stocked
2026-06-04 (Vuong, Barnard–Rubin, Self–Liang, Le Cam acquired + lit-synced). The theory layer
(todo/015–021) stays LOCKED.

**Post-session addenda (same day):** GPT-5.5 grading is COMPLETE (both modes, gate cleared — see
Latest above and todo/024); an independent-session audit of derivation.qmd returned a clean PASS
(0 BLOCKER / 0 WARN after the engine brace-glob fix `80d2d7e` — the "3 known false positives"
disclaimer is RETIRED; any new WARN is a real signal).

**SCOPE REVISION (2026-06-04, later same day — todo/026 REVISION 2):** the calibration-ladder
rungs 1–3 move **IN-PAPER** (user decision; recovered 06-03 design discussion at
`verification/cache/_equating_extract.txt`): the IC application must contrast mean (tr(RIV_⊥),
I_com metric) vs SB two-moment (coefficients now DERIVED from the @sec-lrt weighted-χ² law) vs
equipercentile equating (closed-form for nested pairs via Davies/Imhof) on saturated-anchored
pairwise ΔAIC, with the null/noncentral achievability split preregistered. **The SB arm FLIPS
retire→FIX as rung 2** (new script; frozen originals untouched; issue #1 closes after the ladder
lands). Sequel (todo/023, trimmed) keeps: de-shrinkage map, pairwise-matrix-with-Z testbed,
copula/triangle at scale. Pre-session user action: acquire Kolen & Brennan (todo/003, High).

**Next session = `todo/026-ic-landing-and-submission-handoff.md` (REVISION 2):** (1) preregister
the ladder arm (todo/027 or todo/004 Amendment 3 — BEFORE code); (2) build + run the new ladder
script (moderate scale, few cores); (3) land the combined @sec-ic (IC application + ladder
contrast + honest noncentral/copula fences); (4) small closures (todo/022 item B remark, Stage-3
SKIP disposition); (5) mi-spectral.qmd opening = stretch goal.

**Project:** JAIGP theory paper on deviance-bias correction for the Q-function under congenial multiple imputation, with applications to LRT model comparison and information-criterion model selection.

## How to resume

1. Read this file.
2. Read `IDEAS.md` — the "Comprehensive sweep results (2026-05-23)" section near the bottom has the freshest empirical landings: 60-cell W3 sweep + 18-cell W1 sweep + H3b rate arm + Phase 4 parameter-bias measurement, all run via the centralized `verification/run_all.R`. The "Reframing note (2026-05-22)" at top explains the major mid-session pivot.
3. Read `CLAUDE.md` Scope + Core contribution sections.
4. The active work item is **manuscript drafting** — all empirical witnesses are now in. Open side artifacts: `todo/007-sympy-proof-verification.md` (Sympy/Quarto algebra-verification companion to W1, pickup-able cold).

**Reproducing the empirical evidence**: `Rscript verification/run_all.R 2000 prod all 20`. Single command, ~3 hours on 20 cores, all 5 phases. Outputs at `verification/cache/run_all-prod/phase{0,1,2,3,4,5}/`.

## Open issues

- None. **[#1](https://github.com/marcus-waldman/mi-spectral/issues/1) CLOSED 2026-06-04** as
  superseded by the calibration ladder rung 2 (`verification/ic-ladder.R`, todo/027,
  derivation.qmd @sec-ic): the two-moment arm was rebuilt with coefficients DERIVED from the
  @sec-lrt weighted-χ² null law; the frozen preregistered scripts carry retirement comments
  only (logic untouched, SHA ddc9037 results stand); measured impact of the repair
  0.824→0.904 (MAIN), 0.596→0.702 (JUNK).

## What happened this session

**Big things, in chronological order:**

1. **Phase 1 corpus acquisition** — closed. 26 references in `literature/<citekey>.md`, all verified or acquired, indexed in litrev RAG. Pipeline: Zotero → migrate to drive folder → Mathpix conversion → lit-sync → citation hook enforces at edit time.
2. **Infrastructure built** — `scripts/lit_sync.py` (BBT → literature/<citekey>.md bridge), `.claude/hooks/check_citations.py` (PreToolUse hook blocking unverified cites), `.claude/skills/lit-sync/SKILL.md` (invokable as `/lit-sync`).
3. **Upstream issues filed at litrev_mcp:** #21 (embed batch overflow on math-heavy long books — patched and verified) and #22 (Windows hardening for generate_index_script — proposed fixes).
4. **Manuscript design converged** through extended discussion on style, contributions, voice, witness placement.
5. **Mid-session reframe (the big one)** — read Chan (2022, *Annals of Statistics*) "General and feasible tests with multiply-imputed datasets" and discovered it substantially preempts the original spectral-correction headline. Pivoted the paper to the deviance-bias decomposition (originally Claim 1), with Chan & Meng (2022) and Chan (2022) AoS repositioned as adjacent test-calibration work that consumes our bias-corrected numerator. See IDEAS.md Reframing note for details.
6. **Three documents updated to reflect the reframe:** IDEAS.md (major rewrite, archive at bottom), litrev `_context.md`, CLAUDE.md.
7. **Witness apparatus reduced** from V1–V7 (spectral correction validation) to W1/W2/W3 (deviance-bias-focused). W1 validates the theorem; W2 quantifies LRT power loss under local alternatives; W3 demonstrates model-selection distortion under uncorrected MI-AIC/BIC.

## Next action (pick up here)

**Write `todo/004-simulation-hypotheses.md`.** For each of W1, W2, W3:

- **W1 (theorem validation):** Empirical $E[\bar Q_\infty(\hat\theta_{\text{obs}}) - \ell_{\text{com}}(\hat\theta_{\text{obs}})]$ should match $+\tfrac{1}{2}\text{tr}(\text{RIV})$. Imputation-bias term should match $+\text{tr}(\text{RIV})$. Estimation-mismatch should match $-\tfrac{1}{2}\text{tr}(\text{RIV})$.
- **W2 (LRT power):** Under local alternatives $\theta = \theta_0 + n^{-1/2}\delta$, bias-corrected LRT statistic has higher power than bias-uncorrected (both using Chan 2022 AoS reference distribution). Gap widens with $\|\delta\|$. Four configurations: oracle, bias-corrected + Chan, bias-uncorrected + Chan, bias-uncorrected + EFMI/Meng-Rubin.
- **W3 (model selection bias):** Uncorrected MI-AIC systematically favors models with smaller RIV. True-model selection rate for corrected MI-AIC ≈ oracle; uncorrected drops by some materially-large fraction.

For each: predicted outcome, simulation design (N, M, missingness pattern, models compared), fallback path if prediction fails. Pre-registered design.

## Then implement W1, W2, W3

Three pending tasks (#25, #26, #27) — execute in order W1 → W2 → W3. W1 is the gate: if it fails empirically, the framework is wrong and the paper doesn't justify. W3 is the headline empirical claim; gets the most polish once W1/W2 are solid.

Code lives in `verification/`:

```
verification/
├── 00-setup.R                  # shared MVN data gen, MI, fits
├── W1-bias-decomposition.R     # theorem validation
├── W2-lrt-power.R              # LRT power under local alternatives
├── W3-model-selection.R        # MI-AIC/BIC accuracy
└── cache/                      # RDS outputs read by manuscript
```

## Open user actions

- **Task #13:** Refresh BBT keys for 3 Zotero items still in snake_case (`li1991large`, `li1991significance`, `petersen2008matrix`). Cosmetic — corpus works without it, but breaks the camelCase pattern of the other 23. Right-click each → Better BibTeX → Refresh BibTeX key in Zotero desktop. Then re-export BBT.

## Project state at a glance

| Component | Status |
|---|---|
| Phase 1 literature corpus (todo/001) | ✅ 26 papers, all verified/acquired |
| Citation-discipline infrastructure | ✅ lit-sync skill + check_citations.py hook live |
| Reference-acquisition backlog (todo/003) | ✅ tracking system in place |
| Chan-Meng verification reading (todo/002) | ✅ both papers cold-read, machinery understood |
| Project narrative (IDEAS.md, CLAUDE.md, litrev) | ✅ all updated for the 2026-05-22 reframe |
| Witness apparatus design | ✅ W1/W2/W3 defined; pre-registration document pending |
| Simulation code (verification/) | ⏸ not started |
| Manuscript draft (manuscript/) | ⏸ not started |

## Key documents

- `IDEAS.md` — directional anchor, reframing note + archive
- `CLAUDE.md` — scope, core contribution, lineage, citation discipline, R style
- `manuscript/mi-spectral.qmd` — empty Quarto stub waiting for §3 draft
- `literature/<citekey>.md` — 26 source markdown files, hook-protected
- `literature/mi-spectral-better-bibTeX.bib` — BBT export, source of truth for citekeys
- `scripts/lit_sync.py` — Zotero/BBT → literature/ bridge
- `.claude/hooks/check_citations.py` — PreToolUse enforcement
- `.claude/skills/lit-sync/SKILL.md` — `/lit-sync` slash command
- `verification/` — empty, awaiting W1/W2/W3 implementations
- `todo/001-literature-and-hooks.md` — closed (Phase 1 corpus acquisition)
- `todo/002-verification-implementation.md` — Chan-Meng reading queue, mostly closed
- `todo/003-references-to-acquire.md` — living reference backlog
- `todo/004-simulation-hypotheses.md` — closed (W1/W2/W3 preregistered at SHA ddc9037; results in IDEAS.md)
- `todo/005-comprehensive-sweep-hypotheses.md` — closed (sweep complete 2026-05-23; H3b partial)
- `todo/006-comprehensive-sweep-execution.md` — closed (executed)
- `todo/007-sympy-proof-verification.md` — open side artifact (Sympy/Quarto algebra-verification notebook spec; pickup-able cold)

## External issues filed

- [litrev_mcp #21](https://github.com/marcus-waldman/litrev_mcp/issues/21) — embed batch overflow on math-heavy long books. Patched (tiktoken-based token counting, 100K batch cap).
- [litrev_mcp #22](https://github.com/marcus-waldman/litrev_mcp/issues/22) — Windows hardening for generate_index_script (SSL cert via truststore + UTF-8 stdout). Proposed fixes; pending upstream.
