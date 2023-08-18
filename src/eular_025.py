
"""Eular Problem 25 -
    What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
from src import timer
from src.eular_002 import fibonaccis


DESC = 'The Fibonacci sequence'
SOLUTION = 4782


@timer.timeit
def solve():
    i = 0
    for i, x in enumerate(fibonaccis()):
        if len(str(x)) >= 1000:
            break

    return i + 1  # Avoid off by one err
