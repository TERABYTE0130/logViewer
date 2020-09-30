from PySide2.QtWidgets import QListWidget, QListWidgetItem

import event_dispatcher
import event_key


class CategoryWindow():
    def __init__(self, window: QListWidget):
        self.list_window = window
        self.list_window.itemDoubleClicked.connect(self.select_category)
        self.category_list = []

    def recv_log(self, log):
        if not self.is_contain(log["category"]):
            self.add_category(log["category"])

        # self.category_list.append(log)

    def add_category(self, data):
        self.category_list.append(data)
        self.list_window.addItem(data)

    def is_contain(self, category: str) -> bool:
        return True if category in self.category_list else False

    def clear(self):
        self.category_list.clear()
        self.list_window.clear()

    def select_category(self, item: QListWidgetItem):
        select_category = item.text()
        # event_dispatcher.EmitEvent(event_key.SELECT_LOG_CATEGORY)
