# Week 1 — Python Programming Fundamentals

Companion code for Week 1 of the 3-Month ML Mentorship Program.
Matches the slide deck: `Week1_Python_Fundamentals.pptx`.

## Files

| File | Session | Topic |
|---|---|---|
| `01_syntax_and_variables.py` | Monday | Variables, types, f-strings, operators |
| `02_data_structures.py` | Monday | Lists, tuples, dicts, sets |
| `03_control_flow.py` | Tuesday | if/elif/else, for, while, break/continue |
| `04_functions.py` | Tuesday | Functions, default args, *args, **kwargs |
| `05_oop_basics.py` | Tuesday | Classes, objects, attributes, methods |
| `06_file_io.py` | Thursday | Reading, writing, and appending to files |
| `07_mini_project_grade_tracker.py` | Thursday (practice) | Capstone project combining everything above |

## Running the examples

Each file is self-contained and runnable on its own:

```bash
python 01_syntax_and_variables.py
python 02_data_structures.py
python 03_control_flow.py
python 04_functions.py
python 05_oop_basics.py
python 06_file_io.py
python 07_mini_project_grade_tracker.py
```

`06_file_io.py` and `07_mini_project_grade_tracker.py` will create small
`.txt` files in the same folder (`scores.txt` and `grade_report.txt`) —
open them after running to see the saved output.

## Setting up a virtual environment (recommended)

None of these scripts need external packages, but it's good practice to
start every project — including this one — inside its own virtual
environment.

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Installing packages later (for future weeks):**
```bash
pip install <package-name>
pip freeze > requirements.txt   # save your installed packages
```

**Deactivating when you're done:**
```bash
deactivate
```

## Practice project brief

`07_mini_project_grade_tracker.py` is the Week 1 capstone: a small
Grade Tracker that stores students in a dictionary, uses a `Student`
class to hold each student's grades and compute their average and
status, and saves a summary report to a text file.

Try extending it yourself:
1. Let a user type in names and scores instead of using the sample data
2. Add a method that returns the *lowest*-performing student
3. Read the roster back in from a saved file on startup
4. Push the finished project to a GitHub repo — this becomes the first
   entry in your portfolio.
