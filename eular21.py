#!/usr/bin/env python3
# coding=utf-8
import factors


def d(n):
    """
    Return the sum of the proper divisors of n
    (numbers less than n which divide evenly into n).
    """
    divisors = factors.proper_divisors(n)
    return sum(divisors)


def get_divisor_sums(upto):
    # make a dictionary of divisor sums
    return {n: d(n) for n in range(2, upto)}


def amicable(a, b):
    if d(a) == b and d(b) == a:
        return a != b
    else:
        return False

if __name__ == "__main__":
    LIMIT = 10000
    amicable_sum = 0
    amicables = set()
    div_sums = get_divisor_sums(LIMIT)

    for k, v in div_sums.items():
        if amicable(k, v):
            if k < LIMIT:
                amicables.add(k)

    print('{} amicable #s found'.format(len(amicables)))

    for n in amicables:
        print('{} --> {}'.format(n, div_sums[n]))

    # Add all of the amicable numbers together
    print('The sum of all amicables #s up to {} = {}'.format(LIMIT, sum(amicables)))
