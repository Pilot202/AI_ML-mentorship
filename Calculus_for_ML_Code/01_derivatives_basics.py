"""
Calculus for ML - Part 1: Derivatives
Topic: What derivatives are, the core rules, and computing them two ways

Run this file with:  python 01_derivatives_basics.py
"""

import sympy as sp

# ---------------------------------------------------------
# 1. A derivative via symbolic differentiation (sympy)
# ---------------------------------------------------------
print("--- Symbolic differentiation ---")
x = sp.symbols('x')
f = x**2 + 3 * x

f_prime = sp.diff(f, x)
print(f"f(x)  = {f}")
print(f"f'(x) = {f_prime}")
print(f"f'(1) = {f_prime.subs(x, 1)}   -- the slope of f at x=1")

# ---------------------------------------------------------
# 2. The core rules, verified one at a time
# ---------------------------------------------------------
print("\n--- Core rules, verified ---")

# power rule: d/dx[x^n] = n*x^(n-1)
print("Power rule:      d/dx[x^3] =", sp.diff(x**3, x))

# constant multiple rule: d/dx[c*f(x)] = c*f'(x)
print("Constant mult.:  d/dx[5x^2] =", sp.diff(5 * x**2, x))

# sum rule: d/dx[f(x)+g(x)] = f'(x)+g'(x)
print("Sum rule:        d/dx[x^2+3x] =", sp.diff(x**2 + 3 * x, x))

# constant rule: d/dx[c] = 0
print("Constant rule:   d/dx[7] =", sp.diff(sp.Integer(7), x))

# ---------------------------------------------------------
# 3. A derivative via the definition (numerical / finite difference)
#    This is what a derivative *actually means*: the limit of the
#    slope between two very close points.
# ---------------------------------------------------------
print("\n--- Numerical derivative (finite difference) ---")


def f_numeric(x_val):
    return x_val**2 + 3 * x_val


def numerical_derivative(func, x_val, h=1e-6):
    return (func(x_val + h) - func(x_val - h)) / (2 * h)


approx = numerical_derivative(f_numeric, 1.0)
exact = float(f_prime.subs(x, 1))
print(f"Numerical approximation at x=1: {approx:.6f}")
print(f"Exact symbolic answer at x=1:   {exact:.6f}")
print("These should match closely -- the numerical version is how a")
print("computer could estimate a derivative even without doing algebra.")
