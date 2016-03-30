#!/usr/bin/env python

import eular3


def getprime(index):
    currentprime = 1
    i = 0
    while currentprime <= index:
        i += 1
        if eular3.is_prime(i):
            currentprime += 1
    else:
        return i


def test():
    for prime in range(10):
        print('Prime #{} = {}'.format(prime, getprime(prime)))


def main():
    print('Eular 7')
    targetprime = 10001
    # test()

    print('Prime #{} = {}'.format(targetprime, getprime(targetprime)))

if __name__ == "__main__":
    main()
