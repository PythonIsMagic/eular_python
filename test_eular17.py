import unittest
import eular17


class TestEular17(unittest.TestCase):
    # Tests for num_to_list(n):
    def test_numtolist_0_returns0(self):
        expected = [0]
        result = eular17.num_to_list(0)
        self.assertEqual(expected, result)

    def test_numtolist_10_returns1_0(self):
        expected = [1, 0]
        result = eular17.num_to_list(10)
        self.assertEqual(expected, result)

    # Tests for get_digit(n, i)

    # Tests get_ones_digit(n):
    def test_getdigit_n0_ones_returns0(self):
        expected = 0
        result = eular17.get_digit(0, 0)
        self.assertEqual(expected, result)

    def test_getdigit_1_ones_returns1(self):
        expected = 1
        result = eular17.get_digit(1, 0)
        self.assertEqual(expected, result)

    def test_getdigit_12_ones_returns2(self):
        expected = 2
        result = eular17.get_digit(12, 0)
        self.assertEqual(expected, result)

    def test_getdigit_123_ones_returns3(self):
        expected = 3
        result = eular17.get_digit(123, 0)
        self.assertEqual(expected, result)

    def test_getdigit_1234_ones_returns4(self):
        expected = 4
        result = eular17.get_digit(1234, 0)
        self.assertEqual(expected, result)

    # Tests get_tens_digit(n):
    #  def test_getdigit_0_tens_raisesException(self):
        #  Raise exception
        #  self.assertRaises(ValueError, eular17.get_digit, 0, 1)

    #  def test_getdigit_1_tens_raisesException(self):
        #  Raise exception
        #  self.assertRaises(ValueError, eular17.get_digit, 1, 1)

    def test_getdigit_12_tens_returns1(self):
        expected = 1
        result = eular17.get_digit(12, 1)
        self.assertEqual(expected, result)

    def test_getdigit_123_tens_returns2(self):
        expected = 2
        result = eular17.get_digit(123, 1)
        self.assertEqual(expected, result)

    def test_getdigit_1234_tens_returns3(self):
        expected = 3
        result = eular17.get_digit(1234, 1)
        self.assertEqual(expected, result)

    # Tests get_hundreds_digit(n):
    #  def test_getdigit_0_raiseException(self):
        #  self.assertRaises(ValueError, eular17.get_digit, 0, 2)

    #  def test_getdigit_1_raiseException(self):
        #  self.assertRaises(ValueError, eular17.get_digit, 1, 2)

    #  def test_getdigit_12_raiseException(self):
        #  self.assertRaises(ValueError, eular17.get_digit, 12, 2)

    def test_getdigit_123_hundreds_returns1(self):
        expected = 1
        result = eular17.get_digit(123, 2)
        self.assertEqual(expected, result)

    def test_getdigit_1234_hundreds_returns2(self):
        expected = 2
        result = eular17.get_digit(1234, 2)
        self.assertEqual(expected, result)


################################################################################
    # Tests for get_text(n):
    def test_gettext_0_raisesException(self):
        self.assertRaises(ValueError, eular17.get_text, 0)

    def test_gettext_1_returnsOne(self):
        expected = 'one'
        result = eular17.get_text(1)
        self.assertEqual(expected, result)

    def test_gettext_2_returnsTwo(self):
        expected = 'two'
        result = eular17.get_text(2)
        self.assertEqual(expected, result)

    def test_gettext_3_returnsThree(self):
        expected = 'three'
        result = eular17.get_text(3)
        self.assertEqual(expected, result)

    def test_gettext_4_returnsFour(self):
        expected = 'four'
        result = eular17.get_text(4)
        self.assertEqual(expected, result)

    def test_gettext_5_returnsFive(self):
        expected = 'five'
        result = eular17.get_text(5)
        self.assertEqual(expected, result)

    def test_gettext_6_returnsSix(self):
        expected = 'six'
        result = eular17.get_text(6)
        self.assertEqual(expected, result)

    def test_gettext_7_returnsSeven(self):
        expected = 'seven'
        result = eular17.get_text(7)
        self.assertEqual(expected, result)

    def test_gettext_8_returnsEight(self):
        expected = 'eight'
        result = eular17.get_text(8)
        self.assertEqual(expected, result)

    def test_gettext_9_returnsNine(self):
        expected = 'nine'
        result = eular17.get_text(9)
        self.assertEqual(expected, result)

    def test_gettext_10_returnsTen(self):
        expected = 'ten'
        result = eular17.get_text(10)
        self.assertEqual(expected, result)

    def test_gettext_11_returnsEleven(self):
        expected = 'eleven'
        result = eular17.get_text(11)
        self.assertEqual(expected, result)

    def test_gettext_12_returnsTwelve(self):
        expected = 'twelve'
        result = eular17.get_text(12)
        self.assertEqual(expected, result)

    def test_gettext_13_returnsThirteen(self):
        expected = 'thirteen'
        result = eular17.get_text(13)
        self.assertEqual(expected, result)

    def test_gettext_14_returnsFourteen(self):
        expected = 'fourteen'
        result = eular17.get_text(14)
        self.assertEqual(expected, result)

    def test_gettext_15_returnsFifteen(self):
        expected = 'fifteen'
        result = eular17.get_text(15)
        self.assertEqual(expected, result)

    def test_gettext_16_returnsSixteen(self):
        expected = 'sixteen'
        result = eular17.get_text(16)
        self.assertEqual(expected, result)

    def test_gettext_17_returnsSeventeen(self):
        expected = 'seventeen'
        result = eular17.get_text(17)
        self.assertEqual(expected, result)

    def test_gettext_18_returnsEighteen(self):
        expected = 'eighteen'
        result = eular17.get_text(18)
        self.assertEqual(expected, result)

    def test_gettext_19_returnsNineteen(self):
        expected = 'nineteen'
        result = eular17.get_text(19)
        self.assertEqual(expected, result)

    def test_gettext_20_returnsTwenty(self):
        expected = 'twenty'
        result = eular17.get_text(20)
        self.assertEqual(expected, result)

    def test_gettext_21_returnsTwentyOne(self):
        expected = 'twenty-one'
        result = eular17.get_text(21)
        self.assertEqual(expected, result)

    def test_gettext_100_returnsOneHundred(self):
        expected = 'one hundred'
        result = eular17.get_text(100)
        self.assertEqual(expected, result)

    def test_gettext_101_returnsOneHundredAndOne(self):
        expected = 'one hundred and one'
        result = eular17.get_text(101)
        self.assertEqual(expected, result)

    def test_gettext_121_returnsOneHundredAndTwentyOne(self):
        expected = 'one hundred and twenty-one'
        result = eular17.get_text(121)
        self.assertEqual(expected, result)

    # Tests for num_to_alpha(n):
    # 0 = 'zero'
    def test_numtoalpha_0_returnsZero(self):
        expected = 'zero'
        result = eular17.num_to_alpha(0)
        self.assertEqual(expected, result)

    # 1000 = 'one thousand'
    def test_numtoalpha_1000_returnsOneThousand(self):
        expected = 'one thousand'
        result = eular17.num_to_alpha(1000)
        self.assertEqual(expected, result)

    # 1001 = 'one thousand and one'
    def test_numtoalpha_1001_returnsOneThousandAndOne(self):
        expected = 'one thousand one'
        result = eular17.num_to_alpha(1001)
        self.assertEqual(expected, result)

    # Tests for letter_qty(s):
    # 'abc' returns 3
    # 'abc1' returns 3
    # '123' returns 3
    # 123(the integer) returns 3
