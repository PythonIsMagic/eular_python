"""
  " Unittest tests for eular_functions.py
  """
import unittest
import functions


class TestEularFunctions(unittest.TestCase):
    """ Function tests """
    def test_abundantsupto_12_returns12(self):
        expected = [12]
        result = functions.abundants_upto(12)
        self.assertEqual(expected, result)

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

    def test_largestpalindrome_2digit_returns9009(self):
        expected = 9009
        result = functions.largest_palindrome(10, 100)
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

    # January has 31 days
    def test_getdays_1_returns31(self):
        expected = 31
        result = functions.get_days(1)
        self.assertEqual(expected, result)

    # February. No year passed raises an exception - we need that.
    def test_getdays_noyear_raisesException(self):
        self.assertRaises(ValueError, functions.get_days, 2)

    # February has 29 days for a leap-year.
    def test_getdays_2_year2004_returns29(self):
        expected = 29
        result = functions.get_days(2, 2004)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year.
    def test_getdays_2_year2001_returns28(self):
        expected = 28
        result = functions.get_days(2, 2001)
        self.assertEqual(expected, result)

    # March has 31 days
    def test_getdays_3_returns31(self):
        expected = 31
        result = functions.get_days(3)
        self.assertEqual(expected, result)

    # April has 30 days
    def test_getdays_4_returns30(self):
        expected = 30
        result = functions.get_days(4)
        self.assertEqual(expected, result)

    # May has 31 days
    def test_getdays_5_returns31(self):
        expected = 31
        result = functions.get_days(5)
        self.assertEqual(expected, result)

    # June has 30 days
    def test_getdays_6_returns30(self):
        expected = 30
        result = functions.get_days(6)
        self.assertEqual(expected, result)

    # July has 31 days
    def test_getdays_7_returns31(self):
        expected = 31
        result = functions.get_days(7)
        self.assertEqual(expected, result)

    # August has 31 days
    def test_getdays_8_returns31(self):
        expected = 31
        result = functions.get_days(8)
        self.assertEqual(expected, result)

    # September has 30 days
    def test_getdays_9_returns30(self):
        expected = 30
        result = functions.get_days(9)
        self.assertEqual(expected, result)

    # October has 31 days
    def test_getdays_10_returns31(self):
        expected = 31
        result = functions.get_days(10)
        self.assertEqual(expected, result)

    # November has 30 days
    def test_getdays_11_returns30(self):
        expected = 30
        result = functions.get_days(11)
        self.assertEqual(expected, result)

    # December has 31 days
    def test_getdays_12_returns31(self):
        expected = 31
        result = functions.get_days(12)
        self.assertEqual(expected, result)

    # Tests for is_leap_year(year)
    # February has 29 days for a leap-year. Year = 0 = leap year.
    def test_isleapyear_0_returnsTrue(self):
        expected = True
        result = functions.is_leap_year(0)
        self.assertEqual(expected, result)

    # February has 29 days for a century leap-year. Year divisible by 400.
    def test_isleapyear_2000_returnsTrue(self):
        expected = True
        result = functions.is_leap_year(2000)
        self.assertEqual(expected, result)

    # February has 29 days for a leap-year. Divisible by 4.
    def test_isleapyear_2004_returnsTrue(self):
        expected = True
        result = functions.is_leap_year(2004)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year.
    def test_isleapyear_2001_returnsFalse(self):
        expected = False
        result = functions.is_leap_year(2001)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year. Year is not divisible by 400.
    def test_isleapyear_2100_returnsFalse(self):
        expected = False
        result = functions.is_leap_year(2100)
        self.assertEqual(expected, result)

    # Tests for sum_of_squares(upto):

    # Tests for read_file_to_list(filename)
    def test_readfiletolist_just1_listIs1(self):
        expected = [1]
        result = functions.read_file_to_list('data/test_digits1.txt')
        self.assertEqual(expected, result)

    def test_readfiletolist_3x3digits_listmatches(self):
        expected = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        result = functions.read_file_to_list('data/test_digits2.txt')
        self.assertEqual(expected, result)

    # Tests for calculate_product(alist)
    def test_calculateproduct_1_returns1(self):
        expected = 1
        test_list = [1]
        result = functions.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_1x2_returns2(self):
        expected = 2
        test_list = [1, 2]
        result = functions.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_1x2x3_returns6(self):
        expected = 6
        test_list = [1, 2, 3]
        result = functions.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_0x2x3_returns0(self):
        expected = 0
        test_list = [0, 2, 3]
        result = functions.calculate_product(test_list)
        self.assertEqual(expected, result)

    # Tests for find_product_in_list(alist, factors)
    def test_findproductinlist_1to9_3factors_returns504(self):
        factors = 3
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 504
        result = functions.find_product_in_list(test_list, factors)
        self.assertEqual(expected, result)

    def test_findproductinlist_1to9_2factors_returns72(self):
        factors = 2
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 72
        result = functions.find_product_in_list(test_list, factors)
        self.assertEqual(expected, result)

    # Tests for num_to_list(n):
    def test_numtolist_0_returns0(self):
        expected = [0]
        result = functions.num_to_list(0)
        self.assertEqual(expected, result)

    def test_numtolist_10_returns1_0(self):
        expected = [1, 0]
        result = functions.num_to_list(10)
        self.assertEqual(expected, result)

    # Tests for get_digit(n, i)

    # Tests get_ones_digit(n):
    def test_getdigit_n0_ones_returns0(self):
        expected = 0
        result = functions.get_digit(0, 0)
        self.assertEqual(expected, result)

    def test_getdigit_1_ones_returns1(self):
        expected = 1
        result = functions.get_digit(1, 0)
        self.assertEqual(expected, result)

    def test_getdigit_12_ones_returns2(self):
        expected = 2
        result = functions.get_digit(12, 0)
        self.assertEqual(expected, result)

    def test_getdigit_123_ones_returns3(self):
        expected = 3
        result = functions.get_digit(123, 0)
        self.assertEqual(expected, result)

    def test_getdigit_1234_ones_returns4(self):
        expected = 4
        result = functions.get_digit(1234, 0)
        self.assertEqual(expected, result)

    # Tests get_tens_digit(n):
    #  def test_getdigit_0_tens_raisesException(self):
        #  Raise exception
        #  self.assertRaises(ValueError, functions.get_digit, 0, 1)

    #  def test_getdigit_1_tens_raisesException(self):
        #  Raise exception
        #  self.assertRaises(ValueError, functions.get_digit, 1, 1)

    def test_getdigit_12_tens_returns1(self):
        expected = 1
        result = functions.get_digit(12, 1)
        self.assertEqual(expected, result)

    def test_getdigit_123_tens_returns2(self):
        expected = 2
        result = functions.get_digit(123, 1)
        self.assertEqual(expected, result)

    def test_getdigit_1234_tens_returns3(self):
        expected = 3
        result = functions.get_digit(1234, 1)
        self.assertEqual(expected, result)

    # Tests get_hundreds_digit(n):
    #  def test_getdigit_0_raiseException(self):
        #  self.assertRaises(ValueError, functions.get_digit, 0, 2)

    #  def test_getdigit_1_raiseException(self):
        #  self.assertRaises(ValueError, functions.get_digit, 1, 2)

    #  def test_getdigit_12_raiseException(self):
        #  self.assertRaises(ValueError, functions.get_digit, 12, 2)

    def test_getdigit_123_hundreds_returns1(self):
        expected = 1
        result = functions.get_digit(123, 2)
        self.assertEqual(expected, result)

    def test_getdigit_1234_hundreds_returns2(self):
        expected = 2
        result = functions.get_digit(1234, 2)
        self.assertEqual(expected, result)


