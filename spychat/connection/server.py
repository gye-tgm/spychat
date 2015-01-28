import socket
import pickle


class Server(object):
    def __init__(self, port=50007):
        """Initializes a new server with the given port number (default:
        50007)
        :param int port: the port to listen to
        """
        self.port = port

    def listen(self):
        """Starts listening to clients, and returns the bytes that were
        received. 

        :return bytes
        """
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
        """
        :return bytes the bytes from the client
        """
        return pickle.loads(super(PickleServer, self).listen())
