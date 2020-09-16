from PySide2.QtCore import (QObject, Signal, QByteArray, QDataStream, QIODevice, QThread, QByteArray,
                            QDataStream, QIODevice, Qt)
from PySide2.QtNetwork import (QHostAddress, QNetworkInterface, QTcpServer, QTcpSocket)


class StringSignal(QObject):
    logging_signal = Signal(str)


class LogThread(QThread):
    error = Signal(QTcpSocket.SocketError)

    def __init__(self, socket_desc, signal, parent):
        super(LogThread, self).__init__(parent)
        self.socket_desc = socket_desc
        self.signal = signal
        self.log_signal = StringSignal()
        self.is_connect_client = True

    def createResponce(self, msg: str):
        write_block = QByteArray()
        output_buf = QDataStream(write_block, QIODevice.WriteOnly)
        output_buf.setVersion(QDataStream.Qt_5_15)
        output_buf.writeUInt16(0)
        output_buf.writeQString(msg)
        output_buf.device().seek(0)
        output_buf.writeUInt16(write_block.size() - 2)
        return write_block

    def sendToClient(self, socket: QTcpSocket, buf):
        socket.write(buf)

    def setLogSlot(self, slot_func):
        self.log_signal.logging_signal[str].connect(slot_func)

    def run(self):
        tcp_socket = QTcpSocket()
        # socket生成
        if not tcp_socket.setSocketDescriptor(self.socket_desc):
            self.error.emit(tcp_socket.error())
            print("faild create socket")
            return
        connect_response = self.createResponce("test")
        self.sendToClient(tcp_socket,connect_response)
        while self.is_connect_client:
            while tcp_socket.bytesAvailable() < 2:
                print("wait next log ...")
                if not tcp_socket.waitForReadyRead(-1):
                    print("failed recv")
                print("loop... ")

            read_buf = QDataStream(tcp_socket)
            block_size = read_buf.readUInt16()
            print(block_size)
            while tcp_socket.bytesAvailable() < block_size:
                if not tcp_socket.waitForReadyRead(-1):
                    print(tcp_socket.errorString())

            recv_log = read_buf.readQString()
            print("success recv log")
            print(recv_log)

        connect_responce = self.createResponce("connect log server!!")
        tcp_socket.write(connect_responce)
        self.log_signal.logging_signal[str].emit("send message")
        tcp_socket.disconnectFromHost()
        tcp_socket.waitForDisconnected()


class Server(QTcpServer):
    def __init__(self, log_slot):
        super(Server, self).__init__()
        self.log_slot = log_slot

    def incomingConnection(self, socket_desc):
        thread = LogThread(socket_desc, self.log_slot, self)
        thread.setLogSlot(self.log_slot)
        # 終了をトリガーして破棄する
        thread.finished.connect(thread.deleteLater)
        thread.start()
       
