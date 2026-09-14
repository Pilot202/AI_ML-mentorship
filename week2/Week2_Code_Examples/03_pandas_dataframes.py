"""
Week 2 - Tuesday Session
Topic: Pandas DataFrames

Run this file with:  python 03_pandas_dataframes.py

This script creates a small sample CSV so the read_csv() example
works without needing an external file.
"""

import pandas as pd

# ---------------------------------------------------------
# 0. Create a small sample dataset to work with
# ---------------------------------------------------------
sample_data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ada", "Chidi", "Ngozi", "Tunde", "Bisi"],
    "subject": ["Math", "Math", "Science", "Science", "Math"],
    "grade": [85, 60, 95, 45, 78],
}
df_sample = pd.DataFrame(sample_data)
df_sample.to_csv("students.csv", index=False)
print("Created students.csv for this example.\n")

# ---------------------------------------------------------
# 1. Series vs. DataFrame
# ---------------------------------------------------------
print("--- Series vs. DataFrame ---")
grade_series = pd.Series([85, 90, 78], name="grade")
print("A Series (one column):\n", grade_series)

# ---------------------------------------------------------
# 2. Loading data
# ---------------------------------------------------------
print("\n--- Loading data with read_csv ---")
df = pd.read_csv("students.csv")
print(df)

# ---------------------------------------------------------
# 3. First look at data
# ---------------------------------------------------------
print("\n--- .head() ---")
print(df.head(3))

print("\n--- .info() ---")
df.info()

print("\n--- .describe() ---")
print(df.describe())

# ---------------------------------------------------------
# 4. Selecting data: loc vs iloc
# ---------------------------------------------------------
print("\n--- Selecting data ---")
print("df.loc[0, 'name']  (label-based):", df.loc[0, "name"])
print("df.iloc[0, 1]       (position-based):", df.iloc[0, 1])

print("\nSelecting a column (returns a Series):")
print(df["name"])

print("\nSelecting multiple columns:")
print(df[["name", "grade"]])

print("\nFiltering rows where grade >= 70:")
print(df[df["grade"] >= 70])
