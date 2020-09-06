import sys
import os.path
import log_server
import threading


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

CURRENT_PATH = os.path.dirname(os.path.join(os.path.abspath(sys.argv[0])))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, "window", "log_window.ui"))
        self.setCentralWidget(self.ui)
        self.ui.DebugLogPushButton.clicked.connect(self.clickLogPushButton)

    def clickLogPushButton(self):
        text = self.ui.DebugInputText.toPlainText()
        self.ui.LogView.append(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    server = threading.Thread(target=log_server.RunServer)
    server.start()
    window.show()
    sys.exit(app.exec_())
    server.join()