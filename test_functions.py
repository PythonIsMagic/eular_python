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

    # Tests for calcsum(upto):
    def test_calcsumofevens_upto0_return0(self):
        expected = 0
        result = functions.calc_sum_of_evens(0)
        self.assertEqual(expected, result)

    def test_calcsumofevens_upto1_return0(self):
        expected = 0
        result = functions.calc_sum_of_evens(1)
        self.assertEqual(expected, result)

    def test_calcsumofevens_upto2_return2(self):
        expected = 2
        result = functions.calc_sum_of_evens(2)
        self.assertEqual(expected, result)

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
