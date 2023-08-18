"""Eular Problem 21 -
    Evaluate the sum of all the amicable numbers under 10000.
"""
from . import timer

from .eular_012 import divisors

DESC = 'Amicable numbers'
SOLUTION = 31626


def add_amicables(limit):
    """ Adds all the amicable numbers up to limit and returns the sum. """
    amicables = set()
    div_sums = divisor_sum_dict(limit)

    for k, v in div_sums.items():
        # Skip divisor sums that are equal to or over the limit - they won't be in the keys.
        # Also - k and v cannot be equal. k != v.
        if v >= limit or k == v:
            continue

        # Since we have the divisor sum of k as v, we can conversely lookup the opposite
        # div_sums[v] and check if it equals k.
        if div_sums.get(v, -1) == k:
            amicables.add(k)

    return sum(amicables)


@timer.timeit
def solve():
    LIMIT = 10000
    # Add all of the amicable numbers together
    return add_amicables(LIMIT)


def divisor_sum_dict(limit):
    """ Make a dictionary of divisor sums up to, but not including, limit.
        Example: The divisor sum of 2 would be 1 + 2 = 3.
        The divisor sum of 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    """
    return {n: sum_proper_divisors(n) for n in range(1, limit)}


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n(numbers less than n which divide evenly into n).
    """
    divs = divisors_proper(n)
    return sum(divs)


def divisors_proper(n):
    """ Return a set containing the proper divisors of n (numbers less than n
        which divide evenly into n).
    """
    d = divisors(n)
    d.remove(n)
    return d
