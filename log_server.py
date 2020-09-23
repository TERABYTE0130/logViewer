from PySide2.QtNetwork import (QTcpServer, QTcpSocket)

import event_dispatcher
import event_key
import json

class Server(QTcpServer):
    def __init__(self):
        super(Server, self).__init__()
        self.socket = QTcpSocket()
        self.socket.readyRead.connect(self.ReadRecvData)
        self.socket.disconnected.connect(self.DisconnectSocket)

    def ReadRecvData(self):
        data = self.socket.readAll()
        utf_str = data.data().decode()
        #format to json
        json_data = json.loads(utf_str)
        event_dispatcher.EmitEvent(event_key.RECV_LOG, json_data)

    def DisconnectSocket(self):
        event_dispatcher.EmitEvent(event_key.DISCONNECT_CLIENT, "null")

    def incomingConnection(self, socket_desc):
        if not self.socket.setSocketDescriptor(socket_desc):
            self.error.emit(self.socket.error())
            print("faild create socket")
            return
        event_dispatcher.EmitEvent(event_key.CONNECT_CLIENT, "null")
