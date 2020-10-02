from PySide2.QtWidgets import QListWidget, QListWidgetItem
import PySide2.QtCore
import event_dispatcher
import event_key


class CategoryApplyWindow:
    def __init__(self, window: QListWidget):
        self.list_window = window
        self.current_filter = []
        event_dispatcher.add_event(event_key.ADD_LOG_CATEGORY_FILTER, self.receive_add_filter)
        self.list_window.itemDoubleClicked.connect(self.delete)

    def add(self, category: str):
        self.current_filter.append(category)
        self.list_window.addItem(category)

    def delete(self, category_item):
        print(self.current_filter)
        category_text = category_item.text()
        self.current_filter.remove(category_text)
        print(self.current_filter)
        remove_list = self.list_window.findItems(category_text, PySide2.QtCore.Qt.MatchFixedString)
        for item in remove_list:
            row = self.list_window.row(item)
            self.list_window.takeItem(row)

    def clear(self):
        self.current_filter.clear()
        self.list_window.clear()

    def is_contain(self, category: str) -> bool:
        return True if category in self.current_filter else False

    def receive_add_filter(self, category):
        if not self.is_contain(category):
            self.add(category)
            # dispatch
