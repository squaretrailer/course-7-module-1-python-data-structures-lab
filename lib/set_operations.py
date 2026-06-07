def unique_majors(students):
    """
    Return a set of unique student majors using set comprehension.

    Args:
        students: list of student tuples (ID, Name, Major)

    Returns:
        a set containing each unique major found in the student list
    """
    return {student[2] for student in students}