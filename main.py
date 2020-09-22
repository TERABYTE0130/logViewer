import sys
import os.path
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtNetwork import (QHostAddress)

from pyside_material import apply_stylesheet

import log_server
import log_window
import event_dispatcher
import event_key

CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))
SERVER_IP = QHostAddress(QHostAddress.LocalHost)
SERVER_PORT = 10001


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # load window
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)


def BeginLogServer(server, address, port):
    print("begin listen ", (address.toString()))
    if not server.listen(address, port):
        QMessageBox.critical("logserver", "unable to start server")
        server.close()
        return

def RegisterLogEventToDispatcher(log_view):
    #Log受信
    event_dispatcher.AddEvent(event_key._RECV_LOG, log_view.AppendDataToWindow)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # apply materialdesign
    #apply_stylesheet(app, theme="dark_blue.xml")

    server = log_server.Server()
    BeginLogServer(server, SERVER_IP, SERVER_PORT)

    log_view = log_window.LogWindow(window.ui.LogView)

    #init event dispatcher
    event_dispatcher.StartupDispatcher()
    RegisterLogEventToDispatcher(log_view)
    #execute app
    window.show()
    sys.exit(app.exec_())
