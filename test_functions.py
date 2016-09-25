import unittest
import functions


class TestFunctions(unittest.TestCase):
    def test_ismultipleof_emptylist_returnFalse(self):
        expected = False
        result = functions.is_multiple_of(10, [])
        self.assertEqual(expected, result)

    def test_ismultipleof_1div1_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(1, [1])
        self.assertEqual(expected, result)

    def test_ismultipleof_0div1_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(0, [1])
        self.assertEqual(expected, result)

    def test_ismultipleof_1div0_RaiseException(self):
        self.assertRaises(ValueError, functions.is_multiple_of, 1, [0])

        #  expected = False
        #  result = functions.is_multiple_of(1, [0])
        #  self.assertEqual(expected, result)

    def test_ismultipleof_1div2_ReturnFalse(self):
        expected = False
        result = functions.is_multiple_of(1, [2])
        self.assertEqual(expected, result)

    def test_ismultipleof_4div2_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(4, [2])
        self.assertEqual(expected, result)

    def test_ismultipleof_3fromlist_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(3, [1, 2, 9])
        self.assertEqual(expected, result)

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

    def test_nextcollatz_1_returns4(self):
        expected = 4
        result = functions.next_collatz(1)
        self.assertEqual(expected, result)

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
    def test_collatzseq_neg1_raiseException(self):
        self.assertRaises(ValueError, functions.collatz_seq, -1)

    def test_collatzseq_0_raiseException(self):
        self.assertRaises(ValueError, functions.collatz_seq, 0)

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
    def test_numdivbyallupto_1_returns1(self):
        expected = 1
        result = functions.num_div_by_all_upto(1)
        self.assertEqual(expected, result)

    def test_numdivbyallupto_2_returns2(self):
        expected = 2
        result = functions.num_div_by_all_upto(2)
        self.assertEqual(expected, result)

    def test_numdivbyallupto_3_returns6(self):
        expected = 6
        result = functions.num_div_by_all_upto(3)
        self.assertEqual(expected, result)

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

    # Tests for factorial(n):
    def test_factorial_neg1_RaiseException(self):
        self.assertRaises(ValueError, functions.factorial, -1)

    def test_factorial_0_(self):
        self.assertRaises(ValueError, functions.factorial, 0)

    def test_factorial_1_returns1(self):
        expected = 1
        result = functions.factorial(1)
        self.assertEqual(expected, result)

    def test_factorial_2_returns2(self):
        expected = 2
        result = functions.factorial(2)
        self.assertEqual(expected, result)

    def test_factorial_3_returns6(self):
        expected = 6
        result = functions.factorial(3)
        self.assertEqual(expected, result)

    # Tests for add_digits(n):
    def test_adddigits_1_returns1(self):
        expected = 1
        result = functions.add_digits(1)
        self.assertEqual(expected, result)

    def test_adddigits_1_2_returns3(self):
        expected = 3
        result = functions.add_digits(12)
        self.assertEqual(expected, result)

    def test_adddigits_1_2_3_returns6(self):
        expected = 6
        result = functions.add_digits(123)
        self.assertEqual(expected, result)

    def test_adddigits_2_2_9_7_returns20(self):
        expected = 20
        result = functions.add_digits(2297)
        self.assertEqual(expected, result)

    """
    Tests for is_prime(target):
    """
    def test_isprime_0_returnFalse(self):
        expected = False
        result = functions.isprime_2step(0)
        self.assertEqual(expected, result)

    def test_isprime_1_returnFalse(self):
        expected = False
        result = functions.isprime_2step(1)
        self.assertEqual(expected, result)

    def test_isprime_2_returnTrue(self):
        expected = True
        result = functions.isprime_2step(2)
        self.assertEqual(expected, result)

    def test_isprime_3_returnTrue(self):
        expected = True
        result = functions.isprime_2step(3)
        self.assertEqual(expected, result)

    """
    Tests for max_prime_factor(target):
    """
    def test_maxprimefactor_0_returnNone(self):
        expected = None
        result = functions.max_prime_factor(0)
        self.assertEqual(expected, result)

    def test_maxprimefactor_1_returnNone(self):
        expected = None
        result = functions.max_prime_factor(1)
        self.assertEqual(expected, result)

    def test_maxprimefactor_2_return2(self):
        expected = 2
        result = functions.max_prime_factor(2)
        self.assertEqual(expected, result)

    def test_maxprimefactor_3_return3(self):
        expected = 3
        result = functions.max_prime_factor(3)
        self.assertEqual(expected, result)

    def test_maxprimefactor_4_return2(self):
        expected = 2
        result = functions.max_prime_factor(4)
        self.assertEqual(expected, result)

    def test_maxprimefactor_10_return5(self):
        expected = 5
        result = functions.max_prime_factor(10)
        self.assertEqual(expected, result)

    def test_maxprimefactor_100_return5(self):
        expected = 5
        result = functions.max_prime_factor(100)
        self.assertEqual(expected, result)

    def test_maxprimefactor_1000_return5(self):
        expected = 5
        result = functions.max_prime_factor(1000)
        self.assertEqual(expected, result)

    """
    Tests for getprime(index):
    """
    def test_getprime_neg1_raiseException(self):
        self.assertRaises(ValueError, functions.getprime, -1)

    def test_getprime_0_returns2(self):
        expected = 2
        result = functions.getprime(0)
        self.assertEqual(expected, result)

    def test_getprime_1_returns3(self):
        expected = 3
        result = functions.getprime(1)
        self.assertEqual(expected, result)

    def test_getprime_2_returns5(self):
        expected = 5
        result = functions.getprime(2)
        self.assertEqual(expected, result)

    """
    Tests for def generate_primes(n)
    """
    def test_generateprimes_0_raiseException(self):
        self.assertRaises(ValueError, functions.generate_primes, 0)

    def test_generateprimes_2_return2(self):
        expected = [2]
        result = functions.generate_primes(2)
        self.assertEqual(expected, result)

    def test_generateprimes_3_return2_3(self):
        expected = [2, 3]
        result = functions.generate_primes(3)
        self.assertEqual(expected, result)

    def test_generateprimes_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = functions.generate_primes(11)
        self.assertEqual(expected, result)

    """
    Tests for def sieve_rm_method(n):
    """
    def test__0_raiseException(self):
        self.assertRaises(ValueError, functions.sieve_rm_method, 0)

    def test_sievermmethod_2_return2(self):
        expected = [2]
        result = functions.sieve_rm_method(2)
        self.assertEqual(expected, result)

    def test_sievermmethod_3_return2_3(self):
        expected = [2, 3]
        result = functions.sieve_rm_method(3)
        self.assertEqual(expected, result)

    def test_sievermmethod_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = functions.sieve_rm_method(11)
        self.assertEqual(expected, result)

    def test_sievermmethod_20_returns5primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = functions.sieve_rm_method(20)
        self.assertEqual(expected, result)

    """
    Tests for def sieve_markers(n):
    """
    def test_sievemarkers_0_raiseException(self):
        self.assertRaises(ValueError, functions.sieve_markers, 0)

    def test_sievemarkers_2_return2(self):
        expected = [2]
        result = functions.sieve_markers(2)
        self.assertEqual(expected, result)

    def test_sievemarkers_3_return2_3(self):
        expected = [2, 3]
        result = functions.sieve_markers(3)
        self.assertEqual(expected, result)

    def test_sievemarkers_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = functions.sieve_markers(11)
        self.assertEqual(expected, result)

    def test_sievemarkers_20_returns8primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = functions.sieve_markers(20)
        self.assertEqual(expected, result)

    """
    Tests for get_prime_factors(target):
    """
    # of -1 = None
    def test_getprimefactors_neg1_returnsNone(self):
        expected = None
        result = functions.get_prime_factors(-1)
        self.assertEqual(expected, result)

    # of 0 = None
    def test_getprimefactors_0_returnsNone(self):
        expected = None
        result = functions.get_prime_factors(0)
        self.assertEqual(expected, result)

    # of 1 = None
    def test_getprimefactors_1_returnsNone(self):
        expected = None
        result = functions.get_prime_factors(1)
        self.assertEqual(expected, result)

    # of 2 = 2
    def test_getprimefactors_2_returns2(self):
        expected = {2}
        result = functions.get_prime_factors(2)
        self.assertEqual(expected, result)

    # of 3 = 3
    def test_getprimefactors_3_returns3(self):
        expected = {3}
        result = functions.get_prime_factors(3)
        self.assertEqual(expected, result)

    # of 4 = 2
    def test_getprimefactors_4_returns2(self):
        expected = {2}
        result = functions.get_prime_factors(4)
        self.assertEqual(expected, result)

    # of 5 = 5
    def test_getprimefactors_5_returns5(self):
        expected = {5}
        result = functions.get_prime_factors(5)
        self.assertEqual(expected, result)

    # of 6 = 2, 3
    def test_getprimefactors_6_returns2_3(self):
        expected = {2, 3}
        result = functions.get_prime_factors(6)
        self.assertEqual(expected, result)

    # of 7 = 7
    def test_getprimefactors_7_returns7(self):
        expected = {7}
        result = functions.get_prime_factors(7)
        self.assertEqual(expected, result)

    # of 10 = 2, 5
    def test_getprimefactors_10_returns2_5(self):
        expected = {2, 5}
        result = functions.get_prime_factors(10)
        self.assertEqual(expected, result)

    # of 12 = 2, 3
    def test_getprimefactors_12_returns2_3(self):
        expected = {2, 3}
        result = functions.get_prime_factors(12)
        self.assertEqual(expected, result)

    # of 24 = 2, 3
    def test_getprimefactors_24_returns2_3(self):
        expected = {2, 3}
        result = functions.get_prime_factors(24)
        self.assertEqual(expected, result)

    # Tests for bruteforce(n):
    def test_bruteforce_0_raiseException(self):
        self.assertRaises(ValueError, functions.bruteforce, 0)

    # 1 has 1 factor: 1
    def test_bruteforce_1_returns1(self):
        expected = {1}
        result = functions.bruteforce(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_bruteforce_2_returns2factors(self):
        expected = {1, 2}
        result = functions.bruteforce(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_bruteforce_3_returns2factors(self):
        expected = {1, 3}
        result = functions.bruteforce(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_bruteforce_4_returns3factors(self):
        expected = {1, 2, 4}
        result = functions.bruteforce(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_bruteforce_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = functions.bruteforce(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_bruteforce_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = functions.bruteforce(24)
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
        result = functions.d(1)
        self.assertEqual(expected, result)

    # Proper divisors of 2 = 1. Sum = 1
    def test_d_2_returns1(self):
        expected = 1
        result = functions.d(2)
        self.assertEqual(expected, result)

    # Proper divisors of 3 = 1. Sum = 1
    def test_d_3_returns1(self):
        expected = 1
        result = functions.d(3)
        self.assertEqual(expected, result)

    # Proper divisors of 4 = 1, 2. Sum = 3
    def test_d_4_returns3(self):
        expected = 3
        result = functions.d(4)
        self.assertEqual(expected, result)

    # Proper divisors of 6 = 1, 2, 3. Sum = 6
    def test_d_6_returns6(self):
        expected = 6
        result = functions.d(6)
        self.assertEqual(expected, result)

    # Tests for amicable(a, b):
    def test_amicable_1_2_returnsFalse(self):
        expected = False
        result = functions.is_amicable(1, 2)
        self.assertEqual(expected, result)

    def test_amicable_1_1_returnsFalse(self):
        expected = False
        result = functions.is_amicable(1, 1)
        self.assertEqual(expected, result)

    def test_amicable_220_284_returnsTrue(self):
        expected = True
        result = functions.is_amicable(220, 284)
        self.assertEqual(expected, result)
