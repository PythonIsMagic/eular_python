#!/usr/bin/env python
""" Module for generating Fibonacci numbers """


def main():
    # the sum of two elements defines the next
    T1, T2 = 0, 1

    while T2 < 100:
        print T2
        T1, T2 = T2, T1+T2
        # or a = b and b = a+b

    T1, T2 = 0, 1
    while T2 < 100:
        print T2,
        T1, T2 = T2, T1+T2
        # or a = b and b = a+b

if __name__ == "main":
    main()
