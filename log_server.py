from PySide2.QtCore import (QObject, Signal, QThread, QByteArray, QDataStream, QIODevice)
from PySide2.QtNetwork import (QHostAddress, QNetworkInterface, QTcpServer, QTcpSocket)

class Server(QTcpServer):
    def __init__(self):
        super(Server, self).__init__()
        self.socket = QTcpSocket()

    def ReadBuf(self):
        data = self.socket.readAll()
        utf_str = data.data().decode()
        print(utf_str)

    def incomingConnection(self, socket_desc):
        if not self.socket.setSocketDescriptor(socket_desc):
            self.error.emit(self.socket.error())
            print("faild create socket")
            return
        self.socket.readyRead.connect(self.ReadBuf)
