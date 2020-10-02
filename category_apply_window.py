from PySide2.QtWidgets import QListWidget, QListWidgetItem
import PySide2.QtCore
import event_dispatcher
import event_key
import copy

class CategoryApplyWindow:
    def __init__(self, window: QListWidget):
        self.list_window = window
        self.current_filter = []
        self.list_window.itemDoubleClicked.connect(self.delete)

    def add(self, category: str):
        self.current_filter.append(category)
        self.list_window.addItem(category)

    def delete(self, category_item):
        category_text = category_item.text()
        self.current_filter.remove(category_text)
        remove_list = self.list_window.findItems(category_text, PySide2.QtCore.Qt.MatchFixedString)
        for item in remove_list:
            row = self.list_window.row(item)
            self.list_window.takeItem(row)
        # dispatch
        dispatch_data = copy.deepcopy(self.current_filter)
        event_dispatcher.emit_event(event_key.SEND_CATEGORY_FILTER, dispatch_data)
        event_dispatcher.emit_event(event_key.LOG_FILTERING, None)

    def clear(self):
        self.current_filter.clear()
        self.list_window.clear()

    def is_contain(self, category: str) -> bool:
        return True if category in self.current_filter else False

    # @Event
    def receive_add_filter_event(self, category):
        if not self.is_contain(category):
            self.add(category)
            # dispatch
            dispatch_data = copy.deepcopy(self.current_filter)
            event_dispatcher.emit_event(event_key.SEND_CATEGORY_FILTER, dispatch_data)
            event_dispatcher.emit_event(event_key.LOG_FILTERING, None)
