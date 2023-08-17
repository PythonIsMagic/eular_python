"""Eular Problem 3 - Largest Prime Factor:
    What is the largest prime factor of the number 600,851,475,143 ?
"""
import toolkit
import timer

DESC = 'Largest Prime Factor'
SOLUTION = 6857


@timer.timeit
def solve():
    bignumber = 600851475143
    return toolkit.max_prime_factor(bignumber)
