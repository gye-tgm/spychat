import socket

__author__ = 'gary'


class Client:
    def __init__(self, host, port=50007):
        self.host = host
        self.port = port

    def send(self, obj):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.host, self.port))
        except:
            print('Unable to connect to %s with port %s' % self.host,
                  self.port)
        s.send(obj)
        s.close()

# Test code
client = Client('localhost')
client.send(b'abc')