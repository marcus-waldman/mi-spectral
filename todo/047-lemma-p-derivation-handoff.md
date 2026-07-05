# todo/047 — session handoff: the Lemma P formal section in derivation.qmd

**STATUS: OPEN (written 2026-07-04, at the close of the session that merged the complete
v1-review response to main @ `8055daf`).** Marcus decided (2026-07-04): the canonical-GLM
extension gets a formal section in `manuscript/derivation.qmd`, with FULL citation discipline
enforced. This file is the self-contained spec + resume prompt for that session.

## Recommended model / effort

**Fable 5, effort HIGH.** The mathematics is already derived, CAS-verified, and cross-model
cleared — this session is high-precision formalization into the repo's most exacting document
(the sourced derivation, which must survive `/derivation-audit` at 0 blocker / 0 warn), not new
derivation. That precision bar argues for Fable over the Sonnet default; max effort is not
needed unless drafting surfaces a genuine gap requiring new mathematics (e.g., the
general-missingness or non-canonical-link fences turn out to need sharpening rather than
stating) — bump to max for that sub-task only, and any genuinely NEW derivation re-enters the
standing cross-model protocol (GPT-5.5 Pro xhigh, backgrounded) before landing.

## What the section states (all already proven and verified — nothing new to derive)

Source of record: `todo/045-phase3-bernoulli-investigation.md` §3.1 (the dated derivation),
§3.4 (production scorecard), §3.5 (gate verdict). One-paragraph summary:

For a one-parameter exponential-family response $f(y\mid x;\beta)=h(y)\exp\{y\eta-A(\eta)\}$
with canonical link $\eta=x^\top\beta$, response-only MCAR missingness at rate $r$, and the
FITTED (deterministic FIML plug-in) arm:
$$\mathbb{E}[T_{\text{fitted}}] = +\tfrac12\operatorname{tr}(\mathrm{RIV}) + \Delta_h + O(1/N),$$
because the A4 design pieces $(A)=\alpha^\top\mathbb{E}[\delta]$ (entropy gradient × Cox–Snell
MLE bias) and $(C)=\tfrac12\operatorname{tr}(\mathcal H_\phi I_{\text{obs}}^{-1})$ cancel
exactly at $O(1)$ — **Lemma P**:
$\mathbb{E}[\eta wX^\top]\Omega^{-1}\mathbb{E}[A'''(X^\top\Omega^{-1}X)X]
= \mathbb{E}[\eta A'''(X^\top\Omega^{-1}X)]$ (since $\eta=X^\top\beta_0$ and
$\Omega=\mathbb{E}[wXX^\top]$ share the weight $w=A''$), leaving only the base-measure
functional $\Delta_h$ built from $g(\eta)=\mathbb{E}_\eta[\log h(Y)]$. Corollaries: Bernoulli
($h\equiv1$): $\Delta_h=0$, the general $+\tfrac12$ value transfers exactly; Poisson
($h=1/y!$): $\Delta_h/\operatorname{tr}(\mathrm{RIV})=-0.396$ at the studied design, FITTED
target $+0.104$; proper-draw discount $=$ the $(C)$ functional ($-0.2606$ at the Bernoulli
design) — the GLM analog of the D-22 engine gap; fixed-scale location families (Student-t):
FITTED $0$, proper draw $-\tfrac12$. **Mode B's binding cosmetic note: state explicitly that
the $(A)/(C)$ displays carry an outer expectation over design and missingness.**

## Requirements (fixed at decision time; charter Next-3 #2 mirrors this)

1. **Placement decision first.** Read the current `derivation.qmd` structure before writing:
   the natural anchor points are the known-scale scope callout (:792-827 region), the
   @sec-termA A4 lemma (whose MCAR-cancellation claim this section extends beyond MVN), and
   the D-22 scope-and-correction callout. Decide subsection vs callout-cluster; keep the
   theorem's existing statement untouched (this is an EXTENSION section, not a rewrite).
