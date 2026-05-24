# Comprehensive sweep verdicts (run_all out_suffix = prod)

Generated 2026-05-23 21:59:53

| Hypothesis | Verdict | Detail |
|---|---|---|
| H1 | FAIL | median monotone=+0.0977, non_monotone=+0.1467, diff=-0.0490 |
| H2_MAR | PASS | min W3-C=1.000, min W3-A=0.088 |
| H2_MNAR | observational | W3-A range [+0.093,+0.156] med +0.127; W3-C range [1.000,1.000]; mean param ||bias|| under MNAR=0.262 (max rel bias on sigma_24 = -13.2%) |
| H3 | PASS | W3-B shrinks: TRUE (0.101 vs 0.089); W3-A inv: max-min=0.014; W3-C all>=0.80: TRUE |
| H3b | observational (partial - rate=60% deferred) | monotone-in-rate: TRUE; mean ratio W3A(40%)/W3A(20%) = 3.11 (linear scaling predicts 2.0) |
| H4 | PASS | all MAR+cong cells satisfy W3-A(M=200) >= W3-A(M=20) - 0.02 |
| H5 | observational | median W3-A: cong=+0.117 uncong=+0.046; median W3-C: cong=1.000 uncong=1.000 |
| H6 | PASS | max |FIML - Amelia cong M=200| W3-A gap = 0.012 |