################################################################################
    # Tests for get_text(n):
    def test_gettext_0_raisesException(self):
        self.assertRaises(ValueError, functions.get_text, 0)

    def test_gettext_1_returnsOne(self):
        expected = 'one'
        result = functions.get_text(1)
        self.assertEqual(expected, result)

    def test_gettext_2_returnsTwo(self):
        expected = 'two'
        result = functions.get_text(2)
        self.assertEqual(expected, result)

    def test_gettext_3_returnsThree(self):
        expected = 'three'
        result = functions.get_text(3)
        self.assertEqual(expected, result)

    def test_gettext_4_returnsFour(self):
        expected = 'four'
        result = functions.get_text(4)
        self.assertEqual(expected, result)

    def test_gettext_5_returnsFive(self):
        expected = 'five'
        result = functions.get_text(5)
        self.assertEqual(expected, result)

    def test_gettext_6_returnsSix(self):
        expected = 'six'
        result = functions.get_text(6)
        self.assertEqual(expected, result)

    def test_gettext_7_returnsSeven(self):
        expected = 'seven'
        result = functions.get_text(7)
        self.assertEqual(expected, result)

    def test_gettext_8_returnsEight(self):
        expected = 'eight'
        result = functions.get_text(8)
        self.assertEqual(expected, result)

    def test_gettext_9_returnsNine(self):
        expected = 'nine'
        result = functions.get_text(9)
        self.assertEqual(expected, result)

    def test_gettext_10_returnsTen(self):
        expected = 'ten'
        result = functions.get_text(10)
        self.assertEqual(expected, result)

    def test_gettext_11_returnsEleven(self):
        expected = 'eleven'
        result = functions.get_text(11)
        self.assertEqual(expected, result)

    def test_gettext_12_returnsTwelve(self):
        expected = 'twelve'
        result = functions.get_text(12)
        self.assertEqual(expected, result)

    def test_gettext_13_returnsThirteen(self):
        expected = 'thirteen'
        result = functions.get_text(13)
        self.assertEqual(expected, result)

    def test_gettext_14_returnsFourteen(self):
        expected = 'fourteen'
        result = functions.get_text(14)
        self.assertEqual(expected, result)

    def test_gettext_15_returnsFifteen(self):
        expected = 'fifteen'
        result = functions.get_text(15)
        self.assertEqual(expected, result)

    def test_gettext_16_returnsSixteen(self):
        expected = 'sixteen'
        result = functions.get_text(16)
        self.assertEqual(expected, result)

    def test_gettext_17_returnsSeventeen(self):
        expected = 'seventeen'
        result = functions.get_text(17)
        self.assertEqual(expected, result)

    def test_gettext_18_returnsEighteen(self):
        expected = 'eighteen'
        result = functions.get_text(18)
        self.assertEqual(expected, result)

    def test_gettext_19_returnsNineteen(self):
        expected = 'nineteen'
        result = functions.get_text(19)
        self.assertEqual(expected, result)

    def test_gettext_20_returnsTwenty(self):
        expected = 'twenty'
        result = functions.get_text(20)
        self.assertEqual(expected, result)

    def test_gettext_21_returnsTwentyOne(self):
        expected = 'twenty-one'
        result = functions.get_text(21)
        self.assertEqual(expected, result)

    def test_gettext_100_returnsOneHundred(self):
        expected = 'one hundred'
        result = functions.get_text(100)
        self.assertEqual(expected, result)

    def test_gettext_101_returnsOneHundredAndOne(self):
        expected = 'one hundred and one'
        result = functions.get_text(101)
        self.assertEqual(expected, result)

    def test_gettext_121_returnsOneHundredAndTwentyOne(self):
        expected = 'one hundred and twenty-one'
        result = functions.get_text(121)
        self.assertEqual(expected, result)

    # Tests for num_to_alpha(n):
    # 0 = 'zero'
    def test_numtoalpha_0_returnsZero(self):
        expected = 'zero'
        result = functions.num_to_alpha(0)
        self.assertEqual(expected, result)

    # 1000 = 'one thousand'
    def test_numtoalpha_1000_returnsOneThousand(self):
        expected = 'one thousand'
        result = functions.num_to_alpha(1000)
        self.assertEqual(expected, result)

    # 1001 = 'one thousand and one'
    def test_numtoalpha_1001_returnsOneThousandAndOne(self):
        expected = 'one thousand one'
        result = functions.num_to_alpha(1001)
        self.assertEqual(expected, result)

    # Tests for letter_qty(s):
    # 'abc' returns 3
    # 'abc1' returns 3
    # '123' returns 3
    # 123(the integer) returns 3

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


