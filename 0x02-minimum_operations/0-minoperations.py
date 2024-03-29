#!/usr/bin/python3
'''0x02-minimum_operations'''


def minOperations(n):
    '''method that calculates the fewest number of
      operations needed to result in exactly n H characters
        in the file.'''
    ops = 0  # Counter for operations

    while n > 1:  # Iterate until n is 1 or 0
        # Find the largest power of 2 less than or equal to n
        largest_factor = largest_power_of_2(n)

        if largest_factor == 1:  # Handle odd or numbers just above
            #  a power of 2
            ops += 1  # Copy All (ensures at least one doubling)
            n //= 2  # Divide by 2 for potential doubling
            if n > 1:  # Check if further doubling is possible
                ops += 1  # Paste (if doubling happened)
            else:
                ops += n - 1  # Individual copies for remaining characters
        else:
            ops += 2  # Copy All and Paste (normal doubling)
            n //= largest_factor
    return ops


def largest_power_of_2(n):
    """Finds the largest power of 2 less than or equal to n."""

    power = 0
    while 2**power <= n:
        power += 1
    return 2**(power - 1)
