"""Eular problem 5 - Smallest multiple:
    What is the smallest positive number that is evenly divisible by all
    numbers 1 to 20?
"""

import primes
import timer

DESC = 'Smallest multiple'
SOLUTION = 232792560


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
        elif primes.factor_of_all_upto(i, limit):
            break

        # Increase by the size of the largest factor we are testing by. This should dramatically
        # increase the speed and we don't need to test numbers in between since they won't be
        # divisible by that number.
        i += limit
    return i


@timer.timeit
def solve():
    limit = 20
    return div_by_all_upto(limit)
