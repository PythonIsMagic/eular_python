"""
  " Collection of function to process prime numbers and divisors.
  """
import itertools
import math
import string
import timer


def get_multiples():
    """Used for problem 1"""
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


def fibonaccis(limit=None):
    """ Fibonacci number generator.
        Sequence starts [1, 1, 2, 3, 5] and so on.
    """
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


def sift_primes(n):
    """Sieve of eratosthenese. For all integers up to n, sifts out the non-primes
        and returns list of all primes up to n.
    """
    if n < 2:
        print('Passed in integer is not large enough to contain primes.')
        return -1

    numbers = [x for x in range(2, n + 1)]
    #  numbers = [True for x in range(2, n + 1)]

    i = 2
    while i < len(numbers) + 2:
        for j in range(i*2, n + 1, i):
            #  print('j = {}'.format(j))
            if j in numbers:
                numbers.remove(j)

        i += 1

    # Failed attempt
    """
    for i in numbers:
        for j in numbers:
            if j % i == 0:
                numbers.remove(j)
    """

    return numbers


def divisors(n):
    """ Creates a list of all the factors of n and returns them as a set. First
        we get the prime factors of n. To get any remaining factors, we take all
        the prime factors and take each to it's maximum power. This results in a
        list of factors we can use to build the remaining factors.
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


def divisors_bruteforce(n):
    """
    Returns a set of all the divisors of n using a brute force check.  We only need to check up
    to (n/2) for any n, because n won't be divisible by anything larger than that. We'll also
    skip checking even divisors for odd numbers, since they won't be divisible, however this is
    still pretty slow for numbers over a million.
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


def divisors_proper(n):
    """ Return a set containing the proper divisors of n (numbers less than n
        which divide evenly into n).
    """
    d = divisors(n)
    d.remove(n)
    return d


def divisor_sum_dict(limit):
    """ Make a dictionary of divisor sums up to, but not including, limit.
        Example: The divisor sum of 2 would be 1 + 2 = 3.
        The divisor sum of 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
    """
    return {n: sum_proper_divisors(n) for n in range(1, limit)}


def factor_of_all_upto(num, limit):
    """ Returns True if num is divisible by all numbers in the range of integers
        in 1 up to and including limit.

        # Speed up by skipping 1. Any integer is divisible by 1!
        # If the number ends in 1, 3, 7, or 9, it's more likely to be prime.
        # Check backwards from the largest possible factor
    """
    start = 2
    for factor in range(start, limit + 1):
        if num % factor != 0:
            return False
    return True


