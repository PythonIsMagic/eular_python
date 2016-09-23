import alphanumbers
import math


def factorial(n):
    if n <= 0:
        raise ValueError('eular20.factorial(n): n must be a positive integer!')
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def add_digits(n):
    digits = alphanumbers.num_to_list(n)
    sum = 0
    for d in digits:
        sum += d
    return sum


def fact_sum(n):
    return sum([int(x) for x in str(math.factorial(100))])
