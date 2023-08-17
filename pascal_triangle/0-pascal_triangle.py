#!/usr/bin/python3
"""0. Pascal's Triangle"""


def pascal_triangle(n):
    '''function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    Args:
        n (int): the number of lists in the list.
    Returns:
        List of lists of integers
        or empty list if n <= 0
    '''
    if n <= 0:
        return []

    triangle = []
    lists = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            lists = [1]
            for j in range(1, i):
                lists.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            lists.append(1)
            triangle.append(lists)
    return triangle
