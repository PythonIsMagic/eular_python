import unittest
import factors


class TestFactors(unittest.TestCase):
    # Tests for bruteforce(n):
    def test_bruteforce_0_raiseException(self):
        self.assertRaises(ValueError, factors.bruteforce, 0)

    # 1 has 1 factor: 1
    def test_bruteforce_1_returns1(self):
        expected = {1}
        result = factors.bruteforce(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_bruteforce_2_returns2factors(self):
        expected = {1, 2}
        result = factors.bruteforce(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_bruteforce_3_returns2factors(self):
        expected = {1, 3}
        result = factors.bruteforce(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_bruteforce_4_returns3factors(self):
        expected = {1, 2, 4}
        result = factors.bruteforce(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_bruteforce_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = factors.bruteforce(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_bruteforce_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = factors.bruteforce(24)
        self.assertEqual(expected, result)

    # 13195 has x factors:

    # Tests for divisors(n):
    def test_divisors_0_raiseException(self):
        self.assertRaises(ValueError, factors.divisors, 0)

    # 1 has 1 factor: 1
    def test_divisors_1_returns1(self):
        expected = {1}
        result = factors.divisors(1)
        self.assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisors_2_returns2factors(self):
        expected = {1, 2}
        result = factors.divisors(2)
        self.assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisors_3_returns2factors(self):
        expected = {1, 3}
        result = factors.divisors(3)
        self.assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisors_4_returns3factors(self):
        expected = {1, 2, 4}
        result = factors.divisors(4)
        self.assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_divisors_6_returns4factors(self):
        expected = {1, 2, 3, 6}
        result = factors.divisors(6)
        self.assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_divisors_24_returns8factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        result = factors.divisors(24)
        self.assertEqual(expected, result)

    # 13195 has x factors:


    # Tests for proper_divisors(n)
    def test_properdivisors_7_returns1(self):
        expected = {1}
        result = factors.proper_divisors(7)
        self.assertEqual(expected, result)

    def test_properdivisors_24_returns7factors(self):
        expected = {1, 2, 3, 4, 6, 8, 12}
        result = factors.proper_divisors(24)
        self.assertEqual(expected, result)
