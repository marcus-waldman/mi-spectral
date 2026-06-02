# Todo 003 — Reference acquisition backlog

**Status:** Living document. New entries added whenever a paper is proposed during planning but not yet acquired.

## Why this exists

The PreToolUse citation hook prevents `@<citekey>` tokens from landing in `manuscript/` without a backing `literature/<citekey>.md`. That catches violations *at the edit*. But during planning/conversation Claude (or the human) often **proposes** papers by name from training knowledge — citations of intent, not yet citations of record. Without tracking, these proposals leak silently: by the time we draft a section, the question "did we ever acquire that?" gets lost.

This file is the running list of proposals through to either acquisition (paper enters Zotero → lit-sync → eligible for `@cite`) or rejection (we don't actually need it).

## Lifecycle

```
proposed ──► queued ──► acquired ──► verified ──► cited
              │
              └──► rejected (we decided we don't need it)
```

- **proposed** — first mentioned in conversation. Probably from Claude's training-weight knowledge. **Not yet citeable.**
- **queued** — confirmed we want to acquire. Added to Zotero `mi-spectral` collection (possibly as a stub `_needs-pdf` entry).
- **acquired** — PDF in `Google Drive/Literature/MI-SPECTRAL/`, Mathpix-converted, `literature/<citekey>.md` exists.
- **verified** — read in-session, the claim attributed to it has been checked against the actual text. **Eligible for citation per CLAUDE.md.**
- **cited** — actually appears as `@<citekey>` in `manuscript/`.
- **rejected** — examined and decided unnecessary; remove from active queue.

## Discipline

- Whenever Claude proposes a paper by name in conversation (e.g., "as in Ledoit-Wolf shrinkage"), **add a row to this table within the same session**, even if it's just `[proposed]` with a partial citation. Otherwise the proposal evaporates.
- The conversation entry should record: (a) what claim it was meant to support, (b) approximately where in the manuscript it would land, (c) whether it's a "must have" or "nice to have" for the paper.
- Promote `proposed → queued` only when a human (the user, not Claude) confirms acquisition.
- Once acquired, follow the normal acquisition pipeline (Zotero → migrate → index_papers → lit-sync). Then mark `acquired`.

## Active queue

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| Ledoit, O. & Wolf, M. — shrinkage estimation of covariance matrices | **rejected (subsumed by Lam 2019)** | — | — | — | Initially proposed 2026-05-22 from my training-weight knowledge. After Consensus search (2026-05-22, saved at `~/Google Drive/Literature/MI-SPECTRAL/_notes/consensus-regularized-covariance-2026-05-22.md`), decided Lam (2019) review is the single canonical citation. |
| Marchenko, V. A. & Pastur, L. A. (1967) | **rejected (subsumed by Lam 2019)** | — | — | — | Same — generic-phrasing decision plus Lam (2019) covers MP-based methods. |
| **Lam, C. (2019).** "High-dimensional covariance matrix estimation." *Wiley Interdisciplinary Reviews: Computational Statistics* 12. DOI: 10.1002/wics.1485 | acquired | **Single future-work citation** for the small-$M$ / $M \leq k$ regime. WIREs review covers all the families (structural, shrinkage, rotation-invariant, Bayesian/robust). | Discussion (§10) future-work paragraph | Medium | In `literature/lamHighdimensionalCovarianceMatrix2020.md`; in RAG. Treated as future-reference pointer only — no deep read needed. |
| **Chan, K. W. (2021).** "General and feasible tests with multiply-imputed datasets." *Annals of Statistics* (date as listed in Chan-Meng 2022 references; volume TBD — may have been published post-2022). | **cited** (`chanGeneralFeasibleTests2022`, 2026-06-01) | **Potentially closest predecessor to mi-spectral.** Chan-Meng (2022) explicitly cite this paper as "a possible remedy" for the EFMI-violation regime, which is precisely mi-spectral's target. **Must read before finalizing §1 contribution claims** — may reshape what we claim as novel, or in the worst case fully preempt our contribution. | §1 Introduction (lineage), C1–C4 framing, §7 Related Work | **High — read carefully** | Discovered 2026-05-22 in §2.3 of Chan-Meng (2022). Search hint: title is "General and feasible tests with multiply-imputed datasets" by Kwun Chuen Gary Chan, *Annals of Statistics*. Listed as "to appear" in 2022 references — actual publication may be late 2022 or 2023. Try Annals of Statistics archive or arXiv. **Update 2026-06-01:** acquired, read in-session, and verified by the derivation audit; now cited in `manuscript/derivation.qmd` (§1 lineage / LRT calibration). Complementary, not preempting — Chan calibrates the reference distribution; this work corrects the deviance numerator referred to it. |
| **Satterthwaite, F. E. (1946).** "An Approximate Distribution of Estimates of Variance Components." *Biometrics Bulletin* 2(6), 110–114. DOI: 10.2307/3002019 | queued (in Zotero, 2026-05-22) | **HIGH — anchor for moment-matching variance approximation.** Our scaled-shifted form $a\chi^2 + b$ is the two-moment Satterthwaite generalization. | §6 and §7 (introducing the correction); reviewers will demand this cite. | High | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Imhof, J. P. (1961).** "Computing the Distribution of Quadratic Forms in Normal Variables." *Biometrika* 48(3–4), 419–426. DOI: 10.1093/biomet/48.3-4.419 | queued (in Zotero, 2026-05-22) | Exact distribution of $\sum_j \lambda_j Z_j^2$ (generalized chi-squared) that our scaled-shifted approximates | §6 (defining the target distribution); V5/V6 witnesses for exact-vs-approximation comparison | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| **Davies, R. B. (1980).** "Algorithm AS 155: The Distribution of a Linear Combination of χ² Random Variables." *Applied Statistics* 29(3), 323–333. DOI: 10.2307/2346911 | queued (in Zotero, 2026-05-22) | Computational algorithm for generalized chi-squared distribution (Imhof alternative) | §6 if we discuss computational details of the exact reference distribution | Medium | User added to Zotero 2026-05-22. Pending: BBT re-export → migrate → index → lit-sync. |
| `claeskensconsentinoVariableSelectionIncomplete2008` | acquired (literature/) | Anchor citation for the block-diagonal decomposition of RIV under $(β, α)$ when $X$ has missingness | Discussion (§10), one sentence on the missing-covariates extension | Medium | Zotero key U3F5HN8W (also in MI-IC); markdown synced; in MI-SPECTRAL RAG. Not yet read in-session. |
| `consentinoclaeskensOrderSelectionTests2010` | **verified (cold-read 2026-05-22)** | Adjacent prior MI-testing work — omnibus order-selection lack-of-fit testing. **NOT a competitor for our headline.** They use Meng-Rubin's scalar-r F-reference as-is; no EFMI/anisotropy treatment; "order" in their sense ≠ our spectral order. | §7 Related Work, one sentence | Medium | Zotero key 9U4662KK; markdown synced; in RAG. Cited in body as adjacent literature; doesn't preempt any C1–C3 claim. |
| **Honaker, J., King, G. & Blackwell, M. (2011).** "Amelia II: A Program for Missing Data." *Journal of Statistical Software* 45(7), 1–47. | **proposed** | Canonical citation for the EMB (Expectation-Maximization with Bootstrapping) imputation algorithm used as the primary MI engine in `verification/`. Replaces `norm::da.norm` (Schafer 1997) after W1 pilot revealed `norm` was delivering systematically different posterior draws (Term 1 ~5× too small). | §3 (W1 implementation), §4 (W2 implementation), §5 (W3 implementation), §6 (Methods / Simulation Design) | High | Pilot validated 2026-05-22; engine swap committed at the corresponding pre-registration amendment. Need PDF acquisition + lit-sync before any `@honakerAmeliaIIProgram2011` citation in `manuscript/`. **2026-06-02:** user added the Amelia PDF to Zotero; pending BBT re-export → migrate → Mathpix convert → lit-sync. Now also the engine-ID citation for the approximate-Bayesian *limitation* note in `derivation.qmd` §sec-combine (todo/017 engine-sensitivity follow-up). |
| **Anderson, T. W. (1957).** "Maximum likelihood estimates for a multivariate normal distribution when some observations are missing." *Journal of the American Statistical Association* 52(278), 200–203. | **proposed** | Primary source for the closed-form MLE of $(\mu,\Sigma)$ under a **monotone/nested** ("missing observations") MVN pattern via the factored marginal × conditional likelihood — the construction underlying the per-step-regression decomposition needed for the **monotone** branch of $b_\Sigma = \lim n\,E[\hat\Sigma_{\text{obs}}-\Sigma]$ in (A)+(C). Anderson's textbook (owned) cites this exact paper for Problem 4.48 ("Missing observations") but gives **no estimator-bias result** — only the MLE construction. | §3 / Term-A derivation (monotone $b_\Sigma$ branch); Background lineage on monotone-pattern MLE | Medium | Surfaced 2026-06-01 while auditing Anderson 3rd ed for a reusable second-order Sigma-MLE bias under missing data. Textbook has only the exact complete-data result $E[\hat\Sigma]=\frac{N-1}{N}\Sigma$ (Thm 3.3.2) and CR bound; the monotone case is delegated to this 1957 paper as a "find the MLE" exercise. Acquire only if the monotone $b_\Sigma$ branch needs a primary citation for the factored-likelihood MLE; the *bias* itself is not in either source and must be derived. |

## Derivation-ledger references (proposed 2026-05-23)

Surfaced while mapping the formalized derivation ledger (explicit axioms / regularity
conditions / lemmas, each step tagged). Backbone already covered by the corpus above
(van der Vaart, Matrix Cookbook, Anderson, Meng 1994, Rubin 1976/1987, Schafer,
Little-Rubin, Cavanaugh-Shumway). These four are the gaps; the first two carry the
theorem's hard content (L2, L3).

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Louis, T. A. (1982).** "Finding the Observed Information Matrix When Using the EM Algorithm." *JRSS-B* 44(2), 226-233. | **proposed -> likely REJECT (subsumed by Schafer, owned)** | Missing-information principle `I_obs = I_com - I_mis|obs` (ledger D7) and score projection `E[U_com U_obs^T] = I_obs` (ledger L3). | §3 derivation (D7, L3); appendix ledger | Low | **Search 2026-05-23:** `schaferAnalysisIncompleteMultivariate1997` SS3 "The missing information principle" states D7 directly as eq (3.19) `I_c = I_o + I_m`, with the rigorous derivation and the interchange-of-differentiation regularity, and names Orchard-Woodbury (1972) / DLR (1977) / Louis (1982) / Meng-Rubin (1991a) as the primary sources. Schafer (owned) read in-session -> VERIFIED for D7. Cite Schafer; acquire Louis only if a reviewer wants the primary-source observed-information formula specifically. NOTE: Schafer's "fraction of missing information" D = I_c^{-1} I_m (EM rate) is NOT our RIV = I_obs^{-1} I_mis -- the ledger must define and relate the two (shared I_mis, different left factor). |
| **Hausman, J. A. (1978).** "Specification Tests in Econometrics." *Econometrica* 46(6), 1251-1271. | **proposed -> likely REJECT** | Efficient-estimator orthogonality -> `Var(theta_obs - theta_com) = I_obs^{-1} - I_com^{-1}` (ledger L2, the line where the -1/2 k bug hid). | §3 derivation (L2); appendix ledger | Low | **Search 2026-05-23:** van der Vaart Ch 11 (Projections) carries the needed machinery -- `cov(T, S_hat) = var S_hat` (md line 5147) and the Pythagorean rule for variances (line 5132), i.e. `var(T - S_hat) = var(T) - var(S_hat)` when `S_hat` is the projection. With the efficient estimator as the projection (efficiency chapter) + Louis (1982) missing-data specialization, L2 is grounded in owned material. Drop Hausman unless we want the one-line applied statement. |
| **Magnus, J. R. & Neudecker, H. (2019).** *Matrix Differential Calculus with Applications in Statistics and Econometrics*, 3rd ed. Wiley. citekey `magnusMatrixDifferentialCalculus2019` | **VERIFIED (acquired 2026-05-23)** | Duplication-matrix / `vech` identities and the MVN Fisher-information closed form via matrix calculus (ledger A8). | §3 (MVN instantiation); appendix ledger | Medium | **Search 2026-05-23 (re-checked broadly):** `petersen2008matrix` (Matrix Cookbook) HAS `vec` (full vectorization, Sec 10.2.2) + Kronecker/trace identities, but NOT `vech` (half-vec) or the duplication matrix `D_p` (no index entry; every "vec" hit is full vectorization). `anderson...2003` likewise lacks it (its 6 "duplication" hits are all the gamma-function formula). So the Cookbook covers A3-A5 (vec/Kronecker/trace) but not (Anderson's 6 "duplication" hits are all the gamma-function duplication formula). Needed ONLY IF the manuscript presents the MVN Fisher info in explicit `vech`/duplication form. The abstract theorem is parameterization-free and never touches `vech`; the MVN closed form is already verified numerically (Sympy notebook). Decision pending the §3 framing fork (explicit `vech` vs coordinate-free matrix form citing Anderson). **RESOLVED 2026-05-23 -> Option A (explicit `vech`).** Migrated (litrev) -> Mathpix-converted (47-pp excerpt) -> lit-synced to `literature/magnusMatrixDifferentialCalculus2019.md` -> read in-session. Confirmed: Ch 3 SS15 defines `vech` + duplication matrix `D_n` (`D_n vech(A)=vec A`, eq 23) and `(D_n'(A(x)A)D_n)^{-1}`; the MVN section derives the information matrix for `mu, vech(Omega)` as `n Omega^{-1}` and `(n/2) D_m'(Omega^{-1}(x)Omega^{-1})D_m` -- identical to our `fisher_info_com_mvn`. Eligible for `@magnusMatrixDifferentialCalculus2019`. |
| **Orchard, T. & Woodbury, M. A. (1972).** "A Missing Information Principle: Theory and Applications." *Proc. 6th Berkeley Symp.* | **proposed** | Original missing-information principle. | §3 / ledger provenance footnote | Low | Likely subsumed by Louis (1982) + Little-Rubin (2019). Acquire only if we want the primary-source attribution. |

## Methods/credibility references (proposed 2026-05-25)

Surfaced while discussing an IMRAD restructure: the manuscript needs an explicit
**Background** (demonstrated command of the lineage) and a **Methods** section that
houses the current §2 verification material *descriptively* rather than defensively.
For Methods to read as principled rather than idiosyncratic, the verification choices
(pre-registration, reproducibility layering, CAS check of LLM-generated algebra) should
sit in an established literature. None of the three veins below is in `literature/` yet;
all are training-weight proposals, **not citeable** until acquired + read in-session.
Citations are approximate and must be checked against the actual text.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Nosek, B. A., Ebersole, C. R., DeHaven, A. C. & Mellor, D. T. (2018).** "The preregistration revolution." *PNAS* 115(11), 2600–2606. | **proposed** | Grounds the "hypotheses frozen at SHA ddc9037 before simulation" claim in an established norm rather than an idiosyncratic choice — separates evidence from storytelling. | Methods (verification subsection); current §2 "predictions registered before data" paragraph | High | Approx. cite from training knowledge — verify authors/volume/pages. Pre-registration is the load-bearing norm for the W1/W2/W3 apparatus. |
| **Peng, R. D. (2011).** "Reproducible research in computational science." *Science* 334(6060), 1226–1227. | **proposed** | Grounds the three-layer reproducibility (IDEAS.md / run_all.R / caches) and the second-language re-implementation as recognized practice. | Methods (reproducibility subsection) | Medium | Canonical short citation for computational reproducibility. Verify before citing. |
| **AI-assisted-math / proof-verification reference (specific paper TBD)** — candidate veins: formal proof assistants (Lean/mathlib), or recent LLM mathematical-reliability work (e.g. a FrontierMath-style benchmark or an LLM-hallucination-in-reasoning study). | **proposed — needs scoping** | *The* load-bearing citation: justifies *why* an AI-assisted derivation specifically requires the CAS/symbolic check and the four-route triangulation. Turns the verification section from idiosyncratic to principled. | Methods (why-verify framing); current §2 opening | High | No specific paper chosen yet — needs a Consensus/Semantic Scholar pass to pick the right anchor. JAIGP audience makes this the citation most likely to be scrutinized. Acquire deliberately. |

## Finite-sample observed-vs-expected information (proposed 2026-05-30)

Surfaced while diagnosing the W1 finite-sample remainder (why $\hat B + \tfrac12\operatorname{tr}(\mathrm{RIV})$
sits ~10% from zero and does not visibly decay over $N=200\dots2000$). The
`verification/_scratch_b_diagnostic.R` triangulation showed three measurements of $\operatorname{tr}(\mathrm{RIV})$
at $N=500$ split into two camps: closed-form **expected**-information $=5.62$ vs.
numerical-Hessian **observed** $=6.13$ and Rubin between/within **sample-based** $=6.20$.
The $\hat B$ term tracks the observed/sample value, not the expected one — the classic
Efron–Hinkley distinction. This is now load-bearing for the W1 evidence (it reconciles
the theorem's expected-info $\mathrm{RIV}=I_{\text{obs}}^{-1}I_{\text{mis}}$ with the
sample-based $\mathrm{RIV}$ the operational correction actually subtracts).

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Efron, B. & Hinkley, D. V. (1978).** "Assessing the accuracy of the maximum likelihood estimator: Observed versus expected Fisher information." *Biometrika* 65(3), 457–487. | **verified (read in-session 2026-05-31; citekey `efronAssessingAccuracyMaximum1978`)** | The finite-sample W1 remainder: $\hat B$ tracks observed/sample-based $\operatorname{tr}(\mathrm{RIV})$ (≈6.2 at $N=500$), not expected-information (5.62); the ~10% gap is observed-vs-expected information. Grounds benchmarking the bias terms against the sample-based (Rubin between/within) $\operatorname{tr}(\mathrm{RIV})$ and reconciling it with the theorem's expected-info statement. | §3 (W1 numerical confirmation, finite-sample remainder); Methods/Discussion note on expected-info RIV (theorem) vs sample RIV (correction) | Medium–High | Surfaced 2026-05-30 via `_scratch_b_diagnostic.R`. Decomposition: the remainder is ~entirely the variance-identity term (ledger L2); Taylor + evaluation-point pieces vanish cleanly. Training-weight proposal — verify exact volume/pages before citing. Relates to the Hausman/L2 row above (the $\operatorname{Var}(\hat\theta_{\text{obs}}-\hat\theta_{\text{com}})=I_{\text{obs}}^{-1}-I_{\text{com}}^{-1}$ identity, which holds only asymptotically — Efron–Hinkley explains the finite-sample deviation). |

## Information-matrix distinction: J (score-variance) vs I (expected Hessian) (proposed 2026-05-31)

Surfaced when the user pointed to Pawitan's AIC derivation (§13.6, "Robustness of
likelihood specification"), which gives the penalty as $\operatorname{trace}(\mathcal{J}_k\mathcal{I}_k^{-1})$
with $\mathcal{J}=E[UU']$ (score variance / outer product) and $\mathcal{I}=-E[\partial^2\ell]$
(expected negative Hessian). Under correct specification $\mathcal{J}=\mathcal{I}$ (info
equality) and the trace = $k$ (ordinary AIC); under misspecification it is TIC. This is
the precise framework for our 2026-05-30/31 finding: B's $-\tfrac12\operatorname{tr}(\mathrm{RIV})$
weights the estimator-gap variance by the **curvature** $\mathcal{I}_{\text{com}}$ but we
substituted the **expected-information** gap variance $I_{\text{obs}}^{-1}-I_{\text{com}}^{-1}$
(an implicit $\mathcal{J}=\mathcal{I}$ assumption), whereas the gap's *actual* variance is the
sandwich/score-variance ($\mathcal{J}$-flavored) object — exactly the expected-RIV (5.5) vs
sample/observed-RIV (6.1) split. Our `fisher_info_{com,obs}_mvn` compute the $\mathcal{I}$
(expected-Hessian) version only; Rubin between/within and the numerical Hessian give the
$\mathcal{J}$/sandwich version. The derivation must say which information sits in each slot.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Pawitan, Y. (2001).** *In All Likelihood: Statistical Modelling and Inference Using Likelihood.* Oxford University Press. (§3.5 Lindsey AIC; §13.6 robustness, eq. for $\operatorname{trace}(\mathcal{J}_k\mathcal{I}_k^{-1})$ and (13.4).) | **verified (read in-session 2026-05-31; citekey `pawitanAllLikelihoodStatistical2013`)** | The $\mathcal{J}$ vs $\mathcal{I}$ distinction and $E[n(\hat\theta-\theta_0)'\mathcal{I}(\hat\theta-\theta_0)]\approx\operatorname{tr}(\mathcal{J}\mathcal{I}^{-1})$ — the framework clarifying which information enters tr(RIV); connects our IC application to TIC. | §setup (define both informations), §3.3 (expected-vs-sample RIV), §5 (IC↔TIC) | **High** | Verified in `literature/pawitanAllLikelihoodStatistical2013.md` §13.6: $\mathcal{J}\equiv E(UU')$ (L14618), sandwich $\mathcal{I}^{-1}\mathcal{J}\mathcal{I}^{-1}$ (L14696), **"model correct ⇒ $\mathcal{J}=\mathcal{I}$, reduces to $\mathcal{I}^{-1}$ naive"** (L14699), $\operatorname{trace}(\mathcal{J}\mathcal{I}^{-1})$ (L14707). Pawitan's $\mathcal{I}$=expected Hessian, $\mathcal{J}$=score variance — note convention (opposite of some texts). (Acquired edition is the 2013 printing → year in citekey.) |
| **Konishi, S. & Kitagawa, G. (1996).** "Generalised information criteria in model selection." *Biometrika* 83(4), 875–890. | **verified (read in-session 2026-05-31; citekey `konishiGeneralisedInformationCriteria1996`)** | TIC/GIC anchor: GIC = bias-corrected log-likelihood when "the parametric family does not necessarily contain the true distribution" (Thm 2.1) — the misspecification generalization of AIC's $k$ to a $\operatorname{tr}(\mathcal{J}\mathcal{I}^{-1})$-type penalty. | §5 (IC↔TIC lineage) | **High** | Chosen TIC anchor (accessible substitute for Takeuchi 1976). In `literature/`. |
| **Burnham, K. P. & Anderson, D. R.** *Model Selection and Multimodel Inference* (2nd ed.). Springer. | acquired (`literature/burnhamModelSelectionMultimodel2010.md`) | Textbook TIC discussion; secondary/optional given Konishi–Kitagawa is the primary anchor. | §5 (optional) | Low | Acquired + indexed. Cite only if a textbook-level TIC reference is wanted alongside KK. (litrev key year 2010; verify edition/year if cited.) |
| **Takeuchi, K. (1976).** "Distribution of informational statistics and a criterion of model fitting." *Suri-Kagaku* 153, 12–18 (in Japanese). | **superseded — not acquired** | Origin of TIC. | — | — | Hard to obtain (Japanese, 1976). Cite via Konishi–Kitagawa (1996, verified) instead; keep Takeuchi as a historical-origin mention only. |

## Observed-data information under MAR carries a mechanism-induced cross term (proposed 2026-05-31)

Surfaced via the rate-of-decay study (todo/008): the observed-vs-"expected" RIV gap does **not**
decay (it plateaus under MAR, vanishes under MCAR). Localized to a mean–covariance cross block
that our `fisher_info_obs_mvn` (block-diagonal, as-if-MCAR) omits. MCAR control + analytic
selected-Gaussian moment (`E[Xₖ|R1=1] ∝ b·Σₖ₃·inverse-Mills`) confirm: under MAR the selection
shifts per-pattern observed means, so `E[−∂²ℓ_obs]` has a real cross term. The decisive A-vs-RIV
check then showed **A and B both track the observed-data RIV** — one RIV, not two. **This retires
the Efron–Hinkley "finite-sample observed-vs-expected" interpretation** in the 2026-05-30 section
above: the gap is structural (MAR mechanism), not a vanishing finite-sample effect. `efron…1978`
stays in `literature/` but is no longer the right anchor for the W1 remainder.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Kenward, M. G. & Molenberghs, G. (1998).** "Likelihood Based Frequentist Inference When Data Are Missing at Random." *Statistical Science* 13(3), 236–247. (JSTOR 2676702) citekey `kenwardLikelihoodBasedFrequentist1998` | **verified (read in-session 2026-05-31)** | Canonical result that under MAR the **expected** information depends on the missingness mechanism, so the mechanism-free ("naive", block-diagonal) expected info is biased and the **observed** information should be used. Our MVN cross-term is a concrete instantiation. | §setup (which information defines RIV — cite for "use observed info under MAR"); retires the two-RIV/Appendix C reframing | **High — VERDICT: not novel** | **Resolved 2026-05-31.** §3.2 "Bivariate Gaussian Data" is our finding almost verbatim: their *naive* info $i_N$ = our block-diagonal `fisher_info_obs_mvn`; *unconditional* $i_U$ = correct expected info (with cross term); *observed* $i_O$ = `observed_info_obs_mvn`. Eqs (8)–(11): the mean×(co)variance cross-terms of $i_U$ "do not all vanish, and the orthogonality of mean and variance-covariance parameters is lost under the MAR mechanism"; vanish **iff** $\alpha_0=\alpha_1=0$ = MCAR. Their selection shift $E_{Y\mid R}(Y_{i2}-\mu_2)=\beta\alpha_1$, $\beta=\sigma_{12}\sigma_{11}^{-1}$ is our `E[X_k\mid R1] ∝ Σ_{k3}·(shift)` (they use logistic, we probit/inverse-Mills; same phenomenon). Abstract: "the classical expected information matrix is biased and the use of the observed information matrix is recommended." §5: "provided the observed information matrix is used, conventional likelihood based frequentist inference is applicable in the MAR setting." §4 (rats) also notes the off-diagonal block "has expectation zero but is likely to depart from this in small samples" — the Efron–Hinkley small-sample face, distinct from the structural MAR term. → **Cite K&M for the observed-info-under-MAR choice; the cross term is not our contribution.** Eligible for `@kenwardLikelihoodBasedFrequentist1998`. |

## Closed-form (A)+(C) cancellation for the MVN (proposed 2026-05-31)

For the **bivariate-monotone** closed-form `(A)+(C)=O(1/n)` (Item 2 of the audit follow-up,
derivation.qmd Appendix B/C), the literature is **already owned**: Little & Rubin (2019) §7.3
"Bivariate Normal Monotone Data: Small-Sample Inference" + §7.4.2 (factored likelihood for monotone
patterns) is the exact case; Anderson (2003) supplies the MVN MLE moments (`Σ̂` bias, unbiased `S`,
Cramér–Rao); Magnus (2019) the matrix-calculus/Gaussian-entropy algebra. No acquisition needed for
the monotone scope.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Cox, D. R. & Snell, E. J. (1968).** "A General Definition of Residuals." *JRSS-B* 30(2), 248–275. | **proposed — fork reached** (was CONDITIONAL; see the 2026-06-01 `b_Σ` pass below) | General second-order (O(1/n)) MLE bias `E[δ]` — the `αᵀE[δ]` piece of `(A)+(C)`. | derivation.qmd general-MVN `(A)+(C)`, **only if** scope is pushed to the *general non-monotone* MVN (the monotone case reuses Hyodo/Kanda–Fujikoshi closed forms instead). | High if general-scope, else defer | Vol/pages confirmed 2026-06-01. The general non-monotone `b_Σ` has **no published formula**; Cordeiro & Klein (1994) gives the matrix/vec form valid under non-independence; Patriota & Lemonte (2008) is the MVN execution template. Full reuse-vs-derive log in the 2026-06-01 section below. |

## Term-A MAR correction — novelty check (2026-05-31)

The Term-A imputation/design-imbalance bias `(A)+(C) = (n_mis/n_obs)[1 − ½tr(Q_mis Q_obs⁻¹)]`
(nonzero under MAR, zero under MCAR; todo/008) is a candidate **contribution** — a deviance/AIC
correction beyond the RIV/FMI penalty. Consensus search (2026-05-31, saved verbatim at
`literature/consensus-searches/AIC_bias_correction_multiple_imputation_MAR_2026-05-31.md`,
queries: "AIC bias correction multiple imputation MAR expected log-likelihood" + alternates)
found **no direct predecessor** — hits are (i) general AIC-as-bias-corrected-expected-loglik,
(ii) structural/small-sample AIC refinements, (iii) *using* AIC/BIC to select the imputation model
(the reverse problem). None has a bias depending on the missing-vs-observed covariate distribution.
Supports novelty, **but the broad search missed the three closest candidates** — check these
specifically before any novelty claim:

| Proposed citation | Status | Claim it supports / role | Priority | Notes |
|---|---|---|---|---|
| **Shimodaira, H. (1994).** "A new criterion (RIC) for selecting models from partially observed data." (in *Selecting Models from Data: AI and Statistics IV*, Springer) | **proposed — HIGH (closest possible predecessor)** | Penalized expected-log-likelihood / AIC-type criterion for *partially observed* data — the most likely prior art for a Term-A-style correction. Must read before claiming novelty. | **High** | Not in bib; not surfaced by Consensus. Acquire via Zotero → migrate → index → lit-sync. Verify exact title/venue/pages. |
| **Cavanaugh & Shumway (1998)** — `cavanaughAkaikeInformationCriterion1998a` (OWNED) | re-examine | AICcd (complete-data discrepancy, EM). **Re-read to check whether its correction is MCAR-implicit or already carries a MAR design-imbalance term** — decides whether our Term-A term is genuinely new vs a special case. | High | Owned in `literature/`; just needs an in-session re-read with this question. |
| **Claeskens & Consentino (2008)** — `claeskensconsentinoVariableSelectionIncomplete2008` (OWNED) | re-examine | Missing-covariate AIC. Check whether the missing-covariate correction includes the design-imbalance term. | Medium | Owned; re-read with this lens. |

## Shimodaira prior art — found in MI-IC database, flips the novelty picture (2026-05-31)

The broad Consensus search (above) missed the actual predecessor cluster, which IS in the MI-IC
litrev database (`mcp__litrev__search_papers`). Read via RAG passages — **needs full read + sync to
`literature/` before any contribution claim.** These bear on the novelty of the *whole* deviance-bias
result, not just the Term-A MAR term.

| Proposed citation | Status | Why it matters | Priority | Notes |
|---|---|---|---|---|
| **Shimodaira, H. & Maeda, H. (2017).** "An information criterion for model selection with missing data via complete-data divergence." *Ann. Inst. Statist. Math.* (citekey in MI-IC: `shimodairaInformationCriterionModel2017`) | **proposed — CRITICAL** | Shows PDIO/AICcd penalty `2·tr(RIV)` is **biased**; correct penalty (weaker assumption) is **halved to `tr(RIV)`** = our net correction. Their strong assumption (22) `q̂_x = p_{z\|y}(θ̂_y)q̂_y` **is FIML imputation (our barQ)**. Our core IC result may coincide with their `AIC_{x;y}`. | **Critical — read fully** | In MI-IC database/bib, NOT in mi-spectral `literature/`. Sync (Zotero→migrate→index→lit-sync) + read. |
| **Shimodaira, H. (2000).** "Improving predictive inference under covariate shift by weighting the log-likelihood function." *J. Stat. Plan. Inf.* (`shimodairahidetoshiImprovingPredictiveInference2000`) | **proposed — HIGH** | Covariate shift (observed vs population covariate distribution) = structurally our `Q_mis≠Q_obs` Term-A imbalance. Possible home for the MAR term. | High | In MI-IC db. Sync + read. |
| **Hens, N., Aerts, M. & Molenberghs, G. (2006).** weighting complete cases by inverse selection probabilities for IC under missingness (via Claeskens–Consentino 2008) | **proposed — Medium** | Horvitz–Thompson-style correction for the selection/design imbalance — another route to the MAR term. | Medium | Find exact cite via Claeskens–Consentino (owned). |

**Positioning questions to settle from the full reads (affects mi-spectral AND MI-IC):**
1. Is our net `tr(RIV)` correction identical to Shimodaira–Maeda's `AIC_{x;y}`? If so, our novelty is the *decomposition* (Term A/B), the *K&M observed-info RIV under MAR*, and the *MI/posterior-draw* generality — not the penalty.
2. Is the **Term-A MAR `(A)+(C)` design-imbalance term** within Shimodaira–Maeda's framework (looks fixed-pattern/iid → maybe MCAR-implicit) or genuinely beyond it? Shimodaira (2000) covariate-shift is where it might already live.
3. MI-IC cites `@shimodaira1994` (PDIO, `2tr(RIV)`) — does it position against the **2017** halved result? Both papers' framing may need updating.

## Phase-1 novelty gate — VERDICT (2026-06-01, full in-session reads)

Read in full in-session: Shimodaira–Maeda (2017), Shimodaira (2000), Cavanaugh–Shumway (1998),
Claeskens–Consentino (2008). Question: is the **Term-A MAR `(A)+(C)`** design-imbalance term
(`(n_mis/n_obs)[1−½tr(Q_mis Q_obs⁻¹)]`, 0 iff MCAR) precedented?

**Branch A (proceed) — no owned predecessor carries `(A)+(C)`:**

| Paper | Status now | Verdict |
|---|---|---|
| `shimodairaInformationCriterionModel2017` | **verified** | Net `tr(RIV)` penalty = their `AIC_{x;y}` (precedent — cite, don't claim). Their "O(1) Q-deviance bias" is the *imputation-estimation* effect in an i.i.d. fixed-pattern setup with no MCAR/MAR switch — cannot form `Q_mis≠Q_obs`. §8 names "combine a missing mechanism with covariate shift (Shimodaira 2000)" as **future work** = our slot. |
| `shimodairahidetoshiImprovingPredictiveInference2000` | **verified** | Covariate-shift `q0≠q1` + IPW reweighting is the *conceptual home*, but covariates fully observed, no missing-data instantiation, no `(A)+(C)`. |
| `cavanaughAkaikeInformationCriterion1998a` | **re-examined** | Targets complete-data discrepancy (like us); penalty **`2tr(RIV)`** (doubled). Derivation **assumes the term away** via `Q(θ_o\|θ̂)≈Q(θ_o\|θ_o)` (eqs 3.15–3.16); sims are **MCAR** (fixed discard probs) ⇒ `(A)+(C)=0`. Neither derives nor could observe it. |
| `claeskensconsentinoVariableSelectionIncomplete2008` | **re-examined** | Targets the EM-**adjusted**-likelihood KL (`f̃=exp Q`), not complete-data divergence; penalty `tr(JI⁻¹)`→`p` (NO `tr(RIV)`); bias is clean **O(1/n)** TIC optimism. MAR sim *does* have covariate-dependent missingness, but `(A)+(C)` doesn't enter their target. Flag the Q-vs-L entropy distinction as unresolved future work (App., near eq A.2). |

**Conclusion:** `(A)+(C)` is novel vs all four. Proceed (Branch A). MI-IC already implements 1×`tr(RIV)`
(`compute_ic.R:37`) but doesn't cite Shimodaira–Maeda 2017 — citation/shared-finding coordination, not a
penalty-correctness fix.

**Residual gate item (acquire before the final novelty claim):**

| Paper | Status | Why it's the last gate |
|---|---|---|
| **Hens, N., Aerts, M. & Molenberghs, G. (2006).** "Model selection for incomplete and design-based samples." *Statistics in Medicine* 25, 2502–2520. **DOI 10.1002/sim.2559** (PMID 16596577). | **VERIFIED — read in-session 2026-06-01; GATE CLOSED → Branch A confirmed** (citekey `hensModelSelectionIncomplete2006a`) | **Does NOT carry `(A)+(C)`.** Complete-case + IPW (Horvitz–Thompson) reweighted AIC: `AIC_W = -2Σ(δ_i/π_i)log f + 2K`. Same *goal* (model best describing the hypothetically complete data, §6) and they diagnose the same MAR selection-imbalance bias (CC-KL minimum shifts by `Cov(y_i,π_i)/E{π_i}`, eqs 10–11), but the *mechanism* is reweighting (needs estimated π_i), penalty stays `2K` — **no `tr(RIV)`, no closed-form deviance term**. §6 names "explicit imputation-based AIC" as an *obvious alternative / topic of current research* and uses the **naive `2K`** for it (= the uncorrected MI-AIC our framework corrects). → **Cite as the IPW alternative route + the paper that flagged the imputation-IC gap we fill; `(A)+(C)` is novel.** |

**New proposals — proper-MI generalization layer (Phase 3b):**

| Paper | Status | Claim it supports |
|---|---|---|
| **Wang, Naisyin & Robins, J. M. (1998).** "Large-sample theory for parametric multiple imputation procedures." *Biometrika* 85(4), 935–948. **DOI 10.1093/biomet/85.4.935**. | **proposed**; **DOI verified via litrev Semantic Scholar + S2 Graph API 2026-06-01** | Proper-vs-improper MI large-sample variance; the posterior-draw (Rubin) layer beyond the EM plug-in `barQ_∞`. |
| **Nielsen, Søren Feodor (2003).** "Proper and Improper Multiple Imputation." *International Statistical Review* 71(3), 593–607. **DOI 10.1111/j.1751-5823.2003.tb00214.x**. | **proposed**; **DOI verified via litrev Semantic Scholar + Crossref 2026-06-01** | Canonical proper-vs-improper MI distinction; grounds "the `½tr(RIV)` result transfers EM→proper MI." (Nielsen 2000 *Bernoulli* already cited by Claeskens–Consentino.) |

## (A)+(C) closed form: second-order MVN covariance MLE-bias `b_Σ` literature pass (2026-06-01)

Resolves the "don't reinvent the wheel" search for `b_Σ = lim n·E[Σ̂_obs − Σ_0]` (the Σ-block
second-order FIML MLE bias under missing data; only the Σ-block matters because the entropy gradient
`α` is covariance-only). 9-agent litrev/consensus/web/owned-corpus pass (todo/010 task).
**Verdict: monotone = REUSE; general non-monotone = DERIVE (no published formula exists).**

**Monotone branch — reusable closed forms exist:**

| Proposed citation | Status | Role for `b_Σ` | Priority | Notes |
|---|---|---|---|---|
| **Hyodo, M., Shutoh, N., Seo, T. & Pavlenko, T.** "Estimation of the large covariance matrix with two-step monotone missing data." (`hyodoestimation`) | **cited** (2026-06-01, `§sec-termA`) | Explicit 2-step monotone MLE of every Σ-block (Anderson–Olkin form) AND an exactly-unbiased estimator (Lemma 2.1) with explicit divisors ⇒ `b_Σ = lim N·(MLE − unbiased)` blockwise. Confirms the per-step regression-residual-variance bias hypothesis against printed divisors. | **High** | Synced + **verified in-session 2026-06-01**: `literature/hyodoestimation.md` Sec. 2 carries the Anderson–Olkin MLE + Lemma 2.1 unbiased pair with explicit divisors. (Synced markdown is the Hiroshima TR13-05 version; same Sec-2 content as the published Comm. Stat. paper.) |
| **Kanda, T. & Fujikoshi, Y. (1998).** "Some Basic Properties of the MLEs for a Multivariate Normal Distribution with Monotone Missing Data." *Amer. J. Math. & Mgmt. Sci.* 18(1–2), 161–190. DOI 10.1080/01966324.1998.10737458 (`kandaBasicPropertiesMles1998`) | **cited** (2026-06-01, `§sec-termA`) | EXACT bias of Σ̂ for k=2,3-step monotone (on Σ̂ directly — the abstract distinguishes this from the transformed Δ used only for the general-k construction); asymptotic expansions for general k. | High | Synced + **verified in-session 2026-06-01**: `literature/kandaBasicPropertiesMles1998.md` Theorem 2.2 gives the exact `E[Σ̂]` bias (k=2); abstract confirms k=2,3. |
| **Anderson, T. W. & Olkin, I. (1985).** "Maximum-likelihood estimation of the parameters of a multivariate normal distribution." *Lin. Alg. Appl.* 70, 147–171. | **proposed — Medium** | Primary source of the explicit 2-step monotone MLE construction (the estimator whose bias we take). | Medium | Pairs with Kanda–Fujikoshi (bias) and Anderson (1957) (factorization origin). |
| **Tsukada, S. (2014, two-step; 2019, three-step).** Unbiased estimator for a covariance matrix under monotone incomplete sampling. *Comm. Stat. — Theory & Methods* / *Lin. Alg. Appl.* | **proposed — Medium** | Independent corroboration: Σ MLE biased under monotone, UBE derived ⇒ bias = MLE − UBE; k-step pattern. | Medium | Corroborates Hyodo; secondary. |

Owned + already sufficient for the monotone scaffold (no acquisition): L&R (2019) §7.4.2 sweep
factorization; Schafer (1997) §6.5 `φ_j` regression factorization; Anderson (2003) Thm 3.3.2
complete-data baseline `E[Σ̂]=((N−1)/N)Σ`; Pawitan (2013) §5.2 `b₁/n+…` form + normal-variance
`−σ²/n`; Magnus (2019) §18.6/18.15/18.16 — confirms `α` and `𝓗` are fully mechanical (no gap).

**General non-monotone branch — NO published formula; DERIVE via Cox–Snell machinery:**

| Proposed citation | Status | Role | Priority | Notes |
|---|---|---|---|---|
| **Cox, D. R. & Snell, E. J. (1968).** JRSS-B 30(2), 248–275. DOI 10.1111/j.2517-6161.1968.tb00724.x (`coxGeneralDefinitionResiduals1968`) | **cited** (2026-06-01, `§sec-termA` scope note) | The general O(1/n) MLE-bias engine (cumulant form). Apply to the observed-data FIML MVN log-likelihood (does not factor under non-monotone). | High (if general scope) | Synced + **verified in-session 2026-06-01**: the canonical second-order MLE-bias formula (reproduced as eq. (1) in Cordeiro–Klein 1994). |
| **Cordeiro, G. M. & Klein, R. (1994).** "Bias correction in ARMA models." *Stat. & Prob. Lett.* 19(3), 169–176. DOI 10.1016/0167-7152(94)90100-7 (`cordeiroBiasCorrectionARMA1994`) | **cited** (2026-06-01, `§sec-termA` scope note) | The matrix/vec form of Cox–Snell **valid under non-independence** — the right tool since non-monotone observed-data contributions are pattern-mixed (heterogeneous), not iid. | High | Synced + **verified in-session 2026-06-01**: general matrix formula for second-order MLE bias of structured-covariance (non-iid) models, depending on V, V⁻¹ and first/second derivatives. |
| **Patriota, A. G. & Lemonte, A. J. (2008).** "Bias correction in a multivariate normal regression model with general parameterization." *Stat. & Prob. Lett.* (`patriotaBiasCorrectionMultivariate2009`) | **acquired** (`literature/patriotaBiasCorrectionMultivariate2009.md`, 2026-06-01) | Closest concrete TEMPLATE: second-order biases of MLEs in a general MVN model with shared (μ,Σ) parameters, executed via weighted-least-squares regressions. Complete-data; adapt to the FIML observed-data score/info. | High | The "how to execute Cox–Snell for the MVN" template. Synced; not yet read in-session — needed for the non-monotone Phase D derivation. |
| **Cordeiro, G. M. & McCullagh, P. (1991).** JRSS-B 53(3), 629–643. DOI 10.1111/j.2517-6161.1991.tb01852.x | **proposed — Medium** | Matrix `b₁` (supplementary-weighted-regression) template; GLM-specific, structural model only. | Medium | Authority for the matrix-form bias representation. |
| **`mle.tools` (Mazucheli, Menezes & Nadarajah, 2017).** *R Journal.* `coxsnell.bc()`. | **proposed — Low** | Numerical cross-check of a derived `b_Σ` against the Cox–Snell formula. | Low | Validation only. |
| **"Expectations and Variances of MLEs of the MVN Parameters with Missing Data"** (authors/year unresolved; S2 paperId `96e04824eb867caf238d86ae471634d18a14f3f9`). | **proposed — INVESTIGATE** | Title literally promises `E[Σ̂]` under missing data = `b_Σ`. If its missingness is **general** (not just monotone) and it states the closed form, it could upgrade the general branch DERIVE→REUSE. | High to triage | S2 metadata returned null; resolve authors/year + acquire to verify monotone-vs-general before relying on it. |

**Correctly excluded (information-not-bias trap):** Kenward–Molenberghs (1998, owned), Hocking–Smith
(1968), Touloumi (2003), Tan (2014), Hyodo's shrinkage angle — all about the asymptotic
variance/information of the estimators, not `E[Σ̂]−Σ`.

### Verbatim claim-check for the four `§sec-termA` `@cite`s (in-session read 2026-06-01)

Recorded so the claim attribution is auditable (CLAUDE.md citation discipline). Each quote is the exact
backing passage from the synced `literature/<citekey>.md`.

- **`hyodoestimation`** — claim: *explicit 2-step monotone MLE (Anderson–Olkin form) + exactly-unbiased
  estimator.* Sec. 2: "From Anderson and Olkin (1985), we can express the MLE's μ̂ and Σ̂ as follows …
  $\hat\Sigma_{11}=\frac1N(W_{11}^{(1)}+W^{(2)})$, $\hat\Sigma_{12}=\hat\Sigma_{11}(W_{11}^{(1)})^{-1}W_{12}^{(1)}$,
  $\hat\Sigma_{22}=\frac1{N_1}W_{22\cdot1}^{(1)}+\hat\Sigma_{21}\hat\Sigma_{11}^{-1}\hat\Sigma_{12}$."
  Lemma 2.1: "Let $\hat\Sigma_1$ and $\hat\Sigma_2$ be defined as … Then $\mathrm{E}[\hat\Sigma_1]=\mathrm{E}[\hat\Sigma_2]=\Sigma$"
  (with explicit divisor $b_1=\frac1{N_1-p_1-1}(1-\frac{p_1}{N-1}-\frac{N_2p_1}{(N-1)(N_1-p_1-2)})$).
- **`kandaBasicPropertiesMles1998`** — claim: *exact bias of Σ̂ for k=2,3.* Abstract: "For $k=2$ and 3,
  we obtain the exact means and variances of $\hat\mu$ and the exact bias of $\hat\Sigma$." Theorem 2.2(i):
  "$\mathrm{E}[\hat\Sigma]=\frac{N-1}{N}\Sigma+\begin{pmatrix}O&O\\O&\frac{b_0}{N}\Sigma_{22\cdot1}\end{pmatrix}$,
  $(N_1>p_1+2)$, where $b_0=-\frac{N_2\{N_1-(p_1+1)(p_1+2)\}}{N_1(N_1-p_1-2)}$."
- **`coxGeneralDefinitionResiduals1968`** — claim: *general O(1/n) MLE-bias engine (cumulant form).*
  §3, eq. (20): "$b_s\equiv E(\hat\beta_s-\beta_s)=\frac12 I^{rs}I^{tu}(K_{rtu}+2J_{t,ru})$ … which is
  of order $n^{-1}$" (with $I_{rs}=E(-V_{rs}^{(.)})$, $J_{r,st}=E\{\sum U_r^{(j)}V_{st}^{(j)}\}$,
  $K_{rst}=E(W_{rst}^{(.)})$). Read from the Cox–Snell source directly, not via Cordeiro–Klein's reproduction.
- **`cordeiroBiasCorrectionARMA1994`** — claim: *matrix/vec form of Cox–Snell valid under non-independence.*
  Abstract: "We give a general matrix formula for computing the bias of the exact unconditional maximum
  likelihood estimate in ARMA models … up to order $1/n$." §2: "(1) continues to be valid for
  non-independent observations provided that all $k$'s are $\mathrm{O}(n)$, as is the case for ARMA models."

## Foundational references verified during the 2026-06-01 derivation audit

Cited in `manuscript/derivation.qmd` and confirmed real + synced + read-in-session by the
2026-06-01 `/derivation-audit`, but not previously logged in any lifecycle table (they predate the
proposal workflow — Phase-1 corpus). Recorded here so the lifecycle is complete.

| Citation | Status | Role | Notes |
|---|---|---|---|
| `littleStatisticalAnalysisMissing2019` | **cited** | Foundational MAR/MI text; monotone sequential-regression factorization (joint cite with Anderson/Schafer) | Synced + verified in-session, 2026-06-01 audit. |
| `rubinInferenceMissingData1976b` | **cited** | MAR / ignorability foundations (D2, R3) | Synced + verified in-session, 2026-06-01 audit. |
| `andersonIntroductionMultivariateStatistical2003` | **cited** | MVN Gaussian-conditional / Schur complement (`@sec-alg`); Term-A normal Q-function | Synced + verified in-session, 2026-06-01 audit. |

## Imputation-engine properness limitation (proposed 2026-06-02)

Follow-up to the todo/017 engine-sensitivity verdict (NOT SENSITIVE, EMB/Amelia ≈ analytic). The user
asked to acknowledge in the manuscript that, although we see no sensitivity, the EMB/Amelia engine is
**not Bayesianly proper in Schafer's sense** — its bootstrap is only an *approximate* posterior (Little
& Rubin describe resampling-based imputation as approximately Bayesian / large-sample, with small-sample
behaviour "questionable"). The limitation note in `derivation.qmd` §sec-combine has already been landed
with the **owned/backed** citations (`@littleStatisticalAnalysisMissing2019` §5.5 + `@schaferAnalysisIncompleteMultivariate1997`);
the two references below are the canonical engine-ID and DA-origin cites to **add to that note once acquired**.

| Proposed citation | Status | Claim it supports | Where it would land | Priority | Notes |
|---|---|---|---|---|---|
| **Honaker, J., King, G. & Blackwell, M. (2011).** "Amelia II: A Program for Missing Data." *JSS* 45(7). | **cited** (`@honakerAmeliaIIProgram2011`, 2026-06-02) | Identifies the engine actually used (EMB = EM-with-bootstrap) and that its posterior is a bootstrap approximation — the subject of the limitation note. | `derivation.qmd` §sec-combine limitation note ("the EMB sampler") | High | Migrated → Mathpix → lit-synced → **verified in-session 2026-06-02**: p.1 "Amelia II draws imputations … the EMB (expectation-maximization with bootstrapping) algorithm … uses the familiar EM algorithm on multiple bootstrapped samples … to draw values of the complete-data parameters." Cited. |
| **Tanner, M. A. & Wong, W. H. (1987).** "The Calculation of Posterior Distributions by Data Augmentation." *JASA* 82(398), 528–540. (with discussion) | **cited** (`@TannerCalculationPosteriorDistributions1987`, 2026-06-02) | Seminal data-augmentation source — the exact-posterior MCMC alternative to the bootstrap, alongside Schafer (1997, MVN application). | `derivation.qmd` §sec-combine limitation note ("proper data augmentation") | High | Migrated → Mathpix → lit-synced → **verified in-session 2026-06-02**: abstract + §1 give the iterative exact-posterior algorithm with convergence proof "under mild regularity conditions"; §3 applies it to "the covariance matrix of the multivariate normal distribution with missing values." Citekey **normalized 2026-06-02** from the litrev override `Tanner01061987` to `TannerCalculationPosteriorDistributions1987` (user refreshed the BBT key + re-exported; re-synced; orphaned `Tanner01061987.md` removed; cite swapped in `derivation.qmd`). |

## Recently rejected (kept as a record so we don't re-propose)

- **2026-05-22 — Wood, A. T. A. (1989).** "An F approximation to the distribution of a linear combination of chi-squared variables." *Comm. Stat. — Simul. Comp.* 18(4), 1439–1456. DOI: `10.1080/03610918908812585`. Reason: We're sticking with χ² reference (not F), so the F-approximation is not load-bearing. Citation lineage for the scaled-shifted moment-matching form is already covered by Satterthwaite (1946) + Satorra-Bentler (2010) + Asparouhov-Muthén (2006). Imhof (1961) + Davies (1980) cover the exact reference distribution. Full text was also not freely available, which would have been a small acquisition cost — combined with non-load-bearing status → reject. Re-propose only if we change framing to F-reference.
- **2026-05-22 — Ledoit & Wolf (specific paper TBD)** and **Marchenko & Pastur (1967).** Reason: Subsumed by Lam (2019) review which covers the same ground in one citation. See proposed entry above.

## Recently promoted to `literature/` (kept as a record)

- **2026-05-22:** `claeskensconsentinoVariableSelectionIncomplete2008` and `consentinoclaeskensOrderSelectionTests2010` — both acquired via Zotero/migrate/index/lit-sync. The 2010 paper has been read cold and `verified` (synthesis in conversation 2026-05-22; reads as adjacent, not competing).
- *(Phase 1 corpus from `todo/001` already in `literature/` since session opening.)*

---

*Last updated: 2026-06-01*
