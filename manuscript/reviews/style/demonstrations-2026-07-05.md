# Demonstration rewrites for ratification (todo/048, Phase C)

**Date: 2026-07-05. Six side-by-side rewrites — current register vs. proposed register.
NOTHING here is applied: level3 is untouched, and these paragraphs live only in this
document until Marcus ratifies, amends, or rejects the direction.** Rubric of record:
`manuscript/reviews/style/rubric-2026-07-05.md`. Each demonstration lists (a) the rubric
features exercised and (b) an invariance check confirming that every fact, number, hedge,
and citation is unchanged. Bucket-3 vocabulary (e.g. "ladder") is left as-is pending
Marcus's call; Bucket-2 replacements are exercised.

The six span the registers the handoff asked for: the S1 opener, the S1 central-result
paragraph, an S2 background paragraph, an S4 theorem-adjacent part-opener, an S5 results
paragraph, and the S6 discussion opener.

---

## Demonstration 1 — S1-P1 (the Introduction opener)

### Current

> Multiple imputation treats missing data through a division of labor, and that division
> has served applied research for nearly four decades. An imputer fills in the missing
> values several times from a model for the complete data. An analyst then fits the model
> of substantive interest to each completed data set, and simple rules combine the results
> [@rubinMultipleImputationNonresponse1987]. The field's own accounts of its state of the
> art describe a mature methodology [@schaferMissingDataOur2002a;
> @endersMissingDataUpdate2025]. In those accounts the role of the missing-data mechanism
> is understood, point estimates recover their complete-data targets under stated
> conditions, and Wald-type tests for single and multiple parameters are well calibrated.
> On that testimony, the major inferential questions read as settled.

### Proposed

> Multiple imputation treats missing data through a division of labor that has served
> applied research for nearly four decades: an imputer fills in the missing values several
> times from a model for the complete data, an analyst fits the model of substantive
> interest to each completed data set, and simple rules combine the results
> [@rubinMultipleImputationNonresponse1987]. Reviews of the field's state of the art
> describe a mature methodology [@schaferMissingDataOur2002a; @endersMissingDataUpdate2025],
> in which the role of the missing-data mechanism is understood, point estimates recover
> their complete-data targets under stated conditions, and Wald-type tests for single and
> multiple parameters are well calibrated. On these accounts, the major inferential
> questions appear settled.

### Rubric features exercised

- **R1**: six sentences become three; the three-step division of labor rides in one
  colon-introduced series (the register's default architecture; cf.
  `barnardMiscellaneaSmallsampleDegrees1999:31`, a single opening sentence with three
  parallel members).
- **R6/C7**: "The field's own accounts of its state of the art describe" (the attribution
  scaffold) becomes the ordinary attributed construction "Reviews of the field's state of
  the art describe" — attribution preserved, contortion removed.
- **C8**: "On that testimony ... read as settled" (literary) becomes "On these accounts
  ... appear settled".

### Invariance check

- Facts: division of labor; imputer/analyst/combining-rules roles; "nearly four decades";
  mechanism understood; point estimates recover complete-data targets *under stated
  conditions*; Wald-type tests for single and multiple parameters — all present, none
  added.
- Numbers: none in either version.
- Hedges: "under stated conditions" kept verbatim; "well calibrated" kept verbatim;
  settledness remains *attributed, not endorsed* (T-06): "Reviews ... describe" + "On
  these accounts ... appear settled" carries the same typed claim as "The field's own
  accounts ... read as settled".
- Citations: identical three citekeys, same attachment points.

---

## Demonstration 2 — S1-P4 (the central-result paragraph)

### Current

