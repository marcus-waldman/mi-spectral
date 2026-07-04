# todo/045c — STAGED rewrites of r3#2, G9, D-24/D-25, and the todo/040 §9 amendment

**Status: STAGED, NOT LANDED (2026-07-04); COMPLIANCE-VALIDATED same day.** A repo-grounded
cross-model compliance validation (Gemini 3.1 Pro via Antigravity, `todo/045d` handoff;
report: `tkal-reviews/gemini-045c-compliance-20260704/REPORT.md`) scored the staged texts
against the quorum's binding amendments: 9/10 axes HONORED, all three verification scripts
reproduced, git chronology confirmed. The one VIOLATED axis (A1: §4's todo/040 amendment put
the correction before the misses and omitted the measured values) is FIXED in place below
(reordered, exact decimals restored per the report's optional suggestion); no other text
changed. Remaining landing gate: Marcus's ratification. This file holds the complete replacement text for
the three stale artifacts flagged by the quorum (`tkal-reviews/quorum-phase3-bernoulli-20260703/`)
plus the registration-doc amendment its OBJ-01 requires. Landing is gated on (i) the GPT-5.5 Pro
cross-model verdict on the §3.1 derivation (`todo/045b`, running when this was staged) and
(ii) Marcus's ratification. Nothing below touches the repo until both clear. The quorum's binding
amendments are honored in every text: original targets and misses stated FIRST (OBJ-01/OBJ-09),
the corrected target labeled a post-hoc correction that was then independently verified rather
than an a priori prediction (OBJ-05/OBJ-11), the claim stated at derived-strength only
(OBJ-02/OBJ-06), the residual attributed with evidence (OBJ-03/OBJ-07), the scope choice named
(OBJ-04/OBJ-08), and the shrinkage check nowhere load-bearing (OBJ-10).

Evidence base: todo/045 §3.1 (derivation + CAS, commit `4aaeaae`), §3.4 (production scorecard,
commit `afa4438`), caches `verification/cache/phase3-family-scan-*-prod.rds`.

---

## 1. Response letter — full replacement of the r3#2 section body

Replace everything between the r3#2 blockquote and the `## reviewer3 — r3#3` heading in
`manuscript/reviews/v1/response/response-letter.md` (keep the heading + quote; status stays
DRAFTED) with:

---

We ran checks outside the multivariate normal family rather than leaving this as a
prediction-only paragraph — and the first round exposed an error in our own registration, which
we report first, because the corrected analysis only exists on account of that miss.

**What was registered, and what happened.** Two families were pre-registered before any code ran
(`todo/040-v1-review-response-registration.md` §9), chosen to match the reviewer's own "skewed
continuous" and "categorical" examples: Gamma (estimated dispersion) and Bernoulli, which the
registration classified as the known-scale exemplar on the reasoning "no explicit dispersion
parameter." The registered Bernoulli targets were approximately $0$ for the deterministic plug-in
and approximately $-0.5$ for the genuine posterior draw. The measured values ($R{=}1{,}000$,
$N{=}200$) were $+0.85$ (se $0.16$), about $5$ standard errors from the registered target, and
$+0.63$ (se $0.16$), about $7$ standard errors away and of the opposite sign. The family
selection was pre-registered; the theoretical target attached to it was not correct, and it was
corrected only after the miss. The error is a category error, not a computation: the known-scale
collapse requires the family's conditional missing-data entropy to be flat in the estimated
parameter, and the binary entropy is not flat ($dH/dp=-\operatorname{logit}(p)$, zero only at
$p=\tfrac12$). "Has no dispersion parameter" and "has a dispersion parameter, held fixed" are
opposite structural situations, and the registration mapped one onto the other.

**The corrected target was then derived, not asserted — and verified blind.** Because a post-hoc
correction prompted by a miss is exactly the pattern an adversarial review flagged in our own
process, the corrected analysis was rebuilt to a higher standard than the original: (i) a full
derivation of what a canonical-link GLM should show, from the paper's own Term-A objects — under
response-only MCAR the two order-one design terms (entropy-gradient $\times$ MLE-bias, and
cross-entropy curvature) cancel exactly for any canonical link, leaving the general
$+\tfrac12\operatorname{tr}(\mathrm{RIV})$ plus a base-measure term that is zero for Bernoulli
and nonzero for Poisson; (ii) a 15-check computer-algebra verification, including exact finite-$n$
enumerations that need no Monte Carlo; (iii) pre-registration of every new target in a commit
that precedes the production runs in the git history; and (iv) an independent, blinded
cross-model re-derivation requested from a different model family given only the problem setup.

**Every registered criterion the corrected theory implies then passed.** An $N$-scan of the
Bernoulli plug-in arm ($N{=}200$ to $2{,}000$, up to $R{=}200{,}000$) gives an asymptote of
$+0.512\pm0.037$ against the derived $+0.500$; its $N{=}200$ value is $+0.518\pm0.012$, which
also settles the residual the earlier run left unattributed — the $+0.85$ was Monte-Carlo noise
at $R{=}1{,}000$ around a true value near $+0.52$, not a hidden term. A Poisson model, simulated
in this project for the first time only after its target was fixed, lands at $+0.113\pm0.027$
against its derived target of $+0.104$ — a target far from both naive candidates ($+0.5$ and
$0$), because Poisson's base measure ($1/y!$) contributes a derived $-0.40$ correction that
Bernoulli's constant base measure does not have. The posterior-draw arm matches its derived
discount ($-0.31\pm0.07$ at $N{=}2{,}000$ against $-0.261$). And a Student-t location model with
scale and degrees of freedom held fixed — a genuine known-scale family outside the normal, with
both targets derived and dated before any code ran — measures $+0.02\pm0.05$ (plug-in) and
$-0.48\pm0.05$ (posterior draw) against the derived $0$ and $-0.5$, so the known-scale collapse
is no longer verified only in the multivariate normal family. In the course of this the original
Bernoulli draw value was found to carry a second defect: the original script fixed the imputation
seed across all repetitions, so its quoted standard error overstated independence
(`verification/spikes/phase3-mice-seed-diagnostic.R` reproduces the old value with the fixed
seed and the corrected one without it). All superseded numbers stay in the record; none is
load-bearing.

**The Gamma check stays a directional confirmation.** The plug-in measures $+0.32$ (se $0.20$),
inside a wide interval around the predicted one half, and the posterior draw is more negative
($-0.52$, se $0.20$), the same direction as the multivariate-normal posterior-draw result (r1#8).
Gamma's log link is not canonical, so the new lemma does not cover it, and its run shares the
fixed-seed caveat above — we therefore claim direction, not magnitude, for this family.

**Scope of what this answers.** This addresses the trace penalty and design-imbalance terms named
in the reviewer's question — the quantities the paper's applications use — now with a derived,
blind-tested GLM extension rather than only an empirical spot-check; and separately it closes the
known-scale boundary result's non-normal gap with the Student-t exemplar. The remaining
non-normal opening is stated in the manuscript (G9): non-canonical links (including Gamma's) have
no derived magnitude, and general missingness patterns beyond response-only are not covered by
the new lemma.

*Manuscript change landed:* Discussion paragraph G9 (`S6-P4d`) rewritten to the corrected,
chronology-first account; `decisions.md` D-25 records the correction (D-24 carries a superseding
pointer). *Reproducibility:* `verification/spikes/phase3-family-scan.R` (four arms) +
`phase3-family-scan-score.R` (registered-criteria scorecard) + `phase3-mice-seed-diagnostic.R`,
all with CLAUDE.md Commands entries; CAS companion
`verification/cas-wolfram/verify_bernoulli_fitted_gap.py` (15 checks); registration and results
are separate commits (`4aaeaae` then `afa4438`), so the pre-registration is checkable in the git
history, not asserted.

---

## 2. G9 (`S6-P4d`) — full replacement `draft_prose` (via a `manuscript/plan/updates/*.py` script)

New `proposition`: "G9: a first check outside the normal family exposed a registration error
(Bernoulli misclassified as known-scale by a category-error analogy), whose correction was then
derived (canonical-link GLMs hit the general $+\tfrac12$ trace value; a base-measure term moves
Poisson to $+0.104$), CAS-verified, and confirmed by pre-registered blind scans — including a
Student-t fixed-scale exemplar that verifies the known-scale collapse outside the normal family
for the first time."

New `draft_prose`:

**G9.** A first check outside the normal family exposed an error in our own registration before
it sharpened the theory, and we report it in that order. We registered a Gamma model as the
estimated-scale exemplar and a Bernoulli model as the known-scale exemplar. The registered
Bernoulli prediction for the genuine posterior draw was approximately $-0.5$ times the trace; the
measured value was $+0.63$ (se $0.16$), about seven standard errors away and of the opposite
sign, and the plug-in arm missed its registered target of approximately $0$ by about five
standard errors. The registration had treated the absence of a named dispersion parameter as the
known-scale condition, but the collapse actually requires the family's conditional missing-data
entropy to stay flat in the estimated parameter, and the binary entropy is not flat, because its
derivative is the negative logit. After the miss we derived what a canonical-link model should
show, rather than re-scoring against an assumed value. Under response-only MCAR missingness the
two order-one design terms in the theorem's proof cancel exactly for any canonical link, so the
plug-in lands on the general $+\tfrac12$ trace value plus a base-measure term. That term is zero
for Bernoulli and moves Poisson to a derived $+0.10$. Because this derivation was produced after
the miss, its predictions were pre-registered and then run blind. The Bernoulli plug-in reaches
an asymptote of $+0.51\pm0.04$ across an $N$-scan against the derived $+0.5$, and the earlier
$+0.85$ at $N{=}200$ proves to have been Monte-Carlo noise around a true $+0.52$. A Poisson
model, simulated here for the first time only after its target was fixed, lands at $+0.11\pm0.03$
against its derived $+0.10$. A Student-t location model with fixed scale, a genuine known-scale
family, measures $+0.02\pm0.05$ for the plug-in and $-0.48\pm0.05$ for the posterior draw against
the derived $0$ and $-0.5$, so the known-scale collapse now has a check outside the normal family.
The superseded Bernoulli draw value also carried a fixed imputation seed across repetitions,
which its quoted standard error did not reflect. The Gamma result stays directional
($+0.32\pm0.20$ against the predicted one half), because its log link is not canonical and the
new argument does not cover it. What G6 keeps is therefore sharper but real: membership in the
two regimes is decided by the entropy-gradient condition and, for canonical links, the base
measure — not by the family's name — and non-canonical links remain underived.

New `review.topic_sentence`: "A first check outside the normal family exposed an error in our
own registration before it sharpened the theory, and we report it in that order."
New `review.closing_sentence`: "...and non-canonical links remain underived."
New `review.flags` (append): "rewritten 2026-07-04 per the quorum amendments (todo/045 §4 →
todo/045c); chronology-first disclosure; numbers from phase3-family-scan-*-prod.rds."
New `audit.numbers` (replace the Bernoulli/Gamma entries):
- "Bernoulli draw registered -0.5, measured +0.63 (se 0.16); plug-in registered ~0, measured
  +0.85 (se 0.16)": "verif:verification/cache/phase3-nonnormal-prod.rds" (superseded originals,
  quoted as history)
- "Bernoulli plug-in asymptote +0.51+/-0.04; N=200 truth +0.52": 
  "verif:verification/cache/phase3-family-scan-bern_fitted-prod.rds"
- "Poisson +0.11+/-0.03 vs derived +0.10": 
  "verif:verification/cache/phase3-family-scan-pois_fitted-prod.rds"
- "t exemplar +0.02+/-0.05 and -0.48+/-0.05 vs 0 / -0.5": 
  "verif:verification/cache/phase3-family-scan-t_exemplar-prod.rds"
- "draw discount -0.31+/-0.07 at N=2000 vs derived -0.261": 
  "verif:verification/cache/phase3-family-scan-bern_draw-prod.rds"
- "Gamma FITTED +0.32 (se 0.20), brms draw -0.52": 
  "verif:verification/cache/phase3-nonnormal-prod.rds"

## 3. decisions.md — D-24 superseding pointer + new D-25

Append to the END of the D-24 entry (never rewrite it):

> **(Partially superseded 2026-07-04 — see D-25.)** The mechanism sentence stands, but three
> specifics are corrected by the todo/045 investigation: the "identical one-line argument applies
> to Poisson" clause is wrong as a magnitude claim (Poisson escapes the known-scale collapse but
> its non-constant base measure moves its plug-in value to a derived $+0.104$, confirmed blind at
> $+0.113\pm0.027$); the quoted Bernoulli measurements are superseded (the $+0.853$ was
> Monte-Carlo noise around a true $+0.518\pm0.012$, and the $+0.628$ draw value also carried a
> fixed `mice` seed across repetitions); and the "two-regime" framing now has a derived
> canonical-GLM theorem plus a Student-t known-scale exemplar behind it rather than a
> post-hoc re-scoring.

