# lib/data_processing.py
# Handles formatting and displaying student records.
# Separates presentation logic from data storage and filtering.


def format_student_data(student):
    """
    Return a human-readable string for a single student tuple.

    Args:
        student (tuple): A student tuple in the format (ID, Name, Major).

    Returns:
        str: Formatted as "ID: <id> | Name: <name> | Major: <major>"

    Example:
        >>> format_student_data((101, "Alice Johnson", "Computer Science"))
        'ID: 101 | Name: Alice Johnson | Major: Computer Science'
    """
    student_id, name, major = student   # unpack tuple for readability
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students):
    """
    Print formatted details for every student in the given list.

    Iterates through each student and delegates formatting to
    format_student_data, keeping display and format logic separate.

    Args:
        students (list): A list of student tuples (ID, Name, Major).

    Returns:
        None
    """
    for student in students:
        print(format_student_data(student))