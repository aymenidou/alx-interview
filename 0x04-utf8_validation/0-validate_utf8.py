#!/usr/bin/python3
'''0x04-utf8_validation'''


def validUTF8(data):
    '''validUTF8
    method that determines if a given data
      set represents a valid UTF-8 encoding.
    '''
    count_ones = 0
    for num in data:
        # Extract the 8 least significant bits
        num = num & 0xFF
        # If the first bit is 1
        if num & 0x80:
            # Must follow 1 to 4 bytes with the format 10xxxxxx
            if count_ones == 0:
                count_ones += 1
                if num & 0x40 == 0:
                    return False
                elif num & 0x20 == 0:
                    count_ones = 3
                elif num & 0x10 == 0:
                    count_ones = 4
                else:
                    count_ones = 2
            else:
                # Subsequent bytes must start with 10
                if not (num & 0xC0 == 0x80):
                    return False
                count_ones -= 1
        # Byte does not start with 1
        else:
            # If expecting more bytes, return False
            if count_ones > 0:
                return False
            count_ones = 0
    # If expecting more bytes at the end, return False
    return count_ones == 0
