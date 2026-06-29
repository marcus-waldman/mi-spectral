# Contributions brief — grounded input for the tkal-in-ket Delphi (todo/035)

**Purpose.** This is the self-contained input for a cross-family Delphi (Claude +
GPT-5.5 + Gemini) that will converge on, and then ratify, the set of contributions
this paper claims. The panel has **no repository access**, so every candidate
contribution below is stated with the evidence behind it: what was derived (anchor),
what was verified (dual computer-algebra plus Monte Carlo), and the witness study
plus the number. Read it as the whole evidentiary basis; nothing outside this brief
is available to the panel.

**What the Delphi decides.**

- **Pool phase** — converge on the best *set, ordering, and framing* of the
  contributions this paper should claim, and of the applied-research implications.
  The contributions will be presented twice: an enumerated **Contributions** list
  closing the Introduction (the skim hook), and an **implications for applied
  research** passage in the Discussion. The applied angle is the priority: an
  applied researcher who only skims the paper should still see why it matters.
- **Axes phase** — ratify each converged contribution against four criteria:
  1. **Real** — is it genuinely supported by the stated evidence, at the standing
     claimed (proved-and-verified vs measured vs conjecture)?
  2. **Novel** — is it new against the lineage below, or already in the literature?
  3. **Important to applied readers** — would a practitioner who uses multiple
     imputation care?
  4. **Correctly scoped** — is the phrasing free of overclaim (right conditions,
     right hedges)?

---

## The paper in three sentences

The paper shows that the averaged log-likelihood across imputations — the object
that multiple-imputation versions of likelihood-ratio tests and information criteria
are built on — carries a systematic deviance bias of one half the trace of the
relative-increase-in-variance matrix, plus a smaller design-imbalance term. It
characterizes this bias, gives the correction, and works out the two places it
changes practice: likelihood-ratio model comparison and information-criterion model
selection. It is an AI-assisted derivation with transparent, ORCID-verified human
prompting, prepared for the Journal for AI Generated Papers, with every load-bearing
claim paired to a preregistered numerical study.

Target reader: an applied researcher with quantitative training and working
knowledge of multiple imputation.

## Lineage (for the novelty judgment)

Rubin (1987, multiple imputation and the combining rules) → Meng & Rubin (1992,
likelihood-ratio combining) and Meng (1994, congeniality) → Cavanaugh & Shumway
(1998, AICcd — a bias correction for the *EM-based observed-data* MLE, a parallel
universe with a different target and improper, not proper, imputation) →
Consentino & Claeskens (2010, the prior MI-AIC proposal, penalty 2·p_S, whose
authors explicitly flag its theoretical justification as beyond their scope) →
Chan & Meng (2022, *Statistica Sinica*) and Chan (2022, *Annals of Statistics*,
the canonical reference for calibrating MI likelihood-ratio tests — it fixes the
*reference distribution*) → **this work**, which corrects the *bias of the
statistic* being referred to that distribution. Calibration and centering are
complementary: a calibrated reference and a centered statistic are both needed for
complete-data-equivalent inference under imputation. Separately, Shimodaira (2017)
derived an AIC penalty AIC_{x;y} for a related covariate-shift problem; its trace
term coincides with the trace correction here, reached from a different motivation
(target prediction rather than complete-data replication).

---

## Candidate contributions

### C1 — Theory: the deviance-bias decomposition

**Claim.** Under congenial proper multiple imputation, with the complete-data
maximum-likelihood estimate as the target, the averaged log-likelihood across
imputations overstates its complete-data counterpart by exactly **+½·tr(RIV) +
(A)+(C)**. The half-trace splits into an imputation-bias term **+tr(RIV)** and an
estimation-mismatch term **−½·tr(RIV)** (the mismatch arises because imputation
targets the complete-data estimate, not the observed-data estimate). The result
requires an *estimated scale*: a known-scale, location-only fit collapses the bias
to 0 (full-information likelihood) or −½·tr(RIV) (proper imputation). The (A)+(C)
term is a design-imbalance term that appears only under data missing at random and
**vanishes exactly under data missing completely at random**.

**Evidence and standing.**
- Derived analytically (anchor: sec-thm), and cross-confirmed by a convention-free
  reading in which the same bias equals a conditional-entropy plug-in bias under an
  entropy–Hessian split.
