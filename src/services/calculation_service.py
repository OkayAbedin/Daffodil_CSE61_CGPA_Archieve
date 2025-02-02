from utils.constants import SEMESTER_IDS

class CalculationService:
    def calculate_sgpa(self, results):
        semester_gpas = {}
        
        # Group results by semester
        for result in results:
            semester_id = result['semesterId']
            if semester_id not in semester_gpas:
                semester_gpas[semester_id] = {
                    'total_points': 0,
                    'total_credits': 0
                }
            
            semester_gpas[semester_id]['total_points'] += result['pointEquivalent'] * result['totalCredit']
            semester_gpas[semester_id]['total_credits'] += result['totalCredit']
        
        # Calculate SGPA for each semester
        sgpas = []
        for semester_id in SEMESTER_IDS:
            if semester_id in semester_gpas:
                semester = semester_gpas[semester_id]
                if semester['total_credits'] > 0:
                    sgpa = semester['total_points'] / semester['total_credits']
                    sgpas.append(sgpa)
        
        # Calculate CGPA
        return sum(sgpas) / len(sgpas) if sgpas else 0