def isprime_ver1(n):
    """
    Returns True if n is prime, False otherwise.
    * Checks all factors of n.
    * Rediculously slow. For checking up to 100k, takes over a minute.
    """
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def isprime_ver2(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.

    # We only need to search up to the square root of n because if a number N is not prime, it
    # can be factored into 2 factors A and B.  N = A * B

    # If A and B > squareroot(N), A*B would be greater than N.  Therefore, at least one of those
    # factors must be less or equal to the square root of N. This is why we only need to test for
    # factors less than or equal to the square root.

    # Mathematical representation: if N = A*N and A <= B then A*A <= A*N = N
    """
    if n < 2:
        return False
    i = 2
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def isprime_ver3(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.
    * Start checking at 3 and skip evens.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def isprime_ver4(n):
    """
    Returns True if n is prime, False otherwise.
    * Only check up to the square root of n.
    * Start checking at 3 and skip evens.
    * Check 2 and the modulus at the same time. (Saves 2 lines)
    """
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2

    i = 3
    limit = math.sqrt(n)
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def primes():
    """
    Defines a prime number generator that generates prime numbers. The first prime number
    defined is 2. Uses the is_prime tests.
    """
    i = 2
    while True:
        if isprime_ver4(i):
            yield i
        i += 1


def eratosthenes_sieve(n):
    """
    Eratosthenes sieve.
    * Implemented using a list and None to specify a non-prime slot.
    """
    # Great speed!
    L = [x for x in range(n+1)]
    L[0], L[1] = None, None

    i = 0
    while i < len(L):
        if L[i] is None:
            pass
        else:
            for j in range(i * 2, len(L), i):
                L[j] = None
        i += 1
    return [x for x in L if x is not None]


def max_prime_factor(n):
    """
    Finds the largest prime factor of n and returns it.
    """
    factors = get_prime_factors(n)
    if factors is None:
        return None
    else:
        return max(factors)


def get_prime_factors(n):
    """
    Find all prime factors in N and return them as a list.
    """
    i = 2
    factors = set()

    while n > 1:
        if n % i == 0:
            factors.add(i)
            n = n / i
        else:
            # only increment if we did not find a factor.
            i = i + 1
    if len(factors) == 0:
        return None
    else:
        return factors


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n(numbers less than n which divide evenly into n).
    """
    divs = divisors_proper(n)
    return sum(divs)


@timer.timeit
def count_primes(upto, func):
    c = 0
    for i in range(upto):
        if func(i):
            c += 1
    return c


@timer.timeit
def sieve_primes(upto, func):
    p = func(upto)
    return len(p)


def main():
    """ Runs through some tests for different prime functions. """
    print('~~~~~~~~~~~')
    print('Prime tests')

    counts = {
        1000: 168,
        10000: 1229,
        100000: 9592,
        1000000: 78498,
        10000000: 664579,
        # 100000000: 5761455  # too big - got 'Killed'
    }

    funcs = [isprime_ver2, isprime_ver3, isprime_ver4]
    sieves = [eratosthenes_sieve]

    for k, v in sorted(counts.items()):
        print('---------------------------------')
        #  print('Testing 0-{}'.format(k))
        for f in funcs:
            if k < 1000000:
                count = count_primes(k, f)
                print('{} primes found up to {}.'.format(count, k))
                # Validate count
                assert count == v

        # Test the sieves
        for s in sieves:
            count = sieve_primes(k, s)
            assert count == v
            print('{} primes found up to {}.'.format(count, k))


if __name__ == "__main__":
    main()


def print_list(alist):
    """ Prints a list recursively. """
    pl(alist, 0)


def pl(alist, index):
    if index < len(alist) - 1:
        print(alist[index])
        pl(alist, index + 1)
    else:
        # Base case: index is at the end
        print(alist[index])


def print_selection(alist, index, factors):
    # Base case: At index 0
    if factors == 0:
        print(alist[index])
    else:
        print(alist[index])
        print_selection(alist, index + 1, factors - 1)


def multiply(alist, index, factors, product=1):
    # Base case: At index 0
    if index < 0 or index >= len(alist):
        # Out of bounds, just return 0?
        raise ValueError('index is out of bounds!')
        #  return 0
    elif factors == 1:
        return alist[index]
    else:
        return alist[index] * multiply(alist, index + 1, factors - 1, product)


def recursive_try():
    pass
    #  print('Eular 9: Recursive solution')
    #  result = recursive_solution()
    #  if result is None:
        #  print('No solution was found')
        #  exit()
    #  else:
        #  a2, b2, c2 = result

    #  a = math.sqrt(a2)
    #  b = math.sqrt(b2)
    #  c = math.sqrt(c2)


def is_palindrome(number):
    """ Returns True if the variable passed is a palindrome, False otherwise.  """
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
    return True


def largest_palindrome(lowerlimit, upperlimit):
    """ Finds the largest palindrome in the given integer limits. """
    largest = 0

    for m1 in range(lowerlimit, upperlimit):
        # Start from m1 for this range so we don't hit duplicate factors
        for m2 in range(m1, upperlimit):
            product = m1 * m2
            if is_palindrome(product):
                if product > largest:
                    largest = product
    return largest


def div_by_all_upto(limit):
    """ Finds the first integer that is divisible by all numbers 1 through, and
        including, limit.
    """
    # Start at the highest factor we are testing by because the target number won't be divisible
    # by any numbers larger than it.
    if limit < 10:
        raise ValueError('This function only tests for ranges 10 and above!')
    elif limit % 10 != 0:
        raise ValueError('This function only tests multiples of 10!')

    i = limit

    while True:
        # Skip any number that doesn't end in 0.
        # Ending in 0 maximizes our chance of a big divisor.
        if i % 10 != 0:
            pass
        elif factor_of_all_upto(i, limit):
            break

        # Increase by the size of the largest factor we are testing by. This should dramatically
        # increase the speed and we don't need to test numbers in between since they won't be
        # divisible by that number.
        i += limit
    return i


def sum_of_squares(limit):
    """ Returns the sum of all squares in the range 1 up to and including limit. """
    return sum([i ** 2 for i in range(limit+1)])


def square_of_sum(limit):
    """ Returns the square of the sum of all integers in the range 1 up to and
        including limit.
    """
    return sum([i for i in range(limit + 1)]) ** 2


def calculate_product(alist):
    """ Returns the product of a list of numbers. """
    product = 1
    for fact in alist:
        product *= fact
    return product


def read_file_to_list(filename):
    """ Reads a file containing digits(or a big number) and converts it to a
        list of individual.
    """
    digits = []
    with open(filename) as _file:
        while True:
            _char = _file.read(1)
            if not _char:  # End of file
                break
            else:
                try:
                    digits.append(int(_char))
                except ValueError:
                    pass
    return digits


def find_product_in_list(alist, factors):
    """ Takes in a list of digits and finds the greatest possible product of x
        factors.
    """
    largest_product = 0
    # Ending point = size - (FACTORS - 1)
    end = len(alist) - (factors - 1)

    # Iterate through the list until we get to the ending point
    n = 0
    while n < end:
        # For each point, calculate the product.
        list_slice = alist[n: n + factors]
        product = calculate_product(list_slice)
        if product > largest_product:
            largest_product = product
        n += 1
    return largest_product


def extract_line(matrix, point, xyincrement):
    """ Takes an x by x matrix and scans a matrix for a list of items.

        Uses a starting point tuple (x, y) and an increment tuple(x-increment, y-increment).
        Starts the list from the x, y coordinate and goes in the increments given by xinc and yinc.
    """
    x, y = point[0], point[1]
    xinc, yinc = xyincrement[0], xyincrement[1]
    items = []

    while 0 <= x < len(matrix) and y >= 0 and y < len(matrix):
        items.append(matrix[y][x])
        x += xinc
        y += yinc
    return items


def find_greatest_product(_matrix, factors):
    """ Finds the greatest product of (x * factors) adjacent integers in a matrix. """
    greatest_product = 0
    lines = scan_matrix_lines(_matrix)

    for sequence in lines:
        endpoint = len(sequence) - factors
        if len(sequence) < factors:
            continue
        i = 0
        while i <= endpoint:
            product = multiply(sequence, i, factors)
            if product > greatest_product:
                greatest_product = product
            i += 1

    return greatest_product


def get_rows(matrix):
    rows = []
    for i in range(len(matrix)):
        point = (0, i)
        inc = (1, 0)
        rows.append(extract_line(matrix, point, inc))
    return rows


def get_columns(matrix):
    cols = []
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (0, 1)
        cols.append(extract_line(matrix, point, inc))
    return cols


def get_right_diagonals(matrix):
    """ Extracts all the right-facing diagonal lines of a matrix and returns
        them as a list.
    """

    diags = []

    # Scan right diagonals: bottom left to top left.
    for i in range(len(matrix) - 1, 0, -1):
        point = (0, i)
        inc = (1, 1)
        diags.append(extract_line(matrix, point, inc))

    # Scan right diagonals: top left to top right
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (1, 1)
        diags.append(extract_line(matrix, point, inc))

    return diags


def get_left_diagonals(matrix):
    """ Extracts all the left-facing diagonal lines of a matrix and returns them
        as a list.
    """
    diags = []
    # Scan left diagonals: top left to top right
    for i in range(len(matrix)):
        point = (i, 0)
        inc = (-1, 1)
        diags.append(extract_line(matrix, point, inc))

    # Scan left diagonals: top right to bottom right
    for i in range(1, len(matrix)):
        point = (len(matrix) - 1, i)
        inc = (-1, 1)
        diags.append(extract_line(matrix, point, inc))
    return diags


def read_matrix(filename):
    """ Reads a file containing integers to a matrix(list of lists). """
    digits = []

    with open(filename) as f:
        for line in f.readlines():
            ints = [int(n) for n in line.split()]
            digits.append(ints)
    return digits


def scan_matrix_lines(matrix):
    """ Scans for all rows, columns, and diagonals in the given matrix and
        returns them as a list of lists.
    """
    lines = []
    lines.extend(get_rows(matrix))
    lines.extend(get_columns(matrix))
    lines.extend(get_right_diagonals(matrix))
    lines.extend(get_left_diagonals(matrix))
    return lines


def print_matrix(matrix):
    _str = ''
    for row in matrix:
        for col in row:
            # Format for 2 digit integers and fill zeros in.
            _str += '{:3}'.format(str(col).zfill(2))
        _str = _str.rstrip() + '\n'
    return _str


def triangles():
    """ Defines a generator that generates triangle numbers. The sequence of
        triangle numbers is generated by adding the natural numbers. The first
        triangle number is 1, followed by 3, 6, 10, and so on.
    """
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x


def read_numbers(filename):
    """ Read each number as a line from the file and return the numbers as a list. """
    with open(filename) as f:
        numbers = [int(l) for l in f.readlines()]
    return numbers


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


ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen',
         6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}


