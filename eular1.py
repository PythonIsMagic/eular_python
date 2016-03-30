#!/usr/bin/env python
"""
Eular problem 1:
If we list all the natural numbers below 10 that are

multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import unittest


def sum_multiples(factorlist, limit):
    """
    Returns the sum of the specificed multiples.
    """

    result = 0

    # Go through all numbers up to 1000
    for i in range(limit):
        if is_multiple_of(i, factorlist):
            result += i

    return result


def is_multiple_of(dividend, factorlist):
    if factorlist == []:
        raise ValueError()

    for n in factorlist:
        if dividend % n == 0:
            return True
    else:
        return False


class TestEular1(unittest.TestCase):
    def test_ismultipleof_emptylist_throwException(self):
        self.assertRaises(ValueError, is_multiple_of, 10, [])

    def test_ismultipleof_1with1_ReturnTrue(self):
        expected = True
        result = is_multiple_of(1, [1])
        self.assertEqual(expected, result)

    def test_ismultipleof_2of4_ReturnTrue(self):
        expected = True
        result = is_multiple_of(4, [2])
        self.assertEqual(expected, result)

if __name__ == "__main__":
    factors = [3, 5]
    UPTO = 1000
    result = sum_multiples(factors, UPTO)
    print('Sum of all multiples of 3 and 5 up to 1000 is {}'.format(result))
