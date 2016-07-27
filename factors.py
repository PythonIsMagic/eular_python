"""
Module for determine divisors of numbers
"""


def divisors(n):
    # Returns a set of all the divisors of n.
    # We only need to check up to (n/2) for any n, bc n won't be divisible by anything larger
    # than that.
    if n < 1:
        raise ValueError('n must be a positive integer.')

    factors = set()
    middle = n // 2

    if n % 2 == 0:  # It's even
        for i in range(1, middle + 1):
            if n % i == 0:
                factors.add(i)
    else:
        # It's odd (skip checking even factors)
        for i in range(1, middle + 1, 2):
            if n % i == 0:
                factors.add(i)

    # n will ALWAYS be a factor of itself.
    factors.add(n)
    return factors


def divisors_dividing(n):
    """
    Finds all divisors of the target number and returns them as a set.
    * NOTE!!!!! THIS FAILS TO FIND CERTAIN FACTORS
    * EXAMPLE: FOR 24, it skips 8. only finds 1, 2, 3, 6, 12, 24
    """
    if n < 1:
        raise ValueError('n must be a positive integer.')

    factors = set()
    factors.add(n)

    i = 2
    while i <= n:
        if n % i == 0:
            n = int(n / i)
            factors.add(i)
            factors.add(n)

        else:
            # only increment if we did not find a factor.
            i = i + 1

    return factors
