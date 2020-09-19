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

CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))
SERVER_IP = QHostAddress(QHostAddress.LocalHost)
SERVER_PORT = 10001


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # load window
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)

def TestEvent(data):
    print(data)


def BeginLogServer(server, address, port):
    print("begin listen ", (address.toString()))
    if not server.listen(address, port):
        QMessageBox.critical("logserver", "unable to start server")
        server.close()
        return



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # apply materialdesign
    apply_stylesheet(app, theme="dark_teal.xml")

    server = log_server.Server()
    BeginLogServer(server, SERVER_IP, SERVER_PORT)

    log_view = log_window.LogWindow(window.ui.LogView)

    event_dispatcher.StartupDispatcher()

    event_dispatcher.AddEvent("log.recv",log_view.AppendDataToWindow)
    window.show()
    sys.exit(app.exec_())

