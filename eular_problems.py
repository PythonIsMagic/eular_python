# -*- coding: utf-8 -*-
"""
  " Manages the running of all Eular Problems
  """
import functions
import itertools
import primes


def separator():
    print('_'*80)


def eular1():
    """Eular problem 1 - Multiples of 3 and 5:
        Find the sum of all the multiples of 3 or 5 below 1000.
    """
    print(eular1.__doc__)
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print('Sum = {}'.format(result))
    assert result == 233168


def eular2():
    """Eular problem 2 - Even Fibonacci numbers:
        By considering the terms in the Fibonacci sequence whose values do not
        exceed 4 million, find the sum of the even-valued terms.
    """
    print(eular2.__doc__)
    UPPERLIMIT = 4000000
    result = sum([x for x in functions.fibonaccis(UPPERLIMIT) if x % 2 == 0])
    assert result == 4613732
    print('Sum = {}'.format(result))


def eular3():
    """Eular Problem 3 - Largest Prime Factor:
        What is the largest prime factor of the number 600,851,475,143 ?
    """
    print(eular3.__doc__)
    bignumber = 600851475143
    result = primes.max_prime_factor(bignumber)
    assert result == 6857
    print('Largest prime factor of {}: {}'.format(bignumber, result))


def eular4():
    """Eular problem 4 - Largest palindrome product:
        Find the largest palindrome made from the product of two 3-digit numbers.
    """
    print(eular4.__doc__)
    result = functions.largest_palindrome(100, 1000)
    assert result == 906609
    print('Largest palindrome between the factors of 100 and 1000 = {}'.format(result))
    print()


def eular5():
    """Eular problem 5 - Smallest multiple:
        What is the smallest positive number that is evenly divisible by all
        numbers 1 to 20?
    """
    print(eular5.__doc__)
    limit = 20
    result = functions.div_by_all_upto(limit)
    assert result == 232792560
    print('Finding a number divisible by all the numbers 1-{}'.format(limit))
    print("{} is a factor of all numbers 1-{}!".format(result, limit))


def eular6():
    """Eular Problem 6 - Sum square difference:
        Find the difference between the sum of the squares of the first one
        hundred natural numbers and the square of the sum.
    """
    print(eular6.__doc__)
    upto = 100
    sum_of_sq = functions.sum_of_squares(upto)
    sq_of_sum = functions.square_of_sum(upto)

    result = abs(sq_of_sum - sum_of_sq)
    assert result == 25164150

    print('The difference between the sum of the squares of the first 100 ' +
          'numbers and the square of the sum is {}'.format(result))


def eular7():
    """Eular Problem 8 - 10001st prime:
        What is the 10001st prime number?
    """
    print(eular5.__doc__)
    targetprime = 10001
    result = 0
    for i, result in enumerate(primes.primes()):
        if i == targetprime - 1:
            break
    print('Prime #{} = {}'.format(targetprime, result))
    assert result == 104743


def eular8():
    """Eular Problem 8 - Largest product in a series:
        Find the 13 adjacent digits in the 1000-digit number that have the
        greatest product.  What is the value of this product?
    """
    print(eular8.__doc__)
    FACTORS = 13
    filename = 'data/eular8.txt'
    digits = functions.read_file_to_list(filename)
    result = functions.find_product_in_list(digits, FACTORS)
    assert result == 23514624000
    print('The largest product is {}'.format(result))


def eular9():
    """Eular Problem 9 - Special Pythagorean triplet:
        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product a * b * c.
    """
    print(eular9.__doc__)
    a, b, c = functions.iterative_solution()
    result = a * b * c
    assert result == 31875000
    print('a^2 + b^2 = c^2')
    print('{} + {} = {}'.format(a ** 2, b ** 2, c ** 2))
    print('{} + {} + {} = 1000!'.format(a, b, c))
    print('The product abc = {}'.format(result))


