"""
Week 1 - Thursday Session
Practice Project: Grade Tracker CLI

This mini project ties together everything from Week 1:
  - data structures  (dict of students -> Student objects)
  - control flow      (if/elif/else, for loops)
  - functions         (helper functions + methods)
  - basic OOP         (a Student class)
  - file I/O          (saving a summary report to disk)

Run this file with:  python 07_mini_project_grade_tracker.py
"""


class Student:
    """Represents one student and their grades."""

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        """Add a single grade to this student's record."""
        self.grades.append(score)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def status(self):
        """Classify the student's average into pass/credit/retake."""
        avg = self.average()
        if avg >= 70:
            return "Pass"
        elif avg >= 50:
            return "Credit"
        else:
            return "Retake"

    def __str__(self):
        return f"{self.name}: average={self.average():.1f}, status={self.status()}"


class GradeTracker:
    """Manages a roster of Student objects, keyed by name."""

    def __init__(self):
        self.students = {}  # dict: name -> Student object

    def add_grade(self, name, score):
        """Add a grade for a student, creating the student if new."""
        if name not in self.students:
            self.students[name] = Student(name)
        self.students[name].add_grade(score)

    def average(self, name):
        return self.students[name].average()

    def top_student(self):
        """Return the Student object with the highest average."""
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.average())

    def summary_lines(self):
        """Build a list of report lines, one per student."""
        lines = []
        for student in self.students.values():
            lines.append(str(student))
        return lines

    def save_report(self, filename="grade_report.txt"):
        """Write the full summary, plus the top student, to a file."""
        lines = self.summary_lines()
        top = self.top_student()

        with open(filename, "w") as f:
            f.write("Grade Tracker Report\n")
            f.write("=====================\n\n")
            for line in lines:
                f.write(line + "\n")
            if top:
                f.write(f"\nTop student: {top.name} ({top.average():.1f})\n")

        return filename


def main():
    tracker = GradeTracker()

    # Sample roster — swap this for real data any time
    sample_data = {
        "Ada": [85, 90, 78],
        "Chidi": [60, 55, 48],
        "Ngozi": [95, 92, 98],
        "Tunde": [45, 50, 40],
    }

    for name, scores in sample_data.items():
        for score in scores:
            tracker.add_grade(name, score)

    print("--- Class Summary ---")
    for line in tracker.summary_lines():
        print(line)

    top = tracker.top_student()
    print(f"\nTop student: {top.name} with an average of {top.average():.1f}")

    filename = tracker.save_report()
    print(f"\nSaved full report to '{filename}'")


if __name__ == "__main__":
    main()
