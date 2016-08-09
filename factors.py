"""
Module for determine divisors of numbers
"""

import primes


def bruteforce(n):
    """
    Returns a set of all the divisors of n using a brute force check.  We only need to check up
    to (n/2) for any n, bc n won't be divisible by anything larger than that. We can also skip
    checking even divisors for odd numbers, since they won't be divisible - this should speed up
    the checking a little. But this is still pretty slow for numbers over a million.
    """
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


def divisors(n):
    """
    Creates a list of all the factors of n and returns them as a set. First we get the prime
    factors of n. To get any remaining factors, we take all the prime factors and take each to
    it's maximum power. This results in a list of factors we can use to build the remaining
    factors.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')
    elif n == 1:
        return {1}

    prime_facts = primes.get_prime_factors(n)
    if prime_facts is None:
        return None

    factors = list(prime_facts)

    for x in factors:
        for y in factors:
            product = y * x

            if n % product == 0 and product not in factors:
                factors.append(product)

    # Cutting out 1 saves a lot of checks and is a factor of every positive number.
    factors.append(1)
    return set(factors)


def proper_divisors(n):
    """
    Return a set containing the proper divisors of n (numbers less than n which divide evenly
    into n).
    """
    d = divisors(n)
    d.remove(n)
    return d


def test_fromprime(n):
    failures = 0

    for i in range(1, n):
        bf = bruteforce(i)
        fp = divisors(i)

        if bf != fp:
            print('Test failed on {}!'.format(i))
            print('bruteforce: {}'.format(sorted(bf)))
            print('fromprime:  {}'.format(sorted(fp)))
            failures += 1
        else:
            print('{} - Check.'.format(i))

    if failures > 0:
        print('{} out of {} tests failed.'.format(failures, n - 1))
    else:
        print('All tests passed! (up to {})'.format(n))
