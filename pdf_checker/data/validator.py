# pdf_checker/data/validator.py
from typing import Dict, List, Tuple

class DataValidator:
    """Validates data structures and content."""
    
    @staticmethod
    def validate_question_data(data: Dict) -> Tuple[bool, List[str]]:
        """Validate question data structure and content."""
        errors = []
        
        # Validate question text
        if not data.get('questionText', '').strip():
            errors.append("Question text cannot be empty")
        
        # Validate options
        options = data.get('options', [])
        if len(options) < 2:
            errors.append("At least 2 options required")
        
        # Validate correct option
        try:
            correct_opt = int(data.get('correctOption', 0))
            if not (1 <= correct_opt <= len(options)):
                errors.append("Correct option index out of range")
        except (ValueError, TypeError):
            errors.append("Correct option must be a valid number")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_coordinates(coord: Tuple[float, float, float, float]) -> bool:
        """Validate that coordinates form a valid rectangle."""
        x0, y0, x1, y1 = coord
        return x0 < x1 and y0 < y1
