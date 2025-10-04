from PySide6.QtWidgets import QTableWidgetItem
from typing import Optional, Dict, Any

class TableManager:
    """Manages table editing and preview functionality."""
    
    def __init__(self, main_view):
        self.main_view = main_view
        self.main_view.ui.tbl_match.itemChanged.connect(self.on_table_item_changed)
    
    def populate_table(self, match_data: Optional[Dict[str, Any]] = None):
        """Populate the table with match column data."""
        self.main_view.ui.tbl_match.blockSignals(True)
        self.main_view.ui.tbl_match.setRowCount(0)  # Clear table

        if match_data and isinstance(match_data, dict):
            col_a = match_data.get("columnA", [])
            col_b = match_data.get("columnB", [])
            num_rows = max(len(col_a), len(col_b))
            
            self.main_view.ui.tbl_match.setRowCount(num_rows)
            self.main_view.ui.tbl_match.setColumnCount(2)
            self.main_view.ui.tbl_match.setHorizontalHeaderLabels(["Column A", "Column B"])

            for r in range(num_rows):
                if r < len(col_a):
                    self.main_view.ui.tbl_match.setItem(r, 0, QTableWidgetItem(str(col_a[r])))
                if r < len(col_b):
                    self.main_view.ui.tbl_match.setItem(r, 1, QTableWidgetItem(str(col_b[r])))
        
        self.main_view.ui.tbl_match.resizeRowsToContents()
        self.main_view.ui.tbl_match.blockSignals(False)
        self.on_table_item_changed(None)
    
    def get_table_data(self) -> Optional[Dict[str, Any]]:
        """Get current table data as dictionary."""
        if self.main_view.ui.tbl_match.rowCount() == 0:
            return None
            
        col_a, col_b = [], []
        for r in range(self.main_view.ui.tbl_match.rowCount()):
            item_a = self.main_view.ui.tbl_match.item(r, 0)
            col_a.append(item_a.text() if item_a else "")
            item_b = self.main_view.ui.tbl_match.item(r, 1)
            col_b.append(item_b.text() if item_b else "")
            
        return {"columnA": col_a, "columnB": col_b}
    
    def on_table_item_changed(self, item):
        """Render table content as HTML in the web view."""
        html = "<table>"
        html += "<thead><tr><th>Column A</th><th>Column B</th></tr></thead>"
        html += "<tbody>"
        
        for r in range(self.main_view.ui.tbl_match.rowCount()):
            html += "<tr>"
            for c in range(self.main_view.ui.tbl_match.columnCount()):
                cell_item = self.main_view.ui.tbl_match.item(r, c)
                cell_text = cell_item.text() if cell_item else ""
                html += f"<td>{cell_text}</td>"
            html += "</tr>"
            
        html += "</tbody></table>"
        full_html = self.main_view.html_renderer.generate_html(html)
        self.main_view.ui.we_match.setHtml(full_html)