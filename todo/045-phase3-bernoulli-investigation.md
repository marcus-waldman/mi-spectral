# Todo 045 — REGISTRATION + PLAN: why the Phase-3 Bernoulli check HARKed, and why the numbers look the way they do

**Status:** REGISTERED 2026-07-03, **before any new code**. Written at the end of the session that
ran the Phase-3 non-normal illustration (todo/040 §9-10), then ran it through an adversarial
`tkal-in-ket` quorum (Gemini + Claude-Opus peers) after Marcus flagged the write-up as
HARKing-shaped. Determination: **AMENDED** — the position survives only via substantial
concessions, and one objection (OBJ-08) is sustained, not resolved. Full record:
`tkal-reviews/quorum-phase3-bernoulli-20260703/DETERMINATION.md`.

Marcus's direction closing that session: stop rewriting the manuscript-facing text for now. The
next session is a **full investigation** into two linked but distinct questions — (1) *why* the
registration process produced a post-hoc-corrected target instead of a pre-registered correct one
(a process failure), and (2) *why* the measured numbers look the way they do (a substantive
open question the process failure left unresolved). Both need real answers before any
manuscript text is finalized. This file is doc-before-code for that investigation — no simulation
runs until the plan below is reviewed.

---

## 0. What actually happened (compressed; full detail in todo/040 §9-10 and the quorum record)

- Todo/040 §9 registered Bernoulli as the "scale-free" exemplar, predicting it would hit the
  known-scale collapse (~0 FITTED, ~-0.5 for a genuine Bayesian draw), on the reasoning "no
  explicit dispersion parameter -> known-scale case." This reasoning was a **heuristic analogy**,
  not a derivation from the theorem's own stated condition.
- Measured (R=1000, M=50): Bernoulli FITTED = +0.853 (se 0.161), ~5.3 se from the registered ~0.
  mice-draw = +0.628 (se 0.161), ~7 se from the registered -0.5, wrong sign.
- After the miss, a post-hoc calculation showed Bernoulli's binary entropy has
  $dH/dp = -\operatorname{logit}(p) \neq 0$ generically, so Bernoulli does not satisfy the
  theorem's own known-scale condition (entropy must be parameter-free) at all. The write-up then
  re-scored Bernoulli against the GENERAL case's +0.5 target instead.
- Marcus flagged this as HARKing (hypothesizing after results are known): the *only* reason the
  general-case target was computed was that the known-scale target had already failed.
- The quorum (Gemini lead + Claude-Opus, `preset: max` minus the open-weights peer, 3 rounds)
  determined **AMENDED**. Two objections were **conceded outright**, not just amended:
  - **OBJ-05** (blocking): the same advocate, holding the same two inputs (the theorem's condition
    + Bernoulli's entropy formula) reached opposite conclusions before vs. after seeing data. No
    blinded, timestamped, independent re-derivation exists to rule out the miss having driven the
    "correction." Conceded as a permanent limitation of this specific instance, not resolvable by
    better wording.
  - **OBJ-07** (major): the 2.2 se gap between the measured +0.853 and the corrected +0.5 target is
    **unattributed** — no named finite-sample or higher-order term, no N-scaling check. Conceded
    that "same sign, same ballpark" was doing the work of a confirmation claim with no evidence
    behind it.
  - **OBJ-08** (major, **sustained**, not resolved): whether Gamma+Bernoulli (both now testing the
    general case after the correction) is *sufficient* to answer r3#2, given the known-scale
    collapse remains verified only in the multivariate normal family and r3#2 arguably asks about
    "the current findings" broadly. The advocate's textual rebuttal (the antecedent of "current
    findings" is the two quantities r3#2 names a few words earlier — trace penalty,
    design-imbalance terms — not the unmentioned known-scale collapse) was accepted as
    *defensible*, not *decisive*. This is now Marcus's call, informed by whatever this
    investigation finds.

---

## 1. Two questions, kept explicitly separate

**Q1 (process): why did the registration produce the wrong target instead of the right one, given
the right one was reachable by elementary calculus the whole time?**

