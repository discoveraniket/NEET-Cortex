"""
PDF Checker Application - Main Entry Point

This module serves as the main entry point for the PDF Checker application,
which provides question viewing and OCR correction functionality.
"""

import sys
from pathlib import Path
from typing import List, Tuple
from PySide6.QtWidgets import QApplication

from pdf_checker.app.presenter import AppPresenter
from pdf_checker.ui.main_view import MainView
from pdf_checker.data.data_manager import DataManager
from pdf_checker.data.question_manager import QuestionManager
from pdf_checker.utils.path_manager import PathManager
from pdf_checker.app.error_handler import ErrorHandler
class ApplicationBuilder:
    """Builds and configures the application components."""
    
    def __init__(self, pdf_path: Path, bbox_path: Path, ocr_path: Path, image_dir: Path):
        self.pdf_path = pdf_path
        self.bbox_path = bbox_path
        self.ocr_path = ocr_path
        self.image_dir = image_dir
    
    def build(self) -> Tuple[QApplication, AppPresenter, MainView]:
        """
        Build and connect all application components.
        
        Returns:
            Tuple containing (QApplication, AppPresenter, MainView)
            
        Raises:
            Exception: If any component fails to initialize
        """
        # Create Qt Application
        app = QApplication(sys.argv)
        
        # Create managers and utilities
        data_manager = DataManager(
            str(self.pdf_path), 
            str(self.bbox_path), 
            str(self.ocr_path)
        )
        question_manager = QuestionManager(data_manager)
        path_manager = PathManager(str(self.pdf_path.parent))
        
        # Create and configure the View
        view = MainView()
        
        # Create and configure the Presenter
        presenter = AppPresenter(
            view, 
            question_manager, 
            data_manager, 
            path_manager, 
            str(self.image_dir)
        )
        
        # Connect components
        view.set_presenter(presenter)
        
        return app, presenter, view

def run_application(pdf_path: Path, bbox_path: Path, ocr_path: Path, image_dir: Path) -> int:
    """
    Run the main application.
    
    Args:
        pdf_path: Path to PDF file
        bbox_path: Path to bounding box JSON file
        ocr_path: Path to OCR JSON file
        image_dir: Path to image directory
        
    Returns:
        Application exit code
    """
    try:
        # Build application components
        app_builder = ApplicationBuilder(pdf_path, bbox_path, ocr_path, image_dir)
        app, presenter, view = app_builder.build()
        
        # Start application logic and show view
        presenter.start()
        view.showMaximized()
        
        # Start Qt event loop
        return app.exec()
        
    except Exception as e:
        ErrorHandler.handle_error(f"Failed to start application: {e}", exception=e)
        return 1

def main() -> None:
    """
    Main entry point for the PDF Checker application.
    
    Orchestrates the application setup, validation, and execution.
    """
    # Get script directory and set up application
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    sys.path.insert(0, str(project_root))
    sys.path.insert(0, str(script_dir))

    ErrorHandler.setup_logging()

    # Define default file paths for easy modification
    pdf_path = project_root / "Data"/ "PYQ" / "BIO" / "pdf" / "2018.pdf"
    bbox_path = project_root / "Data"/ "PYQ" / "BIO" / "json" / "bbox" /"2018_bbox.json"
    ocr_path = project_root / "Data"/ "PYQ" / "BIO" / "json" / "2018.json"
    image_dir = project_root / "Data"/ "PYQ" / "BIO" / "json" / "images"
    
    # Run the application
    exit_code = run_application(pdf_path, bbox_path, ocr_path, image_dir)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
