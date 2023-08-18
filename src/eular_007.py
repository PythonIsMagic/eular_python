"""Eular Problem 7 -
    What is the 10001st prime number?
"""
import math
from . import timer

DESC = '10001st prime'
SOLUTION = 104743


@timer.timeit
def solve():
    targetprime = 10001
    result = 0
    for i, result in enumerate(primes()):
        if i == targetprime - 1:
            break
    return result


def primes():
    """
    Defines a prime number generator that generates prime numbers. The first prime number
    defined is 2. Uses the is_prime tests.
    """
    i = 2
    while True:
        if isprime_ver4(i):
            yield i
        i += 1


def isprime_ver1(n):
    """
    Returns True if n is prime, False otherwise.
    * Checks all factors of n.
    * Rediculously slow. For checking up to 100k, takes over a minute.
    """
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def isprime_ver2(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.

    # We only need to search up to the square root of n because if a number N is not prime, it
    # can be factored into 2 factors A and B.  N = A * B

    # If A and B > squareroot(N), A*B would be greater than N.  Therefore, at least one of those
    # factors must be less or equal to the square root of N. This is why we only need to test for
    # factors less than or equal to the square root.

    # Mathematical representation: if N = A*N and A <= B then A*A <= A*N = N
    """
    if n < 2:
        return False
    i = 2
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def isprime_ver3(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.
    * Start checking at 3 and skip evens.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def isprime_ver4(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.
    * Start checking at 3 and skip evens.
    * Check 2 and the modulus at the same time. (Saves 2 lines)
    """
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    i = 3
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

