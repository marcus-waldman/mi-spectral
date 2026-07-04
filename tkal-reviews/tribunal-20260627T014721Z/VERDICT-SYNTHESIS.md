# S5 tribunal — verdict synthesis

**Outcome: AMEND** (both cross-family examiners; no reject, no cannot_hit on any criterion).

## Process
- **R1 Challenge** — three cross-family examiners (openai, gemini, claude) independently converged on four blockers: W1 goalpost, block-diagonal luck, W3C=1.000 tautology, plus the uncongenial "hidden failure."
- **R2 Defense (harness)** — a defender with NO repository access conceded all 21 challenges by default. Discarded as uninformative.
- **R2' Defense (repo-grounded)** — re-run with repository access: recomputed numbers, commit dates, pre-registration text. See `defense-repo-grounded.md`.
- **R3 Press** — the two cross-family examiners (openai xhigh, gemini via DeepInfra) re-ruled on their own R1 challenges against the evidence. See `r3-press/`.

## What the evidence settled
- **W1 goalpost — estimate-chasing rebutted by both.** Pooled T-hat = 2.434 +/- 0.258 (recomputed in-session from the four committed W1-prod-fiml*.rds); 95% CI [1.93, 2.94] contains the pre-registered 2.774 (z = -1.32, not rejected). The O(1) (A)+(C) term is independently derived (Cox-Snell 08ee37b, 2026-06-01; 2 CAS + MC; value ~ -0.22 set by theory) and logged in dated Amendment 2 (2026-06-04). openai: "rebuts estimate-chasing/rejection." gemini: "the estimate-chasing charge is defeated."
- **Uncongenial/MNAR hidden failure — rebutted by both.** todo/005 registered H5 (uncongenial) and H2-MNAR as observational, "no required pass" (lines 100, 158). gemini fully WITHDREW; openai downgraded to a section-6 disclosure note.
- **Block-diagonal — general-superiority charge rebutted.** The equality is disclosed (S5-P20 table); "overstates elsewhere" is proved (prp-naive) and measured in Study 8 (trnaive 8.74 vs trperp 7.95). Residue: prose must not present the moment-map (naive-input) 0.824/0.904 gap as trace-formula evidence.
- **W3C=1.000 — artifact charge rebutted, scope concession kept.** Registered directional prediction (todo/005 H2) that held across all 60 cells; but in a nested RIV-ordered set the saturated endpoint is the natural overfit sink, so it confirms direction, not the specific decomposition.

## Per-criterion scorecard (worst-case across openai + gemini, post-press)
| Criterion | Status | Gating item |
|---|---|---|
| reproducible_numbers | at_risk (fixable) | Study 9 exact-row pointer (openai still-blocking); ncratio labels |
| claim_strength | at_risk (fixable) | W1 prose bridge (gemini still-blocking); two-sided interval + weak-cell conjecture label |
| mechanism_not_artifact | at_risk (fixable) | W3C direction-not-mechanism; localize 52-sigma |
| generic_not_lucky | at_risk (fixable) | S5-P20 decouple moment-map from trace-formula (gemini still-blocking) |

No criterion is cannot_hit. Every gating item is a local wording/scoping/auditability edit.

## Forced amendment list (the deliverable)
1. **S5-P22** — cite exact engine-sensitivity rows/cols for "2-3% / 0.011" or remove pending that. (only openai-blocking item)
2. **S5-P12** — declare the 2.77 anchor, then "consistent with (z = -1.3) and centered on the dated O(1)-augmented 2.42-2.55"; cite Amendment 2 + the derivation. (gemini-blocking until done)
3. **S5-P20** — decouple the 0.824/0.904 moment-map gap from trace-formula superiority; point the latter to prp-naive + Study 8. (gemini-blocking)
4. **S5-P17** — "direction not mechanism" rescope; note the registered prediction held across the sweep.
5. **section-6** — name the uncongenial overshoot (completes the pre-registered H5 disclosure).
6. **S5-P15** — localize the 52-sigma to the engineered cell; correctness rests on the 2.64 match.
7. **S5-P18/19** — two-sided interval for "indistinguishable"; conjecture-label the weak-cell attribution; resolve ncratio labels.

## Note on method
The harness tribunal's defender is a fresh model with no repository access; for a manuscript-vs-data review it concedes everything checkable. The informative run is: harness R1 challenges (cross-family) -> repo-grounded defense authored with artifact access -> cross-family press round on that defense. The two unanimous "blockers" were artifacts of the defender's information starvation, not the manuscript.
