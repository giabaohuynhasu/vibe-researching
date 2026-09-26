"""
01_generate_data.py

Generates a SYNTHETIC dataset for this demo walkthrough only. This is not real
income/lifespan data and must not be cited as such -- it exists to give the
demo something concrete to run the skill's steps against. In a real project
this script would instead be a documented download/extraction from an actual
source, and its output would still land in data/raw/ untouched thereafter.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)
n = 400

income = rng.lognormal(mean=10.5, sigma=0.6, size=n)  # skewed, like real income
noise = rng.normal(0, 4, size=n)
life_expectancy = 45 + 3.0 * np.log(income) + noise
life_expectancy = np.clip(life_expectancy, 40, 95)

df = pd.DataFrame({"household_income_usd": income.round(2),
                    "life_expectancy_years": life_expectancy.round(1)})
df.to_csv("data/raw/synthetic_income_lifespan.csv", index=False)
print(f"Wrote {len(df)} synthetic rows to data/raw/synthetic_income_lifespan.csv")
print(df.describe())
