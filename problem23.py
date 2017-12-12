"""Eular Problem 23 -
    Find the sum of all positive integers which cannot be written as the sum
    of two abundant numbers.
"""

import itertools
import primes
import timer

DESC = 'Non-abundant sums:'
SOLUTION = 4179871

def abundant(n):
    """ A number n is called abundant if the sum of its proper divisors is more
        than n. Returns True if n is an abundant number, False otherwise.
    """
    return sum(primes.divisors_proper(n)) > n


def abundants_upto(limit):
    """ Returns a list of all abundant numbers up, and including, the limit. """
    return [i for i in range(1, limit + 1) if abundant(i)]


def nonsummable_by_abundants():
    """ Return the sum of all integers that cannot be written as the sum of
        abundant numbers.
    """
    LIMIT = 28123
    # Calculate all the abundant numbers up to limit.
    abundants = abundants_upto(LIMIT)

    # Create all possible 2 term combinations for sums.
    #  pairs = list(itertools.combinations(abundants, 2)) # No
    #  pairs = itertools.combinations(abundants, 2) # No
    #  pairs = itertools.permutations(abundants, 2) # No
    # We want the Cartesian product, because the abundant numbers, can be repeated(ex: 12 - the
    # lowest abundant number, can be repeated 12+12 to sum 24.)
    pairs = itertools.product(abundants, repeat=2)

    # Create a set of sums using a set comprehension
    abundant_sums = {a + b for a, b in pairs}

    unsummable = [i for i in range(LIMIT + 1) if i not in abundant_sums]

    return sum(unsummable)



@timer.timeit
def solve():
    return nonsummable_by_abundants()
