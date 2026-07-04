# Todo 045 — REGISTRATION + PLAN: why the Phase-3 Bernoulli check HARKed, and why the numbers look the way they do

**Status:** Q1 CLOSED 2026-07-03 (same session, continued); Q2 3a DERIVED + CAS-VERIFIED
2026-07-04 (§3.1 below; cross-model gate launched same day), 3b/3c REGISTERED 2026-07-04 (§3.2,
§3.3 below) with all targets derived and dated before the production scans ran. Written at the
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

### §3.1 Q2 3a FINDINGS — the derivation (dated 2026-07-04; CAS-verified; gate pending)

**Information state, disclosed first (OBJ-05 hygiene).** When this derivation was written, the
N=200 phase-3 cache (`verification/cache/phase3-nonnormal-prod.rds`, run 2026-07-03) was already
known: mean $T_{\text{fitted}} = +0.4772$ (se $0.0910$; ratio $+0.846\pm0.161$ against the
analytic $\operatorname{tr}(\mathrm{RIV})=2\cdot0.22/0.78=0.5641$), mice-draw ratio $+0.623$,
paired $\mathbb{E}[T_{\text{draw}}-T_{\text{fitted}}] = -0.1259$ (se $0.0122$; ratio
$-0.2232\pm0.0216$), sample $\operatorname{tr}(\mathrm{RIV})$ mean $0.5594$ (within $0.8\%$ of
analytic — the denominator is NOT the anomaly). What did NOT exist when the derivation was
written: any $N>200$ Bernoulli value, any Poisson simulation in this repo, any Student-t
simulation, the intercept-only and two-point exact enumeration curves. Those are this
derivation's out-of-sample tests, registered in §3.2/§3.3 below **before** running. An
independent blind re-derivation (GPT-5.5 Pro, xhigh, Mode A of `todo/045b-gpt55-gate-package.md`)
was launched the same day from the setup alone, with no access to this section or to any number
above — the blinded, timestamped, independent re-derivation OBJ-05 said was missing for the
original post-hoc correction is thereby supplied for THIS claim (it cannot retroactively repair
the Phase-3 registration, which stays reported as a miss).

**Setup.** One-parameter exponential-family response
$f(y\mid x;\beta)=h(y)\exp\{y\eta - A(\eta)\}$, canonical link $\eta = x^\top\beta$,
$\beta\in\mathbb{R}^q$; $X$ fully observed, $Y$ MCAR at rate $r$ (response-only missingness, so
$\ell_{\text{mis}\mid\text{obs}}=\sum_{i\in\text{mis}}\log f(y_i\mid x_i;\theta)$ and
$\hat\theta_{\text{obs}}$ is the complete-case MLE). Write $w=A''$ (the information weight),
$A'''$ (the third cumulant), $g(\eta)=\mathbb{E}_\eta[\log h(Y)]$ (the base-measure mean),
$J_\bullet=\sum_\bullet w_i x_i x_i^\top$, $\Omega=\mathbb{E}[wXX^\top]$,
$Q_i = x_i^\top J_{\text{obs}}^{-1} x_i$. The FITTED arm's analytic anchor (missing rows
contribute $-H_i(\hat\theta_{\text{obs}})$) is EXACTLY the $M\to\infty$ FITTED $\bar Q_\infty$
for any family, because $\mathbb{E}_{\tilde Y\sim f(\cdot;\theta)}[\log f(\tilde Y;\theta)]
= -H(\theta)$ — so the anchor-vs-draws distinction is not a gap for this arm.

**Step 1 — the paper's own theorem structure transfers.** The A/B split and the A3 expansion
(`derivation.qmd` @sec-termA) are family-generic under R1–R2: Term B $=-\tfrac12\operatorname{tr}(\mathrm{RIV})+O(1/N)$
(second-order expansion of $\ell_{\text{com}}$ + L1–L3, no MVN input), and Term A
$=\operatorname{tr}(\mathrm{RIV})+[(A)+(C)]+O(1/N)$ with the A4 objects instantiated for the GLM:
$$ (A)=\alpha^\top\mathbb{E}[\delta],\quad \alpha=\sum_{i\in\text{mis}}\big(g'_i+\eta_i w_i\big)x_i,\qquad
   (C)=\tfrac12\operatorname{tr}\big(\mathcal H_\phi J_{\text{obs}}^{-1}\big),\quad
   \mathcal H_\phi=\sum_{i\in\text{mis}}\big(g''_i+\eta_i A'''_i\big)x_i x_i^\top. $$
