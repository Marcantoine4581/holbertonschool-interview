#!/usr/bin/python3
""" 0. Minimum Operations """


def minOperations(n):
    '''Method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Args:
        n (int): the number of character to reach.
    Returns:
        an integer
        or O if n is impossible to achieve
    '''
    if n == 1:
        return 0

    H = 1
    H_copy = 0
    number_ops = 0

    while H < n:
        if n % H == 0:
            H_copy = H
            H *= 2
            number_ops += 2  # Copy All and Paste
        else:
            H += H_copy
            number_ops += 1  # Paste

    if H != n:
        return 0
    return number_ops
