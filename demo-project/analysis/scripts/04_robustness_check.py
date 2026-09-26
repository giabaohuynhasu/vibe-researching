"""
04_robustness_check.py
Per the researcher's decision (see decision card), runs all three scenarios
raised at the Step 6 stop rather than picking one in advance, and compares
the coefficient on log_income across them.
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv("data/processed/clean_income_lifespan.csv")
df["log_income"] = np.log(df["household_income_usd"])
X = sm.add_constant(df["log_income"])
y = df["life_expectancy_years"]

# Scenario 1: original OLS, nonrobust SE, all data
m1 = sm.OLS(y, X).fit()

# Scenario 2: same data, HC3 robust SE
m2 = sm.OLS(y, X).fit(cov_type="HC3")

# Scenario 3: exclude the 12 flagged high-leverage points, refit
influence = m1.get_influence()
leverage = influence.hat_matrix_diag
threshold = 3 * X.shape[1] / len(df)
keep = leverage <= threshold
X3, y3 = X[keep], y[keep]
m3 = sm.OLS(y3, X3).fit()

print(f"{'Scenario':<32} {'coef':>8} {'se':>8} {'p':>10} {'n':>6}")
print(f"{'1. As-is (nonrobust SE)':<32} {m1.params['log_income']:>8.4f} {m1.bse['log_income']:>8.4f} {m1.pvalues['log_income']:>10.2e} {int(m1.nobs):>6}")
print(f"{'2. HC3 robust SE':<32} {m2.params['log_income']:>8.4f} {m2.bse['log_income']:>8.4f} {m2.pvalues['log_income']:>10.2e} {int(m2.nobs):>6}")
print(f"{'3. High-leverage excluded':<32} {m3.params['log_income']:>8.4f} {m3.bse['log_income']:>8.4f} {m3.pvalues['log_income']:>10.2e} {int(m3.nobs):>6}")

coefs = [m1.params["log_income"], m2.params["log_income"], m3.params["log_income"]]
spread = (max(coefs) - min(coefs)) / np.mean(coefs) * 100
print(f"\nCoefficient spread across scenarios: {spread:.1f}% of the mean estimate")
