import alphanumbers
import bignumber
import countingdays
import filework
import functions
import itertools
import latticepaths
import matrix
import numbertree
import primes
import pythagorean
import text


def separator():
    print('#'*80)


def eular1():
    print(text.eular1)
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    #  result = functions.sum_multiples([3, 5], 1000)
    print('Sum = {}'.format(result))
    assert result == 233168


def eular2():
    print(text.eular2)
    UPPERLIMIT = 4000000
    result = sum([x for x in functions.fibonacci(UPPERLIMIT) if x % 2 == 0])
    assert result == 4613732
    print('Sum = {}'.format(result))


def eular3():
    print(text.eular3)
    bignumber = 600851475143
    result = primes.max_prime_factor(bignumber)
    assert result == 6857
    print('Largest prime factor of {}: {}'.format(bignumber, result))


def eular4():
    print(text.eular4)
    result = functions.get_largest_palindrome(100, 1000)
    assert result == 906609
    print('Largest palindrome between the factors of 100 and 1000 = {}'.format(result))
    print()


def eular5():
    print(text.eular5)
    limit = 20
    result = functions.num_div_by_all_upto(limit)
    assert result == 232792560
    print('Finding a number divisible by all the numbers 1-{}'.format(limit))
    print("{} is a factor of all numbers 1-{}!".format(result, limit))


def eular6():
    print(text.eular6)
    upto = 100
    sum_of_sq = functions.sum_of_squares(upto)
    sq_of_sum = functions.square_of_sum(upto)

    result = abs(sq_of_sum - sum_of_sq)
    assert result == 25164150

    print('The difference between the sum of the squares of the first 100 ' +
          'numbers and the square of the sum is {}'.format(result))


def eular7():
    print(text.eular7)
    targetprime = 10001
    for i, result in enumerate(primes.primes()):
        if i == targetprime - 1:
            break
    print('Prime #{} = {}'.format(targetprime, result))
    assert result == 104743


def eular8():
    print(text.eular8)
    FACTORS = 13
    filename = 'eular8.txt'
    digits = bignumber.read_file_to_list(filename)
    result = bignumber.find_product_in_list(digits, FACTORS)
    assert result == 23514624000
    print('The largest product is {}'.format(result))


def eular9():
    print(text.eular9)
    a, b, c = pythagorean.iterative_solution()
    result = a * b * c
    assert result == 31875000
    print('a^2 + b^2 = c^2')
    print('{} + {} = {}'.format(a ** 2, b ** 2, c ** 2))
    print('{} + {} + {} = 1000!'.format(a, b, c))
    print('The product abc = {}'.format(result))


def eular10():
    print(text.eular10)
    upperlimit = 2000000
    result = sum(primes.eratosthenes_sieve(upperlimit))
    assert result == 142913828922
    print('The sum of all primes up to {} = {}'.format(upperlimit, result))


def eular11():
    print(text.eular11)
    m = matrix.read_matrix('matrix1.txt')
    result = matrix.find_greatest_product(m, 4)
    assert result == 70600674
    print('The greatest product in the is {}'.format(result))


def eular12():
    print(text.eular12)
    for result in functions.triangle_num():
        # Skip checking numbers that don't end in 0.
        if result % 10 != 0:
            continue
        f = functions.divisors(result)

        if len(f) > 500:
            break
    assert result == 76576500
    print('{} is the first triangle number to have over 500 divisors.'.format(result))


def eular13():
    print(text.eular13)
    n = bignumber.read_numbers('bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x

    print('sum = {}'.format(bigsum))
    sum_list = list(str(bigsum))
    result = int(''.join(sum_list[0:10]))
    print(result)
    assert result == 5537376230


def eular14():
    print(text.eular14)
    upto = 1000000
    longest_seq = functions.longest_collatz_seq(upto)
    result = longest_seq[0]
    assert result == 837799
    print('\n\n')
    print('The longest collatz sequence under {} starts with the number {}'.format(upto, result))
    print('which has a length of {}'.format(len(longest_seq)))


def eular15():
    print(text.eular15)
    GRIDSIZE = 20
    remembered = {}
    result = latticepaths.find_all_routes(GRIDSIZE, remembered)
    assert result == 137846528820
    print('{} routes in a {}x{} grid!'.format(result, GRIDSIZE, GRIDSIZE))


def eular16():
    print(text.eular16)
    result = sum([int(x) for x in str(2 ** 1000)])
    assert result == 1366
    print('Sum = {}'.format(result))


def eular17():
    print(text.eular17)
    result = 0
    for i in range(1, 1001):
        number = alphanumbers.num_to_alpha(i)
        qty = alphanumbers.letter_qty(number)
        result += qty
    assert result == 21124
    print('It take {} letter to represent all the numbers in 1-1000'.format(result))


def eular18():
    print(text.eular18)
    tree = matrix.read_matrix('number_tree.txt')
    result = numbertree.find_max_path(tree)
    assert result == 1074
    print('The maximum sum = {}'.format(result))


def eular19():
    print(text.eular19)
    result = countingdays.count_sundays()
    assert result == 171
    print('{} Sundays counted.'.format(result))


def eular20():
    print(text.eular20)
    num = 100
    result = functions.fact_sum(num)
    assert result == 648
    print('The sum of the digits in {}! = {}'.format(num, result))


def eular21():
    print(text.eular21)
    LIMIT = 10000
    # Add all of the amicable numbers together
    result = functions.add_amicable_numbers(10000)
    assert result == 31626
    print('The sum of all amicables #s up to {} = {}'.format(LIMIT, result))


def eular22():
    print(text.eular22)
    names = filework.import_names('names.txt')
    print('names has {} entries.'.format(len(names)))
    result = 0

    for i, n in enumerate(names):
        result += functions.alphabetical_value(n) * (i+1)

    assert result == 871198282
    print('The total of all name scores = {}'.format(result))


def eular23():
    print(text.eular23)
    LIMIT = 28123
    abundants = [i for i in range(1, LIMIT + 1) if functions.is_abundant(i)]
    sums = set([a + abundants[b]
                for i, a in enumerate(abundants)
                for b in range(i, len(abundants))])
    unsummable = [i for i in range(LIMIT + 1) if i not in sums]
    result = sum(unsummable)
    assert result == 4179871
    print('Sum of all positive ints which can\'t be summed by 2 abundants={}'.format(result))


def eular24():
    print(text.eular24)
    perms = list(itertools.permutations(str('0123456789'), len('0123456789')))
    result = int(''.join(perms[999999]))
    print(result)
    assert result == 2783915460


def eular25():
    print(text.eular25)
    for i, x in enumerate(functions.fibonacci()):
        if len(str(x)) >= 1000:
            break

    i += 1  # Avoid off by one err
    assert i == 4782
    print('Fibonacci Term {} has over 1000 digits!'.format(i))


if __name__ == "__main__":
    eular1()
    separator()

    eular2()
    separator()

    eular3()
    separator()

    eular4()
    separator()

    eular5()
    separator()

    eular6()
    separator()

    eular7()
    separator()

    eular8()
    separator()

    eular9()
    separator()

    # sum primes - takes a while
    eular10()
    separator()

    eular11()
    separator()

    # Triangle num
    eular12()
    separator()

    eular13()
    separator()

    #  eular14()
    separator()

    eular15()
    separator()

    eular16()
    separator()

    eular17()
    separator()

    eular18()
    separator()

    eular19()
    separator()

    eular20()
    separator()

    eular21()
    separator()

    eular22()
    separator()

    eular23()
    separator()

    eular24()
    separator()

    eular25()
    separator()
