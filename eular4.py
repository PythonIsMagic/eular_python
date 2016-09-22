#!/usr/bin/env python3
# coding=utf-8


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


def main():
    print('Calculating the largest palindrome producable between the factors' +
          ' of 10 and 100')
    print(get_largest_palindrome(10, 100))

    print('Calculating the largest palindrome producable between the factors' +
          ' of 100 and 1000')
    print(get_largest_palindrome(100, 1000))


if __name__ == "__main__":
    main()
