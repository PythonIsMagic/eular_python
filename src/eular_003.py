"""Eular Problem 3 - Largest Prime Factor:
    What is the largest prime factor of the number 600,851,475,143 ?
"""
from . import timer


DESC = 'Largest Prime Factor'
SOLUTION = 6857


@timer.timeit
def solve():
    bignumber = 600851475143
    return max_prime_factor(bignumber)


def max_prime_factor(n):
    """
    Finds the largest prime factor of n and returns it.
    """
    factors = get_prime_factors(n)
    if factors is None:
        return None
    else:
        return max(factors)


def get_prime_factors(n):
    """
    Find all prime factors in N and return them as a list.
    """
    i = 2
    factors = set()

    while n > 1:
        if n % i == 0:
            factors.add(i)
            n = n / i
        else:
            # only increment if we did not find a factor.
            i = i + 1
    if len(factors) == 0:
        return None
    else:
        return factors
