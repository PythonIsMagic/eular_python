"""Eular Problem 13 -
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
"""

from src import timer
from src.toolkit import DATADIR
from src.toolkit import read_numbers

DESC = 'Large Sum'
SOLUTION = 5537376230


@timer.timeit
def solve():
    n = read_numbers(DATADIR + 'bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x

    sum_list = list(str(bigsum))
    return int(''.join(sum_list[0:10]))
