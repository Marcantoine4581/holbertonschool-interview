#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    '''function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    Args:
        coins (list[int]): values of the coins in your possession.
        total (int) : total to meet with coins.
    Returns:
        The fewest number of coins needed to meet total.
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    
    sorted_coins = sorted(coins, reverse=True)
    nb_coin = 0

    for coin in sorted_coins:
        if total % coin <= total:
            nb_coin += total // coin
            total = total % coin

    return nb_coin if total == 0 else -1