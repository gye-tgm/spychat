"""
This module contains easy to use functions for asymmetric encryption using
the `RSA`-algorithm.
"""

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


# encryption parameters used in this file
RSA_MODE = PKCS1_OAEP  #: RSA padding mode
RSA_E = 65537  #: RSA public exponent
RSA_KEY_LEN_BITS = 2048  #: RSA key-length in bits
RSA_KEY_FORMAT = 'PEM'  #: RSA key-export format


def encrypt(data, public_key):
    """
    Encrypts the given data with the given public key

    :param bytearray() data:   the data to encrypt
    :param _RSAobj public_key: the public key to use for encryption
    :return bytes():           the resulting ciphertext with the used IV
                               prepended
    """

    rsa = RSA_MODE.new(public_key)
    return rsa.encrypt(data)

def decrypt(data, private_key):
    """
    Decrypts the given data using the given private key

    :param bytes() data:        the data to decrypt
    :param _RSAobj private_key: the private key to use for decryption
    :return bytes():            the resulting plaintext
    """

    rsa = RSA_MODE.new(private_key)
    return rsa.decrypt(data)

def gen_key():
    """
    Generates a new random key to use for asymmetric encryption

    :return _RSAobj: the randomly generated key
    """

    return RSA.generate(RSA_KEY_LEN_BITS, e=RSA_E)
