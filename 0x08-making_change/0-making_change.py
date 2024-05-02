#!/usr/bin/python3
"""0x08-making_change"""


def makeChange(coins, total):
    """
      Make Change :
      determine the fewest number of coins needed to meet a given amount total
    """

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate over each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(
                min_coins[amount], min_coins[amount - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
