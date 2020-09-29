import sys
import os.path
import json
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox, QMenu, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtNetwork import (QHostAddress)

from pyside_material import apply_stylesheet

import log_server
import log_window
import category_window
import log_filter_box
import event_dispatcher
import event_key
import connect_state
import session_data


CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))
SERVER_IP = QHostAddress(QHostAddress.LocalHost)
SERVER_PORT = 10001


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # load window
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)

        # session log
        self.session_log = session_data.SessionLog()

        # server
        self.server = log_server.Server()
        # log view
        self.log_view = log_window.LogWindow(self.ui.LogView)
        self.log_filter_utility = log_filter_box.LogFilterBox(self.ui.AutoScrollBox, self.ui.TypeFilterBox)

        # category view
        self.category_view = category_window.CategoryWindow(self.ui.CategoryView)

        # session connect state view
        self.connect_view = connect_state.ConnectState(self.ui.ConnectView)

        self.menu_file = self.ui.menuFile

        self.create_menu_bar()
        self.register_log_event_to_dispatcher()
        self.register_connect_event()

        self.begin_log_server(SERVER_IP, SERVER_PORT)

    def create_menu_bar(self) -> None:
        self.menu_file.addAction("Save as", self.save_session_log)
        self.menu_file.addAction("Load", self.load_from_file)

    def register_log_event_to_dispatcher(self) -> None:
        # recv log
        event_dispatcher.add_event(event_key.RECV_LOG, self.session_log.Add)
        event_dispatcher.add_event(event_key.RECV_LOG, self.log_view.append_data_to_window)
        event_dispatcher.add_event(event_key.RECV_LOG, self.category_view.recv_log)

        # auto acroll
        event_dispatcher.add_event(event_key.AUTO_SCROLL_LOG, self.log_view.set_auto_scroll_flg)
        # change type filter
        event_dispatcher.add_event(event_key.TYPE_FILER_CHANGED, self.log_view.change_log_type)

    def register_connect_event(self):
        event_dispatcher.add_event(event_key.CONNECT_CLIENT, self.connect_view.connect_client)
        event_dispatcher.add_event(event_key.DISCONNECT_CLIENT, self.connect_view.disconnect_client)

    def begin_log_server(self, address, port) -> None:
        print("begin listen ", (address.toString()))
        if not self.server.listen(address, port):
            QMessageBox.critical("logserver", "unable to start server")
            self.server.close()
            return

    def save_session_log(self):
        path = QFileDialog.getSaveFileName(None, "save as", "*.log")
        self.session_log.SaveToFile(path[0])

    def load_from_file(self):
        path = QFileDialog.getOpenFileName(None, "load log...", None, "*.log")
        fp = open(path[0],'r')
        log_str = json.load(fp)
        data = json.loads(log_str)
        self.session_log.SetSessionData(data)
        self.log_view.clear()
        self.log_view.show_display_log_from_log_data(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # init event dispatcher
    event_dispatcher.startup_dispatcher()

    window = MainWindow()
    # apply material design
    # apply_stylesheet(app, theme="dark_blue.xml")
    # execute app
    window.show()
    sys.exit(app.exec_())
