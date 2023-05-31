#!/usr/bin/python3
"""this program checks the perimeter of an island in a grid"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    island_perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                island_perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    island_perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    island_perimeter -= 2
    return island_perimeter
