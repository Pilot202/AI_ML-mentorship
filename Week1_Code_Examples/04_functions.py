"""
Week 1 - Tuesday Session
Topic: Functions

Run this file with:  python 04_functions.py
"""


# ---------------------------------------------------------
# 1. Basic function with a docstring and return value
# ---------------------------------------------------------
def calculate_average(scores):
    """Return the mean of a list of numeric scores."""
    total = sum(scores)
    return total / len(scores)


print("--- Basic function ---")
grades = [85, 90, 78]
print("Average:", calculate_average(grades))


# ---------------------------------------------------------
# 2. Default arguments
# ---------------------------------------------------------
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print("\n--- Default arguments ---")
print(greet("Ada"))
print(greet("Ada", greeting="Welcome"))


# ---------------------------------------------------------
# 3. *args — accept any number of positional arguments
# ---------------------------------------------------------
def total(*args):
    return sum(args)


print("\n--- *args ---")
print("Total:", total(10, 20, 30))
print("Total:", total(5, 5))


# ---------------------------------------------------------
# 4. **kwargs — accept any number of keyword arguments
# ---------------------------------------------------------
def build_profile(**kwargs):
    return kwargs


print("\n--- **kwargs ---")
profile = build_profile(name="Ada", age=14, subject="Basic Science")
print(profile)


# ---------------------------------------------------------
# 5. Functions calling other functions
# ---------------------------------------------------------
def letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


def report(scores):
    """Build a short report line for each score using letter_grade()."""
    lines = []
    for score in scores:
        lines.append(f"{score} -> {letter_grade(score)}")
    return lines


print("\n--- Functions calling functions ---")
for line in report(grades):
    print(line)