> The obstacle is a bias in the averaged log-likelihood. This paper's central result
> describes that bias exactly. Suppose a likelihood model with an estimated variance or
> covariance is fit to congenially imputed data. We show that the averaged log-likelihood
> then overstates its complete-data counterpart by
> $$ \tfrac{1}{2}\operatorname{tr}(\mathrm{RIV}) \;+\; (A){+}(C). $$
> The first term is one half the trace of the relative-increase-in-variance matrix. This
> matrix is a standard object in the MI literature. Its trace adds up the missing
> information about the model's parameters. The second term is smaller. It reflects
> imbalance between the observed and the missing units on the conditioning variables, and
> vanishes when the data are missing completely at random. The practical consequence is
> that, for such a model, every deviance and information criterion built on the averaged
> log-likelihood across imputations is, in expectation, too optimistic. Worse, the
> optimism is not uniform across models. Each candidate's criterion is inflated in
> proportion to that candidate's own missing information. A model-comparison table built
> on imputed data therefore tends, all else equal, to favor the candidates with the most
> missing information. In our pre-registered simulations, 100% of uncorrected MI-AIC's
> misclassifications fell on the candidate with the largest RIV. The fix is direct. Add
> each candidate's own trace back to its criterion. We show that the corrected criterion
> recovers its complete-data expectation at any signal strength. This is the principle's
> second level, met in full.

### Proposed

> The obstacle is a bias in the averaged log-likelihood, and this paper's central result
> describes that bias exactly. When a likelihood model with an estimated variance or
> covariance is fit to congenially imputed data, we show that the averaged log-likelihood
> overstates its complete-data counterpart by
> $$ \tfrac{1}{2}\operatorname{tr}(\mathrm{RIV}) \;+\; (A){+}(C). $$
> The first term, one half the trace of the relative-increase-in-variance matrix (a
> standard object in the MI literature), adds up the missing information about the model's
> parameters; the second, smaller term reflects imbalance between the observed and the
> missing units on the conditioning variables, and vanishes when the data are missing
> completely at random. The practical consequence is that, for such a model, every
> deviance and information criterion built on the averaged log-likelihood across
> imputations is, in expectation, too optimistic. The more serious consequence is that the
> optimism is not uniform across models: because each candidate's criterion is inflated in
> proportion to that candidate's own missing information, a model-comparison table built
> on imputed data tends, all else equal, to favor the candidates with the most missing
> information, and in our pre-registered simulations 100% of uncorrected MI-AIC's
> misclassifications fell on the candidate with the largest RIV. The correction is direct.
> Adding each candidate's own trace back to its criterion recovers, as we show, the
> criterion's complete-data expectation at any signal strength, so the principle's second
> level is met in full.

### Rubric features exercised

- **R1**: seventeen sentences become nine; the two-term gloss becomes one subordinated
  sentence with a semicolon join (C6); the mechanism-to-consequence chain
  ("because ... tends ... and in our simulations ...") rides in one sentence.
- **R2**: "(a standard object in the MI literature)" — the parenthetical gloss replacing
  a stand-alone declarative.