def get_digit(n, i):
    """ Returns the i'th digit(from the right of the ones digit) of an integer n """
    modulus = pow(10, i + 1)
    power = pow(10, i)
    return (n % modulus) // power


def get_text(n):
    """ Returns the test representation of an integer from 0-999 """
    if n < 1 or n > 999:
        raise ValueError('n is out of bounds. Must be between 1 and 999 inclusive.')

    alpha = ''
    # Hundreds digit
    if n < 100:
        pass
    elif n % 100 == 0:
        alpha += ones[get_digit(n, 2)] + ' hundred'
    else:
        alpha += ones[get_digit(n, 2)] + ' hundred and '

    # Teens
    if get_digit(n, 1) == 1:
        alpha += teens[get_digit(n, 0)]
    # Factors of 10
    elif n % 10 == 0:
        alpha += tens[get_digit(n, 1)]
    # Ten+single, ie: "twenty-one"
    elif get_digit(n, 1) >= 2:
        alpha += tens[get_digit(n, 1)] + '-' + ones[get_digit(n, 0)]
    else:
        alpha += ones[get_digit(n, 0)]
    return alpha


def letter_qty(s):
    """ Returns how many letters are in the string """
    _sum = 0
    for c in s:
        if c in string.ascii_letters:
            _sum += 1
    return _sum


