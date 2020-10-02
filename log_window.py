from PySide2.QtWidgets import QTextBrowser
from enum import IntEnum

_LOG_TYPE = [
    "[INFO]",
    "[WARNING]",
    "[ERROR]"
]


class LogType(IntEnum):
    ALL = -1
    INFO = 0
    WARNING = 1
    ERROR = 2


def log_filter(src: list, log_type: LogType, log_category: list):
    def filter_function(data):
        if log_type == LogType.ALL:
            if len(log_category) == 0:
                return True
            if data["category"] in log_category:
                return True
            return False

        if data["loglevel"] == LogType:
            if len(log_category) == 0:
                return True
            if data["category"] in log_category:
                return True
            return False
        return False

    return filter(filter_function, src)


class LogWindow():
    def __init__(self, window: QTextBrowser):
        self.display_data = []
        self.text_window = window
        self.auto_scroll = False
        self.log_type = LogType.ALL
        self.log_category = []
        # self.AdjustWindowSize()

    # def AdjustWindowSize(self):
    #    self.table_widget.horizontalHeader().setStretchLastSection(True)

    # @Event
    def append_data_to_window(self, log_list: list) -> None:
        filter_list = log_filter(log_list,self.log_type,self.log_category)

        for json_data in filter_list:
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
        self.log_type = type_no - 1

    def clear(self) -> None:
        self.display_data.clear()
        self.text_window.clear()
