import alphanumbers
import bignumber
import countingdays
import filework
import functions
import itertools
import matrix
import numbertree
import pythagorean
import text


def separator():
    print('#'*80)


def eular1():
    print(text.eular1)
    result = functions.sum_multiples([3, 5], 1000)
    print('Sum = {}'.format(result))


def eular2():
    print(text.eular2)
    UPPERLIMIT = 4000000
    fibsum = sum([x for x in functions.fibonacci(UPPERLIMIT) if x % 2 == 0])
    print('Sum = {}'.format(fibsum))


def eular3():
    print(text.eular3)
    bignumber = 600851475143
    print('Largest prime factor of {}: {}'.format(
        bignumber, functions.max_prime_factor(bignumber)))


def eular4():
    print(text.eular4)
    print('Calculating the largest palindrome producable between the factors' +
          ' of 10 and 100')
    print(functions.get_largest_palindrome(10, 100))

    print('Calculating the largest palindrome producable between the factors' +
          ' of 100 and 1000')
    print(functions.get_largest_palindrome(100, 1000))


def eular5():
    print(text.eular5)
    testrange = 20
    n = functions.num_div_by_all_upto(testrange)

    print('Finding a number divisible by all the numbers 1-{}'.format(testrange))
    print("{} is a factor of all 1-{}!".format(n, testrange))


def eular6():
    print(text.eular6)
    upto = 100
    sum_of_sq = functions.sum_of_squares(upto+1)

    sq_of_sum = functions.square_of_sum(upto+1)

    print('Sum of squares(100) = {}'.format(sum_of_sq))
    print('Square of sums(100) = {}'.format(sq_of_sum))
    difference = abs(sq_of_sum - sum_of_sq)

    print('The difference between the sum of the squares of the first 100 ' +
          'numbers and the square of the sum is {}'.format(difference))


def eular7():
    print(text.eular7)
    targetprime = 10001
    print('Prime #{} = {}'.format(targetprime, functions.getprime(targetprime)))


def eular8():
    print(text.eular8)
    FACTORS = 13
    filename = 'eular8.txt'
    digits = bignumber.read_file_to_list(filename)
    p = bignumber.find_product_in_list(digits, FACTORS)
    print('The largest product is {}'.format(p))


def eular9():
    print(text.eular9)
    a, b, c = pythagorean.iterative_solution()
    print('a^2 + b^2 = c^2')
    print('{} + {} = {}'.format(a ** 2, b ** 2, c ** 2))
    print('{} + {} + {} = 1000!'.format(a, b, c))
    print('The product abc = {}'.format(a * b * c))


def eular10():
    print(text.eular10)
    upperlimit = 2000000
    prime_sum = functions.sum_via_iteration(upperlimit)
    print('The sum of all primes up to {} = {}'.format(upperlimit, prime_sum))


def eular11():
    print(text.eular11)
    m = matrix.read_matrix('matrix1.txt')
    p = matrix.find_greatest_product(m, 4)
    print('The greatest product in the is {}'.format(p))


def eular12():
    print(text.eular12)
    for t in functions.triangle_num():
        f = functions.divisors(t)

        if len(f) > 500:
            print('{} is the first triangle number to have over 500 divisors.'.format(t))
            break


def eular13():
    print(text.eular13)
    n = bignumber.read_numbers('bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x
        print(x)

    print('sum = {}'.format(bigsum))
    sum_list = list(str(bigsum))
    first_ten_digits = sum_list[-10:]
    print(first_ten_digits)


def eular14():
    print(text.eular14)
    functions.longest_collatz_seq(1000000)


def eular15():
    print(text.eular15)
    for i in range(1, 21):
        remembered = {}
        print('{} routes in a {}x{} grid!'.format(functions.find_all_routes(i, remembered), i, i))


def eular16():
    print(text.eular16)
    print(sum([int(x) for x in str(2 ** 1000)]))


def eular17():
    print(text.eular17)
    letters = 0
    for i in range(1, 1001):
        number = alphanumbers.num_to_alpha(i)
        qty = alphanumbers.letter_qty(number)
        print('{} has {} letters'.format(number, qty))
        letters += qty

    print('It take {} letter to represent all the numbers in 1-1000'.format(letters))


def eular18():
    print(text.eular18)
    tree = matrix.read_matrix('number_tree.txt')
    print(matrix.print_matrix(tree))
    print()
    numbertree.find_max_path(tree)


def eular19():
    print(text.eular19)
    print('There were {} Sundays counted.'.format(countingdays.count_sundays()))


def eular20():
    print(text.eular20)
    num = 100
    fact = functions.factorial(num)
    print('The factorial of {}! = {}'.format(num, fact))
    print('The sum of the digits in {}! = {}'.format(num, functions.add_digits(fact)))
    print('or using the super shorted version: {}'.format(functions.fact_sum(num)))


def eular21():
    print(text.eular21)
    LIMIT = 10000
    # Add all of the amicable numbers together
    print('The sum of all amicables #s up to {} = {}'.format(LIMIT, functions.add_amicable_numbers(10000)))


def eular22():
    print(text.eular22)
    names = filework.import_names('names.txt')
    print('names has {} entries.'.format(len(names)))
    namescore = 0

    for i, n in enumerate(names):
        namescore += functions.alphabetical_value(n) * (i+1)

    print('The total of all name scores = {}'.format(namescore))


def eular23():
    print(text.eular23)
    LIMIT = 28123
    abundants = [i for i in range(1, LIMIT + 1) if functions.is_abundant(i)]
    sums = set([a + abundants[b]
                for i, a in enumerate(abundants)
                for b in range(i, len(abundants))])
    unsummable = [i for i in range(LIMIT + 1) if i not in sums]

    print('Sum of all positive ints which can\'t be summed by 2 abundants={}'.format(
        sum(unsummable)))


def eular24():
    print(text.eular24)
    perms = list(itertools.permutations(str('0123456789'), len('0123456789')))
    print(''.join(perms[999999]))


def eular25():
    print(text.eular25)
    for i, x in enumerate(functions.fibonacci()):
        if len(str(x)) >= 1000:
            print('Term {} has over 1000 digits!'.format(i+1))
            break

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
    #  eular10()
    separator()

    eular11()
    separator()

    # Triangle num
    #  eular12()
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
