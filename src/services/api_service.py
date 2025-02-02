class ApiService:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_results(self, student_id, semester_id):
        import requests

        url = f"{self.base_url}/result?grecaptcha&semesterId={semester_id}&studentId={student_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()