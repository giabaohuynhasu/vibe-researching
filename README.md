# Vibe Researching: A Reproducibility Protocol and Agent Skill for Humanities & Social-Science Quantitative Analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22978433.svg)](https://doi.org/10.5281/zenodo.22978433)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-blue)](https://huggingface.co/datasets/giabaohuynhasu/vibe-researching)

### Bridging the gap between a qualitative humanities question and a fully reproducible quantitative analysis

**Author**: Gia Bao Huynh  
*Independent Researcher, Ho Chi Minh City, Vietnam*  
*Email: huynhbao@asu.edu · ORCID: [0009-0008-2372-5852](https://orcid.org/0009-0008-2372-5852)*  
*Research Stance: Challenging the unchecked power, epistemic asymmetries, and monopolized governance of non-state actors across frontier technologies.*  
*Collaborator: Claude (Anthropic)*

**Persistent Identifiers & Repositories**:
- 🏛️ **Zenodo DOI**: [10.5281/zenodo.22978433](https://doi.org/10.5281/zenodo.22978433)
- 🌐 **GitHub**: [https://github.com/giabaohuynhasu/vibe-researching](https://github.com/giabaohuynhasu/vibe-researching)
- 🤗 **Hugging Face Hub**: [https://huggingface.co/datasets/giabaohuynhasu/vibe-researching](https://huggingface.co/datasets/giabaohuynhasu/vibe-researching)

---

## 📌 What This Is

**Vibe Researching** is an agent skill and reproducible-research framework designed for researchers who work in humanities and social-science fields — philosophy, political theory, comparative jurisprudence, institutional analysis, and area studies — and want to move from a conceptual research question to a real quantitative analysis (fitting a model, testing a hypothesis, analyzing a dataset) without losing ownership of substantive intellectual decisions along the way.

### The Problem It Solves
AI coding assistants can generate project scaffolding, data cleaning pipelines, econometric model calls, and diagnostic plots far faster than a non-programmer could build them by hand. However, that mechanical speed introduces an acute epistemic failure mode: **the AI system silently resolves the researcher's substantive theoretical choices by default** (e.g., implicitly selecting model functional forms, omitting confounders, establishing outlier exclusion cutoffs, or adopting arbitrary significance thresholds) without the researcher ever realizing a consequential decision was made.

### The Mechanism
**Vibe Researching enforces mandatory epistemic checkpoints** that strictly isolate technical scaffolding generation from the researcher's theoretical sovereignty:

1. **Mandatory Research Question Gate (Step 1)**: Collaborative completion of `research_question.md` before any code is written or data is touched.
2. **Strict Raw-to-Processed Separation (Step 2)**: Immutable `data/raw/` storage with reproducible scripted pipelines.
3. **Ordered-Script Workflow (Step 3)**: Sequential execution (`01_clean_data.py`, `02_fit_model.py`, etc.) making analytical provenance transparent.
4. **Substantive Decision Cards (Step 4)**: Explicit documentation of every choice capable of shifting empirical conclusions, detailing alternatives and counterfactuals.
5. **Contemporaneous Research Log (Step 5)**: Real-time session logging recording actual deliberation, not retrospective rationalization.
6. **The Anti-Default Hard Rule (Step 6)**: AI systems are strictly prohibited from silently resolving substantive choices; they must pause and surface 2–3 defensible alternatives with empirical trade-offs.
7. **Living Documentation (Step 7)**: Continuous maintenance of `README.md` and `CITATION.cff`.

---

## 📂 Repository Structure

```
vibe-researching/
├── SKILL.md                          # The core agent skill definition (7 steps)
├── vibe-researching-skill/           # Installable skill distribution package
│   ├── SKILL.md                      # Skill instructions (with template references)
│   └── templates/                    # Blank standardized templates
│       ├── research_question.md      # Prerequisite question-framing gate
│       ├── decision_card.md          # Substantive choice record template
│       ├── research_log_entry.md     # Contemporaneous session log template
│       ├── README.md                 # Project root template
│       └── CITATION.cff              # Citation metadata template
├── demo-project/                     # Complete end-to-end worked demonstration
│   ├── research_question.md          # Completed research question
│   ├── analysis/
│   │   ├── scripts/                  # Numbered reproducible pipeline (01–05)
│   │   │   ├── 01_generate_data.py
│   │   │   ├── 02_clean_data.py
│   │   │   ├── 03_fit_model.py
│   │   │   ├── 04_robustness_check.py
│   │   │   └── 05_make_figure.py
│   │   └── models/                   # Formal decision cards
│   │       └── decision_leverage_points.md
│   ├── data/
│   │   ├── raw/                      # Untouched raw observation data
│   │   └── processed/                # Pipeline-generated clean data
│   ├── figures/                      # High-resolution publication plots
│   │   └── income_lifespan_fit.png
│   ├── research_log/                 # Real-time session documentation
│   │   └── log.md
│   ├── README.md
│   └── CITATION.cff
├── CITATION.cff                      # Master citation metadata
├── LICENSE                           # MIT License
└── README.md                         # Project documentation
```

---

## 🔬 The 7-Step Protocol

| Step | Phase | Function & Enforcement |
|:---:|:---|:---|
| **0** | **Recognize** | Activates when a researcher from a qualitative/humanities discipline initiates a project without existing codebase. |
| **1** | **Research Question Gate** | Halts technical execution until `research_question.md` is agreed upon: defining Question, Theoretical Claim, Model Justification, Identifying Assumptions, Falsification Criteria, and Reproducibility Specifications. |
| **2** | **Scaffold Project** | Establishes standard directory layout. Enforces strict write-protection on `data/raw/`. |
| **3** | **Numbered Pipeline** | Enforces chronological script naming (`01_`, `02_`, `03_`), narrating the complete analytical trajectory. |
| **4** | **Decision Cards** | Requires a stand-alone decision record in `analysis/models/` for any substantive analytical fork. |
| **5** | **Research Log** | Records real-time decisions, rejected alternatives, and open questions during the working session. |
| **6** | **The Hard Rule** | Mandatory pause on any fork that could alter conclusions. AI must present options with trade-offs; silent picking is forbidden. |
| **7** | **Living Closeout** | Synchronizes status, citations, and outputs into `README.md` and `CITATION.cff` at every natural checkpoint. |

---

## 🎯 Demo Walkthrough

The repository includes a complete empirical demonstration (`demo-project/`) analyzing household income vs. life expectancy:

- **Empirical Question**: Does household income predict longevity, and what is the magnitude of association?
- **Model**: OLS regression of life expectancy on log-transformed household income.
- **Surfaced Decision (Step 6)**: Influence diagnostics identified 12 high-leverage observations at extreme income brackets.
- **Deliberation & Resolution**: Rather than arbitrarily dropping points or silently applying robust errors, the researcher chose a tripartite comparison (baseline OLS, HC3 heteroskedasticity-robust SEs, and leverage-excluded OLS).
- **Result**: Demonstrated empirical stability across all three specifications (slopes: 2.696 vs. 2.696 vs. 2.624; <2.7% divergence), establishing robust conclusions without obscured data deletion.

### Executing the Demonstration
```bash
cd demo-project
pip install pandas numpy statsmodels matplotlib
python analysis/scripts/01_generate_data.py
python analysis/scripts/02_clean_data.py
python analysis/scripts/03_fit_model.py
python analysis/scripts/04_robustness_check.py
python analysis/scripts/05_make_figure.py
```

---

## 🏛️ Intellectual Context & Authorship

This framework was developed during the empirical investigations of *The Floor That Does Not Rise* research program — an interdisciplinary queueing-theoretic critique of technological acceleration across housing markets, synthetic AI capabilities, longevity biotechnology, and national-scale cybersecurity.

Conducting complex quantitative modelling alongside generative AI assistants revealed that speed of synthesis often masks epistemic capture: technical co-pilots routinely make foundational theoretical compromises under the guise of syntax completion. **Vibe Researching** codifies a protocol of **epistemic sovereignty**, ensuring non-programmer scholars retain total ownership and transparent accountability over their scientific claims.

---

## 📜 Citation

```bibtex
@software{huynh2026viberesearching,
  author       = {Huynh, Gia Bao},
  title        = {Vibe Researching: A Reproducibility Protocol and Agent Skill for Humanities and Social-Science Quantitative Analysis},
  month        = sep,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {2.0.0},
  doi          = {10.5281/zenodo.22978433},
  url          = {https://doi.org/10.5281/zenodo.22978433}
}
```

---

## ⚖️ License

Distributed under the [MIT License](LICENSE).
