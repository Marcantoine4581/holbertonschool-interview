#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    '''method that determines if a given data set
    represents a valid UTF-8 encoding.
    Args:
        data (list[int]): data set
    Returns:
        True if data is a valid UTF-8 encoding,
        else return False
    '''
    for i in data:
        if i > 255:
            return False

    return True
