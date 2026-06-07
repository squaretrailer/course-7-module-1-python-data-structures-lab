def format_student_data(student):
    """
    Return a formatted string for a given student tuple.

    Args:
        student: a tuple of (ID, Name, Major)

    Returns:
        a string formatted as "ID: <id> | Name: <name> | Major: <major>"
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students):
    """
    Loop through all students and print each student's details
    using the format_student_data function.

    Args:
        students: list of student tuples (ID, Name, Major)
    """
    for student in students:
        print(format_student_data(student))