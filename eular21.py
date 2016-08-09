#!/usr/bin/env python3
"""
++ Eular21

*Amicable numbers*

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

example: The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.


Evaluate the sum of all the amicable numbers under 10000.
"""

import factors


def d(n):
    """
    Return the sum of the proper divisors of n
    (numbers less than n which divide evenly into n).
    """
    divisors = factors.fromprime(n)
    divisors.remove(n)
    return sum([int(x) for x in divisors])


def find_amicable_pair(n, pair_dict):
    pass


if __name__ == "__main__":
    amicable_sum = 0
    div_sums = []
    amicables = set()

    # For all numbers from 0-10000, make a list containing their divisor sums.

    # for each entry in the sums list, check for an amicable pair and add it to a set.

    # Add all of the amicable numbers together
