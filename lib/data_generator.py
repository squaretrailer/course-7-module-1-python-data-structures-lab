def student_generator(students, major):
    """
    Return a generator that lazily yields students filtered by major.

    Unlike a list comprehension, this generator does NOT load all matching
    students into memory at once. Instead it produces one student tuple
    at a time as the caller iterates — ideal for large datasets.

    Args:
        students (list): A list of student tuples (ID, Name, Major).
        major (str): The major to filter by (case-sensitive).

    Returns:
        generator: A generator object yielding matching student tuples.

    Example:
        >>> students = [(101, "Alice", "CS"), (102, "Bob", "Math")]
        >>> gen = student_generator(students, "Math")
        >>> next(gen)
        (102, 'Bob', 'Math')
    """
    return (student for student in students if student[2] == major)


def all_student_generator(students):
    """
    Return a generator that lazily yields ALL students regardless of major.

    Useful when you want to stream or pipeline the full dataset without
    materialising it as a new list in memory.

    Args:
        students (list): A list of student tuples (ID, Name, Major).

    Returns:
        generator: A generator object yielding every student tuple.
    """
    return (student for student in students)