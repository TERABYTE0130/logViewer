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
    def AppendDataToWindow(self, data: str) -> None:
        # convert dict from json string
        log_dict = json.loads(data)
        format_text = "{} | {} | {} | {}".format(
            log_dict["timestamp"],
            _LOG_TYPE[log_dict["loglevel"]],
            log_dict["category"],
            log_dict["message"])
        self.display_data.append(format_text)
        self.text_window.append(format_text)
        # if self.auto_scroll:
        #    self.ScrollToEnd()

    # @Event
    def SetAutoScrollFlg(self, flg: bool):
        self.auto_scroll = flg

    def ScrollToEnd(self) -> None:
        scroll = self.text_window.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def ChangeLogCategory(self, type: int):
        print(type)

    def Clear(self) -> None:
        self.display_data.clear()
        self.table_widget.clear()
