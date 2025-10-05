"""
PDF Checker Application - Main Entry Point

This module serves as the main entry point for the PDF Checker application,
which provides question viewing and OCR correction functionality.
"""

import os
import sys
from pathlib import Path
from typing import Optional
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
from pdf_checker.app.session_manager import SessionManager


def main() -> None:
    """
    Main entry point for the PDF Checker application.
    
    Orchestrates the application setup, validation, and execution.
    """
    # 1. Basic application setup
    ErrorHandler.setup_logging()
    app = QApplication(sys.argv)

    # 2. Get script directory and set up paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # 3. Initialize components in a "blank" state
    view = MainView()
    session_manager = SessionManager(script_dir / "session.json")
    
    # Create managers with an initial empty state
    data_manager = DataManager(None, None, None)
    question_manager = QuestionManager(data_manager)
    path_manager = PathManager(str(project_root)) # Path manager might need a base path
    image_dir = project_root / "Data"/ "PYQ" / "BIO" / "json" / "images"

    # Create the presenter
    presenter = AppPresenter(
        view,
        question_manager,
        data_manager,
        path_manager,
        str(image_dir),
        session_manager=session_manager,
        initial_question_index=0 # Start at 0, will be updated by session
    )
    view.set_presenter(presenter)

    # 4. Set up exit behavior
    app.aboutToQuit.connect(presenter.save_session)

    # 5. Show the main window
    view.showMaximized()

    # 6. Load last session if it exists
    session = session_manager.load_session()
    if session and "ocr_json_path" in session:
        ocr_path = Path(session["ocr_json_path"])
        if ocr_path.exists():
            initial_question_index = session.get("last_question_index", 0)
            # Presenter's load_files will handle creating new data/question managers and showing the right question
            presenter.load_files(ocr_path, initial_question_index)
        else:
            view.show_message("Session Error", f"Could not find the last used file: {ocr_path}", msg_type="error")

    # 7. Start the Qt event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
