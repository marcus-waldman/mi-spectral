# Todo 024 — W2 LRT differential: analytic derivation FIRST, then audit, then simulation

**Status:** OPEN (2026-06-03). Supersedes the "just build the paired estimator" reading of
todo/022 item C. User directive: multimodal evidence — analytic derivation + blind GPT-5.5
adversarial audit BEFORE any full-scale simulation. The simulation confirms a pre-stated analytic
claim; it does not explore.

**Scope decision context:** the paper is now bias correction + LRT (W1/W2); the W3
distributional-calibration ladder is the sequel (`todo/023`). W2 is therefore the application
centerpiece and its differential claim must be derived, not just measured.

## The claims to derive (in-house first, Claude lineage)

Setting: nested models `ψ0 ⊂ ψ` (df difference `q_d`), both fit to the SAME congenially imputed
MVN data under ignorable MAR; `d̂_L = 2[Q̄_∞(ψ̂*) − Q̄_∞(ψ̂0*)]`. From the locked theory, each
model's deviance carries `+tr(RIV_model) + 2(A+C)_model + O(1/n)`.

- **D1 (differential structure — mostly assembled, make rigorous).**
  `Bias[d̂_L] = [tr RIV_ψ − tr RIV_ψ0] + 2[(A+C)_ψ − (A+C)_ψ0] + O(1/n)`, with both differentials
  `O(1)`. Establish precisely what "the same imputed data" buys: which realized quantities are
  common to the two fits.

- **D2 (conditioning — the load-bearing NEW claim).** The per-dataset statistic for the LEVEL,
  `ac_i = A_rb,i − tr_obs,i`, has sd `≍ c√n` (heavy right tail) — established in todo/020/021. The
  per-dataset PAIRED DIFFERENTIAL `ac_i(ψ) − ac_i(ψ0)` (same dataset, same imputations, nested
  fits) has sd of strictly lower order. Derive the order. Mechanism to formalize: the `O(√n)`
  linear noise term `α^⊤δ` is driven by the common realized data through the shared sufficient
  statistics; for nested fits the two linear terms agree on the shared parameter subspace, so the
  difference retains only the `q_d`-dimensional complement — kill the `O(√n)` component, leaving
  `O(1)` sd (conjectured; DERIVE, do not assume). This is the analytic content behind the
  manuscript's "structurally better-conditioned" clause and the design basis for the paired
  estimator (mirror of `term-ac-controlvariate-pin.R` / `term-ac-higherorder-paired.R`).

- **D3 (value at H0 and under local alternatives).** Show the `(A)+(C)` differential is 0 at H0 to
  leading order (both differentials vanish when the extra parameters are null and carry no
  missing-information differential), and derive its leading-order magnitude under local
  alternatives `ψ = ψ0 + n^{-1/2}·h` — in particular whether it is `O(1)` (matters for power) or
  `o(1)` (the tr(RIV) differential dominates). This determines what §4 may claim about WHERE the
  differential bias bites.

**Verification per claim (multimodal):** (i) derivation written two independent ways where
feasible (the WAY-1/WAY-2 discipline of todo/020); (ii) CAS check of the expansion coefficients
(sympy, mirroring the bivariate/4-variate machinery); (iii) SMALL-scale paired MC spot check
(few cores, R ≤ 2000, the existing 4-variate non-monotone MAR design) — NOT the full sweep.

## Stage 2 — blind GPT-5.5 adversarial audit (the gate)

After the in-house derivation is written and CAS-checked, author the layer-3 packet in this file
(below a `## MODE A` header, exactly the todo/019/021 template):

- **Mode A (blind):** self-contained problem — derive the order of the per-dataset paired
  differential's sd and the H0/local-alternative behavior of the differential, from scratch. No
  hint of our answer.
- **Mode B (red-team):** our claim + lemma sheet + the heavy-tail empirical facts; attack the
  cancellation argument (e.g. "the linear terms do NOT agree on the shared subspace because the
  two MLEs differ at O(n^{-1/2})").
- **GRADING KEY at bottom** — hard-strip before sending; runner truncates at the `##` header.
- Pre-send: dry-run `extract_modes` + token-scan for leakage (no `-0.22`, no verdict words, no
  order answers in the modes).
- Launch BACKGROUNDED:
  `py verification/run_layer3_openai.py gpt-5.5 --effort xhigh --timeout 86400 --package todo/024-w2-differential-analytic-first.md --tag -w2diff`

**While the audit runs (~hours, 24h timeout):** proceed with todo/022 item A (W1/H1
reconciliation — empirical, governed by the LOCKED theory, no new analytic claim, no gate).

## Stage 3 — paired simulation (only after the audit returns)

- Escalation NOT hit ⇒ build the paired between-model estimator (template:
  `term-ac-controlvariate-pin.R` pairing logic, across nested models on shared imputations),
  prereg the predicted orders from D2/D3, run at moderate scale, then upgrade §4's
  "structurally better-conditioned" to a derived + audited + measured claim.
- Escalation HIT ⇒ stop, reconcile, re-derive; do NOT run the sweep against a disputed claim.

## Guardrails (carried)

- Few-core targeted runs; heavy-tailed statistics ⇒ paired/control-variate only.
- Do NOT re-open the locked level results (headline, (A)+(C) value not-pinned, −0.22 anchor).
- Touch manuscript ⇒ render exit-0 + /derivation-audit 0 BLOCKER.

*Opened 2026-06-03; the analytic-first sequencing is a user directive for this session.*
