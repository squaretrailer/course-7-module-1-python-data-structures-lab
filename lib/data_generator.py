def student_generator(students, major):
    """
    Return a generator expression that yields students filtered by major.

    Args:
        students: list of student tuples (ID, Name, Major)
        major: string representing the major to filter by

    Returns:
        a generator that yields student tuples matching the given major
    """
    return (student for student in students if student[2] == major)