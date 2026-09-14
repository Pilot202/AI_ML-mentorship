"""
Deep Dive - Part 1: Linear Algebra
Topic: PCA From Scratch, Built From Eigenvectors

This shows the direct line from "eigenvalues and eigenvectors" to a
real, widely-used ML technique: Principal Component Analysis (PCA).
We build it from scratch using only NumPy, then check our answer
against scikit-learn's PCA implementation.

Run this file with:  python 05_pca_with_eigenvectors.py
"""

import numpy as np
from sklearn.decomposition import PCA

# ---------------------------------------------------------
# 1. A small dataset with 2 correlated features
# ---------------------------------------------------------
print("--- Dataset ---")
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9],
], dtype=float)
print(X)

# ---------------------------------------------------------
# 2. PCA from scratch, step by step
# ---------------------------------------------------------
print("\n--- Step 1: Center the data ---")
mean = X.mean(axis=0)
X_centered = X - mean
print("Mean:", mean)

print("\n--- Step 2: Covariance matrix ---")
cov_matrix = np.cov(X_centered.T)
print(cov_matrix)

print("\n--- Step 3: Eigen-decomposition of the covariance matrix ---")
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors (columns):\n", eigenvectors)

print("\n--- Step 4: Sort by eigenvalue, largest first ---")
order = np.argsort(eigenvalues)[::-1]
eigenvalues_sorted = eigenvalues[order]
eigenvectors_sorted = eigenvectors[:, order]
print("Sorted eigenvalues:", eigenvalues_sorted)

print("\n--- Step 5: Project data onto the top principal component ---")
top_component = eigenvectors_sorted[:, 0]
X_projected = X_centered @ top_component
print("First principal component direction:", top_component)
print("Data projected onto it (first 5 points):", X_projected[:5])

variance_explained = eigenvalues_sorted[0] / eigenvalues_sorted.sum() * 100
print(f"\nThis first component explains {variance_explained:.1f}% of the total variance.")

# ---------------------------------------------------------
# 3. Compare against scikit-learn's PCA
# ---------------------------------------------------------
print("\n--- Checking against scikit-learn's PCA ---")
pca = PCA(n_components=2)
pca.fit(X)
print("scikit-learn's principal component directions:\n", pca.components_)
print("scikit-learn's explained variance ratio:", pca.explained_variance_ratio_)
print("\nOur from-scratch top direction:", top_component)
print("(directions may point opposite ways -- that's still the same line/component)")
