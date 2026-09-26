# Vibe Researching: A Reproducibility Protocol, Agent Skill, and Epistemic Audit Engine for Humanities & Social-Science Quantitative Analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22978433.svg)](https://doi.org/10.5281/zenodo.22978433)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-blue)](https://huggingface.co/datasets/giabaohuynhasu/vibe-researching)

### Bridging the gap between a qualitative humanities question and a fully reproducible, epistemically audited quantitative analysis

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

**Vibe Researching** is an agent skill, reproducible-research framework, and automated epistemic audit system designed for researchers who work in humanities and social-science fields — philosophy, political theory, comparative jurisprudence, institutional analysis, and area studies — and want to move from a conceptual research question to a real quantitative analysis (fitting a model, testing a hypothesis, analyzing a dataset) without losing ownership of substantive intellectual decisions along the way.

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
8. **The Third-Order Epistemic Audit (Step 8)**: Automated, stateless verification across Popperian falsifiability (Order 1), Mertonian external grounding and escape-route closure (Order 2), and Lakatosian research trajectory progressiveness (Order 3).

---

## 📂 Repository Structure

```
vibe-researching/
├── SKILL.md                          # The core agent skill definition (8 steps)
├── audit/                            # Third-Order Audit engine (Huynh 2026)
│   ├── sandbox.py                    # Core research sandbox & multi-order audit engine
│   ├── vibe_audit.py                 # Bridge & CLI for auditing Vibe Researching projects
│   ├── SPEC.md                       # Formal audit specification & mapping standards
│   ├── example_corpus.json           # Reference test corpus
│   ├── test_sandbox.py               # Engine unit tests (16 tests)
│   └── test_vibe_audit.py            # Integration tests for project audits
├── vibe-researching-skill/           # Installable skill distribution package
│   ├── SKILL.md                      # Skill instructions (with template references)
│   └── templates/                    # Blank standardized templates
│       ├── research_question.md      # Prerequisite question-framing gate
│       ├── decision_card.md          # Substantive choice record template
│       ├── research_log_entry.md     # Contemporaneous session log template
│       ├── third_order_audit_report.md # Epistemic audit report template
│       ├── README.md                 # Project root template
│       └── CITATION.cff              # Citation metadata template
├── demo-project/                     # Complete end-to-end worked demonstration
│   ├── research_question.md          # Completed research question
│   ├── audit/                        # Automated third-order audit artifacts
│   │   ├── third_order_audit_report.md
│   │   └── audit_object.json
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

## 🔬 The 8-Step Protocol

| Step | Phase | Function & Enforcement |
|:---:|:---|:---|
| **0** | **Recognize** | Activates when a researcher from a qualitative/humanities discipline initiates a project without an existing codebase. |
| **1** | **Research Question Gate** | Halts technical execution until `research_question.md` is agreed upon: defining Question, Theoretical Claim, Model Justification, Identifying Assumptions, Falsification Criteria, and Reproducibility Specifications. |
| **2** | **Scaffold Project** | Establishes standard directory layout. Enforces strict write-protection on `data/raw/`. |
| **3** | **Numbered Pipeline** | Enforces chronological script naming (`01_`, `02_`, `03_`), narrating the complete analytical trajectory. |
| **4** | **Decision Cards** | Requires a stand-alone decision record in `analysis/models/` for any substantive analytical fork. |
| **5** | **Research Log** | Records real-time decisions, rejected alternatives, and open questions during the working session. |
| **6** | **The Hard Rule** | Mandatory pause on any fork that could alter conclusions. AI must present options with trade-offs; silent picking is forbidden. |
| **7** | **Living Closeout** | Synchronizes status, citations, and outputs into `README.md` and `CITATION.cff` at every natural checkpoint. |
| **8** | **The Third-Order Audit** | Programmatic verification: Order 1 (Popperian falsifiability), Order 2 (Mertonian grounding / closed escape routes), and Order 3 (Lakatosian Constraint Ratio across session revisions). |

---

## 🛡️ The Third-Order Epistemic Audit (Huynh 2026)

The Third-Order Audit engine (`audit/vibe_audit.py`, built upon `audit/sandbox.py`) provides rigorous, automated verification of a project's epistemic integrity across three philosophical orders:

### 1. Order 1 (Karl Popper) -- Object-Level Falsifiability
- **Principle**: A scientific hypothesis must specify empirical observations that would refute it.
- **Audit Verification**: Inspects `research_question.md` to verify that an explicit falsification condition ($F_1 \dots F_k$) is formally articulated (rejecting placeholders, tautologies, or unfalsifiable formulations).

### 2. Order 2 (Robert K. Merton / *The Price of a Promise*) -- Mechanism-Level Grounding & Closed Escape Routes
- **Principle**: Falsification criteria must point outward to independent external reality rather than collapsing into circular, model-internal jargon.
- **Audit Verification**:
  - Confirms external anchors in `data/raw/` and authoritative citations in `references/`.
  - Verifies that analytical escape routes are closed by confirming that decision cards in `analysis/models/` document counterfactual options and explain the exact sensitivity of conclusions.
  - Monitors for **Third Break boundary risk**: flags hypotheses that rely on model-internal queries without empirical validation.

### 3. Order 3 (Imre Lakatos / *The Artifact Problem*) -- Programme-Level Trajectory
- **Principle**: Distinguishes **progressive** research programmes from **degenerating** ones across time. Progressive programmes respond to empirical anomalies by narrowing their claims or withdrawing refuted assertions; degenerating programmes preserve initial dogmas through ad-hoc protective belt additions.
- **Audit Verification**: Evaluates multi-session entries in `research_log/log.md`, classifying each revision into:
  - `NARROWED`: Scope or claim strength reduced under empirical tension.
  - `WITHDRAWN`: Claim explicitly abandoned.
  - `REAFFIRMED`: Claim retained unchanged despite testing.
  - `EXTENDED`: New hypothesis or expansion.
- **The Lakatosian Constraint Ratio**:
  $$\text{Constraint Ratio} = \frac{\text{Narrowed} + \text{Withdrawn}}{\text{Total Revisions}}$$
  - $\text{Ratio} > 0$: **Progressive** programme (empirical evidence actively constrains claims).
  - Repeated `REAFFIRMED` with $\text{Ratio} = 0$: **Degenerating Risk** (confirmation bias / protective insulation).

### The Stateless Auditor Advantage
Human researchers naturally experience escalation of commitment (Staw 1976) and motivated reasoning (Kunda 1990) to defend decisions they previously invested effort into. A fresh, stateless AI instance executing the Third-Order Audit has zero personal attachment or sunk cost in prior conclusions, enabling unbiased structural verification.

### Running the Audit
```bash
# Audit any Vibe Researching project folder
python audit/vibe_audit.py demo-project

