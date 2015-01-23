from Crypto.PublicKey import RSA
from spychat.connection.client import PickleClient
from spychat.connection.server import PickleServer

from spychat.crypto import asymmetric
from spychat.crypto import symmetric


# setup connection
server = PickleServer(8888)
print('Started communication')

# receive the other's public key
other_pub_key = RSA.importKey(server.listen()) #: only exported keys are sent
print('Received a public-key')

# generate a session key, encrypt it with the public-key and send it back
session_key = symmetric.gen_key()
enc_session_key = asymmetric.encrypt(session_key, other_pub_key)

client = PickleClient('localhost', 9999)
client.send(enc_session_key)
print('Send a newly generated session-key')
