#!/usr/bin/python3
'''0x04-utf8_validation'''


def validUTF8(data):
    """
    This function checks if the given data represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing the bytes of the data.

    Returns:
        True if the data is a valid UTF-8 encoding, False otherwise.
    """
    count_ones = 0
    for byte in data:
        # Extract the 8 least significant bits
        byte = byte & 0b11111111

        # Check for valid ASCII characters (first byte)
        if count_ones == 0:
            if byte <= 0x7F:
                continue
            elif byte <= 0xDF:
                count_ones = 1
            elif byte <= 0xEF:
                count_ones = 2
            elif byte <= 0xF7:
                count_ones = 3
            else:
                return False
        # Check for continuation bytes (subsequent bytes)
        elif 0 <= count_ones <= 3:
            if byte >= 0x80 and byte <= 0xBF:
                count_ones -= 1
            else:
                return False
        else:
            return False
    # Check if all continuation bytes were consumed
    return count_ones == 0
