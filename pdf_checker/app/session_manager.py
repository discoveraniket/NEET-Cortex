import json
from pathlib import Path
from typing import Optional, Dict, Any

class SessionManager:
    """Manages saving and loading of application session data."""

    def __init__(self, session_file: Path):
        """
        Initializes the SessionManager.

        Args:
            session_file: Path to the session file (e.g., session.json).
        """
        self.session_file = session_file

    def save_session(self, ocr_json_path: str, question_index: int) -> None:
        """
        Saves the session data to a JSON file.

        Args:
            ocr_json_path: The full path to the OCR JSON file.
            question_index: The index of the last question viewed.
        """
        session_data = {
            "ocr_json_path": ocr_json_path,
            "last_question_index": question_index
        }
        try:
            with self.session_file.open('w') as f:
                json.dump(session_data, f, indent=4)
        except IOError as e:
            # Handle potential write errors, maybe log them
            print(f"Error saving session: {e}")

    def load_session(self) -> Optional[Dict[str, Any]]:
        """
        Loads the session data from a JSON file.

        Returns:
            A dictionary with session data or None if not found or invalid.
        """
        if not self.session_file.exists():
            return None
        try:
            with self.session_file.open('r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            # Handle potential read errors or corrupt file
            print(f"Error loading session: {e}")
            return None
