from PySide2.QtWidgets import QCheckBox, QComboBox

import event_dispatcher
import event_key

class LogFilterBox():
    def __init__(self, checkbox: QCheckBox):
        self.auto_scroll_checkbox = checkbox
        self.auto_scroll_checkbox.stateChanged.connect(self.ClickedAutoScrollBox)
        self.is_auto_scroll = False

    def ClickedAutoScrollBox(self, state: int):
        self.is_auto_scroll = True if (state > 0) else False
        # dispatch event
        event_dispatcher.EmitEvent(event_key._AUTO_SCROLL_LOG,self.is_auto_scroll)