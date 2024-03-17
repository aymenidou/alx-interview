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

    to_explore = set(boxes[0]).difference(set([0]))
    while len(to_explore) > 0:
        current_box = to_explore.pop()
        if not current_box or current_box >= n or current_box < 0:
            continue
        if current_box not in opened_boxes:
            to_explore = to_explore.union(boxes[current_box])
            opened_boxes.add(current_box)
    return n == len(opened_boxes)
