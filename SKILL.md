---
name: vibe-researching
description: Use when someone without a coding or statistics background wants to move from a research question -- often in philosophy, political theory, or another humanities or social-science field -- to a real quantitative analysis: fitting a model, testing a hypothesis, analyzing a dataset, and wanting the result to be reproducible by someone else later. This skill inserts a mandatory question-framing step before any code is written, keeps a timestamped research log, and requires surfacing every substantive analytical choice to the person rather than deciding it silently. Do not trigger this skill if the person already has their own codebase or pipeline and is asking for a targeted fix or a quick extension to it -- in that case just help directly.
---

# Vibe Researching for Humanities & Social Science

## The rule this skill exists to enforce

Claude can generate the technical scaffolding of a research project far faster than a non-programmer researcher could build it by hand: the folder structure, the cleaning script, the model call, the plot. What Claude must never do is quietly make the researcher's own substantive judgment calls while doing that -- what the question actually is, what would count as a good answer, what assumptions a chosen model smuggles in, what evidence would show the whole thing is wrong. Those calls belong to the researcher. This skill's only job is to keep the two kinds of work from blurring together, by forcing a small number of checkpoints that a purely technical workflow would skip.

The person using this skill is trusted to be capable of making these calls once they are put in front of them clearly. The failure mode this skill prevents is not "the researcher is incapable" -- it is "Claude filled in a judgment call by default because stopping to ask felt like friction."

## Step 0 -- Recognize when this applies

Trigger when someone brings a research question from a non-technical field and wants to test it against data or fit it to a model, and does not already have a codebase of their own for this project. Signals: they describe a hypothesis or a claim they want to check rather than a specific piece of code they want written; they mention a dataset (uploaded, or one they plan to find) without yet having a script; they say something close to "I don't really code" or "I'm not a stats person" in the same breath as wanting an analysis.

Do not trigger, and just help directly instead, when the person already has a repository, a script, or an established pipeline for this project and is asking to extend, fix, or debug it. This skill governs how a project *starts*, not every subsequent edit to it.

## Step 1 -- The mandatory gate: research_question.md before any code

Before writing a single line of analysis code or touching the data, create `research_question.md` in the project root and fill it in together with the person. Do not skip this because the person is eager to see results, and do not fill it in on their behalf and present it as a fait accompli -- draft your best attempt at each field from what they have said so far, then show it to them and ask them to correct it before moving on. The file must answer, in plain language:

- **Question.** What is actually being asked, in one or two sentences a non-specialist could understand.
- **Claim.** If there is a causal or comparative claim (X affects Y, group A differs from group B), state it explicitly. If the project is exploratory rather than claim-testing, say that instead of forcing a claim into existence.
- **Model and why.** What kind of model or test is planned, and why this one rather than an obvious alternative. "Because it's standard for this kind of data" is an acceptable answer if true, but say so explicitly rather than leaving the choice unexplained.
- **Assumptions.** What the model or test assumes about the data or the world that, if false, would undermine the results. List the ones that are actually plausible risks for this dataset, not a generic textbook list.
- **Falsification.** What result, if observed, would count against the claim. If the person cannot answer this yet, that is a signal to slow down before writing code, not a box to leave blank.
- **Reproducibility check.** What another person would need -- files, package versions, a data source -- to run this again in six months and get the same result.

## Step 2 -- Scaffold the project

Once `research_question.md` is agreed, create the project structure:

```
project/
├── README.md
├── research_question.md
├── hypotheses.md
├── data/
│   ├── raw/
│   └── processed/
├── analysis/
│   ├── scripts/
│   └── models/
├── figures/
├── results/
├── references/
├── research_log/
└── CITATION.cff
```

Never write into `data/raw/` after the initial data is placed there. All cleaning and transformation happens in scripts that read from `raw/` and write to `processed/`, so the path from original data to any figure is always reconstructible from code rather than from memory of what was clicked or edited by hand.

## Step 3 -- Write analysis code with a numbered-script convention

Scripts in `analysis/scripts/` are numbered in the order they must run: `01_clean_data.py`, `02_fit_model.py`, `03_make_figures.py`, and so on. Each script does one identifiable job and says so at the top in a comment. A person who has never seen the project should be able to tell the whole story of the analysis by reading the filenames in order, before reading a single line of code inside them.

## Step 4 -- A decision card for every substantive choice

A choice is substantive if a different reasonable choice could plausibly have changed the result: which model family, which variables to include or exclude, which observations to drop, which threshold counts as significant, which transformation to apply to a variable. For each one, write a short decision card into `analysis/models/` (or append to an existing one for that script) with: what was chosen, what the plausible alternatives were, why this one, and what would change if a different alternative had been picked instead. This is not a comment buried in code. It is a short, separately readable note, because the person relying on it should not have to read source code to find out that a decision was made at all.

## Step 5 -- The research log

Every working session gets one dated entry appended to `research_log/log.md`, in the form:

```
## YYYY-MM-DD
- What was tried:
- What was decided, and why:
- What was rejected, and why:
- Open questions carried to next session:
```

This is not a summary written at the end of the project. It is written as the session happens, because its value is in showing what was known at the time a decision was made, not a reconstruction after the fact that already knows how things turned out.

## Step 6 -- The hard rule: never decide a substantive choice silently

When a substantive choice (Step 4's definition) comes up during the work, stop and present it to the person before proceeding, with two or three concrete, genuinely reasonable options and what each implies for the result -- not a single default framed as the obvious answer. Proceed only once they pick, and record the pick as a decision card. This is the one step in this skill that overrides ordinary efficiency: taking longer here is the point, not a cost to be minimized. A researcher who was never shown the choice cannot be said to have made it, however clearly it gets written up afterward.

## Step 7 -- Close out: README and CITATION.cff

At natural stopping points -- not only at the very end -- update the project's top-level `README.md` to reflect current status (what question, what data, what's done, what's open), and keep `CITATION.cff` current with the project's title, author, and date so the work is citable at whatever stage it is in. Treat both as living documents updated as part of the work, not paperwork left for the end.
