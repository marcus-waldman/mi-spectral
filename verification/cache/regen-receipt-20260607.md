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

## Still outstanding before submission

W2 (`W2-lrt-power.R`) and W4 (`w4-nonnested-vuong.R`, `w4-dissimilar-vuong.R`) were
NOT part of this gate; they are preregistered originals with their own seeds. A
complete pre-submission reproducibility pass should regenerate them too and append
to this receipt.
