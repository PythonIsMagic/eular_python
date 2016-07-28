import unittest
import recursion


class TestRecursion(unittest.TestCase):
    # Tests for multiply(alist, index, factors, product):

    def test_multiply_2factors_returns2(self):
        n = [1, 2, 3, 4, 5]
        expected = 2
        result = recursion.multiply(n, 0, 2)
        self.assertEqual(expected, result)

    def test_multiply_3factors_returns6(self):
        n = [1, 2, 3, 4, 5]
        expected = 6
        result = recursion.multiply(n, 0, 3)
        self.assertEqual(expected, result)

    def test_multiply_3factors_index1_returns24(self):
        n = [1, 2, 3, 4, 5]
        expected = 24
        result = recursion.multiply(n, 1, 3)
        self.assertEqual(expected, result)

    def test_multiply_indexoutofbounds_raiseException(self):
        n = [1, 2, 3, 4, 5]
        self.assertRaises(ValueError, recursion.multiply, n, 10, 3)

    def test_multiply_3factors_size3_returns24(self):
        n = [2, 3, 4]
        expected = 24
        result = recursion.multiply(n, 0, 3)
        self.assertEqual(expected, result)

    def test_multiply_13factors_size14_index0_returns157689344584365834240(self):
        n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
        expected = 157689344584365834240

        result = recursion.multiply(n, 0, 13)
        self.assertEqual(expected, result)

    def test_multiply_13factors_size14_index1_returns211895056785241589760(self):
        n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
        expected = 211895056785241589760

        result = recursion.multiply(n, 1, 13)
        self.assertEqual(expected, result)
