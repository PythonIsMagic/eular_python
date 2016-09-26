import math


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


def getprime(n):
    if n < 0:
        raise ValueError('getprime(n) must take an integer greater than or equal to 0.')

    i = 2
    prime = 0
    while True:
        if prime == n:
            return i

        i += 1
        if isprime_ver4(i):
            prime += 1


def generate_primes(n):
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    primes = []
    for i in range(n + 1):
        if isprime_ver4(i):
            primes.append(i)
        #  primes.append(getprime(i))
    return primes


def sieve_rm_method(n):
    """
    For integers up to n, sifts out non-primes via Sieve of Eratosthenese and returns
    list of all primes up to, and including, n.
    """
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    numbers = [x for x in range(2, n + 1)]
    i = 2
    while i < len(numbers) + 2:
        for j in range(i * 2, n + 1, i):
            if j in numbers:
                numbers.remove(j)
        i += 1
    return numbers


def sieve_markers(n):
    """
    Sieve of Eratosthenese; returns list primes up to, and including, n.
    * Uses enumerate while going through the list to remove numbers by index.
    """
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    numbers = [x for x in range(n + 1)]
    numbers[0] = None
    numbers[1] = None

    size = len(numbers)
    i = 1
    while i < size:
        i += 1
        if i is None:
            continue
        for j in range(i * 2, size, i):
            numbers[j] = None

    return [x for x in numbers if x is not None]


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


def max_prime_factor(n):
    """
    Finds the largest prime factor of n and returns it.
    """
    factors = get_prime_factors(n)
    if factors is None:
        return None
    else:
        return max(factors)


def sum_primes_via_iteration(n):
    prime_sum = 0
    for i in range(n):
        if isprime_ver4(i):
            prime_sum += i
    return prime_sum


def sum_primes_via_sieve(n):
    prime_sum = 0
    set_of_primes = sieve_rm_method(n - 1)
    for p in set_of_primes:
        prime_sum += p
    return prime_sum
