#!/usr/bin/python3
""" program the  determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """ checking the lenght of boxes """
    if(len(boxes) == 0 or type(boxes) != list):
        """initialization for unchecked boxes """
        return false

    a_locked = len(boxes)
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if (box != 0 and box < a_locked):
                keys.append(box)

    keys = set(keys)

    if (len(keys) == len(boxes)):
        return True
    else:
        return False
