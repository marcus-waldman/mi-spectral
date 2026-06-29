#!/usr/bin/env python3
r"""Assemble the canonical apaquarto-pdf manuscript from the CURRENT level3 prose.
This is the manuscript's official render. Targets apaquarto-pdf with documentmode: man and a
JAIGP-style TWO-CLASS author block (AI Authors / Prompters), rendered by overriding
apa7's \\displayauthors / \\displayaffiliations via header-includes. Only the
prompter carries an affiliation + ORCID. Output manuscript/mi-spectral-apa.qmd; render with `quarto render mi-spectral-apa.qmd`
from manuscript/ (apaquarto extension at manuscript/_extensions)."""
import json
from pathlib import Path

REPO = Path(r"C:/Users/marcu/git-repositories/mi-spectral")
L3 = REPO / "manuscript" / "plan" / "level3-paragraphs.json"
OUTDIR = REPO / "manuscript"
OUT = OUTDIR / "mi-spectral-apa.qmd"

doc = json.loads(L3.read_text(encoding="utf-8"))
ABSTRACT = doc.get("abstract") or "(abstract pending)"
sections = doc.get("sections_order") or []
paras = doc.get("paragraphs") or []
by_sec = {}
for p in paras:
    by_sec.setdefault(p.get("section"), []).append(p)

# Author note: two author classes + CRediT-style contributions (DRAFT roles).
GRAT = (
    "The journal recognizes two classes of author. The AI authors are the model "
    "lineages that produced the derivations, drafts, and computations and carried "
    "out the cross-model adversarial and Delphi review: Claude Opus 4.7–4.8 "
    "(Anthropic), GPT-5.5 Pro (OpenAI), and Gemini 3.1 Pro (Google). The prompter, "
    "Marcus Waldman, conceived and directed the work and is the ORCID-verified human "
    "prompter of record. Contributor roles (CRediT): Marcus Waldman -- "
    "conceptualization, supervision, validation, project administration; Claude Opus "
    "4.7–4.8 -- methodology, software, formal analysis, writing of the original "
    "draft; GPT-5.5 Pro and Gemini 3.1 Pro -- validation through cross-model review "
    "and Delphi consensus. The companion sourced derivation, the verification "
    "directory with its pre-registered studies, the cross-model grading records, and "
    "the full session transcripts are part of the public record, and citation "
    "discipline is enforced mechanically."
)

# Two-class title block. apa7 typesets the author block through \displayauthors and
# \displayaffiliations inside a centered box at \maketitle; we override both. AI
# authors carry no affiliation; only the prompter does. \setcounter neutralizes apa7's
# author-vs-superscript count check (guarded). \let\openbox\relax fixes the apa7-vs-
# amsthm clash.
HDR = r"""\let\openbox\relax
\makeatletter
\@ifundefined{c@NumberOfSuperscripts}{}{\setcounter{NumberOfSuperscripts}{0}}
\makeatother
\renewcommand{\displayauthors}{%
  {\bfseries AI Authors}\\[3pt]
  Claude Opus 4.7\textendash4.8\quad GPT-5.5 Pro\quad Gemini 3.1 Pro\\[11pt]
  {\bfseries Prompters}\\[3pt]
  Marcus Waldman%
}
\renewcommand{\displayaffiliations}{%
  Center for Innovative Design and Analysis, Department of Biostatistics and Informatics, Colorado School of Public Health, University of Colorado Anschutz Medical Campus, Aurora, CO%
}
\leftheader{Waldman et al.}"""


def block(text, indent):
    pad = " " * indent
    return "\n".join(pad + ln for ln in text.split("\n"))


grat_block = block(GRAT, 6)
abs_block = block(ABSTRACT, 2)
hdr_block = block(HDR, 4)

front = f"""---
title: "Model selection after multiple imputation: a deviance correction for AIC, BIC, and likelihood-ratio tests"
shorttitle: "Model selection after multiple imputation"
author:
  - name: Marcus Waldman
    corresponding: true
    orcid: 0000-0002-3288-4803
    email: marcus.waldman@cuanschutz.edu
    affiliations:
      - id: id1
        name: University of Colorado Anschutz Medical Campus
        department: "Center for Innovative Design and Analysis, Department of Biostatistics and Informatics, Colorado School of Public Health"
        city: Aurora
        region: CO
  - name: Claude Opus 4.7–4.8
  - name: GPT-5.5 Pro
  - name: Gemini 3.1 Pro
author-note:
  disclosures:
    gratitude: |
{grat_block}
abstract: |
{abs_block}
keywords: [multiple imputation, model selection, likelihood-ratio test, information criterion, missing data]
documentmode: man
header-includes:
  - |
{hdr_block}
format:
  apaquarto-pdf:
    keep-tex: true
    number-sections: true
    number-depth: 1
bibliography: ../literature/mi-spectral-better-bibTeX.bib
---
"""

body = [front.rstrip("\n")]
for s in sections:
    sid = s.get("id")
    if sid == "FRONT":
        continue
    body.append("")
    body.append(f"# {s.get('title')} {{#{s.get('anchor')}}}")
    for p in by_sec.get(sid, []):
        prose = p.get("draft_prose")
        if prose is None:
            continue
        body.append("")
        body.append(prose.rstrip("\n"))

OUTDIR.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(body) + "\n", encoding="utf-8")
n = sum(len(by_sec.get(s.get("id"), [])) for s in sections if s.get("id") != "FRONT")
print(f"wrote {OUT} ({n} paragraphs across "
      f"{len([s for s in sections if s.get('id') != 'FRONT'])} sections)")
