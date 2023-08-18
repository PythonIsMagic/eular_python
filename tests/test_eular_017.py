import pytest

from ..src import eular_017


# Tests for get_digit(n, i)
# Tests for letter_qty(s):
# 'abc' returns 3
# 'abc1' returns 3
# '123' returns 3
# 123(the integer) returns 3
def test_getdigit_n0_ones_returns0():
    assert eular_017.get_digit(0, 0) == 0


def test_getdigit_1_ones_returns1():
    assert eular_017.get_digit(1, 0) == 1


def test_getdigit_12_ones_returns2():
    assert eular_017.get_digit(12, 0) == 2


def test_getdigit_123_ones_returns3():
    assert eular_017.get_digit(123, 0) == 3


def test_getdigit_1234_ones_returns4():
    assert eular_017.get_digit(1234, 0) == 4


def test_getdigit_12_tens_returns1():
    assert eular_017.get_digit(12, 1) == 1


def test_getdigit_123_tens_returns2():
    assert eular_017.get_digit(123, 1) == 2


def test_getdigit_1234_tens_returns3():
    assert eular_017.get_digit(1234, 1) == 3


def test_getdigit_123_hundreds_returns1():
    assert eular_017.get_digit(123, 2) == 1


def test_getdigit_1234_hundreds_returns2():
    assert eular_017.get_digit(1234, 2) == 2


def test_gettext_0_raisesException():
    with pytest.raises(ValueError):
        eular_017.get_text(0)


def test_gettext_1_returnsOne():
    assert eular_017.get_text(1) == 'one'


def test_gettext_2_returnsTwo():
    assert eular_017.get_text(2) == 'two'


def test_gettext_3_returnsThree():
    assert eular_017.get_text(3) == 'three'


def test_gettext_4_returnsFour():
    assert eular_017.get_text(4) == 'four'


def test_gettext_5_returnsFive():
    assert eular_017.get_text(5) == 'five'


def test_gettext_6_returnsSix():
    assert eular_017.get_text(6) == 'six'


def test_gettext_7_returnsSeven():
    assert eular_017.get_text(7) == 'seven'


def test_gettext_8_returnsEight():
    assert eular_017.get_text(8) == 'eight'


def test_gettext_9_returnsNine():
    assert eular_017.get_text(9) == 'nine'


def test_gettext_10_returnsTen():
    assert eular_017.get_text(10) == 'ten'


def test_gettext_11_returnsEleven():
    assert eular_017.get_text(11) == 'eleven'


def test_gettext_12_returnsTwelve():
    assert eular_017.get_text(12) == 'twelve'


def test_gettext_13_returnsThirteen():
    assert eular_017.get_text(13) == 'thirteen'


def test_gettext_14_returnsFourteen():
    assert eular_017.get_text(14) == 'fourteen'


def test_gettext_15_returnsFifteen():
    assert eular_017.get_text(15) == 'fifteen'


def test_gettext_16_returnsSixteen():
    assert eular_017.get_text(16) == 'sixteen'


def test_gettext_17_returnsSeventeen():
    assert eular_017.get_text(17) == 'seventeen'


def test_gettext_18_returnsEighteen():
    assert eular_017.get_text(18) == 'eighteen'


def test_gettext_19_returnsNineteen():
    assert eular_017.get_text(19) == 'nineteen'


def test_gettext_20_returnsTwenty():
    assert eular_017.get_text(20) == 'twenty'


def test_gettext_21_returnsTwentyOne():
    assert eular_017.get_text(21) == 'twenty-one'


def test_gettext_100_returnsOneHundred():
    assert eular_017.get_text(100) == 'one hundred'


def test_gettext_101_returnsOneHundredAndOne():
    assert eular_017.get_text(101) == 'one hundred and one'


def test_gettext_121_returnsOneHundredAndTwentyOne():
    assert eular_017.get_text(121) == 'one hundred and twenty-one'

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
def test_numtoalpha_0_returnsZero():
    assert eular_017.num_to_alpha(0) == 'zero'


def test_numtoalpha_1000_returnsOneThousand():
    assert eular_017.num_to_alpha(1000) == 'one thousand'


def test_numtoalpha_1001_returnsOneThousandAndOne():
    assert eular_017.num_to_alpha(1001) == 'one thousand one'
