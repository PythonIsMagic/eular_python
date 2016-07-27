#!/usr/bin/env python
"""
Eular problem 1:
If we list all the natural numbers below 10 that are

multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiples(factorlist, limit):
    """
    Returns the sum of the specificed multiples.
    """

    result = 0

    # Go through all numbers up to 1000
    for i in range(limit):
        if is_multiple_of(i, factorlist):
            result += i

    return result


def is_multiple_of(dividend, factorlist):
    if 0 in factorlist:
        raise ValueError('0 is not valid in list of factors!')

    for n in factorlist:
        if dividend % n == 0:
            return True
    else:
        return False
