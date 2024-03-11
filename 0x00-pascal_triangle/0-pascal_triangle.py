#!/usr/bin/python3
''' A module for 0x00. Pascal's Triangle. '''


def pascal_triangle(n):
    '''returns a list of lists of integers
    representing the Pascal's triangle of n
    '''
    pascal_list = []
    if type(n) is not int or n <= 0:
        return pascal_list

    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])
        pascal_list.append(line)
    return pascal_list
