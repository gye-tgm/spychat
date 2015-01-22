import socket

# Important
# https://docs.python.org/2/library/pickle.html#pickle.HIGHEST_PROTOCOL
import pickle


class Client(object):
    def __init__(self, host, port=50007):
        """
        Initializes a client with the given host and port address, which are
        the network informations of the other communication partner.

        :param str host: the hostname
        :param int port: the port address
        :return:
        """
        self.host = host
        self.port = port

    def send(self, obj):
        """
        Sends an object to the communication partner (server) as a serialized
        object, converted with pickle.

        :param bytes obj: the object to send as bytes
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            try:
                s.connect((self.host, self.port))
                s.send(obj)
            except ConnectionRefusedError:
                print('Unable to connect to %s with port %s' % (self.host,
                                                                self.port))
            except:
                raise


class PickleClient(Client):
    def send(self, obj):
        super(PickleClient, self).send(pickle.dumps(obj))

# Test code
client = PickleClient('localhost')
client.send('a' * 10000)