"""
Week 1 - Monday Session
Topic: Core Data Structures — List, Tuple, Dict, Set

Run this file with:  python 02_data_structures.py
"""

# ---------------------------------------------------------
# 1. List — ordered, mutable, allows duplicates
# ---------------------------------------------------------
print("--- List ---")
grades = [85, 90, 78]
grades.append(92)                 # add to the end
grades[0] = 88                    # update by index
print("Grades:", grades)
print("First grade:", grades[0])
print("Last grade:", grades[-1])
print("Slice (first two):", grades[:2])

# ---------------------------------------------------------
# 2. Tuple — ordered, immutable
# ---------------------------------------------------------
print("\n--- Tuple ---")
point = (4, 7)
print("Point:", point)
print("x =", point[0], "y =", point[1])
# point[0] = 10  # <- this would raise a TypeError; tuples can't be changed

# ---------------------------------------------------------
# 3. Dict — key-value pairs, fast lookups
# ---------------------------------------------------------
print("\n--- Dict ---")
student = {"name": "Ada", "age": 14, "grades": [85, 90, 78]}
student["gpa"] = 3.8              # add a new key
print("Student record:", student)
print("Name:", student["name"])
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

# ---------------------------------------------------------
# 4. Set — unordered, only unique values
# ---------------------------------------------------------
print("\n--- Set ---")
unique_ids = {1, 2, 3, 2, 1}      # duplicates are dropped automatically
print("Unique IDs:", unique_ids)
unique_ids.add(4)
print("After adding 4:", unique_ids)
print("Is 2 in the set?", 2 in unique_ids)

# ---------------------------------------------------------
# 5. Choosing the right structure
# ---------------------------------------------------------
print("\n--- Quick Reference ---")
print("Use a LIST when order matters and values may change.")
print("Use a TUPLE when the data should never change (fixed coordinates, RGB values).")
print("Use a DICT when you need to look values up by a name/key.")
print("Use a SET when you only care about uniqueness, not order.")
