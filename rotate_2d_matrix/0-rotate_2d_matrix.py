#!/usr/bin/python3
"""0. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    '''function that rotate 90 degrees clockwise an n x n 2D matrix
    The matrix must be edited in-place.
    Args:
        matrix (list of list): n x n 2D matrix.
    Returns:
        nothing
    '''
    for i in range(int(len(matrix) / 2)):
        for j in range(i, len(matrix) - 1 - i):
            opposite_i = (len(matrix) - j - 1)
            opposite_j = (len(matrix) - 1 - i)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[opposite_i][i]
            matrix[opposite_i][i] = matrix[opposite_j][opposite_i]
            matrix[opposite_j][opposite_i] = matrix[j][opposite_j]
            matrix[j][opposite_j] = tmp
