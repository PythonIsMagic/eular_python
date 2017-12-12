"""Eular Problem 8 -
    What is the 10001st prime number?
"""
import primes
import timer

DESC = '10001st prime:'
SOLUTION = 104743


@timer.timeit
def solve():
    targetprime = 10001
    result = 0
    for i, result in enumerate(primes.primes()):
        if i == targetprime - 1:
            break
    return result
