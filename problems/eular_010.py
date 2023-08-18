"""Eular Problem 10 - Summation of primes:
    Find the sum of all the primes below two million.
"""
from src import timer
from src.toolkit import eratosthenes_sieve

DESC = 'Summation of primes'
SOLUTION = 142913828922


@timer.timeit
def solve():
    upperlimit = 2000000
    return sum(eratosthenes_sieve(upperlimit))
