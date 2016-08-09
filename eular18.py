#!/usr/bin/env python3

"""
++ Eular18
*Maximum path sum I*

    By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from top to
    bottom is 23.

    3
    7 4
    2 4 6

Find the maximum total from top to bottom of the triangle below:
"""

import eular11

if __name__ == "__main__":
    tree = eular11.read_matrix('number_tree.txt')
    print(eular11.print_matrix(tree))
