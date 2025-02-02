class ExcelService:
    def __init__(self, filename='student_results.xlsx'):
        self.filename = filename

    def generate_excel(self, data):
        import pandas as pd

        df = pd.DataFrame(data)
        df.to_excel(self.filename, index=False)