from PySide2.QtWidgets import QCheckBox, QComboBox

import event_dispatcher
import event_key


class LogFilterBox():
    def __init__(self, checkbox: QCheckBox, combo_box: QComboBox):
        self.auto_scroll_checkbox = checkbox
        self.auto_scroll_checkbox.stateChanged.connect(self.ClickedAutoScrollBox)
        self.is_auto_scroll = False

        self.type_filter = combo_box
        self.current_filter = 0
        self.type_filter.currentIndexChanged.connect(self.ChangeTypeFilter)

    def ChangeTypeFilter(self, state: int):
        self.current_filter = state
        event_dispatcher.EmitEvent(event_key.TYPE_FILER_CHANGED, self.current_filter)

    def ClickedAutoScrollBox(self, state: int):
        self.is_auto_scroll = True if (state > 0) else False
        # dispatch event
        event_dispatcher.EmitEvent(event_key.AUTO_SCROLL_LOG, self.is_auto_scroll)