New decision entry:

## Canonical-GLM extension derived + blind-verified; known-scale exemplar closes the non-normal gap (2026-07-04, D-25)

The todo/045 investigation (opened after the D-24 write-up was found HARKing-shaped by Marcus and
determined AMENDED by an adversarial quorum) resolved the substance. Q1 traced the registration
error to a category-error analogy ("no dispersion parameter" mapped onto "dispersion parameter
held fixed"). Q2 then derived the corrected result rather than assuming it: for a canonical-link
GLM under response-only MCAR, the theorem's two $O(1)$ design terms — entropy-gradient $\times$
Cox–Snell MLE bias, and cross-entropy curvature — cancel exactly (Lemma P: because $\eta$ is
linear in $X$ and $\Omega$ carries the information weight, $\mathbb{E}[\eta wX^\top]\Omega^{-1}
\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]=\mathbb{E}[\eta A'''(X^\top\Omega^{-1}X)]$), so
$\mathbb{E}[T_{\text{fitted}}]=+\tfrac12\operatorname{tr}(\mathrm{RIV})+\Delta_h+O(1/N)$ with
$\Delta_h$ a base-measure functional: $0$ for Bernoulli ($h\equiv1$), $-0.396\cdot
\operatorname{tr}(\mathrm{RIV})$ for Poisson at the studied design. CAS: 15 checks incl. exact
finite-$n$ enumerations (`verification/cas-wolfram/verify_bernoulli_fitted_gap.py`). All targets
were re-registered in a commit preceding the production runs (`4aaeaae`); all five substantive
criteria passed (`afa4438`): Bernoulli asymptote $+0.512\pm0.037$ (derived $+0.5$); Poisson blind
arm $+0.113\pm0.027$ (derived $+0.104$; first Poisson simulation in the repo); draw discount
$-0.313\pm0.070$ at $N{=}2000$ (derived $-0.2606$); Student-t fixed-scale exemplar
$+0.025\pm0.049$ / $-0.483\pm0.049$ (derived $0$ / $-0.5$) — the known-scale collapse verified
outside MVN for the first time, with the entropy condition derived and dated before any code
(the Q1 process fix in action). Also found: the original phase-3 script fixed `mice(seed = 1)`
across all repetitions (one shared 50-draw set; se overstated independence) —
`verification/spikes/phase3-mice-seed-diagnostic.R`. Cross-model gate: GPT-5.5 Pro xhigh, Mode A
blind re-derivation + Mode B red-team (`todo/045b`), verdict recorded in todo/045. Manuscript
consequence: G9 rewritten chronology-first per the quorum's binding amendments; r3#2 response
rewritten to match; Gamma stays directional (non-canonical link, underived).

## 4. todo/040 registration doc — dated amendment to §9 (OBJ-01's third document)

Append at the end of §9:

> **Amendment (2026-07-04, after the quorum and the todo/045 investigation; reordered
> 2026-07-04 per the Gemini compliance validation,
> `tkal-reviews/gemini-045c-compliance-20260704/REPORT.md`, to keep the misses strictly before
> the corrected framing).** This section registered Bernoulli as "the scale-free/known-scale
> exemplar, dispersion fixed at 1 by the family," with targets of approximately $0$ for the
> deterministic plug-in and approximately $-0.5$ for the genuine posterior draw, and asserted
> the classification "with no new derivation needed." Both targets were missed: the measured
> plug-in value was $+0.853$ (se $0.161$), about $5.3$ standard errors from the registered
> $\approx0$, and the measured posterior-draw value was $+0.628$ (se $0.161$), about $7$
> standard errors from the registered $\approx-0.5$ and of the opposite sign. The
> classification was wrong, and "no new derivation needed" was the process failure that let it
> through: the known-scale collapse requires a flat conditional missing-data entropy, which
> Bernoulli does not have ($dH/dp=-\operatorname{logit}(p)$, zero only at $p=\tfrac12$). The
> family choice was pre-registered; the target attached to it was corrected post hoc, and the
> corrected target was then derived, CAS-verified, re-registered (`4aaeaae`), and confirmed
> blind (`afa4438`) — full record: todo/045 §§2–3.5, quorum record
> `tkal-reviews/quorum-phase3-bernoulli-20260703/`. The §10 numbers for Bernoulli are
> superseded (the plug-in value was Monte-Carlo noise around a true $+0.518\pm0.012$ at
> $R=200{,}000$; the draw value also carried a fixed `mice` seed across all repetitions — see
> `verification/spikes/phase3-mice-seed-diagnostic.R`).

## 5. Landing checklist (do NOT execute before the two gates clear)

1. GPT-5.5 Pro gate verdict triaged (Mode A blind landing scored; Mode B refutations, if any,
   triaged against the CAS + exact enumerations). If any C1–C8 refutation survives triage,
   todo/045 §3.1 reopens and NOTHING below lands.
2. Marcus ratifies this file.
3. Land G9 via a new `manuscript/plan/updates/update-g9-rewrite-YYYYMMDD.py` (edit level3 only),
   run `scripts/check_plan.py` (must be green), rebuild `py scripts/build_manuscript_apa.py`,
   render, confirm exit 0.
4. Land the r3#2 letter body + the decisions.md D-24 pointer + D-25 + the todo/040 §9 amendment
   via Bash writes (citation-hook cwd gotcha for manuscript/ subdirs).
5. Commit as ONE landing commit citing this file; update todo/045 status to CLOSED; then resume
   the Phase-4 tail (r3#3) and annotation/compile-enablement.
