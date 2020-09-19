from PySide2.QtNetwork import (QTcpServer, QTcpSocket)

import event_dispatcher


class Server(QTcpServer):
    def __init__(self):
        super(Server, self).__init__()
        self.socket = QTcpSocket()

    def ReadRecvData(self):
        data = self.socket.readAll()
        utf_str = data.data().decode()
        print(utf_str)
        event_dispatcher.EmitEvent("log.recv", utf_str)

    def incomingConnection(self, socket_desc):
        if not self.socket.setSocketDescriptor(socket_desc):
            self.error.emit(self.socket.error())
            print("faild create socket")
            return
        self.socket.readyRead.connect(self.ReadRecvData)
