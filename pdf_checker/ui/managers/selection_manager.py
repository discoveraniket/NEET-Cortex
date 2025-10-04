from PySide6.QtWidgets import QRubberBand
from PySide6.QtCore import QRect, QSize, QEvent, Qt

class SelectionManager:
    """Manages PDF selection with rubber band functionality."""
    
    def __init__(self, main_view):
        self.main_view = main_view
        self.rubber_band = QRubberBand(QRubberBand.Shape.Rectangle, main_view.ui.pdf_render_label)
        self.selection_origin = None
    
    def handle_mouse_event(self, source, event):
        """Handle mouse events for rubber band selection."""
        if source != self.main_view.ui.pdf_render_label:
            return False
            
        if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
            self.selection_origin = event.pos()
            self.rubber_band.setGeometry(QRect(self.selection_origin, QSize()))
            self.rubber_band.show()
            return True
            
        elif event.type() == QEvent.Type.MouseMove and self.selection_origin:
            self.rubber_band.setGeometry(QRect(self.selection_origin, event.pos()).normalized())
            return True
            
        elif event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.LeftButton and self.selection_origin:
            self.selection_origin = None
            return True
            
        return False
    
    def get_cropped_image(self):
        """Get the selected area of the pixmap as a QImage."""
        pixmap = self.main_view.ui.pdf_render_label.pixmap()
        if not pixmap or self.rubber_band.geometry().isEmpty():
            self.rubber_band.hide()
            return None

        # Calculate the offset of the pixmap within the label (due to AlignCenter)
        label_size = self.main_view.ui.pdf_render_label.size()
        pixmap_size = pixmap.size()
        offset_x = (label_size.width() - pixmap_size.width()) / 2
        offset_y = (label_size.height() - pixmap_size.height()) / 2

        # Translate selection rectangle from label to pixmap coordinates
        pixmap_selection_rect = self.rubber_band.geometry().translated(-int(offset_x), -int(offset_y))
        pixmap_selection_rect = pixmap_selection_rect.intersected(pixmap.rect())

        if pixmap_selection_rect.isEmpty():
            self.rubber_band.hide()
            return None

        cropped_image = pixmap.copy(pixmap_selection_rect).toImage()
        self.rubber_band.hide()
        return cropped_image