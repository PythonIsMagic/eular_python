import unittest
import countingdays


class Testcountingdays(unittest.TestCase):
    ###########################
    # Tests for get_days(month)

    # January has 31 days
    def test_getdays_1_returns31(self):
        expected = 31
        result = countingdays.get_days(1)
        self.assertEqual(expected, result)

    # February. No year passed raises an exception - we need that.
    def test_getdays_noyear_raisesException(self):
        self.assertRaises(ValueError, countingdays.get_days, 2)

    # February has 29 days for a leap-year.
    def test_getdays_2_year2004_returns29(self):
        expected = 29
        result = countingdays.get_days(2, 2004)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year.
    def test_getdays_2_year2001_returns28(self):
        expected = 28
        result = countingdays.get_days(2, 2001)
        self.assertEqual(expected, result)

    # March has 31 days
    def test_getdays_3_returns31(self):
        expected = 31
        result = countingdays.get_days(3)
        self.assertEqual(expected, result)

    # April has 30 days
    def test_getdays_4_returns30(self):
        expected = 30
        result = countingdays.get_days(4)
        self.assertEqual(expected, result)

    # May has 31 days
    def test_getdays_5_returns31(self):
        expected = 31
        result = countingdays.get_days(5)
        self.assertEqual(expected, result)

    # June has 30 days
    def test_getdays_6_returns30(self):
        expected = 30
        result = countingdays.get_days(6)
        self.assertEqual(expected, result)

    # July has 31 days
    def test_getdays_7_returns31(self):
        expected = 31
        result = countingdays.get_days(7)
        self.assertEqual(expected, result)

    # August has 31 days
    def test_getdays_8_returns31(self):
        expected = 31
        result = countingdays.get_days(8)
        self.assertEqual(expected, result)

    # September has 30 days
    def test_getdays_9_returns30(self):
        expected = 30
        result = countingdays.get_days(9)
        self.assertEqual(expected, result)

    # October has 31 days
    def test_getdays_10_returns31(self):
        expected = 31
        result = countingdays.get_days(10)
        self.assertEqual(expected, result)

    # November has 30 days
    def test_getdays_11_returns30(self):
        expected = 30
        result = countingdays.get_days(11)
        self.assertEqual(expected, result)

    # December has 31 days
    def test_getdays_12_returns31(self):
        expected = 31
        result = countingdays.get_days(12)
        self.assertEqual(expected, result)

    # Tests for is_leap_year(year)
    # February has 29 days for a leap-year. Year = 0 = leap year.
    def test_isleapyear_0_returnsTrue(self):
        expected = True
        result = countingdays.is_leap_year(0)
        self.assertEqual(expected, result)

    # February has 29 days for a century leap-year. Year divisible by 400.
    def test_isleapyear_2000_returnsTrue(self):
        expected = True
        result = countingdays.is_leap_year(2000)
        self.assertEqual(expected, result)

    # February has 29 days for a leap-year. Divisible by 4.
    def test_isleapyear_2004_returnsTrue(self):
        expected = True
        result = countingdays.is_leap_year(2004)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year.
    def test_isleapyear_2001_returnsFalse(self):
        expected = False
        result = countingdays.is_leap_year(2001)
        self.assertEqual(expected, result)

    # February has 28 days for a non-leap-year. Year is not divisible by 400.
    def test_isleapyear_2100_returnsFalse(self):
        expected = False
        result = countingdays.is_leap_year(2100)
        self.assertEqual(expected, result)
