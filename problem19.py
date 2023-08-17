"""Eular problem 19 -
    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
"""

import timer
from toolkit import count_sundays

DESC = 'Counting Sundays'
SOLUTION = 171


@timer.timeit
def solve():
    return count_sundays()
