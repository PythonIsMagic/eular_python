
"""Eular Problem 8 - Largest product in a series:
    Find the 13 adjacent digits in the 1000-digit number that have the
    greatest product.  What is the value of this product?
"""
from . import timer

DESC = 'Largest product in a series'
SOLUTION = 23514624000


@timer.timeit
def solve():
    FACTORS = 13
    filename = 'data/eular8.txt'
    digits = read_file_to_list(filename)
    return find_product_in_list(digits, FACTORS)


def calculate_product(alist):
    """ Returns the product of a list of numbers. """
    product = 1
    for fact in alist:
        product *= fact
    return product


def read_file_to_list(filename):
    """ Reads a file containing digits(or a big number) and converts it to a
        list of individual.
    """
    digits = []
    with open(filename) as _file:
        while True:
            _char = _file.read(1)
            if not _char:  # End of file
                break
            else:
                try:
                    digits.append(int(_char))
                except ValueError:
                    pass
    return digits


def find_product_in_list(alist, factors):
    """ Takes in a list of digits and finds the greatest possible product of x
        factors.
    """
    largest_product = 0
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
