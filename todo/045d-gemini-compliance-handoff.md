# todo/045d — Cross-model compliance validation of the staged rewrites (Gemini 3.1 Pro, repo-grounded)

**You are Gemini 3.1 Pro running in Google Antigravity with read access to this repository.**
Your model family was the LEAD PEER of the adversarial quorum whose determination created the
obligations you are about to verify (`tkal-reviews/quorum-phase3-bernoulli-20260703/DETERMINATION.md`).
You are now the independent validator of whether the staged replacement texts honor that
determination's binding amendments — this time with the repository's evidence in hand, which the
original API-only panel did not have.

## Ground rules (binding)

- **Read-only, with ONE permitted write:** create
  `tkal-reviews/gemini-045c-compliance-20260704/REPORT.md` and write your report there. Do not
  edit any existing file. Do not run any git command that mutates state (no add/commit/checkout/
  restore/stash). Running the verification scripts listed below is allowed and encouraged
  (they only read the repo and write to stdout).
- Confirm at the start: `git branch --show-current` is `da-engine-phase0-todo040` and
  `git status` is clean. Report both in your REPORT.md header. If either fails, stop and say so.
- Verify against the actual files and command outputs, never from this handoff's summaries.
  Where this handoff and a file disagree, the file wins — and flag the disagreement.
- Do not re-derive the mathematics from scratch (a separate blind cross-model gate already did:
  `verification/cache/layer3-gpt-5.5-pro-bern-glm-mode{A,B}.md`). Your job is fidelity of TEXT
  to OBLIGATIONS plus mechanical verification of quoted facts. If you nonetheless notice a
  substantive error, flag it under axis A10 — do not silently expand scope.

## Context in brief (pointers, not the record — read the files)

1. A Phase-3 simulation write-up was found HARKing-shaped and put through an adversarial quorum:
   determination **AMENDED** with binding amendments (the file above; the amendments are itemized
   under "The amendments the deliberation forced" and in each OBJ's "amendment" field).
2. A follow-up investigation (`todo/045-phase3-bernoulli-investigation.md`, §§2–3.5) then derived
   the corrected theory (Lemma P; §3.1), CAS-verified it
   (`verification/cas-wolfram/verify_bernoulli_fitted_gap.py`), pre-registered new targets in
   commit `4aaeaae` BEFORE the production scan (`afa4438`), passed all five substantive criteria
   (§3.4), and cleared a blind + red-team cross-model gate (§3.5, commit `5b35192`).
3. The replacement texts for the three stale artifacts plus a registration amendment are STAGED,
   not landed, in **`todo/045c-staged-rewrites.md`** — sections: §1 (response-letter r3#2 body),
   §2 (manuscript Discussion paragraph G9 / S6-P4d), §3 (decisions.md D-24 pointer + new D-25),
   §4 (todo/040 §9 amendment). The only remaining landing gate is the human owner's ratification;
   your report informs that ruling.

## Your axes (verdict each: HONORED / VIOLATED / AMBIGUOUS, with quoted evidence)

- **A1 (OBJ-01 + OBJ-09, disclosure ordering).** In EACH staged text (§1, §2, §4 of todo/045c):
  are the ORIGINAL registered targets (~0 FITTED; ~−0.5 Bayesian draw) and their measured misses
  (+0.85 at ~5 se; +0.63 at ~7 se, wrong sign) stated BEFORE any corrected framing? OBJ-09
  demanded a near-verbatim sentence with the values +0.628 (se 0.161); the staged texts round to
  +0.63 (se 0.16) per the manuscript's numeral style. Rule explicitly on whether the paraphrase
  honors the amendment's intent or needs the exact decimals restored.
- **A2 (OBJ-02 + OBJ-06, claim strength).** Is the +0.5 magnitude everywhere framed as DERIVED
  AFTER the miss and then independently verified (pre-registration commit, blind scans, the
  cross-model gate) — never as an a priori prediction or a recovered foresight? Is the firm,
  checkable part (Bernoulli escapes the known-scale collapse) kept distinct from the
  once-untested magnitude claim?
- **A3 (OBJ-03 + OBJ-07, residual attribution).** Is the old "+0.853 vs +0.5, 2.2 se" residual
  now ATTRIBUTED with evidence (an R=1000 Monte-Carlo outlier around a true value near +0.52,
  plus a small measured finite-N term) rather than described as a match or as tolerable noise?
  Are the new values quoted with standard errors?
- **A4 (OBJ-04 + OBJ-08, scope).** Is the interpretive scoping of what answers reviewer r3#2
  stated explicitly, and is the known-scale-outside-MVN gap now described as CLOSED by the
  Student-t exemplar (with its targets derived before any code) rather than left as a hedge?
- **A5 (OBJ-10, shrinkage check).** Confirm the slope-shrinkage check appears NOWHERE in the
  staged texts (search todo/045c for "shrink"). It was demoted to non-load-bearing and must not
  be cited as support.
- **A6 (OBJ-11, timing separation).** Is the pre-registered FAMILY selection kept explicitly
  distinct from the post-hoc TARGET correction, with no sentence implying the +0.5 target
  predates the data?
- **A7 (numbers vs the record).** Re-run, and compare every number quoted in the staged texts
  against the outputs and caches:
  ```
  "C:\Program Files\R\R-4.5.1\bin\Rscript.exe" verification/spikes/phase3-family-scan-score.R prod
  py verification/cas-wolfram/verify_bernoulli_fitted_gap.py
  py verification/cas-wolfram/verify_045b_escalations.py
  ```
  Expected: all checks pass; scorecard values match the staged texts' +0.5176±0.0116 /
  +0.512±0.037 / +0.113±0.027 vs +0.104 / −0.313±0.070 vs −0.2606 / +0.025±0.049 /
  −0.483±0.049; the superseded originals (+0.853/+0.628, se 0.161) match
  `verification/cache/phase3-nonnormal-prod.rds` as quoted in todo/045 §3.1. Flag any number in
  the staged texts you cannot reproduce from the repo.
- **A8 (chronology).** Verify with `git log --oneline` (and `git show --stat <sha>` as needed)
  that `4aaeaae` (registration, incl. the pre-registered Poisson +0.1039 and t-exemplar targets)
  strictly precedes `afa4438` (production results), which precedes `bb5ebec` (staged rewrites)
  and `5b35192` (gate verdict). The staged texts claim this ordering as evidence — confirm the
  history supports the claim.
- **A9 (no overclaim beyond the evidence).** Do the staged texts keep Gamma directional-only
  (non-canonical link, magnitude underived, fixed-seed caveat), keep non-canonical links and
  general missingness patterns outside the new lemma's scope, and describe the gate accurately
  (Mode B's two numerical escalations disclosed and closed by a third quadrature route — not
  glossed as "sustained everything")?
- **A10 (open flag).** Anything else — substantive, presentational, or procedural — that should
  block landing, or that the human owner should weigh before ratifying.

## Report format

`tkal-reviews/gemini-045c-compliance-20260704/REPORT.md`, containing: a header (date, model,
branch, git-status result, HEAD sha); a per-axis table (verdict + one-line evidence with file
quotes); the three script outcomes (pass/fail + any mismatched number); a short list of REQUIRED
fixes (empty if none) and OPTIONAL suggestions; and a one-line overall recommendation:
**LAND AS STAGED** or **FIX FIRST** (with the fixes named). Judge fidelity to the amendments as
written; where you exercise judgment (e.g., A1's rounding), say so explicitly and give both the
strict and the pragmatic reading.
