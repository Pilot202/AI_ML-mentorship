"""
Deep Dive - Part 1: Linear Algebra
Topic: Eigenvalues & Eigenvectors

Run this file with:  python 04_eigenvalues_eigenvectors.py
"""

import numpy as np
import sympy as sp

# ---------------------------------------------------------
# 1. The defining equation: A v = lambda v
# ---------------------------------------------------------
print("--- The eigenvalue equation: A v = lambda v ---")
A = np.array([[2, 1], [1, 2]])
print("A =\n", A)

# ---------------------------------------------------------
# 2. Solving by hand, symbolically, with sympy
#    (this mirrors the by-hand steps on the slide, but lets
#    the computer do the algebra so you can check your work)
# ---------------------------------------------------------
print("\n--- Solving the characteristic equation symbolically ---")
lam = sp.symbols("lambda")
A_sym = sp.Matrix(A.tolist())
I_sym = sp.eye(2)

characteristic_poly = (A_sym - lam * I_sym).det()
print("det(A - lambda*I) =", sp.expand(characteristic_poly))

solutions = sp.solve(characteristic_poly, lam)
print("Solutions (eigenvalues):", solutions)

# ---------------------------------------------------------
# 3. Solving numerically with NumPy
# ---------------------------------------------------------
print("\n--- Solving numerically with NumPy ---")
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors (as columns):\n", eigenvectors)

# ---------------------------------------------------------
# 4. Verifying: A @ v should equal lambda * v for each pair
# ---------------------------------------------------------
print("\n--- Verifying A @ v = lambda * v ---")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam_i = eigenvalues[i]
    left_side = A @ v
    right_side = lam_i * v
    matches = np.allclose(left_side, right_side)
    print(f"Eigenvalue {lam_i:.2f}: A @ v = {left_side}, lambda * v = {right_side}, match = {matches}")

# ---------------------------------------------------------
# 5. A matrix that rotates most vectors -- eigenvectors
#    are the special directions that DON'T get rotated
# ---------------------------------------------------------
print("\n--- Most vectors change direction under A, eigenvectors don't ---")
test_vector = np.array([1, 0])
transformed = A @ test_vector
print(f"Original vector:    {test_vector}")
print(f"After A @ v:         {transformed}")
print("Notice the direction changed -- this is a non-eigenvector.")

eigen_v = eigenvectors[:, 0]
transformed_eigen = A @ eigen_v
print(f"\nEigenvector:         {eigen_v}")
print(f"After A @ v:         {transformed_eigen}")
print("This one only got longer/shorter -- same direction (or exactly opposite).")
