#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True
    keys = boxes[0].copy()

    while keys:
        key = keys.pop()
        if key < len(boxes) and not opened_boxes[key]:
            opened_boxes[key] = True
            keys.extend(boxes[key])

    return all(opened_boxes)


def main():
    """Entry point"""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False


if __name__ == '__main__':
    main()
