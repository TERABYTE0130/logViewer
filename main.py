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

        # session connect state view
        self.connect_view = connect_state.ConnectState(self.ui.ConnectView)

        self.menu_file = self.ui.menuFile

        self.CreateMenuBar()
        self.RegisterLogEventToDispatcher()
        self.RegisterConnectEvent()

        self.BeginLogServer(SERVER_IP, SERVER_PORT)

    def CreateMenuBar(self) -> None:
        self.menu_file.addAction("Save as", self.SaveSessionLog)
        self.menu_file.addAction("Load", self.LoadFromFile)

    def RegisterLogEventToDispatcher(self) -> None:
        # recv log
        event_dispatcher.AddEvent(event_key.RECV_LOG, self.session_log.Add)
        event_dispatcher.AddEvent(event_key.RECV_LOG, self.log_view.AppendDataToWindow)
        # auto acroll
        event_dispatcher.AddEvent(event_key.AUTO_SCROLL_LOG, self.log_view.SetAutoScrollFlg)
        # change type filter
        event_dispatcher.AddEvent(event_key.TYPE_FILER_CHANGED, self.log_view.ChangeLogType)

    def RegisterConnectEvent(self):
        event_dispatcher.AddEvent(event_key.CONNECT_CLIENT, self.connect_view.ConnectClient)
        event_dispatcher.AddEvent(event_key.DISCONNECT_CLIENT, self.connect_view.DisconnectClient)

    def BeginLogServer(self, address, port) -> None:
        print("begin listen ", (address.toString()))
        if not self.server.listen(address, port):
            QMessageBox.critical("logserver", "unable to start server")
            self.server.close()
            return

    def SaveSessionLog(self):
        path = QFileDialog.getSaveFileName(None, "save as", "*.log")
        self.session_log.SaveToFile(path[0])

    def LoadFromFile(self):
        path = QFileDialog.getOpenFileName(None, "load log...", None, "*.log")
        fp = open(path[0],'r')
        log_str = json.load(fp)
        data = json.loads(log_str)
        self.session_log.SetSessionData(data)
        self.log_view.Clear()
        self.log_view.ShowDisplayLogFromLogData(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # init event dispatcher
    event_dispatcher.StartupDispatcher()

    window = MainWindow()
    # apply material design
    # apply_stylesheet(app, theme="dark_blue.xml")
    # execute app
    window.show()
    sys.exit(app.exec_())