- **R4/R5**: "Worse," becomes "The more serious consequence is that" — the register's own
  escalation (cf. `rubinMultipleImputationNonresponse1987:588` "The more serious problem
  concerns bias.").
- Formula variety (R3): one "we show that" survives up front; the second becomes the
  interpolated "as we show", breaking the repetition.

### Invariance check

- Facts: estimated variance/covariance condition; congenial imputation; overstatement;
  two-term decomposition with the first = ½tr(RIV) and the second smaller,
  imbalance-driven, MCAR-vanishing; per-candidate inflation proportional to own missing
  information; direction of the selection tilt; the correction (add each candidate's own
  trace) — all unchanged. Display equation byte-identical.
- Numbers: "100%" kept; "one half the trace" kept.
- Hedges: "in expectation", "tends, all else equal", "at any signal strength",
  "in our pre-registered simulations" — all verbatim. "Worse" → "The more serious
  consequence" preserves the escalation (not a neutral "moreover").
- Citations: none in either version (the display and claims are the paper's own).
- Accuracy invariants: candidates favored by *missing information*, never by data
  quantity — wording preserved exactly.

---

## Demonstration 3 — S2-P7 (background: proper imputation)

### Current

> **Proper imputation.** The imputations this paper studies are proper in Rubin's sense,
> and whether imputation is proper or improper changes the bias the theorem derives.
> Proper imputation propagates parameter uncertainty. A parameter value is first drawn
> from its posterior given the observed data, and the missing values are then drawn from
> the predictive distribution at that drawn value. Chapter 4 of
> @rubinMultipleImputationNonresponse1987 states the validity conditions and gives the
> fully normal Bayesian scheme as the canonical example. Improper imputation skips the
> first draw and imputes at a fixed parameter value. The Monte Carlo E-step of the
> previous paragraph is improper by construction, and so is the entire deterministic-EM
> line of work in which the earlier missing-data criteria were derived
> [@cavanaughAkaikeInformationCriterion1998a; @shimodairaInformationCriterionModel2017].
> The distinction is not bookkeeping, because the extra posterior draw contributes its own
> variation to the averaged log-likelihood, and the main theorem prices it exactly.
> Consider the known-scale case. The bias is zero under improper imputation at the
> observed-data estimate, while under proper imputation it is
> $-\tfrac12\operatorname{tr}(\mathrm{RIV})$, so the two forms differ by precisely the
> posterior-draw contribution. Properness is also not absolute.
> @nielsenProperImproperMultiple2003 shows that Bayesian imputations are proper when the
> analyst's complete-data estimator is the maximum likelihood estimator, but the same
> imputations can fail to be proper for a different estimator. This paper's analyst always
> uses the complete-data MLE, which is the case where congeniality implies properness
> [@nielsenProperImproperMultiple2003]. The extension of the bias accounting from the
> improper, deterministic Q-function to proper multiple imputation is one of the things
> this paper adds.

### Proposed

> **Proper imputation.** The imputations this paper studies are proper in Rubin's sense,
> and whether imputation is proper or improper changes the bias the theorem derives.
> Proper imputation propagates parameter uncertainty: a parameter value is first drawn
> from its posterior given the observed data, and the missing values are then drawn from
> the predictive distribution at that drawn value; Chapter 4 of
> @rubinMultipleImputationNonresponse1987 states the validity conditions and gives the
> fully normal Bayesian scheme as the canonical example. Improper imputation, by contrast,
> skips the first draw and imputes at a fixed parameter value — the Monte Carlo E-step of
> the previous paragraph is improper by construction, as is the entire deterministic-EM
> line of work in which the earlier missing-data criteria were derived
> [@cavanaughAkaikeInformationCriterion1998a; @shimodairaInformationCriterionModel2017].
> The distinction is more than a matter of bookkeeping, because the extra posterior draw
> contributes its own variation to the averaged log-likelihood, and the main theorem
> quantifies that contribution exactly: in the known-scale case the bias is zero under
> improper imputation at the observed-data estimate but
> $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper imputation, so the two forms
> differ by precisely the posterior-draw contribution. Nor is properness absolute.
> @nielsenProperImproperMultiple2003 shows that Bayesian imputations are proper when the
> analyst's complete-data estimator is the maximum likelihood estimator, yet the same
> imputations can fail to be proper for a different estimator; this paper's analyst always
> uses the complete-data MLE, which is the case where congeniality implies properness
> [@nielsenProperImproperMultiple2003]. The extension of the bias accounting from the
> improper, deterministic Q-function to proper multiple imputation is one of the things
> this paper adds.

*(If the em-dash ban stays (rubric C3 recommendation), the third sentence's dash becomes
a semicolon or a parenthesis; it is shown here to display the appositive option.)*

### Rubric features exercised

- **R1/C6**: twelve sentences become seven; the definition rides a colon; the source
  pointer joins by semicolon rather than standing alone.
- **R2**: the improper-by-construction observation becomes an appositive rider.
- **C8**: "prices it exactly" (finance metaphor, 3× in the manuscript) becomes
  "quantifies that contribution exactly".
- **R5**: "Nor is properness absolute." — a short pivot sentence *kept*, showing the
  punctuating short sentence used as the register uses it.

### Invariance check

- Facts: proper vs improper definition; the posterior-then-predictive two-step; Chapter 4
  attribution; the Monte Carlo E-step and the deterministic-EM line both improper; the
  known-scale contrast (0 vs $-\tfrac12\operatorname{tr}(\mathrm{RIV})$); Nielsen's
  properness result and its estimator-dependence; the MLE-analyst scope; the
  paper's-own-addition claim — all unchanged.
- Numbers: $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ and 0 kept.
- Hedges: "in Rubin's sense", "by construction", "precisely", "which is the case where
  congeniality implies properness" — verbatim; the closing modesty ("one of the things
  this paper adds") verbatim.
- Citations: identical four attachment points, same citekeys (Rubin Ch. 4;
  Cavanaugh–Shumway + Shimodaira pair; Nielsen twice).

---

## Demonstration 4 — S4-P16 (theorem-adjacent: the selection part-opener)

### Current

> This part takes up the replication principle's third level for selection, where the
> bias has no reference distribution to hide behind. Model selection by information
> criterion compares penalized deviances as numbers and takes the smallest, so whatever
> bias each candidate's $-2\bar Q_\infty$ carries lands directly in the ranking. By
> @thm-bias that bias is model-specific, because $\mathrm{RIV}_k$ is computed on candidate
> $k$'s own parameter space. The corrected criterion takes this form.
> $$ \mathrm{AIC}_{\mathrm{MI}}^{c}(k) \;=\; -2\bar Q_\infty(\hat\psi^{*}_k) + 2q_k + \operatorname{tr}(\mathrm{RIV}_k). $$
> This penalty reproduces $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017,
> and its missing-data surcharge is exactly half that of the earlier
> complete-data-discrepancy criteria [@cavanaughAkaikeInformationCriterion1998a]. What
> @thm-bias adds is the anatomy, the MAR term, and the proper-MI scope. The ranking
> consequence is immediate. For two candidates the uncorrected difference carries a
> differential bias whose leading term is the surplus of missing information, so the
> candidate with more missing information about its own parameters looks artificially
> better by exactly that surplus.

### Proposed

> This part takes up the replication principle's third level for selection, where no
> reference distribution stands between the statistic and its use. Because model selection
> by information criterion compares penalized deviances as numbers and takes the smallest,
> whatever bias each candidate's $-2\bar Q_\infty$ carries enters the ranking directly,
> and by @thm-bias that bias is model-specific, since $\mathrm{RIV}_k$ is computed on
> candidate $k$'s own parameter space. The corrected criterion is
> $$ \mathrm{AIC}_{\mathrm{MI}}^{c}(k) \;=\; -2\bar Q_\infty(\hat\psi^{*}_k) + 2q_k + \operatorname{tr}(\mathrm{RIV}_k). $$
> This penalty reproduces $\mathrm{AIC}_{x;y}$ of @shimodairaInformationCriterionModel2017,
> with a missing-data surcharge exactly half that of the earlier complete-data-discrepancy
> criteria [@cavanaughAkaikeInformationCriterion1998a]; what @thm-bias adds is the
> decomposition of the bias, the MAR term, and the proper-MI scope. The consequence for
> ranking is immediate: for two candidates, the uncorrected difference carries a
> differential bias whose leading term is the surplus of missing information, so the
> candidate with more missing information about its own parameters looks artificially
> better by exactly that surplus.

### Rubric features exercised

- **C8 (Bucket 2)**: "lands directly in the ranking" → "enters the ranking directly";
  "has no reference distribution to hide behind" (figurative) → "no reference
  distribution stands between the statistic and its use" — the manuscript's own phrasing
  from S4-P14, reused for consistency rather than invented.
- **C8**: "the anatomy" (figurative) → "the decomposition of the bias" — the literal
  content, matching the S1-P6 novelty list ("the decomposition of the bias into an
  imputation-bias part and an estimation-mismatch part").
- **R1/C6**: the display's lead-in becomes "The corrected criterion is" (register norm:
  displays are introduced mid-sentence); the Shimodaira/Cavanaugh sentence joins its
  companion by semicolon; the consequence sentence rides a colon.

### Invariance check

- Facts: third level for selection; compares-penalized-deviances mechanism;
  model-specificity via $\mathrm{RIV}_k$ on candidate $k$'s own parameter space; the
  Shimodaira reproduction; the exactly-half surcharge relation; the three additions of
  @thm-bias; the surplus-of-missing-information direction — all unchanged. Display
  byte-identical.
- Numbers: "exactly half" kept.
- Hedges: "looks artificially better by exactly that surplus" verbatim (including
  "artificially" — the accuracy-invariant wording that attributes the tilt to missing
  information, not data quantity).
- Citations: identical two citekeys, same attachment points; cross-references @thm-bias
  (2×) unchanged.

---

## Demonstration 5 — S5-P18 (results: the distribution-matching ladder)

*"Ladder" is Bucket 3 (Marcus's call) and is left unchanged here; @tbl-ladder itself
(numbers) is untouched and omitted from the quotation for space.*

### Current

> **The distribution-matching ladder.** Across three levels of signal strength the
> stronger constructions recover the complete-data benchmark where the errors come from
> choosing too rich a model. A floor remains where selection is genuinely hard
> (@fig-ladder). The true-model selection rates are reported in @tbl-ladder, with Monte
> Carlo standard error near $0.010$.
>
> [table unchanged]
>
> At correlation $0.40$ the two-moment and equating arms reach $0.904$ and $0.903$
> against a complete-data benchmark of $0.899$, and the differences are within twice the
> Monte Carlo standard error of about $0.010$. Both arms are therefore statistically
> indistinguishable from the benchmark, with a small overshoot the same interval does not
> resolve. The junk cell closes $90$ percent of the gap from uncorrected to benchmark. In
> the weak-signal cell the benchmark itself drops to $0.820$, and no arm passes $0.650$.
> We read that floor as a limit of the information in the data rather than a calibration
> error, and the calibration checks below support that interpretation, though they do not
> separately decompose it in the weak-signal cell. The residual is a measurement on these
> designs rather than a theorem.

### Proposed

> **The distribution-matching ladder.** Across three levels of signal strength, the
> stronger constructions recover the complete-data benchmark wherever the errors come
> from choosing too rich a model, while a residual shortfall remains where selection is
> hard even with complete data (@fig-ladder). The true-model selection rates are reported
> in @tbl-ladder, with Monte Carlo standard error near $0.010$.
>
> [table unchanged]
>
> At correlation $0.40$ the two-moment and equating arms reach $0.904$ and $0.903$
> against a complete-data benchmark of $0.899$; because the differences are within twice
> the Monte Carlo standard error of about $0.010$, both arms are statistically
> indistinguishable from the benchmark, with a small overshoot the same interval does not
> resolve. The zero-correlation cell removes $90$ percent of the difference between the
> uncorrected criterion and the benchmark. In the weak-signal cell, by contrast, the
> benchmark itself drops to $0.820$ and no arm passes $0.650$. We read that shortfall as
> a limit of the information in the data rather than as a calibration error, an
> interpretation the calibration checks below support, although they do not separately
> decompose it in the weak-signal cell; the residual is a measurement on these designs
> rather than a theorem.

### Rubric features exercised

- **C8 (Bucket 2)**: "A floor remains" → "a residual shortfall remains" (deliberately not
  "bound", which would upgrade a measurement to a proof claim); "genuinely hard" → "hard
  even with complete data" (the sharper literal fact: the benchmark itself is 0.820);
  "The junk cell closes 90 percent of the gap" → "The zero-correlation cell removes 90
  percent of the difference" (the design defines this cell by $\rho = 0$; the matching
  @tbl-ladder row label "(junk)" would change in the same sweep batch).
- **R1**: the finding and its qualifier join in one sentence ("recover ... wherever ...,
  while a residual shortfall remains where ..."); the interpretive close subordinates
  ("an interpretation the calibration checks below support, although ...") and takes a
  C6 semicolon.
- **R5**: "by contrast" added as the register's paragraph-internal pivot.

### Invariance check

- Facts: stronger constructions reach the benchmark where errors are overfit flips; a
  residual remains in the weak-signal cell; interpretation as information limit, not
  calibration error; the checks support but do not decompose it there; measurement, not
  theorem — all unchanged.
- Numbers: $0.904$, $0.903$, $0.899$, $0.010$ (twice), $90$ percent, $0.820$, $0.650$ —
  all present, all identical; the table is untouched.
- Hedges: "near $0.010$", "about $0.010$", "statistically indistinguishable", "a small
  overshoot the same interval does not resolve", "We read that ... as", "though/although
  they do not separately decompose it", "a measurement ... rather than a theorem" — all
  preserved at identical strength.
- Citations: none; cross-references @fig-ladder/@tbl-ladder unchanged.

---

## Demonstration 6 — S6-P1 (the Discussion opener)

### Current

> The result is scoped by its own mechanism. The scope comes first. The deviance optimism
> that inflates the criteria exists only when the fit estimates a scale or covariance. In
> that case the conditional missing-data entropy depends on the estimated parameters. A
> known-scale, location-only fit has no such bias under deterministic FIML and only
> $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper MI. That is why the
> estimated-scale clause sits in the theorem rather than in a footnote. Congeniality is
> assumed throughout. What the bias becomes without it
> [@mengMultipleImputationInferencesUncongenial1994a] is a separate question. This paper
> does not take it up. Beyond these scope conditions, six specific limits remain. Each is
> stated next to the claim it qualifies, with its evidential standing. They are followed
> by one conjecture, three directions, and the answer to the question the paper opened
> with.

### Proposed

> The scope of the result follows from its own mechanism, and we state that scope first.
> The deviance optimism that inflates the criteria exists only when the fit estimates a
> scale or covariance, because only then does the conditional missing-data entropy depend
> on the estimated parameters; a known-scale, location-only fit has no such bias under
> deterministic FIML and only $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper MI,
> which is why the estimated-scale clause belongs in the statement of the theorem rather
> than in a footnote. Congeniality is assumed throughout, and what the bias becomes
> without it [@mengMultipleImputationInferencesUncongenial1994a] is a separate question
> that this paper does not take up. Beyond these scope conditions, six specific limits
> remain, each stated next to the claim it qualifies together with its evidential
> standing, and they are followed by one conjecture, three directions, and the answer to
> the question the paper opened with.

*(Incidental catch, flagged in the Phase B review and NOT fixed here: "six specific
limits" appears stale against the current G1–G9 list; the count is preserved verbatim in
this demonstration because a style pass changes no facts. Reconciling the count is a
separate one-line content fix for Marcus to order.)*

### Rubric features exercised

- **C8 (Bucket 2)**: "is scoped by" → "The scope of the result follows from"; "sits in
  the theorem" → "belongs in the statement of the theorem".
- **R1**: twelve sentences become four; mechanism, condition, special case, and
  placement-consequence chain into one subordinated sentence with a C6 semicolon; the
  standing-assumption sentence absorbs its two fragment followers ("is a separate
  question that this paper does not take up").
- The paragraph retains its contract function (what follows and in what order) — R7.

### Invariance check

- Facts: estimated-scale condition; entropy dependence as the mechanism; the known-scale
  collapse pair (0 under deterministic FIML, $-\tfrac12\operatorname{tr}(\mathrm{RIV})$
  under proper MI); congeniality standing assumption; uncongeniality deferred; the
  Discussion's structure promise — all unchanged, including the (stale, flagged) "six".
- Numbers: $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ kept.
- Hedges: "only when", "no such bias", "a separate question" — verbatim strength.
- Citations: @mengMultipleImputationInferencesUncongenial1994a kept at the same
  attachment point.

---

## What ratification decides

1. **The direction**: rewrite the corpus toward the register these six demonstrate
   (R1/R2 sentence architecture, C7 attribution repair, Bucket-2 vocabulary), in
   section-sized Marcus-gated batches per the handoff's Phase D.
2. **The C-table dispositions** (rubric §2), each becoming a dated decisions.md amendment
   plus CLAUDE.md rewrite plus check_plan/scout recalibration in one commit — notably C1
   (drop FK-10 for the register band), C2 (subordination default), C3 (parentheses
   unbanned; em-dash ban kept or lifted), C5 (narrowed color-commentary ban), C6
   (semicolon budget).
3. **Bucket 3 calls**: "ladder" (keep-and-introduce vs rename), the "Perfect is" caption
   convention (rephrase vs keep), e.g./i.e. in parentheses, the em-dash question, and
   whether one or two signature sentences ("Corrected criteria are honest, not
   clairvoyant."; "the data no longer say") survive as deliberate exceptions.
4. **The incidental catches** (Phase B review §"Incidental accuracy catches"): the
   "six specific limits" count and the @fig-w4-nonnested caption escaping.
