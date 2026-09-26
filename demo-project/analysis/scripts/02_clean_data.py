"""
02_clean_data.py
Reads from data/raw/ (never written to directly) and writes a processed
version to data/processed/. For this synthetic demo there is little real
cleaning to do, but the step stays in the pipeline so the raw-to-processed
boundary is never skipped, even when it looks unnecessary.
"""
import pandas as pd

df = pd.read_csv("data/raw/synthetic_income_lifespan.csv")
before = len(df)
df = df.dropna()
df = df[df["household_income_usd"] > 0]
after = len(df)

df.to_csv("data/processed/clean_income_lifespan.csv", index=False)
print(f"Rows: {before} -> {after} after dropping missing/non-positive income")
