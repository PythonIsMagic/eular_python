"""Eular Problem 14 -
    Which starting number, under one million, produces the longest Collatz
    chain?
"""

import timer
from toolkit import longest_collatz_seq

DESC = 'Longest Collatz sequence'
SOLUTION = 837799


@timer.timeit
def solve():
    upto = 1000000
    longest_seq = longest_collatz_seq(upto)
    return longest_seq[0]
