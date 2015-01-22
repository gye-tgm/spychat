from Crypto import Random
from spychat.crypto.constants import *


# PKCS5 padding implementation
def pad(data):
    pad_nr = AES_BLOCK_SIZE - (len(data) % AES_BLOCK_SIZE)
    return data + (chr(pad_nr) * pad_nr)
def unpad(data):
    return data[:len(data) - data[-1]]


def encrypt(data, key, iv=None):
    """
    Encrypts the given data with the given key and iv.

    :param String data:     the data to encrypt
    :param bytearray() key: the key to use for encryption
    :param bytearray() iv:  the IV to use for encryption; if None a new random
                            one will be generated
    :return bytearray():    the resulting ciphertext with the used IV prepended
    """

    if iv is None:
        iv = Random.new().read(AES_BLOCK_SIZE)

    aes = AES.new(key, AES_MODE, iv)

    return iv + aes.encrypt(pad(data))

def decrypt(data, key, iv=None):
    """
    Decrypts the given data using the given key and iv.

    :param String data:     the data to decrypt
    :param bytearray() key: the key to use for decryption
    :param bytearray() iv:  the IV to use for decryption; if None the IV is
                            assumed to be prepended to the ciphertext
    :return bytearray():    the resulting plaintext
    """

    if iv is None:
        iv = data[:AES_BLOCK_SIZE]
        data = data[AES_BLOCK_SIZE:]

    aes = AES.new(key, AES_MODE, iv)

    return unpad(aes.decrypt(data))
