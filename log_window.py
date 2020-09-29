from PySide2.QtWidgets import QTextBrowser
import json

_LOG_TYPE = [
    "[INFO]",
    "[WARNING]",
    "[ERROR]"
]


class LogWindow():
    def __init__(self, window: QTextBrowser):
        self.display_data = []
        self.text_window = window
        self.auto_scroll = False
        # self.AdjustWindowSize()

    # def AdjustWindowSize(self):
    #    self.table_widget.horizontalHeader().setStretchLastSection(True)

    # @Event
    def append_data_to_window(self, json_data) -> None:
        # convert dict from json string

        format_text = "{}  {}  [ {} ]  {}".format(
            json_data["timestamp"],
            _LOG_TYPE[json_data["loglevel"]],
            json_data["category"],
            json_data["message"])
        self.display_data.append(format_text)
        self.text_window.append(format_text)
        # if self.auto_scroll:
        #    self.scroll_to_end()

    # @Event
    def set_auto_scroll_flg(self, flg: bool) -> None:
        self.auto_scroll = flg

    def scroll_to_end(self) -> None:
        scroll = self.text_window.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def change_log_type(self, type_no: int) -> None:
        print(type_no)

    def clear(self) -> None:
        self.display_data.clear()
        self.text_window.clear()

    def show_display_log_from_log_data(self, log_data: list):
        for log in log_data:
            self.append_data_to_window(log)