(Derivation of $\alpha,\mathcal H_\phi$: the cross-entropy per missing unit is
$f_{0,i}(\phi)=g(\eta_i(\phi))+A'(\eta_i(\phi))\,\eta_{0,i}-A(\eta_{0,i})$; differentiate twice
in $\phi$ at $\theta_0$.) What R1–R7 do NOT supply is the A4 cancellation "$(A)+(C)=O(n^{-1})$
under MCAR" for this family: the paper derives that step for the multivariate normal (where
$\alpha$ is covariance-only) and checks it closed-form for scalar no-covariate families
($N(\mu,\sigma^2)$ exact, $\mathrm{Exp}(\lambda)$ $O(1/n)$). For a covariate GLM, whose $\alpha$
has support on ALL of $\beta$, the step needed its own proof. That is precisely the gap OBJ-06
named. The proof follows.

**Step 2 — the MLE-bias input (Cox–Snell for a canonical link), derived inline.** For canonical
links the observed information is deterministic given the design and
$\operatorname{Var}(U_{\text{obs}})=J_{\text{obs}}$, so expanding the score equation
$0=U(\hat\beta)$ to second order gives
$\delta = J_{\text{obs}}^{-1}U - \tfrac12 J_{\text{obs}}^{-1}\sum_{j\in\text{obs}}A'''_j x_j (x_j^\top\delta)^2+\dots$,
hence
$$ b := \mathbb{E}[\hat\beta_{\text{obs}}-\beta_0]
   = -\tfrac12\,J_{\text{obs}}^{-1}\sum_{j\in\text{obs}}A'''_j\,\big(x_j^\top J_{\text{obs}}^{-1}x_j\big)\,x_j
   \;+\;O(N^{-2}). $$
Verified two independent ways in `verification/cas-wolfram/verify_bernoulli_fitted_gap.py`:
symbolically it reduces on the intercept-only design to the delta-method value
$\mathbb{E}[\operatorname{logit}\bar y]-\eta = \sinh(\eta)/n + O(n^{-2})$ (check [3]), and on a
two-point covariate design it matches the EXACT enumerated $\mathbb{E}[\hat\beta]$ (check [5];
agreement 2% at $n_g=240$ and converging).

**Step 3 — Lemma P (the projection cancellation; the new step).** Substituting $b$ into $(A)$
and passing to the population design ($J_{\text{obs}}\to(1-r)N\Omega$,
$\sum_{\text{mis}}\to rN\,\mathbb{E}[\cdot]$ under MCAR), the two $O(1)$ pieces built from the
CANONICAL-STRUCTURE parts of $\alpha,\mathcal H_\phi$ are
$$ (A)_{\eta w} = -\tfrac{r}{2(1-r)}\,\mathbb{E}[\eta w X^\top]\,\Omega^{-1}\,
   \mathbb{E}\big[A'''(X^\top\Omega^{-1}X)X\big],\qquad
   (C)_{\eta A'''} = +\tfrac{r}{2(1-r)}\,\mathbb{E}\big[\eta A'''(X^\top\Omega^{-1}X)\big], $$
and these cancel EXACTLY, for every design distribution and every canonical family, because
$\eta=X^\top\beta_0$ is linear in $X$ and $\Omega=\mathbb{E}[wXX^\top]$ uses the same weight
$w$: $\mathbb{E}[\eta wX^\top]=\beta_0^\top\Omega$, so
$$ \mathbb{E}[\eta wX^\top]\Omega^{-1}\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]
   = \beta_0^\top\,\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]
   = \mathbb{E}[\eta A'''(X^\top\Omega^{-1}X)]. \tag{Lemma P} $$
