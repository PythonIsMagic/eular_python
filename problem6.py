"""Eular Problem 6 - Sum square difference:
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
"""
import timer
from toolkit import sum_of_squares, square_of_sum

DESC = 'Sum square difference'
SOLUTION = 25164150


@timer.timeit
def solve():
    upto = 100
    sum_of_sq = sum_of_squares(upto)
    sq_of_sum = square_of_sum(upto)

    return abs(sq_of_sum - sum_of_sq)
