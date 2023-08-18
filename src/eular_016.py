"""Eular Problem 16 -
    What is the sum of the digits of the number 2^1000?
"""
from src import timer

DESC = 'Power digit sum'
SOLUTION = 1366


@timer.timeit
def solve():
    return sum([int(x) for x in str(2 ** 1000)])
