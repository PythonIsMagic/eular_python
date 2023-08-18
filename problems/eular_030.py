"""Eular Problem 30 -
    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
"""
from src import timer

DESC = 'Digit fifth powers'
SOLUTION = None


def power_sums(power):
    i = 0
    while True:
        if not writable_by_powers(i, power):
            break
        i += 1

    fifth_sums = []
    for n in range(2, i + 1):
        if sum_powers(n, power) == n:
            fifth_sums.append(n)
    return fifth_sums


def sum_powers(n, p):
    return sum(int(x) ** p for x in str(n))


def writable_by_powers(n, p):
    digits = len(str(n))
    max_amt = digits * (9 ** p)
    if max_amt < n:
        return False
    else:
        return True


@timer.timeit
def solve():
    POWER = 5
    return sum(power_sums(POWER))
