"""
Deep Dive - Part 1: Linear Algebra
Topic: The Dot Product, In Depth

Run this file with:  python 03_dot_product_deep_dive.py
"""

import numpy as np

# ---------------------------------------------------------
# 1. Algebraic definition: sum of products
# ---------------------------------------------------------
print("--- Algebraic definition ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_manual = sum(x * y for x, y in zip(a, b))
dot_np = np.dot(a, b)
dot_operator = a @ b   # the @ operator also computes the dot product for 1D arrays

print(f"a = {a}, b = {b}")
print(f"Manual (sum of products): {dot_manual}")
print(f"np.dot(a, b):             {dot_np}")
print(f"a @ b:                    {dot_operator}")

# ---------------------------------------------------------
# 2. Geometric definition: relates to the angle between vectors
# ---------------------------------------------------------
print("\n--- Geometric definition ---")
cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)
print(f"cos(theta) = {cos_theta:.4f}")
print(f"theta = {angle_deg:.1f} degrees")

# ---------------------------------------------------------
# 3. Orthogonal vectors (dot product = 0)
# ---------------------------------------------------------
print("\n--- Orthogonal vectors ---")
x_axis = np.array([1, 0])
y_axis = np.array([0, 1])
print(f"{x_axis} . {y_axis} = {np.dot(x_axis, y_axis)}  (perpendicular -> 0)")

# ---------------------------------------------------------
# 4. Same direction vs. opposite direction
# ---------------------------------------------------------
print("\n--- Direction sign ---")
same_direction = np.array([2, 2])
opposite_direction = np.array([-2, -2])
reference = np.array([1, 1])
print(f"Same direction dot product: {np.dot(reference, same_direction)}  (positive)")
print(f"Opposite direction dot product: {np.dot(reference, opposite_direction)}  (negative)")

# ---------------------------------------------------------
# 5. ML connection: a neuron's weighted sum
# ---------------------------------------------------------
print("\n--- ML connection: a single neuron ---")
inputs = np.array([0.5, 0.8, 0.2])
weights = np.array([0.4, -0.6, 0.9])
bias = 0.1

weighted_sum = np.dot(inputs, weights) + bias
print(f"inputs:  {inputs}")
print(f"weights: {weights}")
print(f"weighted sum (dot product) + bias = {weighted_sum:.4f}")
print("This single number is what an activation function like sigmoid or ReLU acts on.")

# ---------------------------------------------------------
# 6. ML connection: cosine similarity (used with embeddings)
# ---------------------------------------------------------
print("\n--- ML connection: cosine similarity ---")


def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


doc1 = np.array([1, 1, 0, 0])   # e.g. word-count vector for "cat dog"
doc2 = np.array([1, 0, 0, 1])   # e.g. word-count vector for "cat bird"
doc3 = np.array([0, 0, 1, 1])   # e.g. word-count vector for "fish bird"

print(f"Similarity(doc1, doc2): {cosine_similarity(doc1, doc2):.3f}")
print(f"Similarity(doc1, doc3): {cosine_similarity(doc1, doc3):.3f}")
print("Higher cosine similarity means the vectors point in a more similar direction.")
