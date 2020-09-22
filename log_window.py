from PySide2.QtWidgets import QTextEdit
import json

class LogWindow():
    def __init__(self, window: QTextEdit):
        self.display_data = []
        self.text_window = window
        #self.AdjustWindowSize()

    #def AdjustWindowSize(self):
    #    self.table_widget.horizontalHeader().setStretchLastSection(True)

    def AppendDataToWindow(self, data: str):
        #convert dict from json string
        log_dict = json.loads(data)
        format_text = "{} | {} | {} | {}".format(
            log_dict["timestamp"],
            log_dict["loglevel"],
            log_dict["category"],
            log_dict["message"])
        self.display_data.append(format_text)
        self.text_window.append(format_text)

    def Clear(self):
        self.display_data.clear()
        self.table_widget.clear()

