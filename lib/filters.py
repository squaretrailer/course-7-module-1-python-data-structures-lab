# lib/filter.py  (the test file imports from lib.filters — rename if needed)
# Provides filtering utilities for the student dataset.
# Uses list and dictionary comprehensions for concise, readable logic.


def filter_students_by_major(students, major):
    """
    Return a filtered list of students who match the given major.

    Uses a list comprehension to iterate over all students and select
    only those whose major (index 2) matches the given value.

    Args:
        students (list): A list of tuples in the format (ID, Name, Major).
        major (str): The major to filter by (case-sensitive).

    Returns:
        list: A list of student tuples whose major matches the given major.

    Example:
        >>> students = [(101, "Alice", "CS"), (102, "Bob", "Math")]
        >>> filter_students_by_major(students, "CS")
        [(101, 'Alice', 'CS')]
    """
    return [student for student in students if student[2] == major]


def students_by_major_dict(students):
    """
    Return a dictionary mapping each major to a list of student names.

    Uses a dictionary comprehension combined with a list comprehension
    to group student names under their respective majors.

    Args:
        students (list): A list of tuples in the format (ID, Name, Major).

    Returns:
        dict: Keys are majors (str), values are lists of student names (str).

    Example:
        >>> students = [(101, "Alice", "CS"), (102, "Bob", "Math"), (103, "Eve", "CS")]
        >>> students_by_major_dict(students)
        {'CS': ['Alice', 'Eve'], 'Math': ['Bob']}
    """
    majors = {student[2] for student in students}   # unique majors via set comprehension
    return {
        major: [s[1] for s in students if s[2] == major]
        for major in majors
    }