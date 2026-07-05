# Evidence-map table proposal (S5 claims-to-evidence organization, for Marcus's gate)

**Date: 2026-07-05. GATE DOCUMENT — content addition, not a style change; nothing
applied until Marcus approves.** Marcus's diagnosis: a reader reaching any single
simulation study cannot hold the connection to the claim it tests — the claim lives in
S4, the design in S5's setup subsection, the outcome in S5's results subsection, and the
reader's working memory is the only join. The remedy: one table, early in S5, mapping
claim → analytic basis → design → result, so the reader can enter any exhibit and
recover its purpose from one place.

Two supporting facts. First, the manuscript already PROMISES this mapping in prose
(S5-P1: "every quantitative claim in @sec-derivations points here, and every number here
traces to one study") without giving the reader the map. Second, the plan system
maintains exactly this join table internally (`manuscript/plan/level4-evidence.json`,
linted by check_plan) — the table surfaces existing, checkable structure rather than
inventing new claims. Register precedent: simulation sections in JASA/Biometrika
routinely open with a design-summary table.

## Mechanics

- New level3 unit **S5-P1b**, placed directly after S5-P1: a two-sentence lead-in + the
  table (`{#tbl-evidence-map}`). Full paragraph object (proposition, review, audit,
  depends_on S5-P1) so check_plan's structural gates pass.
- Optional (flagged for your call): one pointer clause appended to S4-P1's final
  sentence — "...and all empirical evidence is reported in @sec-simulations, where
  @tbl-evidence-map maps each claim to its study." — so the reader learns the map exists
  before S4's claims start arriving. RECOMMENDED.
- Rendering: an 11-row, 4-column table with math cells; if the apaquarto longtable
  overflows the text width at render, the fallback is trimming the Design column to
  study names only (the designs are fully stated in the setup paragraphs regardless).
  The render check happens before commit, per batch protocol.

## Proposed lead-in (S5-P1b prose)

> The correspondence between the derivations and the studies is collected in
> @tbl-evidence-map before the designs are stated: each row names a claim, the analytic
> result behind it, the study that tests it, and the outcome with the exhibit that
> reports it. A reader can treat the table as the section's map, and return to it from
> any single design or result.

## Proposed table

| Claim tested | Analytic basis | Study (design) | Result |
|---|---|---|---|
| The averaged log-likelihood overstates its complete-data counterpart by $\tfrac12\operatorname{tr}(\mathrm{RIV}) + (A){+}(C)$ | @thm-bias | Theorem validation: four-variate normal, non-monotone MAR, $N \in \{200,\ldots,2000\}$, analytic arm | pooled $2.43 \pm 0.26$, centered on the augmented band $2.42$ to $2.55$; the $N=1000$ cell is the one reported miss (@fig-w1-theorem) |
| Known-scale collapse: bias $0$ under deterministic FIML, $-\tfrac12\operatorname{tr}(\mathrm{RIV})$ under proper MI | @eq-knownscale | Known-scale run: mean-only fit, $N=200$, $2 \times 10^5$ repetitions | $0.025 \pm 0.018$ and $-0.536 \pm 0.018$ against targets $0$ and $-0.561$ (@fig-knownscale) |
| Imputing from the true model reverses the sign of the total | the conditioning fork at @eq-qbar | Sign-regime run: true-model imputation | the total reverses sign, as the fitted-versus-true-model distinction requires (reported with @fig-knownscale) |
| A calibrated reference absorbs the null bias, so correcting the numerator on top double-counts | @eq-spectrum-sum | Likelihood-ratio test: $H_0\!:\sigma_{12}=0$, $N=200$, $M=200$ | Type I error $0.042$ uncorrected and $0.034$ corrected, near the nominal $0.05$ (@fig-lrt-absorption) |
| The differential bias at the null is $\operatorname{tr}(\mathrm{RIV}_\perp)$, not the naive trace difference | @prp-lrt, @prp-naive | Formula discrimination: one coordinate $70$ to $79$ percent missing, $N \in \{500, 1000\}$ | $2.64 \pm 0.11$ and $2.70 \pm 0.11$ against the predicted $2.64$; the naive $8.5$ excluded at $52$ standard errors (@fig-discrimination) |
| Pairing holds the differential's noise at $O(1)$ | @prp-pairing | Pairing: $N \in \{500, 1000, 2000\}$, null, local, and fixed arms | null sd near $1.5$ and flat, against $18.4$ to $36.5$ for a single model; the fixed alternative reverts (@fig-pairing) |
| Uncorrected MI-AIC favors the largest-RIV candidate, and the trace correction restores selection | @thm-bias, @eq-ic-corrected | Selection sweep: four nested candidates, $60$ cells | $0.67$ uncorrected, $0.82$ corrected, benchmark $0.90$ at $N=500$; 100% of misclassifications on the largest-RIV candidate (@fig-w3-selection) |
| The null side calibrates map by map, and noncentral statistics shrink by predictable factors | the three maps of @sec-derivations | Distribution-matching ladder: three signal cells at $N=500$ | two-moment and equating arms reach $0.904$ and $0.903$ against the benchmark $0.899$; shrinkage $0.59$ and $0.36$ against predicted $0.56$ and $0.40$ (@tbl-ladder, @fig-ladder-internals) |
| Block-diagonal families fall at the equality case, and per-model maps cannot calibrate a difference | @prp-naive; the structural limits of @sec-derivations | Within the ladder cells | equality to $3.6 \times 10^{-15}$; naive-input cost $0.824$ against $0.904$; difference law $6.10$ and $5.99$ against $10.00$ and $7.10$ (@tbl-structural-limits) |
| The design-imbalance differential decouples only for separated candidates and grows with dissimilarity | @prp-ac-diff | Non-nested measurement: AR(1) truth, similar and dissimilar pairs, MCAR twins, $20{,}000$ repetitions | the dissimilar pair resolves at $-1.2$ ($3.5$ standard errors); the similar pair stays below resolution, the reported failure (@fig-w4-nonnested) |
| The bootstrap engine tracks the analytic arm, bounding the cost of not running data augmentation | the G3 scope statement of @sec-discussion | Engine sensitivity: the hardest non-monotone MAR cells | $\operatorname{tr}(\mathrm{RIV})$ within $2$ to $3$ percent; selection within $0.011$ |

Proposed caption: "**The studies of this section mapped to the claims they test.** Each
row names a claim from @sec-derivations, the analytic result behind it, the study that
tests it, and the outcome with its exhibit. {#tbl-evidence-map}"

## Invariance

Every cell restates facts and numbers already in the manuscript; all 27 numerically
distinctive values were verified verbatim against the current qmd before this proposal
was committed. No grade labels are asserted in the table (the text carries them), no
hedge is strengthened or weakened, and no new claim is introduced — the table is a
pure index. The failed predictions appear in it exactly as the text reports them (the
$N=1000$ miss; the similar-pair below-resolution result).

## Gate

Approve / amend (including the optional S4-P1 pointer). On approval: atomic script
adding S5-P1b (+ the S4-P1 clause if approved) → check_plan (structural gates on the
new unit) → rebuild → render (width check) → scouts → commit.
