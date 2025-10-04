# pdf_checker/app/events.py
from enum import Enum
from typing import Dict, List, Callable, Any

class ResizeHandle(Enum):
    """Enumeration for resize handle positions."""
    TOP_LEFT = "top-left"
    TOP_RIGHT = "top-right"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_RIGHT = "bottom-right"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
    NONE = None


class EventTypes:
    """Event types for the event-driven architecture."""
    QUESTION_CHANGED = "question_changed"
    DATA_SAVED = "data_saved"
    IMAGE_SELECTION_CHANGED = "image_selection_changed"


class EventManager:
    """Manages event publishing and subscription."""
    
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event_type: str, listener: Callable) -> None:
        """Subscribe a listener to an event type."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)
    
    def publish(self, event_type: str, data: Any = None) -> None:
        """Publish an event to all subscribers."""
        for listener in self._listeners.get(event_type, []):
            listener(data)
