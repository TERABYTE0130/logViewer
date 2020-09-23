from PySide2.QtWidgets import QTextEdit
import json

_LOG_TYPE = [
    "[  INFO  ]",
    "[  WARNING  ]",
    "[  ERROR  ]"
]

class LogWindow():
    def __init__(self, window: QTextEdit):
        self.display_data = []
        self.text_window = window
        self.auto_scroll = False
        # self.AdjustWindowSize()

    # def AdjustWindowSize(self):
    #    self.table_widget.horizontalHeader().setStretchLastSection(True)

    # @Event
    def AppendDataToWindow(self, json_data) -> None:
        # convert dict from json string

        format_text = "{} | {} | {} | {}".format(
            json_data["timestamp"],
            _LOG_TYPE[json_data["loglevel"]],
            json_data["category"],
            json_data["message"])
        self.display_data.append(format_text)
        self.text_window.append(format_text)
        # if self.auto_scroll:
        #    self.ScrollToEnd()

    # @Event
    def SetAutoScrollFlg(self, flg: bool)->None:
        self.auto_scroll = flg

    def ScrollToEnd(self) -> None:
        scroll = self.text_window.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def ChangeLogType(self, type: int)->None:
        print(type)

    def Clear(self) -> None:
        self.display_data.clear()
        self.table_widget.clear()
