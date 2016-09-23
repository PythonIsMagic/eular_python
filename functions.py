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


def add_digits(n):
    digits = alphanumbers.num_to_list(n)
    sum = 0
    for d in digits:
        sum += d
    return sum


def fact_sum(n):
    return sum([int(x) for x in str(math.factorial(100))])


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
