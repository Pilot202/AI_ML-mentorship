"""
Week 1 - Tuesday Session
Topic: Control Flow — if/elif/else, for, while, break/continue

Run this file with:  python 03_control_flow.py
"""

# ---------------------------------------------------------
# 1. if / elif / else
# ---------------------------------------------------------
print("--- if / elif / else ---")
grades = [85, 62, 41, 90]

for grade in grades:
    if grade >= 70:
        result = "Pass"
    elif grade >= 50:
        result = "Credit"
    else:
        result = "Retake"
    print(f"Grade {grade}: {result}")

# ---------------------------------------------------------
# 2. for loops over different sequences
# ---------------------------------------------------------
print("\n--- for loops ---")
for letter in "Python":
    print(letter, end=" ")
print()

for i in range(1, 6):          # 1, 2, 3, 4, 5
    print(f"Step {i}")

# ---------------------------------------------------------
# 3. while loops
# ---------------------------------------------------------
print("\n--- while loop ---")
count = 0
while count < 3:
    print(f"count = {count}")
    count += 1

# ---------------------------------------------------------
# 4. break and continue
# ---------------------------------------------------------
print("\n--- break ---")
for grade in grades:
    if grade < 50:
        print(f"Stopping early — found a failing grade: {grade}")
        break
    print(f"Checked grade: {grade}")

print("\n--- continue ---")
for grade in grades:
    if grade < 50:
        continue  # skip failing grades, keep going
    print(f"Processing passing grade: {grade}")

# ---------------------------------------------------------
# 5. Putting it together: average with a running total
# ---------------------------------------------------------
print("\n--- Combined example ---")
total = 0
passing_count = 0
for grade in grades:
    if grade >= 50:
        total += grade
        passing_count += 1

if passing_count > 0:
    print(f"Average of passing grades: {total / passing_count:.1f}")
else:
    print("No passing grades found.")
