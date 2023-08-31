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
    H = 1
    H_copy = 0
    rest = n - H
    number_ops = 0

    if n == 1:
        return 1

    while H < n:
        if H <= (rest / 2) and (H + H_copy) != ((rest - H_copy) / 2):
            H_copy = H
            H *= 2
            rest = n - H
            number_ops += 2
        else:
            H += H_copy
            rest = n - H
            number_ops += 1
    if H != n:
        return 0
    return number_ops
