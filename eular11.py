# coding=utf-8

import recursion
import matrix


def find_greatest_product(_matrix, factors):
    greatest_product = 0
    lines = matrix.scan_matrix_lines(_matrix)

    for sequence in lines:
        endpoint = len(sequence) - factors
        #  print('List: {}'.format(sequence))
        if len(sequence) < factors:
            continue
        i = 0
        while i <= endpoint:
            product = recursion.multiply(sequence, i, factors)
            #  print('\tProduct: {}'.format(product))
            if product > greatest_product:
                greatest_product = product
            i += 1

    return greatest_product


if __name__ == "__main__":
    print('Eular problem #11')
    m = matrix.read_matrix('matrix1.txt')
    p = find_greatest_product(m, 4)
    print('The greatest product in the is {}'.format(p))
