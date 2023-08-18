# -*- coding: utf-8 -*-
"""Eular Problem 11 - Largest product in a grid:
    In the 20×20 grid below, four numbers along a diagonal line have been
    marked in red. What is the greatest product of four adjacent numbers in
    the same direction(up, down, left, right, or diagonally) in the 20×20 grid?
"""
from src import timer
from src.toolkit import DATADIR
from src.toolkit import find_greatest_product, read_matrix

DESC = 'Largest product in a grid'
SOLUTION = 70600674


@timer.timeit
def solve():
    m = read_matrix(DATADIR + 'matrix1.txt')
    return find_greatest_product(m, 4)
