from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from spychat.crypto import symmetric
from spychat.crypto.constants import *


def encrypt(data, public_key):
    """
    Encrypts the given data with the given public key

    :param bytearray() data:       the data to encrypt
    :param bytearray() public_key: the public key to use for encryption
    :return bytearray():           the resulting ciphertext with the used IV
                                   prepended
    """

    rsa = PKCS1_OAEP.new(public_key)
    return rsa.encrypt(data)

def decrypt(data, private_key):
    """
    Decrypts the given data using the given private

    :param bytearray() data:        the data to decrypt
    :param bytearray() private_key: the private key to use for decryption
    :return bytearray():            the resulting plaintext
    """

    rsa = PKCS1_OAEP.new(private_key)
    return rsa.decrypt(data)

def gen_key():
    """
    Generates a new random key to use for asymmetric encryption

    :return bytearray(): the randomly generated key
    """

    return RSA.generate(RSA_KEY_LEN_BITS, e=RSA_E)
