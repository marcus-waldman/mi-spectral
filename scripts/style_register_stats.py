"""Register statistics: manuscript prose vs. exemplar statistics-journal prose.

READ-ONLY diagnostic for the todo/048 style review. Compares sentence-level
register features of the manuscript (manuscript/mi-spectral-apa.qmd body prose)
against the Rubin-authored and top-venue exemplars in literature/ named in
todo/048-style-review-handoff.md.

Features per corpus:
  - sentences, mean/median/sd words per sentence
  - share of long sentences (>35 words) and short sentences (<10 words)
  - Flesch-Kincaid grade (syllable heuristic)
  - commas per sentence (subordination proxy)
  - semicolons / parentheses per 1000 words
  - subordinator openers+joiners per sentence (although/while/because/since/
    whereas/if/when/that/which)
  - first-person "we"/"our" per 1000 words
  - sentence-opener profile: The/This/That/It/We shares

Usage:  py scripts/style_register_stats.py
Output: verification/cache/style-register-stats.md
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXEMPLARS = [
    "rubinInferenceMissingData1976b.md",
    "rubinMultipleImputationNonresponse1987.md",
    "Meng01121991.md",
    "mengPerformingLikelihoodRatio1992b.md",
    "barnardMiscellaneaSmallsampleDegrees1999.md",
    "dempsterMaximumLikelihoodIncomplete1977a.md",
    "littleStatisticalAnalysisMissing2019.md",
    "mengMultipleImputationInferencesUncongenial1994a.md",
    "kenwardLikelihoodBasedFrequentist1998.md",
    "coxGeneralDefinitionResiduals1968.md",
    "firthBiasReductionMaximum1993.md",
    "efronBootstrapMethodsAnother1979.md",
]

BOILERPLATE = re.compile(
    r"JSTOR|jstor|Terms\s*&|Oxford University Press|Stable URL|Author\(s\)|"
    r"Downloaded|Accessibility|Linked references|Published by|www\.|http|"
    r"^Source:|Accessed:", re.I)

ABBREV = re.compile(
    r"\b(e\.g|i\.e|cf|vs|et al|Fig|Eq|Sec|Ch|chap|pp|No|Vol|Dr|Mr|Ms|St|"
    r"approx|resp)\.$")


def strip_prose(text, is_qmd=False):
    """Return prose-only lines: no YAML, math displays, tables, headers, code."""
    lines = text.split("\n")
    out = []
    in_yaml = False
    in_math = False
    in_code = False
    for i, ln in enumerate(lines):
        s = ln.strip()
        if i == 0 and s == "---":
            in_yaml = True
            continue
        if in_yaml:
            if s == "---":
                in_yaml = False
            continue
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if s.startswith("$$"):
            # toggle for $$ ... $$ blocks; a one-line $$...$$ stays closed
            if not (len(s) > 2 and s.endswith("$$")):
                in_math = not in_math
            continue
        if in_math:
            continue
        if not s:
            continue
        if s.startswith("#") or s.startswith("|") or s.startswith("!["):
            continue
        if s.startswith(":::") or s.startswith(": ") or s.startswith("[^"):
            continue
        if BOILERPLATE.search(s):
            continue
        # drop lines that are mostly math/markup
        letters = sum(c.isalpha() for c in s)
        if letters < 0.5 * len(s):
            continue
        out.append(s)
    return " ".join(out)


def clean_for_sentences(prose):
    prose = re.sub(r"\$[^$]*\$", "MATH", prose)          # inline math -> token
    prose = re.sub(r"@[A-Za-z0-9_:\-]+", "CITE", prose)   # citekeys -> token
    prose = re.sub(r"\[[^\]]*\]\([^)]*\)", "REF", prose)  # md links
    prose = re.sub(r"[*_`]", "", prose)
    prose = re.sub(r"\s+", " ", prose)
    return prose.strip()


def split_sentences(prose):
    """Naive splitter with abbreviation guards."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", prose)
    sents = []
    buf = ""
    for p in parts:
        buf = (buf + " " + p).strip() if buf else p
        head = buf.rstrip()
        # if the fragment ends in an abbreviation, keep accumulating
        last = head.split()[-1] if head.split() else ""
        if ABBREV.search(last):
            continue
        sents.append(buf)
        buf = ""
    if buf:
        sents.append(buf)
    # keep real sentences only
    return [s for s in sents if len(s.split()) >= 3]


def syllables(word):
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    n = len(groups)
    if word.endswith("e") and n > 1:
        n -= 1
    return max(1, n)


SUBORD = re.compile(
    r"\b(although|though|while|because|since|whereas|unless|if|when|which|"
    r"that|so that|provided|given that)\b", re.I)


