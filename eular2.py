#!/usr/bin/env python
"""
Eular problem 2:
Each new term in the Fibonacci sequence is generated

by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence

whose values do not exceed
4 million, find the sum of the even-valued terms.
"""


def main():
    UPPERLIMIT = 4000000
    sum = 0

    # Define first 2 Fibonacci numbers
    A = 0
    B = 1

    while (B < UPPERLIMIT):
        # Test if the current fib # is even and if so, add it to the sum.
        if B % 2 == 0:
            print("Even Pibonacci # %d" % B)
            sum += B

        # Advance the fib #
        A, B = B, A + B
        # B, A = B + A, B

    print("The sum is %d" % sum)

if __name__ == "__main__":
    main()
