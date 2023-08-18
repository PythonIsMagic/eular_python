"""Eular Problem 24 -
    What is the millionth lexicographic permutation of the digits:
        0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from src import timer
import itertools


DESC = 'Lexicographic permutations'
SOLUTION = 2783915460


@timer.timeit
def solve():
    perms = list(itertools.permutations(str('0123456789'), len('0123456789')))
    return int(''.join(perms[999999]))
