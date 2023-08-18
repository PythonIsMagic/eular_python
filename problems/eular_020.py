"""Eular Problem 20 -
    Find the sum of the digits in the number 100!
"""

import math
import timer

DESC = 'Factorial digit sum:'
SOLUTION = 648


def factorial_sum(n):
    """ Returns the sum of the integers in the factorial of n. """
    return sum([int(x) for x in str(math.factorial(n))])


@timer.timeit
def solve():
    num = 100
    return factorial_sum(num)