def eular10():
    """Eular Problem 10 - Summation of primes:
        Find the sum of all the primes below two million.
    """
    print(eular10.__doc__)
    upperlimit = 2000000
    result = sum(primes.eratosthenes_sieve(upperlimit))
    assert result == 142913828922
    print('The sum of all primes up to {} = {}'.format(upperlimit, result))


def eular11():
    """Eular Problem 11 - Largest product in a grid:
        In the 20×20 grid below, four numbers along a diagonal line have been
        marked in red. What is the greatest product of four adjacent numbers in
        the same direction(up, down, left, right, or diagonally) in the 20×20 grid?
    """
    print(eular11.__doc__)
    m = functions.read_matrix('data/matrix1.txt')
    result = functions.find_greatest_product(m, 4)
    assert result == 70600674
    print('The greatest product in the is {}'.format(result))


def eular12():
    """Eular Problem 12 - Triangle numbers:
        What is the value of the first triangle number to have over five hundred
        divisors?
    """
    print(eular12.__doc__)
    result = 0
    for result in functions.triangles():
        # Skip checking numbers that don't end in 0.
        if result % 10 != 0:
            continue
        f = primes.divisors(result)

        if len(f) > 500:
            break
    assert result == 76576500
    print('{} is the first triangle number to have over 500 divisors.'.format(result))


