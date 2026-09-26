"""
05_make_figure.py
Scatter of income vs life expectancy with the fitted line, marking the
high-leverage points examined in the robustness check.
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/clean_income_lifespan.csv")
df["log_income"] = np.log(df["household_income_usd"])
X = sm.add_constant(df["log_income"])
y = df["life_expectancy_years"]
m1 = sm.OLS(y, X).fit()
leverage = m1.get_influence().hat_matrix_diag
threshold = 3 * X.shape[1] / len(df)
flagged = leverage > threshold

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df.loc[~flagged, "household_income_usd"], df.loc[~flagged, "life_expectancy_years"],
           alpha=0.5, s=18, label="observation")
ax.scatter(df.loc[flagged, "household_income_usd"], df.loc[flagged, "life_expectancy_years"],
           color="crimson", s=40, label="flagged high-leverage")
x_line = np.linspace(df["household_income_usd"].min(), df["household_income_usd"].max(), 200)
y_line = m1.params["const"] + m1.params["log_income"] * np.log(x_line)
ax.plot(x_line, y_line, color="black", linewidth=1.5, label="fitted (as-is)")
ax.set_xscale("log")
ax.set_xlabel("Household income (USD, log scale)")
ax.set_ylabel("Life expectancy (years)")
ax.set_title("Synthetic demo: income vs. life expectancy")
ax.legend()
fig.tight_layout()
fig.savefig("figures/income_lifespan_fit.png", dpi=150)
print("Saved figures/income_lifespan_fit.png")
