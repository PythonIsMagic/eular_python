"""
  " Tests for the prime (and division) related functions
  """
from ..src import toolkit
import pytest


@pytest.fixture(params=[toolkit.isprime_ver1, toolkit.isprime_ver2])
def isprime(request):
    return request.param


def test_isprime_0_returnFalse(isprime):
    assert isprime(0) is False


def test_isprime_1_returnFalse(isprime):
    assert isprime(1) is False


def test_isprime_2_returnTrue(isprime):
    assert isprime(2)


def test_isprime_3_returnTrue(isprime):
    assert isprime(3)


def test_fromprime():
    """ Compares divisors and divisors_bruteforce. """
    TRIES = 100
    failures = 0

    for i in range(1, TRIES):
        bf = toolkit.divisors_bruteforce(i)
        fp = toolkit.divisors(i)

        if bf != fp:
            print('Test failed on {}!'.format(i))
            print('bruteforce: {}'.format(sorted(bf)))
            print('fromprime:  {}'.format(sorted(fp)))
            failures += 1
        else:
            print('{} - Check.'.format(i))

    if failures > 0:
        print('{} out of {} tests failed.'.format(failures, TRIES - 1))
    else:
        print('All tests passed! (up to {})'.format(TRIES))


def test_maxprimefactor_0_returnNone():
    assert toolkit.max_prime_factor(0) is None


def test_maxprimefactor_1_returnNone():
    assert toolkit.max_prime_factor(1) is None


def test_maxprimefactor_2_return2():
    assert toolkit.max_prime_factor(2) == 2


def test_maxprimefactor_3_return3():
    assert toolkit.max_prime_factor(3) == 3


def test_maxprimefactor_4_return2():
    assert toolkit.max_prime_factor(4) == 2


def test_maxprimefactor_10_return5():
    assert toolkit.max_prime_factor(10) == 5


def test_maxprimefactor_100_return5():
    assert toolkit.max_prime_factor(100) == 5


def test_maxprimefactor_1000_return5():
    assert toolkit.max_prime_factor(1000) == 5


def test_primes_1next_return2():
    g = toolkit.primes()
    assert next(g) == 2


def test_primes_2next_return3():
    g = toolkit.primes()
    next(g)
    assert next(g) == 3


def test_primes_3next_return5():
    g = toolkit.primes()
    next(g)
    next(g)
    assert next(g) == 5


# of -1 = None
def test_getprimefactors_neg1_returnsNone():
    assert toolkit.get_prime_factors(-1) is None


# of 0 = None
def test_getprimefactors_0_returnsNone():
    assert toolkit.get_prime_factors(0) is None


# of 1 = None
def test_getprimefactors_1_returnsNone():
    assert toolkit.get_prime_factors(1) is None


# of 2 = 2
def test_getprimefactors_2_returns2():
    assert toolkit.get_prime_factors(2) == {2}


# of 3 = 3
def test_getprimefactors_3_returns3():
    assert toolkit.get_prime_factors(3) == {3}


# of 4 = 2
def test_getprimefactors_4_returns2():
    assert toolkit.get_prime_factors(4) == {2}


# of 5 = 5
def test_getprimefactors_5_returns5():
    assert toolkit.get_prime_factors(5) == {5}


# of 6 = 2, 3
def test_getprimefactors_6_returns2_3():
    assert toolkit.get_prime_factors(6) == {2, 3}


# of 7 = 7
def test_getprimefactors_7_returns7():
    assert toolkit.get_prime_factors(7) == {7}


# of 10 = 2, 5
def test_getprimefactors_10_returns2_5():
    assert toolkit.get_prime_factors(10) == {2, 5}


# of 12 = 2, 3
def test_getprimefactors_12_returns2_3():
    assert toolkit.get_prime_factors(12) == {2, 3}


# of 24 = 2, 3
def test_getprimefactors_24_returns2_3():
    assert toolkit.get_prime_factors(24) == {2, 3}


def test_multiply_2factors_returns2():
    n = [1, 2, 3, 4, 5]
    assert toolkit.multiply(n, 0, 2) == 2


