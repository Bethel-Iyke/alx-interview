#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.
Write a method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    '''Function to determine if all boxes can be opened'''
    # initialize process by creating a set, key_ caddy
    # with 1 key for box 0, element 0
    key_caddy = [0]

    # define small box state
    locked = False
    unlocked = True

    # Store unlocked boxes in a dictionary with box number as key
    # and state as value, initialize with box 0 as unlocked
    box_state = {0: unlocked}

    # if boxes is a list of lists
    if type(boxes) is not list or len(boxes) == 0:
        return False

    if len(boxes) == 1:
        return True

    # count the number of small boxes in the big box
    for key in key_caddy:
        for box in boxes[key]:
            if box not in key_caddy and box < len(boxes):
                key_caddy.append(box)
                box_state[key] = unlocked

    if len(key_caddy) == len(boxes):
        return True
    return False


if __name__ == "__main__":
    canUnlockAll(boxes)
