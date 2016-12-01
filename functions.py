"""
  " Collection of functions for the various Eular problems.
  """

import itertools
import math
import primes
import recursion
import string

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen',
         6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}


def abundant(n):
    """ A number n is called abundant if the sum of its proper divisors is more
        than n. Returns True if n is an abundant number, False otherwise.
    """
    return sum(primes.divisors_proper(n)) > n


def abundants_upto(limit):
    """ Returns a list of all abundant numbers up, and including, the limit. """
    return [i for i in range(1, limit + 1) if abundant(i)]


def add_amicables(limit):
    """ Adds all the amicable numbers up to limit and returns the sum. """
    amicables = set()
    div_sums = primes.divisor_sum_dict(limit)

    for k, v in div_sums.items():
        # Skip divisor sums that are equal to or over the limit - they won't be in the keys.
        # Also - k and v cannot be equal. k != v.
        if v >= limit or k == v:
            continue

        # Since we have the divisor sum of k as v, we can conversely lookup the opposite
        # div_sums[v] and check if it equals k.
        if div_sums.get(v, -1) == k:
            amicables.add(k)

    return sum(amicables)


def add_digits(n):
    """ Adds all the digits in the list and returns the sum."""
    return sum(num_to_list(n))


def adds_to_1000(a, b, c):
    if a + b + c == 1000:
        return True
    else:
        return False


def alphabetical_value(name):
    """ Returns the sum of the alphabetical values of the string passed. Each
        letter is equal to it's position in the alphabet.
        Example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
    """
    return sum([ord(x.lower()) - 96 for x in list(name)])


def calculate_product(alist):
    """ Returns the product of a list of numbers. """
    product = 1
    for fact in alist:
        product *= fact
    return product


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


def extract_line(matrix, point, xyincrement):
    """ Takes an x by x matrix and scans a matrix for a list of items.

        Uses a starting point tuple (x, y) and an increment tuple(x-increment, y-increment).
        Starts the list from the x, y coordinate and goes in the increments given by xinc and yinc.
    """
    x, y = point[0], point[1]
    xinc, yinc = xyincrement[0], xyincrement[1]
    items = []

    while x >= 0 and y >= 0 \
            and x < len(matrix) and y < len(matrix):
        items.append(matrix[y][x])
        x += xinc
        y += yinc
    return items


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
        elif primes.factor_of_all_upto(i, limit):
            break

        # Increase by the size of the largest factor we are testing by. This should dramatically
        # increase the speed and we don't need to test numbers in between since they won't be
        # divisible by that number.
        i += limit
    return i


def factorial_sum(n):
    """ Returns the sum of the integers in the factorial of n. """
    return sum([int(x) for x in str(math.factorial(n))])


def fibonaccis(limit=None):
    """ Fibonacci number generator. Sequence starts [1, 1, 2, 3, 5] and so on. """
    a, b = 0, 1
    while True:
        if limit and b >= limit:
            raise StopIteration()
        a, b = b, a + b
        yield a


def find_ab(a, b, c, squares):
    #  print('find_ab({}, {}, {}, squares)'.format(a, b, c))
    print('find_ab({} + {} = {}?'.format(squares[a], squares[b], squares[c]))
    # base case:
    if is_pythagorean_triplet(squares[a], squares[b], squares[c]) and b != c:
        print('Base case encountered.')
        return squares[a], squares[b], squares[c]
    elif a == c - 2 and b == c - 1:
        print('No pythagorean triplet found for {}^2.'.format(squares[c]))
        return None
    elif b < c:
        return find_ab(a, b + 1, c, squares)
    else:
        a = a + 1
        return find_ab(a, a + 1, c, squares)


def find_all_routes(grid_size, remembered):
    """ Finds all routes through a lattice array if we can only go right and down. """
    # The lattice array is really grid_size + 1

    # Start constructing the counts from the last space
    for i in range(grid_size, -1, -1):
        for j in range(grid_size, -1, -1):
            # Remember the count of paths from the current (i, j) position
            if (i, j) not in remembered:
                remembered[i, j] = get_routes(i, j, grid_size, remembered)

    routes = get_routes(0, 0, grid_size, remembered)

    return routes


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
            product = recursion.multiply(sequence, i, factors)
            if product > greatest_product:
                greatest_product = product
            i += 1

    return greatest_product


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


