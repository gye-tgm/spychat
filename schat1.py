from spychat.connection.client import PickleClient
from spychat.connection.server import PickleServer

from spychat.crypto import asymmetric
from spychat.crypto import symmetric


# setup connection

client = PickleClient('localhost', 8888)
server = PickleServer(9999)
print('Started communication')

# generate a key-pair
keypair = asymmetric.gen_key()
print('Generated a new key-pair')

# send your own public key
pub_key = keypair.publickey().exportKey(asymmetric.RSA_KEY_FORMAT)
client.send(pub_key)  #: we can only send exported keys
print('Sent the public-key')

# receive and decrypt the session key
response = server.listen()
session_key = asymmetric.decrypt(response, keypair)
print('Received a session-key: %s' % session_key)
