import unittest
import eular20


class TestEular20(unittest.TestCase):
    # Tests for factorial(n):
    def test_factorial_neg1_RaiseException(self):
        self.assertRaises(ValueError, eular20.factorial, -1)

    def test_factorial_0_(self):
        self.assertRaises(ValueError, eular20.factorial, 0)

    def test_factorial_1_returns1(self):
        expected = 1
        result = eular20.factorial(1)
        self.assertEqual(expected, result)

    def test_factorial_2_returns2(self):
        expected = 2
        result = eular20.factorial(2)
        self.assertEqual(expected, result)

    def test_factorial_3_returns6(self):
        expected = 6
        result = eular20.factorial(3)
        self.assertEqual(expected, result)

    # Tests for add_digits(n):
    """
    def test_adddigits_1_returns1(self):
    def test_adddigits_1_2_returns2(self):
    def test_adddigits_1_2_3returns6(self):
    """
