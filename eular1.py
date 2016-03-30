#!/usr/bin/env python
"""
Eular problem 1:
If we list all the natural numbers below 10 that are

multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    # Declare constants
    UPPERLIMIT = 1000
    MULTIPLE1 = 3
    MULTIPLE2 = 5

    # Initialize the sum variable
    sum = 0

    # Go through all numbers up to 1000
    for i in range(UPPERLIMIT):
        # If the current number is a multiple of 3 or 5, add it to the sum
        if i % MULTIPLE1 == 0 or i % MULTIPLE2 == 0:
            sum += i

    # Display the sum of all the correct multiples.
    print(sum)

if __name__ == "__main__":
    main()
