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
    """
    Determines the fewest number of coins needed to meet total
    """
    coins = sorted(coins)
    if total <= 0:
        return 0
    if len(coins) <= 0:
        return -1
    count = 1
    finder = 0
    maxi = max(coins)
    target = total - maxi
    while (finder != target):
        if (finder < target):
            finder += maxi
            count += 1
        if finder > target:
            finder -= maxi
            count -= 1
            coins.remove(maxi)
            if (len(coins) <= 0):
                return -1
            maxi = max(coins)
        if finder == target:
            # coins.remove(maxi)
            return count

    '''
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))

    print(makeChange([1, 5, 10, 25], 43))

    print(makeChange([1, 7, 13, 21], 50))


    print(makeChange([1, 3, 5, 9], 15))

    print(makeChange([1, 4, 6, 8], 12))

    print(makeChange([1, 2, 5, 10, 20], 37))

    print(makeChange([1, 3, 4, 7], 10))
'''


'''def makeChange(coins, total):
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
