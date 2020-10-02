from PySide2.QtWidgets import QCheckBox, QComboBox

import event_dispatcher
import event_key


class LogFilterBox():
    def __init__(self, checkbox: QCheckBox, combo_box: QComboBox):
        self.auto_scroll_checkbox = checkbox
        self.auto_scroll_checkbox.stateChanged.connect(self.clicked_auto_scroll_box)
        self.is_auto_scroll = True

        self.type_filter = combo_box
        self.current_filter = 0
        self.type_filter.currentIndexChanged.connect(self.change_type_filter)

    def change_type_filter(self, state: int):
        self.current_filter = state
        event_dispatcher.EmitEvent(event_key.TYPE_FILER_CHANGED, self.current_filter)
        event_dispatcher.EmitEvent(event_key.LOG_FILTERING, None)

    def clicked_auto_scroll_box(self, state: int):
        self.is_auto_scroll = True if (state > 0) else False
        # dispatch event
        event_dispatcher.EmitEvent(event_key.AUTO_SCROLL_LOG, self.is_auto_scroll)
