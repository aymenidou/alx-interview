#!/usr/bin/python3
''''''
def sieve(n):
    ''''''
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [i for i in range(n + 1) if is_prime[i]]


def isWinner(x, nums):
    ''''''
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    def count_primes_up_to(n):
        return sum(1 for p in primes if p <= n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example usage:
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
