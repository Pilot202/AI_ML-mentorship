"""
Week 2 - Monday Session
Topic: NumPy Array Basics

Run this file with:  python 01_numpy_arrays.py
"""

import numpy as np

# ---------------------------------------------------------
# 1. Creating arrays
# ---------------------------------------------------------
print("--- Creating arrays ---")
grades = np.array([85, 90, 78, 92])
print("From a list:", grades)

zeros = np.zeros((2, 3))
print("\nZeros (2x3):\n", zeros)

ones = np.ones((3,))
print("\nOnes (length 3):", ones)

steps = np.arange(0, 10, 2)
print("\narange(0, 10, 2):", steps)

evenly_spaced = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", evenly_spaced)

# ---------------------------------------------------------
# 2. Shape and dtype
# ---------------------------------------------------------
print("\n--- Shape & dtype ---")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)   # (2, 3) -> 2 rows, 3 columns
print("Dtype:", matrix.dtype)
print("Number of dimensions:", matrix.ndim)
print("Total elements:", matrix.size)

# ---------------------------------------------------------
# 3. Indexing & slicing
# ---------------------------------------------------------
print("\n--- Indexing & slicing ---")
print("First grade:", grades[0])
print("Last grade:", grades[-1])
print("First two grades:", grades[:2])

print("\nMatrix element at row 0, col 1:", matrix[0, 1])
print("Entire first row:", matrix[0, :])
print("Entire second column:", matrix[:, 1])

# ---------------------------------------------------------
# 4. Reshaping
# ---------------------------------------------------------
print("\n--- Reshaping ---")
flat = np.arange(6)
print("Flat array:", flat)
reshaped = flat.reshape(2, 3)
print("Reshaped to (2, 3):\n", reshaped)
