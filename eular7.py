#!/usr/bin/env python

import primes


def main():
    print('Eular 7')
    targetprime = 10001

    print('Prime #{} = {}'.format(targetprime, primes.getprime(targetprime)))

if __name__ == "__main__":
    main()
