#!/usr/bin/env python
"""
++ Eular Problem3
*Largest Prime Factor*
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600,851,475,143 ?
"""

import primes


def main():
    """ Main function """
    bignumber = 600851475143
    print('Largest prime factor of {}: {}'.format(
        bignumber, primes.max_prime_factor(bignumber)))

if __name__ == "__main__":
    main()
