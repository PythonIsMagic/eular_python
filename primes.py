import math


def isprime_checkall(target):
    """ Checks if an integer is prime. Returns True or False.."""
    # Start checking at 2.
    currentfactor = 3

    while currentfactor <= math.sqrt(target):
        if target % currentfactor == 0:
            # target is divisible by something other than 1 and itself. it is not prime.
            return False

        # Increment currentfactor and keep searching
        currentfactor += 2

    # Found no other factors, which means the number is prime.
    return True


def isprime_2step(target):
    """ Checks if an integer is prime. Returns True or False.."""
    if target == 2:  # The only prime even
        return True

    # Check evens: Might save processing
    if target % 2 == 0:
        return False

    if target < 2:  # Anything below 3 is not prime.
        return False

    # Start checking at 3. Lets us increment checks by 2 and skip evens.
    currentfactor = 3

    """
    We only need to search up to the square root of n because if a number N is not prime, it can
    be factored into 2 factors A and B.  N = A * B

    If A and B > squareroot(N), A*B would be greater than N.  Therefore, at least one of those
    factors must be less or equal to the square root of N. This is why we only need to test for
    factors less than or equal to the square root.

    Mathematical representation: if N = A*N and A <= B then A*A <= A*N = N
    """

    while currentfactor <= math.sqrt(target):
        if target % currentfactor == 0:
            # target is divisible by something other than 1 and itself. it is not prime.
            return False

        # Increment currentfactor and keep searching
        currentfactor += 2

    # Found no other factors, which means the number is prime.
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
        if isprime_2step(i):
            prime += 1


def generate_primes(n):
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    primes = []
    for i in range(n + 1):
        if isprime_2step(i):
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


def get_prime_factors(N):
    """
    Find all prime factors in N and return them as a list
    """
    i = 2
    factors = set()

    while N > 1:
        if N % i == 0:
            factors.add(i)
            N = N / i
        else:
            # only increment if we did not find a factor.
            i = i + 1
    if len(factors) == 0:
        return None
    else:
        return factors


def max_prime_factor(N):
    factors = get_prime_factors(N)
    if factors is None:
        return None
    else:
        return max(factors)
