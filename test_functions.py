import unittest
import functions


class TestFunctions(unittest.TestCase):
    # Tests for triangle_num()
    # Call 1 returns 1
    def test_trianglenum_call1_returns1(self):
        expected = 1
        gen = functions.triangle_num()
        #  result = gen.__next__()
        result = next(gen)
        self.assertEqual(expected, result)

    # Call 2 returns 1
    def test_trianglenum_call2_returns3(self):
        expected = 3
        gen = functions.triangle_num()
        #  result = gen.__next__()
        #  result = gen.__next__()
        result = next(gen)
        result = next(gen)
        self.assertEqual(expected, result)

    # Call 3 returns 1
    def test_trianglenum_call3_returns6(self):
        expected = 6
        gen = functions.triangle_num()
        #  result = gen.__next__()
        #  result = gen.__next__()
        #  result = gen.__next__()
        result = next(gen)
        result = next(gen)
        result = next(gen)
        self.assertEqual(expected, result)

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

    # Tests for collatz_seq(n):
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

    # Tests for fibonacci():
    def test_fibonacci_call1_return1(self):
        expected = 1
        calls = 0
        for i, result in enumerate(functions.fibonacci()):
            if i >= calls:
                self.assertEqual(expected, result)
                break

    def test_fibonacci_call2_return1(self):
        expected = 1
        calls = 1
        for i, result in enumerate(functions.fibonacci()):
            if i >= calls:
                self.assertEqual(expected, result)
                break

    # Tests for ispalindrome(number):
    def test_ispalindrome_emptyString_returnFalse(self):
        expected = False
        result = functions.ispalindrome('')
        self.assertEqual(expected, result)

    def test_ispalindrome_1_returnTrue(self):
        expected = True
        result = functions.ispalindrome(1)
        self.assertEqual(expected, result)

    def test_ispalindrome_10_returnFalse(self):
        expected = False
        result = functions.ispalindrome(10)
        self.assertEqual(expected, result)

    def test_ispalindrome_11_returnTrue(self):
        expected = True
        result = functions.ispalindrome(11)
        self.assertEqual(expected, result)

    def test_ispalindrome_101_returnTrue(self):
        expected = True
        result = functions.ispalindrome(101)
        self.assertEqual(expected, result)

    def test_ispalindrome_110_returnFalse(self):
        expected = False
        result = functions.ispalindrome(110)
        self.assertEqual(expected, result)

    # Tests for get_largest_palindrome(lowerlimit, upperlimit):
    def test_getlargestpalindrome_2digit_returns9009(self):
        expected = 9009
        result = functions.get_largest_palindrome(10, 100)
        self.assertEqual(expected, result)

    # Tests for isfactorofall(number, upto):
    def test_isfactorofall_1_upto1_returnTrue(self):
        expected = True
        result = functions.isfactorofall(1, 1)
        self.assertEqual(expected, result)

    def test_isfactorofall_1_upto2_returnFalse(self):
        expected = False
        result = functions.isfactorofall(1, 2)
        self.assertEqual(expected, result)

    def test_isfactorofall_2520_upto10_returnTrue(self):
        expected = True
        result = functions.isfactorofall(2520, 10)
        self.assertEqual(expected, result)

    # Tests for num_div_by_all_upto(upto):
    def test_numdivbyallupto_1_raiseException(self):
        self.assertRaises(ValueError, functions.num_div_by_all_upto, 1)

    def test_numdivbyallupto_2_raisesException(self):
        self.assertRaises(ValueError, functions.num_div_by_all_upto, 1)

    def test_numdivbyallupto_15_raisesException(self):
        self.assertRaises(ValueError, functions.num_div_by_all_upto, 15)

    def test_numdivbyallupto_10_returns2520(self):
        expected = 2520
        result = functions.num_div_by_all_upto(10)
        self.assertEqual(expected, result)

    # Tests for sum_of_squares(upto):
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

    # Tests for square_of_sum(upto):
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

    # Tests for bruteforce(n):
    def test_bruteforce_0_raiseException(self):
        self.assertRaises(ValueError, functions.divisors_bruteforce, 0)

    # 1 has 1 factor: 1
    def test_bruteforce_1_returns1(self):
        expected = {1}
        result = functions.divisors_bruteforce(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_bruteforce_2_returns2factors(self):
        expected = {1, 2}
        result = functions.divisors_bruteforce(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_bruteforce_3_returns2factors(self):
        expected = {1, 3}
        result = functions.divisors_bruteforce(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_bruteforce_4_returns3factors(self):
        expected = {1, 2, 4}
        result = functions.divisors_bruteforce(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_bruteforce_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = functions.divisors_bruteforce(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_bruteforce_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = functions.divisors_bruteforce(24)
        self.assertEqual(expected, result)

    # 13195 has x factors:

    # Tests for divisors(n):
    def test_divisors_0_raiseException(self):
        self.assertRaises(ValueError, functions.divisors, 0)

    # 1 has 1 factor: 1
    def test_divisors_1_returns1(self):
        expected = {1}
        result = functions.divisors(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisors_2_returns2factors(self):
        expected = {1, 2}
        result = functions.divisors(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisors_3_returns2factors(self):
        expected = {1, 3}
        result = functions.divisors(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisors_4_returns3factors(self):
        expected = {1, 2, 4}
        result = functions.divisors(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_divisors_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = functions.divisors(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_divisors_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = functions.divisors(24)
        self.assertEqual(expected, result)

    # 13195 has x factors:

    # Tests for proper_divisors(n)
    def test_properdivisors_7_returns1(self):
        expected = {1}
        result = functions.proper_divisors(7)
        self.assertEqual(expected, result)

    def test_properdivisors_24_returns7factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12}
        result = functions.proper_divisors(24)
        self.assertEqual(expected, result)

    # Tests for d(n)
    # Proper divisors of 1 = None. Sum = 0
    def test_d_1_returns0(self):
        expected = 0
        result = functions.sum_proper_divisors(1)
        self.assertEqual(expected, result)

    # Proper divisors of 2 = 1. Sum = 1
    def test_d_2_returns1(self):
        expected = 1
        result = functions.sum_proper_divisors(2)
        self.assertEqual(expected, result)

    # Proper divisors of 3 = 1. Sum = 1
    def test_d_3_returns1(self):
        expected = 1
        result = functions.sum_proper_divisors(3)
        self.assertEqual(expected, result)

    # Proper divisors of 4 = 1, 2. Sum = 3
    def test_d_4_returns3(self):
        expected = 3
        result = functions.sum_proper_divisors(4)
        self.assertEqual(expected, result)

    # Proper divisors of 6 = 1, 2, 3. Sum = 6
    def test_d_6_returns6(self):
        expected = 6
        result = functions.sum_proper_divisors(6)
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