def test_multiply_3factors_returns6():
    n = [1, 2, 3, 4, 5]
    assert toolkit.multiply(n, 0, 3) == 6


def test_multiply_3factors_index1_returns24():
    n = [1, 2, 3, 4, 5]
    assert toolkit.multiply(n, 1, 3) == 24


def test_multiply_indexoutofbounds_raiseException():
    n = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        toolkit.multiply(n, 10, 3)


def test_multiply_3factors_size3_returns24():
    n = [2, 3, 4]
    assert toolkit.multiply(n, 0, 3) == 24


def test_multiply_13factors_size14_index0_returns157689344584365834240():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 157689344584365834240
    assert toolkit.multiply(n, 0, 13) == expected


def test_multiply_13factors_size14_index1_returns211895056785241589760():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 211895056785241589760
    assert toolkit.multiply(n, 1, 13) == expected


def test_fibonaccis_call1_return1():
    f = toolkit.fibonaccis()
    assert next(f) == 1


def test_fibonaccis_call2_return1():
    f = toolkit.fibonaccis()
    next(f)
    assert next(f) == 1


def test_fibonaccis_call3_return2():
    f = toolkit.fibonaccis()
    next(f)
    next(f)
    assert next(f) == 2


def test_fibonaccis_call4_return3():
    f = toolkit.fibonaccis()
    next(f)
    next(f)
    next(f)
    assert next(f) == 3


def test_ispalindrome_emptyString_returnFalse():
    assert toolkit.is_palindrome('') is False


def test_ispalindrome_1_returnTrue():
    assert toolkit.is_palindrome(1)


def test_ispalindrome_10_returnFalse():
    assert toolkit.is_palindrome(10) is False


def test_ispalindrome_11_returnTrue():
    assert toolkit.is_palindrome(11)


def test_ispalindrome_101_returnTrue():
    assert toolkit.is_palindrome(101)


def test_ispalindrome_110_returnFalse():
    assert toolkit.is_palindrome(110) is False


def test_largestpalindrome_2digit_returns9009():
    assert toolkit.largest_palindrome(10, 100) == 9009


def test_divbyallupto_1_raiseException():
    with pytest.raises(ValueError):
        toolkit.div_by_all_upto(1)


def test_divbyallupto_2_raisesException():
    with pytest.raises(ValueError):
        toolkit.div_by_all_upto(1)


def test_divbyallupto_15_raisesException():
    with pytest.raises(ValueError):
        toolkit.div_by_all_upto(15)


def test_divbyallupto_10_returns2520():
    assert toolkit.div_by_all_upto(10) == 2520


def test_sumofsquares_upto0_returns0():
    assert toolkit.sum_of_squares(0) == 0


def test_sumofsquares_upto1_returns1():
    assert toolkit.sum_of_squares(1) == 1


def test_sumofsquares_upto2_returns5():
    assert toolkit.sum_of_squares(2) == 5


def test_squareofsum_upto1_returns0():
    assert toolkit.square_of_sum(0) == 0


def test_squareofsum_upto1_returns1():
    assert toolkit.square_of_sum(1) == 1


def test_squareofsum_upto2_returns9():
    assert toolkit.square_of_sum(2) == 9


def test_calculateproduct_1_returns1():
    test_list = [1]
    assert toolkit.calculate_product(test_list) == 1


def test_calculateproduct_1x2_returns2():
    test_list = [1, 2]
    assert toolkit.calculate_product(test_list) == 2


def test_calculateproduct_1x2x3_returns6():
    test_list = [1, 2, 3]
    assert toolkit.calculate_product(test_list) == 6


def test_calculateproduct_0x2x3_returns0():
    test_list = [0, 2, 3]
    toolkit.calculate_product(test_list) == 0


def test_findproductinlist_1to9_3factors_returns504():
    factors = 3
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    toolkit.find_product_in_list(test_list, factors) == 504


def test_findproductinlist_1to9_2factors_returns72():
    factors = 2
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert toolkit.find_product_in_list(test_list, factors) == 72


