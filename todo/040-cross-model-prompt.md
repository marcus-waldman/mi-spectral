# Prompt to send (with the handoff attached)

You are performing an adversarial derivation audit of a statistical theorem, at maximum
reasoning effort. The attached handoff (`040-cross-model-derivation-handoff.md`) is self-contained:
it gives the setup, the theorem, exactly how the derivation treats "proper multiple imputation,"
and an empirical finding — reproduced by two independent canonical data-augmentation engines — that
appears to contradict the headline for the exact-Bayesian-DA engine class while confirming it for
the bootstrap (Amelia) engine.

Your job is to decide whether this is (i) a separable, prior-dependent, finite-sample term that
leaves the leading-order $+\tfrac12\operatorname{tr}(\mathrm{RIV})$ theorem correct (scoped to the
asymptotic/Laplace-posterior and EMB construction of proper MI), or (ii) a genuine qualification of
the "holds for proper MI" claim.

Rules:
- Trust nothing on authority. If our sampler or our reading of the derivation is wrong, show the
  error with algebra. If the finding is real, say what it implies for the theorem's scope.
- Q1 is load-bearing: derive the leading-order coefficient of
  $\mathbb{E}[T_{\text{proper,IW}}]-\mathbb{E}[T_{\text{fitted}}]$ explicitly and settle whether it
  is $O(\operatorname{tr}(\mathrm{RIV}))$ (persistent) or $o(1)$ (vanishing). Show the algebra.
- Answer Q1–Q4 in §6 of the handoff, in order, each with its reasoning.
- Flag any place where you need a number we can compute (we can run the exact-DA engines at any
  $N$, any prior, and can report $\mathbb{E}[\Sigma\mid Y]$, per-cell imputation variance, etc.).

Then read the handoff and answer.
