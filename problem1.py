"""Eular problem 1 - Multiples of 3 and 5:
    Find the sum of all the multiples of 3 or 5 below 1000.
"""
import timer

DESC = "Sum multiples"
SOLUTION = 233168


@timer.timeit
def solve():
    return get_multiples()


def get_multiples():
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result
