#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid.
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if ((i != 0 or i != (len(grid) - 1)) and (
                   (j != 0) or j != (len(grid[i]) - 1))):
                    top_c = grid[i - 1][j]
                    right_c = grid[i][j + 1]
                    bottom_c = grid[i + 1][j]
                    left_c = grid[i][j - 1]
                    perimeter += (4 - top_c - right_c - bottom_c - left_c)
    return perimeter
