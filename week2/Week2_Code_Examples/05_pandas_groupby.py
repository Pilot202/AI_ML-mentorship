"""
Week 2 - Tuesday Session
Topic: GroupBy — Split, Apply, Combine

Run this file with:  python 05_pandas_groupby.py
"""

import pandas as pd

df = pd.DataFrame({
    "name": ["Ada", "Chidi", "Ngozi", "Tunde", "Bisi", "Femi"],
    "subject": ["Math", "Math", "Science", "Science", "Math", "Science"],
    "grade": [85, 60, 95, 45, 78, 88],
})
print("--- Full dataset ---")
print(df)

# ---------------------------------------------------------
# 1. Basic groupby: one column, one aggregation
# ---------------------------------------------------------
print("\n--- Average grade per subject ---")
print(df.groupby("subject")["grade"].mean())

# ---------------------------------------------------------
# 2. Multiple aggregations at once
# ---------------------------------------------------------
print("\n--- Multiple stats per subject ---")
print(df.groupby("subject")["grade"].agg(["mean", "min", "max", "count"]))

# ---------------------------------------------------------
# 3. Grouping and counting
# ---------------------------------------------------------
print("\n--- Students per subject ---")
print(df.groupby("subject").size())

# ---------------------------------------------------------
# 4. Applying a custom function per group
# ---------------------------------------------------------
print("\n--- Custom function: pass rate per subject ---")


def pass_rate(grades):
    return (grades >= 70).mean() * 100


print(df.groupby("subject")["grade"].apply(pass_rate))

# ---------------------------------------------------------
# 5. Sorting group results
# ---------------------------------------------------------
print("\n--- Subjects sorted by average grade, highest first ---")
averages = df.groupby("subject")["grade"].mean().sort_values(ascending=False)
print(averages)
