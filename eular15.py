#!/usr/bin/env python3

"""
Eular15

*Lattice paths*

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


# Assume a square matrix
def set_paths(row, col, size):
    paths = []
    if row < size - 1:
        paths.append('>')
    if col < size - 1:
        paths.append('V')
    return paths


def lattice_matrix(size):
    return [[set_paths(row, col, size + 1) for row in range(size + 1)]
            for col in range(size + 1)]


def print_matrix(matrix):
    _str = ''
    for row in matrix:
        for col in row:
            _str += '{}'.format(str(col))
        _str = _str.rstrip() + '\n'
    return _str


if __name__ == "__main__":
    LENGTH = 5
    matrix5 = lattice_matrix(5)
    print(print_matrix(matrix5))

    x, y = 0, 0
    end = LENGTH
    paths = []

    while x < LENGTH and y < LENGTH:
        # increase x first

        # increase y

        pass
