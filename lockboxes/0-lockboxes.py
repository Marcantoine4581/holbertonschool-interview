#!/usr/bin/python3
"""0. Lockboxes"""


def canUnlockAll(boxes):
    '''Method that determines if all the boxes can be opened.
    Args:
        boxes: is a list of lists of positive integers.
    Returns:
        True if all boxes can be opened, else return False
    '''
    number_of_boxes = len(boxes)
    unlocked_boxes = [False] * number_of_boxes
    unlocked_boxes[0] = True  # The first box boxes[0] is unlocked
    keys = [0]  # Start with the keys from the first box

    for i in keys:
        for key in boxes[i]:
            if unlocked_boxes[key] is False:
                unlocked_boxes[key] = True
                keys.append(key)
    return all(unlocked_boxes)
