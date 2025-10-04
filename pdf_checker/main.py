"""
PDF Checker Application - Main Entry Point

This module serves as the main entry point for the PDF Checker application,
which provides question viewing and OCR correction functionality.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Optional
from PySide6.QtWidgets import QApplication

# Add the project root to the Python path to allow for absolute imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(project_root)) # Add parent of pdf_checker to path
sys.path.insert(0, project_root) # Add pdf_checker to path

from pdf_checker.app.presenter import AppPresenter
from pdf_checker.ui.main_view import MainView
from pdf_checker.data.data_manager import DataManager
from pdf_checker.data.question_manager import QuestionManager
from pdf_checker.utils.path_manager import PathManager
from pdf_checker.app.error_handler import ErrorHandler


class ApplicationConfig:
    """Configuration class for application settings and paths."""
    
    def __init__(self, script_dir: str):
        self.script_dir = Path(script_dir)
        self.project_root = self.script_dir.parent
        self._setup_paths()
    
    def _setup_paths(self) -> None:
        """Set up Python path for imports."""
        sys.path.insert(0, str(self.project_root))
        sys.path.insert(0, str(self.script_dir))


class ArgumentParser:
    """Handles command line argument parsing."""
    
    def __init__(self, script_dir: Path, default_pdf: Optional[Path], default_bbox: Optional[Path], default_ocr: Optional[Path]):
        self.script_dir = script_dir
        self.default_pdf = default_pdf
        self.default_bbox = default_bbox
        self.default_ocr = default_ocr
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create and configure the argument parser."""
        parser = argparse.ArgumentParser(
            description='Question Viewer and OCR Corrector'
        )
        
        parser.add_argument(
            '--pdf',
            default=str(self.default_pdf) if self.default_pdf else None,
            required=not self.default_pdf,
            help='Path to the PDF file'
        )
        parser.add_argument(
            '--bbox-json',
            default=str(self.default_bbox) if self.default_bbox else None,
            required=not self.default_bbox,
            help='Path to bounding box JSON file'
        )
        parser.add_argument(
            '--ocr-json',
            default=str(self.default_ocr) if self.default_ocr else None,
            required=not self.default_ocr,
            help='Path to OCR JSON file'
        )
        
        return parser
    
    def parse_arguments(self) -> argparse.Namespace:
        """Parse and return command line arguments."""
        return self.parser.parse_args()


class FileValidator:
    """Validates existence of required files."""
    
    @staticmethod
    def validate_files(file_paths: List[Path]) -> Tuple[bool, List[str]]:
        """
        Validate that all required files exist.
        
        Args:
            file_paths: List of file paths to validate
            
        Returns:
            Tuple of (is_valid, list_of_missing_files)
        """
        missing_files = []
        
        for file_path in file_paths:
            if not file_path.exists():
                missing_files.append(f"{file_path.name}: {file_path}")
        
        return len(missing_files) == 0, missing_files


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


def setup_application(script_path: str) -> ApplicationConfig:
    """
    Set up the application configuration and paths.
    
    Args:
        script_path: Path to the main script
        
    Returns:
        ApplicationConfig instance
    """
    config = ApplicationConfig(script_path)
    ErrorHandler.setup_logging()
    return config


def parse_arguments(script_dir: Path, default_pdf: Optional[Path], default_bbox: Optional[Path], default_ocr: Optional[Path]) -> Tuple[Path, Path, Path, Path]:
    """
    Parse command line arguments and resolve file paths.
    
    Args:
        script_dir: Directory containing the main script
        default_pdf: Default path to the PDF file
        default_bbox: Default path to the bounding box JSON file
        default_ocr: Default path to the OCR JSON file
        
    Returns:
        Tuple of (pdf_path, bbox_path, ocr_path, image_dir)
    """
    arg_parser = ArgumentParser(script_dir, default_pdf, default_bbox, default_ocr)
    args = arg_parser.parse_arguments()
    
    # Resolve absolute paths
    pdf_path = Path(args.pdf).resolve()
    bbox_path = Path(args.bbox_json).resolve()
    ocr_path = Path(args.ocr_json).resolve()
    image_dir = (ocr_path.parent / "images").resolve()
    
    return pdf_path, bbox_path, ocr_path, image_dir


def validate_required_files(pdf_path: Path, bbox_path: Path, ocr_path: Path) -> None:
    """
    Validate that all required files exist.
    
    Args:
        pdf_path: Path to PDF file
        bbox_path: Path to bounding box JSON file
        ocr_path: Path to OCR JSON file
        
    Raises:
        SystemExit: If any required files are missing
    """
    required_files = [pdf_path, bbox_path, ocr_path]
    is_valid, missing_files = FileValidator.validate_files(required_files)
    
    if not is_valid:
        error_message = "The following required files were not found:\n" + "\n".join(missing_files)
        ErrorHandler.handle_error(error_message)
        sys.exit(1)


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
    setup_application(str(script_dir))

    # # Define default file paths for easy modification
    # default_pdf = None
    # default_bbox = None
    # default_ocr = None
    
    # Define default file paths for easy modification
    default_pdf = script_dir / ".." / "PYQ" / "BIO" / "pdf" / "2018.pdf"
    default_bbox = script_dir / ".." / "PYQ" / "BIO" / "json" / "bbox" /"2018_bbox.json"
    default_ocr = script_dir / ".." / "PYQ" / "BIO" / "json" / "2018.json"


    # Parse and validate arguments
    pdf_path, bbox_path, ocr_path, image_dir = parse_arguments(script_dir, default_pdf, default_bbox, default_ocr)
    validate_required_files(pdf_path, bbox_path, ocr_path)
    
    # Run the application
    exit_code = run_application(pdf_path, bbox_path, ocr_path, image_dir)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()