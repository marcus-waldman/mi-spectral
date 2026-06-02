#!/usr/bin/env python
r"""Layer-3 cross-model adversarial check (todo/013, Layer 3) via the OpenAI API.

Sends Mode A (blind) and Mode B (red-team) from
`todo/013b-layer3-crossmodel-package.md` to a different model family (o-series /
GPT), so the deviance-bias decomposition is stress-tested off the Claude lineage.
Independence is on the MODEL axis: who fires the request is irrelevant; what
matters is (i) the packet does not leak the answer and (ii) the GRADING KEY is
NEVER transmitted. This script HARD-TRUNCATES the package at the grading-key
banner before doing anything else, so the key cannot be sent even by accident.

Key handling: reads OPENAI_API_KEY from the environment, or from a file via
--key-file. Never pass the key on the command line (it lands in shell history).

Run:    py verification/run_layer3_openai.py [model] [--key-file PATH]
        e.g.  py verification/run_layer3_openai.py o3
Out:    verification/cache/layer3-<model>-modeA.md , -modeB.md  (raw responses)
Exit:   0 ok; 2 setup/missing; 3 API error.
"""
import json
import os
import sys
import urllib.error
import urllib.request

PKG = "todo/013b-layer3-crossmodel-package.md"
KEY_BANNER = "GRADING KEY"          # hard stop: never send anything at/after this
MODE_A_BEG = "## MODE A"
MODE_A_END = "<!-- MODE-A END -->"
MODE_B_BEG = "## MODE B"
ENDPOINT = "https://api.openai.com/v1/chat/completions"


def load_key(key_file):
    if key_file:
        with open(key_file, "r", encoding="utf-8") as fh:
            return fh.read().strip()
    return os.environ.get("OPENAI_API_KEY", "").strip()


def declutter(text):
    """Strip markdown blockquote '> ' prefixes and HTML comments; keep the prose."""
    out = []
    for line in text.splitlines():
        if line.strip().startswith("<!--"):
            continue
        if line.startswith("> "):
            out.append(line[2:])
        elif line.strip() == ">":
            out.append("")
        else:
            out.append(line)
    return "\n".join(out).strip()


def extract_modes(pkg_path):
    with open(pkg_path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    # HARD SAFETY: drop everything from the grading-key SECTION HEADER onward.
    # ("GRADING KEY" also appears inline in the intro, so anchor on the '##' header
    #  line, not the first substring match.)
    lines = raw.splitlines(keepends=True)
    for idx, line in enumerate(lines):
        if line.lstrip().startswith("##") and KEY_BANNER in line:
            raw = "".join(lines[:idx])
            break
    a0 = raw.find(MODE_A_BEG)
    a1 = raw.find(MODE_A_END)
    b0 = raw.find(MODE_B_BEG)
    if min(a0, a1, b0) < 0 or not (a0 < a1 < b0):
        raise ValueError("could not locate Mode A / Mode B markers in the package")
    mode_a = declutter(raw[a0:a1])
    mode_b = declutter(raw[b0:])            # to end of the key-stripped text
    if KEY_BANNER in mode_a or KEY_BANNER in mode_b:
        raise RuntimeError("ABORT: grading key leaked into a prompt")
    return mode_a, mode_b


def call(model, prompt, key, effort):
    body = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    if effort and effort != "none":
        body["reasoning_effort"] = effort
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=1800) as resp:
        out = json.loads(resp.read().decode("utf-8"))
    return out["choices"][0]["message"]["content"]


def main():
    model = "gpt-5.5"
    effort = "high"
    key_file = None
    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        if argv[i] == "--key-file":
            key_file = argv[i + 1]
            i += 2
        elif argv[i] == "--effort":
            effort = argv[i + 1]
            i += 2
        else:
            model = argv[i]
            i += 1

    key = load_key(key_file)
    if not key:
        print("No API key. Set OPENAI_API_KEY in the environment or pass --key-file PATH.")
        print("(Do NOT pass the key on the command line.)")
        return 2
    if not os.path.exists(PKG):
        print(f"Package not found: {PKG}")
        return 2

    try:
        mode_a, mode_b = extract_modes(PKG)
    except Exception as e:
        print(f"Package parse error: {e}")
        return 2

    print(f"Model: {model}   reasoning_effort: {effort}")
    print(f"Mode A prompt: {len(mode_a)} chars   Mode B prompt: {len(mode_b)} chars")
    print("Grading key excluded from both prompts (hard-truncated at the banner).\n")

    results = {}
    for tag, prompt in (("modeA", mode_a), ("modeB", mode_b)):
        print(f"--- calling {model} [{tag}] ---")
        try:
            results[tag] = call(model, prompt, key, effort)
        except urllib.error.HTTPError as e:
            print(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")
            return 3
        except Exception as e:
            print(f"API error ({type(e).__name__}): {e}")
            return 3
        outpath = f"verification/cache/layer3-{model}-{tag}.md"
        with open(outpath, "w", encoding="utf-8") as fh:
            fh.write(f"# Layer-3 {tag} response — model={model}\n\n{results[tag]}\n")
        print(f"  saved -> {outpath}  ({len(results[tag])} chars)\n")

    print("Done. Both responses saved for grading against the §key in todo/013b.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
