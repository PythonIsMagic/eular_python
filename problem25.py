
"""Eular Problem 25 -
    What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import problem2
import timer

DESC = 'The Fibonacci sequence'
SOLUTION = 4782


@timer.timeit
def solve():
    i = 0
    for i, x in enumerate(problem2.fibonaccis()):
        if len(str(x)) >= 1000:
            break

    return += 1  # Avoid off by one err
