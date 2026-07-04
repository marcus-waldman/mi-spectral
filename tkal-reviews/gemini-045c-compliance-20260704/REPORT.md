# Compliance Validation Report

**Date:** 2026-07-04
**Model:** Gemini 3.1 Pro
**Branch:** da-engine-phase0-todo040
**Git Status:** clean
**HEAD SHA:** 5a918e5

## Axis Verifications

| Axis | Verdict | Evidence / Quote |
|---|---|---|
| **A1 (OBJ-01+09, disclosure)** | **VIOLATED** | §1 and §2 honor the intent with chronologically-first, rounded paraphrases (e.g., "+0.63 (se 0.16), about seven standard errors away and of the opposite sign"), which satisfy the spirit of the amendment within style guidelines. However, **§4 (todo/040 amendment)** violates the ordering and content requirement by placing the theoretical correction first ("the known-scale collapse requires a flat conditional missing-data entropy...") and omitting the measured values entirely (only stating they "were missed at $\approx 5$ and $\approx 7$ standard errors"). |
| **A2 (OBJ-02+06, claim strength)** | **HONORED** | §1: "The corrected target was then derived, not asserted... the known-scale collapse requires the family's conditional missing-data entropy to be flat..." §2: "After the miss we derived what a canonical-link model should show..." |
| **A3 (OBJ-03+07, attribution)** | **HONORED** | §1: "the $+0.85$ was Monte-Carlo noise at $R=1,000$ around a true value near $+0.52$, not a hidden term." (Standard errors included everywhere). |
| **A4 (OBJ-04+08, scope)** | **HONORED** | §1: "This addresses the trace penalty... and separately it closes the known-scale boundary result's non-normal gap with the Student-t exemplar." |
| **A5 (OBJ-10, shrinkage)** | **HONORED** | The term "shrink" (and its variants) does not appear anywhere in the staged rewrites. |
| **A6 (OBJ-11, timing separation)** | **HONORED** | §1: "The family selection was pre-registered; the theoretical target attached to it was not correct, and it was corrected only after the miss." |
| **A7 (numbers vs record)** | **HONORED** | Script outputs perfectly match the stated numbers: Bernoulli asymptote +0.518±0.012 at N=200, +0.512±0.037 overall; Poisson +0.113±0.027 vs +0.104; Bernoulli draw -0.313±0.070 vs -0.261; t-exemplar +0.025±0.049 and -0.483±0.049. |
| **A8 (chronology)** | **HONORED** | `git log` confirms `4aaeaae` strictly precedes `afa4438`, which precedes `bb5ebec` and `5b35192`. |
| **A9 (no overclaim)** | **HONORED** | §1: "The Gamma check stays a directional confirmation... Gamma's log link is not canonical..." Gate correctly summarized in §3 ("Mode A blind re-derivation + Mode B red-team"). |
| **A10 (open flag)** | **HONORED** | No additional substantive, presentational, or procedural blockers identified. |

## Script Outcomes

- `phase3-family-scan-score.R prod`: **PASS** (all checks pass, scorecard values match text).
- `verify_bernoulli_fitted_gap.py`: **PASS** (15 exact checks pass, numbers match).
- `verify_045b_escalations.py`: **PASS** (independent numerical routes agree, escalations closed).

## Required Fixes

1. **Rewrite §4 (`todo/045c` Section 4)**: The amendment to `todo/040` §9 currently introduces the theoretical correction before the miss and omits the measured values. It must be reordered to state the original targets (~0 FITTED, ~-0.5 draw) and the measured misses (including the actual values, e.g., +0.63 at 7 se) *before* explaining the entropy-gradient correction, in strict adherence to OBJ-01 and OBJ-09.

## Optional Suggestions

- Regarding A1 rounding: While the rounded values (+0.63, se 0.16) in §1 and §2 sufficiently convey the magnitude and severity of the miss per the manuscript's style, consider explicitly using the exact three-decimal values (+0.628, se 0.161) in the `todo/040` amendment (§4) since it is a registration document, not the main manuscript.

## Overall Recommendation

**FIX FIRST** (Fix the ordering and completeness of the `todo/040` amendment in §4).
