#!/usr/bin/python3
""" method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ function that take data argument,
    checks if it has utf valid code """
    byte_num = 0
    for byte in data:
        if byte_num == 0:
            if (byte & 0b10000000) == 0b00000000:
                byte_num = 0
            elif (byte & 0b11100000) == 0b11000000:
                byte_num = 1
            elif (byte & 0b11110000) == 0b11100000:
                byte_num = 2
            elif (byte & 0b11111000) == 0b11110000:
                byte_num = 3
            else:
                return False

        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            byte_num -= 1
    return byte_num == 0
