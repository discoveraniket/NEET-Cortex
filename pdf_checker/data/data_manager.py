# pdf_checker/data/data_manager.py
import json
from typing import Optional, Dict
import fitz  # PyMuPDF

from app.config import Config
from app.error_handler import ErrorHandler

class DataManager:
    """Manages PDF and JSON data operations."""
    
    def __init__(self, pdf_path: str, bbox_json_path: str, ocr_json_path: str):
        self.pdf_path = pdf_path
        self.bbox_json_path = bbox_json_path
        self.ocr_json_path = ocr_json_path
        self.doc: Optional[fitz.Document] = None
        self.bbox_data: Optional[Dict] = None
        self.ocr_data: Optional[Dict] = None
    
    def load_all_data(self) -> bool:
        """Load PDF and JSON data with error handling."""
        try:
            self.doc = fitz.open(self.pdf_path)
            
            with open(self.bbox_json_path, 'r', encoding=Config.DEFAULT_ENCODING) as f:
                self.bbox_data = json.load(f)
            
            with open(self.ocr_json_path, 'r', encoding=Config.DEFAULT_ENCODING) as f:
                self.ocr_data = json.load(f)
            
            return True
            
        except Exception as e:
            ErrorHandler.handle_error(f"Failed to load required files: {e}")
            return False
    
    def save_ocr_data(self) -> bool:
        """Save OCR data to JSON file."""
        try:
            with open(self.ocr_json_path, 'w', encoding=Config.DEFAULT_ENCODING) as f:
                json.dump(self.ocr_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            ErrorHandler.handle_error(f"Failed to save OCR data: {e}")
            return False
    
    def close_document(self) -> None:
        """Close the PDF document."""
        if self.doc:
            self.doc.close()
            self.doc = None
