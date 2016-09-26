import math
import timer


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
    Defines a prime number generator that generates prime numbers up until the n'th prime number.
    The first prime number defined is 2. Uses the is_prime tests.
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


if __name__ == "__main__":
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
