from PySide2.QtCore import (Signal, QByteArray, QDataStream, QIODevice, QThread, Qt)
from PySide2.QtNetwork import (QHostAddress, QNetworkInterface, QTcpServer, QTcpSocket)


class LogThread(QThread):
    error = Signal(QTcpSocket.SocketError)

    def __init__(self, socket_desc, parent):
        super(LogThread,self).__init__(parent)
        self.socket_desc = socket_desc

    def returnResponce(msg:str)


    def run(self):
        tcp_socket = QTcpSocket()
        #socket生成
        if not tcp_socket.setSocketDescriptor(self.socket_desc):
            self.error.emit(tcp_socket.error())
            print("faild create socket")
            return
        print("connected!!")


class Server(QTcpServer):
    def incomingConnection(self, socket_desc):
        print("connect begin")
        thread = LogThread(socket_desc, self)
        # 終了をトリガーして破棄する
        thread.finished.connect(thread.deleteLater)
        thread.start()
