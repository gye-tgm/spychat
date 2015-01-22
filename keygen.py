"""
Securely generates a new RSA key-pair and saves public- and private-key in
separate files.

Usage: ``python keygen.py <priv key filename> <pub key filename>``
"""

from Crypto.PublicKey import RSA
import sys
from spychat.crypto import asymmetric
from spychat.crypto.constants import *


def save_key(filename, content):
    with open(filename, 'wb') as file:
        file.write(content)


if len(sys.argv) != 3:
    print("Usage: python keygen.py <priv key filename> <pub key filename>")
    sys.exit()

priv_key_file = sys.argv[1]
pub_key_file = sys.argv[2]

# generate a new RSA keypair
keypair = asymmetric.gen_key()

# extract the public and private key in a storable format
pub_key = keypair.publickey().exportKey(RSA_KEY_FORMAT)
priv_key = keypair.exportKey(RSA_KEY_FORMAT)

# save the keys in files
save_key(pub_key_file, pub_key)
save_key(priv_key_file, priv_key)
