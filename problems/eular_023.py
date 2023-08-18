"""Eular Problem 23 -
    Find the sum of all positive integers which cannot be written as the sum
    of two abundant numbers.
"""
from src import timer
from src.toolkit import nonsummable_by_abundants

DESC = 'Non-abundant sums'
SOLUTION = 4179871


@timer.timeit
def solve():
    return nonsummable_by_abundants()
