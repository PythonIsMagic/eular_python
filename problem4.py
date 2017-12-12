"""Eular problem 4 -
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

import timer

DESC = 'Largest palindrome product'
SOLUTION = 906609


def is_palindrome(number):
    """ Returns True if the variable passed is a palindrome, False otherwise.  """
    numlist = list(str(number))

    if len(numlist) <= 0:
        return False
    if len(numlist) == 1:
        return True

    i = 0
    while i <= len(numlist) / 2:
        if numlist[i] != numlist[-(i+1)]:
            return False
        i += 1
    return True


def largest_palindrome(lowerlimit, upperlimit):
    """ Finds the largest palindrome in the given integer limits. """
    largest = 0

    for m1 in range(lowerlimit, upperlimit):
        # Start from m1 for this range so we don't hit duplicate factors
        for m2 in range(m1, upperlimit):
            product = m1 * m2
            if is_palindrome(product):
                if product > largest:
                    largest = product
    return largest


@timer.timeit
def solve():
    return largest_palindrome(100, 1000)
