from PySide2.QtWidgets import QTextEdit

class LogWindow():
    def __init__(self, window_handle: QTextEdit):
        self.display_data = []
        self.window = window_handle

    def AppendDataToWindow(self, data: str):
        self.display_data.append(data)
        self.window.append(data)

    def Clear(self):
        self.display_data.clear()
        self.window.clear()
