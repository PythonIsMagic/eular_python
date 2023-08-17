"""Eular Problem 12 - :
    What is the value of the first triangle number to have over five hundred
    divisors?
"""

import toolkit
import timer
from toolkit import triangles

DESC = 'Triangle numbers'
SOLUTION = 76576500


@timer.timeit
def solve():
    result = 0
    for result in triangles():
        # Skip checking numbers that don't end in 0.
        if result % 10 != 0:
            continue
        f = toolkit.divisors(result)

        if len(f) > 500:
            break
    return result
