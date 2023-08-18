"""Eular Problem 17 -
    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?
"""

import timer
from toolkit import letter_qty, num_to_alpha

DESC = 'Number letter counts'
SOLUTION = 21124


@timer.timeit
def solve():
    result = 0
    for i in range(1, 1001):
        number = num_to_alpha(i)
        qty = letter_qty(number)
        result += qty
    return result
