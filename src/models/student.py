class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def get_results(self):
        return self.results

    def calculate_cgpa(self):
        total_points = 0
        total_credits = 0
        for result in self.results:
            total_points += result.cgpa * result.total_credit
            total_credits += result.total_credit
        return total_points / total_credits if total_credits > 0 else 0

    def __repr__(self):
        return f"Student(student_id={self.student_id})"