# Tests for read_matrix(filename):
    # Reading just 0 in a file, returns 1x1 matrix with 0
    def test_readmatrix_1x1file_1x1matrix(self):
        expected = [[0]]
        result = functions.read_matrix('data/test_matrix1.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_zerofilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = functions.read_matrix('data/test_matrix2.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_nonfilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = functions.read_matrix('data/test_matrix3.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_3x3file_zerofilled_3x3matrix(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = functions.read_matrix('data/test_matrix4.txt')
        self.assertEqual(expected, result)

    # Tests for print_matrix(matrix):
    def test_printmatrix_1x1(self):
        expected = '00\n'
        m = functions.read_matrix('data/test_matrix1.txt')
        result = functions.print_matrix(m)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_zerofilled(self):
        expected = '01 02\n03 04\n'
        m = functions.read_matrix('data/test_matrix2.txt')
        result = functions.print_matrix(m)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_nonfilled(self):
        expected = '01 02\n03 04\n'
        m = functions.read_matrix('data/test_matrix3.txt')
        result = functions.print_matrix(m)
        self.assertEqual(expected, result)

    # Tests for extract_line(matrix, point, xyincrement) are implicit since get_rows,
    # get_columns, get_right_diagonals, get_right_diagonals use extract_line.

    # Tests get_rows(matrix):
    def test_getrows_3x3_returns3lists(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.get_rows(m)
        self.assertEqual(expected, result)

    # Tests get_columns(matrix):
    def test_getcolumns_3x3_returns3lists(self):
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.get_columns(m)
        self.assertEqual(expected, result)

    # Tests get_right_diagonals(matrix):
    def test_get_right_diagonals_3x3_returns5lists(self):
        expected = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.get_right_diagonals(m)
        self.assertEqual(expected, result)

    # Tests get_left_diagonals(matrix):
    def test_get_left_diagonals_3x3_returns5lists(self):
        expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.get_left_diagonals(m)
        self.assertEqual(expected, result)

    # Tests for scan_matrix_lines(matrix):
    def test_scanmatrixlines_3x3_returns16lists(self):
        """ Make sure we get all the right lines from the matrix.
            In this order: rows, columns, right diagonals, left diagonals.
        """
        expected = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [7], [4, 8], [1, 5, 9], [2, 6], [3],
            [1], [2, 4], [3, 5, 7], [6, 8], [9]
        ]
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.scan_matrix_lines(m)
        self.assertEqual(expected, result)

    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_3x3_returns504(self):
        # 7 * 8 * 9 = 504
        expected = 504
        m = functions.read_matrix('data/test_matrix4.txt')
        result = functions.find_greatest_product(m, 3)
        self.assertEqual(expected, result)

    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_2x2_returns12(self):
        expected = 12
        m = functions.read_matrix('data/test_matrix2.txt')
        result = functions.find_greatest_product(m, 2)
        self.assertEqual(expected, result)
