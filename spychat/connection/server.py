import socket
import pickle
from spychat.crypto import symmetric


class Server(object):
    def __init__(self, port=50007):
        self.port = port

    def listen(self):
        global data
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen(1)

        conn, addr = s.accept()

        print('Connection established with', addr)

        buf = bytes()

        while True:
            data = conn.recv(2048)

            if data:
                buf += data
            else:
                break
        conn.close()
        return buf


class PickleServer(Server):
    def listen(self):
        return pickle.loads(super(PickleServer, self).listen())
