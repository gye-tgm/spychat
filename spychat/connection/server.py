__author__ = 'gary'

import socket


class Server:
    def __init__(self, port=50007):
        self.port = port

    def listen(self):
        global data
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen(1)
        conn, addr = s.accept()

        print('Connected by', addr)

        data = conn.recv(2048)

        conn.close()
        return data

# Test code
server = Server()
print(server.listen())