def test_readfiletolist_just1_listIs1():
    assert toolkit.read_file_to_list('data/test_digits1.txt') == [1]


def test_readfiletolist_3x3digits_listmatches():
    expected = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert toolkit.read_file_to_list('data/test_digits2.txt') == expected


def test_readmatrix_1x1file_1x1matrix():
    expected = [[0]]
    assert toolkit.read_matrix('data/test_matrix1.txt') == expected


def test_readmatrix_2x2file_zerofilled_2x2matrix():
    expected = [[1, 2], [3, 4]]
    assert toolkit.read_matrix('data/test_matrix2.txt') == expected


def test_readmatrix_2x2file_nonfilled_2x2matrix():
    expected = [[1, 2], [3, 4]]
    assert toolkit.read_matrix('data/test_matrix3.txt') == expected


def test_readmatrix_3x3file_zerofilled_3x3matrix():
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert toolkit.read_matrix('data/test_matrix4.txt') == expected


def test_printmatrix_1x1():
    expected = '00\n'
    m = toolkit.read_matrix('data/test_matrix1.txt')
    assert toolkit.print_matrix(m) == expected


def test_printmatrix_2x2file_zerofilled():
    expected = '01 02\n03 04\n'
    m = toolkit.read_matrix('data/test_matrix2.txt')
    assert toolkit.print_matrix(m) == expected


def test_printmatrix_2x2file_nonfilled():
    expected = '01 02\n03 04\n'
    m = toolkit.read_matrix('data/test_matrix3.txt')
    assert toolkit.print_matrix(m) == expected


def test_getrows_3x3_returns3lists():
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.get_rows(m) == expected


# Tests for extract_line(matrix, point, xyincrement) are implicit since get_rows,
# get_columns, get_right_diagonals, get_right_diagonals use extract_line.

def test_getcolumns_3x3_returns3lists():
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.get_columns(m) == expected


def test_get_right_diagonals_3x3_returns5lists():
    expected = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.get_right_diagonals(m) == expected


def test_get_left_diagonals_3x3_returns5lists():
    expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.get_left_diagonals(m) == expected


def test_scanmatrixlines_3x3_returns16lists():
    """ Make sure we get all the right lines from the matrix.
        In this order: rows, columns, right diagonals, left diagonals.
    """
    expected = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [7], [4, 8], [1, 5, 9], [2, 6], [3],
        [1], [2, 4], [3, 5, 7], [6, 8], [9]
    ]
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.scan_matrix_lines(m) == expected


def test_findgreatestproduct_3x3_returns504():
    # 7 * 8 * 9 = 504
    m = toolkit.read_matrix('data/test_matrix4.txt')
    assert toolkit.find_greatest_product(m, 3) == 504


def test_findgreatestproduct_2x2_returns12():
    m = toolkit.read_matrix('data/test_matrix2.txt')
    assert toolkit.find_greatest_product(m, 2) == 12


def test_trianglenum_call1_returns1():
    gen = toolkit.triangles()
    assert next(gen) == 1


def test_trianglenum_call2_returns3():
    gen = toolkit.triangles()
    next(gen)
    assert next(gen) == 3


def test_trianglenum_call3_returns6():
    gen = toolkit.triangles()
    next(gen)
    next(gen)
    assert next(gen) == 6


def test_collatzseq_1_returns1():
    expected = [1]
    assert toolkit.collatz_seq(1) == expected


def test_collatzseq_2_returns2_1():
    expected = [2, 1]
    assert toolkit.collatz_seq(2) == expected


def test_collatzseq_3_returns3_10_5_16_8_4_2_1():
    expected = [3, 10, 5, 16, 8, 4, 2, 1]
    assert toolkit.collatz_seq(3) == expected


def test_collatzseq_4_returns4_2_1():
    expected = [4, 2, 1]
    assert toolkit.collatz_seq(4) == expected


def test_collatzseq_5_returns5_16_8_4_2_1():
    expected = [5, 16, 8, 4, 2, 1]
    assert toolkit.collatz_seq(5) == expected


def test_nextcollatz_neg1_raiseException():
    with pytest.raises(ValueError):
        toolkit.next_collatz(-1)


