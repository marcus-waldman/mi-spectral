# Comprehensive sweep verdicts (run_all out_suffix = prod)

Generated 2026-05-31 21:13:03

| Hypothesis | Verdict | Detail |
|---|---|---|
| H1 | FAIL | median monotone=+0.1075, non_monotone=+0.1557, diff=-0.0483 |
| H2_MAR | PASS | min W3-C=1.000, min W3-A=0.097 |
| H2_MNAR | observational | W3-A range [+0.095,+0.166] med +0.134; W3-C range [1.000,1.000]; mean param ||bias|| under MNAR=0.262 (max rel bias on sigma_24 = -13.2%) |
| H3 | PASS | W3-B shrinks: TRUE (0.093 vs 0.082); W3-A inv: max-min=0.017; W3-C all>=0.80: TRUE |
| H3b | observational (partial - rate=60% deferred) | monotone-in-rate: TRUE; mean ratio W3A(40%)/W3A(20%) = 3.25 (linear scaling predicts 2.0) |
| H4 | PASS | all MAR+cong cells satisfy W3-A(M=200) >= W3-A(M=20) - 0.02 |
| H5 | observational | median W3-A: cong=+0.126 uncong=+0.049; median W3-C: cong=1.000 uncong=1.000 |
| H6 | PASS | max |FIML - Amelia cong M=200| W3-A gap = 0.011 |
| INFO | observational (exploratory; todo/008) | ONE RIV (observed-data): E[A]~+tr_obs (max|A-tr_obs|=1.33), E[B]~-tr_obs/2 (max|B+tr_obs/2|=0.42); lemmas vs observed info L1 in [14.1,15.2] L3 in [13.8,14.2] (~k=14); info-eq tr(J O_obs^-1) in [13.9,14.5] (correct spec); naive RIV smaller: tr_obs-tr_exp in [0.45,0.87], Rubin tr_samp~tr_obs (max|tr_samp-tr_obs|=0.22) |
