import io
import json
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PATH = r"C:\Users\marcu\.claude\projects\C--Users-marcu-git-repositories-mi-spectral\ea505749-6826-4c13-99c5-804311090f69.jsonl"
TERMS = ("equipercentile", "equating", "all moment", "all-moment")


def text_of(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return c
    out = []
    if isinstance(c, list):
        for b in c:
            if isinstance(b, dict) and b.get("type") == "text":
                out.append(b.get("text", ""))
    return "\n".join(out)


rows = []
with open(PATH, encoding="utf-8") as fh:
    for i, line in enumerate(fh):
        try:
            rec = json.loads(line)
        except Exception:
            continue
        msg = rec.get("message") or {}
        role = msg.get("role", rec.get("type", "?"))
        txt = text_of(msg)
        if not txt:
            continue
        low = txt.lower()
        if any(t in low for t in TERMS):
            rows.append((i, role, txt))

print(f"{len(rows)} matching messages\n")
for i, role, txt in rows:
    print(f"===== line {i} role={role} chars={len(txt)} =====")
    # print the match neighborhoods, not whole giant messages
    low = txt.lower()
    spans = []
    for t in TERMS:
        start = 0
        while True:
            j = low.find(t, start)
            if j < 0:
                break
            spans.append((max(0, j - 900), min(len(txt), j + 1400)))
            start = j + 1
    # merge overlapping spans
    spans.sort()
    merged = []
    for a, b in spans:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    for a, b in merged[:4]:
        print(txt[a:b])
        print("   ...---...")
    print()
