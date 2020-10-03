from PySide2.QtWidgets import  QComboBox

from src import event_key, event_dispatcher


class TypeFilter:
    def __init__(self, combo_box: QComboBox):
        self.type_filter = combo_box
        self.current_filter = 0
        self.type_filter.currentIndexChanged.connect(self.change_type_filter)

    def change_type_filter(self, state: int):
        self.current_filter = state
        event_dispatcher.emit_event(event_key.SEND_TYPE_FILTER, self.current_filter)
        event_dispatcher.emit_event(event_key.LOG_FILTERING, None)
