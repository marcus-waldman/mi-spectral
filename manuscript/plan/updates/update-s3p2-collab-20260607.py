# S3-P2 rewrite from the collaboration analysis, 2026-06-07 (todo/032 Phase D).
#
# The drafted P2 was flagged awaiting_collaboration_analysis: its role statement
# compressed the collaboration into one line, and its examples were
# recency-sampled from the 2026-06-06/07 sessions. todo/032 executed the
# qualitative coding of the full 34-transcript record (599 substantive human
# turns, 13-code taxonomy, 58 verified episodes), committed as
# verification/collaboration-analysis.md. P2 is rewritten heuristic-first from
# that analysis (five patterns, counts attached), with one verified example per
# challenge direction. Every count carries a verif: pointer in the audit object.
# Level 4 gains E-S3-P2-2 pointing at the analysis.

import json

PLAN = r"C:\Users\marcu\git-repositories\mi-spectral\manuscript\plan"

P2_PROSE = (
    "**Roles and decision records.** Direction, scope, and the acceptance or "
    "rejection of every result were decided by the human author of record. "
    "Derivations, drafts, and computations were produced by an AI assistant. "
    "This division of labor was measured rather than recalled. The complete "
    "session record, 34 transcripts containing 599 substantive human turns, was "
    "qualitatively coded, and the committed analysis backs the counts given "
    "here. Five patterns characterize the collaboration. First, the human "
    "author set standards more often than steps. Rules of process such as "
    "preregistration before code and independent cross-model review appear in "
    "136 of the 599 turns, the densest block of interventions after plain task "
    "assignment. Second, decisions were proposed by the assistant and ratified "
    "by the human author. The record shows 71 explicit ratifications, and each "
    "strategic decision was logged with its date, the options rejected, and the "
    "rationale. Third, challenge ran in both directions. The human author "
    "disputed derivations, contested framing, caught omissions, and rejected "
    "prose 172 times. The assistant flagged risks and surfaced decisions rather "
    "than deciding silently, with 175 such moves observed. One example of each "
    "direction is on record from the same week. The human author caught that "
    "the cited EM-based results concern improper imputation, which produced the "
    "Background's paragraph on proper imputation. Blind re-derivation by an "
    "independent model exposed a silently substituted conditioning in the main "
    "theorem, and the human author ratified the repair. Fourth, field knowledge "
    "entered from the human side, as literature leads, methodological "
    "alternatives, and venue judgment, 131 times. Fifth, scope was actively cut "
    "and the work was partitioned across sessions with written handoffs, 183 "
    "such moves. Recorded decisions were not revisited without a dated "
    "amendment. The transcripts, the decision log, and the coded analysis are "
    "all part of the public record, so this description is auditable rather "
    "than self-reported. The discipline cannot certify correctness. Recording "
    "who decided what catches nothing about whether a derivation is right. The "
    "remaining parts exist for that."
)

VERIF = "verif:verification/collaboration-analysis.md"

with open(PLAN + r"\level3-paragraphs.json", encoding="utf-8") as f:
    l3 = json.load(f)

for p in l3["paragraphs"]:
    if p["id"] != "S3-P2":
        continue
    p["proposition"] = (
        "Roles and decision discipline, characterized from the coded session "
        "record: five collaboration patterns (standards over steps, "
        "proposal-then-ratification with a written record, bidirectional "
        "challenge, human-supplied field knowledge, managed scope and "
        "continuity); blind spot = records not correctness."
    )
    p["draft_prose"] = P2_PROSE
    p["review"]["flags"] = None
    p["review"]["status"] = "drafted"
    p["audit"]["status"] = "complete"
    p["audit"]["numbers"] = {
        "34 transcripts / 599 substantive human turns": VERIF,
        "136 set-standard turns": VERIF,
        "71 explicit ratifications": VERIF,
        "172 human challenge-class assignments": VERIF,
        "175 AI-side moves observed (68 flag-risk + 63 surface-decision + 44 propose-options)": VERIF,
        "131 domain-supply assignments (80 supply-domain-judgment + 51 provide-resource)": VERIF,
        "183 scope/continuity assignments (103 scope-decision + 80 redirect-priority)": VERIF,
        "improper-imputation catch episode": VERIF + " (E11; commit f1126db)",
        "blind re-derivation sign episode": VERIF + " (E14; commit 6bc7206)",
    }
    p["audit"]["notes"] = (
        "Rewritten 2026-06-07 from the todo/032 qualitative analysis "
        "(verification/collaboration-analysis.md): heuristic first, examples "
        "second, per the 2026-06-07 in-chat direction. Counts are turn/"
        "assignment frequencies from the committed coded outputs; both cited "
        "episodes are verified entries (E11, E14) in the analysis episode "
        "table. Supersedes the placeholder whose examples were recency-sampled."
    )

l3["metadata"]["status"] = "drafting_s3_p2_rewritten_from_collab_analysis"

with open(PLAN + r"\level3-paragraphs.json", "w", encoding="utf-8") as f:
    json.dump(l3, f, indent=2, ensure_ascii=False)
    f.write("\n")

with open(PLAN + r"\level4-evidence.json", encoding="utf-8") as f:
    l4 = json.load(f)

ids = {e["id"] for e in l4["evidence_map"]}
if "E-S3-P2-2" not in ids:
    anchor = max(
        i for i, e in enumerate(l4["evidence_map"]) if e["proposition_id"] == "S3-P2"
    )
    l4["evidence_map"].insert(
        anchor + 1,
        {
            "id": "E-S3-P2-2",
            "proposition_id": "S3-P2",
            "pointer": VERIF,
            "evidence_status": "verified",
            "passage_or_value": (
                "Five-pattern heuristic with frequencies (599 turns, 13 codes) "
                "and a 25-episode verified table; episodes E11 and E14 are the "
                "two cited in P2."
            ),
            "note": (
                "todo/032 qualitative coding of the 34-transcript session "
                "record; primary data committed under "
                "verification/cache/collab-analysis/."
            ),
        },
    )

with open(PLAN + r"\level4-evidence.json", "w", encoding="utf-8") as f:
    json.dump(l4, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("S3-P2 rewritten from the collaboration analysis; level4 E-S3-P2-2 added")
