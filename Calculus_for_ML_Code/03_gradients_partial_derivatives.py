"""
Calculus for ML - Part 2: Gradients
Topic: Partial Derivatives & the Gradient Vector

Run this file with:  python 03_gradients_partial_derivatives.py
"""

import numpy as np
import sympy as sp

# ---------------------------------------------------------
# 1. Partial derivatives: differentiate w.r.t. one variable,
#    treating the others as constants
# ---------------------------------------------------------
print("--- Partial derivatives ---")
x, y = sp.symbols('x y')
f = x**2 + y**3

df_dx = sp.diff(f, x)   # treat y as a constant
df_dy = sp.diff(f, y)   # treat x as a constant
print(f"f(x, y) = {f}")
print(f"df/dx = {df_dx}   (y treated as constant)")
print(f"df/dy = {df_dy}   (x treated as constant)")

# ---------------------------------------------------------
# 2. The gradient vector: collect all partials into one vector
# ---------------------------------------------------------
print("\n--- The gradient vector ---")
point = {x: 1, y: 2}
gradient = [df_dx.subs(point), df_dy.subs(point)]
print(f"At the point (1, 2), the gradient is: {gradient}")
print("This vector points in the direction of steepest INCREASE of f.")

# ---------------------------------------------------------
# 3. A function with three variables, for practice
# ---------------------------------------------------------
print("\n--- A function with 3 variables ---")
x1, x2, x3 = sp.symbols('x1 x2 x3')
g = x1**2 + 2 * x2 * x3 + x3**2

gradient_g = [sp.diff(g, var) for var in (x1, x2, x3)]
print(f"g(x1, x2, x3) = {g}")
print(f"Gradient: {gradient_g}")

point_g = {x1: 1, x2: 2, x3: 3}
gradient_g_at_point = [expr.subs(point_g) for expr in gradient_g]
print(f"At (1, 2, 3): {gradient_g_at_point}")

# ---------------------------------------------------------
# 4. Using the gradient as a plain NumPy vector for a
#    gradient-descent-style update
# ---------------------------------------------------------
print("\n--- Using the gradient in an update step ---")
params = np.array([1.0, 2.0])           # current [x, y]
grad_vector = np.array([2.0, 12.0])     # gradient from the earlier example
learning_rate = 0.1

new_params = params - learning_rate * grad_vector
print(f"Old params: {params}")
print(f"Gradient:   {grad_vector}")
print(f"New params (moved opposite the gradient): {new_params}")
