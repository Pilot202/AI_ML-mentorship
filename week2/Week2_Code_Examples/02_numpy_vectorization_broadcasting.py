"""
Week 2 - Monday Session
Topic: Vectorization & Broadcasting

Run this file with:  python 02_numpy_vectorization_broadcasting.py
"""

import time
import numpy as np

# ---------------------------------------------------------
# 1. Vectorized operations
# ---------------------------------------------------------
print("--- Vectorized operations ---")
grades = np.array([85, 90, 78, 92])

curved = grades + 5          # add 5 to every element at once
print("Original:", grades)
print("Curved (+5):", curved)

doubled = grades * 2
print("Doubled:", doubled)

passed = grades >= 70        # vectorized comparison -> array of booleans
print("Passed (>=70)?:", passed)

# ---------------------------------------------------------
# 2. Why vectorization is faster than a Python loop
# ---------------------------------------------------------
print("\n--- Speed comparison ---")
big_array = np.arange(1_000_000)

start = time.time()
loop_result = [x * 2 for x in big_array]  # plain Python loop
loop_time = time.time() - start

start = time.time()
vectorized_result = big_array * 2         # NumPy vectorized operation
vector_time = time.time() - start

print(f"Python loop time:      {loop_time:.4f} seconds")
print(f"Vectorized (NumPy) time: {vector_time:.4f} seconds")
print(f"Vectorized was roughly {loop_time / vector_time:.1f}x faster")

# ---------------------------------------------------------
# 3. Broadcasting
# ---------------------------------------------------------
print("\n--- Broadcasting ---")
# a scalar "stretches" to match the array's shape
scaled = grades * 1.1
print("Scaled by 1.1:", scaled)

# two arrays of compatible shapes broadcast together
bonus_points = np.array([1, 2, 3, 4])
final_grades = grades + bonus_points
print("Grades + per-student bonus:", final_grades)

# broadcasting a (3,) array across a (2, 3) matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_adjustment = np.array([10, 20, 30])
print("\nMatrix:\n", matrix)
print("Row adjustment:", row_adjustment)
print("Matrix + row adjustment (broadcast):\n", matrix + row_adjustment)
