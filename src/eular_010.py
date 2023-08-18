"""Eular Problem 10 - Summation of primes:
    Find the sum of all the primes below two million.
"""
from . import timer

DESC = 'Summation of primes'
SOLUTION = 142913828922


@timer.timeit
def solve():
    upperlimit = 2000000
    return sum(eratosthenes_sieve(upperlimit))


def eratosthenes_sieve(n):
    """
    Eratosthenes sieve.
    * Implemented using a list and None to specify a non-prime slot.
    """
    # Great speed!
    L = [x for x in range(n+1)]
    L[0], L[1] = None, None

    i = 0
    while i < len(L):
        if L[i] is None:
            pass
        else:
            for j in range(i * 2, len(L), i):
                L[j] = None
        i += 1
    return [x for x in L if x is not None]
