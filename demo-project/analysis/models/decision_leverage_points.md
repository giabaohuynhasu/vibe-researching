# Decision: How to handle the 12 high-leverage points flagged after the first model fit

**Script / context:** `analysis/scripts/03_fit_model.py` -> `04_robustness_check.py`
**Date:** 2026-09-26

## What was chosen

Run all three scenarios raised at the Step 6 stop rather than committing to one in advance: (1) the original fit as-is, (2) the same fit with HC3 heteroskedasticity-robust standard errors, (3) the fit with the 12 flagged high-leverage points excluded. Compare the coefficient on log-income across all three and report the spread, rather than choosing a single "correct" specification upfront.

## Plausible alternatives considered

1. Report the as-is model only, footnoting the high-leverage points.
2. Refit once with HC3 robust SEs and stop there.
3. Exclude the high-leverage points and treat that as the "real" model.
4. (Chosen) Run all three and report whether the substantive conclusion depends on the choice.

## Why this one

The researcher's own goal was not to find the single most defensible specification but to know whether the answer changes depending on which reasonable choice is made. Running all three answers that directly, rather than deferring to whichever specification is chosen and leaving the sensitivity unexamined.

## What would change if a different alternative had been picked

If only the as-is model (alternative 1) had been reported, a reader would have no way to know the coefficient was stable to the leverage points -- the robustness would be asserted, not shown. Picking alternative 3 alone would have silently thrown away 12 real observations without ever checking whether doing so mattered. In this dataset the three scenarios turned out to agree closely (2.696, 2.696, 2.624 -- a 2.7% spread), so the choice among them does not change the substantive conclusion here. That agreement is itself the finding this decision was trying to produce, and it would not have been visible under any single one of the three alternatives.
