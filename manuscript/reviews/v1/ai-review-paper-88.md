# AI Review Report

**Paper:** Model selection after multiple imputation: a deviance correction for AIC, BIC, and likelihood-ratio tests
**Paper ID:** 88
**Review Service:** Reviewer3.com
**Generated:** July 01, 2026 at 21:27 UTC

---

## Round 1 — Completed
*Paper version: v1*
*Submitted: July 01, 2026 at 21:20 UTC*
*Completed: July 01, 2026 at 21:25 UTC*

### reviewer3

Although the title explicitly promises a deviance correction for BIC, the manuscript focuses entirely on AIC and likelihood-ratio tests. The formulation of an MI-BIC is completely absent from the text. Applying the derived deviance correction to BIC is not trivial because the BIC penalty relies on the sample size, and defining the effective sample size for multiply imputed data is a recognized challenge in the missing data literature. The authors must explicitly formulate the corrected MI-BIC, discuss the appropriate sample size penalty in this context, and ideally include it in the simulation studies to support the title's claim.

### reviewer3

The manuscript relies exclusively on a four-dimensional multivariate normal distribution for all empirical validations. While the authors acknowledge this limitation, the lack of evaluation for non-normal data (such as categorical or skewed continuous variables commonly modeled via Generalized Linear Models) leaves the practical generalizability of the design-imbalance term unclear. The authors should discuss how the derived trace penalty and design-imbalance terms are expected to behave under non-normal likelihoods, and whether the current findings can be safely generalized to standard GLM frameworks used in applied research.

### reviewer3

The authors correctly identify that uncongeniality causes the proposed correction to overshoot and recommend diagnosing congeniality before applying the method. However, the manuscript does not provide, nor does it cite, any practical methods or established literature for how an applied researcher should actually perform this diagnosis. Given that strict congeniality is rarely achieved in applied settings, the authors should expand the discussion to include specific, actionable diagnostic checks or cite relevant literature that guides users on evaluating imputation model congeniality.

### reviewer2

Throughout the simulation results, the manuscript uses the "±" symbol without defining the measure of dispersion in the main text. Although the figure captions mention 95 percent intervals, the text must explicitly state whether these values represent standard errors, standard deviations, or the half-width of a 95% confidence interval to ensure unambiguous interpretation of the precision.

### reviewer2

The authors define the extremes of the candidate set (diagonal and saturated) but omit the definitions of the two intermediate nested models used in the selection-sweep design. Without knowing the specific constraints applied to these intermediate models (e.g., compound symmetry, autoregressive, block-diagonal), readers cannot fully interpret the selection rates or independently replicate the simulation. Please explicitly define all four models included in the candidate set.

### reviewer2

The manuscript does not specify which of the six possible coordinate pairs in the four-variate normal distribution are assigned the correlations of 0.6, 0.3, and 0.5. Because the missingness mechanism depends specifically on the third and fourth coordinates, the exact placement of these correlations within the covariance matrix will alter the missing information structure and the resulting relative-increase-in-variance trace. Please explicitly state the full covariance matrix or specify which variables correspond to each correlation value to ensure the simulation can be reproduced from the text.

### reviewer1

The authors justify the failure of the N=1000 cell to hit the analytic target by claiming the standard deviation of the per-repetition statistic grows with sample size due to heavy tails. If the estimand is an expectation (the mean bias) and the variance is finite, the standard error of the mean must decrease with sample size. If the underlying distribution has infinite variance, then the standard error bars presented in Figure 1 are mathematically invalid and standard asymptotic confidence intervals cannot be used. The authors must either clarify why the variance of this specific statistic scales positively with N, or re-evaluate the N=1000 cell using robust estimators or a larger repetition count to achieve convergence.

### reviewer1

The manuscript claims to validate the trace correction for proper multiple imputation, but the simulations rely exclusively on an approximately Bayesian bootstrap expectation-maximization approach rather than exact data augmentation. Because the theoretical derivations for proper MI depend on exact posterior draws, the lack of a fully Bayesian Markov chain Monte Carlo (MCMC) control experiment undermines the claim that the correction holds for proper MI, especially under high missingness. I recommend running the headline simulation studies using a standard data augmentation engine to confirm that the analytic results hold without the artifacts of the bootstrap approximation.

### reviewer1

In the selection-sweep design, the candidate models are nested, meaning that model complexity (parameter count) is perfectly confounded with the amount of missing information. Consequently, it is impossible to determine whether the uncorrected MI-AIC misclassifies toward the saturated model specifically because of the missing information bias, or simply because the uncorrected deviance generally favors more complex models when under-penalized. To logically support the claim that the bias is driven by missing information, the authors should include a control experiment comparing non-nested candidate models that have the same number of parameters but differ significantly in their fractions of missing information.

### proof-verifier

The abstract claims generally that under congenial proper multiple imputation, the averaged log-likelihood overstates its complete-data counterpart by one half the trace of the relative-increase-in-variance matrix. However, Theorem 5.1 explicitly restricts this result to "a model that estimates a scale or covariance." This condition is strictly necessary because, as shown in Equation 14 and discussed in Section 7, the bias for a known-scale model under proper MI is actually $-1/2 \operatorname{tr}(\text{RIV})$, which has the opposite sign. The abstract's formulation implies the $+1/2 \operatorname{tr}(\text{RIV})$ bias is a universal property of proper MI, whereas the proof establishes it only for the estimated-scale regime.

### proof-verifier

While the abstract states that adding one trace term per candidate removes the deviance bias in expectation, Theorem 5.1 establishes that the deviance bias actually consists of two components: the trace term and a design-imbalance term $(A) + (C)$ that is $O(1)$ under missing-at-random data. The proposed correction in Equation 21 only offsets the trace component. As shown in Proposition 5.4, the uncorrected design-imbalance term remains and becomes a genuine $O(1)$ differential bias when comparing candidates with separated pseudo-true values. Readers will wonder if the full bias is eliminated, so the claim should be scoped to clarify that the correction removes only the trace component.

### contradictions-reviewer

The text defines $\alpha$ as $-\mathcal{E}'(\theta_0)$ and describes it as 'the gradient of the conditional missing-data entropy'. If $\mathcal{E}$ represents the entropy, its gradient is $\mathcal{E}'(\theta_0)$, making $\alpha$ the negative gradient, not the gradient itself.

### contradictions-reviewer

The main text states that the Kolmogorov-Smirnov distance falls to 0.019 under equating. However, Figure 8 displays the value 0.018 above the equating bar.

### contradictions-reviewer

The symbol $k$ is initially defined as the number of parameters (e.g., $k = p + \frac{1}{2}p(p+1)$). However, in Section 5's information-criterion selection, $k$ is redefined as a model index in $\text{AIC}_{MI}(k)$, and $q_k$ is used instead for the parameter count.

### contradictions-reviewer

The manuscript uses both $m$ and $M$ to denote the number of imputations. Section 3 introduces $m \to \infty$, but Section 5 uses $M \to \infty$ in Equation 8, and Section 6 refers to $M \in \{20, 200\}$ while other passages refer to 'finite-$m$' or 'infinite-$m$' limits.

---