def corpus_stats(name, sents):
    words_per = [len(s.split()) for s in sents]
    nw = sum(words_per)
    ns = len(sents)
    all_words = " ".join(sents).split()
    nsyll = sum(syllables(w) for w in all_words)
    mean_wps = nw / ns
    med = sorted(words_per)[ns // 2]
    var = sum((x - mean_wps) ** 2 for x in words_per) / ns
    fk = 0.39 * (nw / ns) + 11.8 * (nsyll / nw) - 15.59
    commas = sum(s.count(",") for s in sents) / ns
    semis = 1000 * sum(s.count(";") for s in sents) / nw
    parens = 1000 * sum(s.count("(") for s in sents) / nw
    we = 1000 * len(re.findall(r"\b(we|our|us)\b",
                               " ".join(sents), re.I)) / nw
    sub = sum(len(SUBORD.findall(s)) for s in sents) / ns
    openers = {}
    for key in ("The", "This", "That", "It", "We", "A", "In", "For"):
        openers[key] = 100 * sum(
            1 for s in sents if s.split()[0].rstrip(",") == key) / ns
    long_share = 100 * sum(1 for x in words_per if x > 35) / ns
    short_share = 100 * sum(1 for x in words_per if x < 10) / ns
    return {
        "name": name, "sentences": ns, "words": nw,
        "mean_wps": mean_wps, "median_wps": med, "sd_wps": var ** 0.5,
        "long_pct": long_share, "short_pct": short_share, "fk": fk,
        "commas_per_sent": commas, "semis_per_1000w": semis,
        "parens_per_1000w": parens, "we_per_1000w": we,
        "subord_per_sent": sub, "openers": openers,
    }


def fmt_row(st):
    return (f"| {st['name']} | {st['sentences']} | {st['mean_wps']:.1f} | "
            f"{st['median_wps']} | {st['sd_wps']:.1f} | {st['long_pct']:.0f}% | "
            f"{st['short_pct']:.0f}% | {st['fk']:.1f} | "
            f"{st['commas_per_sent']:.2f} | {st['semis_per_1000w']:.1f} | "
            f"{st['parens_per_1000w']:.1f} | {st['we_per_1000w']:.1f} | "
            f"{st['subord_per_sent']:.2f} |")


def main():
    qmd = (ROOT / "manuscript" / "mi-spectral-apa.qmd").read_text(
        encoding="utf-8", errors="replace")
    man_prose = clean_for_sentences(strip_prose(qmd, is_qmd=True))
    man_sents = split_sentences(man_prose)
    man = corpus_stats("MANUSCRIPT", man_sents)

    ex_rows = []
    pooled = []
    for fn in EXEMPLARS:
        p = ROOT / "literature" / fn
        if not p.exists():
            print(f"MISSING: {fn}")
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        sents = split_sentences(clean_for_sentences(strip_prose(text)))
        pooled.extend(sents)
        ex_rows.append(corpus_stats(fn.replace(".md", ""), sents))
    pooled_stats = corpus_stats("EXEMPLARS (pooled)", pooled)

    hdr = ("| corpus | sents | mean w/s | med | sd | >35w | <10w | FK | "
           "commas/s | ;/1000w | (/1000w | we/1000w | subord/s |")
    sep = "|---" * 13 + "|"
    lines = ["# Register statistics: manuscript vs exemplars", "",
             "Prose-only lines; inline math -> MATH token; naive sentence "
             "splitter with abbreviation guards. Books include example/",
             "exercise text, so treat their rows as indicative.", "",
             hdr, sep, fmt_row(man), fmt_row(pooled_stats), ""]
    lines.append("## Per-exemplar")
    lines.extend(["", hdr, sep])
    for st in ex_rows:
        lines.append(fmt_row(st))
    lines.append("")
    lines.append("## Sentence-opener profile (% of sentences)")
    lines.append("")
    keys = ("The", "This", "That", "It", "We", "A", "In", "For")
    lines.append("| corpus | " + " | ".join(keys) + " |")
    lines.append("|---" * 9 + "|")
    for st in [man, pooled_stats]:
        lines.append("| " + st["name"] + " | " +
                     " | ".join(f"{st['openers'][k]:.1f}" for k in keys) + " |")
    out = ROOT / "verification" / "cache" / "style-register-stats.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"manuscript: {man['sentences']} sents, mean {man['mean_wps']:.1f} "
          f"w/s, FK {man['fk']:.1f}, commas/s {man['commas_per_sent']:.2f}")
    print(f"exemplars:  {pooled_stats['sentences']} sents, mean "
          f"{pooled_stats['mean_wps']:.1f} w/s, FK {pooled_stats['fk']:.1f}, "
          f"commas/s {pooled_stats['commas_per_sent']:.2f}")
    print(f"report -> {out}")


if __name__ == "__main__":
    main()
