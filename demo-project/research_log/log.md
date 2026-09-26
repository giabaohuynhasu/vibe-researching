## 2026-09-26

**What was tried:** Generated synthetic income/life-expectancy data (400 obs), cleaned it (no drops needed), fit OLS of life expectancy on log(income) as specified in `research_question.md`.

**What was decided, and why:** Log-transform of income was decided in advance (Step 1), because income-health effects are widely reported as diminishing at higher incomes.

**What was rejected, and why:** Nothing rejected yet -- this is the first pass.

**Open questions carried to next session:** The influence diagnostic flagged 12 high-leverage points, concentrated at both income extremes. Whether to (a) report the model as fit, (b) refit with heteroskedasticity-robust standard errors, or (c) investigate the high-leverage points as possible outliers before trusting the estimate is a substantive choice not yet made -- surfaced to the researcher rather than decided here (see chat).

---

**Continued same day, after researcher input:** Researcher chose to run all three scenarios rather than pick one (see `analysis/models/decision_leverage_points.md`). Coefficient on log-income: 2.696 (as-is) / 2.696 (HC3 robust) / 2.624 (leverage points excluded) -- a 2.7% spread. The finding is not sensitive to this choice. Figure and closing README done; this demo walkthrough is complete.
