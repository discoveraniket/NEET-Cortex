from PySide6.QtWidgets import QMainWindow, QRubberBand, QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtGui import QPixmap, QImage, QKeySequence, QShortcut, QAction
from PySide6.QtCore import Qt, QRect, QPoint, QEvent, QSize
# import fitz  # PyMuPDF
import os
from typing import Optional, Dict, Any

from .main_ui import Ui_MainWindow
from .managers.focus_manager import FocusManager
from .managers.html_renderer import HTMLRenderer
from .managers.selection_manager import SelectionManager
from .managers.table_manager import TableManager

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize managers
        self.focus_manager = FocusManager(self)
        self.selection_manager = SelectionManager(self)
        self.html_renderer = HTMLRenderer()
        self.table_manager = TableManager(self)
        
        # Initialize state
        self.project_root = None
        self.original_image_pixmap = None
        self.presenter = None
        
        self._setup_ui()
        self._setup_shortcuts()
        self._setup_connections()
    
    def _setup_ui(self):
        """Configure UI elements and initial state."""
        # Table configuration
        self.ui.tbl_match.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Splitter configurations
        self.ui.tableSplitter.setSizes([100, 100])
        self.ui.questionSplitter.setSizes([400, 200])
        
        # Install event filter for PDF rendering label
        self.ui.pdf_render_label.installEventFilter(self)
    
    def _setup_shortcuts(self):
        """Setup keyboard shortcuts."""
        shortcuts = {
            "Ctrl+T": lambda: self.ui.tab_editor.setCurrentWidget(self.ui.tableTab),
            "Ctrl+Q": lambda: self.ui.tab_editor.setCurrentWidget(self.ui.questionTab),
        }
        # Other shortcuts are defined in the .ui file.
        
        for key_sequence, callback in shortcuts.items():
            shortcut = QShortcut(QKeySequence(key_sequence), self)
            shortcut.activated.connect(callback)
    
    def _setup_connections(self):
        """Connect signals to slots."""
        self.ui.tab_editor.currentChanged.connect(self._on_tab_changed)
        self.ui.actionOpen.triggered.connect(self._open_file)

    def _open_file(self):
        """Open a file dialog to select a JSON file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open JSON File",
            str(self.project_root) if self.project_root else "",
            "JSON Files (*.json)"
        )

        if file_path:
            if self.presenter:
                self.presenter.load_files(file_path)
    
    def set_presenter(self, presenter):
        """Connect signals from the UI to the presenter's methods."""
        self.presenter = presenter
        
        # Connect navigation controls
        self.ui.actionNext.triggered.connect(self.presenter.handle_next_question)
        self.ui.actionPrevious.triggered.connect(self.presenter.handle_previous_question)
        self.ui.spinBox_goto_question.valueChanged.connect(self.presenter.handle_goto_question)

        # TODO: Connect other signals from the UI to the presenter.
        # self.ui.actionUpdate.triggered.connect(self.presenter.handle_update)
        self.ui.actionSave.triggered.connect(self.presenter.handle_save)
        self.ui.actionCapture.triggered.connect(self.presenter.handle_save_selection)

    def set_project_root(self, path):
        self.project_root = path

    def update_question_display(self, display_data: dict):
        """Update the UI with data for the current question."""
        self.selection_manager.rubber_band.hide()

        self._update_pdf_view(display_data.get('pixmap'))
        self._update_question_content(display_data.get('ocr_data', {}))
        self._update_navigation_controls()
        self._update_editor_fields(display_data.get('ocr_data', {}))
        self._update_image_display(display_data.get('ocr_data', {}))
        
        # Set initial focus
        self.ui.txt_editor_question.setFocus()

    def _update_pdf_view(self, pixmap):
        """Update PDF view with new pixmap."""
        if pixmap:
            qimage = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format.Format_RGB888)
            qpixmap = QPixmap.fromImage(qimage)
            self.ui.pdf_render_label.setPixmap(qpixmap)

    def _update_question_content(self, ocr_data: dict):
        """Update question and options in web view."""
        question_text = ocr_data.get("questionText", "")
        options = ocr_data.get("options", [])
        correct_option = ocr_data.get("correctOption")

        # Combine question and options into a single Markdown string
        markdown_content = f"{question_text}\n\n"
        option_lines = []
        for i, option in enumerate(options):
            # Using "1." for all items is valid in Markdown for an ordered list
            option_lines.append(f"1. {option}")
        
        markdown_content += "\n".join(option_lines)

        # Add the correct answer if it exists
        if correct_option:
            markdown_content += f"\n\n**Ans: {correct_option}**"
        
        # Generate the full HTML and set it in the web view
        combined_html = self.html_renderer.generate_html(markdown_content)
        self.ui.we_question.setHtml(combined_html)

    def _update_navigation_controls(self):
        """Update navigation controls state."""
        if not (self.presenter and self.presenter.question_manager):
            return
            
        question_keys = self.presenter.question_manager.question_keys
        current_index = self.presenter.question_manager.current_question_index
        
        if question_keys:
            min_q = int(question_keys[0])
            max_q = int(question_keys[-1])
            current_q = int(question_keys[current_index])

            self.ui.label_total_questions.setText(f"/ {max_q}")
        
            # Block signals to prevent feedback loop
            self.ui.spinBox_goto_question.blockSignals(True)
            self.ui.spinBox_goto_question.setRange(min_q, max_q)
            self.ui.spinBox_goto_question.setValue(current_q)
            self.ui.spinBox_goto_question.blockSignals(False)

        self.ui.actionNext.setEnabled(self.presenter.question_manager.can_go_next())
        self.ui.actionPrevious.setEnabled(self.presenter.question_manager.can_go_previous())

    def _update_editor_fields(self, ocr_data: dict):
        """Populate editor fields with OCR data."""
        self.ui.txt_editor_question.setPlainText(ocr_data.get("questionText", ""))
        
        # Update option fields
        editor_options = [
            self.ui.editor_option1_lineEdit,
            self.ui.editor_option2_lineEdit, 
            self.ui.editor_option3_lineEdit,
            self.ui.editor_option4_lineEdit
        ]
        
        options = ocr_data.get("options", [])
        for i, widget in enumerate(editor_options):
            widget.setText(options[i] if i < len(options) else "")
        
        self.ui.le_editor_answer.setText(str(ocr_data.get("correctOption", "")))
        self.ui.le_editor_imagePath.setText(ocr_data.get("imagePath", ""))
        
        # Update table data
        match_data = ocr_data.get("matchColumns")
        self.table_manager.populate_table(match_data)

    def _update_image_display(self, ocr_data: dict):
        """Load and display the question image if available."""
        image_path = ocr_data.get("imagePath")
        
        if image_path and self.project_root:
            from pathlib import Path
            full_path = Path(self.project_root) / image_path
            if full_path.exists():
                self.original_image_pixmap = QPixmap(str(full_path))
                self.ui.label_image.setText("")
                self._rescale_image_label()
            else:
                self._clear_image_display("Image not found")
        else:
            self._clear_image_display("No Image")

    def _clear_image_display(self, message: str):
        """Clear image display and show message."""
        self.original_image_pixmap = None
        self.ui.label_image.setText(message)
        self.ui.label_image.setPixmap(QPixmap())

    def get_editor_data(self) -> dict:
        """Retrieve current data from editor fields."""
        data = {
            'questionText': self.ui.txt_editor_question.toPlainText(),
            'options': [
                self.ui.editor_option1_lineEdit.text(),
                self.ui.editor_option2_lineEdit.text(),
                self.ui.editor_option3_lineEdit.text(),
                self.ui.editor_option4_lineEdit.text(),
            ],
            'correctOption': self.ui.le_editor_answer.text(),
            'imagePath': self.ui.le_editor_imagePath.text(),
            'matchColumns': self.table_manager.get_table_data()
        }
        return data

    def _refresh_webview_from_editors(self):
        """Gather data from editors and refresh the question webview."""
        editor_data = self.get_editor_data()
        self._update_question_content(editor_data)

    def populate_question_list(self, question_keys: list):
        """Populate the question list widget."""
        # TODO: Implement this method to populate the QListWidget
        # self.ui.question_list_widget.clear()
        # self.ui.question_list_widget.addItems(question_keys)
        pass

    def show_message(self, title: str, message: str, msg_type: str = "info"):
        """Display a message box."""
        # TODO: Implement using QMessageBox
        pass

    def resizeEvent(self, event):
        """Handle window resize events."""
        super().resizeEvent(event)
        self._rescale_image_label()

    def _rescale_image_label(self):
        """Rescale the image label while maintaining aspect ratio."""
        if (hasattr(self, 'original_image_pixmap') and 
            self.original_image_pixmap and 
            not self.original_image_pixmap.isNull()):
            
            self.ui.label_image.setPixmap(self.original_image_pixmap.scaled(
                self.ui.label_image.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        else:
            self.ui.label_image.setPixmap(QPixmap())

    def eventFilter(self, source, event):
        """Handle events for focus management and selection."""
        # Handle focus/tab navigation
        if self.focus_manager.handle_tab_navigation(source, event):
            return True
            
        # Handle mouse events for selection
        if self.selection_manager.handle_mouse_event(source, event):
            return True
            
        # Handle live preview on focus out
        if event.type() == QEvent.Type.FocusOut:
            # Check if the widget that lost focus is one of our text editors
            if source in self.focus_manager.focus_widgets:
                self._refresh_webview_from_editors()

        return super().eventFilter(source, event)

    def _on_tab_changed(self, index):
        """Set focus to appropriate widget when tab changes."""
        current_widget = self.ui.tab_editor.widget(index)
        if current_widget == self.ui.questionTab:
            self.ui.txt_editor_question.setFocus()
        elif current_widget == self.ui.tableTab:
            self.ui.tbl_match.setFocus()