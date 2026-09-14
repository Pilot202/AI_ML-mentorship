"""
Week 1 - Tuesday Session
Topic: Object-Oriented Programming Basics

Run this file with:  python 05_oop_basics.py
"""


# ---------------------------------------------------------
# 1. A basic class: blueprint for Student objects
# ---------------------------------------------------------
class Student:
    """Represents a single student and their grades."""

    def __init__(self, name, grades):
        # self.name and self.grades are ATTRIBUTES —
        # data stored on each individual object
        self.name = name
        self.grades = grades

    def average(self):
        # a METHOD — a function that belongs to the class
        # and can use the object's own data via `self`
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.average()
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def __str__(self):
        # controls what print(student) displays
        return f"{self.name}: avg={self.average():.1f}, grade={self.letter_grade()}"


# ---------------------------------------------------------
# 2. Creating objects (instances) from the class
# ---------------------------------------------------------
print("--- Creating Student objects ---")
ada = Student("Ada", [85, 90, 78])
chidi = Student("Chidi", [60, 55, 48])

print(ada)
print(chidi)

# ---------------------------------------------------------
# 3. Objects are independent — each has its own attributes
# ---------------------------------------------------------
print("\n--- Independent state ---")
print(f"{ada.name}'s grades: {ada.grades}")
print(f"{chidi.name}'s grades: {chidi.grades}")

# ---------------------------------------------------------
# 4. A small class roster combining OOP + a list
# ---------------------------------------------------------
print("\n--- Class roster ---")
roster = [ada, chidi, Student("Ngozi", [95, 92, 98])]

for student in roster:
    print(student)

top_student = max(roster, key=lambda s: s.average())
print(f"\nTop student: {top_student.name} with an average of {top_student.average():.1f}")
