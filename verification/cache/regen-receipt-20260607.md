# Regeneration receipt — 2026-06-07

End-to-end reproducibility check of the committed simulation evidence, run on a
clean session before drafting `@sec-simulations`. This is the exercise behind the
manuscript's claim (`@sec-methods`, S3-P7) that *every number regenerates from
committed code*.

## What was run

| Entry point | Command | Wall clock | Exit |
|---|---|---|---|
| Comprehensive sweep | `Rscript verification/run_all.R 2000 regen all 20` | 241.7 min | 0 |
| IC calibration ladder | `Rscript verification/ic-ladder.R 2000 6 MAIN,WEAK,JUNK` | ~8 min | 0 |

Host: Windows 11, R 4.5.1, 20-core PSOCK cluster. Seeds are fixed in both scripts
(`ic-ladder.R`: 20260604+r, core-count-invariant). The sweep wrote to a fresh
`run_all-regen/` suffix so the canonical `run_all-prod/` evidence could not be
clobbered; the ladder overwrites its tracked outputs, so its fidelity was checked
by diffing against a pre-run snapshot and then restoring the committed files.

## Verdict: bit-identical modulo wall-clock timing

Every statistical quantity reproduced exactly. The only bytes that differ between
the committed caches and the regeneration are the per-cell `elapsed_sec` /
`elapsed` timing columns.

**Sweep (`run_all-prod` vs `run_all-regen`, per-phase summary CSVs):**

| Phase | Verdict |
|---|---|
| phase0 preflight tr(RIV) | bit-identical |
| phase1-w1 (bias decomposition) | bit-identical |
| phase2-w3 (60-cell selection) | identical modulo `elapsed_sec` |
| phase3-rate | identical modulo timing |
| phase4-mnar-bias | identical modulo timing |
| phase5 (aggregate) | identical modulo timing |
| phase6-info | bit-identical |
| phase7-rate-decay | bit-identical |

Spot check, W3 cell `fiml_non_monotone_MAR_N200`: pi_oracle 0.9065,
pi_uncorrected 0.6505, pi_corrected 0.806, pi_SB 0.809, W3C_n_miscl 699 —
identical in both runs (only elapsed_sec 88.58 -> 98.85).

**Ladder (`ic-ladder-summary.csv`, committed snapshot vs regeneration):**

All three cells identical on every statistic; only `elapsed` differs.

| Cell | oracle | uncorrected | mean | two-moment | equating | (manuscript table) |
|---|---|---|---|---|---|---|
| MAIN ρ=0.40 | 0.899 | 0.678 | 0.8135 | 0.9045 | 0.903 | matches |
| WEAK ρ=0.10 | 0.8195 | 0.582 | 0.650 | 0.6485 | 0.650 | matches |
| JUNK ρ=0    | 0.7265 | 0.4225 | 0.5845 | 0.7015 | 0.6955 | matches |

(The manuscript's `@sec-simulations` table rounds MAIN's oracle/mean to 3 places:
0.899 / 0.814; the ladder summary's 0.8135 rounds to 0.814.)

## Disposition

- `run_all-regen/` is a throwaway verification artifact, not committed (it is the
  copy that proves `run_all-prod/` regenerates).
- The ladder's tracked outputs were restored to their committed bytes with
  `git checkout` after the diff, so the repository continues to hold the
  evidence-of-record (timing churn discarded).
- Full run logs: `verification/cache/regen-runlog-sweep.txt`,
  `verification/cache/regen-runlog-ladder.txt`.

## W2 + W4 regeneration (appended 2026-06-08)

Run before drawing the `@sec-simulations` figures from `W2-prod-amelia.rds`,
`w4-nonnested-summary.csv`, and `w4-dissimilar-summary.csv`, so every W2/W4 exhibit
rests on gate-confirmed data. Driver: `verification/_regen-w2-w4.sh` (sequential, so
the 20-core cluster is never oversubscribed; snapshots the committed caches first).

| Entry point | Command | Wall clock | Exit |
|---|---|---|---|
| W2 LRT power | `Rscript verification/W2-lrt-power.R prod amelia 20` | 73 min | 0 |
| W4 non-nested | `Rscript verification/w4-nonnested-vuong.R 20000 20` | 44 min | 0 |
| W4 dissimilar | `Rscript verification/w4-dissimilar-vuong.R 20000 20` | 21 min | 0 |

**Verdict: every reported quantity reproduced; only environment churn differs.**

- **W2** — the full rejection table reproduced. The four reported rejection-rate
  columns (`C1_oracle`, `C2_corrected`, `C3_uncorrected`, `C5_SB`) are bit-identical
  across all eight `delta` rows (max abs diff 0). The null row is `0.040 / 0.034 /
  0.042 / 0.045`, matching the committed cache and the manuscript. The only difference
  anywhere in the object is `median_r_hat`, a diagnostic median the manuscript never
  reports, wobbling by `3.4e-5` (consistent with an imputation-package rebuild on this
  host).
- **W4 non-nested and dissimilar** — both summary CSVs are identical to the committed
  bytes except the `elapsed_sec` timing column. Every statistic (`resid`, `resid_se`,
  `D_pair`, `d_trperp`, the per-candidate `lvl_diag`/`lvl_ar`, the trace columns)
  reproduced exactly. The per-cell `.rds` files differ by 2-3 bytes each
  (high-precision serialization), with statistically identical content.

As for the ladder in the gate above, the tracked W2/W4 caches were restored to their
committed bytes with `git checkout` after the diff (timing and 3.4e-5 diagnostic churn
discarded); the repository keeps the evidence-of-record. The S5 figures
(`fig-lrt-absorption`, `fig-w4-nonnested`) are drawn from these gate-confirmed caches.

Note: the driver's optional `identical()` convenience check on the W2 `.rds` hit a
transient segmentation fault while the W4 cluster was still resident in memory; the
column-by-column comparison above was run separately and stands. Full log:
`verification/cache/regen-w2-w4-runlog.txt`.

## Still outstanding before submission

W1's preregistered originals (`W1-prod-fiml{,-N500,-N1000,-N2000}.rds`) back the lead
theorem-validation figure (`fig-w1-theorem`: pooled `2.43 ± 0.26`, target `2.77`, the
`N=1000` 2.6-se miss) and were NOT in either gate. They are deterministic analytic-FIML
runs, cheap to regenerate. Adding them would complete the pre-submission reproducibility
pass for every figure-bearing cache in S5.
