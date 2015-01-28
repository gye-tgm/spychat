"""
This module contains some helper functions
"""

import binascii


def to_hex(bytes):
    """
    Converts the given bytes to a hex-encoded String

    :param bytes() bytes: the bytes to convert
    :return String: the hex-encoded String
    """

    return binascii.hexlify(bytes).decode('ASCII')
