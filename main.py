import sys
import os.path
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtNetwork import (QHostAddress, QNetworkInterface)
import log_server



CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))
SERVER_IP = QHostAddress(QHostAddress.LocalHost)
SERVER_PORT = 10001

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        #load window
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)
        #self.ui.DebugLogPushButton.clicked.connect(self.clickLogPushButton)

        #init server
        self.server = log_server.Server()

    def startLogServer(self, address, port):
        print("begin listen ", (address.toString()))
        if not self.server.listen(address, port):
            QMessageBox.critical(self, "logserver", "unable to start server")
            self.close()
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.startLogServer(SERVER_IP, SERVER_PORT)
    window.show()
    sys.exit(app.exec_())