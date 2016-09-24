import alphanumbers
import factors
import math


def factorial(n):
    if n <= 0:
        raise ValueError('eular20.factorial(n): n must be a positive integer!')
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def fact_sum(n):
    return sum([int(x) for x in str(math.factorial(100))])


def add_digits(n):
    digits = alphanumbers.num_to_list(n)
    sum = 0
    for d in digits:
        sum += d
    return sum


def d(n):
    """
    Return the sum of the proper divisors of n
    (numbers less than n which divide evenly into n).
    """
    divisors = factors.proper_divisors(n)
    return sum(divisors)


def get_divisor_sums(upto):
    # make a dictionary of divisor sums
    return {n: d(n) for n in range(2, upto)}


def is_amicable(a, b):
    if d(a) == b and d(b) == a:
        return a != b
    else:
        return False


def add_amicable_numbers(upto):
    amicables = set()
    div_sums = get_divisor_sums(upto)

    for k, v in div_sums.items():
        if is_amicable(k, v):
            if k < upto:
                amicables.add(k)

    #  print('{} amicable #s found'.format(len(amicables)))
    #  for n in amicables:
        #  print('{} --> {}'.format(n, div_sums[n]))

    return sum(amicables)


def alphabetical_value(name):
    return sum([ord(x.lower()) - 96 for x in list(name)])


def ispalindrome(number):
    numlist = list(str(number))

    if len(numlist) <= 0:
        return False
    if len(numlist) == 1:
        return True

    i = 0
    while i <= len(numlist) / 2:
        if numlist[i] != numlist[-(i+1)]:
            return False
        i += 1
    else:
        return True


def get_largest_palindrome(lowerlimit, upperlimit):
    largest_palindrome = 0

    for m1 in range(lowerlimit, upperlimit):
        # Start from m1 for this range so we don't hit duplicate factors
        for m2 in range(m1, upperlimit):
            product = m1 * m2
            if ispalindrome(product):
                # print("Found palindrome!: {}".format(product))
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome


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


# Generator
def triangle_num():
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x
