# Prompt to send (with the handoff attached)

You are performing an adversarial derivation audit of a statistical theorem, at maximum
reasoning effort. The attached handoff (`040-cross-model-derivation-handoff.md`) is self-contained:
it gives the setup, the theorem, exactly how the derivation treats "proper multiple imputation,"
and a high-powered empirical finding. The finding: every genuine Bayesian posterior-draw imputer
carries a *persistent* O(tr(RIV)) deviance discount vs the $+\tfrac12\operatorname{tr}(\mathrm{RIV})$
headline (Jeffreys IW $\approx-0.74$ — my hand-rolled conjugate DA and Schafer's `norm::da.norm`
agree to the third decimal; the MLE-centered Gaussian/Laplace draw $\approx-0.11$; brms $-1.36$),
while Amelia's bootstrap EMB — the engine the paper actually validated with — *converges* to
$+\tfrac12$ as $N\to\infty$.

Your job is to decide whether this is (i) a separable, characterizable term (removable prior
mean-inflation + a persistent draw-$\Sigma$ Jensen term) that leaves the leading-order
$+\tfrac12\operatorname{tr}(\mathrm{RIV})$ theorem correct — scoped to the bootstrap/EMB
(MLE-centered) construction of proper MI the paper validated — or (ii) a genuine qualification of
the unscoped "holds for proper MI" claim.

Rules:
- Trust nothing on authority. If our sampler or our reading of the derivation is wrong, show the
  error with algebra. If the finding is real, say what it implies for the theorem's scope.
- Q1 is load-bearing: derive the leading-order coefficient of
  $\mathbb{E}[T_{\text{proper,IW}}]-\mathbb{E}[T_{\text{fitted}}]$ explicitly and settle whether it
  is $O(\operatorname{tr}(\mathrm{RIV}))$ (persistent) or $o(1)$ (vanishing). Show the algebra.
- Q1b is also load-bearing: derive the persistent Jensen coefficient carried even by the correct
  MLE-centered Gaussian/Laplace draw ($\approx-0.11$).
- Q2 is the anomaly to explain: why does the bootstrap (Amelia) escape the Jensen term and converge
  to $+\tfrac12$ while every Bayesian posterior draw (Gaussian, IW, HMC) does not?
- Answer Q1, Q1b, Q2, Q3, Q4 (§6 of the handoff) in order, each with its reasoning.
- Flag any place where you need a number we can compute (we can run the exact-DA engines at any
  $N$, any prior, and can report $\mathbb{E}[\Sigma\mid Y]$, per-cell imputation variance, etc.).

Then read the handoff and answer.
