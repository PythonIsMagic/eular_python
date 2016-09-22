#!/usr/bin/env python3
import primes


def sum_via_iteration(n):
    prime_sum = 0
    for i in range(n):
        if primes.isprime_2step(i):
            prime_sum += i
    return prime_sum


def sum_via_sieve(n):
    prime_sum = 0

    set_of_primes = primes.sieve_rm_method(n - 1)
    for p in set_of_primes:
        prime_sum += p
    return prime_sum

if __name__ == "__main__":
    upperlimit = 2000000
    prime_sum = primes.sieve_rm_method(upperlimit)
    print('The sum of all primes up to {} = {}'.format(upperlimit, prime_sum))
