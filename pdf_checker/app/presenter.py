from typing import Dict
import os
from typing import Dict
import fitz # PyMuPDF
from pathlib import Path

from data.data_manager import DataManager
from data.question_manager import QuestionManager
from data.validator import DataValidator
from utils.path_manager import PathManager
from app.error_handler import ErrorHandler
from app.config import Config

class AppPresenter:
    """Handles the application logic and acts as a presenter in an MVP pattern."""

    def __init__(self, view, question_manager: QuestionManager, data_manager: DataManager, path_manager: PathManager, image_dir: str):
        self.view = view
        self.question_manager = question_manager
        self.data_manager = data_manager
        self.path_manager = path_manager
        self.image_dir = image_dir
        self.app_config = Config()
        self.project_root = self.path_manager.base_dir.parent.parent.parent
        self.view.set_project_root(self.project_root)

    def load_files(self, ocr_json_path: Path):
        """
        Load PDF, OCR JSON, and Bbox JSON files based on the provided OCR JSON path.
        """
        try:
            ocr_json_path = Path(ocr_json_path)
            
            # Deduce PDF path from a file like NEET_2024_BIO.json
            stem = ocr_json_path.stem
            stem_parts = stem.split('_')
            
            if len(stem_parts) > 1:
                year = stem_parts[1] # Assumes format like XXX_YYYY_...
            else:
                year = stem # Assumes format is just YYYY
            
            # Further check if year is a valid year
            if not year.isdigit() or len(year) != 4:
                self.view.show_message("Error", f"Could not determine year from filename: {ocr_json_path.name}", msg_type="error")
                return
            # Assumes the pdf is in a parent directory of the json file's location
            pdf_path = next(ocr_json_path.parent.parent.parent.rglob(f"NEET_{year}.pdf"))

            # Deduce Bbox JSON path
            bbox_json_path = ocr_json_path.with_name(f"{ocr_json_path.stem}_bbox.json")

            if not pdf_path.exists():
                self.view.show_message("Error", f"PDF file not found: {pdf_path}", msg_type="error")
                return

            if not bbox_json_path.exists():
                self.view.show_message("Error", f"Bbox JSON file not found: {bbox_json_path}", msg_type="error")
                return

            # Create new instances of managers
            self.data_manager = DataManager(str(pdf_path), str(bbox_json_path), str(ocr_json_path))
            self.question_manager = QuestionManager(self.data_manager)
            
            # Restart the application with the new data
            self.start()

        except StopIteration:
            self.view.show_message("Error", f"Could not find PDF for year {year}", msg_type="error")
        except Exception as e:
            ErrorHandler.handle_error(f"Failed to load files: {e}", show_message=False)
            self.view.show_message("Error", f"An error occurred while loading files: {e}", msg_type="error")

    def start(self):
        """Initializes the application state and displays the first question."""
        if not self.data_manager.load_all_data():
            self.view.destroy()
            return

        if not self.question_manager.initialize_questions():
            self.view.show_message("Info", "No questions found.")
            return

        self.view.populate_question_list(self.question_manager.question_keys)
        self._show_question(0)

    def _show_question(self, index: int):
        if not self.question_manager.go_to_question(index):
            return

        question_key = self.question_manager.get_current_question_key()
        if not question_key or not self.data_manager.doc:
            return

        try:
            bbox_data = self.question_manager.get_question_bbox_data(question_key)
            if not bbox_data:
                raise ValueError("Bounding box data not found.")

            page = self.data_manager.doc.load_page(bbox_data["page"] - 1)
            rect = fitz.Rect(bbox_data["bbox"]) + (-self.app_config.IMAGE_PADDING, -self.app_config.IMAGE_PADDING, self.app_config.IMAGE_PADDING, self.app_config.IMAGE_PADDING)
            pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(self.app_config.IMAGE_ZOOM_FACTOR, self.app_config.IMAGE_ZOOM_FACTOR)) #type: ignore

            total_questions = len(self.question_manager.question_keys)
            display_data = {
                'pixmap': pix,
                'label': f"Question {question_key} ({index + 1}/{total_questions})",
                'prev_state': 'normal' if self.question_manager.can_go_previous() else 'disabled',
                'next_state': 'normal' if self.question_manager.can_go_next() else 'disabled',
                'index': index,
                'ocr_data': self.question_manager.get_question_ocr_data(question_key)
            }
            self.view.update_question_display(display_data)

        except Exception as e:
            ErrorHandler.handle_error(f"Failed to display question {question_key}: {e}", show_message=False)
            self.view.show_message("Error", f"Failed to display question {question_key}.", msg_type="error")

    def handle_listbox_select(self, index: int):
        self._show_question(index)

    def handle_next_question(self):
        if self.question_manager.go_to_next():
            self._show_question(self.question_manager.current_question_index)

    def handle_previous_question(self):
        if self.question_manager.go_to_previous():
            self._show_question(self.question_manager.current_question_index)

    def handle_goto_question(self, value: int):
        """Handles jumping to a specific question from the spinbox."""
        # The spinbox value is a question number. Find the corresponding index.
        try:
            index = self.question_manager.question_keys.index(str(value))
            self._show_question(index)
        except ValueError:
            # This can happen if the spinbox value is not a valid question number (e.g., gaps)
            # We can choose to ignore it or provide feedback. For now, we ignore it.
            pass

    def handle_save(self):
        """Handles the save action from the menu."""
        form_data = self.view.get_editor_data()
        self.handle_save_form_data(form_data)

    def handle_save_form_data(self, form_data: Dict):
        question_key = self.question_manager.get_current_question_key()
        if not question_key:
            self.view.show_message("Error", "No question selected to save.", msg_type="error")
            return

        try:
            # Convert correctOption to int
            form_data['correctOption'] = int(form_data['correctOption'])

            is_valid, errors = DataValidator.validate_question_data(form_data)
            if not is_valid:
                self.view.show_message("Validation Error", "\n".join(errors), msg_type="error")
                return

            if self.question_manager.update_question_ocr_data(question_key, form_data):
                if self.data_manager.save_ocr_data():
                    self.view.show_message("Success", f"Changes for Question {question_key} saved successfully!")
                    # Refresh view to show updated data (e.g., imagePath)
                    self._show_question(self.question_manager.current_question_index)
                    self.handle_next_question()
                else:
                    self.view.show_message("Error", "Failed to save data to file.", msg_type="error")
            else:
                self.view.show_message("Error", "Failed to update question data.", msg_type="error")
        except ValueError:
            self.view.show_message("Validation Error", "Correct option must be a number.", msg_type="error")
        except Exception as e:
            ErrorHandler.handle_error(f"An error occurred while saving: {e}", show_message=False)
            self.view.show_message("Error", "An error occurred while saving.", msg_type="error")

    def handle_save_selection(self):
        question_key = self.question_manager.get_current_question_key()
        if not question_key: return

        # cropped_image = self.view.get_cropped_image()
        cropped_image = self.view.selection_manager.get_cropped_image()
        if not cropped_image: return

        year = "unknown_year"
        if self.data_manager.ocr_data is not None:
            year = self.data_manager.ocr_data.get("examDetails", {}).get("year", "unknown_year")
        image_dir_path = self.path_manager.ensure_directory_exists(self.image_dir)
        image_path = image_dir_path / f"{year}_{question_key}.jpg"

        try:
            cropped_image.save(str(image_path), self.app_config.IMAGE_FORMAT)
            
            question_data = self.question_manager.get_question_ocr_data(question_key)
            question_data["imagePath"] = str(image_path.relative_to(self.project_root))

            if self.question_manager.update_question_ocr_data(question_key, question_data):
                if self.data_manager.save_ocr_data():
                    self.view.show_message("Success", f"Screenshot saved to {image_path} and JSON updated.")
                    self._show_question(self.question_manager.current_question_index)
                else:
                    raise IOError("Failed to save updated JSON file.")
            else:
                raise ValueError("Failed to update question data in the manager.")

        except Exception as e:
            ErrorHandler.handle_error(f"Failed to save selection: {e}", show_message=False)
            self.view.show_message("Error", f"Failed to save selection: {e}", msg_type="error")

    def handle_closing(self):
        self.data_manager.close_document()
        self.view.destroy()
