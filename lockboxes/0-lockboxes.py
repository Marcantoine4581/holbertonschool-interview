#!/usr/bin/python3
"""0. Lockboxes"""


def canUnlockAll(boxes):
    '''Method that determines if all the boxes can be opened.
    Args:
        boxes: is a list of lists of positive integers.
    Returns:
        True if all boxes can be opened, else return False
    '''
    if not isinstance(boxes, list):
            raise TypeError("boxes must be an list")

    if not isinstance(boxes[0], list):
            raise TypeError("boxes must be a list of lists")

    number_of_boxes = len(boxes)
    unlocked_boxes = [False] * number_of_boxes
    unlocked_boxes[0] = True  # The first box boxes[0] is unlocked
    keys = [0]  # Start with the keys from the first box

    for i in keys:
        if i < number_of_boxes:  # Check if i is not out of range
            for key in boxes[i]:
                if key < number_of_boxes and unlocked_boxes[key] is False:
                    unlocked_boxes[key] = True
                    keys.append(key)

    return all(unlocked_boxes)
