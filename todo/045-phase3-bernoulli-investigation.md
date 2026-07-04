# Todo 045 — REGISTRATION + PLAN: why the Phase-3 Bernoulli check HARKed, and why the numbers look the way they do

**Status:** Q1 CLOSED 2026-07-03 (same session, continued); Q2 OPEN, no code yet. Written at the
end of the session that ran the Phase-3 non-normal illustration (todo/040 §9-10), then ran it
through an adversarial `tkal-in-ket` quorum (Gemini + Claude-Opus peers) after Marcus flagged the
write-up as HARKing-shaped. Determination: **AMENDED** — the position survives only via substantial
concessions, and one objection (OBJ-08) is sustained, not resolved. Full record:
`tkal-reviews/quorum-phase3-bernoulli-20260703/DETERMINATION.md`. **Q1's findings are in §2 below**
("Q1 FINDINGS," dated 2026-07-03): the registration explicitly declined to derive anything for
Bernoulli ("no new derivation needed," quoted verbatim from §9), the same description-only pattern
was used for Gamma, and Gamma landed correctly because it is a genuine structural analogy
(a real second parameter, like MVN's $\Sigma$) while Bernoulli's was a category error (no such
parameter exists to map at all). Q2 (§3) is unstarted.

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

### Q1 FINDINGS (executed 2026-07-03, dated amendment — resolves Q1)

**2a — confirmed against the actual text, not memory.** `todo/040` §9 states, verbatim: *"The
theorem's known-scale scope callout (`derivation.qmd` :792–827) already gives the two-regime
prediction with **no new derivation needed**"* (§9, "What this illustrates," first sentence). This
is a direct textual admission, not an inference — the registration explicitly declined to derive
anything for the new instance, treating the EXISTENCE of the general known-scale/estimated-scale
split (proven for MVN) as sufficient license to classify a brand-new family without checking the
split's own antecedent condition against that family. The classification itself is asserted purely
descriptively: *"a model with a known scale (dispersion fixed by the mean–variance relationship, as
in Bernoulli/Poisson GLMs) collapses to..."* (§9) and, in the Design section, *"Bernoulli (logit
link — the scale-free/known-scale exemplar, dispersion fixed at 1 by the family)"*. Neither passage
writes down Bernoulli's entropy $H(p)=-[p\log p+(1-p)\log(1-p)]$ or computes $dH/dp$. The entropy
formula and its derivative appear for the first time in §10, **after** the miss — confirming the
quorum's OBJ-05 finding directly from the primary text: the derivation genuinely did not exist
before the data.

**2b — the same shortcut was used for Gamma, but it is a structurally sound analogy, not merely a
lucky one.** Gamma's classification is equally description-only in §9: *"Gamma (log link, shape
estimated — the estimated-scale exemplar)"* and, in §10 (written after the run), *"a model with an
estimated dispersion parameter (Gamma's shape, **playing the role $\Sigma$ plays** in the MVN
case)"* — analogy language ("playing the role"), not a derivation. Neither section computes
$dH_{\text{Gamma}}/d\beta$ or $dH_{\text{Gamma}}/d\text{shape}$ anywhere. Checked now, directly from
the entropy formula already coded in `verification/spikes/phase3-nonnormal-illustration.R:90-95`
($H_i = \text{shape}+\log(\text{scale}_i)+\log\Gamma(\text{shape})+(1-\text{shape})\psi(\text{shape})$,
$\text{scale}_i=\mu_i/\text{shape}=e^{X_i\beta}/\text{shape}$): $dH_i/d\beta = X_i \neq 0$ (entropy
depends on $\beta$ through $\log\text{scale}_i=X_i\beta-\log\text{shape}$, so its $\beta$-gradient is
exactly $X_i$, generically nonzero) and $dH_i/d\text{shape}=1-1/\text{shape}+(1-\text{shape})\psi'(\text{shape})$,
also not identically zero (both confirmed symbolically, sympy). So the Gamma classification's
*conclusion* is correct by direct calculation, not just by the empirical match — but this
calculation was done **now**, for this investigation, not at registration time either. §9/§10 never
performed it.

