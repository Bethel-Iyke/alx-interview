#!/usr/bin/python3
'''taking turns with prime numbers from a set of integers'''


def isWinner(x, nums):
    ''' Returns:
    name of the player that won the most rounds.
    If the winner cannot be determined, return None.
    '''
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria_score = 0
    ben_score = 0

    prime = [1 for x in range(sorted(nums)[-1] + 1)]
    prime[0], prime[1] = 0, 0
    for i in range(2, len(prime)):
        rm_multiples(prime, i)

    for i in nums:
        if sum(prime[0:i + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def rm_multiples(rm, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(rm)):
        try:
            rm[i * x] = 0
        except (ValueError, IndexError):
            break


'''#!/usr/bin/python3
"""
Determine who the winner of each game is.

input: rounds = x
       array = nums
return: name of the player that won the most rounds
        None if winner cannot be determined
"""


def isPrime(n):
    """
    Check if number is prime
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    return game winner
    """
    maria = 0
    ben = 0
    for i in range(x):
        noRounds = nums[i]
        prime_count = sum(isPrime(num) for num in range(2, noRounds + 1))

        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
'''
