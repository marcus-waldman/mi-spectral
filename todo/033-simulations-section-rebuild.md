# todo/033 — Rebuild the Simulation studies section (S5)

**Status:** open (handoff). Created 2026-06-07.
**Target:** `manuscript/plan/level3-paragraphs.json`, section S5 (anchor `sec-simulations`).
**Blocks:** nothing downstream; S6 already points here. This is a quality rebuild of the
weakest section.

## Why

The current S5 (14 paragraphs, commit `8dcae96` + the D-03-A1 expansion) is the paper's
complete empirical account but it reads as a dense numbers-in-prose dump. Marcus's
direction (2026-06-07):

1. **Setup must read like a Methods, per individual simulation.** Not one shared
   apparatus paragraph followed by results. Each study group gets its own setup block
   stating, concretely: the data-generating model and its parameters, the sample
   size(s), the missingness pattern and mechanism and rate, the imputation engine and M,
   the number of Monte Carlo repetitions, the estimand/metric, and the pre-registered
   pass criterion. A reader should be able to reproduce the design from the paragraph.

2. **Results need tables and graphs, not prose.** Every headline comparison should be a
   figure or table, each carrying an explicit **reference marker for "perfect"** (the
   complete-data / oracle value, the nominal level, the analytic target) and a clear
   marker for **where we landed** (the corrected/measured value), so the gap is visual.
   Move numbers out of sentences and into exhibits.

3. **Impatient-reader test.** A reader must be able to jump straight to this section, or
   to a single plot, and understand it without having read S1-S4. Self-contained
   captions. Each figure says what it shows, what perfect looks like, and what we got.

## What the section currently carries (inventory to preserve)

All of these have committed artifacts (regeneration gate PASS, receipt
`verification/cache/regen-receipt-20260607.md`):

| Study | Key exhibit needed | Artifact |
|---|---|---|
| Theorem validation (W1) | E[T] vs the analytic 1/2 tr(RIV) target across N; show the N=1000 2.6-se miss + the 9-20% component misses; pooled 2.43+/-0.26 vs 2.42-2.55 | `run_all-prod/phase1-w1/summary.csv` |
| Sign-regime + known-scale | the four known-scale values vs {0, -1/2 tr(RIV)} targets within 4% | `rederivation-knownvar-N200-R20000.rds` |
| LRT absorption (W2) | null rejection 0.042 uncorrected / 0.034 corrected vs nominal 0.05 line | `W2-prod-amelia.rds` |
| Discrimination | observed differential vs the predicted 2.64 line and the naive 8.47 line; 52 se | `run_all-prod` |
| Pairing | sd(single) 18.4->36.5 vs sd(paired) flat ~1.5 across N — a 2-line plot | `run_all-prod` |
| Selection sweep (W3) | oracle 0.898 / uncorrected 0.674 / corrected 0.816 bars; 100% largest-RIV signature | `run_all-prod/phase2-w3/summary.csv` |
| Ladder (the headline table) | the 3-cell x 5-arm selection-rate table -> grouped bar chart with the oracle as the "perfect" reference line per cell | `ic-ladder-summary.csv` |
| Ladder internals | null-side KS 0.281->0.019, var ratio 3.18->0.97; noncentral shrinkage 0.586 vs 0.570, 0.362 vs 0.398 (measured-vs-predicted) | `ic-ladder-summary.csv` |
| Structural limits | naive-input arm 0.824 vs derived 0.904; difference-dist 6.10 vs 10.00 | `ic-ladder-summary.csv` |
| Non-nested (W4) | +2.5 level collapsing under MCAR; similar-pair BELOW resolution (the reported failure); dissimilar -1.2 at 3.5 se | `w4-nonnested-summary.csv` |
| Engine sensitivity | EMB vs observed-data RIV within 2-3%; selection within 0.011 | `run_all-prod` |

The reported FAILURES must stay prominent (D-05): the N=1000 W1 cell, the component-level
misses, the similar-pair W4 headline below resolution.

## Plan for the rebuild session

1. **Decide figure technology.** The repo is R-first. Options: (a) Quarto executable R
   chunks in the qmd that read the committed CSVs and draw with ggplot2 (live, but breaks
   the "qmd is compiled from JSON" model — figures would be code, not prose); (b) a
   standalone `verification/figures.R` that writes PNG/PDF exhibits into
   `manuscript/figures/`, committed, and S5 paragraphs `![caption](...)`-include them.
   RECOMMEND (b): keeps the compile-from-JSON model intact, figures are committed
   artifacts with their own provenance, and the impatient-reader captions live in the
   prose. Confirm with Marcus first.

2. **Restructure S5 into per-study blocks.** Replace the single Apparatus paragraph with
   one setup paragraph per study group (design + parameters + pass criterion), each
   immediately followed by its exhibit and a one-paragraph reading. This likely grows S5
   well past 14 paragraphs; that is expected and fine.

3. **Author the figures.** Each with: an explicit "perfect" reference (oracle line,
   nominal-level line, analytic-target line, or y=x for measured-vs-predicted) and the
   achieved value. Self-contained titles/captions. Colour/линetype legend that names
   oracle / uncorrected / corrected / the ladder arms.

4. **D-03-A1 still holds for S4.** Numbers stay OUT of the Derivations section; this
   rebuild is entirely within S5. Forward pointers in S4 already target `@sec-simulations`
   and `@fig-...`/`@tbl-...` anchors can be added.

5. **Update level4-evidence.json** for any new figure-bearing paragraphs; keep every
   exhibit pointed at its committed cache. Lint green; the prose punctuation gate
   (check_plan) now runs automatically.

6. **Pre-submission reproducibility rider (separate, noted in the receipt):** W2 and W4
   were NOT in the 2026-06-07 regeneration gate. Before the figures are final, regenerate
   `W2-lrt-power.R` and the W4 scripts and confirm the cached numbers, so the exhibits
   draw from gate-confirmed data.

## Constraints carried in

- Plain expository cadence + the punctuation budget (CLAUDE.md; now lint-enforced).
- "repetitions", never "replications" (T-07).
- Failures in the main text (D-05).
- The setup/results subhead split stays (D-09-A1): "Simulation studies: setup" /
  "Simulation studies: results" — but "setup" becomes per-study Methods blocks.
- compile_enabled still false; mi-spectral.qmd frozen until Marcus's per-paragraph passes.

## Preview tooling already in place

`manuscript/preview-jasa/` has the JASA extension installed and `build_preview.py`
(assembles a render-only qmd from level3 JSON). Re-run it to preview S5 with its new
figures. The dir is untracked/disposable.
