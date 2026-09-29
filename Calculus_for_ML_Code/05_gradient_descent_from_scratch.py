"""
Calculus for ML - Part 4: Optimization
Topic: Gradient Descent From Scratch (1D and 2D)

Run this file with:  python 05_gradient_descent_from_scratch.py
"""

import numpy as np

# ---------------------------------------------------------
# 1. 1D gradient descent: minimize f(x) = (x - 3)^2
# ---------------------------------------------------------
print("--- 1D gradient descent ---")


def f(x_val):
    return (x_val - 3) ** 2


def f_prime(x_val):
    return 2 * (x_val - 3)


x = 0.0
learning_rate = 0.1

for step in range(20):
    grad = f_prime(x)
    x = x - learning_rate * grad
    if step % 4 == 0 or step == 19:
        print(f"step {step:>2}: x = {x:.4f}, f(x) = {f(x):.4f}")

print(f"\nFinal x: {x:.4f}  (true minimum is at x=3.0)")

# ---------------------------------------------------------
# 2. 2D gradient descent: minimize f(x, y) = x^2 + y^2
#    (a bowl-shaped surface, minimum at the origin)
# ---------------------------------------------------------
print("\n--- 2D gradient descent ---")


def f2(params):
    x_val, y_val = params
    return x_val**2 + y_val**2


def gradient2(params):
    x_val, y_val = params
    return np.array([2 * x_val, 2 * y_val])   # [df/dx, df/dy]


params = np.array([5.0, -3.0])   # random-ish starting point
learning_rate_2d = 0.1

for step in range(30):
    grad = gradient2(params)
    params = params - learning_rate_2d * grad
    if step % 6 == 0 or step == 29:
        print(f"step {step:>2}: params = [{params[0]:.4f}, {params[1]:.4f}], "
              f"f = {f2(params):.4f}")

print(f"\nFinal params: {params}  (true minimum is at [0, 0])")

# ---------------------------------------------------------
# 3. What happens with a learning rate that's too large?
# ---------------------------------------------------------
print("\n--- A learning rate that's too big (diverges instead of converging) ---")
x_bad = 0.0
bad_learning_rate = 1.1   # too large for this function's curvature

for step in range(6):
    grad = f_prime(x_bad)
    x_bad = x_bad - bad_learning_rate * grad
    print(f"step {step}: x = {x_bad:.2f}, f(x) = {f(x_bad):.2f}")

print("\nNotice x oscillates and grows instead of settling near 3 --")
print("this is exactly why learning rate is such a critical hyperparameter.")
