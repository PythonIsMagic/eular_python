#!/usr/bin/env python
"""
Eular problem 2:
Each new term in the Fibonacci sequence is generated

by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 4
million, find the sum of the even-valued terms.
"""


def fibonacci():
    a, b = 0, 1
    while(True):
        a, b = b, a + b
        yield a


def calc_sum_of_evens(upto):
    sum = 0

    for x in fibonacci():
        if x > upto:
            break
        #  print(x)

        # Test if the current fib # is even and if so, add it to the sum.
        if x % 2 == 0:
            sum += x

    return sum


if __name__ == "__main__":
    UPPERLIMIT = 4000000
    sum = calc_sum_of_evens(UPPERLIMIT)
    print('The sum of all even numbered Fibonacci numbers up to 4000000 = {}'.format(sum))
