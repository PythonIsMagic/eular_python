import unittest
import eular21


class TestEular21(unittest.TestCase):
    # Tests for d(n)
    # Proper divisors of 1 = None. Sum = 0
    def test_d_1_returns0(self):
        expected = 0
        result = eular21.d(1)
        self.assertEqual(expected, result)

    # Proper divisors of 2 = 1. Sum = 1
    def test_d_2_returns1(self):
        expected = 1
        result = eular21.d(2)
        self.assertEqual(expected, result)

    # Proper divisors of 3 = 1. Sum = 1
    def test_d_3_returns1(self):
        expected = 1
        result = eular21.d(3)
        self.assertEqual(expected, result)

    # Proper divisors of 4 = 1, 2. Sum = 3
    def test_d_4_returns3(self):
        expected = 3
        result = eular21.d(4)
        self.assertEqual(expected, result)

    # Proper divisors of 6 = 1, 2, 3. Sum = 6
    def test_d_6_returns6(self):
        expected = 6
        result = eular21.d(6)
        self.assertEqual(expected, result)

    # Tests for amicable(a, b):
    def test_amicable_1_2_returnsFalse(self):
        expected = False
        result = eular21.is_amicable(1, 2)
        self.assertEqual(expected, result)

    def test_amicable_1_1_returnsFalse(self):
        expected = False
        result = eular21.is_amicable(1, 1)
        self.assertEqual(expected, result)

    def test_amicable_220_284_returnsTrue(self):
        expected = True
        result = eular21.is_amicable(220, 284)
        self.assertEqual(expected, result)
