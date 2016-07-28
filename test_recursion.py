import unittest
import recursion


class TestFactors(unittest.TestCase):
    # Tests for multiply(alist, index, factors, product):

    def test_multiply_2factors_returns2(self):
        n = [1, 2, 3, 4, 5]
        expected = 2
        result = recursion.multiply(n, 0, 2, 1)
        self.assertEqual(expected, result)

    def test_multiply_3factors_returns6(self):
        n = [1, 2, 3, 4, 5]
        expected = 6
        result = recursion.multiply(n, 0, 3, 1)
        self.assertEqual(expected, result)

    def test_multiply_3factors_index1_returns24(self):
        n = [1, 2, 3, 4, 5]
        expected = 24
        result = recursion.multiply(n, 1, 3, 1)
        self.assertEqual(expected, result)

    def test_multiply_indexoutofbounds_raiseException(self):
        n = [1, 2, 3, 4, 5]
        self.assertRaises(ValueError, recursion.multiply, n, 10, 3, 1)

    def test_multiply_3factors_size3_returns24(self):
        n = [2, 3, 4]
        expected = 24
        result = recursion.multiply(n, 0, 3, 1)
        self.assertEqual(expected, result)
