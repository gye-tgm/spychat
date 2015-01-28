"""
The `Bob` test-script for sPyChat

.. note::
    Must be started before `alice.py`!
"""

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA

from spychat.connection.client import PickleClient
from spychat.connection.server import PickleServer

from spychat.crypto import asymmetric
from spychat.crypto import symmetric

from spychat.utils import to_hex


# setup connection
server = PickleServer(8888)
print('Waiting for key-exchange request ...')

# receive a public key
other_pub_key = server.listen()
print('Received a public-key with fingerprint:',
      MD5.new(other_pub_key).hexdigest())
other_pub_key = RSA.importKey(other_pub_key)  #: keys are sent exported

# generate a session key, encrypt it with the public-key and send it back
session_key = symmetric.gen_key()
print('Generated a new session-key:', to_hex(session_key))
enc_session_key = asymmetric.encrypt(session_key, other_pub_key)

client = PickleClient('localhost', 9999)
client.send(enc_session_key)
print('Sending session-key')

# receive an unencrypted message
m = server.listen()
print('Received unencrypted message:', m)

# receive an encrypted message
m_enc = server.listen()
print('Received encrypted message:', to_hex(m_enc))
m = symmetric.decrypt(m_enc, session_key)
print('Decrypted message:',  m.decode('ASCII'))