def test_nextcollatz_0_raiseException():
    with pytest.raises(ValueError):
        toolkit.next_collatz(0)


def test_nextcollatz_1_raiseException():
    with pytest.raises(ValueError):
        toolkit.next_collatz(1)


def test_nextcollatz_2_returns1():
    expected = 1
    assert toolkit.next_collatz(2) == expected


def test_nextcollatz_3_returns10():
    expected = 10
    assert toolkit.next_collatz(3) == expected


def test_nextcollatz_4_returns2():
    expected = 2
    assert toolkit.next_collatz(4) == expected


def test_nextcollatz_5_returns16():
    expected = 16
    assert toolkit.next_collatz(5) == expected


# Tests for get_digit(n, i)
# Tests for letter_qty(s):
# 'abc' returns 3
# 'abc1' returns 3
# '123' returns 3
# 123(the integer) returns 3

def test_getdigit_n0_ones_returns0():
    assert toolkit.get_digit(0, 0) == 0


def test_getdigit_1_ones_returns1():
    assert toolkit.get_digit(1, 0) == 1


def test_getdigit_12_ones_returns2():
    assert toolkit.get_digit(12, 0) == 2


def test_getdigit_123_ones_returns3():
    assert toolkit.get_digit(123, 0) == 3


def test_getdigit_1234_ones_returns4():
    assert toolkit.get_digit(1234, 0) == 4


def test_getdigit_12_tens_returns1():
    assert toolkit.get_digit(12, 1) == 1


def test_getdigit_123_tens_returns2():
    assert toolkit.get_digit(123, 1) == 2


def test_getdigit_1234_tens_returns3():
    assert toolkit.get_digit(1234, 1) == 3


def test_getdigit_123_hundreds_returns1():
    assert toolkit.get_digit(123, 2) == 1


def test_getdigit_1234_hundreds_returns2():
    assert toolkit.get_digit(1234, 2) == 2


# Tests get_tens_digit(n):
#  def test_getdigit_0_tens_raisesException():
#  Raise exception
#  .assertRaises(ValueError, problem17.get_digit, 0, 1)


#  def test_getdigit_1_tens_raisesException():
#  Raise exception
#  .assertRaises(ValueError, problem17.get_digit, 1, 1)


# Tests get_hundreds_digit(n):
#  def test_getdigit_0_raiseException():
#  .assertRaises(ValueError, problem17.get_digit, 0, 2)


#  def test_getdigit_1_raiseException():
#  .assertRaises(ValueError, problem17.get_digit, 1, 2)


#  def test_getdigit_12_raiseException():
#  .assertRaises(ValueError, problem17.get_digit, 12, 2)


def test_gettext_0_raisesException():
    with pytest.raises(ValueError):
        toolkit.get_text(0)


def test_gettext_1_returnsOne():
    assert toolkit.get_text(1) == 'one'


def test_gettext_2_returnsTwo():
    assert toolkit.get_text(2) == 'two'


def test_gettext_3_returnsThree():
    assert toolkit.get_text(3) == 'three'


def test_gettext_4_returnsFour():
    assert toolkit.get_text(4) == 'four'


def test_gettext_5_returnsFive():
    assert toolkit.get_text(5) == 'five'


def test_gettext_6_returnsSix():
    assert toolkit.get_text(6) == 'six'


def test_gettext_7_returnsSeven():
    assert toolkit.get_text(7) == 'seven'


def test_gettext_8_returnsEight():
    assert toolkit.get_text(8) == 'eight'


def test_gettext_9_returnsNine():
    assert toolkit.get_text(9) == 'nine'


def test_gettext_10_returnsTen():
    assert toolkit.get_text(10) == 'ten'


def test_gettext_11_returnsEleven():
    assert toolkit.get_text(11) == 'eleven'


def test_gettext_12_returnsTwelve():
    assert toolkit.get_text(12) == 'twelve'


def test_gettext_13_returnsThirteen():
    assert toolkit.get_text(13) == 'thirteen'


def test_gettext_14_returnsFourteen():
    assert toolkit.get_text(14) == 'fourteen'


