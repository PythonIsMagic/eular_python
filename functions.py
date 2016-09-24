import alphanumbers
import math
import primes


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
    divisors = proper_divisors(n)
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


def bruteforce(n):
    """
    Returns a set of all the divisors of n using a brute force check.  We only need to check up
    to (n/2) for any n, bc n won't be divisible by anything larger than that. We can also skip
    checking even divisors for odd numbers, since they won't be divisible - this should speed up
    the checking a little. But this is still pretty slow for numbers over a million.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')

    factors = set()
    middle = n // 2

    if n % 2 == 0:  # It's even
        for i in range(1, middle + 1):
            if n % i == 0:
                factors.add(i)
    else:
        # It's odd (skip checking even factors)
        for i in range(1, middle + 1, 2):
            if n % i == 0:
                factors.add(i)

    # n will ALWAYS be a factor of itself.
    factors.add(n)
    return factors


def divisors(n):
    """
    Creates a list of all the factors of n and returns them as a set. First we get the prime
    factors of n. To get any remaining factors, we take all the prime factors and take each to
    it's maximum power. This results in a list of factors we can use to build the remaining
    factors.
    """
    if n < 1:
        raise ValueError('factors.divisors(n): n needs to be a positive integer')
    elif n == 1:
        return {1}

    prime_facts = primes.get_prime_factors(n)
    if prime_facts is None:
        return None

    factors = list(prime_facts)

    for x in factors:
        for y in factors:
            product = y * x

            if n % product == 0 and product not in factors:
                factors.append(product)

    # Cutting out 1 saves a lot of checks and is a factor of every positive number.
    factors.append(1)
    return set(factors)


def proper_divisors(n):
    """
    Return a set containing the proper divisors of n (numbers less than n which divide evenly
    into n).
    """
    d = divisors(n)
    d.remove(n)
    return d


def test_fromprime(n):
    failures = 0

    for i in range(1, n):
        bf = bruteforce(i)
        fp = divisors(i)

        if bf != fp:
            print('Test failed on {}!'.format(i))
            print('bruteforce: {}'.format(sorted(bf)))
            print('fromprime:  {}'.format(sorted(fp)))
            failures += 1
        else:
            print('{} - Check.'.format(i))

    if failures > 0:
        print('{} out of {} tests failed.'.format(failures, n - 1))
    else:
        print('All tests passed! (up to {})'.format(n))


def is_abundant(n):
    return sum(proper_divisors(n)) > n


def sum_multiples(factorlist, limit):
    # Returns the sum of the specificed multiples.
    return sum([is_multiple_of(i, factorlist) for i in range(limit)])


def is_multiple_of(num, factorlist):
    if 0 in factorlist:
        raise ValueError('0 is not valid in list of factors!')

    for n in factorlist:
        if num % n == 0:
            return True
    else:
        return False


def isfactorofall(number, upto):
    for factor in range(1, upto + 1):
        if number % factor != 0:
            return False
    return True


def num_div_by_all_upto(upto):
    # Start at the highest factor we are testing by
    # The number won't be divisible by any numbers larger than it!
    currentnum = upto
    while True:
        if isfactorofall(currentnum, upto):
            break

        # Increase by the size of the largest factor we are testing by
        # This will dramatically increase the speed and we don't need to test
        # numbers in between since they won't be divisible by that number.
        currentnum += upto
    return currentnum
