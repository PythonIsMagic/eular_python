# encoding=utf-8
"""
++ Eular25

*The Fibonacci sequence*
    is defined by the recurrence relation:
        F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

    The 12th term, F_12, is the first term to contain three digits.
    What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import eular2

if __name__ == "__main__":
    print('Eular Problem 25:')

    for i, x in enumerate(eular2.fibonacci()):
        if len(str(x)) >= 1000:
            print('Term {} has over 1000 digits!'.format(i+1))
            break
