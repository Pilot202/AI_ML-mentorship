"""
Week 1 - Monday Session
Topic: Python Syntax & Variables

Run this file with:  python 01_syntax_and_variables.py
"""

# ---------------------------------------------------------
# 1. Variables & dynamic typing
# ---------------------------------------------------------
# Python infers the type from the value you assign — no need
# to declare it up front.
name = "Ada"            # str
age = 14                 # int
gpa = 3.8                 # float
is_enrolled = True        # bool

print("--- Variables & Types ---")
print(name, type(name))
print(age, type(age))
print(gpa, type(gpa))
print(is_enrolled, type(is_enrolled))

# ---------------------------------------------------------
# 2. f-strings for formatting output
# ---------------------------------------------------------
print("\n--- f-string Formatting ---")
print(f"{name} is {age} years old and has a GPA of {gpa}.")

# ---------------------------------------------------------
# 3. Multiple assignment
# ---------------------------------------------------------
print("\n--- Multiple Assignment ---")
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# ---------------------------------------------------------
# 4. Basic operators
# ---------------------------------------------------------
print("\n--- Basic Operators ---")
a, b = 7, 2
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")   # true division -> float
print(f"{a} // {b} = {a // b}")  # floor division -> int
print(f"{a} % {b} = {a % b}")    # remainder
print(f"{a} ** {b} = {a ** b}")  # exponent

# ---------------------------------------------------------
# 5. Comments
# ---------------------------------------------------------
# Use comments to explain WHY code does something, not just
# what it does — the "what" should be clear from good naming.

# ---------------------------------------------------------
# 6. Type conversion
# ---------------------------------------------------------
print("\n--- Type Conversion ---")
score_text = "85"
score_number = int(score_text)   # str -> int
print(f"'{score_text}' converted to int: {score_number}, doubled: {score_number * 2}")
