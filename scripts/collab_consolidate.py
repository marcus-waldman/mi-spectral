# todo/032 Phase C — consolidate the per-session coded outputs into the
# frequency tables cited by verification/collaboration-analysis.md.
#
# Inputs:
#   verification/cache/collab-analysis/coded/<session>.json  (primary data:
#     per-turn codes produced by the 34 Phase B coding agents; committed)
#   verification/cache/collab-analysis/turns/<session>.json   (cleaned turn
#     inventory; regenerable from the transcript archive via
#     scripts/collab_extract_turns.py)
#
# The join against turns/ enforces the machine-turn exclusion: 65 coded turns
# were harness-injected task notifications (identified during Phase B), and the
# fixed extractor drops them, so any coded uuid absent from turns/ is excluded
# here and counted.
#
# Output: verification/cache/collab-analysis/clean-tally.json (committed).

import collections
import glob
import json
import os

BASE = r"C:\Users\marcu\git-repositories\mi-spectral\verification\cache\collab-analysis"


def main():
    coded_files = sorted(glob.glob(os.path.join(BASE, "coded", "*.json")))
    freq = collections.Counter()
    dom = collections.Counter()
    ai = collections.Counter()
    n_turns = 0
    n_machine = 0
    n_episode = 0
    per_session = {}
    for p in coded_files:
        s = json.load(open(p, encoding="utf-8"))
        raw = json.load(open(os.path.join(BASE, "turns", s["session_id"] + ".json"), encoding="utf-8"))
        human_uuids = {t["uuid"] for t in raw["turns"]}
        kept = 0
        for t in s["coded_turns"]:
            if t["uuid"] not in human_uuids:
                n_machine += 1
                continue
            n_turns += 1
            kept += 1
            dom[t["codes"][0]] += 1
            for c in t["codes"]:
                freq[c] += 1
            if t.get("episode_candidate"):
                n_episode += 1
        per_session[s["session_id"]] = kept
        for a in s.get("ai_side", []):
            ai[a["kind"]] += 1

    out = {
        "n_human_turns": n_turns,
        "n_machine_excluded": n_machine,
        "n_episode_candidates": n_episode,
        "freq_all": dict(freq.most_common()),
        "freq_dominant": dict(dom.most_common()),
        "ai_side": dict(ai.most_common()),
        "per_session": per_session,
    }
    with open(os.path.join(BASE, "clean-tally.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(f"human turns: {n_turns}  machine excluded: {n_machine}")
    for c, n in freq.most_common():
        print(f"  {c:28s} {n:4d}")
    print("AI-side:", dict(ai.most_common()))


if __name__ == "__main__":
    main()
