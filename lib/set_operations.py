def unique_majors(students):
    """
    Return a set of unique majors found across all students.

    Uses a set comprehension — like a list comprehension but produces a set,
    guaranteeing uniqueness without manual deduplication.

    Args:
        students (list): A list of student tuples (ID, Name, Major).

    Returns:
        set: A set of unique major strings (order not guaranteed).

    Example:
        >>> students = [(101, "Alice", "CS"), (102, "Bob", "Math"), (103, "Eve", "CS")]
        >>> unique_majors(students)
        {'CS', 'Math'}
    """
    return {student[2] for student in students}


def major_summary(students):
    """
    Return a dict mapping each unique major to the count of students in it.

    Combines set comprehension (to find unique majors) with a dictionary
    comprehension (to count students per major).

    Args:
        students (list): A list of student tuples (ID, Name, Major).

    Returns:
        dict: e.g. {'Computer Science': 2, 'Mathematics': 2, 'Physics': 1}
    """
    majors = unique_majors(students)
    return {major: sum(1 for s in students if s[2] == major) for major in majors}