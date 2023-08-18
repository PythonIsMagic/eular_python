
"""Eular Problem 8 - Largest product in a series:
    Find the 13 adjacent digits in the 1000-digit number that have the
    greatest product.  What is the value of this product?
"""
import timer
from toolkit import read_file_to_list, find_product_in_list

DESC = 'Largest product in a series'
SOLUTION = 23514624000


@timer.timeit
def solve():
    FACTORS = 13
    filename = 'data/eular8.txt'
    digits = read_file_to_list(filename)
    return find_product_in_list(digits, FACTORS)
