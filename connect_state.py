from PySide2.QtWidgets import QLabel

_WAIT_CONNECT_TEXT = "wait connect .."
_CONNECT_TEXT = "connect client!"


class ConnectState():
    def __init__(self, label: QLabel):
        self.current_text = _WAIT_CONNECT_TEXT
        self.connect_label = label
        self.connect_label.setText(self.current_text)

    def ConnectClient(self, arg):
        self.current_text = _CONNECT_TEXT
        self.connect_label.setText(self.current_text)

    def DisconnectClient(self, arg):
        self.current_text = _WAIT_CONNECT_TEXT
        self.connect_label.setText(self.current_text)
