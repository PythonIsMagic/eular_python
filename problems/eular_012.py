"""Eular Problem 12 - :
    What is the value of the first triangle number to have over five hundred
    divisors?
"""
from src import timer
from src.toolkit import divisors, triangles

DESC = 'Triangle numbers'
SOLUTION = 76576500


@timer.timeit
def solve():
    result = 0
    for result in triangles():
        # Skip checking numbers that don't end in 0.
        if result % 10 != 0:
            continue
        f = divisors(result)

        if len(f) > 500:
            break
    return result
