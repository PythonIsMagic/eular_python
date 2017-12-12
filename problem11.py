# -*- coding: utf-8 -*-
"""Eular Problem 11 - Largest product in a grid:
    In the 20×20 grid below, four numbers along a diagonal line have been
    marked in red. What is the greatest product of four adjacent numbers in
    the same direction(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import recursion
import timer

DESC = 'Largest product in a grid:'
SOLUTION = 70600674


def extract_line(matrix, point, xyincrement):
    """ Takes an x by x matrix and scans a matrix for a list of items.

        Uses a starting point tuple (x, y) and an increment tuple(x-increment, y-increment).
        Starts the list from the x, y coordinate and goes in the increments given by xinc and yinc.
    """
    x, y = point[0], point[1]
    xinc, yinc = xyincrement[0], xyincrement[1]
    items = []

    while x >= 0 and y >= 0 \
            and x < len(matrix) and y < len(matrix):
        items.append(matrix[y][x])
        x += xinc
        y += yinc
    return items


def find_greatest_product(_matrix, factors):
    """ Finds the greatest product of (x * factors) adjacent integers in a matrix. """
    greatest_product = 0
    lines = scan_matrix_lines(_matrix)

    for sequence in lines:
        endpoint = len(sequence) - factors
        if len(sequence) < factors:
            continue
        i = 0
        while i <= endpoint:
            product = recursion.multiply(sequence, i, factors)
            if product > greatest_product:
                greatest_product = product
            i += 1

    return greatest_product


def get_rows(matrix):
    rows = []
    for i in range(len(matrix)):
        point = (0, i)
        inc = (1, 0)
        rows.append(extract_line(matrix, point, inc))
    return rows


def get_columns(matrix):
    cols = []
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (0, 1)
        cols.append(extract_line(matrix, point, inc))
    return cols


def get_right_diagonals(matrix):
    """ Extracts all the right-facing diagonal lines of a matrix and returns
        them as a list.
    """

    diags = []

    # Scan right diagonals: bottom left to top left.
    for i in range(len(matrix) - 1, 0, -1):
        point = (0, i)
        inc = (1, 1)
        diags.append(extract_line(matrix, point, inc))

    # Scan right diagonals: top left to top right
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (1, 1)
        diags.append(extract_line(matrix, point, inc))

    return diags


def get_left_diagonals(matrix):
    """ Extracts all the left-facing diagonal lines of a matrix and returns them
        as a list.
    """
    diags = []
    # Scan left diagonals: top left to top right
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (-1, 1)
        diags.append(extract_line(matrix, point, inc))

    # Scan left diagonals: top right to bottom right
    for i in range(1, len(matrix)):
        point = (len(matrix) - 1, i)
        inc = (-1, 1)
        diags.append(extract_line(matrix, point, inc))
    return diags


def read_matrix(filename):
    """ Reads a file containing integers to a matrix(list of lists). """
    digits = []

    with open(filename) as f:
        for line in f.readlines():
            ints = [int(n) for n in line.split()]
            digits.append(ints)
    return digits


def scan_matrix_lines(matrix):
    """ Scans for all rows, columns, and diagonals in the given matrix and
        returns them as a list of lists.
    """
    lines = []
    lines.extend(get_rows(matrix))
    lines.extend(get_columns(matrix))
    lines.extend(get_right_diagonals(matrix))
    lines.extend(get_left_diagonals(matrix))
    return lines


def print_matrix(matrix):
    _str = ''
    for row in matrix:
        for col in row:
            # Format for 2 digit integers and fill zeros in.
            _str += '{:3}'.format(str(col).zfill(2))
        _str = _str.rstrip() + '\n'
    return _str


@timer.timeit
def solve():
    m = read_matrix('data/matrix1.txt')
    return find_greatest_product(m, 4)
