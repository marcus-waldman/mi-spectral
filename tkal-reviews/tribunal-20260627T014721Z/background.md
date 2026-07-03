# Shared framing (the cardinal invariant)

This is a confidence gate before the manuscript proceeds to per-paragraph annotation and submission. The question is narrow and evidential, not stylistic: **does each Section 5 figure/table actually prove the claim it is asserted to prove, given the simulation data?**

Non-negotiable context the examiners must hold:

- **The target is the validity of claims against data, not the prose.** Do not score wording, citation formatting, or readability. Score whether each claim is supported by the numbers, whether any claim overreaches, and whether any figure demonstrates an artifact rather than the named mechanism.
- **A correctly disclosed failure is not a defect.** The paper's discipline (call it D-05) requires unmet pre-registered predictions to appear in the main text. A claim that says "this prediction was not met" is *passing* the standard, not failing it. Penalize *hidden* failures and *overclaimed* successes, not honestly-reported misses.
- **Trust tiers.** The paper labels results as *firm* (proved and symbolically verified), *measured* (Monte Carlo within a preset precision), or *conjecture* (partial support, labelled). A measured result need not be a theorem; it needs to be honestly scoped to the designs studied. Judge each claim against the tier it actually asserts.
- **The estimands are deviance-bias quantities**, not effect sizes. "tr(RIV)" is the amount of missing information and the size of the bias being corrected. The oracle (complete-data reference) is "perfect" for every study.
- **Pre-registration is real but not infinitely fine.** Predictions and pass criteria were fixed before code; amendments are dated. A *refinement* of a target after seeing data is legitimate only if it follows from an independently-derived term, not from the observed estimate. That distinction is squarely in scope.

The defender concedes individual claims and proposes minimal rewrites where the data do not support the prose as written; the goal is a hardened, defensible Section 5, not a rhetorical victory.
