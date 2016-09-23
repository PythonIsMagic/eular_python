# coding=utf-8
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
