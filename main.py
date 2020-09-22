import sys
import os.path
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtNetwork import (QHostAddress)

from pyside_material import apply_stylesheet

import log_server
import log_window
import log_filter_box
import event_dispatcher
import event_key
import connect_state

CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))
SERVER_IP = QHostAddress(QHostAddress.LocalHost)
SERVER_PORT = 10001


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # load window
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)


def BeginLogServer(server, address, port) -> None:
    print("begin listen ", (address.toString()))
    if not server.listen(address, port):
        QMessageBox.critical("logserver", "unable to start server")
        server.close()
        return


def RegisterLogEventToDispatcher(log_view: log_window.LogWindow,
                                 log_filter_utility: log_filter_box.LogFilterBox) -> None:
    # recv log
    event_dispatcher.AddEvent(event_key._RECV_LOG, log_view.AppendDataToWindow)
    # auto acroll
    event_dispatcher.AddEvent(event_key._AUTO_SCROLL_LOG, log_view.SetAutoScrollFlg)
    # change type filter
    event_dispatcher.AddEvent(event_key._TYPE_FILER_CHANGED, log_view.ChangeLogCategory)


def RegisterConnectEvent(connect_view: connect_state.ConnectState):
    event_dispatcher.AddEvent(event_key._CONNECT_CLIENT, connect_view.ConnectClient)
    event_dispatcher.AddEvent(event_key._DISCONNECT_CLIENT, connect_view.DisconnectClient)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # apply material design
    # apply_stylesheet(app, theme="dark_blue.xml")

    server = log_server.Server()
    BeginLogServer(server, SERVER_IP, SERVER_PORT)

    log_view = log_window.LogWindow(window.ui.LogView)

    log_filter_utility = log_filter_box.LogFilterBox(
        window.ui.AutoScrollBox,
        window.ui.TypeFilterBox)

    connect_view = connect_state.ConnectState(window.ui.ConnectView)

    # init event dispatcher
    event_dispatcher.StartupDispatcher()
    RegisterLogEventToDispatcher(log_view, log_filter_utility)
    RegisterConnectEvent(connect_view)
    # execute app
    window.show()
    sys.exit(app.exec_())
