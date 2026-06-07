# Student Data Management System

A Python application for storing, filtering, and processing student records using core Python data structures — lists, tuples, sets, and dictionaries — along with comprehensions and generator expressions.

---

## Features

| Feature | File | Technique |
|---|---|---|
| Student dataset | `student_data.py` | List of tuples |
| Filter by major | `filter.py` | List comprehension |
| Group students by major | `filter.py` | Dictionary comprehension |
| Format & display records | `data_processing.py` | f-strings, iteration |
| Find unique majors | `set_operations.py` | Set comprehension |
| Count students per major | `set_operations.py` | Dict + set comprehension |
| Lazy streaming by major | `data_generator.py` | Generator expression |

---

## Project Structure

```
.
├── student_data.py      # Core dataset — list of (ID, Name, Major) tuples
├── filter.py            # List & dictionary comprehensions for filtering/grouping
├── data_processing.py   # Format and display student records
├── set_operations.py    # Set comprehensions for unique majors and summaries
├── data_generator.py    # Generator expressions for memory-efficient streaming
└── README.md
```

---

## Setup

No external dependencies required — this project uses the Python standard library only.

**Requirements:** Python 3.7+

```bash
# Clone the repository
git clone <your-repo-url>
cd <repo-folder>
```

---

## Usage

Each module can be run independently for a quick demo:

```bash
# See filtering and grouping in action
python filter.py

# See formatted student output
python data_processing.py

# See unique majors and per-major counts
python set_operations.py

# See generator lazy evaluation
python data_generator.py
```

Or import functions into your own scripts:

```python
from student_data import students
from filter import filter_students_by_major, students_by_major_dict
from data_processing import format_student_data, display_students
from set_operations import unique_majors, major_summary
from data_generator import student_generator

# Filter to one major
cs_students = filter_students_by_major(students, "Computer Science")

# Group all students by major (dictionary comprehension)
grouped = students_by_major_dict(students)

# Display all students
display_students(students)

# Get unique majors (set comprehension)
majors = unique_majors(students)

# Stream students lazily (generator expression)
gen = student_generator(students, "Mathematics")
print(next(gen))  # (102, 'Bob Smith', 'Mathematics')
```

---

## Data Structures Used

- **List** — ordered, mutable collection of student tuples (`student_data.py`)
- **Tuple** — immutable record per student `(ID, Name, Major)`
- **Set** — unordered, deduplicated collection of majors (`set_operations.py`)
- **Dictionary** — major → students mapping (`filter.py`, `set_operations.py`)

## Comprehensions & Generators

- **List comprehension** — filters students by major in a single readable line
- **Dictionary comprehension** — groups students by major into a dict
- **Set comprehension** — extracts unique majors without manual deduplication
- **Generator expression** — streams students lazily, one at a time, saving memory

---

## Git Workflow

```bash
# Create and switch to a feature branch
git checkout -b feature/student-data-structures

# Stage and commit your work
git add .
git commit -m "Implement student filtering and set operations"

# Push branch and open a Pull Request on GitHub
git push origin feature/student-data-structures

# After PR is reviewed and merged, clean up locally
git checkout main
git pull origin main
git branch -d feature/student-data-structures
```