**Q2 (substance): now that Bernoulli is known to test the general case, what is the *actual*
leading-order target for a one-parameter, logit-link GLM, and does +0.853 confirm it, refute it,
or land somewhere the theorem doesn't yet speak to?**

Q1 without Q2 risks becoming a self-flagellation exercise that fixes process but leaves the number
unexplained. Q2 without Q1 risks silently re-deriving a target that happens to fit +0.853 and
repeating the exact failure mode just adjudicated. Both are required. Do Q1 first (cheap, no code)
because its answer shapes how Q2 must be run (e.g., if Q1 finds the registration skipped a
derivation step that should be mandatory, Q2's re-derivation must be done and timestamped BEFORE
looking at any new numbers, to actually satisfy OBJ-05's "what would satisfy").

---

## 2. Q1 — process retrospective (no code; a reading-and-writing task)

- **2a. Reconstruct exactly what reasoning step was skipped.** Todo/040 §9's registration text
  should be read literally, alongside `derivation.qmd`'s known-scale scope callout (:792-827,
  quoted in the quorum background). Confirm precisely: was the entropy-gradient condition
  ($\alpha = -\mathcal{E}'$, entropy parameter-free) ever written down for Bernoulli specifically,
  or only pattern-matched against "no dispersion parameter"? (Expected finding, to confirm rather
  than assume: pattern-matched, not derived — this is what the quorum record already shows, but it
  should be confirmed against the actual todo/040 §9 text rather than asserted from memory.)
- **2b. Check whether the SAME shortcut affected the Gamma choice.** Gamma was assumed to be
  "estimated-scale" because it has a separate shape parameter, by analogy to MVN's
  $(\mu,\Sigma)$ — was this ALSO an analogy rather than an explicit check that
  $dH_{\text{Gamma}}/d\theta \neq 0$? (It happens to be correct — Gamma's entropy does depend on
  scale, shown inline in todo/040 §10 — but if the reasoning that reached it was equally
  underivied at registration time, that is a second instance of the same process gap, not a
  one-off Bernoulli mistake, and changes the process fix from "watch for tricky one-parameter
  families" to "always derive $\alpha$ explicitly for every family, full stop.")
- **2c. Root-cause the skip.** Candidate causes to check against the actual session transcript /
  timeline, not assume: time pressure to move from "scope approved" to "code running" same
  session; the registration doc's own template not prompting for an explicit entropy-gradient
  derivation step; the "no dispersion parameter" heuristic being *usually* a fine proxy for
  low-dimensional standard families and this being the first time it broke.
- **2d. Write the process fix.** A concrete, checkable addition to the registration discipline
  (todo/040's own doc-before-code norm, and possibly a CLAUDE.md addition): for any family entering
  a registration doc for the first time, the entropy-gradient condition must be **derived inline,
  shown in the registration text, and dated**, before any pass criterion naming a target value is
  written. This is cheap (a few lines of calculus per family) and directly closes the OBJ-05 gap
  for any *future* instance, even though it cannot retroactively fix this one.

## 3. Q2 — substantive re-derivation and, if warranted, new code

**3a. Derive (not assume) whether R1-R7 hold for a Bernoulli/logit-link GLM with response-only MCAR
missingness.** Go through each condition in `derivation.qmd` (R1 smoothness, R2 positive-definite
information, R3 ignorability, R4-R6 congeniality/properness/self-efficiency, R7 infinite-imputation
idealization) and check it explicitly for this family, rather than assuming "regular parametric
model, should be fine." This is the single check OBJ-06 says is missing and OBJ-02 says the +0.5
claim "smuggles in." **If this derivation is genuinely new** (not just confirming existing
conditions transfer trivially), it goes through the project's cross-model derivation protocol
(`feedback_crossmodel_derivation_protocol`: GPT-5.5 at xhigh effort, backgrounded, 24h timeout)
before being treated as settled, matching how the DA-engine master formula was cross-checked.

**3b. If R1-R7 hold with the SAME leading constant, find out why +0.853 doesn't land near +0.5.**
Candidate explanations to check, in order of cost:
  - **Finite-N / higher-order term.** Rerun the Bernoulli FITTED arm (no brms needed, this is the
    cheap mice-only side) at $N \in \{200, 500, 1000, 2000\}$, same design as the paper's own W1
    N-scan and the DA-engine's Amelia-vs-Bayesian-draw N-scan. If the ratio moves toward $+0.5$ as
    $N$ grows, that is direct evidence of an $O(1/N)$ finite-sample term the leading-order theorem
    doesn't capture at $N=200$ — report the rate, don't just eyeball convergence. If it stays fixed
    near $+0.85$ across $N$, that is evidence the true asymptote for this family is NOT $+0.5$, a
    materially different and more important finding.
  - **A discreteness correction to the analytic FIML anchor.** The anchor construction (observed
    rows contribute actual log-density, missing rows contribute the model's own entropy) was
    validated against brute-force Monte Carlo for the ENTROPY FORMULA alone (to $10^{-4}$), but
    that validation did not check whether combining it with the REST of the theorem's leading-order
    expansion (the Taylor expansion in $(\tilde\phi - \theta_0)$ underlying `S4-P7`) introduces an
    extra term specific to discrete outcomes that a continuous family like Gaussian or Gamma
    doesn't have. Check this by hand or with a CAS (sympy/Mathematica) on the univariate Bernoulli
    case, analogous to `verification/cas-wolfram/verify_engine_gap_sympy.py`'s toy-table approach.
  - **mice's `logreg` approximation quality.** `mice`'s proper-imputation methods for discrete
    outcomes are approximate-Bayesian (a weighted-bootstrap-like construction for the coefficient
    draw), not exact MCMC. Check whether the specific approximation `logreg` uses could itself be
    the source of part of the +0.628 anomaly, independent of the general mechanism — e.g. by
    comparing against a `brms`/Stan-based genuine posterior draw for a CONTINUOUS relaxation of
    the same design (a probit link with a latent continuous representation, which brms CAN fit via
    `mi()`, unlike raw Bernoulli) as a cross-check engine.

**3c. Resolve OBJ-08 with evidence, not just a reading of the reviewer's sentence.** Decide,
informed by 3a/3b's findings, whether the response to r3#2 needs a genuine two-parameter,
fixed-scale, non-normal exemplar (Student-t or Laplace location model with scale and df held
fixed) to directly test the known-scale collapse outside MVN — the thing the quorum could not
settle and left for Marcus. If Q2 turns up something that makes the general-case story for GLMs
shakier than currently written (e.g., R1-R7 genuinely fail, or the N-scan shows a different
asymptote), that independently strengthens the case for also running the known-scale exemplar,
since it would mean NEITHER regime currently has solid non-normal support.

---

## 4. What this investigation does NOT do (scope discipline)

- Does not touch the frozen preregistered originals (W1/W2/W3 @ SHA ddc9037).
- Does not rewrite `manuscript/reviews/v1/response/response-letter.md`'s r3#2 entry, the G9
  Discussion paragraph, or `decisions.md` D-24 until Q1 and Q2 produce real findings — those files
  currently reflect the PRE-quorum framing and are known to be too strong; they are flagged stale,
  not deleted, pending this investigation's outcome.
- Does not treat the quorum's "amended, sustained OBJ-08" as license to just add more hedge words
  to the existing text. Either the investigation resolves what the numbers mean (and the text gets
  rewritten once, correctly) or it concludes the Bernoulli check cannot be salvaged and should be
  dropped from the manuscript response entirely in favor of a properly pre-registered known-scale
  exemplar (Student-t/Laplace) run cleanly from scratch, with the entropy-gradient condition
  derived and dated BEFORE any code, per the Q1 process fix.

## 5. Entry point for next session

Start with Q1 (§2), which is pure reading/writing, no code, and should take well under an hour.
Its findings determine how rigorously Q2's re-derivation (§3a) must be timestamped/documented
before Q2's code (§3b) runs. Do not skip straight to reruns.
