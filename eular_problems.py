import bignumber
import factors
import fibseries
import matrix
import primes
import pythagorean
import palindrome
import text
import triangle


def separator():
    print('#'*80)


def eular1():
    print(text.eular1)
    result = factors.sum_multiples([3, 5], 1000)
    print('Sum = {}'.format(result))


def eular2():
    print(text.eular2)
    UPPERLIMIT = 4000000
    fibsum = sum([x for x in fibseries.fibonacci(UPPERLIMIT) if x % 2 == 0])
    print('Sum = {}'.format(fibsum))


def eular3():
    print(text.eular3)
    bignumber = 600851475143
    print('Largest prime factor of {}: {}'.format(
        bignumber, primes.max_prime_factor(bignumber)))


def eular4():
    print(text.eular4)
    print('Calculating the largest palindrome producable between the factors' +
          ' of 10 and 100')
    print(palindrome.get_largest_palindrome(10, 100))

    print('Calculating the largest palindrome producable between the factors' +
          ' of 100 and 1000')
    print(palindrome.get_largest_palindrome(100, 1000))


def eular5():
    print(text.eular5)
    testrange = 20
    n = factors.num_div_by_all_upto(testrange)

    print('Finding a number divisible by all the numbers 1-{}'.format(testrange))
    print("{} is a factor of all 1-{}!".format(n, testrange))


def eular6():
    print(text.eular6)
    upto = 100
    sum_of_sq = sum([i ** 2 for i in range(upto+1)])
    sq_of_sums = sum([i for i in range(upto + 1)]) ** 2

    print('Sum of squares(100) = {}'.format(sum_of_sq))
    print('Square of sums(100) = {}'.format(sq_of_sums))
    difference = abs(sq_of_sums - sum_of_sq)

    print('The difference between the sum of the squares of the first 100 ' +
          'numbers and the square of the sum is {}'.format(difference))


def eular7():
    print(text.eular7)
    targetprime = 10001
    print('Prime #{} = {}'.format(targetprime, primes.getprime(targetprime)))


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
    prime_sum = primes.sum_via_iteration(upperlimit)
    print('The sum of all primes up to {} = {}'.format(upperlimit, prime_sum))


def eular11():
    print(text.eular11)
    m = matrix.read_matrix('matrix1.txt')
    p = matrix.find_greatest_product(m, 4)
    print('The greatest product in the is {}'.format(p))


def eular12():
    print(text.eular12)
    for t in triangle.triangle_num():
        f = factors.divisors(t)

        if len(f) > 500:
            print('{} is the first triangle number to have over 500 divisors.'.format(t))
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

    eular10()
    separator()

    eular11()
    separator()

    eular12()
    separator()