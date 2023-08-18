"""Eular problem 1 - Multiples of 3 and 5:
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
from src import timer
from src.toolkit import get_multiples

DESC = "Sum multiples"
SOLUTION = 233168


@timer.timeit
def solve():
    return get_multiples()