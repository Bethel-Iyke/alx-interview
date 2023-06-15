#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1

        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    if total <= 0:
        return 0

    placeholder = total + 1

    memo = {0: 0}

    for i in range(1, total + 1):
        memo[i] = placeholder

        for coin in coins:
            current = i - coin
            if current < 0:
                continue

            memo[i] = min(memo[current] + 1, memo[i])

    if memo[total] == total + 1:
        return -1

    return memo[total]

''''#!/usr/bin/python3


"""
check to see that the total is not zero
check to none of the coin denomination can make the total
if the total in the list of the coin return 1
create a list of the given coin in a descending order
create a for loop using the new list
create a new total from the total - element(i)
then subtract it from the new total
if new element (i) is == new total or new total == 0  the return the element
mini coin is == len(i) """


def makeChange(coins, total):
    counter = 0
    if total <= 0:
        return 0
    if min(coins) > total:
        return -1
    if sum(coins) == total:
        return len(coins)
    if total in coins:
        return 1
    new_coins = sorted(coins, reverse=True)
    for i in range(len(new_coins)):
        while new_coins[i] <= total:
            total = total - new_coins[i]
            counter += 1
    if total == 0:
        return counter
    return -1
'''