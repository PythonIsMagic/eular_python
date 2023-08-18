"""Eular problem 5 - Smallest multiple:
    What is the smallest positive number that is evenly divisible by all
    numbers 1 to 20?
"""

from src import timer
from src.toolkit import div_by_all_upto

DESC = 'Smallest multiple'
SOLUTION = 232792560


@timer.timeit
def solve():
    limit = 20
    return div_by_all_upto(limit)
