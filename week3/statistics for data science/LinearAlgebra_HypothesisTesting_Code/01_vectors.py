"""
Deep Dive - Part 1: Linear Algebra
Topic: Vectors — creation, operations, magnitude, unit vectors

Run this file with:  python 01_vectors.py
"""

import numpy as np

# ---------------------------------------------------------
# 1. Creating a vector
# ---------------------------------------------------------
print("--- Creating vectors ---")
v = np.array([3, 2])
print("v =", v)
print("shape:", v.shape)   # (2,) -- a 1-dimensional array

# A vector in ML is often a single data point's features
student = np.array([6, 92, 78])   # [study_hours, attendance_pct, prior_score]
print("student feature vector:", student)

# ---------------------------------------------------------
# 2. Addition
# ---------------------------------------------------------
print("\n--- Addition ---")
a = np.array([1, 2])
b = np.array([3, 1])
print(f"{a} + {b} = {a + b}")

# ---------------------------------------------------------
# 3. Scalar multiplication
# ---------------------------------------------------------
print("\n--- Scalar multiplication ---")
print(f"2 * {a} = {2 * a}")
print(f"0.5 * {a} = {0.5 * a}")

# ---------------------------------------------------------
# 4. Magnitude (norm) -- the vector's length
# ---------------------------------------------------------
print("\n--- Magnitude (norm) ---")
mag = np.linalg.norm(a)
print(f"||{a}|| = {mag:.4f}")

# verify by hand: sqrt(1^2 + 2^2) = sqrt(5)
manual_mag = (a[0]**2 + a[1]**2) ** 0.5
print(f"Manual calculation: sqrt(1^2 + 2^2) = {manual_mag:.4f}")

# ---------------------------------------------------------
# 5. Unit vectors -- same direction, length 1
# ---------------------------------------------------------
print("\n--- Unit vectors ---")
unit_a = a / np.linalg.norm(a)
print(f"Unit vector of {a}: {unit_a}")
print(f"Its magnitude: {np.linalg.norm(unit_a):.4f}   (should be 1.0)")

# ---------------------------------------------------------
# 6. Vectors of any length (not just 2D)
# ---------------------------------------------------------
print("\n--- Higher-dimensional vectors ---")
features_5d = np.array([1.2, 3.4, 0.5, 7.1, 2.2])
print("A 5-dimensional feature vector:", features_5d)
print("Its magnitude:", np.linalg.norm(features_5d))
