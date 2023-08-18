"""Eular Problem 18 -
    Find the maximum total from top to bottom of the given triangle:
"""
import toolkit
import timer
from toolkit import DATADIR, find_max_path

DESC = 'Maximum path sum I'
SOLUTION = 1074


@timer.timeit
def solve():
    tree = toolkit.read_matrix(DATADIR + 'number_tree.txt')
    return find_max_path(tree)
