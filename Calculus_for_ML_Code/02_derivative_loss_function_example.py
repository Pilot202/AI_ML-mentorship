"""
Calculus for ML - Part 1: Derivatives
Topic: Worked Example — Derivative of a Loss Function

Run this file with:  python 02_derivative_loss_function_example.py
"""

import sympy as sp

# ---------------------------------------------------------
# Setup: a tiny model y_hat = w * x, compared against a true
# value y using squared error loss.
# ---------------------------------------------------------
print("--- Setting up the loss function ---")
w = sp.symbols('w')
x_val, y_val = 2, 10   # one training example: x=2, true y=10

y_hat = w * x_val
loss = (y_val - y_hat) ** 2
print(f"Model: y_hat = w * {x_val}")
print(f"Loss:  L(w) = (y - y_hat)^2 = {loss}")

# ---------------------------------------------------------
# The derivative tells us how loss changes as w changes
# ---------------------------------------------------------
print("\n--- Derivative of the loss w.r.t. w ---")
dL_dw = sp.diff(loss, w)
print(f"dL/dw = {sp.expand(dL_dw)}")

# ---------------------------------------------------------
# Evaluate at a few candidate values of w to see the pattern
# ---------------------------------------------------------
print("\n--- Evaluating the slope at different starting guesses ---")
for w_guess in [0, 1, 3, 5, 7]:
    slope = dL_dw.subs(w, w_guess)
    loss_value = loss.subs(w, w_guess)
    direction = "increase w" if slope < 0 else "decrease w" if slope > 0 else "at the minimum!"
    print(f"w={w_guess}: loss={float(loss_value):.1f}, slope={float(slope):.1f}  -> {direction}")

# ---------------------------------------------------------
# The true minimum, found two ways
# ---------------------------------------------------------
print("\n--- Finding the minimum ---")
critical_points = sp.solve(dL_dw, w)
print(f"Setting dL/dw = 0 and solving gives w = {critical_points}")
print("This is the exact value gradient descent will converge toward.")
