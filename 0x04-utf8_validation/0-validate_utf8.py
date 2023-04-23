#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ function that take data argument,
    checks if it has utf valid code """
    bytes_number = 0
    """byte counts initialized to 0"""
    for byte in data:
        if bytes_number == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                bytes_number = 1
            elif (byte >> 4) == 0b1110:
                bytes_number = 2
            elif (byte >> 3) == 0b11110:
                bytes_number = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_number -= 1
    return bytes_number == 0
