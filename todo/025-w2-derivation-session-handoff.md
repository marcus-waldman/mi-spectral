# Todo 025 — Handoff: derive the W2 LRT differential (D1–D3), audit it, reconcile H1

**Status:** Handoff (2026-06-04). Execute in a **fresh session** (user plans to run it in ultracode).
Continues todo/024 (the analytic-first plan, written 2026-06-03) under the scope split recorded in
todo/023 + memory `project-scope-split-2026-06-03`. The literature is now fully stocked — nothing on
the citation side blocks this session.

## 0. Scope frame (decided 2026-06-03–04, do not re-litigate)

- **This paper = bias correction + LRT application (W1/W2).** The W3 distributional-calibration
  ladder (SB two-moment, equipercentile equating, pairwise-ΔAIC matching, common-reference anchoring,
  triangle-closure residuals, noncentrality de-shrinkage) is the SEQUEL — parked in `todo/023`. Do
  not start it; at most a future-work pointer sentence.
- **Current target document is `manuscript/derivation.qmd` ONLY.** The JAIGP submission file
  (`mi-spectral.qmd`) does NOT exist yet (confirmed 2026-06-03 — CLAUDE.md/todo references to its
  §4/§5/§6 are aspirational). Submission drafting comes after derivation.qmd is done.