**However, Gamma's underlying analogy is a fundamentally different kind of claim than Bernoulli's,
and this matters for the process fix.** Gamma genuinely is a two-parameter family with an
independently-identifiable dispersion parameter (shape) that is structurally the same kind of
object MVN's $\Sigma$ is — a quantity that COULD be held fixed while only the mean/location varies,
exactly the construction the known-scale collapse requires as its point of comparison. Bernoulli has
no such second parameter *at all* — there is nothing in the family that could be held fixed while a
separate location parameter varies, because the single natural parameter fixes the entire
distribution. The registration's error for Bernoulli was not merely "skipped a check that happened
to fail" — it was a **category error**: mapping "has no parameter of this kind" onto "has this kind
of parameter, held fixed," when these are opposite conditions, not similar ones. Gamma's analogy
mapped a real structural correspondence (a genuine second parameter, estimated) onto the right
regime; Bernoulli's analogy mapped the *absence* of that structure onto the *other* regime, which
does not follow. Both were unverified when written; only one was also incoherent by construction.

**One further honest calibration, so this finding does not overcorrect in the other direction.**
Confirming $dH_{\text{Gamma}}/d\theta \neq 0$ shows Gamma is not in the known-scale case — the same
*necessary-but-not-sufficient* limit the quorum's OBJ-02/OBJ-06 already placed on the Bernoulli
side. It does not, by itself, verify that the theorem's full regularity conditions (R1-R7) hold
without modification for a Gamma GLM (as opposed to the additive-Gaussian family they were stated
and verified in). Gamma's measured FITTED value (+0.318, inside the interval around +0.5) is
evidence *for* R1-R7 transferring, but "the empirical match is good" is exactly the standard of
evidence the quorum ruled insufficient for Bernoulli's post-hoc +0.5 claim (OBJ-07). By the same
standard applied consistently, Gamma's match is suggestive, not yet a proof that R1-R7 hold — that
is Q2's job, not retroactively settled by this Q1 finding.

**2c — root cause.** Two compounding causes, both visible directly in the §9 text: (i) the
registration's own attention was allocated almost entirely to feasibility mechanics (the brms
family-restriction discovery, per-fit runtime costs, the two-engine design) — the theoretical
classification of which regime each family tests occupies two sentences out of a multi-paragraph
section, the least-scrutinized part of the document even though it is the part that determines what
the pass criteria mean. (ii) A conflation between "the general rule is proven" (true — the
known-scale collapse is a proven, MC-verified fact of this paper, for MVN) and "this new instance
satisfies the rule's antecedent" (a claim that needs its own check every time the rule is applied to
a family it was not proven for). Citing an existing, true theorem is not the same as verifying a new
case falls under it. Doc-before-code protects against moving the goalposts after seeing data; it did
not, by itself, protect against aiming at the wrong goalposts, because the registration's own
internal discipline never required showing the aim was correct before firing.

**2d — the process fix, sharpened by 2a/2b's distinction.** Before any pass criterion naming a
target value is written for a new family:
1. Write the family's exact entropy (or relevant sufficient-statistic) formula.
2. Compute its gradient with respect to **every** component of the parameter vector being
   estimated in the actual design (not a generic "the family" but the specific fitted model).
3. If classifying by analogy to an existing proven case (e.g. "this has a dispersion parameter like
   MVN's $\Sigma$"), state explicitly what structural correspondence licenses the analogy (a
   genuinely separate, independently-identifiable parameter that could be held fixed) — and treat
   the ABSENCE of that structure as its own case requiring its own argument, never as automatically
   implying the opposite regime by default.
4. Date the derivation and place it in the registration text itself, not left to be reconstructed
   afterward.
This is now applied prospectively to any Q2 work (§3) — in particular, if a genuine known-scale
exemplar (Student-t/Laplace, fixed scale) is registered, its entropy-gradient condition must be
derived inline in that registration, not asserted by analogy, before any code runs.

**Q1 is closed.** Both parts of the question are now answered directly from the primary text: the
registration explicitly declined to derive anything ("no new derivation needed"), the same
description-only pattern was used for Gamma, and the reason Gamma nonetheless landed on the correct
side is a real structural correspondence to MVN's estimated-covariance case, not luck. The process
fix above is what should have been in §9 from the start.

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

**Q1 is closed (§2, "Q1 FINDINGS").** Start with Q2 (§3): 3a first (derive whether R1-R7 hold for
a Bernoulli/logit-link GLM, cross-model-verifying if genuinely new — Q1's process fix applies here
directly: derive the condition inline, dated, before trusting any target), then 3b (the N-scan and
CAS check for the unattributed 2.2 se gap), then 3c (resolve OBJ-08 with evidence). Do not skip
straight to reruns without 3a's derivation in hand first — that is exactly the ordering Q1 found
missing the first time.
