import pytest

from ..src import eular_017


# Tests for get_digit(n, i)
# Tests for letter_qty(s):
# 'abc' returns 3
# 'abc1' returns 3
# '123' returns 3
# 123(the integer) returns 3
def test_getdigit_n0_ones_returns0():
    result = eular_017.get_digit(0, 0)
    assert result == 0


def test_getdigit_1_ones_returns1():
    result = eular_017.get_digit(1, 0)
    assert result == 1


def test_getdigit_12_ones_returns2():
    result = eular_017.get_digit(12, 0)
    assert result == 2


def test_getdigit_123_ones_returns3():
    result = eular_017.get_digit(123, 0)
    assert result == 3


def test_getdigit_1234_ones_returns4():
    result = eular_017.get_digit(1234, 0)
    assert result == 4


def test_getdigit_12_tens_returns1():
    result = eular_017.get_digit(12, 1)
    assert result == 1


def test_getdigit_123_tens_returns2():
    result = eular_017.get_digit(123, 1)
    assert result == 2


def test_getdigit_1234_tens_returns3():
    result = eular_017.get_digit(1234, 1)
    assert result == 3


def test_getdigit_123_hundreds_returns1():
    result = eular_017.get_digit(123, 2)
    assert result == 1


def test_getdigit_1234_hundreds_returns2():
    result = eular_017.get_digit(1234, 2)
    assert result == 2


def test_gettext_0_raisesException():
    with pytest.raises(ValueError):
        eular_017.get_text(0)


def test_gettext_1():
    assert eular_017.get_text(1) == 'one'


def test_gettext_2():
    assert eular_017.get_text(2) == 'two'


def test_gettext_3():
    assert eular_017.get_text(3) == 'three'


def test_gettext_4():
    assert eular_017.get_text(4) == 'four'


def test_gettext_5():
    assert eular_017.get_text(5) == 'five'


def test_gettext_6_():
    assert eular_017.get_text(6) == 'six'


def test_gettext_7():
    assert eular_017.get_text(7) == 'seven'


def test_gettext_8():
    assert eular_017.get_text(8) == 'eight'


def test_gettext_9():
    assert eular_017.get_text(9) == 'nine'


def test_gettext_10():
    assert eular_017.get_text(10) == 'ten'


def test_gettext_11():
    assert eular_017.get_text(11) == 'eleven'


def test_gettext_12():
    assert eular_017.get_text(12) == 'twelve'


def test_gettext_13():
    assert eular_017.get_text(13) == 'thirteen'


def test_gettext_14():
    assert eular_017.get_text(14) == 'fourteen'


def test_gettext_15():
    assert eular_017.get_text(15) == 'fifteen'


def test_gettext_16():
    assert eular_017.get_text(16) == 'sixteen'


def test_gettext_17():
    assert eular_017.get_text(17) == 'seventeen'


def test_gettext_18():
    assert eular_017.get_text(18) == 'eighteen'


def test_gettext_19():
    assert eular_017.get_text(19) == 'nineteen'


def test_gettext_20():
    assert eular_017.get_text(20) == 'twenty'


def test_gettext_21():
    assert eular_017.get_text(21) == 'twenty-one'


def test_gettext_100():
    assert eular_017.get_text(100) == 'one hundred'


def test_gettext_101():
    assert eular_017.get_text(101) == 'one hundred and one'


def test_gettext_121():
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
    result = eular_017.num_to_alpha(0)
    assert result == 'zero'


def test_numtoalpha_1000_returnsOneThousand():
    result = eular_017.num_to_alpha(1000)
    assert result == 'one thousand'


def test_numtoalpha_1001_returnsOneThousandAndOne():
    result = eular_017.num_to_alpha(1001)
    assert result == 'one thousand one'