# Run the complete test suite
python -m unittest audit/test_sandbox.py audit/test_vibe_audit.py
```

Sample audit output:
```markdown
# Third-Order Epistemic Audit Report: demo-project

## 📊 Audit Scorecard

| Level | Order Name | Status | Evaluated Metric / Criterion |
| :--- | :--- | :---: | :--- |
| **Order 1** | **Object-Level Falsification** | **✅ PASS** | Explicit falsification condition stated in `research_question.md` |
| **Order 2** | **External Grounding & Escape Routes** | **✅ PASS** | Outward linkage to independent data/records; closed analytical escape routes |
| **Order 3** | **Programme-Level Lakatosian Trajectory** | **ℹ️ BASELINE** | Constraint Ratio = `0.000` (0 narrowed/withdrawn of 1 total revisions) — Initial baseline established |
```

---

## 🎯 Demo Walkthrough

The repository includes a complete empirical demonstration (`demo-project/`) analyzing household income vs. life expectancy:
- **Empirical Question**: Does household income predict longevity, and what is the magnitude of association?
- **Model**: OLS regression of life expectancy on log-transformed household income.
- **Surfaced Decision (Step 6)**: Influence diagnostics identified 12 high-leverage observations at extreme income brackets.
- **Deliberation & Resolution**: Rather than arbitrarily dropping points or silently applying robust errors, the researcher chose a tripartite comparison (baseline OLS, HC3 heteroskedasticity-robust SEs, and leverage-excluded OLS).
- **Result**: Demonstrated empirical stability across all three specifications (slopes: 2.696 vs. 2.696 vs. 2.624; <2.7% divergence), establishing robust conclusions without obscured data deletion.
- **Epistemic Audit (Step 8)**: Automated evaluation in `demo-project/audit/` confirms Order 1 pass (explicit slope threshold for falsification), Order 2 pass (anchored to raw observation records and decision card sensitivity tests), and Order 3 baseline tracking.

### Executing the Demonstration
```bash
cd demo-project
pip install pandas numpy statsmodels matplotlib
python analysis/scripts/01_generate_data.py
python analysis/scripts/02_clean_data.py
python analysis/scripts/03_fit_model.py
python analysis/scripts/04_robustness_check.py
python analysis/scripts/05_make_figure.py
cd ..
python audit/vibe_audit.py demo-project
```

---

## 🏛️ Intellectual Context & Authorship

This framework and audit architecture were developed by **Gia Bao Huynh** (`huynhbao@asu.edu`, ORCID: [0009-0008-2372-5852](https://orcid.org/0009-0008-2372-5852)) during the empirical investigations of *The Floor That Does Not Rise* and *The Third-Order Audit* research programs.

Conducting complex quantitative modelling alongside generative AI assistants revealed that speed of synthesis often masks epistemic capture: technical co-pilots routinely make foundational theoretical compromises under the guise of syntax completion. **Vibe Researching** codifies a protocol of **epistemic sovereignty**, ensuring non-programmer scholars retain total ownership, methodological clarity, and transparent accountability over their scientific claims.

---

## 📜 Citation

```bibtex
@software{huynh2026viberesearching,
  author       = {Huynh, Gia Bao},
  title        = {Vibe Researching: A Reproducibility Protocol, Agent Skill, and Epistemic Audit Engine for Humanities and Social-Science Quantitative Analysis},
  month        = sep,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {2.1.0},
  doi          = {10.5281/zenodo.22978433},
  url          = {https://doi.org/10.5281/zenodo.22978433}
}
```

---

## ⚖️ License

Distributed under the [MIT License](LICENSE).