- Verified in two independent computer-algebra systems and by Monte Carlo: in the
  pooled design the measured deviance bias is **2.43 ± 0.26**, matching the analytic
  +½·tr(RIV)+(A)+(C) range of **2.42–2.55**; the preregistered point 2.77 lies
  inside the 95% confidence interval [1.93, 2.94]. (Witness W1.)
- Standing: the +½·tr(RIV) decomposition is **firm** (proved and verified). The
  (A)+(C) term's **sign and order are firm**; its value is heavy-tailed order-one
  and is not independently pinned to a constant.

**Novelty.** The +½·tr(RIV) trace magnitude coincides with Shimodaira's AIC_{x;y}
penalty, so the trace term itself is precedented. The new pieces are (i) the MAR
design-imbalance term (A)+(C), and (ii) the statement and proof for *proper*
multiple imputation, where the prior bias-correction line (Cavanaugh–Shumway) lives
in the EM/improper universe with a different target.

### C2 — Likelihood-ratio comparison: the differential bias is tr(RIV_⊥)

**Claim.** At the null, the differential deviance bias of the likelihood-ratio
numerator is **tr(RIV_⊥)** — the missing information of the *tested directions*,
projected in the complete-data information metric (the Q-function's curvature is the
complete-data information, so the constrained imputation fit projects there). It is
provably **not** the naive difference of per-model trace corrections,
tr(RIV_full) − tr(RIV_0), which **always overstates** it (a Gram/Schur inequality;
equality only when the tested directions decouple, which includes the
equal-fractions case; the overstatement exceeds threefold in unfavorable designs).
Sharing the same imputations across the two nested fits collapses the paired
Monte-Carlo noise from order √n to order one at the null and local alternatives. The
(A)+(C) differential cancels exactly at the null (a shared-imputation common
constant) and returns at order one only for pseudo-true-separated, non-nested pairs.

**Evidence and standing.**
- Derived analytically (anchor: sec-lrt). Monte Carlo discriminates the exact
  tr(RIV_⊥) from the naive difference at **52 standard errors**.
- At the null, tr(RIV_⊥) is exactly the mean that a correctly calibrated reference
  distribution (Chan 2022) already absorbs. So adding a numerator correction *on top
  of* a calibrated test double-counts: in witness W2 the test size is 0.042
  uncorrected versus 0.034 over-corrected. The bias therefore matters where no
  calibrated reference stands between the statistic and its use.
- Standing: **firm** (proved and verified).

**Novelty.** That the relevant quantity is the *projected* missing information in the
complete-data metric — and is strictly smaller than the naive trace difference —
appears to be new; the prior combining/calibration line handles the reference
distribution, not the numerator's bias.

### C3 — Information-criterion selection: the bias is model-specific

**Claim.** The deviance bias is **model-specific** — different candidate models have
different RIVs — so uncorrected MI-AIC and MI-BIC systematically favor the candidates
with **more missing information**. Adding tr(RIV_k) to each candidate's criterion
restores complete-data-equivalent selection and reproduces Shimodaira's AIC_{x;y}.
Empirically, **100% of uncorrected MI-AIC misclassifications land on the
largest-RIV candidate** (a preregistered directional prediction, W3-C = 1.000 across
all 60 cells). A calibration ladder locates the null/noncentral boundary: on the
null side the corrected criterion selects indistinguishably from complete-data AIC
(0.904 / 0.903 versus 0.899), while under signal the noncentral statistic shrinks by
exactly the predicted factor and the weak-signal selection floor (0.17) is genuine
information loss, not a calibration error.

**Evidence and standing.**
- Derived analytically (anchor: sec-ic); ladder criteria C1–C6 all pass.
- Two structural limits are disclosed honestly. (i) The W3/ladder candidate family
  is exactly the equality case of the Gram/Schur inequality from C2, so the
  overstatement is invisible there (naive ≡ exact to 3.6×10⁻¹⁵). (ii) Per-model
  marginal transforms cannot calibrate a *difference* distribution (a score-copula
  invariance; the equipercentile-equated difference has mean 6.10 against the
  complete-data 10.00).
- Standing: the model-specific bias and the direction of the tilt are **firm**; the
  100%-on-largest-RIV result is a **measured** preregistered prediction that held;
  the structural limits are **proved**.

