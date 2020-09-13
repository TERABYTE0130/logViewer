from PySide2.QtCore import (Signal, QByteArray, QDataStream, QIODevice, QThread, QByteArray,
                            QDataStream, QIODevice, Qt)
from PySide2.QtNetwork import (QHostAddress, QNetworkInterface, QTcpServer, QTcpSocket)


class LogThread(QThread):
    error = Signal(QTcpSocket.SocketError)

    def __init__(self, socket_desc, parent):
        super(LogThread,self).__init__(parent)
        self.socket_desc = socket_desc

    def createResponce(self, msg: str):
        write_block = QByteArray()
        output_buf = QDataStream(write_block, QIODevice.WriteOnly)
        output_buf.setVersion(QDataStream.Qt_5_15)
        #output_buf.setVersion(QDataStream.Qt_4_0)
        output_buf.writeUInt16(0)
        output_buf.writeQString(msg)
        output_buf.device().seek(0)
        output_buf.writeUInt16(write_block.size() - 2)
        return write_block

    def run(self):
        tcp_socket = QTcpSocket()
        #socket生成と
        if not tcp_socket.setSocketDescriptor(self.socket_desc):
            self.error.emit(tcp_socket.error())
            print("faild create socket")
            return
        print("connected!!")
        connect_responce = self.createResponce("connect log server!!")
        tcp_socket.write(connect_responce)

        tcp_socket.disconnectFromHost()
        tcp_socket.waitForDisconnected()

class Server(QTcpServer):
    def incomingConnection(self, socket_desc):
        print("connect begin")
        thread = LogThread(socket_desc, self)
        # 終了をトリガーして破棄する
        thread.finished.connect(thread.deleteLater)
        thread.start()
