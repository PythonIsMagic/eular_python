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