def get_digit(n, i):
    """ Returns the i'th digit(from the right of the ones digit) of an integer n """
    modulus = pow(10, i + 1)
    power = pow(10, i)
    return (n % modulus) // power


def get_routes(x, y, grid_size, remembered={}):
    """ Finds all the routes from a given point (x, y) in a grid. """
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


def get_sum(path, tree):
    """ Returns the sum of all the numbers in the path for the given tree. """
    pathsum = 0
    for i, row in enumerate(tree):
        pathsum += row[path[i]]
    return pathsum


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


def import_names(filename):
    """ Reads the names files from Project Eular(for problem 22) and loads each
        name into a list.
    """
    # Each name is contained in quotes ("NAME")
    # and also separated by commas("NAME1", "NAME2, "NAME3")

    names = []
    newname = ''
    with open(filename) as f:

        while True:
            char = f.read(1)
            if not char:
                break  # Empty string means EOF

            # Start a new name with each quote
            if char == "\"" and newname != '':
                names.append(newname)
                newname = ''
            elif char == "\"" or char == ',':
                # Ignore formatting characters
                continue
            else:
                newname += char

    # To sort we can merely use the builtin sorted()
    return sorted(names)


def iterative_solution():
    """ Finds the Pythagorean triplet that adds to 1000. """
    MAX = 1000
    squares = square_list(MAX)

    for a in range(1, MAX):
        for b in range(a + 1, MAX):
            ab = a ** 2 + b ** 2
            c = int(math.sqrt(ab))
            if a + b + c > MAX:
                continue

            if ab in squares:
                #  print('{} + {} + {} == 1000?'.format(a, b, c))
                if adds_to_1000(a, b, c):
                    return a, b, c


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


def is_pythagorean_triplet(a2, b2, c2):
    if a2 + b2 == c2:
        return True
    else:
        return False


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


def letter_qty(s):
    """ Returns how many letters are in the string """
    _sum = 0
    for c in s:
        if c in string.ascii_letters:
            _sum += 1
    return _sum


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


def next_path(path, grid_len):
    """ Finds the next step through a lattice grid. """
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
    return False, []


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


def num_to_list(n):
    """ Converts a number to a list of digits. """
    return [int(x) for x in str(n)]


def print_matrix(matrix):
    _str = ''
    for row in matrix:
        for col in row:
            # Format for 2 digit integers and fill zeros in.
            _str += '{:3}'.format(str(col).zfill(2))
        _str = _str.rstrip() + '\n'
    return _str


def read_matrix(filename):
    """ Reads a file containing integers to a matrix(list of lists). """
    digits = []

    with open(filename) as f:
        for line in f.readlines():
            ints = [int(n) for n in line.split()]
            digits.append(ints)
    return digits


def read_numbers(filename):
    """ Read each number as a line from the file and return the numbers as a list. """
    with open(filename) as f:
        numbers = [int(l) for l in f.readlines()]
    return numbers


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


def recursive_solution():
    """ Recursive solution to eular9 """
    # We probably won't need any squares above 500.
    squares = square_list(500)

    # Start with c^2, and try to determine a and b from c^2.
    for c in range(2, len(squares)):

        if c + (c - 1) + (c - 2) < 1000:
            continue
        # Check if there is a perfect pythagorean triplet for c
        abc = find_ab(0, 1, c, squares)

        # If something other than None is returns, there is a triplet
        if abc is not None:
            a, b, c = abc[0], abc[1], abc[2]

            # Check if they add to 1000
            if adds_to_1000(a, b, c):
                return abc
            else:
                print('{} + {} + {} != 1000'.format(a, b, c))


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


def sum_of_squares(limit):
    """ Returns the sum of all squares in the range 1 up to and including limit. """
    return sum([i ** 2 for i in range(limit+1)])


def sum_powers(n, p):
    return sum(int(x) ** p for x in str(n))


def square_list(upto):
    return [x ** 2 for x in range(upto)]


def square_of_sum(limit):
    """ Returns the square of the sum of all integers in the range 1 up to and
        including limit.
    """
    return sum([i for i in range(limit + 1)]) ** 2


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


def writable_by_powers(n, p):
    digits = len(str(n))
    max_amt = digits * (9 ** p)
    if max_amt < n:
        return False
    else:
        return True
