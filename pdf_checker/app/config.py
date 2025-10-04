# pdf_checker/app/config.py
class Config:
    """Configuration constants for the application."""
    RESIZE_HANDLE_SIZE = 5
    IMAGE_ZOOM_FACTOR = 2
    IMAGE_PADDING = 10
    
    # UI constants
    CANVAS_BG = "gray"
    SELECTION_OUTLINE = "red"
    SELECTION_DASH = (4, 2)
    
    # File constants
    DEFAULT_ENCODING = "utf-8"
    IMAGE_FORMAT = "JPEG"
