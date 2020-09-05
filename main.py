import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

class UISample(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(UISample, self).__init__(parent)
        self.resize(400,300)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UISample()
    window.show()
    sys.exit(app.exec_())