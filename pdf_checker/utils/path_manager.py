# pdf_checker/utils/path_manager.py
from pathlib import Path

class PathManager:
    """Manages file paths and directory operations."""
    
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir).resolve()
    
    def get_absolute_path(self, relative_path: str) -> Path:
        """Convert relative path to absolute path."""
        return (self.base_dir / relative_path).resolve()
    
    def ensure_directory_exists(self, directory: str) -> Path:
        """Create directory if it doesn't exist."""
        path = self.get_absolute_path(directory)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def file_exists(self, file_path: str) -> bool:
        """Check if a file exists."""
        return self.get_absolute_path(file_path).exists()

    # def get_viewer_template_uri(self) -> str:
    #     """Get the file URI for the viewer_template.html."""
    #     return self.get_absolute_path("pdf_checker/resources/viewer_template.html").as_uri()
