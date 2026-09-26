"""
03_fit_model.py
Fits the planned OLS model (life_expectancy ~ log(income)) and checks
diagnostics before accepting the result. Per the skill's Step 6, this script
stops short of a final answer if a substantive choice shows up that a
different reasonable choice could change -- that choice gets surfaced to the
researcher rather than picked by default.
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv("data/processed/clean_income_lifespan.csv")
df["log_income"] = np.log(df["household_income_usd"])

X = sm.add_constant(df["log_income"])
y = df["life_expectancy_years"]
model = sm.OLS(y, X).fit()
print(model.summary())

influence = model.get_influence()
leverage = influence.hat_matrix_diag
threshold = 3 * X.shape[1] / len(df)
high_leverage = df[leverage > threshold]
print(f"\n{len(high_leverage)} high-leverage point(s) flagged out of {len(df)} (threshold {threshold:.4f}):")
print(high_leverage[["household_income_usd", "life_expectancy_years"]].to_string())
