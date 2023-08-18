"""Eular Problem 3 - Largest Prime Factor:
    What is the largest prime factor of the number 600,851,475,143 ?
"""
from . import timer
from .primes import get_prime_factors

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


