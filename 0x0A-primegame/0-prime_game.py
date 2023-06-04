#!/usr/bin/python3

""" a program that determines the winner of a game that selects
a numer and removes the multiples of the selected number """


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
        return True


def find_prime(num):
    primes = []
    for b in range(2, len(num)):
        if is_prime(b):
            primes.append(b)
        return primes


def find_multiples(given_num, primes):
    multiples = []
    for num in primes:
        if num % given_num == 0:
            multiples.append(num)
        return multiples


def isWinner(x, nums):
    Maria_wins = 0
    Ben_wins = 0
    while x:
        primes = find_prime(nums)
        for val in primes:
            if val in nums:
                nums.remove(val)
                multiples = find_multiples(val, nums)
                for mul in multiples:
                    nums.remove(mul)
            if len(primes) % 2 == 0:
                Ben_wins += 1
            else:
                Maria_wins += 1
            x -= 1
        if Maria_wins > Ben_wins:
            return "Maria"
        elif Ben_wins > Maria_wins:
            return "Ben"
        else:
            return None
