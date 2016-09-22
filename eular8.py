#!/usr/bin/env python

from __future__ import print_function


def read_file_to_list(filename):
    """
    Reads a file containing digits to a list.
    * Reads until the end of file.
    * Only adds digits to the list, ignores other characters.
    """
    digits = []
    # Run through all the digits in the number
    with open(filename) as _file:
        while True:
            _char = _file.read(1)
            if not _char:
                #  print('End of file')
                break
            else:
                # Only add integers
                try:
                    digits.append(int(_char))
                except ValueError:
                    pass
    return digits


def find_product_in_list(alist, factors):
    largest_product = 0
    # Set the endpoints, 0 and 12

    # Ending point = size - (FACTORS - 1)
    end = len(alist) - (factors - 1)

    # Iterate through the list until we get to the ending point
    n = 0
    while n < end:
        # For each point, calculate the product.
        list_slice = alist[n: n + factors]
        product = calculate_product(list_slice)
        if product > largest_product:
            largest_product = product
        n += 1
    return largest_product


def calculate_product(alist):
    # Performs the check for 0's once!
    if 0 in alist:
        return 0

    product = 1
    for fact in alist:
        product *= fact
    return product


def find_product_via_queue(filename):
    FACTORS = 13
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

            if len(digit_queue) > FACTORS:
                digit_queue.pop()

            if len(digit_queue) == FACTORS:
                product = calculate_product(digit_queue)
                print(' = {}'.format(product))
                if product > largest_product:
                    largest_product = product

    return largest_product


if __name__ == "__main__":
    #  largest_product = find_product_via_queue()
    FACTORS = 13
    print("Eular problem 8:")
    filename = 'eular8.txt'

    print('Reading file')
    digits = read_file_to_list('eular8.txt')

    p = find_product_in_list(digits, FACTORS)
    print('The largest product is {}'.format(p))
