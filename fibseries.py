#!/usr/bin/env python
"""
Module for generating Fibonacci numbers
"""


def fibonacci(limit=None):
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


def fibtest():
    # the sum of two elements defines the next
    T1, T2 = 0, 1

    while T2 < 100:
        print(T2)
        T1, T2 = T2, T1+T2
        # or a = b and b = a+b

    T1, T2 = 0, 1
    while T2 < 100:
        print(T2,)
        T1, T2 = T2, T1+T2
        # or a = b and b = a+b
