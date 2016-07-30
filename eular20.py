"""
*Factorial digit sum*
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""

import eular17


def factorial(n):
    pass


def add_digits(n):
    digits = eular17.num_to_list(n)
    pass

if __name__ == "__main__":
    print('Eular Problem #10: Factorial Digit Sum')
    fact = factorial(100)
    print('The factorial of 100! = {}'.format(fact))
    print('The sum of the digits in {} = {}'.format(fact, add_digits(fact)))
