# pdf_checker/data/question_manager.py
from typing import List, Optional, Dict

from app.error_handler import ErrorHandler
from data.data_manager import DataManager

class QuestionManager:
    """Manages question navigation and data retrieval."""
    
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.question_keys: List[str] = []
        self.current_question_index: int = 0
    
    def initialize_questions(self) -> bool:
        """Initialize question keys from OCR data."""
        if not self.data_manager.ocr_data or "questions" not in self.data_manager.ocr_data:
            return False
        
        try:
            question_keys_from_ocr = list(self.data_manager.ocr_data['questions'].keys())
            
            extracted_keys = []
            for key in question_keys_from_ocr:
                if key.startswith('qn_'):
                    try:
                        num_part = int(key[3:])
                        extracted_keys.append(num_part)
                    except ValueError:
                        ErrorHandler.handle_error(f"Invalid question key format in ocr data: {key}")
                        continue
            
            sorted_keys_int = sorted(extracted_keys)
            
            self.question_keys = [str(k) for k in sorted_keys_int]
            
            return len(self.question_keys) > 0
        except Exception as e:
            ErrorHandler.handle_error(f"Failed to initialize questions from OCR data: {e}")
            return False
    
    def get_current_question_key(self) -> Optional[str]:
        """Get the current question key."""
        if 0 <= self.current_question_index < len(self.question_keys):
            return self.question_keys[self.current_question_index]
        return None
    
    def get_question_bbox_data(self, question_key: str) -> Optional[Dict]:
        """Get bounding box data for a specific question."""
        return self.data_manager.bbox_data.get(question_key) if self.data_manager.bbox_data else None
    
    def get_question_ocr_data(self, question_key: str) -> Dict:
        """Get OCR data for a specific question."""
        question_key_str = f"qn_{question_key}"
        if (self.data_manager.ocr_data and 
            isinstance(self.data_manager.ocr_data, dict)):
            return self.data_manager.ocr_data.get("questions", {}).get(question_key_str, {})
        return {}
    
    def update_question_ocr_data(self, question_key: str, data: Dict) -> bool:
        """Update OCR data for a specific question."""
        try:
            question_key_str = f"qn_{question_key}"
            
            if not isinstance(self.data_manager.ocr_data, dict):
                self.data_manager.ocr_data = {}
            
            if "questions" not in self.data_manager.ocr_data:
                self.data_manager.ocr_data["questions"] = {}
            
            self.data_manager.ocr_data["questions"][question_key_str] = data
            return True
        except Exception as e:
            ErrorHandler.handle_error(f"Failed to update question data: {e}")
            return False
    
    def can_go_previous(self) -> bool:
        """Check if previous question is available."""
        return self.current_question_index > 0
    
    def can_go_next(self) -> bool:
        """Check if next question is available."""
        return self.current_question_index < len(self.question_keys) - 1
    
    def go_to_question(self, index: int) -> bool:
        """Navigate to a specific question index."""
        if 0 <= index < len(self.question_keys):
            self.current_question_index = index
            return True
        return False
    
    def go_to_previous(self) -> bool:
        """Navigate to previous question."""
        if self.can_go_previous():
            self.current_question_index -= 1
            return True
        return False
    
    def go_to_next(self) -> bool:
        """Navigate to next question."""
        if self.can_go_next():
            self.current_question_index += 1
            return True
        return False
