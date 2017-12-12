import pytest
import problem19


# January has 31 days
def test_getdays_1_returns31():
    assert problem19.get_days(1) == 31


# February. No year passed raises an exception - we need that.
def test_getdays_noyear_raisesException():
    with pytest.raises(ValueError):
        problem19.get_days(2)


# February has 29 days for a leap-year.
def test_getdays_2_year2004_returns29():
    assert problem19.get_days(2, 2004) == 29


# February has 28 days for a non-leap-year.
def test_getdays_2_year2001_returns28():
    assert problem19.get_days(2, 2001) == 28


# March has 31 days
def test_getdays_3_returns31():
    assert problem19.get_days(3) == 31


# April has 30 days
def test_getdays_4_returns30():
    assert problem19.get_days(4) == 30


# May has 31 days
def test_getdays_5_returns31():
    assert problem19.get_days(5) == 31


# June has 30 days
def test_getdays_6_returns30():
    assert problem19.get_days(6) == 30


# July has 31 days
def test_getdays_7_returns31():
    assert problem19.get_days(7) == 31


# August has 31 days
def test_getdays_8_returns31():
    assert problem19.get_days(8) == 31


# September has 30 days
def test_getdays_9_returns30():
    assert problem19.get_days(9) == 30


# October has 31 days
def test_getdays_10_returns31():
    assert problem19.get_days(10) == 31


# November has 30 days
def test_getdays_11_returns30():
    assert problem19.get_days(11) == 30


# December has 31 days
def test_getdays_12_returns31():
    assert problem19.get_days(12) == 31


# Tests for is_leap_year(year)
# February has 29 days for a leap-year. Year = 0 = leap year.
def test_isleapyear_0_returnsTrue():
    assert problem19.is_leap_year(0)


# February has 29 days for a century leap-year. Year divisible by 400.
def test_isleapyear_2000_returnsTrue():
    assert problem19.is_leap_year(2000)


# February has 29 days for a leap-year. Divisible by 4.
def test_isleapyear_2004_returnsTrue():
    assert problem19.is_leap_year(2004)


# February has 28 days for a non-leap-year.
def test_isleapyear_2001_returnsFalse():
    assert problem19.is_leap_year(2001) is False


# February has 28 days for a non-leap-year. Year is not divisible by 400.
def test_isleapyear_2100_returnsFalse():
    assert problem19.is_leap_year(2100) is False