def num_to_alpha(n):
    """ Converts a number to it's English equivalent. """
    alpha = ''
    if n == 0:
        return 'zero'
    if n >= 1000000:
        millions = (n % 1000000000) // 1000000
        alpha += '{} million '.format(get_text(millions))

    if n >= 1000:
        thousands = (n % 1000000) // 1000
        alpha += '{} thousand '.format(get_text(thousands))

    hundreds = n % 1000
    if hundreds > 0:
        alpha += get_text(hundreds)

    return alpha.strip()


months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def count_sundays():
    """ Counts all the Sundays in a date range. """
    month = 1
    day = 1
    year = 1900
    weekday = 0  # 0=Monday, 6=Sunday
    sundays = 0

    while year < 2001:
        #  print('{}/{}/{} weekday: {}'.format(month, day, year, weekday))

        # Check for Sunday on the first of the month.
        if weekday == 6 and day == 1 and year > 1900:
            sundays += 1
            #  print('Sunday on the first of the month!')

        # advance day
        day += 1
        weekday = (weekday + 1) % 7

        # Advance month
        if day > get_days(month, year):
            day = 1
            month += 1

        # Advance Year
        if month > 12:
            month = 1
            year += 1

    return sundays


def get_days(month, year=None):
    """ Returns the number of days in the month. The year defaults to None, but
        if the month is February, the year will be needed to calculate the days.
    """
    if month == 2:
        if year is None:
            raise ValueError('getdays(month, year) requires a year when taking 2 as the month.')
        elif is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return months[month]


def is_leap_year(year):
    """ Returns True if the passed year is a leap-year, False otherwise. """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def abundant(n):
    """ A number n is called abundant if the sum of its proper divisors is more
        than n. Returns True if n is an abundant number, False otherwise.
    """
    return sum(divisors_proper(n)) > n


def abundants_upto(limit):
    """ Returns a list of all abundant numbers up, and including, the limit. """
    return [i for i in range(1, limit + 1) if abundant(i)]


def nonsummable_by_abundants():
    """ Return the sum of all integers that cannot be written as the sum of
        abundant numbers.
    """
    LIMIT = 28123
    # Calculate all the abundant numbers up to limit.
    abundants = abundants_upto(LIMIT)

    # Create all possible 2 term combinations for sums.
    #  pairs = list(itertools.combinations(abundants, 2)) # No
    #  pairs = itertools.combinations(abundants, 2) # No
    #  pairs = itertools.permutations(abundants, 2) # No
    # We want the Cartesian product, because the abundant numbers, can be repeated(ex: 12 - the
    # lowest abundant number, can be repeated 12+12 to sum 24.)
    pairs = itertools.product(abundants, repeat=2)

    # Create a set of sums using a set comprehension
    abundant_sums = {a + b for a, b in pairs}

    unsummable = [i for i in range(LIMIT + 1) if i not in abundant_sums]

    return sum(unsummable)


def find_max_path(tree):
    """ Finds the path through a tree of numbers that yields the highest sum. """
    # Start all paths at 0(or IOW, the absolute left side of the tree.)
    path = [0 for _ in range(len(tree))]
    maxsum = 0
    iterating = True

    while iterating:
        # Checking for the best sum
        pathsum = get_sum(path, tree)
        if pathsum > maxsum:
            maxsum = pathsum

        # Move path ahead
        iterating = move_path(path, len(tree) - 1)
    return maxsum


def get_sum(path, tree):
    """ Returns the sum of all the numbers in the path for the given tree. """
    pathsum = 0
    for i, row in enumerate(tree):
        pathsum += row[path[i]]
    return pathsum


def move_path(path, row):
    """ Moves to the next path in a tree. """
    # Base case: If the row is 0, we can't move that one since its the top.
    # Should mean iteration is over.
    if row == 0:
        return False
    elif path[row] == path[row - 1]:
        path[row] += 1

        # Make sure all sub rows match! To avoid skips
        for x in range(row + 1, len(path)):
            path[x] = path[row]

        return True
    else:
        return move_path(path, row - 1)
