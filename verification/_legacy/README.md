# `_legacy/` — retired standalone scripts

These scripts have been superseded by the centralized `verification/run_all.R`
entrypoint. They are preserved here for traceability of the
comprehensive-sweep development history (2026-05-23) but **should not be
re-executed for new sweeps**.

For all new sweep work, use `verification/run_all.R`. See its top-of-file
header for usage and phase structure.

| Retired file | Replaced by |
|---|---|
| `00-test-ampute-vs-apply-mar.R` | `_modules/smoke-tests.R::run_smoke_tests()` |
| `W1-sweep.R` | `_modules/w1-sweep.R::run_w1_sweep()` |
| `W3-sweep.R` | `_modules/w3-sweep.R::run_w3_sweep()` |
| `W3-sweep-rate.R` | `_modules/w3-rate.R::run_w3_rate()` |
| `W3-sweep-rivs-preflight.R` | `_modules/smoke-tests.R::run_smoke_tests()` (incorporated into the pre-flight phase) |
| `W3-mnar-bias-measurement.R` | `_modules/mnar-bias.R::run_mnar_bias()` |
| `W3-sweep-summary.R` | `_modules/aggregate.R::run_aggregate()` |

**Originals kept in place at `verification/`:**
- `00-setup.R` — shared primitives.
- `00-test-primitives.R` — smoke tests for shared primitives.
- `W1-bias-decomposition.R`, `W2-lrt-power.R`, `W2-size-adjusted-power.R`,
  `W3-model-selection.R` — original preregistered W1/W2/W3 scripts at
  `todo/004-simulation-hypotheses.md` (frozen at SHA ddc9037).
