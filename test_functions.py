import unittest
import functions


class TestFunctions(unittest.TestCase):
    """
    Tests for abundant(n):
    """

    """
    Tests for abundants_upto(limit):
    """
    def test_abundantsupto_12_returns12(self):
        expected = [12]
        result = functions.abundants_upto(12)
        self.assertEqual(expected, result)

    """
    Tests for add_amicables(limit):
    """

    """
    Tests for alphabetical_value(name):
    """

    """
    Tests for collatz_seq(n, collatz_dict={}):
    """
    def test_collatzseq_1_returns1(self):
        expected = [1]
        result = functions.collatz_seq(1)
        self.assertEqual(expected, result)

    def test_collatzseq_2_returns2_1(self):
        expected = [2, 1]
        result = functions.collatz_seq(2)
        self.assertEqual(expected, result)

    def test_collatzseq_3_returns3_10_5_16_8_4_2_1(self):
        expected = [3, 10, 5, 16, 8, 4, 2, 1]
        result = functions.collatz_seq(3)
        self.assertEqual(expected, result)

    def test_collatzseq_4_returns4_2_1(self):
        expected = [4, 2, 1]
        result = functions.collatz_seq(4)
        self.assertEqual(expected, result)

    def test_collatzseq_5_returns5_16_8_4_2_1(self):
        expected = [5, 16, 8, 4, 2, 1]
        result = functions.collatz_seq(5)
        self.assertEqual(expected, result)

    """
    Tests for div_by_all_upto(upto):
    """
    def test_divbyallupto_1_raiseException(self):
        self.assertRaises(ValueError, functions.div_by_all_upto, 1)

    def test_divbyallupto_2_raisesException(self):
        self.assertRaises(ValueError, functions.div_by_all_upto, 1)

    def test_divbyallupto_15_raisesException(self):
        self.assertRaises(ValueError, functions.div_by_all_upto, 15)

    def test_divbyallupto_10_returns2520(self):
        expected = 2520
        result = functions.div_by_all_upto(10)
        self.assertEqual(expected, result)

    """
    Tests for divisors_proper(n)
    """
    def test_divisorsproper_7_returns1(self):
        expected = {1}
        result = functions.divisors_proper(7)
        self.assertEqual(expected, result)

    def test_divisorsproper_24_returns7factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12}
        result = functions.divisors_proper(24)
        self.assertEqual(expected, result)

    """
    Tests for divisor_sum_dict(limit):
    """

    """
    Tests for factor_of_all_upto(num, limit):
    """
    def test_factorofallupto_1_upto1_returnTrue(self):
        expected = True
        result = functions.factor_of_all_upto(1, 1)
        self.assertEqual(expected, result)

    def test_factorofallupto_1_upto2_returnFalse(self):
        expected = False
        result = functions.factor_of_all_upto(1, 2)
        self.assertEqual(expected, result)

    def test_factorofallupto_2520_upto10_returnTrue(self):
        expected = True
        result = functions.factor_of_all_upto(2520, 10)
        self.assertEqual(expected, result)

    """
    Tests for factorial_sum(n)
    """

    """
    Tests for fibonaccis():
    """
    def test_fibonaccis_call1_return1(self):
        f = functions.fibonaccis()
        expected = 1
        result = next(f)
        self.assertEqual(expected, result)

    def test_fibonaccis_call2_return1(self):
        f = functions.fibonaccis()
        expected = 1
        next(f)
        result = next(f)
        self.assertEqual(expected, result)

    def test_fibonaccis_call3_return2(self):
        f = functions.fibonaccis()
        expected = 2
        next(f)
        next(f)
        result = next(f)
        self.assertEqual(expected, result)

    def test_fibonaccis_call4_return3(self):
        f = functions.fibonaccis()
        expected = 3
        next(f)
        next(f)
        next(f)
        result = next(f)
        self.assertEqual(expected, result)

    """
    Tests for is_palindrome(n):
    """
    def test_ispalindrome_emptyString_returnFalse(self):
        expected = False
        result = functions.is_palindrome('')
        self.assertEqual(expected, result)

    def test_ispalindrome_1_returnTrue(self):
        expected = True
        result = functions.is_palindrome(1)
        self.assertEqual(expected, result)

    def test_ispalindrome_10_returnFalse(self):
        expected = False
        result = functions.is_palindrome(10)
        self.assertEqual(expected, result)

    def test_ispalindrome_11_returnTrue(self):
        expected = True
        result = functions.is_palindrome(11)
        self.assertEqual(expected, result)

    def test_ispalindrome_101_returnTrue(self):
        expected = True
        result = functions.is_palindrome(101)
        self.assertEqual(expected, result)

    def test_ispalindrome_110_returnFalse(self):
        expected = False
        result = functions.is_palindrome(110)
        self.assertEqual(expected, result)

    """
    Tests for largest_palindrome(lowerlimit, upperlimit):
    """
    def test_largestpalindrome_2digit_returns9009(self):
        expected = 9009
        result = functions.largest_palindrome(10, 100)
        self.assertEqual(expected, result)

    """
    Tests for longest_collatz_seq(upto):
    """

    """
    Tests for next_collatz(n):
    """
    def test_nextcollatz_neg1_raiseException(self):
        self.assertRaises(ValueError, functions.next_collatz, -1)

    def test_nextcollatz_0_raiseException(self):
        self.assertRaises(ValueError, functions.next_collatz, 0)

    def test_nextcollatz_1_raiseException(self):
        self.assertRaises(ValueError, functions.next_collatz, 1)

    def test_nextcollatz_2_returns1(self):
        expected = 1
        result = functions.next_collatz(2)
        self.assertEqual(expected, result)

    def test_nextcollatz_3_returns10(self):
        expected = 10
        result = functions.next_collatz(3)
        self.assertEqual(expected, result)

    def test_nextcollatz_4_returns2(self):
        expected = 2
        result = functions.next_collatz(4)
        self.assertEqual(expected, result)

    def test_nextcollatz_5_returns16(self):
        expected = 16
        result = functions.next_collatz(5)
        self.assertEqual(expected, result)

    """
    Tests for nonsummable_by_abundants():
    """

    """
    Tests for sum_of_squares(upto):
    """
    def test_sumofsquares_upto0_returns0(self):
        expected = 0
        result = functions.sum_of_squares(0)
        self.assertEqual(expected, result)

    def test_sumofsquares_upto1_returns1(self):
        expected = 1
        result = functions.sum_of_squares(1)
        self.assertEqual(expected, result)

    def test_sumofsquares_upto2_returns5(self):
        expected = 5
        result = functions.sum_of_squares(2)
        self.assertEqual(expected, result)

    """
    Tests for sum_proper_divisors(n):
    """
    # Proper divisors of 1 = None. Sum = 0
    def test_sumproperdivisors_1_returns0(self):
        expected = 0
        result = functions.sum_proper_divisors(1)
        self.assertEqual(expected, result)

    # Proper divisors of 2 = 1. Sum = 1
    def test_sumproperdivisors_2_returns1(self):
        expected = 1
        result = functions.sum_proper_divisors(2)
        self.assertEqual(expected, result)

    # Proper divisors of 3 = 1. Sum = 1
    def test_sumproperdivisors_3_returns1(self):
        expected = 1
        result = functions.sum_proper_divisors(3)
        self.assertEqual(expected, result)

    # Proper divisors of 4 = 1, 2. Sum = 3
    def test_sumproperdivisors_4_returns3(self):
        expected = 3
        result = functions.sum_proper_divisors(4)
        self.assertEqual(expected, result)

    # Proper divisors of 6 = 1, 2, 3. Sum = 6
    def test_sumproperdivisors_6_returns6(self):
        expected = 6
        result = functions.sum_proper_divisors(6)
        self.assertEqual(expected, result)

    """
    Tests for square_of_sum(upto):
    """
    def test_squareofsum_upto1_returns0(self):
        expected = 0
        result = functions.square_of_sum(0)
        self.assertEqual(expected, result)

    def test_squareofsum_upto1_returns1(self):
        expected = 1
        result = functions.square_of_sum(1)
        self.assertEqual(expected, result)

    def test_squareofsum_upto2_returns9(self):
        expected = 9
        result = functions.square_of_sum(2)
        self.assertEqual(expected, result)

    """
    Tests for triangle_numbers()
    """
    # Call 1 returns 1
    def test_trianglenum_call1_returns1(self):
        expected = 1
        gen = functions.triangles()
        result = next(gen)
        self.assertEqual(expected, result)

    # Call 2 returns 1
    def test_trianglenum_call2_returns3(self):
        expected = 3
        gen = functions.triangles()
        result = next(gen)
        result = next(gen)
        self.assertEqual(expected, result)

    # Call 3 returns 1
    def test_trianglenum_call3_returns6(self):
        expected = 6
        gen = functions.triangles()
        result = next(gen)
        result = next(gen)
        result = next(gen)
        self.assertEqual(expected, result)


def test_fromprime(n):
    """
    This is a thorough test of divisors and divisors_bruteforce that compares both.
    """
    failures = 0

    for i in range(1, n):
        bf = functions.divisors_bruteforce(i)
        fp = functions.divisors(i)

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


class TestDivisors:
    def setUp(self):
        self.div = self.getImpl()  # call to factory method

    # Tests for divisors(n):
    def test_divisors_0_raiseException(self):
        self.assertRaises(ValueError, self.div, 0)

    # 1 has 1 factor: 1
    def test_divisors_1_returns1(self):
        expected = {1}
        result = self.div(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisors_2_returns2factors(self):
        expected = {1, 2}
        result = self.div(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisors_3_returns2factors(self):
        expected = {1, 3}
        result = self.div(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisors_4_returns3factors(self):
        expected = {1, 2, 4}
        result = self.div(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_divisors_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = self.div(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_divisors_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = self.div(24)
        self.assertEqual(expected, result)


class Test_Divisors(TestDivisors, unittest.TestCase):
    def getImpl(self):
        return functions.divisors


class Test_DivisorsBruteForce(TestDivisors, unittest.TestCase):
    def getImpl(self):
        return functions.divisors_bruteforce
