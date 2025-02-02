from flask import Flask, render_template, request, send_file
import requests
import pandas as pd
import os
from typing import List, Dict, Optional

app = Flask(__name__)

SEMESTER_IDS = [221, 222, 223, 231, 233, 241, 243]
API_URL = "http://203.190.10.22:8189/result"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

def calculate_sgpa(results: List[Dict]) -> float:
    if not results:
        return 0.0
    
    total_points = 0.0
    total_credits = 0.0
    
    for result in results:
        point = result.get('pointEquivalent')
        credit = result.get('totalCredit')
        
        if point is not None and credit is not None:
            total_points += float(point) * float(credit)
            total_credits += float(credit)
    
    return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

def fetch_results(student_id: int, semester_id: int) -> Optional[List[Dict]]:
    try:
        response = requests.get(
            f"{API_URL}?grecaptcha&semesterId={semester_id}&studentId=221-15-{student_id}", 
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return data if isinstance(data, list) else None
        return None
    except:
        return None

@app.route('/', methods=['GET'])
def index():
    if 'startStudentId' in request.args and 'endStudentId' in request.args:
        try:
            start_id = int(request.args.get('startStudentId'))
            end_id = int(request.args.get('endStudentId'))
            
            results = []
            for student_id in range(start_id, end_id + 1):
                student_data = {'Student ID': f'221-15-{student_id}'}
                valid_sgpas = []
                
                for semester_id in SEMESTER_IDS:
                    semester_results = fetch_results(student_id, semester_id)
                    sgpa = calculate_sgpa(semester_results or [])
                    student_data[f'Semester {semester_id}'] = sgpa
                    if sgpa > 0:
                        valid_sgpas.append(sgpa)
                
                if valid_sgpas:
                    student_data['CGPA'] = round(sum(valid_sgpas) / len(valid_sgpas), 2)
                    results.append(student_data)

            if results:
                ensure_output_dir()
                excel_path = os.path.join(OUTPUT_DIR, 'student_results.xlsx')
                df = pd.DataFrame(results)
                columns = ['Student ID'] + [f'Semester {sem}' for sem in SEMESTER_IDS] + ['CGPA']
                df = df[columns]
                df.to_excel(excel_path, index=False)
                return send_file(excel_path, as_attachment=True)
            
            return render_template('index.html', message="No results found")
            
        except Exception as e:
            return render_template('index.html', message=f"Error: {str(e)}")
    
    return render_template('index.html')

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

if __name__ == '__main__':
    app.run(debug=True)