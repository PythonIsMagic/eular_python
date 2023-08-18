"""Eular Problem 18 -
    Find the maximum total from top to bottom of the given triangle:
"""
from src import timer
from src.toolkit import DATADIR
from src.toolkit import read_matrix, find_max_path

DESC = 'Maximum path sum I'
SOLUTION = 1074


@timer.timeit
def solve():
    tree = read_matrix(DATADIR + 'number_tree.txt')
    return find_max_path(tree)
