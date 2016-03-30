#!/usr/bin/env python3
"""
*Largest palindrome product* A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit numbers is 9009 = 91 Ã—
99. Find the largest palindrome made from the product of two 3-digit numbers.
"""

# from __future__ import print_function


def ispalindrome(number):
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
    else:
        return True


def get_largest_palindrome(lowerlimit, upperlimit):
    largest_palindrome = 0

    for m1 in range(lowerlimit, upperlimit):
        # Start from m1 for this range so we don't hit duplicate factors
        for m2 in range(m1, upperlimit):
            product = m1 * m2
            if ispalindrome(product):
                # print("Found palindrome!: {}".format(product))
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome


def test():
    # Test the basic boundary conditions
    print("Test!")
    print("ispalindome('')")
    print(ispalindrome(''))

    print("ispalindome(1)")
    print(ispalindrome(1))

    print("ispalindome(11)")
    print(ispalindrome(11))

    print("ispalindome(12)")
    print(ispalindrome(12))

    print("ispalindome(111)")
    print(ispalindrome(111))

    print("ispalindome(121)")
    print(ispalindrome(121))

    print("ispalindome(112)")
    print(ispalindrome(112))

    print("ispalindome(1111)")
    print(ispalindrome(1111))

    print("ispalindome(2112)")
    print(ispalindrome(2112))

    print("ispalindome(1234)")
    print(ispalindrome(1234))
    # print("ispalindome(1) = {}".format(str(ispalindrome(1))))


def main():
    print('Calculating the largest palindrome producable between the factors' +
          ' of 10 and 100')
    print(get_largest_palindrome(10, 100))

    print('Calculating the largest palindrome producable between the factors' +
          ' of 100 and 1000')
    print(get_largest_palindrome(100, 1000))


if __name__ == "__main__":
    main()
