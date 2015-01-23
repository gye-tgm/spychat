"""
The `Alice` test-script for sPyChat

.. note::
    Must be started after `bob.py`!
"""

from Crypto.Hash import MD5

from spychat.connection.client import PickleClient
from spychat.connection.server import PickleServer

from spychat.crypto import asymmetric
from spychat.crypto import symmetric

from spychat.utils import to_hex


# setup connection
client = PickleClient('localhost', 8888)
server = PickleServer(9999)

# generate a key-pair
keypair = asymmetric.gen_key()
print('Generated a new key-pair')

# send your own public key
pub_key = keypair.publickey().exportKey(asymmetric.RSA_KEY_FORMAT)
client.send(pub_key)  #: we can only send exported keys
print('Sending public-key with fingerprint: %s' % MD5.new(pub_key).hexdigest())

# receive and decrypt the session key
response = server.listen()
session_key = asymmetric.decrypt(response, keypair)
print('Received session-key: %s' % to_hex(session_key))

# send an encrypted message
m = 'This is an encrypted message!'
m_enc = symmetric.encrypt(m, session_key)
client.send(m_enc)
print('Sending encrypted message: %s' % to_hex(m_enc))
