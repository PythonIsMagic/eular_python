import pytest

from ..src import eular_019


def test_getdays_1_returns31():
    """January has 31 days"""
    result = eular_019.get_days(1)
    assert result == 31


def test_getdays_noyear_raisesException():
    """February. No year passed raises an exception - we need that."""
    with pytest.raises(ValueError):
        eular_019.get_days(2)


def test_getdays_2_year2004_returns29():
    """February has 29 days for a leap-year."""
    result = eular_019.get_days(2, 2004)
    assert result == 29


def test_getdays_2_year2001_returns28():
    """February has 28 days for a non-leap-year."""
    result = eular_019.get_days(2, 2001)
    assert result == 28


def test_getdays_3_returns31():
    """March has 31 days"""
    result = eular_019.get_days(3)
    assert result == 31


def test_getdays_4_returns30():
    """April has 30 days"""
    result = eular_019.get_days(4)
    assert result == 30


def test_getdays_5_returns31():
    """May has 31 days"""
    result = eular_019.get_days(5)
    assert result == 31


def test_getdays_6_returns30():
    """June has 30 days"""
    result = eular_019.get_days(6)
    assert result == 30


def test_getdays_7_returns31():
    """July has 31 days"""
    result = eular_019.get_days(7)
    assert result == 31


def test_getdays_8_returns31():
    """August has 31 days"""
    result = eular_019.get_days(8)
    assert result == 31


def test_getdays_9_returns30():
    """September has 30 days"""
    result = eular_019.get_days(9)
    assert result == 30


def test_getdays_10_returns31():
    """October has 31 days"""
    result = eular_019.get_days(10)
    assert result == 31


def test_getdays_11_returns30():
    """November has 30 days"""
    result = eular_019.get_days(11)
    assert result == 30


def test_getdays_12_returns31():
    """December has 31 days"""
    result = eular_019.get_days(12)
    assert result == 31


def test_isleapyear_0_returnsTrue():
    """February has 29 days for a leap-year.
        Year = 0 = leap year."""
    result = eular_019.is_leap_year(0)
    assert result is True


def test_isleapyear_2000_returnsTrue():
    """February has 29 days for a century leap-year.
        Year divisible by 400."""
    result = eular_019.is_leap_year(2000)
    assert result is True


def test_isleapyear_2004_returnsTrue():
    """February has 29 days for a leap-year.
        Divisible by 4."""
    result = eular_019.is_leap_year(2004)
    assert result is True


def test_isleapyear_2001_returnsFalse():
    """February has 28 days for a non-leap-year."""
    result = eular_019.is_leap_year(2001)
    assert result is False


def test_isleapyear_2100_returnsFalse():
    """February has 28 days for a non-leap-year.
        Year is not divisible by 400."""
    result = eular_019.is_leap_year(2100)
    assert result is False
