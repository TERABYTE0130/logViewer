from PySide2.QtWidgets import QTextBrowser, QCheckBox
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
    def filter_type(data):
        if log_type == LogType.ALL:
            return True
        return True if log_type == data["loglevel"] else False

    def filter_category(data):
        if len(log_category) == 0:
            return True
        return True if data["category"] in log_category else False

    def filter_func(data):
        if filter_type(data):
            if filter_category(data):
                return True
        return False

    return filter(filter_func, src)


def filter_text(format_text: str, search_text: str):
    if len(search_text) == 0:
        return True
    if search_text in format_text:
        return True
    return False


class LogWindow:
    def __init__(self, window: QTextBrowser,checkbox: QCheckBox):
        self.text_window = window
        self.log_type = LogType.ALL
        self.log_category = []
        self.text_filter = ""

        self.auto_scroll_checkbox = checkbox
        self.auto_scroll_checkbox.stateChanged.connect(self.clicked_auto_scroll_box)
        self.is_auto_scroll = True
        # self.AdjustWindowSize()

    # def AdjustWindowSize(self):
    #    self.table_widget.horizontalHeader().setStretchLastSection(True)

    # @Event
    def append_data_to_window(self, log_list: list) -> None:
        filtering_list = log_filter(log_list, self.log_type, self.log_category)
        for json_data in filtering_list:
            format_text = "{}  {}  [ {} ]  {}".format(
                json_data["timestamp"],
                _LOG_TYPE[json_data["loglevel"]],
                json_data["category"],
                json_data["message"])
            # textのフィルタリングのみformat後に行う
            if filter_text(format_text, self.text_filter):
                self.text_window.append(format_text)

        # if self.is_auto_scroll:
        #    self.scroll_to_end()

    # @Event
    def set_log_type(self, type_no: int) -> None:
        self.log_type = type_no - 1

    # @Event
    def set_category_filter(self, category_list: list):
        self.log_category = category_list

    # @Event
    def set_text_filter(self, text: str):
        self.text_filter = text

    def scroll_to_end(self) -> None:
        scroll = self.text_window.verticalScrollBar()
        scroll.setValue(scroll.maximum())

    def clear(self) -> None:
        self.text_window.clear()

    def clicked_auto_scroll_box(self, state: int):
        self.is_auto_scroll = True if (state > 0) else False

