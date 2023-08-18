"""Eular Problem 6 - Sum square difference:
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
"""
from . import timer

DESC = 'Sum square difference'
SOLUTION = 25164150


@timer.timeit
def solve():
    upto = 100
    sum_of_sq = sum_of_squares(upto)
    sq_of_sum = square_of_sum(upto)

    return abs(sq_of_sum - sum_of_sq)


def sum_of_squares(limit):
    """ Returns the sum of all squares in the range 1 up to and including limit. """
    return sum([i ** 2 for i in range(limit+1)])


def square_of_sum(limit):
    """ Returns the square of the sum of all integers in the range 1 up to and
        including limit.
    """
    return sum([i for i in range(limit + 1)]) ** 2
