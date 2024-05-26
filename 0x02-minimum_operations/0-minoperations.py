#!/usr/bin/python3
'''0x02-minimum_operations'''


def minOperations(n):
    '''method that calculates the fewest number of
        operations needed to result in exactly n H characters
        in the file.'''
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
