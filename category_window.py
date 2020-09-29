from PySide2 import QtWidgets
from PySide2.QtWidgets import QListWidget,QListWidgetItem

import event_dispatcher
import event_key


class CategoryWindow():
    def __init__(self, window: QListWidget):
        self.listwindow = window
        self.listwindow.itemDoubleClicked.connect(self.SelectCategory)
        self.category_list = []

    def recv_log(self, log):
        if not self.IsContain(log["category"]):
            self.AddCategory(log["category"])

        # self.category_list.append(log)

    def AddCategory(self, data):
        self.category_list.append(data)
        self.listwindow.addItem(data)

    def IsContain(self, category: str) -> bool:
        return True if category in self.category_list else False

    def Clear(self):
        self.category_list.clear()
        self.listwindow.clear()

    def SelectCategory(self, item: QListWidgetItem):
        select_category = item.text()
        # event_dispatcher.EmitEvent(event_key.SELECT_LOG_CATEGORY)