2. **Citation discipline (the reason this is its own session).** Re-read in-session before
   citing (the standing rule; prior verify-reads do not carry over):
   - `@coxGeneralDefinitionResiduals1968` — ALREADY owned + cited (derivation.qmd:1126, the
     b_Sigma passage, alongside `@cordeiroBiasCorrectionARMA1994` +
     `@patriotaBiasCorrectionMultivariate2009`). Bias-formula locus pinned 2026-07-04:
     Section 3, scalar $b=(K+2J)/(2I^2)$ at `:229` (second-order score equation `:180`–`:223`),
     vector case `:269`. Add an Appendix A source-quote entry if one does not already exist
     for the bias formula specifically (check `#sec-src-` sections first).
   - `@firthBiasReductionMaximum1993` — acquired + verified 2026-07-04 (todo/003 row has the
     loci: Abstract; §1 corrective standard + separation motivation; `:265` direction
     discussion). OPTIONAL — cite only if the drafted section keeps the one-sentence remark on
     the logistic MLE bias direction ($\sinh(\eta)/n$ intercept-only closed form is derived
     inline regardless).
   - The hook: `@citekey` writes into `manuscript/` require the `literature/<key>.md` to exist
     AND be read this session; use Bash for writes if the cwd-hook gotcha bites (memory:
     `feedback_citation_hook_cwd_bug`). D-17's no-verbatim-quote rule does NOT apply to
     derivation.qmd (it is the sourced-audit companion; Appendix A quotes verbatim with line
     refs by design).
3. **Verification pointers, [mc]-style.** Margin/inline source pointers to:
   `verification/cas-wolfram/verify_bernoulli_fitted_gap.py` (15 checks: Lemma P symbolic + 12
   exact-rational designs; Cox–Snell = delta-method $\sinh(\eta)/n$; exact intercept-only and
   two-point enumerations → ½), `verify_045b_escalations.py` (third-route quadrature),
   `verification/spikes/phase3-family-scan.R` + `phase3-family-scan-score.R` + the four
   `verification/cache/phase3-family-scan-*-prod.rds` caches (registered criteria P1–P6, all
   substantive passes), the two cross-model records
   (`verification/cache/layer3-gpt-5.5-pro-bern-glm-mode{A,B}.md`), and the compliance record
   (`tkal-reviews/gemini-045c-compliance-20260704/REPORT.md`). Registration-before-results is
   checkable in git (`4aaeaae` → `afa4438`) — say so the way the D-22 callout does.
4. **Fences stated plainly:** canonical link only (Gamma's log link NOT covered — directional
   only); response-only missingness; MCAR (the MAR design-imbalance term is separate);
   asymptotic ($O(1/N)$ remainder measured, not derived — intercept-only ≈0.6/n, two-point
   ≈1.6/n exact; Gaussian-x ≈3.5/N measured); the draw-discount corollary assumes a
   second-moment-proper regular draw.
5. **Render + audit:** `quarto render manuscript/derivation.qmd` must exit 0 (executes
   Appendix B; needs sympy/numpy + the fixture json), then run `/derivation-audit` — target
   0 blocker / 0 warn. Frozen preregistered originals untouched.
6. **Optional, same session if cheap:** one-sentence CLAUDE.md core-contribution update
   (the "Holds for any regular likelihood model ... that estimates a scale or covariance"
   sentence can now name the canonical-GLM extension); level4-evidence join-table rows for G9
   if `check_plan` flags missing evidence pointers (check before assuming).

## Marcus prerequisites: NONE blocking

Both sources are in hand and verified. Parked (non-blocking): merge the duplicate Cox–Snell
item in Zotero before the next BBT re-export (else `coxGeneralDefinitionResiduals1968a`
resurrects); the annotation + compile-enablement pass can precede or follow this session at
Marcus's discretion (charter lists annotation first; the two are independent).

## Resume prompt (paste as the opening message)

Resume mi-spectral. Confirm `git branch --show-current` first (should be `main`, in sync with
`origin` — the v1-review branch was merged at `8055daf`). Read `.prometheus/charter.md` for
current state — check `git log` against `last_synced_commit` and run `/prometheus:wrap` if
commits have landed since.

Task — the Lemma P formal section in `manuscript/derivation.qmd`, per
`todo/047-lemma-p-derivation-handoff.md` (read it in full first; it is the spec of record):
formalize the canonical-GLM extension (Lemma P + Delta_h + the draw-discount and known-scale
corollaries, todo/045 §3.1) as an extension section with full citation discipline — re-read
`coxGeneralDefinitionResiduals1968` (bias formula: Section 3, `:229`/`:269`) and, if the
direction remark is kept, `firthBiasReductionMaximum1993` in-session before citing; state the
outer expectation on the (A)/(C) displays (the Mode B note); wire the [mc]/source pointers to
the CAS scripts, scan caches, both cross-model records, and the compliance report; state the
fences (canonical link only, response-only MCAR, measured-not-derived finite-N constants);
then render derivation.qmd (exit 0) and run /derivation-audit to 0/0. Placement decision
(where in derivation.qmd the section sits) is the first in-session call after reading the
document structure. Frozen preregistered originals untouched. Nothing is blocked on Marcus.
