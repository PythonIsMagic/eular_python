import math


def factorial(n):
    """
    Returns the factorial of n.
    """
    if n <= 0:
        raise ValueError('eular20.factorial(n): n must be a positive integer!')
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


def fact_sum(n):
    """
    Returns the sum of the integers in the factorial of n.
    """
    return sum([int(x) for x in str(math.factorial(100))])


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n(numbers less than n which divide evenly into n).
    """
    divisors = proper_divisors(n)
    return sum(divisors)


def divisor_sum_dict(upto):
    # make a dictionary of divisor sums
    return {n: sum_proper_divisors(n) for n in range(2, upto)}


def is_amicable(a, b):
    """
    Determines if integers and b are amicable numbers. Returns True if they are, False otherwise.
    """
    if sum_proper_divisors(a) == b and sum_proper_divisors(b) == a:
        return a != b
    else:
        return False


def add_amicable_numbers(upto):
    """
    Adds all the amicable numbers up to upto and returns the sum.
    """
    amicables = set()
    div_sums = divisor_sum_dict(upto)

    for k, v in div_sums.items():
        if is_amicable(k, v):
            if k < upto:
                amicables.add(k)

    return sum(amicables)


def alphabetical_value(name):
    """
    Returns the sum of the alphabetical values of the string passed. Each letter is equal to it's
    position in the alphabet.
    Example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
    """
    return sum([ord(x.lower()) - 96 for x in list(name)])


def ispalindrome(number):
    """
    Determines if the value passed is a palindrome or not.
    """
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
    """
    Finds the largest palindrome in the given integer limits.
    """
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
    """
    Defines a Fibonacci number generator. The sequence returned is [1, 1, 2, 3, 5] and so on
    as the sequence progresses.
    """
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


def next_collatz(n):
    """
    Takes an integer n and returns the following integer in the Collatz sequence.

    If n is even, it returns n divided by 2.
    If n is odd, it returns (3*n) + 1.

    The end of a collatz sequence is traditionally 1, so we will raise an exception if the n
    passed is 1.
    """
    if n <= 1:
        raise ValueError('eular14.next_collatz: n must be a positive integer larger than 1!')
    elif n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def collatz_seq(n, collatz_dict={}):
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

    prime_facts = get_prime_factors(n)
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


def next_path(path, grid_len):
    while len(path) > 0:
        x, y = path.pop()  # Pop back one step
        if len(path) == 0:
            return False, []
        _x, _y = path[-1]

        if _x == grid_len or _y == grid_len:  # Wall. Only 1 choice available.
            pass
        elif y == _y + 1:
            pass
        else:
            path.append((_x, _y + 1))
            return True, path
    else:
        return False, []


def get_routes(x, y, grid_size, remembered={}):
    # Finds all the routes from a given point (x, y) in a grid.
    if (x, y) not in remembered:
        remembered[x, y] = 0
    routes, path = 0, []
    iterating = True

    while iterating:
        path.append((x, y))
        if x < grid_size:
            x += 1
        elif y < grid_size:
            y += 1
        else:
            routes += 1
            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

        if (x, y) in remembered:
            routes += remembered[x, y]
            path.append((x, y))

            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

    return routes


def find_all_routes(grid_size, remembered):
    # The lattice array is really grid_size + 1

    # Start constructing the counts from the last space
    for i in range(grid_size, -1, -1):
        for j in range(grid_size, -1, -1):
            # Remember the count of paths from the current (i, j) position
            if (i, j) not in remembered:
                remembered[i, j] = get_routes(i, j, grid_size, remembered)

    routes = get_routes(0, 0, grid_size, remembered)

    return routes


def isprime_checkall(target):
    """ Checks if an integer is prime. Returns True or False.."""
    # Start checking at 2.
    currentfactor = 3

    while currentfactor <= math.sqrt(target):
        if target % currentfactor == 0:
            # target is divisible by something other than 1 and itself. it is not prime.
            return False

        # Increment currentfactor and keep searching
        currentfactor += 2

    # Found no other factors, which means the number is prime.
    return True


def isprime_2step(target):
    """ Checks if an integer is prime. Returns True or False.."""
    if target == 2:  # The only prime even
        return True

    # Check evens: Might save processing
    if target % 2 == 0:
        return False

    if target < 2:  # Anything below 3 is not prime.
        return False

    # Start checking at 3. Lets us increment checks by 2 and skip evens.
    currentfactor = 3

    """
    We only need to search up to the square root of n because if a number N is not prime, it can
    be factored into 2 factors A and B.  N = A * B

    If A and B > squareroot(N), A*B would be greater than N.  Therefore, at least one of those
    factors must be less or equal to the square root of N. This is why we only need to test for
    factors less than or equal to the square root.

    Mathematical representation: if N = A*N and A <= B then A*A <= A*N = N
    """

    while currentfactor <= math.sqrt(target):
        if target % currentfactor == 0:
            # target is divisible by something other than 1 and itself. it is not prime.
            return False

        # Increment currentfactor and keep searching
        currentfactor += 2

    # Found no other factors, which means the number is prime.
    return True


def getprime(n):
    if n < 0:
        raise ValueError('getprime(n) must take an integer greater than or equal to 0.')

    i = 2
    prime = 0
    while True:
        if prime == n:
            return i

        i += 1
        if isprime_2step(i):
            prime += 1


def generate_primes(n):
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    primes = []
    for i in range(n + 1):
        if isprime_2step(i):
            primes.append(i)
        #  primes.append(getprime(i))
    return primes


def sieve_rm_method(n):
    """
    For integers up to n, sifts out non-primes via Sieve of Eratosthenese and returns
    list of all primes up to, and including, n.
    """
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    numbers = [x for x in range(2, n + 1)]
    i = 2
    while i < len(numbers) + 2:
        for j in range(i * 2, n + 1, i):
            if j in numbers:
                numbers.remove(j)
        i += 1

    return numbers


def sieve_markers(n):
    """
    Sieve of Eratosthenese; returns list primes up to, and including, n.
    * Uses enumerate while going through the list to remove numbers by index.
    """
    if n < 2:
        raise ValueError('Passed in integer is not large enough to contain primes.')

    numbers = [x for x in range(n + 1)]
    numbers[0] = None
    numbers[1] = None

    size = len(numbers)
    i = 1
    while i < size:
        i += 1
        if i is None:
            continue
        for j in range(i * 2, size, i):
            numbers[j] = None

    return [x for x in numbers if x is not None]


def get_prime_factors(N):
    """
    Find all prime factors in N and return them as a list
    """
    i = 2
    factors = set()

    while N > 1:
        if N % i == 0:
            factors.add(i)
            N = N / i
        else:
            # only increment if we did not find a factor.
            i = i + 1
    if len(factors) == 0:
        return None
    else:
        return factors


def max_prime_factor(N):
    factors = get_prime_factors(N)
    if factors is None:
        return None
    else:
        return max(factors)


def sum_via_iteration(n):
    prime_sum = 0
    for i in range(n):
        if isprime_2step(i):
            prime_sum += i
    return prime_sum


def sum_via_sieve(n):
    prime_sum = 0
    set_of_primes = sieve_rm_method(n - 1)
    for p in set_of_primes:
        prime_sum += p
    return prime_sum


def sum_via_generator(n):
    pass


def sum_of_squares(upto):
    return sum([i ** 2 for i in range(upto+1)])


def square_of_sum(upto):
    return sum([i for i in range(upto + 1)]) ** 2
