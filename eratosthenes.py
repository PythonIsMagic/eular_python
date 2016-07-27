#!/usr/bin/env python3


# Sieve of eratosthenese
def sift_primes(n):
    """
    For all integers up to n, sifts out the non-primes and returns list of all primes up to n.
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

if __name__ == "__main__":
    """
    for i in range(10):
        sift_primes(i)
    """
    #  sift_primes(15)
    #  sift_primes(15)
    num = sift_primes(100)
    print('{} primes'.format(len(num)))
