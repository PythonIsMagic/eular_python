"""Eular Problem 21 -
    Evaluate the sum of all the amicable numbers under 10000.
"""
from src import timer
from src.toolkit import divisor_sum_dict


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
