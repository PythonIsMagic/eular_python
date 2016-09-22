#!/usr/bin/env python

def sum_of_squares(upto):
    total = 0
    for i in range(upto+1):
        total += i ** 2
    return total


def square_of_sum(upto):
    total = 0
    for i in range(upto + 1):
        total += i
    return total ** 2


def main():
    print('Eular6')
    print('sum of squares(100) = {}'.format(sum_of_squares(100)))
    print('square of sums(100) = {}'.format(square_of_sum(100)))
    difference = abs(square_of_sum(100) - sum_of_squares(100))

    print('The difference between the sum of the squares of the first 100 ' +
          'numbers and the square of the sum is {}'.format(difference))

if __name__ == "__main__":
    main()
