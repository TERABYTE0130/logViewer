from PySide2.QtWidgets import QLineEdit

from src import event_key, event_dispatcher


class text_filter_edit:
    def __init__(self, text_edit: QLineEdit):
        self.text_edit = text_edit
        self.text_edit.editingFinished.connect(self.set_filter_text)

    def set_filter_text(self):
        text = self.text_edit.text()
        event_dispatcher.emit_event(event_key.SEND_TEXT_FILTER, text)
        event_dispatcher.emit_event(event_key.LOG_FILTERING, None)
