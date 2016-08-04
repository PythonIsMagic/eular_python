# coding=utf-8
"""
Eular Problem14

*Longest Collatz sequence*
    The following iterative sequence is defined for the set of positive integers:
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz
    Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def next_collatz(n):
    # To make the function more efficient, I will stay with the true definition of the problem
    # and passing 1 will return 4 (3*1 + 1). The calling function will have to track when the
    # end of the sequence has been reached.
    if n < 1:
        raise ValueError('eular14.next_collatz: n must be a positive integer.!')
    elif n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def collatz_seq(n, collatz_dict={}):
    #  pdb.set_trace()
    if n < 1:
        raise ValueError('eular14.collatz_seq: n must be a positive integer.!')

    #  print('\n****** COLLATZ SEQ for {}'.format(n))
    seq = [n]
    while n > 1:
        n = next_collatz(n)
        if n in collatz_dict:
            #  print('found shortcut in {}!'.format(n))
            seq.extend(collatz_dict[n])
            collatz_dict[seq[0]] = seq
            #  print(seq)
            return seq
        else:
            seq.append(n)

    collatz_dict[seq[0]] = seq
    print(seq)
    return seq


def longest_collatz_seq(upto):
    collatz_dict = {}
    n = 0
    n_len = 0

    for i in range(1, upto):
        seq = collatz_seq(i, collatz_dict)
        if len(seq) > n_len:
            n = i
            n_len = len(seq)
            print('New longest seq! {}, for a sequence {} steps long.'.format(n, n_len))
    print('\n\n')
    print('The longest collatz sequence under {} starts with the number {}'.format(upto, n))
    print('which has a length of {}'.format(n_len))
    print('')
    print('The collatz_dict ended up with a length of {} entries.'.format(len(collatz_dict)))

if __name__ == "__main__":
    longest_collatz_seq(1000000)
