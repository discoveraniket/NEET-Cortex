# pdf_checker/app/error_handler.py
import logging
from tkinter import messagebox
from typing import Optional

class ErrorHandler:
    """Handles error logging and user notifications."""
    
    @staticmethod
    def setup_logging() -> None:
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('question_viewer.log'),
                logging.StreamHandler()
            ]
        )
    
    @staticmethod
    def handle_error(error_msg: str, exception: Optional[Exception] = None, 
                   show_message: bool = True) -> None:
        """Handle errors with logging and user notification."""
        log_msg = f"{error_msg}: {exception}" if exception else error_msg
        logging.error(log_msg)
        
        if show_message:
            messagebox.showerror("Error", error_msg)
