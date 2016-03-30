#!/usr/bin/env python
"""
++ Eular Problem3
*Largest Prime Factor*
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600,851,475,143 ?
"""

import math


def is_prime(target):
    """ Checks if a given integer is prime or not. Returns true if it is, false
    otherwise."""
    if target == 2:
        return True      # The only prime even #

    # Check evens: before anything else because it is the most likely scenario.
    # We might save processing if we only need to perform 1 check the majority
    # of the time.
    if target % 2 == 0:
        return False

    # Elementary checks: Check ease cases next.
    if target < 2:
        return False      # Anything below 2 is not prime.

    # If we make it this far, we'll start with 3.
    # Also lets us increment the integer by 2 and skip the even #s.
    currentfactor = 3

    # Start iterating through all the potential factors in n
    # We only need to search up to the square root of n because
    # if a number N is not prime, it can be factored into 2 factors A and B.
    # N = A * B
    # If A and B > squareroot(N), A*B would be greater than N.
    # Therefore, at least one of those factors must be less or equal to the
    # square root of N. This is why we only need to test for factors less than
    # or equal to the square root.
    # Mathematical representation: if N = A*N and A <= B then A*A <= A*N = N

    while currentfactor <= math.sqrt(target):
        # Check if n is divisible by the current potential factor
        if target % currentfactor == 0:
            # YES: number is divisible by something other than 1 and itself.
            # Therefore, it is not prime.
            return False

        # NO: Increment currentfactor and keep searching
        currentfactor += 2  # Advancing by 2 saves time, skips even #s

    # Found no other factors, which means the number is prime.
    return True


def get_largest_prime_factor(target):
    """ Finds the largest prime factor in the target number """
    # PRECONDITIONS
    # Check if target is prime. If prime, return IT.
    if is_prime(target):
        return target

    # Check if target is < 2.
    # Throw an exception(or return -1). It won't have any prime factors.
    if target < 2:
        return -1

    i = 2
    biggest_factor = 0

    # Start searching all the #s in the target for prime factors,
    while i <= target:
        # Is i a factor of n and prime? (If both a factor and prime, then we
        if is_prime(i) and target % i == 0:
            # have actually found 2 factors.)
            # Find the other factor:
            # n = n/i
            target = target/i

            if i >= biggest_factor:
                biggest_factor = i
                print('Another prime factor found! {}'.format(i))
            if is_prime(target) and target >= biggest_factor:
                biggest_factor = target
                print('Another prime factor found! {}'.format(target))

            # If n is also prime, find the larger of n or i and set it as
            # biggestFactor
            # if max(i, target) > biggest_factor:
                # biggest_factor = max(i, target)
            # If factor2 is not prime, simply set the biggestFactor as i.
        else:
            # only increment if we did not find a factor.
            i = i + 1

    return biggest_factor


def test():
    for num in range(20):
        print('Is prime {}? {}'.format(num, is_prime(num)))

    print('Is prime {}? {}'.format(0, is_prime(0)))
    print('Is prime {}? {}'.format(-1, is_prime(-1)))

    print('Largest prime factor of 10: {}'.format(
        get_largest_prime_factor(10)))
    print('Largest prime factor of 100: {}'.format(
        get_largest_prime_factor(100)))
    print('Largest prime factor of 1000: {}'.format(
        get_largest_prime_factor(1000)))
    print('Largest prime factor of 13195: {}'.format(
        get_largest_prime_factor(13195)))


def main():
    """ Main function """
    bignumber = 600851475143
    print('Largest prime factor of {}: {}'.format(
        bignumber, get_largest_prime_factor(bignumber)))

if __name__ == "__main__":
    test()
    main()
