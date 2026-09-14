"""
Deep Dive - Part 1: Linear Algebra
Topic: Matrices — structure, types, and multiplication

Run this file with:  python 02_matrices.py
"""

import numpy as np

# ---------------------------------------------------------
# 1. Creating matrices
# ---------------------------------------------------------
print("--- Creating matrices ---")
A = np.array([[1, 2, 3], [4, 5, 6]])   # 2 rows, 3 columns
print("A =\n", A)
print("shape:", A.shape)   # (2, 3)

# In ML: a whole dataset is naturally a matrix
# rows = data points, columns = features
dataset = np.array([
    [6, 92, 78],   # student 1: study_hours, attendance, prior_score
    [3, 60, 55],   # student 2
    [8, 98, 90],   # student 3
])
print("\nA small dataset as a matrix:\n", dataset)
print("shape:", dataset.shape, "-- 3 students, 3 features each")

# ---------------------------------------------------------
# 2. Special matrix types
# ---------------------------------------------------------
print("\n--- Special matrix types ---")

identity = np.eye(3)
print("Identity matrix (3x3):\n", identity)

zeros = np.zeros((2, 3))
print("\nZero matrix (2x3):\n", zeros)

diagonal = np.diag([1, 2, 3])
print("\nDiagonal matrix:\n", diagonal)

# ---------------------------------------------------------
# 3. Transpose
# ---------------------------------------------------------
print("\n--- Transpose ---")
print("A =\n", A)
print("A.T (transpose) =\n", A.T)
print("Original shape:", A.shape, " Transposed shape:", A.T.shape)

# ---------------------------------------------------------
# 4. Matrix multiplication, worked by hand and verified
# ---------------------------------------------------------
print("\n--- Matrix multiplication ---")
M1 = np.array([[1, 2], [3, 4]])
M2 = np.array([[5, 6], [7, 8]])

# by hand:
# C[0,0] = 1*5 + 2*7 = 19
# C[0,1] = 1*6 + 2*8 = 22
# C[1,0] = 3*5 + 4*7 = 43
# C[1,1] = 3*6 + 4*8 = 50
C = M1 @ M2
print("M1 =\n", M1)
print("M2 =\n", M2)
print("M1 @ M2 =\n", C)

# confirm it's not commutative
C_reversed = M2 @ M1
print("\nM2 @ M1 =\n", C_reversed)
print("Are M1@M2 and M2@M1 equal?", np.array_equal(C, C_reversed))

# ---------------------------------------------------------
# 5. Identity matrix behaves like the number 1
# ---------------------------------------------------------
print("\n--- Identity matrix property ---")
I = np.eye(2)
print("M1 @ I =\n", M1 @ I)
print("Equal to M1?", np.array_equal(M1 @ I, M1))