Verified symbolically on a free-symbol 3-point design, on 12 exact-rational 4-point designs,
and numerically on both quadrature designs (checks [2], [6], [7]). What survives is only the
base-measure part:
$$ (A)+(C) = \Delta_h + O(1/N),\qquad
   \Delta_h = \tfrac{r}{1-r}\Big[-\tfrac12\,\mathbb{E}[g'X^\top]\,\Omega^{-1}\,
   \mathbb{E}[A'''(X^\top\Omega^{-1}X)X] + \tfrac12\,\mathbb{E}[g''\,X^\top\Omega^{-1}X]\Big], $$
which does NOT cancel by Lemma P because $g'(\eta)$ is not linear in $X$.

**Theorem (canonical-GLM FITTED gap, response-only MCAR).** Under R1–R7,
$$ \mathbb{E}[T_{\text{fitted}}] = +\tfrac12\operatorname{tr}(\mathrm{RIV}) + \Delta_h + O(1/N). $$
- **Bernoulli (logit): $h\equiv1$, so $g\equiv0$, $\Delta_h=0$** — the FITTED asymptote is the
  paper's general-case $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ EXACTLY. The $+0.5$ target is
  derivable after all; what the Phase-3 registration lacked was this lemma, not just the entropy
  gradient. (Same conclusion for any unit-base-measure canonical GLM: geometric, exponential.)
- **Poisson (log): $h=1/y!$**, $g(\eta)=-\mathbb{E}_\mu[\log Y!]$, $\Delta_h\neq0$. Quadrature at
  the registered design below gives $\Delta_h/\operatorname{tr}(\mathrm{RIV})=-0.3961$, i.e. a
  FITTED asymptote of $+0.1039$ — far from both $+0.5$ and $0$. Registered as a BLIND
  out-of-family test (§3.2) before any Poisson simulation existed in this repo.
- **Proper-draw corollary.** A second-moment-proper draw $\tilde\phi$ centered at
  $\hat\theta_{\text{obs}}$ leaves $(A)$ and the Term-A main piece unchanged and doubles the
  variance entering $(C)$, so
  $\mathbb{E}[T_{\text{draw}}-T_{\text{fitted}}] = (C) = \tfrac{r}{2(1-r)}\mathbb{E}[(g''+\eta A''')(X^\top\Omega^{-1}X)]+O(1/N)$.
  For the phase-3 Bernoulli design: $K/(2q)$ with
  $K=\mathbb{E}[\eta A'''X^\top\Omega^{-1}X]=-1.0424$, i.e. $\mathbf{-0.2606}$, constant in $N$.
  The already-measured paired value $-0.2232\pm0.0216$ (which predates this formula) sits within
  $1.7$ se. This is also the GLM analog of the DA-engine posterior-draw discount (D-22): the
  Bayesian-draw arm is BELOW FITTED by an $O(\operatorname{tr}(\mathrm{RIV}))$ amount with an
  explicit family constant — the mice-draw's registered $-0.5$ target was wrong for two separate
  reasons (Bernoulli is not known-scale, and the discount is $(C)$, not $-\tfrac12\operatorname{tr}(\mathrm{RIV})$).
- **Known-scale location family (fixed scale and shape).** $H$ is location-free, $\alpha=0$,
  $\mathcal H_\phi$'s entropy part vanishes, and the paper's known-scale collapse applies:
  FITTED $\to 0$, proper draw $\to -\tfrac12\operatorname{tr}(\mathrm{RIV})$ — the §3.3 exemplar.

**R1–R7 walk-through for Bernoulli/logit (the OBJ-06 checklist).** R1: smooth full exponential
family, differentiable in quadratic mean, differentiation under the integral licensed; the MLE
exists only off the separation event, whose probability is exponentially small at this design
($T$ itself stays finite even there, since the anchor and $\ell$ terms are bounded by 0). R2:
$I_{\text{com}}=\mathbb{E}[wXX^\top]\cdot N\succ0$ for a nondegenerate design;
$I_{\text{obs}}=(1-r)I_{\text{com}}\succ0$. R3: MCAR by construction, parameters distinct. R4:
the imputation model IS the analysis model (same logistic regression) — congenial; the FITTED
arm is the theorem's deterministic-FIML branch. R5: needed only for the draw arm; mice `logreg`
draws $\beta^\ast\sim N(\hat\beta,\hat V)$ — second-moment proper to leading order. R6: the
complete-case MLE is the observed-data MLE under MCAR; self-efficiency holds for regular MLEs.
R7: the FITTED anchor is exact-$M{=}\infty$ by construction; the draw arm uses $M=50$ with
Rubin's $(1+1/M)$ in the sample RIV. Conclusion: R1–R7 hold; the additional input the $+0.5$
value needs is the A4 MCAR-cancellation for this family, which Lemma P now supplies.

**What this derivation does NOT establish** (fences, stated before the scans): (i) the finite-$N$
constant in the $O(1/N)$ remainder for the Gaussian-$x$ design — the exact enumerations give
small constants for the homogeneous and two-point designs ($\approx0.6/n$ and $\approx1.6/n$ on
the ratio scale), but the heterogeneous-design constant is MEASURED by the N-scan, not derived;
whether the observed $+0.846$ at $N=200$ is mostly that finite-$N$ term or mostly Monte-Carlo
noise (se $0.161$) is exactly what §3.2 P1 answers. (ii) Non-canonical links (the Gamma log-link
arm stays a directional check; its $\Delta$-analog has extra terms this lemma does not cover).
(iii) General missingness patterns — response-only only. (iv) The lemma is asymptotic; nothing
here claims exactness at $N=200$.

**Verification record.** `verification/cas-wolfram/verify_bernoulli_fitted_gap.py` — 15 checks,
all pass (2026-07-04): entropy identities; Lemma P symbolic + 12 exact-rational designs + 2
numeric designs; Cox–Snell = delta-method (intercept-only, closed form $\sinh(\eta)/n$);
intercept-only exact enumeration ratio$(n)\to\tfrac12$ with $(ratio-\tfrac12)\cdot n\to0.589$;
two-point exact enumeration (bias formula + ratio$\to\tfrac12$); the quadrature constants above;
Student-t entropy closed-form + location-free. Cross-model gate: `todo/045b-gpt55-gate-package.md`
(Mode A blind / Mode B red-team), launched backgrounded 2026-07-04.

### §3.2 Q2 3b REGISTRATION — N-scan + blind Poisson arm (dated 2026-07-04, BEFORE production)

**Script:** `verification/spikes/phase3-family-scan.R` (new; smoke mode = code validation only,
not evidence). Estimator: ratio-of-means; PRIMARY denominator = analytic MCAR
$\operatorname{tr}(\mathrm{RIV}) = q\,r/(1-r)$ ($0.5641$ Bernoulli/Poisson $q{=}2$; $0.2821$
t-exemplar $q{=}1$); realized-design and Rubin-sample denominators reported as diagnostics.
Seeds: BASE 20260704 with disjoint per-arm/per-$N$ offsets. Production sizes: Bernoulli FITTED
$R=200\text{k}/80\text{k}/40\text{k}/20\text{k}$ at $N=200/500/1000/2000$; Bernoulli draw (mice
logreg, $M{=}50$) $R=1000$ per $N$; Poisson FITTED $R=100\text{k}/30\text{k}$ at $N=200/1000$;
t-exemplar $R=20\text{k}$, $M{=}50$, $N{=}200$.

Registered predictions and pass criteria:
- **P1 (Bernoulli FITTED asymptote).** WLS fit of ratio$(N)=a+C/N$ over the four $N$: PASS if
  $\hat a$ is within $2\,\mathrm{se}(\hat a)$ of $+0.500$. $C$ is reported, not predicted.
  Falsifier: a flat ratio $\approx+0.85$ across $N$ refutes Lemma P empirically. Continuity
  check: the new script's $N{=}200$ ratio must sit within $2$ combined se of the cached
  $+0.846\pm0.161$ (same generator).
- **P2 (draw discount).** Paired $(T_{\text{draw}}-T_{\text{fitted}})/0.5641$: PASS if the
  $N{=}2000$ value is within $2$ se of $\mathbf{-0.2606}$. Trajectory across $N$ reported; no
  direction registered for the finite-$N$ drift.
- **P3 (Poisson, blind).** PASS if the $N{=}1000$ ratio is within $2$ se of $\mathbf{+0.1039}$
  (the $N{=}200$ point shows the finite-$N$ view). This family enters the repo for the first
  time with its target pre-computed; a landing near $+0.5$ or $0$ instead refutes the
  $\Delta_h$ mechanism.
- **P4 (sample RIV sanity).** mice sample $\operatorname{tr}(\mathrm{RIV})$ within $3\%$ of
  analytic at every $N$.
- **Interpretation rule, registered now:** if P1 passes, OBJ-07's residual is ATTRIBUTED — the
  $+0.846$ at $N{=}200$ decomposes into the derived $+0.5$ asymptote plus a measured $O(1/N)$
  finite-sample term (constant $C$) plus Monte-Carlo noise (se $0.161$ at $R{=}1000$); the
  honest headline for r3#2 becomes "derived $+0.5$, confirmed by an $N$-scan with a measured
  finite-$N$ correction," NOT "confirmed at $N=200$." If P1 fails flat, the Bernoulli check
  cannot be salvaged as a general-case confirmation and §4's drop-option triggers.

### §3.3 Q2 3c REGISTRATION — Student-t known-scale exemplar (dated 2026-07-04, BEFORE any code ran)

Per the Q1 process fix, the entropy-gradient condition first, inline, dated: for the location
family $f(y\mid\mu)=f_{t_\nu}\!\big(y-\mu\big)$ with $\nu=5$ and $\sigma=1$ BOTH FIXED, the
conditional missing-data entropy is $H(\mu)=H_{t_5}$, a CONSTANT in the single estimated
parameter ($dH/d\mu=0$ exactly, by translation invariance of differential entropy; closed form
and numeric check in CAS [8]). The structural correspondence licensing the classification is
stated per Q1-2d(3): this family genuinely HAS a scale-type parameter pair $(\sigma,\nu)$ that is
HELD FIXED while the location is estimated — the construction the known-scale collapse requires,
which Bernoulli lacks. Student-t is chosen over Laplace because the expansions use third
derivatives of the log-density (R1-adjacent smoothness), which Laplace's kink at zero does not
supply. Design: $N=200$, MCAR $0.22$, $\mu_0=0.3$; MLE by 1-D optimization; proper draw
$\mu^\ast\sim N(\hat\mu_{\text{obs}},\,1/(n_{\text{obs}}I_1))$ with $I_1=(\nu+1)/(\nu+3)=0.75$;
imputations $\tilde Y=\mu^\ast + t_\nu$ noise; $R=20\text{k}$, $M=50$.
**Amendment (2026-07-04, pre-production, dated):** $R$ raised $20\text{k}\to200\text{k}$ after a
200-repetition smoke run (code validation) showed per-repetition ratio noise of $\approx21$, so
the registered $R$ would give se $\approx0.15$ — too wide for a sharp zero-test. Precision-only
change, direction-blind (the smoke point estimate, $+0.76\pm1.52$, is $0.5$ se from $0$ and is
disclosed here rather than used); targets, design, and seeds unchanged.
- **P5 (FITTED).** PASS if the FITTED ratio is within $2$ se of $0$.
- **P6 (proper draw).** PASS if the draw ratio is within $2$ se of $-0.500$.
P5+P6 passing supplies exactly the "genuine two-parameter fixed-scale non-normal exemplar"
OBJ-08's option (b) asked for, with both targets derived and dated before any code ran.

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
