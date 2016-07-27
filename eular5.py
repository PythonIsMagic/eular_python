#!/usr/bin/env python
"""# eular 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""


def isfactorofall(number, upto):
    for factor in range(1, upto + 1):
        if number % factor != 0:
            return False
    return True


def num_div_by_all_upto(upto):
    # Start at the highest factor we are testing by
    # The number won't be divisible by any numbers larger than it!
    currentnum = upto
    while True:
        if isfactorofall(currentnum, upto):
            break

        # Increase by the size of the largest factor we are testing by
        # This will dramatically increase the speed and we don't need to test
        # numbers in between since they won't be divisible by that number.
        currentnum += upto
    return currentnum

if __name__ == "__main__":
    testrange = 20
    n = num_div_by_all_upto(testrange)

    print('Finding a number divisible by all the numbers 1-{}'.format(testrange))
    print("{} is a factor of all 1-{}!".format(n, testrange))
