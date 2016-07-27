"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""


def read_matrix(filename):
    """
    Reads a file containing integers to a matrix(list of lists).
    """
    digits = []

    with open(filename) as f:
        for line in f.readlines():
            ints = [int(n) for n in line.split()]
            digits.append(ints)
    return digits


def print_matrix(matrix):
    _str = ''
    for row in matrix:
        for col in row:
            # Format for 2 digit integers and fill zeros in.
            _str += '{:3}'.format(str(col).zfill(2))
        _str = _str.rstrip() + '\n'
    return _str


def horz_prod(alist, index, factors):
    return get_product(alist, 0, factors)


def get_product(alist, index, factors):
    # Base case:
    if factors == 0:
        print('basecase: {}'.format(alist[index]))
        return alist[index]
    else:
        print('index {}: {}'.format(alist[index]))
        return alist[index] * get_product(alist, index + factors, factors - 1)
