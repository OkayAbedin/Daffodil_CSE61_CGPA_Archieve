def format_student_id(student_id):
    """Format the student ID to a standard format."""
    return student_id.strip().upper()

def validate_student_id(student_id):
    """Validate the student ID format."""
    if not isinstance(student_id, str) or len(student_id) != 11:
        raise ValueError("Invalid student ID format. It should be 11 characters long.")
    return True

def calculate_average_cgpa(results):
    """Calculate the average CGPA from a list of results."""
    total_cgpa = sum(result['cgpa'] for result in results)
    return total_cgpa / len(results) if results else 0

def extract_semester_ids(results):
    """Extract unique semester IDs from the results."""
    return list(set(result['semesterId'] for result in results))