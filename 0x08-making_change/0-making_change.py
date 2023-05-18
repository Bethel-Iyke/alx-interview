#!/usr/bin/python3


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
