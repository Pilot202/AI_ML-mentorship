"""
Week 1 - Thursday Session
Topic: Reading & Writing Files

Run this file with:  python 06_file_io.py

This script creates a small text file, reads it back, appends
to it, and reads it again -- so you can see the full read/write
cycle in one run.
"""

FILE_NAME = "scores.txt"

# ---------------------------------------------------------
# 1. Writing a file ("w" mode overwrites if it already exists)
# ---------------------------------------------------------
print("--- Writing a file ---")
with open(FILE_NAME, "w") as f:
    f.write("Ada: 84.3\n")
    f.write("Chidi: 54.3\n")
print(f"Wrote initial data to {FILE_NAME}")

# ---------------------------------------------------------
# 2. Reading a file line by line
# ---------------------------------------------------------
print("\n--- Reading the file ---")
with open(FILE_NAME) as f:
    for line in f:
        print(line.strip())  # .strip() removes the trailing newline

# ---------------------------------------------------------
# 3. Appending to a file ("a" mode adds without overwriting)
# ---------------------------------------------------------
print("\n--- Appending a new line ---")
with open(FILE_NAME, "a") as f:
    f.write("Ngozi: 95.0\n")
print("Appended a new record.")

# ---------------------------------------------------------
# 4. Reading the file again to confirm the append worked
# ---------------------------------------------------------
print("\n--- Reading again after append ---")
with open(FILE_NAME) as f:
    contents = f.read()
print(contents)

# ---------------------------------------------------------
# 5. Why use 'with'?
# ---------------------------------------------------------
# The 'with' statement is a context manager: it automatically
# closes the file when the block ends, even if an error happens
# partway through. Always prefer it over manual open()/close().
