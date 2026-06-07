def filter_students_by_major(students, major):
    """
    Return a filtered list of students who match the given major.

    Args:
        students: list of tuples (ID, Name, Major)
        major: string representing the major to filter by

    Returns:
        list of student tuples whose major matches the given major
    """
    return [student for student in students if student[2] == major]