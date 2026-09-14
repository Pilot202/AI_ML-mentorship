"""
Week 2 - Tuesday Session
Topic: Cleaning & Merging Data

Run this file with:  python 04_pandas_cleaning_merging.py
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. Cleaning: handling missing values
# ---------------------------------------------------------
print("--- Cleaning: missing values ---")
messy = pd.DataFrame({
    "name": ["Ada", "Chidi", "Ngozi", "Tunde"],
    "grade": [85, np.nan, 95, np.nan],
    "age": [14, 15, np.nan, 14],
})
print("Original (messy) data:\n", messy)

print("\nCount of missing values per column:")
print(messy.isnull().sum())

print("\nDrop rows with any missing value:")
print(messy.dropna())

print("\nFill missing grades with 0:")
filled = messy.copy()
filled["grade"] = filled["grade"].fillna(0)
print(filled)

print("\nFill missing ages with the column average instead:")
filled["age"] = filled["age"].fillna(filled["age"].mean())
print(filled)

# ---------------------------------------------------------
# 2. Cleaning: duplicates and types
# ---------------------------------------------------------
print("\n--- Cleaning: duplicates & types ---")
with_dupes = pd.DataFrame({
    "name": ["Ada", "Ada", "Chidi"],
    "grade": [85, 85, 60],
})
print("Data with a duplicate row:\n", with_dupes)
print("\nDuplicate count:", with_dupes.duplicated().sum())
print("\nAfter drop_duplicates():\n", with_dupes.drop_duplicates())

# ---------------------------------------------------------
# 3. Merging: concat (stacking rows)
# ---------------------------------------------------------
print("\n--- Merging: concat ---")
term1 = pd.DataFrame({"name": ["Ada", "Chidi"], "grade": [85, 60]})
term2 = pd.DataFrame({"name": ["Ngozi", "Tunde"], "grade": [95, 45]})
combined = pd.concat([term1, term2], ignore_index=True)
print("Term 1:\n", term1)
print("\nTerm 2:\n", term2)
print("\nStacked with concat:\n", combined)

# ---------------------------------------------------------
# 4. Merging: merge (joining on a shared column)
# ---------------------------------------------------------
print("\n--- Merging: merge (like a database JOIN) ---")
students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ada", "Chidi", "Ngozi"],
})
grades = pd.DataFrame({
    "id": [1, 2, 3],
    "grade": [85, 60, 95],
})
merged = pd.merge(students, grades, on="id")
print("Students:\n", students)
print("\nGrades:\n", grades)
print("\nMerged on 'id':\n", merged)
