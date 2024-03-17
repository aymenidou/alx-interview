#!/usr/bin/python3
'''0x01. Lockboxes
'''


def canUnlockAll(boxes):
    '''You have n number of locked boxes in front of you.
      Each box is numbered sequentially from 0 to n - 1
        and each box may contain keys to the other boxes,
        this function determines if all the boxes can be opened.
    '''
    n = len(boxes)

    opened_boxes = set()
    opened_boxes.add(0)
    to_explore = [0]
    while to_explore:
        current_box = to_explore.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                to_explore.append(key)
    return len(opened_boxes) == len(boxes)
