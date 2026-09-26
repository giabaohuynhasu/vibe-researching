# Vibe Researching: A Reproducibility Skill for Humanities & Social-Science Quantitative Analysis

### Bridging the gap between a humanities research question and a reproducible quantitative analysis

**Author**: Gia Bao Huynh  
*Independent Researcher, Ho Chi Minh City, Vietnam*  
*Email: huynhbao@asu.edu · ORCID: [0009-0008-2372-5852](https://orcid.org/0009-0008-2372-5852)*  
*Research Stance: Challenging the unchecked power, epistemic asymmetries, and monopolized governance of non-state actors across frontier technologies.*  
*Collaborator: Claude (Anthropic)*

**Repositories**:
- 🌐 **GitHub**: [https://github.com/giabaohuynhasu/vibe-researching](https://github.com/giabaohuynhasu/vibe-researching)
- 🌐 **Hugging Face Hub**: [https://huggingface.co/datasets/giabaohuynhasu/vibe-researching](https://huggingface.co/datasets/giabaohuynhasu/vibe-researching)

---

## 📌 What This Is

**Vibe Researching** is an agent skill and reproducible-research framework designed for researchers who work in humanities and social-science fields — philosophy, political theory, comparative jurisprudence, area studies — and want to move from a research question to a real quantitative analysis (fitting a model, testing a hypothesis, analyzing a dataset) without losing ownership of the substantive intellectual decisions along the way.

The core problem it solves: AI coding assistants can generate project scaffolding, cleaning scripts, model fits, and plots faster than a non-programmer could build them by hand. But that speed creates a dangerous failure mode — the assistant silently makes the researcher's own judgment calls (what the question really is, what model assumptions mean, what evidence would falsify the claim) while generating the technical work, and the researcher never sees that a decision was made at all.

**Vibe Researching enforces a small number of mandatory checkpoints** that keep the technical scaffolding work separate from the researcher's substantive decisions:

1. **Mandatory research question gate** — `research_question.md` must be collaboratively filled in before any code is written
2. **Decision cards** — every substantive analytical choice gets a separately readable record
3. **Timestamped research log** — written during the session, not reconstructed afterward
4. **The hard rule** — never decide a substantive choice silently; always surface alternatives to the researcher

---

## 📂 Repository Structure

```
vibe-researching/
├── SKILL.md                          # The agent skill definition (7 steps)
├── vibe-researching-skill/           # Installable skill package
│   ├── SKILL.md                      # Skill instructions (with template references)
│   └── templates/                    # Blank templates for new projects
│       ├── research_question.md
│       ├── decision_card.md
│       ├── research_log_entry.md
│       ├── README.md
│       └── CITATION.cff
├── demo-project/                     # Complete worked example
│   ├── research_question.md          # Filled-in research question
│   ├── analysis/
│   │   ├── scripts/                  # Numbered pipeline (01–05)
│   │   └── models/                   # Decision cards
│   ├── data/
│   │   ├── raw/                      # Untouched original data
│   │   └── processed/               # Cleaned data (from scripts only)
│   ├── figures/                      # Generated plots
│   ├── research_log/log.md           # Session-by-session record
│   ├── README.md
│   └── CITATION.cff
└── LICENSE
```

---

## 🔬 The 7-Step Protocol

| Step | Name | Purpose |
|------|------|---------|
| 0 | **Recognize** | Trigger only when a non-technical researcher brings a research question without an existing codebase |
| 1 | **Research Question Gate** | Collaboratively fill `research_question.md` before any code — question, claim, model rationale, assumptions, falsification, reproducibility |
| 2 | **Scaffold** | Create project structure with `raw/` → `processed/` data boundary |
| 3 | **Numbered Scripts** | `01_clean.py`, `02_fit.py`, `03_plot.py` — the analysis story is readable from filenames alone |
| 4 | **Decision Cards** | Every choice that could change the result gets a separately readable record |
| 5 | **Research Log** | Dated entries written *during* the session, not reconstructed afterward |
| 6 | **The Hard Rule** | Never decide a substantive choice silently — surface 2–3 alternatives with implications |
| 7 | **Living README** | Keep README and CITATION.cff current at every natural stopping point |

---

## 🎯 Demo Walkthrough

The `demo-project/` directory contains a complete worked example using synthetic income–life expectancy data:

- **Research question**: Does household income predict life expectancy?
- **Model**: OLS regression of life expectancy on log(income)
- **Key decision surfaced**: How to handle 12 high-leverage points flagged by influence diagnostics
- **Researcher's choice**: Run all three scenarios (as-is, HC3 robust SEs, leverage-excluded) and report the spread
- **Finding**: Coefficient stable across all three (2.696, 2.696, 2.624 — 2.7% spread)

Run the demo:
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

## 🏗️ Intellectual Context

This skill emerged from the author's own experience conducting the *Floor That Does Not Rise* research program — a queueing-theoretic analysis of technological inequality across housing, AI, biotech, and cybersecurity — as a non-programmer political theorist working with AI coding assistants. The realization that an assistant could silently choose a model specification, a variable transformation, or an outlier threshold while appearing to simply "help with the code" led to the explicit separation of technical scaffolding from substantive judgment that this skill enforces.

The framework operationalizes the principle that **speed of code generation is not the bottleneck — transparency of analytical choices is**.

---

## 📜 Citation

```bibtex
@software{huynh2026viberesearching,
  author    = {Gia Bao Huynh},
  title     = {Vibe Researching: A Reproducibility Skill for Humanities and Social-Science Quantitative Analysis},
  year      = {2026},
  url       = {https://github.com/giabaohuynhasu/vibe-researching},
  note      = {Agent skill and reproducible-research framework}
}
```

---

## ⚖️ License

This project is licensed under the [MIT License](LICENSE).
