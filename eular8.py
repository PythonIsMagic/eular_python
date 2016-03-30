#!/usr/bin/env python

""" Find the 13 adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?  """

from __future__ import print_function


def main():
    """ Main """
    print("Eular problem 8:")
    filename = 'eular8.txt'
    # Read file line-by-line
    # of = open("eular8.txt")
    # for line in of.readlines():
    # print(line, end='')

    factors = 13
    digit_queue = []
    largest_product = 0

    # Run through all the digits in the number
    with open(filename) as _file:
        while True:
            _char = _file.read(1)
            if not _char:
                print('End of file')
                break

            # Process the character
            try:
                digit_queue.insert(0, int(_char))
            except ValueError:
                pass

            if len(digit_queue) > factors:
                digit_queue.pop()

            if len(digit_queue) == factors:
                product = 1
                print('The product of {}'.format(digit_queue), end='')
                # Product the product from the digits
                for fact in digit_queue:
                    product *= fact

                print(' = {}'.format(product))
                if product > largest_product:
                    largest_product = product

    print('The largest product is {}'.format(largest_product))


if __name__ == "__main__":
    main()
