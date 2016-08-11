"""
++ Eular23

*Non-abundant sums*

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""
from __future__ import print_function
import factors


def is_abundant_sum(n):
    pass


def sum_non_abundant(LIMIT):
    pass


if __name__ == "__main__":
    print('Eular project 25')
    LIMIT = 28123
    abundants = []
    print('Listing all abundant numbers up to {}:'.format(LIMIT))
    for i in range(1, LIMIT + 1):
        if factors.is_abundant(i):
            #  print(i, end=' ')
            abundants.append(i)

    print('Total of {} abundant numbers from 1-{}'.format(len(abundants), LIMIT))
    print('The max abundant # = {}'.format(max(abundants)))
    print('The min abundant # = {}'.format(min(abundants)))
    sums = set()
    #  for i in range(0, len(abundants)):
        #  for j in range(i, len(abundants)):
            #  sums.add(abundants[i] + abundants[j])

    for i, a in enumerate(abundants):
        for b in range(i, len(abundants)):
            sums.add(a + abundants[b])

    print('Found {} sums.'.format(len(sums)))
    print('The max sum = {}'.format(max(sums)))
    print('The min sum = {}'.format(min(sums)))

    unsummable = set()
    for i in range(LIMIT + 1):
        if i not in sums:
            unsummable.add(i)

    for i in range(30):
        if i in unsummable:
            print('{} cannot be written as a sum of 2 abundant #s.'.format(i))

    print('There are {} unsummable #s.'.format(len(unsummable)))
    print('sum of all positive ints which can\'t be summed by 2 abundants={}.'.format(
        sum(unsummable)))
