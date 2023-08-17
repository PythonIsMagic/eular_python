"""Eular problem 2 - Even Fibonacci numbers:
    By considering the terms in the Fibonacci sequence whose values do not
    exceed 4 million, find the sum of the even-valued terms.
"""
import timer
from toolkit import fibonaccis

DESC = 'Even Fibonacci numbers'
SOLUTION = 4613732


@timer.timeit
def solve():
    UPPERLIMIT = 4000000
    return sum([x for x in fibonaccis(UPPERLIMIT) if x % 2 == 0])
