#!/usr/bin/env python3
""" Eular 9 """

import math


def square_list(upto):
    return [x ** 2 for x in range(upto)]


def main():
    """ Main """
    squares = square_list(1000)

    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            ab = a ** 2 + b ** 2
            c = math.sqrt(ab)
            if a + b + c > 1000:
                continue

            if ab in squares:
                if a + b + c == 1000:
                    print('a^2 + b^2 = c^2')
                    print('{} + {} = {}'.format(a**2, b**2, ab))
                    print('a + b + c = 1000')
                    print('{} + {} + {} = 1000!'.format(a, b, c))
                    print('The product abc = {}'.format(a*b*c))

if __name__ == "__main__":
    main()