- **W3 SB arm (issue #1): formally retire**, don't fix — a fixed SB arm is the sequel's rung 2.
- **Sequencing directive (user):** analytic derivation FIRST, blind GPT-5.5 adversarial audit
  SECOND, simulation LAST. Multimodal evidence before any full-scale run.

## 1. LOCKED — do NOT re-open (settled + audited, todo/015–021)

- Headline `E[T]=+½tr(RIV)` + the `+tr/−½tr` split + the `+tr(RIV)` deviance/IC correction
  (= Shimodaira `AIC_{x;y}`); scope-fenced to estimated-scale/covariance models; `Q̄_∞` = FITTED
  predictive (not oracle).
- `(A)+(C)` structure + K&M realized-info convention + closed-form `Δ_KM≈−0.55`.
- `(A)+(C)` absolute value: sign / O(1) order / MCAR-vanishing / O(1/n)-remainder are FIRM; the
  value is NOT independently pinned (−0.22 = conditional analytic anchor). Leave it.

## 2. PRIMARY DELIVERABLE — the D1–D3 derivation through the full protocol

Full claim statements in `todo/024-w2-differential-analytic-first.md`. Setting: nested models
`ψ0 ⊂ ψ` (df gap `q_d`), both fit to the SAME congenially imputed MVN data under ignorable MAR;
`d̂_L = 2[Q̄_∞(ψ̂*) − Q̄_∞(ψ̂0*)]`.

**Stage 1 — derive in-house (Claude lineage), two independent ways where feasible + CAS:**

- **D1 (make rigorous):** `Bias[d̂_L] = [tr RIV_ψ − tr RIV_ψ0] + 2[(A+C)_ψ − (A+C)_ψ0] + O(1/n)`;
  pin down exactly which realized quantities are common to the two fits on shared imputations.
- **D2 (load-bearing NEW claim):** the per-dataset paired differential `ac_i(ψ) − ac_i(ψ0)` has sd
  of strictly lower order than the level's `O(√n)`. Conjectured mechanism: the `O(√n)` linear noise
  `α^⊤δ` agrees on the shared parameter subspace for nested fits; the difference retains only the
  `q_d`-dim complement → `O(1)` sd. DERIVE the order, don't assume. This is the analytic content of
  the manuscript's "structurally better-conditioned" clause.
- **D3:** differential → 0 at H0 to leading order; derive its magnitude under local alternatives
  `ψ = ψ0 + n^{−1/2}h` (contiguity/LAN, van der Vaart Ch. 6–7,16 — held + verified). Determines
  what the LRT section may claim about WHERE the differential bias bites. NOTE: D2 and D3 interact —
  if the differential is `o(1)` at H0, the interesting regime is local alternatives; derive D2 first
  and let D3 fall out of the same expansion.
- **CAS check** of the expansion coefficients (sympy; mirror the bivariate/4-variate machinery).
- **Small-scale paired MC spot check ONLY** (few cores, R ≤ 2000, the 4-variate non-monotone MAR
  design; templates `verification/term-ac-controlvariate-pin.R` pairing logic +
  `term-ac-higherorder-paired.R`). NOT the full sweep.

**Stage 2 — the GPT-5.5 gate (after Stage 1 is written + CAS-checked):**

- Author the Mode A (blind re-derivation) + Mode B (red-team) packet INTO todo/024, exactly the
  todo/021 template. Mode B's planted objection: "the linear terms do NOT cancel because the two
  MLEs differ at O(n^{−1/2})."
- GRADING KEY at the bottom below a `##` header (runner hard-truncates there) — never sent.
- Pre-send: dry-run extract_modes + token-scan for leakage (no order answers, no −0.22, no verdict
  words in the modes).
- Launch BACKGROUNDED:
  `py verification/run_layer3_openai.py gpt-5.5 --effort xhigh --timeout 86400 --package todo/024-w2-differential-analytic-first.md --tag -w2diff`
- Grade on return; escalation hit ⇒ STOP, reconcile, do not simulate against a disputed claim.

**Stage 3 (this session only if the audit clears in time):** the paired between-model estimator at
moderate scale, with the D2/D3 predicted orders preregistered before the run.

**Manuscript landing:** new section in `derivation.qmd` (LRT application / differential), leaving the
locked theory sections untouched. Render exit-0 + `/derivation-audit` 0 BLOCKER (3 cas-wolfram WARN
= known brace-glob false positives).

## 3. GAP-FILLER while the audit runs — W1/H1 reconciliation (todo/022 item A)

Empirical, governed by the LOCKED theory ⇒ no gate. The preregistered sweep records **H1 = FAIL** on
the monotone-vs-non-monotone diff criterion (`cache/run_all-prod/phase5/verdicts.md`;
`That/½tr ≈ 0.55/0.32/0.16/0.37` across N, `passT=FALSE` at N=1000, `phase1-w1/summary.csv`), while
the clean `+½` comes from the controlled run (ratio 0.985). Either (i) re-run W1 at higher R / more N
to pin the trend in the estimated-Σ MAR regime (phase 1 only, FEW cores), or (ii) amend the
preregistration criterion with documented rationale, and/or (iii) surface the tension in the
manuscript. Do NOT lean on the controlled run alone.

## 4. Literature state (stocked 2026-06-04 — nothing blocks)

- D1–D3 needs fully covered by holdings: van der Vaart (contiguity/LAN/noncentral χ²; M-estimator
  linearization), Wilks 1938, Chan ×2 + Meng–Rubin, Meng 1994, Rubin 1987, Schafer, Reiter 2007,
  Pawitan, Shimodaira ×2, Konishi–Kitagawa, Cavanaugh–Shumway, Claeskens–Consentino, Hens–Aerts.
- Four NEW acquisitions, lit-synced, **acquired but NOT yet verified** (in-session read + claim
  check required before any `@cite`):
  - `vuongLikelihoodRatioTests1989` — the one that matters: anchors the non-nested clause IF the
    LRT section keeps "non-zero under non-nested comparison" (CLAUDE.md core contribution). Decide
    the wording, then read+cite or drop.
  - `barnardMiscellaneaSmallsampleDegrees1999` — optional small-sample-df add-on (D2).
  - `selfAsymptoticPropertiesMaximum1987` — boundary nesting; likely never cited (out of scope).
  - `camAsymptoticMethodsStatistical1986` — Le Cam primary; default routing stays cite-via-vdV.
    ⚠️ 2.47M chars (whole book) — read targeted chapters only, NEVER the full file. Citekey
    surname is "Cam", not "lecam".
- Backlog/audit details: `todo/003` "Citation-coverage audit" section (2026-06-03/04).

## 5. Guardrails (carried)

- Heavy parallel R segfaults under contention ⇒ FEW cores for targeted runs.
- em_mvn unreliable for non-monotone ⇒ lavaan FIML or da.norm.
- `(A)+(C)`-type statistics are heavy-tailed (sd ∝ √n) ⇒ paired/control-variate estimators only.
- Citation discipline: `@cite` ⇒ `literature/<key>.md` read in-session (hook enforces; `@TODO:<slug>`
  is the drafting bypass).
- R style per `~/.claude/CLAUDE.md` (`=` for scalars, no `L` suffix, braces + explicit return, etc.).

## 6. FINISH line

- D1–D3 derived (two ways where feasible) + CAS-verified, landed in derivation.qmd.
- GPT-5.5 packet authored, leakage-scanned, launched; graded if returned (escalation ⇒ reconcile).
- H1 reconciled (re-run or amended criterion w/ rationale).
- Render exit-0; `/derivation-audit` 0 BLOCKER.
- Commit(s) on main with the Co-Authored-By trailer; update todo/024 (grading outcome), todo/000,
  and memory (D2/D3 verdicts; H1 disposition).

*Handoff 2026-06-04. Theory locked; literature stocked; this session turns the W2 differential from
conjecture into derived + audited evidence.*
