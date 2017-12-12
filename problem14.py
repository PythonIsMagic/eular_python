"""Eular Problem 14 -
    Which starting number, under one million, produces the longest Collatz
    chain?
"""

import timer

DESC = 'Longest Collatz sequence:'
SOLUTION = 837799


def collatz_seq(n, collatz_dict={}):
    """ Takes an integer n and returs the resulting Collatz sequence as a list. """
    seq = [n]
    while n > 1:
        n = next_collatz(n)
        if n in collatz_dict:
            seq.extend(collatz_dict[n])
            collatz_dict[seq[0]] = seq
            return seq
        else:
            seq.append(n)

    collatz_dict[seq[0]] = seq
    print(seq)
    return seq


def next_collatz(n):
    """ Takes an integer n and returns the following integer in the Collatz sequence.

        If n is even, it returns n divided by 2.
        If n is odd, it returns (3*n) + 1.

        The end of a collatz sequence is traditionally 1, so we will raise an
        exception if the n passed is 1.
    """
    if n <= 1:
        raise ValueError('eular14.next_collatz: n must be a positive integer larger than 1!')
    elif n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def longest_collatz_seq(upto):
    """ Finds the longest collatz sequence in all the integers 0 to the upto
        integer passed and returns it as a list.
    """
    collatz_dict, longestseq = {}, []

    for i in range(1, upto):
        seq = collatz_seq(i, collatz_dict)
        if len(seq) > len(longestseq):
            longestseq = seq
    return longestseq


@timer.timeit
def solve():
    upto = 1000000
    longest_seq = longest_collatz_seq(upto)
    return longest_seq[0]
