from PySide2.QtWidgets import QRadioButton

_WAIT_CONNECT_TEXT = "wait connect .."
_CONNECT_TEXT = "connect app"


class ConnectState:
    def __init__(self, button: QRadioButton):
        self.connect_state_button = button
        self.is_connected = False
        self.connect_state_button.setChecked(self.is_connected)
        self.connect_state_button.setText(_WAIT_CONNECT_TEXT)
        self.connect_state_button.clicked.connect(self.disable_user_click)

    def connect_client(self, arg):
        self.connect_state_button.setText(_CONNECT_TEXT)
        self.is_connected = True
        self.connect_state_button.setChecked(self.is_connected)


    def disconnect_client(self, arg):
        self.connect_state_button.setText(_WAIT_CONNECT_TEXT)
        self.is_connected = False
        self.connect_state_button.setChecked(self.is_connected)


    def disable_user_click(self):
        self.connect_state_button.setChecked(self.is_connected)