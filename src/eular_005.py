"""Eular problem 5 - Smallest multiple:
    What is the smallest positive number that is evenly divisible by all
    numbers 1 to 20?
"""

from . import timer

DESC = 'Smallest multiple'
SOLUTION = 232792560


@timer.timeit
def solve():
    limit = 20
    return div_by_all_upto(limit)


def factor_of_all_upto(num, limit):
    """ Returns True if num is divisible by all numbers in the range of integers
        in 1 up to and including limit.

        # Speed up by skipping 1. Any integer is divisible by 1!
        # If the number ends in 1, 3, 7, or 9, it's more likely to be prime.
        # Check backwards from the largest possible factor
    """
    start = 2
    for factor in range(start, limit + 1):
        if num % factor != 0:
            return False
    return True


def div_by_all_upto(limit):
    """ Finds the first integer that is divisible by all numbers 1 through, and
        including, limit.
    """
    # Start at the highest factor we are testing by because the target number won't be divisible
    # by any numbers larger than it.
    if limit < 10:
        raise ValueError('This function only tests for ranges 10 and above!')
    elif limit % 10 != 0:
        raise ValueError('This function only tests multiples of 10!')

    i = limit

    while True:
        # Skip any number that doesn't end in 0.
        # Ending in 0 maximizes our chance of a big divisor.
        if i % 10 != 0:
            pass
        elif factor_of_all_upto(i, limit):
            break

        # Increase by the size of the largest factor we are testing by. This should dramatically
        # increase the speed and we don't need to test numbers in between since they won't be
        # divisible by that number.
        i += limit
    return i