def test_gettext_15_returnsFifteen():
    assert toolkit.get_text(15) == 'fifteen'


def test_gettext_16_returnsSixteen():
    assert toolkit.get_text(16) == 'sixteen'


def test_gettext_17_returnsSeventeen():
    assert toolkit.get_text(17) == 'seventeen'


def test_gettext_18_returnsEighteen():
    assert toolkit.get_text(18) == 'eighteen'


def test_gettext_19_returnsNineteen():
    assert toolkit.get_text(19) == 'nineteen'


def test_gettext_20_returnsTwenty():
    assert toolkit.get_text(20) == 'twenty'


def test_gettext_21_returnsTwentyOne():
    assert toolkit.get_text(21) == 'twenty-one'


def test_gettext_100_returnsOneHundred():
    assert toolkit.get_text(100) == 'one hundred'


def test_gettext_101_returnsOneHundredAndOne():
    assert toolkit.get_text(101) == 'one hundred and one'


def test_gettext_121_returnsOneHundredAndTwentyOne():
    assert toolkit.get_text(121) == 'one hundred and twenty-one'


def test_numtoalpha_0_returnsZero():
    assert toolkit.num_to_alpha(0) == 'zero'


def test_numtoalpha_1000_returnsOneThousand():
    assert toolkit.num_to_alpha(1000) == 'one thousand'


def test_numtoalpha_1001_returnsOneThousandAndOne():
    assert toolkit.num_to_alpha(1001) == 'one thousand one'


def test_getdays_1_returns31():
    """January has 31 days"""
    assert toolkit.get_days(1) == 31


def test_getdays_noyear_raisesException():
    """February. No year passed raises an exception - we need that."""
    with pytest.raises(ValueError):
        toolkit.get_days(2)


def test_getdays_2_year2004_returns29():
    """February has 29 days for a leap-year."""
    assert toolkit.get_days(2, 2004) == 29


def test_getdays_2_year2001_returns28():
    """February has 28 days for a non-leap-year."""
    assert toolkit.get_days(2, 2001) == 28


def test_getdays_3_returns31():
    """March has 31 days"""
    assert toolkit.get_days(3) == 31


def test_getdays_4_returns30():
    """April has 30 days"""
    assert toolkit.get_days(4) == 30


def test_getdays_5_returns31():
    """May has 31 days"""
    assert toolkit.get_days(5) == 31


def test_getdays_6_returns30():
    """June has 30 days"""
    assert toolkit.get_days(6) == 30


def test_getdays_7_returns31():
    """July has 31 days"""
    assert toolkit.get_days(7) == 31


def test_getdays_8_returns31():
    """August has 31 days"""
    assert toolkit.get_days(8) == 31


def test_getdays_9_returns30():
    """September has 30 days"""
    assert toolkit.get_days(9) == 30


def test_getdays_10_returns31():
    """October has 31 days"""
    assert toolkit.get_days(10) == 31


def test_getdays_11_returns30():
    """November has 30 days"""
    assert toolkit.get_days(11) == 30


def test_getdays_12_returns31():
    """December has 31 days"""
    assert toolkit.get_days(12) == 31


def test_isleapyear_0_returnsTrue():
    """February has 29 days for a leap-year. Year = 0 = leap year."""
    assert toolkit.is_leap_year(0)


def test_isleapyear_2000_returnsTrue():
    """February has 29 days for a century leap-year. Year divisible by 400."""
    assert toolkit.is_leap_year(2000)


def test_isleapyear_2004_returnsTrue():
    """February has 29 days for a leap-year. Divisible by 4."""
    assert toolkit.is_leap_year(2004)


def test_isleapyear_2001_returnsFalse():
    """February has 28 days for a non-leap-year."""
    assert toolkit.is_leap_year(2001) is False


def test_isleapyear_2100_returnsFalse():
    """February has 28 days for a non-leap-year. Year is not divisible by 400."""
    assert toolkit.is_leap_year(2100) is False


def test_abundantsupto_12_returns12():
    assert toolkit.abundants_upto(12) == [12]
