from PySide6.QtCore import QEvent, Qt

class FocusManager:
    """Manages focus trapping and tab navigation for editor widgets."""
    
    def __init__(self, main_view):
        self.main_view = main_view
        self.focus_widgets = [
            main_view.ui.txt_editor_question,
            main_view.ui.editor_option1_lineEdit,
            main_view.ui.editor_option2_lineEdit,
            main_view.ui.editor_option3_lineEdit,
            main_view.ui.editor_option4_lineEdit,
            main_view.ui.le_editor_answer,
            main_view.ui.lineEdit,
            main_view.ui.spinBox_goto_question
        ]
        self._install_event_filters()
    
    def _install_event_filters(self):
        """Install event filters on all focus-managed widgets."""
        for widget in self.focus_widgets:
            widget.installEventFilter(self.main_view)
    
    def handle_tab_navigation(self, source, event):
        """Handle tab navigation between focus widgets."""
        if event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Tab:
            try:
                current_index = self.focus_widgets.index(source)
                is_shift_pressed = event.modifiers() & Qt.KeyboardModifier.ShiftModifier
                
                if is_shift_pressed:  # Backward Tab
                    prev_index = (current_index - 1 + len(self.focus_widgets)) % len(self.focus_widgets)
                    self.focus_widgets[prev_index].setFocus()
                else:  # Forward Tab
                    next_index = (current_index + 1) % len(self.focus_widgets)
                    self.focus_widgets[next_index].setFocus()
                    
                return True  # Consume event
            except ValueError:
                pass  # Source not in our list, let default handling occur
        return False