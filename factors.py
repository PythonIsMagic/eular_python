"""
Module for determine divisors of numbers
"""

import primes


def divisors(n):
    # Returns a set of all the divisors of n using a brute force check.
    # We only need to check up to (n/2) for any n, bc n won't be divisible by anything larger
    # than that. We can also skip checking even divisors for odd numbers, since they won't be
    # divisible - this should speed up the checking a little. But this is still pretty slow
    # for numbers over a million.
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')

    factors = set()
    middle = n // 2

    if n % 2 == 0:  # It's even
        for i in range(1, middle + 1):
            if n % i == 0:
                factors.add(i)
    else:
        # It's odd (skip checking even factors)
        for i in range(1, middle + 1, 2):
            if n % i == 0:
                factors.add(i)

    # n will ALWAYS be a factor of itself.
    factors.add(n)
    return factors


def list_factors(n):
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')

    prime_facts = primes.get_prime_factors(n)
    if prime_facts is None:
        return None
    else:
        factors = list(prime_facts)

    for f in prime_facts:
        x, p = 2, 0
        while p <= n:
            p = pow(f, x)
            if n % p == 0:
                factors.append(p)
            x = x + 1

    """
    for i, x in enumerate(factors):
        for y in range(i, len(factors)):
            print('Trying {} x {}'.format(x, factors[y]))

            if n % (x * y) == 0:
                print('factor found! {}'.format(x*y))
                    factors.append(x * y)
    """
    #  return set(factors)
    return factors
