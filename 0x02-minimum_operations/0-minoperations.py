#!/usr/bin/python3
"""
a method that calculates the fewest number of operations
needed to get a desired result.

"""


def check_prime(n):
    """ checks if number is a prime number """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def num_factors(n):
    """ function that finds list of prime factors of a number taking args n:
    return list of int.
     """
    factors = []
    for i in range(2, n//2):
        while n % i == 0:
            factors.append(i)
            n = n // i
        if (i >= n):
            break

    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    function that calculates the minimum operation taking args: n,int
    """
    if (n <= 1):
        return 0
    primality = check_prime(n)
    if primality:
        return n
    factor = num_factors(n)
    min_operation = sum(factor)
    return min_operation
