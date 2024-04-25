#!/usr/bin/python3
"""0x07-rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
