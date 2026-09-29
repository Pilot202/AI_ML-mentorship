"""
Calculus for ML - Part 3: The Chain Rule
Topic: Differentiating Composite (Nested) Functions

Run this file with:  python 04_chain_rule.py
"""

import sympy as sp

# ---------------------------------------------------------
# 1. A simple composite function, differentiated by hand
#    and checked symbolically
# ---------------------------------------------------------
print("--- f(x) = (3x + 1)^2 ---")
x = sp.symbols('x')

# inner function: g(x) = 3x + 1
# outer function: f(u) = u^2
# chain rule: d/dx[f(g(x))] = f'(g(x)) * g'(x) = 2*(3x+1) * 3

f = (3 * x + 1) ** 2
f_prime_by_hand = 2 * (3 * x + 1) * 3
f_prime_sympy = sp.diff(f, x)

print(f"f(x) = {f}")
print(f"By hand (chain rule):    {sp.expand(f_prime_by_hand)}")
print(f"sympy's sp.diff():        {sp.expand(f_prime_sympy)}")
print(f"Do they match? {sp.expand(f_prime_by_hand) == sp.expand(f_prime_sympy)}")

# ---------------------------------------------------------
# 2. A more layered example: three functions nested together
# ---------------------------------------------------------
print("\n--- A triple-nested function ---")
# h(x) = sin(x^2 + 1) -- outer: sin(u), middle: u = v^2+1... let's use
# something built from operations you'd see in a neural net instead:
# f(x) = (2x + 1)^3, treated as outer cube of an inner linear function
f2 = (2 * x + 1) ** 3
f2_prime = sp.diff(f2, x)
print(f"f(x) = {f2}")
print(f"f'(x) = {f2_prime}")
print(f"Expanded: {sp.expand(f2_prime)}")

# ---------------------------------------------------------
# 3. Chain rule with two variables feeding into a chain --
#    closer to how a real network layer works
# ---------------------------------------------------------
print("\n--- Chain rule through two steps, manually ---")


def forward(x_val, w1, w2):
    """ x -> multiply by w1 -> square -> multiply by w2 -> output """
    a = x_val * w1        # step 1
    b = a ** 2             # step 2 (nonlinearity, like a simple activation)
    c = b * w2             # step 3
    return a, b, c


x_val, w1, w2 = 2.0, 3.0, 0.5
a, b, c = forward(x_val, w1, w2)
print(f"x={x_val}, w1={w1}, w2={w2}")
print(f"a = x*w1 = {a}")
print(f"b = a^2  = {b}")
print(f"c = b*w2 = {c}  (final output)")

# chain rule: dc/dw1 = dc/db * db/da * da/dw1
dc_db = w2            # c = b * w2  -->  dc/db = w2
db_da = 2 * a          # b = a^2     -->  db/da = 2a
da_dw1 = x_val          # a = x*w1    -->  da/dw1 = x

dc_dw1 = dc_db * db_da * da_dw1
print(f"\ndc/db = {dc_db}")
print(f"db/da = {db_da}")
print(f"da/dw1 = {da_dw1}")
print(f"dc/dw1 = dc/db * db/da * da/dw1 = {dc_dw1}")
print("This chained multiplication of local derivatives IS backpropagation.")
