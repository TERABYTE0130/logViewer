from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
import json

class LogWindow():
    def __init__(self, table_widget: QTableWidget):
        self.display_data = []
        print(table_widget.width())
        self.table_widget = table_widget
        self.AdjustWindowSize()

    def AdjustWindowSize(self):
        self.table_widget.horizontalHeader().setStretchLastSection(True)

    def AppendDataToWindow(self, data: str):
        #convert dict from json string
        log_dict = json.loads(data)
        insert = QTableWidgetItem()
        i
        print(log_dict)

    def Clear(self):
        self.display_data.clear()
        self.table_widget.clear()

