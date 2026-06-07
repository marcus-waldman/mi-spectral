# S3 - punctuation rewrite, 2026-06-07
#
# Marcus on the first S3 draft (dc88b76): "Why so many semicolons dashes and colons?
# Again. Write like a high schooler." The plain-cadence rule existed but was not
# applied at the punctuation level. Fix: semicolon chains broken into sentences,
# em-dash glosses removed, colons kept only where they introduce a definition.
# "Punctuation budget" bullet added to the CLAUDE.md prose-style section.
# Substance, structure, blind-spot endings, and passive voice unchanged.

import json

L3 = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan\level3-paragraphs.json"

with open(L3, encoding="utf-8") as f:
    l3 = json.load(f)

prose = {
"S3-P1": (
    "The derivations in this paper were produced by an AI system. They were verified "
    "under a protocol that this section states as the paper's methods. The section "
    "answers one question. Why do the results that follow deserve the same scrutiny "
    "that is applied to human-derived mathematics? The protocol has six parts. The "
    "first is roles and decision records. The second is sourced citations. The third "
    "is a verification pipeline with explicit trust tiers. The fourth is "
    "preregistration of every simulation. The fifth is adversarial cross-model review. "
    "The sixth is full reproducibility. Each part is stated below together with what "
    "it can catch and what it cannot. The complete protocol records are collected in "
    "the appendices and the public repository. These records include the decision "
    "logs, the grading sheets, the amendment histories, and the enforcement code. "
    "This section states the design."
),
"S3-P2": (
    "**Roles and decision records.** Direction, scope, and the acceptance or "
    "rejection of every result were decided by the human author of record. "
    "Derivations, drafts, and computations were produced by an AI assistant. Each "
    "strategic decision was recorded with its date, the options rejected, and the "
    "rationale. Recorded decisions were not revisited without a dated amendment. The "
    "log is part of the public record, so the division of labor is auditable after "
    "the fact. This discipline cannot certify correctness. Recording who decided what "
    "catches nothing about whether a derivation is right. The remaining parts exist "
    "for that."
),
"S3-P3": (
    "**Sourced citations.** Every claim about prior literature was pinned to a source "
    "document that was archived locally and read in the working session that used it. "
    "The rule was enforced by software. A pre-write check blocked any manuscript edit "
    "that cited a paper whose archived copy did not exist. Reliance on the AI "
    "system's trained recollection of a paper was prohibited throughout. The reason "
    "is that invented or misattributed citations are among the most common failures "
    "of AI-assisted scholarship. The enforcement has a stated limit. It checks that a "
    "source exists and where it came from. It does not check understanding. A real "
    "passage can still be misread. Only review catches that."
),
"S3-P4": (
    "**The claim pipeline and trust tiers.** Every analytic claim passed through a "
    "fixed sequence. It was derived first. It was then verified symbolically in two "
    "independent computer-algebra systems. It was then confirmed by Monte Carlo "
    "simulation against criteria fixed in advance. Results are labeled throughout the "
    "paper by the gates they cleared. A claim is *firm* if it was derived in closed "
    "form and passed both symbolic systems and Monte Carlo. A claim is *measured* if "
    "it is a quantitative finding confirmed by preregistered simulation but not "
    "pinned in closed form. A claim is *structural* if it is argued from the form of "
    "the problem but not separately measured. Anything weaker is a *conjecture* and "
    "is labeled as one. These four labels are used in the Derivations and Simulation "
    "studies sections without further comment. The pipeline has a limit, and the "
    "limit is shared setup. Both algebra systems verify the expressions they are "
    "given. An error upstream of the algebra passes both. A wrong conditioning or a "
    "misstated expectation is exactly that kind of error. The next two parts exist "
    "for that class of error."
),
"S3-P5": (
    "**Preregistration before code.** Every simulation in this paper was "
    "preregistered. Predictions, designs, and pass criteria were committed to the "
    "repository before the simulation code was written. Changes were handled by "
    "dated amendments, themselves committed before any new runs. Predictions that "
    "failed are reported in the main text alongside those that held. The limit is "
    "stated directly. Preregistration disciplines the reporting and nothing more. A "
    "frozen prediction can rest on a wrong premise. Committing it early validates "
    "neither the derivation behind it nor the design that tests it."
),
"S3-P6": (
    "**Cross-model adversarial review.** Load-bearing claims were re-derived blind by "
    "a model of an independent lineage. That model was given the setup but not the "
    "result. The claims were then subjected to a second pass in which the model was "
    "instructed to refute each one with the strongest available argument. The grading "
    "records are committed. One episode shows what this gate catches, and it is "
    "reported here as the worked example. The main theorem's sign depends on a "
    "conditioning choice. The averaged log-likelihood can be defined at the fitted "
    "imputation model, which is what multiple imputation computes. It can instead be "
    "defined at an oracle conditioned on the truth, which no procedure computes. "
    "Eight of nine blind re-derivations produced the opposite sign, "
    "$-\\tfrac12\\operatorname{tr}(\\mathrm{RIV})$. They did so because the oracle "
    "conditioning had been silently substituted. The error was not algebraic. Every "
    "algebra check passed, because the algebra was correct for the definition it was "
    "given. The fork is now stated explicitly where the theorem is set up, with both "
    "conditionings and both signs. A derivation produced and checked within a single "
    "model lineage would likely have shipped one sign without noticing that there was "
    "a choice. The gate's limit is the mirror of its strength. Independent lineages "
    "are trained on overlapping corpora. An error common to the corpus can survive "
    "both."
),
"S3-P7": (
    "**Reproducibility.** Every number in this paper regenerates from committed code. "
    "The simulations run from fixed entry points with fixed seeds. Outputs are cached "
    "as committed artifacts. The software environment is recorded. Where a result is "
    "quoted in the text, its audit trail names the artifact it comes from. The limit "
    "is the usual one. Reproducibility guarantees the numbers, not their meaning. A "
    "wrong design reproduces its artifact exactly."
),
"S3-P8": (
    "Read with this section in hand, the rest of the paper carries its evidence with "
    "it. Each claim in the Derivations and Simulation studies sections arrives with a "
    "tier label. Each quantitative claim also arrives with a committed artifact "
    "behind it. The appendices hold the records. The repository holds everything. "
    "The protocol does not ask the reader to trust an AI derivation. It asks the "
    "reader to check one. It states where the checking has already been done and "
    "where it cannot be."
),
}

topics = {
"S3-P1": "The derivations in this paper were produced by an AI system.",
"S3-P3": "Every claim about prior literature was pinned to a source document that was archived locally and read in the working session that used it.",
"S3-P4": "Every analytic claim passed through a fixed sequence.",
"S3-P5": "Every simulation in this paper was preregistered.",
"S3-P6": "Load-bearing claims were re-derived blind by a model of an independent lineage.",
}
closings = {
"S3-P3": "Only review catches that.",
"S3-P8": "It states where the checking has already been done and where it cannot be.",
}

for p in l3["paragraphs"]:
    if p["id"] in prose:
        p["draft_prose"] = prose[p["id"]]
        if p["id"] in topics:
            p["review"]["topic_sentence"] = topics[p["id"]]
        if p["id"] in closings:
            p["review"]["closing_sentence"] = closings[p["id"]]
        p["audit"]["notes"] = (p["audit"]["notes"] + " Punctuation rewrite 2026-06-07 (semicolon/colon/dash budget).").strip()

l3["metadata"]["status"] = "drafting_s3_rewritten"

with open(L3, "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S3 punctuation rewrite applied to 8 paragraphs")
