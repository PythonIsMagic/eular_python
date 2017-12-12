"""Eular Problem 9 - Special Pythagorean triplet:
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product a * b * c.
"""

import math
import timer

DESC = 'Special Pythagorean triplet:'
SOLUTION = 31875000


def adds_to_1000(a, b, c):
    if a + b + c == 1000:
        return True
    else:
        return False


def find_ab(a, b, c, squares):
    #  print('find_ab({}, {}, {}, squares)'.format(a, b, c))
    print('find_ab({} + {} = {}?'.format(squares[a], squares[b], squares[c]))
    # base case:
    if is_pythagorean_triplet(squares[a], squares[b], squares[c]) and b != c:
        print('Base case encountered.')
        return squares[a], squares[b], squares[c]
    elif a == c - 2 and b == c - 1:
        print('No pythagorean triplet found for {}^2.'.format(squares[c]))
        return None
    elif b < c:
        return find_ab(a, b + 1, c, squares)
    else:
        a = a + 1
        return find_ab(a, a + 1, c, squares)


def is_pythagorean_triplet(a2, b2, c2):
    if a2 + b2 == c2:
        return True
    else:
        return False


def iterative_solution():
    """ Finds the Pythagorean triplet that adds to 1000. """
    MAX = 1000
    squares = square_list(MAX)

    for a in range(1, MAX):
        for b in range(a + 1, MAX):
            ab = a ** 2 + b ** 2
            c = int(math.sqrt(ab))
            if a + b + c > MAX:
                continue

            if ab in squares:
                #  print('{} + {} + {} == 1000?'.format(a, b, c))
                if adds_to_1000(a, b, c):
                    return a, b, c


def recursive_solution():
    """ Recursive solution to eular9 """
    # We probably won't need any squares above 500.
    squares = square_list(500)

    # Start with c^2, and try to determine a and b from c^2.
    for c in range(2, len(squares)):

        if c + (c - 1) + (c - 2) < 1000:
            continue
        # Check if there is a perfect pythagorean triplet for c
        abc = find_ab(0, 1, c, squares)

        # If something other than None is returns, there is a triplet
        if abc is not None:
            a, b, c = abc[0], abc[1], abc[2]

            # Check if they add to 1000
            if adds_to_1000(a, b, c):
                return abc
            else:
                print('{} + {} + {} != 1000'.format(a, b, c))


def square_list(upto):
    return [x ** 2 for x in range(upto)]


@timer.timeit
def solve():
    a, b, c = iterative_solution()
    return a * b * c
