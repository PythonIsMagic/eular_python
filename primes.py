"""
  " Collection of function to process prime numbers and divisors.
  """

import math
import timer


def sift_primes(n):
    """Sieve of eratosthenese. For all integers up to n, sifts out the non-primes
        and returns list of all primes up to n.
    """
    if n < 2:
        print('Passed in integer is not large enough to contain primes.')
        return -1
    print('sifting primes of {}'.format(n))

    numbers = [x for x in range(2, n + 1)]
    #  numbers = [True for x in range(2, n + 1)]

    print(numbers)

    i = 2
    while i < len(numbers) + 2:
        #  print('i = {}'.format(i))
        for j in range(i*2, n + 1, i):
            #  print('j = {}'.format(j))
            if j in numbers:
                numbers.remove(j)

        #  print(numbers)
        i += 1

    # Failed attempt
    """
    for i in numbers:
        print('i = {}'.format(i))
        for j in numbers:
            print('j = {}'.format(j))
            if j % i == 0:
                numbers.remove(j)
        print(numbers)
    """

    return numbers


def divisors(n):
    """ Creates a list of all the factors of n and returns them as a set. First
        we get the prime factors of n. To get any remaining factors, we take all
        the prime factors and take each to it's maximum power. This results in a
        list of factors we can use to build the remaining factors.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')
    elif n == 1:
        return {1}

    prime_facts = get_prime_factors(n)
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


def divisors_bruteforce(n):
    """
    Returns a set of all the divisors of n using a brute force check.  We only need to check up
    to (n/2) for any n, because n won't be divisible by anything larger than that. We'll also
    skip checking even divisors for odd numbers, since they won't be divisible, however this is
    still pretty slow for numbers over a million.
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


def divisors_proper(n):
    """ Return a set containing the proper divisors of n (numbers less than n
        which divide evenly into n).
    """
    d = divisors(n)
    d.remove(n)
    return d


def divisor_sum_dict(limit):
    """ Make a dictionary of divisor sums up to, but not including, limit.
        Example: The divisor sum of 2 would be 1 + 2 = 3.
        The divisor sum of 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    """
    return {n: sum_proper_divisors(n) for n in range(1, limit)}


def factor_of_all_upto(num, limit):
    """ Returns True if num is divisible by all numbers in the range of integers
        in 1 up to and including limit.

        # Speed up by skipping 1. Any integer is divisible by 1!
        # If the number ends in 1, 3, 7, or 9, it's more likely to be prime.
        # Check backwards from the largest possible factor
    """
    start = 2
    for factor in range(start, limit + 1):
        if num % factor != 0:
            return False
    return True


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


def eratosthenes_sieve(n):
    """
    Eratosthenes sieve.
    * Implemented using a list and None to specify a non-prime slot.
    """
    # Great speed!
    L = [x for x in range(n+1)]
    L[0], L[1] = None, None

    i = 0
    while i < len(L):
        if L[i] is None:
            pass
        else:
            for j in range(i * 2, len(L), i):
                L[j] = None
        i += 1
    return [x for x in L if x is not None]


def max_prime_factor(n):
    """
    Finds the largest prime factor of n and returns it.
    """
    factors = get_prime_factors(n)
    if factors is None:
        return None
    else:
        return max(factors)


def get_prime_factors(n):
    """
    Find all prime factors in N and return them as a list.
    """
    i = 2
    factors = set()

    while n > 1:
        if n % i == 0:
            factors.add(i)
            n = n / i
        else:
            # only increment if we did not find a factor.
            i = i + 1
    if len(factors) == 0:
        return None
    else:
        return factors


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n(numbers less than n which divide evenly into n).
    """
    divs = divisors_proper(n)
    return sum(divs)


@timer.timeit
def count_primes(upto, func):
    c = 0
    for i in range(upto):
        if func(i):
            c += 1
    return c


@timer.timeit
def sieve_primes(upto, func):
    p = func(upto)
    return len(p)


def main():
    """ Runs through some tests for different prime functions. """
    print('~~~~~~~~~~~')
    print('Prime tests')

    counts = {
        1000: 168,
        10000: 1229,
        100000: 9592,
        1000000: 78498,
        10000000: 664579,
        # 100000000: 5761455  # too big - got 'Killed'
    }

    funcs = [isprime_ver2, isprime_ver3, isprime_ver4]
    sieves = [eratosthenes_sieve]

    for k, v in sorted(counts.items()):
        print('---------------------------------')
        #  print('Testing 0-{}'.format(k))
        for f in funcs:
            if k < 1000000:
                count = count_primes(k, f)
                print('{} primes found up to {}.'.format(count, k))
                # Validate count
                assert count == v

        # Test the sieves
        for s in sieves:
            count = sieve_primes(k, s)
            assert count == v
            print('{} primes found up to {}.'.format(count, k))


if __name__ == "__main__":
    main()
