"""
  " Collection of function to process prime numbers and divisors.
  """

from .eular_010 import eratosthenes_sieve
from .eular_007 import isprime_ver2, isprime_ver3, isprime_ver4
from . import timer

def sift_primes(n):
    """Sieve of eratosthenese. For all integers up to n, sifts out the non-primes
        and returns list of all primes up to n.
    """
    if n < 2:
        print('Passed in integer is not large enough to contain primes.')
        return -1

    numbers = [x for x in range(2, n + 1)]
    #  numbers = [True for x in range(2, n + 1)]

    i = 2
    while i < len(numbers) + 2:
        for j in range(i*2, n + 1, i):
            #  print('j = {}'.format(j))
            if j in numbers:
                numbers.remove(j)

        i += 1

    # Failed attempt
    """
    for i in numbers:
        for j in numbers:
            if j % i == 0:
                numbers.remove(j)
    """

    return numbers


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


def print_list(alist):
    """ Prints a list recursively. """
    pl(alist, 0)


def pl(alist, index):
    if index < len(alist) - 1:
        print(alist[index])
        pl(alist, index + 1)
    else:
        # Base case: index is at the end
        print(alist[index])


def print_selection(alist, index, factors):
    # Base case: At index 0
    if factors == 0:
        print(alist[index])
    else:
        print(alist[index])
        print_selection(alist, index + 1, factors - 1)


def recursive_try():
    pass
    #  print('Eular 9: Recursive solution')
    #  result = recursive_solution()
    #  if result is None:
        #  print('No solution was found')
        #  exit()
    #  else:
        #  a2, b2, c2 = result

    #  a = math.sqrt(a2)
    #  b = math.sqrt(b2)
    #  c = math.sqrt(c2)


def test_primes():
    # def is_prime(target):

    # def max_prime_factor(target):

    # def getprime(index):

    # def sift_primes(n):
    timer.enhanced_tests(toolkit.sieve_rm_method, 1000)
