"""Eular Problem 18 -
    Find the maximum total from top to bottom of the given triangle:
"""
from src import timer
from .eular_011 import read_matrix

DESC = 'Maximum path sum I'
SOLUTION = 1074


@timer.timeit
def solve():
    tree = read_matrix('data/number_tree.txt')
    return find_max_path(tree)


def find_max_path(tree):
    """ Finds the path through a tree of numbers that yields the highest sum. """
    # Start all paths at 0(or IOW, the absolute left side of the tree.)
    path = [0 for _ in range(len(tree))]
    maxsum = 0
    iterating = True

    while iterating:
        # Checking for the best sum
        pathsum = get_sum(path, tree)
        if pathsum > maxsum:
            maxsum = pathsum

        # Move path ahead
        iterating = move_path(path, len(tree) - 1)
    return maxsum


def get_sum(path, tree):
    """ Returns the sum of all the numbers in the path for the given tree. """
    pathsum = 0
    for i, row in enumerate(tree):
        pathsum += row[path[i]]
    return pathsum


def move_path(path, row):
    """ Moves to the next path in a tree. """
    # Base case: If the row is 0, we can't move that one since its the top.
    # Should mean iteration is over.
    if row == 0:
        return False
    elif path[row] == path[row - 1]:
        path[row] += 1

        # Make sure all sub rows match! To avoid skips
        for x in range(row + 1, len(path)):
            path[x] = path[row]

        return True
    else:
        return move_path(path, row - 1)
