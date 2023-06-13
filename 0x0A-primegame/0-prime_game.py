#!/usr/bin/python3
"""Prime Game Implementation
    x: is the number of rounds
    nums: is an array of n
"""


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for i in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i, prime in enumerate(primes) if prime]
    m = 0
    for n in nums:
        m += sum(prime <= n for prime in primes)
    return "Maria" if m % 2 else "Ben"
