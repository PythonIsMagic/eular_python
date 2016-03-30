#!/usr/bin/env python
"""# eular 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""


def isfactorofall(number, upto):
    upto += 1  # offset range upper bound

    for factor in range(1, upto):
        if number % factor != 0:
            return False

    return True


def main():
    upperbound = 20
    print('Testing')

    print("Is 1 divisible by 1-20?")
    print(isfactorofall(1, upperbound))

    print("Is 20 divisible by 1-20?")
    print(isfactorofall(20, upperbound))

    print("Finding a number divisible by all the numbers 1-20")

    # Start at the highest factor we are testing by
    # The number won't be divisible by any numbers larger than it!
    currentnum = upperbound
    while True:
        if isfactorofall(currentnum, upperbound):
            break
        # Increase by the size of the largest factor we are testing by
        # This will dramatically increase the speed and we don't need to test
        # numbers in between since they won't be divisible by that number.
        currentnum += upperbound

    print("{} IS a factor of all 1-20!!!".format(currentnum))

if __name__ == "__main__":
    main()