def eular13():
    """Eular Problem 13 - Large Sum:
        Work out the first ten digits of the sum of the following one-hundred
        50-digit numbers.
    """
    print(eular13.__doc__)
    n = functions.read_numbers('data/bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x

    print('sum = {}'.format(bigsum))
    sum_list = list(str(bigsum))
    result = int(''.join(sum_list[0:10]))
    print(result)
    assert result == 5537376230


def eular14():
    """Eular Problem 14 - Longest Collatz sequence:
        Which starting number, under one million, produces the longest Collatz
        chain?
    """
    print(eular14.__doc__)
    upto = 1000000
    longest_seq = functions.longest_collatz_seq(upto)
    result = longest_seq[0]
    print('\n\n')
    print('The longest collatz sequence under {} starts with the number {}'.format(upto, result))
    print('which has a length of {}'.format(len(longest_seq)))
    assert result == 837799


def eular15():
    """Eular Problem 15 - Lattice paths:
        Starting in the top left corner of a 2×2 grid, and only being able to
        move to the right and down, there are exactly 6 routes to the bottom
        right corner. How many such routes are there through a 20×20 grid?
    """
    print(eular15.__doc__)
    GRIDSIZE = 20
    remembered = {}
    result = functions.find_all_routes(GRIDSIZE, remembered)
    assert result == 137846528820
    print('{} routes in a {}x{} grid!'.format(result, GRIDSIZE, GRIDSIZE))


def eular16():
    """Eular Problem 16 - Power digit sum:
        What is the sum of the digits of the number 2^1000?
    """
    print(eular16.__doc__)
    result = sum([int(x) for x in str(2 ** 1000)])
    assert result == 1366
    print('Sum = {}'.format(result))


def eular17():
    """Eular Problem 17 - Number letter counts:
        If all the numbers from 1 to 1000 (one thousand) inclusive were written
        out in words, how many letters would be used?
    """
    print(eular17.__doc__)
    result = 0
    for i in range(1, 1001):
        number = functions.num_to_alpha(i)
        qty = functions.letter_qty(number)
        result += qty
    assert result == 21124
    print('It take {} letter to represent all the numbers in 1-1000'.format(result))


def eular18():
    """Eular Problem 18 - Maximum path sum I:
        Find the maximum total from top to bottom of the given triangle:
    """
    print(eular18.__doc__)
    tree = functions.read_matrix('data/number_tree.txt')
    result = functions.find_max_path(tree)
    assert result == 1074
    print('The maximum sum = {}'.format(result))


def eular19():
    """Eular problem 19 - Counting Sundays:
        How many Sundays fell on the first of the month during the twentieth
        century (1 Jan 1901 to 31 Dec 2000)?
    """
    print(eular19.__doc__)
    result = functions.count_sundays()
    assert result == 171
    print('{} Sundays counted.'.format(result))


def eular20():
    """Eular Problem 20 - Factorial digit sum:
        Find the sum of the digits in the number 100!
    """
    print(eular20.__doc__)
    num = 100
    result = functions.factorial_sum(num)
    assert result == 648
    print('The sum of the digits in {}! = {}'.format(num, result))


def eular21():
    """Eular Problem 21 - Amicable numbers:
        Evaluate the sum of all the amicable numbers under 10000.
    """
    print(eular21.__doc__)
    LIMIT = 10000
    # Add all of the amicable numbers together
    result = functions.add_amicables(10000)
    print('The sum of all amicables #s up to {} = {}'.format(LIMIT, result))
    assert result == 31626


def eular22():
    """Eular Problem 22 - Names scores:
        Using names.txt, work out the alphabetical value for each name, multiply
        this value by its alphabetical position in the list to obtain a name
        score. What is the total of all the name scores in the file?
    """
    print(eular22.__doc__)
    names = functions.import_names('data/names.txt')
    print('names has {} entries.'.format(len(names)))
    result = 0

    for i, n in enumerate(names):
        result += functions.alphabetical_value(n) * (i+1)

    assert result == 871198282
    print('The total of all name scores = {}'.format(result))


def eular23():
    """Eular Problem 23 - Non-abundant sums:
        Find the sum of all positive integers which cannot be written as the sum
        of two abundant numbers.
    """
    print(eular23.__doc__)
    result = functions.nonsummable_by_abundants()
    print('Sum of all positive ints which can\'t be summed by 2 abundants={}'.format(result))
    assert result == 4179871


def eular24():
    """Eular Problem 24 - Lexicographic permutations:
        What is the millionth lexicographic permutation of the digits:
            0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    print(eular24.__doc__)
    perms = list(itertools.permutations(str('0123456789'), len('0123456789')))
    result = int(''.join(perms[999999]))
    print(result)
    assert result == 2783915460


def eular25():
    """Eular Problem 25 - The Fibonacci sequence:
        What is the first term in the Fibonacci sequence to contain 1000 digits?
    """
    print(eular25.__doc__)
    i = 0
    for i, x in enumerate(functions.fibonaccis()):
        if len(str(x)) >= 1000:
            break

    i += 1  # Avoid off by one err
    assert i == 4782
    print('Fibonacci Term {} has over 1000 digits!'.format(i))


def eular30():
    """Eular Problem 30 - Digit fifth powers:
        Find the sum of all the numbers that can be written as the sum of fifth
        powers of their digits.
    """
    print(eular30.__doc__)
    POWER = 5
    i = 0
    while True:
        if not functions.writable_by_powers(i, POWER):
            break
        i += 1

    print('Max number writable by fifth powers is {}'.format(i))

    fifth_sums = []
    for x in range(2, i + 1):
        if functions.sum_powers(x, POWER) == x:
            fifth_sums.append(x)

    print('These are the numbers that can be written as the sum of 5th powers of their digits.')
    print(fifth_sums)

    print('The sum of these numbers = {}'.format(sum(fifth_sums)))

EULAR_FUNCTIONS = (
    eular1,
    eular2,
    eular3,
    eular4,
    eular5,
    eular6,
    eular7,
    eular8,
    eular9,
    eular10,
    eular11,
    eular12,
    eular13,
    eular14,
    eular15,
    eular16,
    eular17,
    eular18,
    eular19,
    eular20,
    eular21,
    eular22,
    eular23,
    eular24,
    eular25,
    eular30,
)


def main():
    for f in EULAR_FUNCTIONS:
        f()
        separator()

if __name__ == "__main__":
    main()