**Novelty.** The prior MI-AIC proposal (Consentino–Claeskens 2010) left its
theoretical justification open; this supplies the bias term, its model-specificity,
the direction of the resulting tilt, and the boundary of where correction restores
complete-data behavior.

### C4 — Method: a structured, auditable AI–human workflow with provenance

**Claim (foreground this — it is the applied skim hook).** The paper is itself a
worked instance of a structured AI–human collaboration with transparent,
ORCID-verified provenance that is demonstrably **both productive and accurate**.
Division of labor: the human sets direction, standards, field knowledge, and the
acceptance or rejection of every result; the AI produces the derivations, drafts,
and computations; results enter the record only through stated gates. The gates are:
1. **Sourced citations**, enforced mechanically by a pre-write hook — no reference
   appears without a locally archived, session-read copy of the source.
2. **A claim pipeline**: derive → verify in two independent computer-algebra systems
   → confirm by Monte Carlo against frozen criteria, with explicit trust tiers.
3. **Preregistration before code**, with dated amendments and failed predictions
   reported in the main text.
4. **Cross-model adversarial review** by an independent model lineage instructed to
   refute load-bearing claims.
5. **Full reproducibility** — seeds, caches, single-entry-point scripts, environment
   records; every number regenerates.

**Evidence and standing.**
- The collaboration is documented by a qualitative coding of the *complete* session
  record: **599 substantive human-authored turns (29,394 words) across 34 sessions**,
  a five-pattern characterization, and **58 verified episodes** (each with a verbatim
  quote and a traced dated artifact). The analysis was itself run as a 95-agent
  workflow; its checkable parts (quotes, artifact existence and timing, arithmetic)
  were verified mechanically.
- Worked example of what the adversarial gate catches that single-lineage derivation
  would ship: **eight of nine blind re-derivations** by an independent model returned
  the *opposite sign* of the main theorem, exposing a silent conditioning
  substitution; the fix was ratified in one line (episode E14).
- Standing: the workflow and its records are **firm** (the documented facts are
  mechanically verified). The honest limit, stated in the source: the session coding
  was done by the same model lineage being analyzed, with no human second coder, so
  the *frequencies* are model judgments while the quotes, artifacts, and arithmetic
  are verified.

**Novelty.** Transparent AI-assisted derivation with this degree of mechanically
enforced discipline and an after-the-fact coded audit of the collaboration is, to our
knowledge, not yet standard practice; it is offered as a template, not just a
disclosure.

---

## Candidate applied-research implications

1. **A correction practitioners can compute.** Researchers who select models or
   compare nested models on multiply-imputed data are, without realizing it, using
   statistics biased toward the candidates with the most missing information. The
   correction is a single trace term, tr(RIV_k), computed per candidate.
2. **Where the bias bites, and where it does not.** The bias matters precisely where
   no reference distribution stands between the statistic and its use:
   information-criterion ranking, explicit numerator corrections, and non-nested
   comparison. Where a calibrated likelihood-ratio test is used (Chan 2022), the
   mean is already absorbed and the correction must not be applied a second time.
3. **A template for trusting AI-assisted methods work.** The workflow gives an
   applied team a concrete standard to demand of any AI-assisted derivation before
   believing it — sourced citations, dual computer-algebra plus Monte Carlo,
   preregistration with reported failures, cross-model refutation, full
   reproducibility — together with evidence that meeting that standard is compatible
   with actually getting the work done.

---

## Notes for the panel

- Trust tiers are used above deliberately. **Firm** = proved and independently
  verified. **Measured** = a preregistered numerical prediction that held. **Proved**
  (for the structural limits) = analytic. Where a quantity is order-one and not
  pinned to a constant, that is said.
- The applied priority is C4 and the implications: the paper wants a skimming
  applied reader to come away with (i) "my MI model-selection table is biased toward
  high-missing-information models and there is a one-term fix," and (ii) "this is what
  a trustworthy AI-assisted derivation looks like."
- Open question for the panel: is the workflow a *first-class scientific
  contribution* on the same footing as C1–C3, or a *methodological disclosure* that
  should be framed as supporting rather than headline? The author's working position
  is first-class; the Delphi should test it.
