import unittest
import factors


class TestFactors(unittest.TestCase):
    # Tests for divisors(target):
    # 0 has an infinite number of factors
    def test_divisors_0_raiseException(self):
        self.assertRaises(ValueError, factors.divisors, 0)

    # 1 has 1 factor: 1
    def test_divisors_1_returns1(self):
        expected = {1}
        result = factors.divisors(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisors_2_returns1_2(self):
        expected = {1, 2}
        result = factors.divisors(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisors_3_returns1_3(self):
        expected = {1, 3}
        result = factors.divisors(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisors_4_returns1_2_4(self):
        expected = {1, 2, 4}
        result = factors.divisors(4)
        self.assertEqual(expected, result)

    # Tests for divisors_dividing(n):
    # 0 has an infinite number of factors
    def test_divisorsdividing_0_raiseException(self):
        self.assertRaises(ValueError, factors.divisors_dividing, 0)

    # 1 has 1 factor: 1
    def test_divisorsdividing_1_returns1(self):
        expected = {1}
        result = factors.divisors_dividing(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisorsdividing_2_returns1_2(self):
        expected = {1, 2}
        result = factors.divisors_dividing(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisorsdividing_3_returns1_3(self):
        expected = {1, 3}
        result = factors.divisors_dividing(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisorsdividing_4_returns1_2_4(self):
        expected = {1, 2, 4}
        result = factors.divisors_dividing(4)
        self.assertEqual(expected, result)
