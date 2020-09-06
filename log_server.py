import socket

LISTEN_NUM = 5
IP         = "127.0.0.1"
PORT       = 10001

class Server:
    def __init__(self,ip: str,port: int):
        self.ip     = ip
        self.port   = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Run(self):
        self.server.bind((self.ip, self.port))
        self.server.listen(LISTEN_NUM)
        print("run server!!")
        while True:
            client, address = self.server.accept()
            print("connected!! {}",format(address))

            data = client.recv(1024)
            print(data)

            client.send("ok")
            client.close()


def RunServer():
    server = Server(IP,PORT)
    server.Run()