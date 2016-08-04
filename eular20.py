#!/usr/bin/env python3
# coding=utf-8
"""
*Factorial digit sum*
    n! means n × (n − 1) × ... × 3 × 2 × 1
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""

import eular17
import math


def factorial(n):
    if n <= 0:
        raise ValueError('eular20.factorial(n): n must be a positive integer!')
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def add_digits(n):
    digits = eular17.num_to_list(n)
    sum = 0
    for d in digits:
        sum += d
    return sum


def fact_sum(n):
    return sum([int(x) for x in str(math.factorial(100))])


if __name__ == "__main__":
    print('Eular Problem #10: Factorial Digit Sum')
    fact = factorial(100)
    print('The factorial of 100! = {}'.format(fact))
    print('The sum of the digits in {} = {}'.format(fact, add_digits(fact)))
    print('or using the super shorted version: {}'.format(fact_sum(100)))
