class Result:
    def __init__(self, semester_id, course_title, total_credit, cgpa):
        self.semester_id = semester_id
        self.course_title = course_title
        self.total_credit = total_credit
        self.cgpa = cgpa

    def __repr__(self):
        return f"Result(semester_id={self.semester_id}, course_title='{self.course_title}', total_credit={self.total_credit}, cgpa={self.cgpa})"